"""Clean cloned-looking source (the decoy half of the FakeGit shape).

BENIGN CANARY (see NOTICE.md). This file is deliberately ordinary and safe — it
must produce ZERO findings. Its job is to prove specificity: the malice in a
FakeGit repo is never in the tracked source, so a scanner that flags this decoy
would be crying wolf. Modeled on the legitimate Oura MCP server it clones.
"""

from __future__ import annotations

import os

OURA_API_BASE = "https://api.ouraring.com/v2"


def get_token() -> str | None:
    """Read the Oura API token from the environment (never hardcoded)."""
    return os.environ.get("OURA_API_TOKEN")


def daily_readiness(token: str) -> dict[str, str]:
    """Return a stub readiness payload. No network, no side effects."""
    return {"endpoint": f"{OURA_API_BASE}/usercollection/daily_readiness", "auth": "bearer"}
