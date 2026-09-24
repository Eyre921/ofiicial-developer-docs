---
title: "Quickstart"
source: https://docs.fireworks.ai/nexus/quickstart
path: nexus/quickstart
---

Connect a coding harness, application, or LLM gateway to Fireworks and make your first Nexus request.

Connect through a coding harness, an API or SDK, or an LLM gateway. Harnesses and direct API clients use the same Fireworks model IDs and account controls. Gateway setup varies by provider.

<Tabs>
  <Tab title="Coding harness">
    Install FireConnect, sign in, and connect the harness you already use:

    ```bash wrap theme={null}
    curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash

    fireconnect login
    fireconnect claude
    ```

    Or use the raw GitHub URL instead: `curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash`.

    Restart Claude Code, then open `/model`. FireConnect automatically adds coding-ready open models and `auto`. Replace `claude` with another harness from [Coding Harnesses](/nexus/harnesses).
  </Tab>

  <Tab title="API or SDK">
    Point an OpenAI-compatible client at Fireworks and choose a model:

    ```bash wrap theme={null}
    pip install openai
    export FIREWORKS_API_KEY="YOUR_FIREWORKS_API_KEY"
    ```

    ```python wrap theme={null}
    import os

    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.responses.create(
        model="glm-latest",
        input="Review this pull request.",
    )

    print(response.output_text)
    ```

    Fireworks also supports Chat Completions and Anthropic Messages. See [APIs and SDKs](/nexus/apis-and-sdks).
  </Tab>

  <Tab title="LLM gateway">
    Keep your existing gateway and configure its Fireworks provider. For LiteLLM, create `config.yaml`:

    ```yaml theme={null}
    model_list:
      - model_name: glm-latest
        litellm_params:
          model: fireworks_ai/glm-latest
          api_key: os.environ/FIREWORKS_API_KEY
          api_base: https://api.fireworks.ai/inference/v1
    ```

    Start the proxy:

    ```bash wrap theme={null}
    pip install "litellm[proxy]"
    export FIREWORKS_API_KEY="YOUR_FIREWORKS_API_KEY"
    litellm --config config.yaml
    ```

    In another terminal, send a request:

    ```bash wrap theme={null}
    curl http://localhost:4000/chat/completions \
      -H "Content-Type: application/json" \
      -d '{
        "model": "glm-latest",
        "messages": [{"role": "user", "content": "Say pong in one word."}]
      }'
    ```

    Provider names, key configuration, and model catalogs vary by gateway. See [LLM Gateways](/nexus/llm-gateways).
  </Tab>
</Tabs>

## Choose models or manage usage and spend

<CardGroup>
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
    Set per-user caps for supported Fireworks serverless models, with account defaults, group limits, and user exceptions.
  </Card>
</CardGroup>
