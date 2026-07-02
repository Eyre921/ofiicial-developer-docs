#!/usr/bin/env python3
"""
AI 官方文档镜像爬虫 —— Anthropic / OpenAI / Google Gemini。

零第三方依赖（纯 stdlib），设计为在 CNB 定时流水线里运行、抓完把结果写进仓库、
只在内容真正变化时才产生 git diff（省资源、避免无意义的每日提交）。

产物结构（每个来源一致）：
    <provider>/
        llms-full.txt        各家的「Full.txt」（官方原文；Gemini 无官方全量，本脚本拼接生成）
        index.md             导航索引（按分类分组）
        pages/<category>/<slug>.md   拆分后的单篇文档（带 frontmatter，结构清晰）

用法：
    python crawl.py                      # 抓全部来源
    python crawl.py anthropic-api        # 只抓某个来源
    INCLUDE_ALL_SDK_LANGUAGES=1 python crawl.py   # Anthropic API 保留全部 8 种语言 SDK 参考（默认只留 Python，省体积）
"""
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
UA_STR = "ai-official-docs-mirror/1.0 (+https://cnb.cool/vibeapi/ai-ofiicial-docs)"
INCLUDE_ALL_SDK_LANGUAGES = os.environ.get("INCLUDE_ALL_SDK_LANGUAGES") == "1"

# Anthropic Platform API 文档 87MB 里 92% 是 python/typescript/go/java/php/ruby/csharp/cli
# 八种语言各一份的同一套 API 参考。默认只保留概念指南 + Python 参考，体积从 ~87MB 砍到
# 可维护的量级；想要全量把 INCLUDE_ALL_SDK_LANGUAGES=1 打开即可。
ANTHROPIC_API_KEEP_PREFIXES = (
    "/docs/en/agents-and-tools/", "/docs/en/build-with-claude/",
    "/docs/en/manage-claude/", "/docs/en/managed-agents/",
    "/docs/en/test-and-evaluate/", "/docs/en/intro", "/docs/en/get-started",
    "/docs/en/api/python/", "/docs/en/api/messages/",
    "/docs/en/api/models/", "/docs/en/api/completions/",
)


def fetch(url, timeout=90):
    """用 curl 下载：实测这个网络环境里 urllib 对大文件（llms-full.txt 数 MB~数十 MB）
    会 IncompleteRead 截断，curl 稳定完整。curl 缺失时回退 urllib（小页面够用）。

    超时收紧：--connect-timeout 15 让死站点快速失败，--max-time + --retry 2 让单个坏源
    最坏 ~3 分钟就放弃（而不是拖垮整个定时任务）。单源失败不影响其它源（main 里 try 掉）。"""
    try:
        out = subprocess.run(
            ["curl", "-sSL", "--fail", "--connect-timeout", "15", "--retry", "2",
             "--retry-delay", "2", "--max-time", str(timeout), "-A", UA_STR, url],
            capture_output=True, check=True,
        )
        return out.stdout.decode("utf-8", errors="replace")
    except FileNotFoundError:
        req = urllib.request.Request(url, headers={"User-Agent": UA_STR})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"curl failed ({e.returncode}) for {url}: {e.stderr.decode()[:200]}") from e


# 每个来源的「文档路径根」——从官方 URL 里剥掉它，剩下的路径逐段映射成本地目录，
# 一直拆到最深的叶子（用户要求：按官方路径，分到不能再分）。
DOC_ROOTS = {
    "ai-models/anthropic-claude-code": "https://code.claude.com/docs/en/",
    "ai-models/anthropic-api": "https://platform.claude.com/docs/en/",
    "ai-models/openai": "https://developers.openai.com/api/docs/",
    "ai-models/google-gemini": "https://ai.google.dev/gemini-api/docs/",
}


def rel_segments(provider_dir, url):
    """把官方 URL 转成本地路径段列表（去掉文档根、去扩展名、逐段清洗）。"""
    root = DOC_ROOTS.get(provider_dir)
    if root and url.startswith(root):
        rest = url[len(root):]
    else:  # 兜底：去掉 scheme + 域名
        rest = re.sub(r"^https?://[^/]+/", "", url)
    rest = re.sub(r"\.(md|html)$", "", rest.strip("/"))
    if not rest:
        return ["index"]
    return [re.sub(r"[^a-zA-Z0-9._-]", "-", s).strip("-").lower() or "x" for s in rest.split("/")]


