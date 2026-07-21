# ⚠️ NERLO SECURITY CANARY — BENIGN TEST ARTIFACT

**This directory is NOT malware.** It is a deliberately-constructed, **inert**
red-team fixture that reproduces the *structure* of the FakeGit / SmartLoader
campaign (see `docs/fakegit-smartloader-assessment.md`) so Nerlo can test its
own detection pipeline end-to-end **without ever handling a real payload**.

Every "payload" here decodes to a harmless marker (a `console.log` / an echo).
Nothing fetches, installs, persists, or exfiltrates anything. There are no live
IOCs — any URLs are neutered (`example-neutered.test`) and any "C2" is a
loopback placeholder.

## What it models (and which detection layer each part exercises)

| File | FakeGit analogue | Should be flagged by |
|---|---|---|
| `README.md` | the weaponized install instructions | `nerlo-install-instruction` (**live**) |
| `oura_client.py` | the clean cloned source (a decoy) | nothing — must stay Verified (specificity) |
| `release/resource.js` | an obfuscated code payload in the release asset | `nerlo-behavioral` decode-then-exec (**live**, once the release asset is acquired + scanned) |
| `release/resource.txt` | the opaque LuaJIT dropper in the release asset | YARA/entropy malware layer (**roadmap**) — this is the target that will validate that scanner when it lands |

See `EXPECTED.md` for the exact findings each part must produce — that is the
oracle the end-to-end integration test asserts against.

Do not "fix" or delete these files: their whole value is being a stable,
benign reproduction of the attack shape.
