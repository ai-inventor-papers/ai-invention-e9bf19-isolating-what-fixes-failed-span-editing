"""Minimal async OpenRouter client (mirrors aii-openrouter-llms' /responses
payload shape) with a live cumulative-USD cost ledger enforced against a hard
cap. Used for all condition B / D / C1 repair calls.
"""

from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass, field
from pathlib import Path

import aiohttp
from dotenv import load_dotenv
from loguru import logger

load_dotenv(Path(__file__).resolve().parents[6] / ".env")  # repo root, best-effort
load_dotenv(Path(__file__).resolve().parent / ".env")

API_URL = "https://openrouter.ai/api/v1/responses"
MODELS_URL = "https://openrouter.ai/api/v1/models"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")


class BudgetExceededError(RuntimeError):
    pass


@dataclass
class CostLedger:
    cap_usd: float
    spent_usd: float = 0.0
    n_calls: int = 0
    n_input_tokens: int = 0
    n_output_tokens: int = 0
    calls_log: list[dict] = field(default_factory=list)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def add(self, cost_usd: float, input_tokens: int, output_tokens: int, meta: dict) -> None:
        async with self._lock:
            self.spent_usd += cost_usd or 0.0
            self.n_calls += 1
            self.n_input_tokens += input_tokens
            self.n_output_tokens += output_tokens
            self.calls_log.append(
                {"ts": time.time(), "cost_usd": cost_usd, "input_tokens": input_tokens,
                 "output_tokens": output_tokens, **meta}
            )
            if self.spent_usd >= self.cap_usd:
                logger.warning(f"Cost ledger at ${self.spent_usd:.4f} >= cap ${self.cap_usd:.2f}")

    def would_exceed(self, projected_extra_usd: float = 0.0) -> bool:
        return (self.spent_usd + projected_extra_usd) >= self.cap_usd

    def summary(self) -> dict:
        return {
            "spent_usd": round(self.spent_usd, 6),
            "cap_usd": self.cap_usd,
            "n_calls": self.n_calls,
            "n_input_tokens": self.n_input_tokens,
            "n_output_tokens": self.n_output_tokens,
        }


class OpenRouterClient:
    def __init__(self, ledger: CostLedger, *, max_concurrency: int = 8, timeout_s: float = 120.0):
        if not OPENROUTER_API_KEY:
            raise RuntimeError("OPENROUTER_API_KEY not set")
        self.ledger = ledger
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.timeout_s = timeout_s
        self._session: aiohttp.ClientSession | None = None
        self._pricing: dict[str, tuple[float, float]] = {}

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"},
            timeout=aiohttp.ClientTimeout(total=self.timeout_s),
        )
        await self._load_pricing()
        return self

    async def __aexit__(self, *exc):
        if self._session:
            await self._session.close()

    async def _load_pricing(self) -> None:
        try:
            async with self._session.get(MODELS_URL) as resp:
                data = await resp.json()
            for m in data.get("data", []):
                mid = m.get("id")
                pricing = m.get("pricing", {})
                try:
                    self._pricing[mid] = (float(pricing.get("prompt", 0)), float(pricing.get("completion", 0)))
                except (TypeError, ValueError):
                    continue
        except Exception as e:
            logger.warning(f"Could not fetch OpenRouter pricing catalog: {e}")

    def _cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        price = self._pricing.get(model)
        if not price:
            return 0.0
        return input_tokens * price[0] + output_tokens * price[1]

    async def call(
        self,
        model: str,
        prompt: str,
        *,
        temperature: float = 0.0,
        max_tokens: int = 1024,
        meta: dict | None = None,
        max_retries: int = 3,
    ) -> dict:
        """Returns dict: success, text, input_tokens, output_tokens, cost_usd, error."""
        meta = meta or {}
        if self.ledger.would_exceed():
            raise BudgetExceededError(
                f"Cost ledger at ${self.ledger.spent_usd:.4f} would exceed cap ${self.ledger.cap_usd:.2f}"
            )
        payload = {
            "model": model,
            "input": prompt,
            "max_output_tokens": max_tokens,
            "temperature": temperature,
        }
        async with self.semaphore:
            last_err = None
            for attempt in range(max_retries):
                try:
                    async with self._session.post(API_URL, json=payload) as resp:
                        body = await resp.json()
                        if resp.status != 200:
                            last_err = f"HTTP {resp.status}: {str(body)[:300]}"
                            if resp.status in (429, 500, 502, 503):
                                await asyncio.sleep(2 ** attempt)
                                continue
                            break
                        text = self._extract_text(body)
                        usage = body.get("usage", {})
                        in_tok = usage.get("input_tokens", 0)
                        out_tok = usage.get("output_tokens", 0)
                        cost = self._cost(model, in_tok, out_tok)
                        await self.ledger.add(cost, in_tok, out_tok, {"model": model, **meta})
                        return {
                            "success": True, "text": text, "input_tokens": in_tok,
                            "output_tokens": out_tok, "cost_usd": cost, "error": None,
                        }
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    last_err = str(e)
                    await asyncio.sleep(2 ** attempt)
            logger.error(f"LLM call failed after {max_retries} attempts: {last_err}")
            return {"success": False, "text": "", "input_tokens": 0, "output_tokens": 0,
                     "cost_usd": 0.0, "error": last_err}

    @staticmethod
    def _extract_text(body: dict) -> str:
        if body.get("output_text"):
            return body["output_text"]
        for item in body.get("output", []):
            if item.get("type") == "message" and "content" in item:
                content = item["content"]
                if isinstance(content, list) and content:
                    first = content[0]
                    if isinstance(first, dict) and "text" in first:
                        return first["text"]
                elif isinstance(content, str):
                    return content
        return ""