# ---------------------------------------------------------------------------
# 各来源解析器 —— 返回统一的 page dict 列表：{title, url, category, body}
# ---------------------------------------------------------------------------

def parse_claude_code(full_text):
    """code.claude.com/docs/llms-full.txt : '# Title\\nSource: url' 分页。"""
    pat = re.compile(r"^# (.+)\nSource: (\S+)\n", re.MULTILINE)
    matches = list(pat.finditer(full_text))
    pages = []
    for i, m in enumerate(matches):
        title, url = m.group(1).strip(), m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        pages.append({"title": title, "url": url, "category": _cc_category(url),
                      "body": full_text[start:end].strip()})
    return pages


def _cc_category(url):
    tail = url.split("/docs/en/", 1)[-1] if "/docs/en/" in url else ""
    seg = tail.split("/")
    return seg[0] if len(seg) > 1 else "guides"


def parse_anthropic_api(full_text):
    """platform.claude.com/llms-full.txt : 用 '**URL:**' 锚点，两种模板（标题在 URL 前/后）。"""
    url_line = re.compile(r"^\*\*URL:\*\* (\S+)\s*$", re.MULTILINE)
    matches = list(url_line.finditer(full_text))
    pages = []
    for i, m in enumerate(matches):
        url = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        body = re.sub(r"^\s*---\s*\n", "", full_text[body_start:body_end]).strip()

        window = full_text[max(0, m.start() - 300):m.start()]
        before = re.search(r"^#{1,2} (.+)\n+$", window, re.MULTILINE)
        if before:
            title = before.group(1).strip()
        else:
            after = re.match(r"^#{1,3} (.+)$", body, re.MULTILINE)
            title = after.group(1).strip() if after else url.rstrip("/").rsplit("/", 1)[-1]

        path = url.replace("https://platform.claude.com", "")
        if not INCLUDE_ALL_SDK_LANGUAGES and not any(path.startswith(p) for p in ANTHROPIC_API_KEEP_PREFIXES):
            continue
        cat = path.split("/docs/en/", 1)[-1].split("/")[0] if "/docs/en/" in path else "api"
        pages.append({"title": title, "url": url, "category": cat or "api", "body": body})
    return pages


def parse_openai(full_text, index_text):
    """developers.openai.com : llms-full.txt 只有 '# Title'，靠 index 把标题映射到 URL + 分类。"""
    title_to_url, title_to_section = {}, {}
    current_section = "general"
    for line in index_text.splitlines():
        sec = re.match(r"^## (.+)$", line.strip())
        if sec:
            current_section = sec.group(1).strip().lower().replace(" ", "-")
            continue
        m = re.match(r"^- \[(.+?)\]\((\S+?)\.md\)", line.strip())
        if m:
            title_to_url[m.group(1).strip()] = m.group(2).strip()
            title_to_section[m.group(1).strip()] = current_section

    matches = list(re.finditer(r"^# (.+)$", full_text, re.MULTILINE))[1:]  # [0] = file title
    pages, current = [], None
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        seg = full_text[start:end].strip()
        url = title_to_url.get(title)
        if url is not None or current is None:
            if current is not None:
                pages.append(current)
            current = {"title": title, "url": url or "https://developers.openai.com/api/docs/",
                       "category": title_to_section.get(title, "general"), "body": seg}
        else:  # tutorial step heading, not a real page -> fold into current page
            current["body"] += f"\n\n# {title}\n\n{seg}"
    if current is not None:
        pages.append(current)
    return pages


