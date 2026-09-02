---
title: "Configure Kimi Code with Together AI models"
source: https://docs.together.ai/docs/how-to-use-kimi-code
path: docs/how-to-use-kimi-code
---

Power Moonshot AI's coding agent with Together AI-hosted models.

Kimi Code is Moonshot AI's coding agent, available as a terminal CLI and a VS Code extension. It was built around the Kimi model family, which makes it a natural pairing with [Kimi K3 on Together AI](/docs/kimi-k3-quickstart), Moonshot's flagship open-weight model with a 1.05M-token context window.

This guide shows you how to connect the Kimi Code CLI directly to the Together AI serverless endpoint for Kimi K3, so your agent runs on fast, secure infrastructure with your own Together AI API key.

You can use this same approach to connect Kimi Code to any open-source model in the [serverless catalog](/docs/serverless/models), like GLM 5.2 or Qwen3 Coder Next, and switch between them as you work.

## 1. Install Kimi Code

Install with the standalone installer:

```bash theme={null}
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

Or install globally with npm (requires Node.js 22.19.0 or later):

```bash theme={null}
npm install -g @moonshot-ai/kimi-code
```

Verify the installation:

```bash theme={null}
kimi --version
```

## 2. Add Together AI as a provider

Kimi Code reads providers and models from `~/.kimi-code/config.toml`. Add Together AI as an OpenAI-compatible provider, register Kimi K3 under it, and make it the default model:

```toml ~/.kimi-code/config.toml theme={null}
default_model = "together/kimi-k3"

[providers.together]
type = "openai"
base_url = "https://api.together.ai/v1"
api_key = "your_together_api_key"

[models."together/kimi-k3"]
provider = "together"
model = "moonshotai/Kimi-K3"
max_context_size = 1048576
capabilities = ["thinking", "image_in", "tool_use"]
display_name = "Kimi K3 (Together AI)"
```

Replace `your_together_api_key` with your actual [Together AI API key](https://api.together.ai/settings/projects/~current/api-keys).

If the file already exists, keep any settings you have and add the `default_model` line, the `[providers.together]` table, and the `[models."together/kimi-k3"]` table alongside them.

Validate the configuration:

```bash theme={null}
kimi doctor
```

## 3. Run Kimi Code

Launch the agent from your project directory:

```bash theme={null}
cd your_project
kimi
```

Kimi Code starts its terminal UI with Kimi K3 on Together AI as the active model. Use `/model` inside the session to confirm the model or switch between any models you have configured. Kimi K3 thinks by default, and Kimi Code renders the reasoning trace as the agent works.

## Alternative: configure with environment variables

For a quick test without touching `config.toml`, you can select the model entirely through the `KIMI_MODEL_*` environment variables. Kimi Code synthesizes a temporary provider from them for that session only:

```bash theme={null}
export KIMI_MODEL_NAME="moonshotai/Kimi-K3"
export KIMI_MODEL_PROVIDER_TYPE="openai"
export KIMI_MODEL_BASE_URL="https://api.together.ai/v1"
export KIMI_MODEL_API_KEY="your_together_api_key"
export KIMI_MODEL_MAX_CONTEXT_SIZE="1048576"

kimi
```

Nothing persists after the session ends, so use the `config.toml` setup above for day-to-day work.

That's it! You now have Moonshot's own coding agent running Kimi K3 on Together AI. See the [Kimi K3 quickstart](/docs/kimi-k3-quickstart) for model details and pricing, and the [Kimi Code documentation](https://www.kimi.com/code/docs/en/) for the agent's full feature set.
