#!/usr/bin/env python3
"""
把仓库当前工作树打包成 8 个 tar.gz：
    dist/all.tar.gz                          全站
    dist/<7 个分类>.tar.gz                    每分类一包

每个包内自带 MANIFEST.txt：包名、生成时间、git HEAD、包含哪些家。
输出（打给 stdout）：一份 JSON 数组，供后续 release stage 读，形如：
    [{"name": "all.tar.gz", "size": 123456, "sha256": "..."}]
"""
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
CATEGORIES = ["ai-models", "agent-frameworks", "voice-multimodal",
              "vector-db", "coding-agents", "dev-platforms", "libraries"]

VERSION = os.environ.get("RELEASE_VERSION") or time.strftime("%Y.%m.%d", time.gmtime())
HEAD = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def make_manifest(cat_name, paths_included):
    lines = [
        f"package: {cat_name}",
        f"version: {VERSION}",
        f"generated_at: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        f"git_head: {HEAD}",
        f"repo: cnb.cool/lib/ofiicial-developer-docs",
        f"mirror: github.com/Eyre921/ofiicial-developer-docs",
        f"total_sources: {sum(1 for p in paths_included if os.path.isdir(os.path.join(ROOT, p)) and '/' in p)}",
        "",
        "contents:",
    ]
    for p in sorted(paths_included):
        lines.append(f"  {p}")
    return "\n".join(lines) + "\n"


def pack(name, arcname_root, dirs_to_include):
    """打包 dirs_to_include（相对 ROOT）成 dist/<name>，包内根目录名 arcname_root。"""
    out = os.path.join(DIST, name)
    os.makedirs(DIST, exist_ok=True)
    manifest = make_manifest(name, dirs_to_include)
    with tarfile.open(out, "w:gz", compresslevel=6) as tf:
        # MANIFEST 放包内最顶
        import io
        mf_data = manifest.encode()
        info = tarfile.TarInfo(f"{arcname_root}/MANIFEST.txt")
        info.size = len(mf_data)
        info.mtime = int(time.time())
        tf.addfile(info, io.BytesIO(mf_data))
        for d in dirs_to_include:
            src = os.path.join(ROOT, d)
            if os.path.isdir(src):
                tf.add(src, arcname=f"{arcname_root}/{d}", recursive=True)
            elif os.path.isfile(src):
                tf.add(src, arcname=f"{arcname_root}/{d}")
    size = os.path.getsize(out)
    return {"name": name, "size": size, "sha256": sha256(out)}


def main():
    results = []
    root_arc = f"ofiicial-developer-docs-{VERSION}"

    # 全站包：所有分类 + 元数据文件
    all_dirs = CATEGORIES + ["README.md", "crawl.py", "crawl-metadata.json", "pyproject.toml"]
    results.append(pack("all.tar.gz", root_arc, all_dirs))

    # 每分类一包
    for cat in CATEGORIES:
        if os.path.isdir(os.path.join(ROOT, cat)):
            results.append(pack(f"{cat}.tar.gz", root_arc, [cat]))

    # 输出 JSON 到 stdout（release stage 读）
    print(json.dumps(results, ensure_ascii=False, indent=2))
    # 也写 dist/manifest.json 方便调试
    with open(os.path.join(DIST, "manifest.json"), "w") as f:
        json.dump({"version": VERSION, "head": HEAD, "assets": results}, f, ensure_ascii=False, indent=2)
    print(f"\n[done] version={VERSION} packed {len(results)} assets", file=sys.stderr)


if __name__ == "__main__":
    main()