def fetch_gemini():
    """ai.google.dev : 无官方 llms-full.txt，按 index 逐页抓 .md.txt 并发下载。"""
    index_text = fetch("https://ai.google.dev/gemini-api/docs/llms.txt")
    title_to_url = {}
    for line in index_text.splitlines():
        m = re.match(r"^- \[(.+?)\]\((\S+)\):", line.strip())
        if m:
            title_to_url[m.group(1).strip()] = m.group(2).strip()

    def _one(item):
        title, url = item
        return title, url, fetch(url, timeout=30)

    pages = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(_one, it) for it in title_to_url.items()]):
            try:
                title, url, body = fut.result()
                page_url = url[:-4] if url.endswith(".md.txt") else url  # 去掉 .txt 还原可读地址
                pages.append({"title": title, "url": page_url, "category": "docs", "body": body.strip()})
            except Exception as e:  # noqa: BLE001
                print(f"    [warn] gemini page failed: {e}", file=sys.stderr)
    return pages


# ---------------------------------------------------------------------------
# 写盘
# ---------------------------------------------------------------------------

FOLLOW_CAP = int(os.environ.get("FOLLOW_CAP", "100000"))  # 基本不限（CNB 核时充足）；需要时用环境变量压低


def fetch_index_links(index_url):
    """索引型 llms.txt：解析里面的 markdown 链接，把每篇 .md 抓下来拼成全文。
    带页数上限（防 GitHub 这类超大站爆掉，截断会打日志，不静默）；
    链接指向 HTML 页时自动尝试 url+'.md'，仍是 HTML 则跳过。"""
    idx = fetch(index_url)
    host = re.sub(r"^https?://([^/]+)/.*", r"\1", index_url)
    seen, items = set(), []
    for title, url in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", idx):
        u = url.split("#")[0]
        # 只跟同域名的文档链接，去重，跳过明显的资源/外链
        if re.sub(r"^https?://([^/]+)/.*", r"\1", u) != host or u in seen:
            continue
        if re.search(r"\.(png|jpg|jpeg|svg|gif|zip|pdf)$", u, re.I):
            continue
        seen.add(u)
        items.append((title.strip(), u))
    if len(items) > FOLLOW_CAP:
        print(f"    [note] {index_url}: {len(items)} 链接，超上限截断到 {FOLLOW_CAP}（设 FOLLOW_CAP 调大）", flush=True)
        items = items[:FOLLOW_CAP]

    def one(it):
        title, u = it
        body = fetch(u, timeout=30)
        if body.lstrip()[:1] == "<" and not u.endswith(".md"):  # HTML → 试 .md 版
            try:
                body = fetch(u + ".md", timeout=30)
                u = u + ".md"
            except Exception:  # noqa: BLE001
                pass
        return {"title": title, "url": u, "body": body}

    pages = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(one, it) for it in items]):
            try:
                p = fut.result()
                if p["body"].lstrip()[:1] != "<":  # 跳过仍是 HTML 的
                    pages.append(p)
            except Exception:  # noqa: BLE001
                pass
    return pages


def write_if_changed(path, content):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if f.read() == content:
                return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def write_provider(provider_dir, pages, official_full_text):
    base = os.path.join(ROOT, provider_dir)
    # 先清掉旧的 pages（避免上游删页后本地残留），再重写
    pages_dir = os.path.join(base, "pages")
    if os.path.isdir(pages_dir):
        for dirpath, _, files in os.walk(pages_dir, topdown=False):
            for fn in files:
                os.remove(os.path.join(dirpath, fn))
            if not os.listdir(dirpath):
                os.rmdir(dirpath)

    used_paths, tree = set(), {}
    for p in sorted(pages, key=lambda x: x["url"]):
        segs = rel_segments(provider_dir, p["url"])
        rel = os.path.join("pages", *segs) + ".md"
        n = 2  # 极少数 URL 去扩展名后撞车时兜底
        while rel in used_paths:
            rel = os.path.join("pages", *segs) + f"-{n}.md"
            n += 1
        used_paths.add(rel)
        fm = (f"---\ntitle: {json.dumps(p['title'], ensure_ascii=False)}\n"
              f"source: {p['url']}\npath: {'/'.join(segs)}\n---\n\n")
        write_if_changed(os.path.join(base, rel), fm + p["body"] + "\n")
        top = segs[0] if len(segs) > 1 else "(根目录)"
        tree.setdefault(top, []).append((p["title"], rel, p["url"], "/".join(segs)))

    # llms-full.txt：官方原文优先；无官方（Gemini）则拼接
    if official_full_text is not None:
        full = official_full_text
    else:
        full = "\n\n".join(f"# {p['title']}\n\n**URL:** {p['url']}\n\n{p['body']}" for p in pages)
    write_if_changed(os.path.join(base, "llms-full.txt"), full)

    # index.md 导航（按官方路径的顶层段分组，条目按完整路径排序 —— 目录树本身就是最细的导航）
    lines = [f"# {provider_dir} 文档索引\n",
             f"> 共 {len(pages)} 篇，目录严格镜像官方 URL 路径。完整合并版见 [`llms-full.txt`](./llms-full.txt)。\n"]
    for top in sorted(tree):
        lines.append(f"\n## {top}\n")
        for title, rel, url, path in sorted(tree[top], key=lambda x: x[3]):
            lines.append(f"- `{path}` — [{title}]({rel}) · [原文]({url})")
    write_if_changed(os.path.join(base, "index.md"), "\n".join(lines) + "\n")
    return len(pages)


