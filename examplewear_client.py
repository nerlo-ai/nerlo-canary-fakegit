"""Clean cloned-looking source (the decoy half of the FakeGit shape).

BENIGN CANARY (see NOTICE.md). This file is deliberately ordinary and safe — it
must produce ZERO findings. Its job is to prove specificity: the malice in a
FakeGit repo is never in the tracked source, so a scanner that flags this decoy
would be crying wolf.

"Examplewear" is an invented wearables brand and `.test` is reserved by RFC 6761
— the canary deliberately names no real company or product. The detection layers
key on the attack SHAPE (clean tracked source + a weaponized README pointing at a
release asset), never on the brand, so the fictional name exercises every layer
identically. See NOTICE.md.
"""

from __future__ import annotations

import os

EXAMPLEWEAR_API_BASE = "https://api.examplewear.test/v2"


def get_token() -> str | None:
    """Read the Examplewear API token from the environment (never hardcoded)."""
    return os.environ.get("EXAMPLEWEAR_API_TOKEN")


def daily_readiness(token: str) -> dict[str, str]:
    """Return a stub readiness payload. No network, no side effects."""
    return {
        "endpoint": f"{EXAMPLEWEAR_API_BASE}/usercollection/daily_readiness",
        "auth": "bearer",
    }
