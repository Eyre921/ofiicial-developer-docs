---
title: "Microsoft Foundry"
source: https://docs.fireworks.ai/ecosystem/integrations/azure-foundry
path: ecosystem/integrations/azure-foundry
---

Deploy frontier open models inside your Azure subscription, billed through Azure.

Fireworks AI is a first-party inference provider inside Microsoft Foundry. You can access frontier open models through your existing Azure account, with usage billed through Azure and counting toward your Microsoft Azure Consumption Commitment (MACC).

This page covers the Fireworks side of the integration. For Azure portal setup steps, see the [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models).

<Info>
  **New to Fireworks?** Foundry users get the same OpenAI-compatible API and model catalog as direct Fireworks customers. Start with the [PayGo quickstart](#paygo-quickstart) below — you can be making requests in about 10 minutes.
</Info>

## Prerequisites

* An active Azure subscription
* The Fireworks integration enabled at the subscription level (see below)
* A Microsoft Foundry project with the **Azure AI Developer** role assigned

### Opt-in

Fireworks on Foundry requires a one-time opt-in per Azure subscription before you can create deployments. Follow the steps in the [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models#enable-fireworks-on-foundry).

## Deployment modes

Fireworks on Foundry supports three deployment modes.

| Mode              | Also called                    | Pricing                           | Regions              | Right for                                    |
| ----------------- | ------------------------------ | --------------------------------- | -------------------- | -------------------------------------------- |
| **PayGo**         | Serverless, Data Zone Standard | Per token, MACC-eligible          | US Data Zone only    | Prototyping, low-volume workloads            |
| **PTU**           | Provisioned Throughput         | Per PTU-hour, ACD + MACC eligible | Global               | Production workloads with consistent traffic |
| **Custom Models** | Bring Your Own Model           | PTU pricing                       | Global (PTU regions) | Fine-tuned model deployment                  |

PTU deployments can be created directly in the Azure portal. For help with PTU sizing on Fireworks models, contact [sales@fireworks.ai](mailto:sales@fireworks.ai).

## Available models

All models use the OpenAI-compatible chat completions API and are added to the catalog on a rolling basis. For the current list of available models, see the [Microsoft Learn catalog](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models#available-catalog-models).

Chat completions only. Embeddings, image generation, and audio modalities are not available through Foundry.

## PayGo quickstart

PayGo (Data Zone Standard) is available in: East US, East US 2, Central US, North Central US, West US, West US 3.

The throughput limit for PayGo deployments is **250,000 tokens per minute (TPM)**.

### Make your first request

Foundry deployments use an OpenAI-compatible endpoint. Use your Foundry project endpoint and Azure API key.

```python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://<your-project>.services.ai.azure.com/models",
    api_key="<your-azure-api-key>",
)

response = client.chat.completions.create(
    model="fireworks-ai/FW-GLM-5.1",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)
```

Find your project endpoint in the Microsoft Foundry portal under **Project settings**.

## PTU (Provisioned Throughput)

PTU deployments provide dedicated GPU capacity reserved for your workload, with consistent throughput and global region availability.

* Dedicated capacity, not shared with other tenants
* Available globally, not limited to US Data Zone
* ACD-eligible and MACC-eligible

You can create a PTU deployment directly in the Azure portal. For more on provisioned throughput, see the [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput).

For help with PTU sizing on Fireworks models, contact [sales@fireworks.ai](mailto:sales@fireworks.ai).

## Custom Models

Fine-tune on Fireworks and deploy on Foundry, or bring your own weights from wherever you post-train to deploy on Foundry. Your model is served on Fireworks infrastructure within Azure, billed through your Azure account.

### Supported base architectures

For the list of supported custom model architectures, see the [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models#supported-model-architectures).

### Deployment

To import and deploy a custom model, follow the [Import custom models into Foundry guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models?tabs=rest-api).

## Billing

All Fireworks on Foundry usage is billed through Azure. You do not need a separate Fireworks billing account or contract.

* PayGo and PTU usage is MACC-eligible
* PTU deployments are ACD-eligible and qualify for quota retirement
* Direct Fireworks usage at [fireworks.ai](https://fireworks.ai) is billed separately and does not count toward MACC

## Troubleshooting

| Issue                           | Resolution                                                                                                                                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quota exceeded error            | Request a limit increase at [aka.ms/fireworks-quota](https://aka.ms/fireworks-quota)                                                                                                                                        |
| Access denied on deployment     | Verify you have the **Azure AI Developer** role on the project                                                                                                                                                              |
| Opt-in not propagating          | Allow up to 30 minutes after registering `Fireworks.EnableDeploy`                                                                                                                                                           |
| Custom Model deployment failing | Confirm weights are full-weight (not LoRA adapters) and the architecture is in the [supported list](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models#supported-model-architectures) |
| PTU provisioning questions      | Contact [sales@fireworks.ai](mailto:sales@fireworks.ai)                                                                                                                                                                     |

## FireConnect

Use FireConnect to route local coding harnesses through your Foundry deployments without hand-editing config files.

<Card title="FireConnect overview" icon="terminal" href="/ecosystem/fireconnect/overview#fireworks-on-microsoft-foundry">
  Configure `--provider azure`, then run `fireconnect opencode on`, `fireconnect codex on`, or `fireconnect pi on --main <deployment-name>`
</Card>

Supported harnesses for Foundry: **OpenCode**, **Codex**, and **Pi**. Claude Code, Cursor, and VS Code require direct Fireworks routing.

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --harnesses opencode,codex,pi

fireconnect opencode on --main FW-GLM-5.1
```

See [Fireworks on Microsoft Foundry in FireConnect](/ecosystem/fireconnect/overview#fireworks-on-microsoft-foundry) for deployment names, one-off `--azure` routing, and switching back to direct Fireworks.

## Additional resources

* [Enable Fireworks on Foundry (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models)
* [Microsoft Foundry portal](https://ai.azure.com/)
* [Fireworks fine-tuning docs](/fine-tuning/finetuning-intro)
* [Fireworks Trust Center](https://fireworks.ai/trust)
* [sales@fireworks.ai](mailto:sales@fireworks.ai) for PTU provisioning and Custom Model support
