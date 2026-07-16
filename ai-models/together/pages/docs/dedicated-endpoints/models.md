---
title: "Supported models"
source: https://docs.together.ai/docs/dedicated-endpoints/models
path: docs/dedicated-endpoints/models
---

View the supported models you can deploy or fine-tune for dedicated model inference.

This page lists the supported models hosted by Together AI for dedicated model inference. To upload a model you fine-tuned, see [Upload a fine-tuned model](/docs/dedicated-endpoints/custom-models).

<Tip>
  If you're not sure which model to use, check out our list of [recommended models](/docs/recommended-models) by use case.
</Tip>

## Models

The **Deployable hardware** column shows the [instance type](/docs/dedicated-endpoints/concepts#instance-type) of each model's smallest published [deployment profile](/docs/dedicated-endpoints/concepts#deployment-profile). A model may offer other profiles on different hardware. See [Pricing](/docs/dedicated-endpoints/pricing#supported-hardware) for the per-hour cost of each instance type.

<SupportedModelsTable />

## List supported models programmatically

The table above is generated from Together's model catalog. To fetch the same catalog from the command line, list the platform-supported models with `tg beta models public`. Filter by product surface (`--product`), input modality (`--modality`), or a search term (`--search`):

```bash CLI theme={null}
# All models available for dedicated inference
tg beta models public --product DEDICATED

# Narrow by modality or search term
tg beta models public --modality TEXT --search qwen
```

Add `--json` to see the full record for each model, including the `deploymentProfiles` array. Each profile is a certified model-and-config pair Together publishes for that model, so it gives you a vetted `model` and `config` that you can pass straight into [creating a deployment](/docs/dedicated-endpoints/manage#create-a-deployment).

The response looks like this:

```json theme={null}
{
  "data": [
    {
      "id": "arch_abc123",
      "name": "zai-org/GLM-5.2",
      "displayName": "GLM 5.2",
      "displayType": "chat",
      "deploymentProfiles": [
        {
          "profileId": "cfg_a",
          "certifiedConfigRevisionId": "cr_certified",
          "certifiedModelRevisionId": "rv_snap",
          "config": "projects/proj_cfg/configs/cr_certified",
          "model": "projects/proj_weights/models/ml_weight/revisions/rv_snap",
          "parallelism": "TP8",
          "gpuType": "H100",
          "gpuCount": 8
        }
      ]
    }
  ],
  "object": "list"
}
```

Each architecture includes these identity fields:

| Field         | Description                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `id`          | Architecture UID (`arch_...`). Pass to `retrieve_supported` to fetch a single entry. The catalog also accepts the architecture slug. |
| `name`        | Catalog-controlled Hugging Face model ID (for example `zai-org/GLM-5.2`).                                                            |
| `displayName` | Catalog-controlled human-readable display name (for example `GLM 5.2`).                                                              |

Each architecture also includes `displayType`, the model's category. Possible values are `chat`, `language`, `code`, `image`, `embedding`, `rerank`, `moderation`, `audio`, `video`, and `transcribe`.

Each deployment profile includes these fields:

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config`      | Resource name of the certified config revision: `projects/{project_id}/configs/{config_revision_id}`. `{project_id}` is the config's owning project, which is often a platform project rather than your project. Empty when the profile has no config pinned or its owning project is unresolved.                                                                                               |
| `model`       | Resource name of the deployable weight model for this profile (the quantization-specific build, not the architecture's base model): `projects/{project_id}/models/{model_id}[/revisions/{revision_id}]`. This field also exposes the deploy model ID, which the bare `certifiedModelRevisionId` alone does not. Empty when the profile has no model pinned or its owning project is unresolved. |
| `parallelism` | The catalog's free-form parallelism spec (for example `TP8`, `TP4`, `EP`, or `PD`). Not every value is a tensor-parallel degree.                                                                                                                                                                                                                                                                |

The bare `certifiedConfigRevisionId` and `certifiedModelRevisionId` fields remain populated alongside the resource names. Copy `config` and `model` from a profile directly into the `config` and `model` fields when you [create a deployment](/docs/dedicated-endpoints/manage#create-a-deployment).

To list the profiles published for a specific model instead, see [Choose a deployment profile](/docs/dedicated-endpoints/configs).
