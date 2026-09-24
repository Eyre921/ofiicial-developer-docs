---
title: "Fire Pass"
source: https://docs.fireworks.ai/firepass
path: firepass
---

Use selected open-weight model routers for personal, non-production agentic coding

Fire Pass gives eligible users access to selected open-weight model routers for personal, non-production agentic coding. Included requests are covered while the pass is active, subject to its limits and terms. Check the [Fire Pass page](https://app.fireworks.ai/fire-pass) for your status and currently enabled models.

<Note>
  Fire Pass is experimental and is not currently open to new subscriptions.
  Existing users and promo recipients can continue to manage their pass.
  Features, availability, and pricing are subject to change.
</Note>

## What's included

With an active Fire Pass you get:

* Covered usage on the open-weight model routers enabled for your pass
* A dedicated `fpk_...` key that works only with Fire Pass routes
* Access through supported FireConnect harnesses and compatible OpenAI- or Anthropic-style clients

Use a standard Fireworks key (`fw_...`) for models and features outside Fire Pass.

## Getting Started

<Steps>
  <Step title="Create an account">
    If you haven't already, sign up for a [Fireworks
    account](https://app.fireworks.ai).
  </Step>

  <Step title="Activate your pass">
    Go to the [**Fire Pass** page](https://app.fireworks.ai/fire-pass). If you
    received a promo code, enter it there and review the pass details.
  </Step>

  <Step title="Get a Fire Pass API key">
    Create a dedicated Fire Pass API key. Requests to enabled routes are covered
    while your pass is active, subject to its limits and terms.
  </Step>
</Steps>

## Using your Fire Pass

Fire Pass is designed for personal agentic coding. [FireConnect](/ecosystem/fireconnect/overview) detects `fpk_...` keys, selects `kimi-fast-latest` by default, and exposes only the routers supported by Fire Pass.

```bash theme={null}
fireconnect login
fireconnect model list
fireconnect claude
```

| FireConnect harness           | Fire Pass                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------- |
| Claude Code, OpenCode, Pi     | Supported                                                                                           |
| Cursor IDE, VS Code Chat      | Supported                                                                                           |
| GitHub Copilot app and CLI    | Supported                                                                                           |
| DeepSeek Harness              | Supported                                                                                           |
| Codex CLI and ChatGPT desktop | Not supported. These clients use the Responses API, which does not currently accept Fire Pass keys. |

<Warning>
  Fire Pass keys cannot use `auto`, `auto-instant`, or FireRouter. Run
  `fireconnect model list` with your Fire Pass key to see the available routes.
</Warning>

### General Configuration

If your tool supports custom API endpoints, you can configure it manually using these details:

* **Model ID**: `accounts/fireworks/routers/kimi-fast-latest`
* **API Key**: Generate a new Fire Pass API key (generated at [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
* **Base URL (OpenAI-compatible)**: `https://api.fireworks.ai/inference/v1`
* **Base URL (Anthropic-compatible)**: `https://api.fireworks.ai/inference` (some tools may expect `/v1/messages` appended)

`kimi-fast-latest` currently resolves to Kimi K3 Fast, with a 1,040,000-token
context window and up to 131,072 output tokens. Recheck the [Fire Pass
page](https://app.fireworks.ai/fire-pass) when the latest alias changes.

<AccordionGroup>
  <Accordion title="OpenClaw">
    Add Fireworks as an OpenAI-compatible provider in
    `~/.openclaw/openclaw.json`. Use the base URL, Fire Pass key, and
    `kimi-fast-latest` model ID from [General Configuration](#general-configuration).

    <Warning>
      Do not share your Fire Pass key or commit it to version control.
    </Warning>

    Follow the [OpenClaw provider documentation](https://openclaw.ai) to finish
    configuring and testing the custom provider.
  </Accordion>

  <Accordion title="OpenCode">
    Use [FireConnect](/ecosystem/fireconnect/harnesses#opencode):

    ```bash theme={null}
    fireconnect login
    fireconnect opencode
    ```

    Fire Pass keys default to `kimi-fast-latest`. Run `fireconnect model list`
    to see the other routes enabled for Fire Pass.
  </Accordion>

  <Accordion title="Cline">
    To configure Cline with your Fire Pass:

    1. Install the Cline extension in VS Code from [cline.bot](https://cline.bot) or the VS Code marketplace
    2. Open VS Code settings and search for "Cline" or use the Cline panel
    3. Configure the following settings:

    **API Configuration:**

    * **API Provider**: OpenAI Compatible
    * **Base URL**: `https://api.fireworks.ai/inference/v1`
    * **OpenAI Compatible API Key**: Your Fire Pass key (from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
    * **Model ID**: `accounts/fireworks/routers/kimi-fast-latest`

    **Model Configuration:**

    * **Supports Images**: Enabled (checked)
    * **Context Window Size**: 1,040,000
    * **Max Output Tokens**: 131,072
    * **Input Price / 1M tokens**: 0 while covered by an active Fire Pass
    * **Output Price / 1M tokens**: 0 while covered by an active Fire Pass

    4. Save your settings and send a request. Fire Pass applies when the key and route are eligible.
  </Accordion>

  <Accordion title="Claude Code">
    Use [FireConnect](/ecosystem/fireconnect/harnesses#claude-code):

    ```bash theme={null}
    fireconnect login
    fireconnect claude
    ```

    FireConnect pins Claude Code's model slots to the Fire Pass default. Fire
    Pass does not add the standard Fireworks catalog or FireRouter to `/model`.
  </Accordion>

  <Accordion title="Kilo Code">
    To configure Kilo Code with your Fire Pass:

    1. Install the Kilo Code extension in VS Code from the [VS Code marketplace](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code) or [kilocode.ai](https://kilocode.ai)
    2. Open Kilo Code and select **Bring my own Key** on the "How would you like to get started?" screen
    3. Configure the following settings:

    **API Configuration:**

    * **API Provider**: OpenAI Compatible
    * **Base URL**: `https://api.fireworks.ai/inference/v1`
    * **API Key**: Your Fire Pass key (from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys))
    * **Model**: `accounts/fireworks/routers/kimi-fast-latest`
      * Type or paste the router ID and select "Use custom" when it appears

    **Model Configuration:**

    * **Context Window Size**: 1,040,000
    * **Supports images**: Enabled (checked)
    * **Input Price**: 0 while covered by an active Fire Pass
    * **Output Price**: 0 while covered by an active Fire Pass

    4. Save your settings and send a request. Fire Pass applies when the key and route are eligible.
  </Accordion>

  <Accordion title="LangChain Deep Agent">
    Set `FIREWORKS_API_KEY` to your Fire Pass key from [app.fireworks.ai/api-keys](https://app.fireworks.ai/api-keys). Install [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/models) with the Fireworks integration, then pass the latest Fire Pass router as `fireworks:accounts/fireworks/routers/kimi-fast-latest`:

    ```bash theme={null}
    pip install deepagents langchain-fireworks
    ```

    ```python theme={null}
    from deepagents import create_deep_agent

    agent = create_deep_agent(
        model="fireworks:accounts/fireworks/routers/kimi-fast-latest",
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

Fire Pass is intended for **non-production coding use only**. By activating Fire Pass you agree to the following:

* **Allowed**: Personal development, experimentation, and coding with supported agentic harnesses and compatible clients
* **Prohibited**: Production workloads and any use that violates the [Fireworks Terms of Service](https://fireworks.ai/terms-of-service)

<Warning>
  Violations of these terms may result in pass revocation.
</Warning>

## FAQ

<AccordionGroup>
  <Accordion title="Can I use Fire Pass with any model?">
    No. Fire Pass covers only its enabled routes. Check the Fire Pass page for
    the latest set.
  </Accordion>

  <Accordion title="Do I need an invite code?">
    Fire Pass is not currently open to new subscriptions. Existing users and
    promo recipients can manage access on the Fire Pass page.
  </Accordion>

  <Accordion title="Do I need to use a special model ID?">
    Use one of the routers enabled for Fire Pass. FireConnect defaults to
    `kimi-fast-latest`; run `fireconnect model list` to see the current set.
    For manual configuration, use the full ID
    `accounts/fireworks/routers/kimi-fast-latest`.
  </Accordion>

  <Accordion title="Can I use FireRouter or Auto?">
    No. `firerouter`, `auto`, and `auto-instant` require a standard Fireworks
    key (`fw_...`). Fire Pass keys can use only Fire Pass-enabled routes.
  </Accordion>

  <Accordion title="How will this appear on my billing dashboard?">
    Included usage remains visible while it is covered by your active pass.
    View the pass status and expiration date on the [**Billing**
    page](https://app.fireworks.ai/account/billing).
  </Accordion>

  <Accordion title="Can I use other models with my agentic harness?">
    Yes, with a standard Fireworks key (`fw_...`). A Fire Pass key (`fpk_...`)
    works only with routes enabled for Fire Pass. Other models use standard
    per-token billing.
  </Accordion>
</AccordionGroup>
