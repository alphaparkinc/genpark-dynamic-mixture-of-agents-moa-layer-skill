"""
MCP Server for Dynamic Mixture of Agents MoA Layer Skill.
"""

import json
import sys
from client import MixtureOfAgentsLayer

MOA = MixtureOfAgentsLayer(layer_index=1)


def handle_request(req: dict) -> dict:
    method = req.get("method")
    params = req.get("params", {})

    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "aggregate_proposals",
                    "description": "Synthesize candidate responses across multiple agents into unified aggregator prompt",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "original_query": {"type": "string"},
                            "proposals": {
                                "type": "array",
                                "items": {"type": "object"}
                            }
                        },
                        "required": ["original_query", "proposals"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "aggregate_proposals":
            res = MOA.aggregate_proposals(
                args["original_query"],
                args["proposals"]
            )
            return {"content": [{"type": "text", "text": json.dumps(res)}]}

        return {"error": f"Unknown tool: {tool_name}"}

    return {"error": f"Unknown method: {method}"}


def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            resp["id"] = req.get("id")
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"error": str(e)}) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