# ---------------------------------------------------------------------------
# 通用 llms 文件拆分：多数官方 llms-full.txt 都是「# 标题 / Source: url」或「**URL:** url」分页
# ---------------------------------------------------------------------------

def split_generic(raw):
    pat = re.compile(r"^# (.+)\nSource: (\S+)\s*$", re.MULTILINE)
    m = list(pat.finditer(raw))
    if len(m) >= 3:
        pages = []
        for i, mm in enumerate(m):
            s, e = mm.end(), (m[i + 1].start() if i + 1 < len(m) else len(raw))
            pages.append({"title": mm.group(1).strip(), "url": mm.group(2).strip(), "body": raw[s:e].strip()})
        return pages
    pat2 = re.compile(r"^\*\*URL:\*\* (\S+)\s*$", re.MULTILINE)
    m2 = list(pat2.finditer(raw))
    if len(m2) >= 3:
        pages = []
        for i, mm in enumerate(m2):
            s, e = mm.end(), (m2[i + 1].start() if i + 1 < len(m2) else len(raw))
            body = re.sub(r"^\s*---\s*\n", "", raw[s:e]).strip()
            title = (re.match(r"^#{1,3} (.+)$", body, re.MULTILINE) or [None, mm.group(1)])
            title = title.group(1).strip() if hasattr(title, "group") else mm.group(1).rsplit("/", 1)[-1]
            pages.append({"title": title, "url": mm.group(1).strip(), "body": body})
        return pages
    return []


def write_generic(provider_dir, raw, is_full):
    pages = split_generic(raw)
    if pages:  # 能拆 → 复用 write_provider 的深度拆分（pages 镜像官方路径）+ llms-full.txt 原文
        return write_provider(provider_dir, pages, official_full_text=raw)
    # 拆不动（纯索引 llms.txt 或非常规格式如 Cloudflare 的 frontmatter 块）→ 原文存盘
    fname = "llms-full.txt" if is_full else "llms.txt"
    write_if_changed(os.path.join(ROOT, provider_dir, fname), raw)
    return 0


