---
title: "Quickstart"
source: https://docs.fireworks.ai/nexus/quickstart
path: nexus/quickstart
---

Connect a coding harness, application, or LLM gateway to Fireworks and make your first Nexus request.

Pick how you work. Each path takes a few minutes and uses the same Fireworks models, routers, and account controls.

<Columns>
  <Card title="Coding harness" icon="terminal" href="#connect-a-coding-harness">
    Claude Code, Codex, OpenCode, Cursor IDE, and more
  </Card>

  <Card title="API or SDK" icon="code" href="#call-the-api">
    OpenAI, Anthropic, or Fireworks SDK
  </Card>

  <Card title="LLM gateway" icon="shuffle" href="#use-an-llm-gateway">
    LiteLLM, Portkey, and other gateways
  </Card>
</Columns>

You need a [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) for the API and gateway paths. FireConnect can create one for you when you sign in.

## Connect a coding harness

<Steps>
  <Step title="Install FireConnect" icon="download">
    ```bash wrap theme={null}
    curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash
    ```

    Requires Node.js 18 or later. On Windows, run it from Git Bash.
  </Step>

  <Step title="Sign in" icon="key">
    ```bash wrap theme={null}
    fireconnect login
    ```

    Sign in with your browser, or paste an existing Fireworks key.
  </Step>

  <Step title="Connect your harness" icon="plug">
    <CodeGroup>
      ```bash Claude Code theme={null}
      fireconnect claude
      ```

      ```bash Codex CLI theme={null}
      fireconnect codex
      ```

      ```bash Codex app theme={null}
      # Quit the Codex app first
      fireconnect codex
      ```

      ```bash ChatGPT desktop theme={null}
      # Quit the ChatGPT app first
      fireconnect codex
      ```

      ```bash OpenCode theme={null}
      fireconnect opencode
      ```

      ```bash Cursor IDE theme={null}
      fireconnect cursor
      ```

      ```bash VS Code theme={null}
      fireconnect vscode
      ```

      ```bash Pi theme={null}
      fireconnect pi
      ```
    </CodeGroup>

    The Codex CLI, the Codex app, and the ChatGPT desktop app share one config, so `fireconnect codex` connects all three. For desktop apps, including Cursor IDE and VS Code, quit the app first. See [Coding Harnesses](/nexus/harnesses) for every harness.
  </Step>

  <Step title="Restart and pick a model" icon="sparkles">
    Restart the harness and open its model picker. You will see `auto`, FireRouter, and Fireworks open models.

    <Frame>
      <img alt="Claude Code model picker with FireRouter selected and Auto, DeepSeek, GLM, Kimi, and MiniMax options" />
    </Frame>

    <Check>`fireconnect claude status` shows the configured model and Fireworks endpoint.</Check>
  </Step>
</Steps>

<Tip>
  **Prefer not to install anything?** Every harness has a **Manual setup** tab
  in [Coding Harnesses](/nexus/harnesses) with the exact settings to add
  yourself.
</Tip>

## Call the API

<Steps>
  <Step title="Export your key" icon="key">
    ```bash wrap theme={null}
    export FIREWORKS_API_KEY="fw_..."
    ```
  </Step>

  <Step title="Send a request" icon="paper-plane">
    Point the SDK you already use at Fireworks:

    <CodeGroup>
      ```bash cURL theme={null}
      curl https://api.fireworks.ai/inference/v1/chat/completions \
        -H "Authorization: Bearer $FIREWORKS_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "glm-latest",
          "messages": [{"role": "user", "content": "Say pong in one word."}]
        }'
      ```

      ```python OpenAI SDK theme={null}
      import os

      from openai import OpenAI

      client = OpenAI(
          api_key=os.environ["FIREWORKS_API_KEY"],
          base_url="https://api.fireworks.ai/inference/v1",
      )

      response = client.chat.completions.create(
          model="glm-latest",
          messages=[{"role": "user", "content": "Say pong in one word."}],
      )

      print(response.choices[0].message.content)
      ```

      ```python Anthropic SDK theme={null}
      import os

      import anthropic

      client = anthropic.Anthropic(
          api_key=os.environ["FIREWORKS_API_KEY"],
          base_url="https://api.fireworks.ai/inference",
      )

      message = client.messages.create(
          model="glm-latest",
          max_tokens=1024,
          messages=[{"role": "user", "content": "Say pong in one word."}],
      )

      print(next(block.text for block in message.content if block.type == "text"))
      ```

      ```python Fireworks SDK theme={null}
      from fireworks import Fireworks

      client = Fireworks()

      response = client.chat.completions.create(
          model="glm-latest",
          messages=[{"role": "user", "content": "Say pong in one word."}],
      )

      print(response.choices[0].message.content)
      ```
    </CodeGroup>

    <Check>The reply says `pong`.</Check>
  </Step>

  <Step title="Try a router" icon="shuffle">
    Change `model` to `firerouter/opus`. FireRouter picks a model for each turn, and the response `model` field shows which one served it. Routes with closed models need a [provider credential](/nexus/firerouter#provide-anthropic-and-openai-credentials).

    More examples, including the Responses API: [FireRouter Setup](/nexus/firerouter/setup#api-and-sdk).
  </Step>
</Steps>

## Use an LLM gateway

<Steps>
  <Step title="Add a Fireworks model to LiteLLM" icon="file-pen">
    ```yaml config.yaml theme={null}
    model_list:
      - model_name: glm-latest
        litellm_params:
          model: fireworks_ai/accounts/fireworks/routers/glm-latest
          api_key: os.environ/FIREWORKS_API_KEY
          api_base: https://api.fireworks.ai/inference/v1
    ```
  </Step>

  <Step title="Start the proxy" icon="play">
    ```bash wrap theme={null}
    pip install "litellm[proxy]"
    litellm --config config.yaml
    ```
  </Step>

  <Step title="Send a request" icon="paper-plane">
    ```bash wrap theme={null}
    curl http://localhost:4000/chat/completions \
      -H "Content-Type: application/json" \
      -d '{
        "model": "glm-latest",
        "messages": [{"role": "user", "content": "Say pong in one word."}]
      }'
    ```

    <Check>The reply says `pong`.</Check>
  </Step>
</Steps>

Using Portkey, or adding FireRouter to your gateway? See [FireRouter Setup](/nexus/firerouter/setup#llm-gateway) and [LLM Gateways](/nexus/llm-gateways).

## Next steps

<Columns>
  <Card title="Open Models" icon="sparkles" href="/nexus/open-models">
    Use `auto`, follow a model family, choose a fast tier, or pin a version.
  </Card>

  <Card title="FireRouter" icon="shuffle" href="/nexus/firerouter">
    Let one model ID choose a model for each new user turn.
  </Card>

  <Card title="Usage and Cost" icon="chart-line" href="/nexus/metrics">
    See session estimates and Fireworks model usage by model, user, or API key.
  </Card>

  <Card title="Spend Limits" icon="gauge" href="/nexus/usage-limits">
    Set per-user caps for supported Fireworks serverless models.
  </Card>
</Columns>
