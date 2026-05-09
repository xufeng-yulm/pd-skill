#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys


def build_base_cmd():
    cli = shutil.which("lark-cli")
    if cli:
        return [cli]
    if shutil.which("npx"):
        return ["npx", "-y", "@larksuite/cli@latest"]
    print("FAIL: 未找到 lark-cli，也未找到 npx。", file=sys.stderr)
    sys.exit(2)


def run_json(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr.strip() or result.stdout.strip(), file=sys.stderr)
        sys.exit(result.returncode)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(result.stdout, file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description="列出飞书知识库空间和可选父节点")
    parser.add_argument(
        "--space-id",
        help="指定知识库 space_id 后，继续读取该知识库下的节点",
    )
    parser.add_argument(
        "--parent-node-token",
        help="与 --space-id 搭配使用，读取指定父节点下的子节点",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=50,
        help="读取数量上限，默认 50",
    )
    args = parser.parse_args()

    base_cmd = build_base_cmd()
    spaces = run_json(base_cmd + ["wiki", "spaces", "list"])
    output = {
        "spaces": [
            {
                "name": item.get("name", ""),
                "space_id": item.get("space_id", ""),
                "space_type": item.get("space_type", ""),
                "visibility": item.get("visibility", ""),
                "description": item.get("description", ""),
            }
            for item in spaces.get("data", {}).get("items", [])
        ]
    }

    if args.space_id:
        params = {
            "space_id": args.space_id,
            "page_size": args.page_size,
        }
        if args.parent_node_token:
            params["parent_node_token"] = args.parent_node_token
        nodes = run_json(
            base_cmd
            + [
                "wiki",
                "nodes",
                "list",
                "--params",
                json.dumps(params, ensure_ascii=False),
            ]
        )
        output["selected_space_id"] = args.space_id
        output["selected_parent_node_token"] = args.parent_node_token or ""
        output["nodes"] = [
            {
                "title": item.get("title", ""),
                "node_token": item.get("node_token", ""),
                "parent_node_token": item.get("parent_node_token", ""),
                "obj_type": item.get("obj_type", ""),
                "has_child": item.get("has_child", False),
            }
            for item in nodes.get("data", {}).get("items", [])
        ]

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
