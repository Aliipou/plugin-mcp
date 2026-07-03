from dos_plugin_mcp import mcp_call_to_action


def test_mcp_call_maps_to_action():
    a = mcp_call_to_action("agent:bot", "send_email", {"to": "x"},
                           annotations={"call_id": "c1", "data_labels": ["pii"]})
    assert a["capability"] == "tool:send_email"
    assert a["payload"] == {"to": "x"} and a["nonce"] == "c1"
    assert a["data_labels"] == ["pii"]
