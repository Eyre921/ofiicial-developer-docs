#!/usr/bin/env python3
"""在 CNB runner 上跑：把 dist/*.tar.gz 发到 github.com/Eyre921/ofiicial-developer-docs/releases。

设计成 exit 0（软失败）—— GitHub 侧任何异常都不阻断整条流水线。
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

REPO = "Eyre921/ofiicial-developer-docs"
API = f"https://api.github.com/repos/{REPO}"
UPLOAD = f"https://uploads.github.com/repos/{REPO}"


def api(method, url, body=None, ctype="application/json", is_binary=False):
    headers = {
        "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "cnb-ofiicial-developer-docs-release/1.0",
    }
    if body is not None:
        headers["Content-Type"] = ctype
    data = body if is_binary else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(url, method=method, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def main():
    tok = os.environ.get("GH_TOKEN", "")
    if not tok:
        print("跳过：GH_TOKEN 未注入")
        return 0

    with open(".release_version") as f:
        version = f.read().strip()
    tag = f"v{version}"
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # 幂等：如同名 release 已存在，先删
    code, raw = api("GET", f"{API}/releases/tags/{tag}")
    if code == 200:
        rid = json.loads(raw).get("id")
        if rid:
            print(f"删除同名旧 release id={rid}")
            api("DELETE", f"{API}/releases/{rid}")

    # 建 release
    body = {
        "tag_name": tag,
        "name": tag,
        "body": f"每周文档快照 · 生成时间 {now}\n\n8 个 asset：all.tar.gz 全站 + 7 个分类包 + manifest.json",
    }
    code, raw = api("POST", f"{API}/releases", body=body)
    if code >= 300:
        print(f"⚠️ 建 release 失败 HTTP {code}:")
        print(raw.decode(errors="replace")[:400])
        return 0
    release_id = json.loads(raw).get("id")
    print(f"✓ 建 release id={release_id}")

    # 上传 8 个 asset + manifest.json
    files = sorted([f for f in os.listdir("dist") if f.endswith(".tar.gz")]) + ["manifest.json"]
    for name in files:
        path = os.path.join("dist", name)
        with open(path, "rb") as f:
            data = f.read()
        code, _ = api(
            "POST",
            f"{UPLOAD}/releases/{release_id}/assets?name={name}",
            body=data,
            ctype="application/octet-stream",
            is_binary=True,
        )
        print(f"  uploaded {name} ({len(data)} bytes) HTTP {code}")

    print(f"✓ GitHub release {tag} 完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
