---
title: "Coding agent setup"
source: https://docs.together.ai/docs/agent-skills
path: docs/agent-skills
---

Make your AI coding agent Together-AI-aware with ready-made skills for code generation and an MCP server for live docs lookup.

Together AI publishes two complementary tools for coding agents:

* [Skills](#skills): 12 domain-specific skills that load on demand and teach your agent how to write correct Together AI code (right model IDs, SDK patterns, best practices).
* [Docs MCP server](#docs-mcp-server): Gives your agent live access to this documentation site so it can look up current information without leaving your editor.

Install both for the best experience: skills for code generation and MCP for documentation lookup.

## Skills

When your agent detects a relevant task, it automatically loads the right skill. You can also call a skill explicitly with `/<skill_name>`.

### Install skills

<CodeGroup>
  ```bash Any agent theme={null}
  npx skills add togethercomputer/skills
  ```

  ```bash Claude Code theme={null}
  # From the plugin marketplace
  /plugin marketplace add togethercomputer/skills

  # Or install a single skill
  /plugin install together-chat-completions@togethercomputer/skills

  # Or copy manually (project-level)
  cp -r skills/together-* your-project/.claude/skills/

  # Or copy manually (global, available in all projects)
  cp -r skills/together-* ~/.claude/skills/
  ```

  ```bash Cursor theme={null}
  # Install via the Cursor plugin flow using the
  # .cursor-plugin/ manifests in the repository:
  # https://github.com/togethercomputer/skills
  ```

  ```bash Codex theme={null}
  cp -r skills/together-* your-project/.agents/skills/
  ```

  ```bash Gemini CLI theme={null}
  gemini extensions install https://github.com/togethercomputer/skills.git --consent
  ```
</CodeGroup>

To verify the install, you should see one `SKILL.md` per installed skill (for example, `ls your-project/.claude/skills/together-*/SKILL.md`).

### Available skills

| Skill                                                                                                                          | What it covers                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **[together-chat-completions](https://github.com/togethercomputer/skills/tree/main/skills/together-chat-completions)**         | Serverless chat inference, streaming, multi-turn conversations, function calling (6 patterns), structured JSON outputs, and reasoning models. |
| **[together-images](https://github.com/togethercomputer/skills/tree/main/skills/together-images)**                             | Text-to-image generation, image editing with Kontext, FLUX model selection, LoRA-based styling, and reference-image guidance.                 |
| **[together-video](https://github.com/togethercomputer/skills/tree/main/skills/together-video)**                               | Text-to-video and image-to-video generation, keyframe control, model and dimension selection, and async job polling.                          |
| **[together-audio](https://github.com/togethercomputer/skills/tree/main/skills/together-audio)**                               | Text-to-speech (REST, streaming, realtime WebSocket) and speech-to-text (transcription, translation, diarization, timestamps).                |
| **[together-embeddings](https://github.com/togethercomputer/skills/tree/main/skills/together-embeddings)**                     | Dense vector generation, semantic search, RAG pipelines, and reranking with dedicated model inference.                                        |
| **[together-fine-tuning](https://github.com/togethercomputer/skills/tree/main/skills/together-fine-tuning)**                   | LoRA, full, DPO preference, VLM, function-calling, and reasoning fine-tuning, plus BYOM uploads.                                              |
| **[together-batch-inference](https://github.com/togethercomputer/skills/tree/main/skills/together-batch-inference)**           | Async batch jobs with JSONL input, polling, result downloads, and up to 50% cost savings.                                                     |
| **[together-evaluations](https://github.com/togethercomputer/skills/tree/main/skills/together-evaluations)**                   | LLM-as-a-judge workflows: classify, score, and compare evaluations with external provider support.                                            |
| **[together-sandboxes](https://github.com/togethercomputer/skills/tree/main/skills/together-sandboxes)**                       | Remote sandboxed Python execution with session reuse, file uploads, and chart outputs.                                                        |
| **[together-dedicated-endpoints](https://github.com/togethercomputer/skills/tree/main/skills/together-dedicated-endpoints)**   | Single-tenant GPU endpoints with hardware sizing, autoscaling, and fine-tuned model deployment.                                               |
| **[together-dedicated-containers](https://github.com/togethercomputer/skills/tree/main/skills/together-dedicated-containers)** | Custom Dockerized inference workers using the Jig CLI, Sprocket SDK, and queue API.                                                           |
| **[together-gpu-clusters](https://github.com/togethercomputer/skills/tree/main/skills/together-gpu-clusters)**                 | On-demand and reserved GPU clusters (H100, H200, B200) with Kubernetes, Slurm, and shared storage.                                            |

### Use a single skill

Each skill works on its own for focused tasks. Describe what you want and the right skill activates, or invoke a specific skill with `/<skill_name>`.

If you prompt your agent with:

```text theme={null}
Build a multi-turn chatbot using Together AI with Kimi-K2.5
that can call a weather API and return structured JSON.
```

The agent uses `together-chat-completions` to generate correct SDK code with the right model ID, streaming setup, tool definitions, and the complete tool-call loop.

### Chain skills together

Skills define hand-off boundaries between products, so the agent can chain them together for tasks that span multiple Together AI services.

If you prompt your agent with:

```text theme={null}
Embed my document corpus with Together AI, build a retrieval pipeline
with reranking, then evaluate the answer quality with an LLM judge.
```

The agent chains three skills:

1. `together-embeddings`: Generates dense vectors and builds a cosine-similarity retriever with reranking.
2. `together-chat-completions`: Generates answers from the retrieved context.
3. `together-evaluations`: Scores answer quality with an LLM judge and downloads the per-row results.

See the [skills repository](https://github.com/togethercomputer/skills) for more workflow examples.

### SDK compatibility

All generated code targets the Together Python v2 SDK (`together>=2.0.0`) and the Together TypeScript SDK (`together-ai`). If you're upgrading from v1, see the [Python v2 SDK migration guide](/docs/pythonv2-migration-guide).

## Docs MCP server

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) lets AI coding agents call external tools and pull in external data. The Together AI docs MCP server gives your agent direct access to this documentation site without leaving your editor.

### Install

The fastest install is the universal `npx add-mcp` shortcut, which detects your active client and configures the server in one step. The other tabs cover client-specific install commands and manual configuration.

<Tabs>
  <Tab title="Universal">
    ```bash theme={null}
    npx add-mcp https://docs.together.ai/mcp
    ```
  </Tab>

  <Tab title="Claude Code">
    ```bash theme={null}
    claude mcp add --transport http "TogetherAIDocs" https://docs.together.ai/mcp
    ```
  </Tab>

  <Tab title="Cursor">
    <a href="https://cursor.com/en/install-mcp?name=together-docs&config=eyJ1cmwiOiJodHRwczovL2RvY3MudG9nZXRoZXIuYWkvbWNwIn0%3D">
      <img alt="Install MCP Server" />
    </a>

    For manual configuration, add this to your Cursor MCP settings:

    ```json theme={null}
    {
      "mcpServers": {
        "together-docs": {
          "url": "https://docs.together.ai/mcp"
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    [Install in VS Code](https://vscode.dev/redirect/mcp/install?name=Together%20AI%20Docs\&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fdocs.together.ai%2Fmcp%22%7D)

    For manual configuration, add this to your VS Code `settings.json`:

    ```json theme={null}
    {
      "mcp": {
        "servers": {
          "together-docs": {
            "type": "http",
            "url": "https://docs.together.ai/mcp"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Codex">
    See the [Codex repository](https://github.com/openai/codex) for details. To connect to the remote server, add this to your Codex configuration:

    ```toml theme={null}
    [mcp_servers.together_docs]
    type = "http"
    url = "https://docs.together.ai/mcp"
    ```
  </Tab>

  <Tab title="OpenCode">
    Add this to your OpenCode configuration file:

    ```json theme={null}
    {
      "mcp": {
        "together_docs": {
          "type": "remote",
          "url": "https://docs.together.ai/mcp",
          "enabled": true
        }
      }
    }
    ```
  </Tab>
</Tabs>

### Prompt examples

Once installed, your agent can answer prompts like:

* "Write a script to process data with batch inference."
* "Build a simple chat app with Together AI's chat completions API."
* "Find the best open-source model for frontier coding."
* "How do I fine-tune a model on my own data?"

The MCP server provides tools to search and retrieve documentation content, so your agent gets accurate answers without leaving your coding environment.

## Resources

* [Skills repository on GitHub](https://github.com/togethercomputer/skills): Source code, full reference docs, and runnable scripts for all 12 skills.
* [Together AI cookbook](https://github.com/togethercomputer/together-cookbook): End-to-end examples and tutorials.
* [Python v2 SDK migration guide](/docs/pythonv2-migration-guide): Breaking changes between the v1 and v2 SDKs.
* [Agent Skills specification](https://agentskills.io/specification): The open standard these skills follow.