# ---------------------------------------------------------------------------
# 来源注册表：dir = 分类/slug；bespoke=原 4 家深度拆分，generic=通用
# ---------------------------------------------------------------------------
SOURCES = [
    {"dir": "ai-models/anthropic-claude-code", "kind": "cc"},
    {"dir": "ai-models/anthropic-api", "kind": "anthropic_api"},
    {"dir": "ai-models/openai", "kind": "openai"},
    {"dir": "ai-models/google-gemini", "kind": "gemini"},
]
# (dir, url, mode)
#   full     : url 是真正的 llms-full.txt（全文）→ 拆分 + 存原文
#   verbatim : url 内容已很丰富但无独立 full（如 xAI）→ 原样存盘
#   follow   : url 只是索引 → 顺着里面的链接把每篇抓下来拼成全文（带页数上限）
_GENERIC = [
    ("ai-models/xai-grok", "https://docs.x.ai/llms.txt", "verbatim"),
    ("ai-models/perplexity", "https://docs.perplexity.ai/llms-full.txt", "full"),
    ("ai-models/mistral", "https://docs.mistral.ai/llms-full.txt", "full"),
    ("ai-models/cohere", "https://docs.cohere.com/llms.txt", "follow"),
    ("ai-models/groq", "https://console.groq.com/llms-full.txt", "full"),
    ("ai-models/together", "https://docs.together.ai/llms-full.txt", "full"),
    ("ai-models/fireworks", "https://docs.fireworks.ai/llms-full.txt", "full"),
    ("ai-models/openrouter", "https://openrouter.ai/docs/llms.txt", "follow"),
    ("ai-models/replicate", "https://replicate.com/docs/llms.txt", "follow"),
    ("agent-frameworks/mcp", "https://modelcontextprotocol.io/llms-full.txt", "full"),
    ("agent-frameworks/langchain", "https://docs.langchain.com/llms-full.txt", "full"),
    ("agent-frameworks/vercel-ai-sdk", "https://ai-sdk.dev/llms-full.txt", "full"),
    ("agent-frameworks/crewai", "https://docs.crewai.com/llms-full.txt", "full"),
    ("voice-multimodal/elevenlabs", "https://elevenlabs.io/docs/llms.txt", "follow"),
    ("voice-multimodal/deepgram", "https://developers.deepgram.com/llms.txt", "follow"),
    ("voice-multimodal/assemblyai", "https://www.assemblyai.com/docs/llms-full.txt", "full"),
    ("voice-multimodal/vapi", "https://docs.vapi.ai/llms-full.txt", "full"),
    ("vector-db/pinecone", "https://docs.pinecone.io/llms-full.txt", "full"),
    ("vector-db/qdrant", "https://qdrant.tech/llms-full.txt", "full"),
    ("vector-db/weaviate", "https://weaviate.io/llms.txt", "follow"),
    ("vector-db/chroma", "https://docs.trychroma.com/llms-full.txt", "full"),
    ("coding-agents/windsurf", "https://docs.windsurf.com/llms-full.txt", "full"),
    ("dev-platforms/cloudflare", "https://developers.cloudflare.com/llms-full.txt", "full"),
    ("dev-platforms/vercel", "https://vercel.com/docs/llms-full.txt", "full"),
    ("dev-platforms/supabase", "https://supabase.com/llms-full.txt", "full"),
    ("dev-platforms/stripe", "https://docs.stripe.com/llms.txt", "follow"),
    ("dev-platforms/prisma", "https://www.prisma.io/docs/llms-full.txt", "full"),
    ("dev-platforms/drizzle", "https://orm.drizzle.team/llms-full.txt", "full"),
    ("dev-platforms/clerk", "https://clerk.com/docs/llms-full.txt", "full"),
    ("dev-platforms/resend", "https://resend.com/docs/llms-full.txt", "full"),
    ("dev-platforms/sentry", "https://docs.sentry.io/llms.txt", "follow"),
    ("dev-platforms/convex", "https://docs.convex.dev/llms-full.txt", "full"),
    ("dev-platforms/neon", "https://neon.com/llms-full.txt", "full"),
    ("dev-platforms/turso", "https://docs.turso.tech/llms-full.txt", "full"),
    ("dev-platforms/upstash", "https://upstash.com/docs/llms-full.txt", "full"),
    ("dev-platforms/netlify", "https://docs.netlify.com/llms.txt", "follow"),
    ("dev-platforms/expo", "https://docs.expo.dev/llms-full.txt", "full"),
    ("dev-platforms/langfuse", "https://langfuse.com/llms.txt", "follow"),
    ("dev-platforms/github", "https://docs.github.com/llms.txt", "follow"),
    ("dev-platforms/x-developer", "https://docs.x.com/llms-full.txt", "full"),
    ("dev-platforms/n8n", "https://docs.n8n.io/llms-full.txt", "full"),
    ("dev-platforms/trigger-dev", "https://trigger.dev/docs/llms-full.txt", "full"),
    ("dev-platforms/shopify", "https://shopify.dev/llms.txt", "follow"),
    ("dev-platforms/notion", "https://developers.notion.com/llms-full.txt", "full"),
    ("dev-platforms/twilio", "https://www.twilio.com/docs/llms.txt", "follow"),
    ("libraries/hono", "https://hono.dev/llms-full.txt", "full"),
    ("libraries/svelte", "https://svelte.dev/llms-full.txt", "full"),
    ("libraries/bun", "https://bun.sh/llms-full.txt", "full"),
    ("libraries/tanstack", "https://tanstack.com/llms-full.txt", "full"),
    ("libraries/zod", "https://zod.dev/llms-full.txt", "full"),
]
for _d, _u, _m in _GENERIC:
    SOURCES.append({"dir": _d, "kind": "generic", "url": _u, "mode": _m})


