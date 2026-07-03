"""MCP (Model Context Protocol) tool adapter.

INTERFACE ONLY. Maps an MCP tool invocation into a Decision OS `action` dict so the
kernel can gate it. Also carries MCP tool annotations (readOnly/destructive) into
the action for policy to use.
"""

from __future__ import annotations

from typing import Any


def mcp_call_to_action(actor: str, tool_name: str, arguments: dict[str, Any],
                       *, annotations: dict[str, Any] | None = None) -> dict[str, Any]:
    """Translate one MCP tool call into a kernel action dict."""
    ann = annotations or {}
    return {
        "actor": actor,
        "tool": tool_name,
        "capability": f"tool:{tool_name}",
        "action_purpose": ann.get("purpose", ""),
        "data_labels": list(ann.get("data_labels", [])),
        "payload": dict(arguments),
        "nonce": ann.get("call_id", ""),
    }
