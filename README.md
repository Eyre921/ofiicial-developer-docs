# 官方开发者文档镜像 · ofiicial-developer-docs

约 50 个 **AI / 开发平台官方文档** 的结构化镜像，每个来源都经过**域名核对**（必须是该产品自己的官方域名）。
由 CNB 定时任务每天早晚各拉取一次，与上游保持同步。

> 非官方镜像，仅供内部培训 / 检索用途。各文档版权归其厂商，商用请遵循各家官方条款。

## 收录范围（按分类）

| 分类 | 来源 |
|---|---|
| **ai-models** | Anthropic Claude Code、Anthropic API、OpenAI、Google Gemini、xAI Grok、Perplexity、Mistral、Cohere、Groq、Together、Fireworks、OpenRouter、Replicate |
| **agent-frameworks** | MCP（Model Context Protocol）、LangChain（含 LangGraph）、Vercel AI SDK、CrewAI |
| **voice-multimodal** | ElevenLabs、Deepgram、AssemblyAI、Vapi |
| **vector-db** | Pinecone、Qdrant、Weaviate、Chroma |
| **coding-agents** | Windsurf |
| **dev-platforms** | Cloudflare、Vercel、Supabase、Stripe、Prisma、Drizzle、Clerk、Resend、Sentry、Convex、Neon、Turso、Upstash、Netlify、Expo、Langfuse、GitHub、X 开发者平台、n8n、Trigger.dev、Shopify、Notion、Twilio |
| **libraries** | Hono、Svelte、Bun、TanStack、Zod |

具体每个来源的官方 URL 见 `crawl.py` 里的 `SOURCES` 注册表；抓取状态/页数见 `crawl-metadata.json`。

## 目录结构

```
<分类>/<来源>/
    llms-full.txt   或   llms.txt      各家的官方文件（Full.txt 原文；纯索引则为 llms.txt）
    index.md                           拆分页导航（仅当该来源可拆分时）
    pages/…/*.md                       镜像官方 URL 路径的单篇文档（带 frontmatter）
```

**全文优先**（`llms.txt` 常只是链接索引，本仓一律尽量拿到全文）：

1. **有官方 `llms-full.txt` 的** → 直接用全文。共 ~40 个来源，包括最初只提供索引、
   但其实也发布了 full 的 23 家（Mistral/LangChain/Vercel AI SDK/AssemblyAI/Pinecone/Qdrant/
   Prisma/Drizzle/Clerk/Convex/Neon/Turso/Upstash/Expo/n8n/Trigger.dev/Notion/Hono/Svelte/
   Bun/TanStack/Zod/Groq）。文件内嵌 `Source: url` 的会**拆成 `pages/`，目录严格镜像官方 URL
   路径、拆到最深叶子**。例：
   ```
   platform.claude.com/docs/en/api/python/beta/sessions/threads/events/stream
     → ai-models/anthropic-api/pages/api/python/beta/sessions/threads/events/stream.md
   ```
2. **真只有索引、没有 full 的**（Cohere/OpenRouter/Replicate/ElevenLabs/Deepgram/Weaviate/
   Stripe/Sentry/Netlify/Langfuse/GitHub/Shopify/Twilio）→ **顺着索引把每篇 `.md` 抓下来拼成全文**
   （链接指向 HTML 时自动试 `.md`）。设页数上限 `FOLLOW_CAP`（默认 500）防超大站爆掉，
   **命中上限会在日志里记 `[note] … 截断到 500`，不静默**（如 ElevenLabs 762 页截断到 500）。
3. **内容已丰富但无独立 full 的**（xAI Grok）→ 原样存盘。

### 关于两个大源

- **Anthropic API**：官方 `llms-full.txt` ~87MB，其中 92% 是 8 种语言各一份的重复 SDK 参考。
  默认只留概念指南 + Python 参考（~14MB）。要全量：`INCLUDE_ALL_SDK_LANGUAGES=1`。
- **Cloudflare**：官方 `llms-full.txt` ~56MB，原样镜像（frontmatter 格式，不拆）。体积大，但
  「无变化不提交」限制了 git 膨胀。

## 更新机制（CNB 流水线）

- **定时**：`crontab: 30 7,19 * * *` —— 每天 **07:30 / 19:30**（Asia/Shanghai）各一次。
- **手动**：`api_trigger`，或网页自定义按钮。
- **网页按钮 + 面板**（`.cnb/web_trigger.yml`）：仓库页有「🔄 立即刷新全部」和「🎛️ 自定义刷新」
  （面板可按分类刷新、切换 Anthropic API 是否全量八语言）。
- **省资源**：runner `cpus=2`；**上游无变化时不提交**（`git diff --cached --quiet`）。
- **不配 `push` 触发**：流水线自己 commit 回仓库，配 push 会死循环。

## 本地手动跑

```bash
python crawl.py                         # 全部来源
python crawl.py ai-models               # 只抓某个分类
python crawl.py dev-platforms/stripe    # 只抓某个来源
INCLUDE_ALL_SDK_LANGUAGES=1 python crawl.py ai-models/anthropic-api
uv run crawl.py                         # 也可用 uv
```

零第三方依赖（纯 Python 标准库 + 系统 curl）。抓取时间戳由 `CRAWL_TIMESTAMP` 注入，
保证「无变化 = 无 diff」。