def run_source(src):
    d, kind = src["dir"], src["kind"]
    print(f"[*] {d} ({kind}) ...")
    if kind == "cc":
        raw = fetch("https://code.claude.com/docs/llms-full.txt")
        n = write_provider(d, parse_claude_code(raw), official_full_text=raw)
    elif kind == "anthropic_api":
        raw = fetch("https://platform.claude.com/llms-full.txt")
        full = raw if INCLUDE_ALL_SDK_LANGUAGES else None
        n = write_provider(d, parse_anthropic_api(raw), official_full_text=full)
    elif kind == "openai":
        full = fetch("https://developers.openai.com/api/docs/llms-full.txt")
        idx = fetch("https://developers.openai.com/api/docs/llms.txt")
        n = write_provider(d, parse_openai(full, idx), official_full_text=full)
    elif kind == "gemini":
        n = write_provider(d, fetch_gemini(), official_full_text=None)
    elif kind == "generic":
        mode = src.get("mode", "full")
        if mode == "follow":  # 索引型 → 顺链接抓每篇拼全文
            n = write_provider(d, fetch_index_links(src["url"]), official_full_text=None)
        elif mode == "verbatim":  # 内容已丰富但无独立 full → 原样存盘
            n = write_generic(d, fetch(src["url"]), is_full=False)
        else:  # full：真正的 llms-full.txt
            n = write_generic(d, fetch(src["url"]), is_full=True)
    else:
        raise ValueError(f"unknown kind: {kind}")
    print(f"    -> {n} pages")
    return n


def select(targets):
    if not targets or targets == ["all"] or targets == [""]:
        return SOURCES
    out = []
    for t in targets:
        for s in SOURCES:
            if s["dir"] == t or s["dir"].startswith(t.rstrip("/") + "/") or s["dir"].endswith("/" + t):
                out.append(s)
    # 去重保序
    seen, uniq = set(), []
    for s in out:
        if s["dir"] not in seen:
            seen.add(s["dir"])
            uniq.append(s)
    return uniq


def main():
    targets = select(sys.argv[1:])
    meta_path = os.path.join(ROOT, "crawl-metadata.json")
    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)

    # 源级并行、非阻塞：多个源并发抓，单个源失败/卡住（curl 已 --max-time 兜底）只影响它自己，
    # 不阻塞其余。各源只写自己目录，无写冲突；crawl-metadata.json 由主线程最后统一写。
    workers = int(os.environ.get("CRAWL_WORKERS", "8"))
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_source, src): src for src in targets}
        for fut in concurrent.futures.as_completed(futs):
            d = futs[fut]["dir"]
            try:
                results[d] = {"pages": fut.result(), "status": "ok"}
            except Exception as e:  # noqa: BLE001
                print(f"    [ERROR] {d}: {e}", flush=True)
                results[d] = {"status": f"error: {e}"}
    meta.update(results)

    stamp = os.environ.get("CRAWL_TIMESTAMP")
    if stamp:
        meta["_last_crawl"] = stamp
    write_if_changed(meta_path, json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    ok = sum(1 for k, v in meta.items() if isinstance(v, dict) and v.get("status") == "ok")
    print(f"[done] {ok} sources ok")


if __name__ == "__main__":
    main()
