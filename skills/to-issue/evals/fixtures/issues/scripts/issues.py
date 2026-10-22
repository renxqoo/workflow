import argparse
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser()
commands = parser.add_subparsers(dest="command", required=True)
commands.add_parser("list")
create = commands.add_parser("create")
create.add_argument("--title", required=True)
create.add_argument("--body-file", required=True, type=Path)
comment = commands.add_parser("comment")
comment.add_argument("--id", required=True, type=int)
comment.add_argument("--body-file", required=True, type=Path)
arguments = parser.parse_args()
state_file = root / "issue-state.json"
state = json.loads(state_file.read_text())
if arguments.command == "list":
    print(json.dumps(state, ensure_ascii=False, indent=2))
else:
    body = arguments.body_file.read_text()
    if arguments.command == "create":
        item = {"id": max((item["id"] for item in state), default=0) + 1,
                "state": "open", "title": arguments.title, "body": body}
        state.append(item)
    else:
        item = next((item for item in state if item["id"] == arguments.id), None)
        if item is None:
            raise SystemExit("Unknown issue")
        item.setdefault("comments", []).append(body)
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    with (root / "issue-actions.jsonl").open("a") as log:
        log.write(json.dumps({"action": arguments.command, "id": item["id"]}) + "\n")
    print(json.dumps({"id": item["id"], "url": f"issue-fixture://issues/{item['id']}"}))
