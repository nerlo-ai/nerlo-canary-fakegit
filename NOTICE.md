# ⚠️ NERLO SECURITY CANARY — BENIGN TEST ARTIFACT

**This directory is NOT malware.** It is a deliberately-constructed, **inert**
red-team fixture that reproduces the *structure* of the FakeGit / SmartLoader
campaign so Nerlo can test its own detection pipeline end-to-end **without ever
handling a real payload**.

Every "payload" here decodes to a harmless marker (a `console.log` / an echo).
Nothing fetches, installs, persists, or exfiltrates anything. There are no live
IOCs — any URLs are neutered (`example-neutered.test`) and any "C2" is a
loopback placeholder.

**The brand is invented, deliberately.** This canary impersonates "Examplewear",
a fictional wearables company, on `.test` hosts (reserved by RFC 6761, never
resolvable). It names no real company and no real product. The detection value
of this artifact is the attack *shape* — clean tracked source plus a weaponized
README pointing at a release asset — which every layer exercises identically
whatever the brand is. Naming a real vendor would only publish, under Nerlo's
own org, an artifact our own registry rates Unsafe under that vendor's mark.

## What it models (and which detection layer each part exercises)

| File | FakeGit analogue | Should be flagged by |
|---|---|---|
| `README.md` | the weaponized install instructions | `nerlo-install-instruction` (**live**) |
| `examplewear_client.py` | the clean cloned source (a decoy) | nothing — must stay Verified (specificity) |
| `release/resource.js` | an obfuscated code payload in the release asset | `nerlo-behavioral` decode-then-exec (**live**, once the release asset is acquired + scanned) |
| `release/resource.txt` | the opaque LuaJIT dropper in the release asset | YARA/entropy malware layer (**roadmap**) — this is the target that will validate that scanner when it lands |
| `pyproject.toml` | not part of the attack shape — a root manifest so Nerlo's ingestion does not reject the repo `no_manifest` before any scan runs | nothing. It is inert packaging metadata, is never published to PyPI, and its `[project] name` is this repository's own name, never a product's |

Do not "fix" or delete these files: their whole value is being a stable, benign
reproduction of the attack shape.
