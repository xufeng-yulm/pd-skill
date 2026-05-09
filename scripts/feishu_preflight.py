#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys


DEFAULT_SCOPES = [
    "docx:document:create",
    "docx:document:write_only",
    "space:folder:create",
]

WIKI_READ_SCOPES = [
    "wiki:wiki:readonly",
    "wiki:space:retrieve",
    "wiki:node:retrieve",
]

WIKI_WRITE_SCOPES = [
    "wiki:node:create",
]

LOGIN_CMD = (
    'lark-cli auth login --scope '
    '"docx:document:create docx:document:write_only space:folder:create"'
)


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": cmd,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main():
    parser = argparse.ArgumentParser(description="飞书 CLI 发布前检查")
    parser.add_argument(
        "--scope",
        action="append",
        default=[],
        help="额外检查的 scope，可重复传入",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="对 auth status 增加 --verify，校验服务端 token 状态",
    )
    parser.add_argument(
        "--wiki",
        action="store_true",
        help="额外检查知识库发布所需的只读与创建 scopes",
    )
    args = parser.parse_args()

    scopes = DEFAULT_SCOPES + args.scope
    if args.wiki:
        scopes += WIKI_READ_SCOPES + WIKI_WRITE_SCOPES
    cli = shutil.which("lark-cli")
    used_npx = False

    if cli:
        base_cmd = [cli]
    else:
        if shutil.which("npx") is None:
            print("FAIL: 未找到 lark-cli，也未找到 npx，无法执行飞书 CLI 检查。")
            sys.exit(2)
        base_cmd = ["npx", "-y", "@larksuite/cli@latest"]
        used_npx = True

    status_cmd = base_cmd + ["auth", "status"]
    if args.verify:
        status_cmd.append("--verify")

    status = run(status_cmd)
    check = run(base_cmd + ["auth", "check", "--scope", " ".join(scopes)])

    payload = {
        "ok": status["returncode"] == 0 and check["returncode"] == 0,
        "used_npx": used_npx,
        "scopes_checked": scopes,
        "auth_status": status,
        "scope_check": check,
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if payload["ok"]:
        print("\nPASS: 飞书 CLI 已就绪，可以继续发布。")
        return

    print("\nBLOCKED: 飞书 CLI 尚未就绪。")
    print("下一步建议：")
    print(f"1. 运行 `{LOGIN_CMD}` 完成授权")
    print("2. 运行 `lark-cli auth status --verify` 确认登录有效")
    print("3. 补齐所需 scopes 后重新运行本脚本")
    sys.exit(1)


if __name__ == "__main__":
    main()
