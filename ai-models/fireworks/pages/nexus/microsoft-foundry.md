---
title: "Microsoft Foundry"
source: https://docs.fireworks.ai/nexus/microsoft-foundry
path: nexus/microsoft-foundry
---

Route FireConnect harnesses through Fireworks models deployed in your Azure subscription

FireConnect can route supported harnesses through a Fireworks model deployed in your Azure subscription. Azure bills this usage, and it counts toward your Microsoft Azure Consumption Commitment where applicable.

Before configuring FireConnect, open [Microsoft Foundry](/ecosystem/integrations/azure-foundry) to enable Fireworks and create a deployment.

<Note>
  **CLI terminology:** The Foundry provider is `--provider azure`, or `--azure` when you connect one harness. Harness configs display the label **Fireworks on Microsoft Foundry**. With Foundry, `--model` is your Azure deployment name, such as `FW-GLM-5.2`, not a Fireworks serverless ID such as `glm-fast-latest`.
</Note>

## Requirements

* A Microsoft Foundry resource with a Fireworks model deployment
* The resource endpoint and Azure API key
* FireConnect installed

See [Coding Harnesses](/nexus/harnesses#foundry-across-harnesses) for current compatibility.

<Warning>
  Use an **Azure API key** from Foundry, not a Fireworks key (`fw_...`).

  Model routers are not available on the Foundry path. To use `--model firerouter`, first switch to the direct Fireworks gateway with `fireconnect configure --provider fireworks`.
</Warning>

## Configure Foundry as the default

Set the Foundry endpoint once. New connections for supported harnesses use it until you change the default provider.

```bash wrap theme={null}
export AZURE_API_KEY="YOUR_AZURE_API_KEY"

fireconnect configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com"
```

If no Azure key is configured, FireConnect stores an `{env:AZURE_API_KEY}` reference. To store the current value literally, add:

```bash wrap theme={null}
fireconnect configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key "$AZURE_API_KEY"
```

## Connect a harness

Use the deployment name from Foundry:

```bash wrap theme={null}
fireconnect <harness> --model <deployment-name>
fireconnect opencode --model FW-GLM-5.2
```

If you omit `--model`, FireConnect defaults to `FW-GLM-5.2`.

### Accepted endpoint formats

Pass any of these Foundry URLs to `--base-url`. FireConnect converts it to `https://<resource>.services.ai.azure.com/openai/v1`:

* Bare resource root (`https://<resource>.services.ai.azure.com`)
* Portal **project endpoint** (`.../api/projects/<name>`)
* Foundry **Models** route (`.../models`)
* A complete OpenAI-compatible base URL (`.../openai/v1`)

Find the endpoint in the Microsoft Foundry portal under **Project settings**.

## Route one command through Foundry

Route a single harness through Foundry without changing global config:

```bash wrap theme={null}
fireconnect opencode \
  --azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key $AZURE_API_KEY \
  --model FW-MiniMax-M2.5
```

If global config already has a Foundry endpoint, `--azure` alone reuses it:

```bash wrap theme={null}
fireconnect cursor --azure --model FW-GLM-5.2
```

FireConnect keeps Foundry configuration separate from direct Fireworks configuration. `fireconnect <harness> status` reports the provider, endpoint, and model. See [Coding Harnesses](/nexus/harnesses) for files changed and restore behavior.

<Note>
  `fireconnect model list` shows the Fireworks serverless catalog, not Foundry deployments. Enter a Foundry deployment name with `--model`.
</Note>

## Claude Code through a gateway

Direct FireConnect routing does not support Claude Code on Foundry. To use Claude Code with a Foundry deployment, run an LLM gateway between Claude Code and Foundry. The gateway translates between the Anthropic Messages format that Claude Code sends and the OpenAI-compatible format that Foundry expects. FireConnect does not configure this path.

Two patterns are in production use:

* **Claude Code to Envoy AI Gateway to Foundry.** Point `ANTHROPIC_BASE_URL` at the gateway. You keep your Claude Code install unchanged. The gateway renames fields, maps tool schemas, reframes streams, and injects the Azure key, the deployment name, and a shared prompt cache key.
* **Claude Code to LiteLLM to Foundry.** Point Claude Code at LiteLLM and configure Foundry as the upstream provider. See [LLM Gateways](/nexus/llm-gateways) for LiteLLM setup.

Reference implementation for the Envoy path with GLM 5.2 on Foundry:

* [Claude Code on Foundry with Fireworks models](https://github.com/ganac-tech/Claude-code-on-foundry-FW-Open-Source-Models) (gateway config, demos, and cache measurement scripts)

Keep the Azure key in the gateway config. Do not paste it into Claude Code. Model routers stay unavailable on the Foundry path, including through a gateway.

## Switch or disconnect

| Goal                                                | Commands                                                                   |
| --------------------------------------------------- | -------------------------------------------------------------------------- |
| Return a supported harness to the Fireworks gateway | `fireconnect configure --provider fireworks`, then `fireconnect <harness>` |
| Remove FireConnect from one harness                 | `fireconnect <harness> off`                                                |
| Restore all harnesses and remove FireConnect        | `fireconnect uninstall`                                                    |

You do not need to run `off` before reconnecting through Fireworks. The saved Azure endpoint and key remain available if you switch back later.

`off` does not change the global provider. If the provider remains `azure`, the next connection for a supported harness will use Foundry again.

## Verify routing

```bash wrap theme={null}
fireconnect <harness> status
```

Confirm that the provider is `azure` and that the endpoint and deployment name are correct.

## Related documentation

* [Coding Harnesses](/nexus/harnesses)
* [Microsoft Foundry](/ecosystem/integrations/azure-foundry)
* [CLI Reference](/nexus/cli-reference)
