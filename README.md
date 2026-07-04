# plugin-mcp

Model Context Protocol (MCP) tool adapter for the Decision OS / AuthGate stack.

**Status: reference (real, working) — adapter only.**

## What it does

`mcp_call_to_action(actor, tool_name, arguments, annotations=...)` translates one
MCP tool invocation into a Decision OS `action` dict so the kernel can gate it. It
carries MCP tool annotations (e.g. `data_labels`, `call_id`) into the action for
policy to use.

## Authority

This plugin holds **no authority**. It only reshapes an MCP call into the kernel's
action format; the kernel then decides. It performs no authentication and no
authorization of its own.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_mcp import mcp_call_to_action
action = mcp_call_to_action(
    "agent:bot", "send_email", {"to": "x"},
    annotations={"call_id": "c1", "data_labels": ["pii"]},
)
# action["capability"] == "tool:send_email"
```

## Status and limitations

- This is a pure mapping function — it does not host an MCP server or transport.
- The caller is responsible for supplying a verified `actor` and correct
  annotations; the adapter does not validate them.
