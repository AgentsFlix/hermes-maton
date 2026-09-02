#!/usr/bin/env python3
"""Read-only Maton account inventory. Never prints secrets or connection metadata."""
import json
import os
import sys
from collections import Counter
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://api.maton.ai"


def fetch(path: str) -> dict:
    key = os.environ.get("MATON_API_KEY")
    if not key:
        raise RuntimeError("MATON_API_KEY ausente no ambiente atual")
    request = Request(
        BASE_URL + path,
        headers={"Authorization": "Bearer " + key, "Accept": "application/json"},
    )
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    try:
        connections = fetch("/connections").get("connections", [])
        triggers = fetch("/triggers").get("triggers", [])
    except HTTPError as exc:
        print(json.dumps({"status": "http_error", "http_status": exc.code}, ensure_ascii=False))
        return 1
    except URLError:
        print(json.dumps({"status": "network_error"}, ensure_ascii=False))
        return 1
    except (RuntimeError, ValueError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 1

    connection_summary = [
        {"app": item.get("app"), "method": item.get("method"), "status": item.get("status")}
        for item in connections
    ]
    trigger_summary = [
        {"source": item.get("source"), "event_type": item.get("event_type"), "status": item.get("status")}
        for item in triggers
    ]
    result = {
        "status": "ok",
        "connections": connection_summary,
        "connection_count": len(connection_summary),
        "connections_by_status": dict(Counter(x["status"] for x in connection_summary)),
        "triggers": trigger_summary,
        "trigger_count": len(trigger_summary),
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
