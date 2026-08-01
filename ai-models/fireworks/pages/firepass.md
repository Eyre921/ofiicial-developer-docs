---
title: "Fire Pass Setup"
source: https://docs.fireworks.ai/firepass
path: firepass
---

Open weight models for personal agentic coding — Fire Pass

Fire Pass is a pass that gives you access to **Open weight models** for use in agentic coding harnesses like [Claude Code](/ecosystem/fireconnect/claude-code), [OpenCode](/ecosystem/fireconnect/opencode), Cline, Kilo Code, OpenClaw, and [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/models) — with no per-token charges for included models. Check the [Fire Pass page](https://app.fireworks.ai/fire-pass) for the latest enabled models.

<Note>
  **Fire Pass is separate from [Fireworks Nexus](/fireworks-nexus/overview).** Fire Pass is an invite-only promotion for personal, non-production coding. Nexus is the team control plane for connecting harnesses, intelligent routing, and per-seat spend limits.
</Note>

<Note>
  **Fire Pass** is an experimental product. Features, availability, and
  pricing are subject to change.
</Note>

## What's Included

With an active Fire Pass you get:

* Zero per-token costs on included open weight models (a powerful reasoning model with a 1M context window, optimized for complex coding tasks)
* A NEW dedicated Fire Pass key that only works for open weight models. Use your normal Fireworks key for all other models
* Full compatibility with OpenAI- and Anthropic-compatible agentic coding tools

## Getting Started

<Steps>
  <Step title="Create an account">
    If you haven't already, sign up for a [Fireworks
    account](https://app.fireworks.ai).
  </Step>

  <Step title="Activate your pass">
    Go to the [**Fire Pass** page](https://app.fireworks.ai/fire-pass),
    review the details and enter your promo code. Your pass activates immediately.
  </Step>

  <Step title="Get a Fire Pass API key">
    Create a new dedicated Fire Pass API key and use it with any of the supported agentic harnesses below. Requests to included open weight models will no longer incur per-token charges while your pass is active.
  </Step>
</Steps>

## Using your Fire Pass

Fire Pass is designed for use with personal agentic coding harnesses. For Claude Code, OpenCode, Codex, and Pi, use [FireConnect](/ecosystem/fireconnect/overview) — it detects `fpk_...` keys and applies Fire Pass defaults automatically. Below are setup guides for other supported tools.

### General Configuration

If your tool supports custom API endpoints, you can configure it manually using these details:

* **Model ID**: `accounts/fireworks/routers/kimi-k3-fast`
* **API Key**: Generate a new Fire Pass API key (generated at [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
* **Base URL (OpenAI-compatible)**: `https://api.fireworks.ai/inference/v1`
* **Base URL (Anthropic-compatible)**: `https://api.fireworks.ai/inference` (some tools may expect `/v1/messages` appended)

<AccordionGroup>
  <Accordion title="OpenClaw">
    1. **Configure the open weight model as the default model** — run the setup script with your Fireworks API key from the [**API Keys** page](https://app.fireworks.ai/api-keys). Replace `YOUR_FIREWORKS_API_KEY` with your key:

    ```bash theme={null}
    curl -fsSL https://storage.googleapis.com/fireworks-public/openclaw/setup-fireworks.sh | bash -s -- YOUR_FIREWORKS_API_KEY
    ```

    This creates `~/.openclaw/openclaw.json` with your Fireworks credentials.

    <Warning>
      Do not share your API key or commit it to version control. Use the
      placeholder above only as a pattern — substitute your real key locally.
    </Warning>

    2. **Install OpenClaw**

    <Tabs>
      <Tab title="macOS / Linux">
        ```bash theme={null}
        curl -fsSL https://openclaw.ai/install.sh | bash
        ```
      </Tab>

      <Tab title="Windows (PowerShell)">
        ```powershell theme={null}
        iwr -useb https://openclaw.ai/install.ps1 | iex
        ```
      </Tab>
    </Tabs>

    3. **Run the onboarding wizard** — in a terminal:

    ```bash theme={null}
    openclaw onboard --install-daemon
    ```

    Choose **Quickstart** mode, skip model and authentication (already configured), and accept the remaining defaults.

    4. **Open the chat UI** — run:

    ```bash theme={null}
    openclaw dashboard
    ```

    The UI opens at [http://127.0.0.1:18789](http://127.0.0.1:18789). Send a message to confirm the **open weight model** is responding.

    For more about OpenClaw, see [openclaw.ai](https://openclaw.ai).
  </Accordion>

  <Accordion title="OpenCode">
    OpenCode setup lives on the [OpenCode integration guide](/ecosystem/fireconnect/opencode):

    * [FireConnect setup](/ecosystem/fireconnect/opencode#enable-fireworks-routing) (recommended)
    * [Using Fire Pass with OpenCode](/ecosystem/fireconnect/opencode#using-fire-pass)
    * [Built-in provider connection](/ecosystem/fireconnect/opencode#built-in-provider-connection) (`/connect` in OpenCode)

    With FireConnect, Fire Pass keys default to the `kimi-fast-latest` router.
  </Accordion>

  <Accordion title="Cline">
    To configure Cline with your Fire Pass:

    1. Install the Cline extension in VS Code from [cline.bot](https://cline.bot) or the VS Code marketplace
    2. Open VS Code settings and search for "Cline" or use the Cline panel
    3. Configure the following settings:

    **API Configuration:**

    * **API Provider**: OpenAI Compatible
    * **Base URL**: `https://api.fireworks.ai/inference/v1`
    * **OpenAI Compatible API Key**: Your Fireworks API key (from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
    * **Model ID**: `accounts/fireworks/routers/kimi-k3-fast`

    **Model Configuration:**

    * **Supports Images**: Enabled (checked)
    * **Context Window Size**: 256000
    * **Max Output Tokens**: 256000
    * **Input Price / 1M tokens**: 0 (Fire Pass covers all costs)
    * **Output Price / 1M tokens**: 0 (Fire Pass covers all costs)
    * **Temperature**: 1

    4. Save your settings and start using Cline — your Fire Pass will automatically apply to requests to the turbo router
  </Accordion>

  <Accordion title="Claude Code">
    All Claude Code setup lives on the [Claude Code integration guide](/ecosystem/fireconnect/claude-code):

    * [FireConnect overview](/ecosystem/fireconnect/overview#install) (recommended)
    * [Using Fire Pass with Claude Code](/ecosystem/fireconnect/claude-code#using-fire-pass)

    With FireConnect, Fire Pass keys route all model aliases to `kimi-fast-latest`.
  </Accordion>

  <Accordion title="Kilo Code">
    To configure Kilo Code with your Fire Pass:

    1. Install the Kilo Code extension in VS Code from the [VS Code marketplace](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code) or [kilocode.ai](https://kilocode.ai)
    2. Open Kilo Code and select **Bring my own Key** on the "How would you like to get started?" screen
    3. Configure the following settings:

    **API Configuration:**

    * **API Provider**: OpenAI Compatible
    * **Base URL**: `https://api.fireworks.ai/inference/v1`
    * **API Key**: Your Fireworks API key (from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
    * **Model**: `accounts/fireworks/routers/kimi-k3-fast`
      * Type or paste the router ID and select "Use custom" when it appears

    **Model Configuration:**

    * **Context Window Size**: 256000 (256K tokens)
    * **Supports images**: Enabled (checked)
    * **Input Price**: 0 (Fire Pass covers all costs)
    * **Output Price**: 0 (Fire Pass covers all costs)

    4. Save your settings and start using Kilo Code — your Fire Pass will automatically apply to requests to the turbo router
  </Accordion>

  <Accordion title="LangChain Deep Agent">
    Set `FIREWORKS_API_KEY` to your API key from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys). Install [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/models) with the Fireworks integration, then pass the turbo router as `fireworks:accounts/fireworks/routers/kimi-k3-fast`:

    ```bash theme={null}
    pip install deepagents langchain-fireworks
    ```

    ```python theme={null}
    from deepagents import create_deep_agent

    agent = create_deep_agent(
        model="fireworks:accounts/fireworks/routers/kimi-k3-fast",
        system_prompt="You are a helpful coding assistant.",
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Hello"}]},
    )
    ```

    See the LangChain docs for [models](https://docs.langchain.com/oss/python/deepagents/models) and [customization](https://docs.langchain.com/oss/python/deepagents/customization).
  </Accordion>
</AccordionGroup>

## Terms of Use

Fire Pass is intended for **non production coding use only**. By activating Fire Pass you agree to the following:

* **Allowed**: Personal development, experimentation, and coding with agentic harnesses (Claude Code, OpenCode, Codex, Pi, Cline, Kilo Code, OpenClaw, LangChain Deep Agents, and similar tools)
* **Prohibited**: Production workloads and any use that violates the [Fireworks Terms of Service](https://fireworks.ai/terms-of-service)

<Warning>
  Violations of these terms may result in pass revocation.
</Warning>

## FAQ

<AccordionGroup>
  <Accordion title="Can I use Fire Pass with any model?">
    No. Fire Pass only covers the models that are enabled on it.
    Check the Fire Pass page for the latest enabled models.
  </Accordion>

  <Accordion title="Do I need an invite code?">
    Fire Pass is currently by invite only.
  </Accordion>

  <Accordion title="Do I need to use a special model ID?">
    Yes. You must use the specific router ID for the turbo model:
    `accounts/fireworks/routers/kimi-k3-fast`. The Fireworks billing system
    will automatically detect your active Fire Pass and zero out the cost
    for requests to this endpoint.
  </Accordion>

  <Accordion title="How will this appear on my billing dashboard?">
    Your usage of included open weight models will still be logged in your dashboard so you can track your request volume,
    but the associated cost will show as \$0.00 while your pass is active.
    You can also view your pass’s active status and expiration date directly on the [**Billing**
    page](https://app.fireworks.ai/account/billing).
  </Accordion>

  <Accordion title="Can I use other models with my agentic harness?">
    Yes. You can use any Fireworks model with your agentic harness.
    However, only included open weight model requests are covered by Fire Pass.
    Usage of other models will be billed to your account at standard per-token rates.
  </Accordion>
</AccordionGroup>
