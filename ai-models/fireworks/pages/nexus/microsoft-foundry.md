---
title: "Foundry for Coding Harnesses"
source: https://docs.fireworks.ai/nexus/microsoft-foundry
path: nexus/microsoft-foundry
---

Use Fireworks models deployed in Microsoft Foundry from Claude Code, OpenCode, Cursor IDE, VS Code, and other coding harnesses, through FireConnect, manual setup, or an LLM gateway.

Use Fireworks models deployed in your Azure subscription from the coding harness you already use. Azure bills this usage, and it counts toward your Microsoft Azure Consumption Commitment where applicable.

Before you start, [enable Fireworks in Microsoft Foundry](/ecosystem/integrations/azure-foundry) and create a deployment, such as `FW-GLM-5.2`. You need:

* The Foundry resource endpoint, such as `https://YOUR_RESOURCE.services.ai.azure.com`
* An **Azure API key** from Foundry, not a Fireworks key (`fw_...`)
* The deployment name

## Choose a path

| Path                                          | Best for                                           | Harnesses                                                |
| --------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| [FireConnect](#connect-with-fireconnect)      | The quickest setup, with restore                   | OpenCode, Pi, Cursor IDE, VS Code                        |
| [Manual setup](#configure-a-harness-manually) | Harnesses with a custom OpenAI-compatible provider | Any harness that accepts a base URL, key, and model name |
| [LLM gateway](#use-an-llm-gateway)            | Claude Code, or central key management             | Claude Code and any harness your gateway supports        |

| Harness                                    | FireConnect                    | Manual setup                   | LLM gateway                                                          |
| ------------------------------------------ | ------------------------------ | ------------------------------ | -------------------------------------------------------------------- |
| OpenCode, Pi, Cursor IDE, VS Code          | Supported                      | Supported                      | Supported                                                            |
| Codex CLI, Codex app, ChatGPT desktop      | Not supported by current Codex | Not supported by current Codex | Needs a gateway that serves the Responses API                        |
| Claude Code                                | Not supported                  | Not supported                  | [Supported, with format translation](#claude-code-through-a-gateway) |
| DeepSeek Harness, Copilot App, Copilot CLI | Not supported                  | Depends on the harness         | Depends on the harness                                               |

Foundry serves Fireworks models through an OpenAI-compatible Chat Completions API. Claude Code sends Anthropic Messages requests, so it needs a gateway that translates between the two formats. Current Codex releases send only Responses API requests and reject `wire_api = "chat"` in `config.toml`, which is what FireConnect writes for Codex on Foundry.

<Warning>
  FireRouter is not available on Foundry, including through a gateway. To use
  `--model firerouter`, switch back to direct Fireworks first with
  `fireconnect configure --provider fireworks`. See [FireRouter](/nexus/firerouter).
</Warning>

## Connect with FireConnect

FireConnect writes the Foundry endpoint, key, and deployment into supported harnesses and restores the original settings with `off`.

<Steps>
  <Step title="Set Foundry as the default provider">
    ```bash wrap theme={null}
    export AZURE_API_KEY="YOUR_AZURE_API_KEY"

    fireconnect configure \
      --provider azure \
      --base-url "https://YOUR_RESOURCE.services.ai.azure.com"
    ```

    If no Azure key is stored, FireConnect saves an `{env:AZURE_API_KEY}` reference. To store the current value, add `--api-key "$AZURE_API_KEY"`.
  </Step>

  <Step title="Connect a harness with your deployment name">
    ```bash wrap theme={null}
    fireconnect opencode --model FW-GLM-5.2
    ```

    With Foundry, `--model` is your Azure deployment name, not a Fireworks serverless ID such as `glm-latest`. If you omit `--model`, FireConnect uses `FW-GLM-5.2`.
  </Step>

  <Step title="Verify">
    ```bash wrap theme={null}
    fireconnect opencode status
    ```

    Confirm that the provider is `azure` and that the endpoint and deployment name are correct. Harness configs show the label **Fireworks on Microsoft Foundry**.
  </Step>
</Steps>

To route one harness through Foundry without changing the default provider, add `--azure`:

```bash wrap theme={null}
fireconnect opencode \
  --azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key "$AZURE_API_KEY" \
  --model FW-MiniMax-M2.5
```

If a Foundry endpoint is already configured, `--azure` alone reuses it: `fireconnect cursor --azure --model FW-GLM-5.2`.

`fireconnect model list` shows the Fireworks serverless catalog, not your Foundry deployments. Enter the deployment name with `--model`.

### Accepted endpoint formats

Pass any of these Foundry URLs to `--base-url`. FireConnect converts it to `https://<resource>.services.ai.azure.com/openai/v1`:

* Bare resource root (`https://<resource>.services.ai.azure.com`)
* Portal **project endpoint** (`.../api/projects/<name>`)
* Foundry **Models** route (`.../models`)
* A complete OpenAI-compatible base URL (`.../openai/v1`)

Find the endpoint in the Microsoft Foundry portal under **Project settings**.

### Switch or disconnect

| Goal                                         | Commands                                                                   |
| -------------------------------------------- | -------------------------------------------------------------------------- |
| Return a harness to direct Fireworks         | `fireconnect configure --provider fireworks`, then `fireconnect <harness>` |
| Remove FireConnect from one harness          | `fireconnect <harness> off`                                                |
| Restore all harnesses and remove FireConnect | `fireconnect uninstall`                                                    |

`off` does not change the default provider. If it is still `azure`, the next connection uses Foundry again. The saved Azure endpoint and key remain available if you switch back later.

## Configure a harness manually

Any harness that supports a custom OpenAI-compatible provider can call Foundry directly. Use these values:

| Setting    | Value                                                   |
| ---------- | ------------------------------------------------------- |
| API format | OpenAI Chat Completions                                 |
| Base URL   | `https://YOUR_RESOURCE.services.ai.azure.com/openai/v1` |
| API key    | Your Azure API key, sent as a bearer token              |
| Model      | Your deployment name, such as `FW-GLM-5.2`              |

Check that the endpoint works before you configure the harness:

```bash wrap theme={null}
curl "https://YOUR_RESOURCE.services.ai.azure.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer $AZURE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "FW-GLM-5.2",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

Harnesses that only send Anthropic Messages or OpenAI Responses requests need a gateway instead.

## Use an LLM gateway

Put a gateway between the harness and Foundry when the harness needs a different API format, or when you want to keep the Azure key off developer machines. The gateway holds the Azure key and forwards requests to your deployment.

### Claude Code through a gateway

Claude Code sends Anthropic Messages requests, and Foundry serves Fireworks models over OpenAI Chat Completions. A gateway translates between the two, including streaming, tool calls, and reasoning blocks. Your Claude Code install stays unchanged. FireConnect does not configure this path.

<Tabs>
  <Tab title="Envoy AI Gateway">
    These steps follow the reference implementation in [Claude Code on Foundry with Fireworks models](https://github.com/ganac-tech/Claude-code-on-foundry-FW-Open-Source-Models), which includes the gateway config, a smoke test, demos, and cache measurement scripts. The gateway runs locally, with no Docker or Kubernetes.

    <Steps>
      <Step title="Get your Foundry details" icon="cloud">
        From **Project settings** in the [Foundry portal](https://ai.azure.com/), copy the endpoint and the Azure API key. You also need the deployment name, which often has a suffix such as `FW-GLM-5.2-standard`. To list your deployments:

        ```bash wrap theme={null}
        curl -s "https://YOUR_RESOURCE.services.ai.azure.com/openai/deployments?api-version=2023-03-15-preview" \
          -H "api-key: $AZURE_API_KEY"
        ```
      </Step>

      <Step title="Get the gateway and its config" icon="download">
        ```bash wrap theme={null}
        git clone https://github.com/ganac-tech/Claude-code-on-foundry-FW-Open-Source-Models
        cd Claude-code-on-foundry-FW-Open-Source-Models
        mkdir -p bin
        curl -fL -o bin/aigw \
          https://github.com/envoyproxy/ai-gateway/releases/download/v1.0.0/aigw-darwin-arm64
        chmod +x bin/aigw
        ```

        Replace `darwin-arm64` with `linux-amd64` or `linux-arm64` for your machine.
      </Step>

      <Step title="Configure" icon="file-pen">
        Copy `.env.example` to `.env` and fill in three values:

        ```bash .env theme={null}
        FOUNDRY_HOST=YOUR_RESOURCE.services.ai.azure.com
        AZURE_API_KEY=YOUR_AZURE_API_KEY
        FOUNDRY_MODEL=FW-GLM-5.2
        ```

        `FOUNDRY_MODEL` is your deployment name, and it must match `bodyMutation` in `aigw-foundry.yaml`.
      </Step>

      <Step title="Start and test the gateway" icon="play">
        ```bash wrap theme={null}
        ./start-gateway.sh
        ```

        Leave it running. In a second terminal, run `./smoke-test.sh` to check plain, streaming, and tool-call responses before you involve Claude Code.

        <Check>The smoke test reports `11 passed, 0 failed`.</Check>
      </Step>

      <Step title="Point Claude Code at the gateway" icon="terminal">
        Run `./claude-foundry.sh`, or set these values yourself:

        ```bash wrap theme={null}
        export ANTHROPIC_BASE_URL="http://localhost:1975/anthropic"
        export ANTHROPIC_AUTH_TOKEN="gateway-injected"
        export ANTHROPIC_MODEL="FW-GLM-5.2"
        claude
        ```

        The gateway adds the Azure key and the deployment name, so `ANTHROPIC_AUTH_TOKEN` is only a placeholder.
      </Step>
    </Steps>

    The gateway also sends one shared prompt cache key for every request. Keep one key for your whole team, because Claude Code's long system prompt is the same for every user.
  </Tab>

  <Tab title="LiteLLM">
    Point Claude Code at LiteLLM and configure Foundry as an OpenAI-compatible upstream, using the base URL, Azure key, and deployment name from [manual setup](#configure-a-harness-manually). LiteLLM accepts Claude Code's Messages requests and forwards them as Chat Completions. See [LLM Gateways](/nexus/llm-gateways#litellm-proxy) for LiteLLM setup.
  </Tab>
</Tabs>

### Other harnesses

Configure the gateway with Foundry as an OpenAI-compatible upstream, using the base URL, Azure key, and deployment name from [manual setup](#configure-a-harness-manually). Then point the harness at the gateway. For LiteLLM setup, see [LLM Gateways](/nexus/llm-gateways#litellm-proxy).

Keep the Azure key in the gateway config. Do not paste it into harness settings on developer machines.

## Related documentation

* [Microsoft Foundry](/ecosystem/integrations/azure-foundry): enable Fireworks and create deployments
* [Coding Harnesses](/nexus/harnesses): files FireConnect changes and restore behavior
* [CLI Reference](/nexus/cli-reference)
