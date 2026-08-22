---
title: "Supported models"
source: https://docs.together.ai/docs/evaluations-supported-models
path: docs/evaluations-supported-models
---

Serverless models and external provider shortcuts supported by the evaluations API.

The evaluations API supports three model sources for both the judge and the models being evaluated: Together AI serverless models, your own dedicated model inference endpoints, and external provider models. Set the `model_source` field to choose between them.

## Serverless models

Set `model_source = "serverless"` to use Together AI serverless inference.

The evaluations service keeps its own allowlist of serverless models, separate from the full [serverless catalog](/docs/serverless/models). The models below can serve as the judge or as the model being evaluated; this table syncs daily from the allowlist.

| Model                              | Model ID                                  |
| :--------------------------------- | :---------------------------------------- |
| LFM2-24B-A2B                       | `LiquidAI/LFM2-24B-A2B`                   |
| MiniMax-M2.7                       | `MiniMaxAI/MiniMax-M2.7`                  |
| Qwen3-235B-A22B-Instruct-2507-tput | `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` |
| Qwen3-Coder-480B-A35B-Instruct-FP8 | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` |
| Qwen3-Coder-Next-FP8               | `Qwen/Qwen3-Coder-Next-FP8`               |
| Qwen3.5-397B-A17B                  | `Qwen/Qwen3.5-397B-A17B`                  |
| Qwen3.5 9B FP8                     | `Qwen/Qwen3.5-9B`                         |
| Qwen3.6 Plus                       | `Qwen/Qwen3.6-Plus`                       |
| Cogito v2.1 671B                   | `deepcogito/cogito-v2-1-671b`             |
| DeepSeek-R1                        | `deepseek-ai/DeepSeek-R1`                 |
| DeepSeek-V3.1                      | `deepseek-ai/DeepSeek-V3.1`               |
| Deepseek V4 Pro                    | `deepseek-ai/DeepSeek-V4-Pro`             |
| rnj-1-instruct                     | `essentialai/rnj-1-instruct`              |
| Gemma 3N E4B Instruct              | `google/gemma-3n-E4B-it`                  |
| Gemma 4 31B-it FP8                 | `google/gemma-4-31B-it`                   |
| Meta Llama 3.3 70B Instruct Turbo  | `meta-llama/Llama-3.3-70B-Instruct-Turbo` |
| Kimi-K2.5                          | `moonshotai/Kimi-K2.5`                    |
| Kimi-K2.6                          | `moonshotai/Kimi-K2.6`                    |
| OpenAI GPT-OSS 120B                | `openai/gpt-oss-120b`                     |
| OpenAI GPT-OSS 20B                 | `openai/gpt-oss-20b`                      |
| GLM-5                              | `zai-org/GLM-5`                           |
| GLM-5.1                            | `zai-org/GLM-5.1`                         |

**Example configuration:**

```python Python theme={null}
model_config = {
    "model": "deepseek-ai/DeepSeek-V4-Pro",
    "model_source": "serverless",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

### Vision-capable models

To evaluate image inputs, use a serverless model that accepts images, such as the Qwen VL family. The evaluated model, and the judge if it should also see the image, must be vision-capable. Browse the [serverless models](/docs/serverless/models) catalog to find models that support vision, and see [the evaluations page](/docs/ai-evaluations#prepare-a-dataset) for how to add images to a dataset.

## Dedicated models

To evaluate a model served on [dedicated model inference](/docs/dedicated-endpoints/overview), set `model_source = "dedicated"` and enter the endpoint ID (`ep_abc123`, from the deploy output or `tg beta endpoints ls`) in the `model` field. The endpoint must have a running deployment; requests fail with `endpoint_not_ready` while it is stopped.

In the [evaluations console](https://api.together.ai/evaluations), live dedicated model inference endpoints appear under **My Endpoints** in the model picker. Legacy dedicated endpoints appear under **My Legacy Endpoints**. Only endpoints with at least one live deployment are listed. Selecting an endpoint sets `model_source` to `dedicated` and uses the endpoint name as `model`.

**Example configuration:**

```python Python theme={null}
model_config = {
    "model": "<ENDPOINT_ID>",
    "model_source": "dedicated",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

## External models

Set `model_source = "external"` to use models from external providers.

<Warning>
  External models require an API token from the provider. Set the `external_api_token` parameter with the provider's API key.
</Warning>

### Supported shortcuts

Use these shortcuts in the `model` field, and the API resolves the provider base URL automatically.

| Provider  | Model                  | Model ID                        |
| :-------- | :--------------------- | :------------------------------ |
| Anthropic | Claude Haiku 4.5       | `anthropic/claude-haiku-4-5`    |
| Anthropic | Claude Opus 4.5        | `anthropic/claude-opus-4-5`     |
| Anthropic | Claude Opus 4.6        | `anthropic/claude-opus-4-6`     |
| Anthropic | Claude Opus 4.7        | `anthropic/claude-opus-4-7`     |
| Anthropic | Claude Sonnet 4.5      | `anthropic/claude-sonnet-4-5`   |
| Anthropic | Claude Sonnet 4.6      | `anthropic/claude-sonnet-4-6`   |
| Google    | Gemini 2.5 Flash       | `google/gemini-2.5-flash`       |
| Google    | Gemini 2.5 Flash Lite  | `google/gemini-2.5-flash-lite`  |
| Google    | Gemini 2.5 Pro         | `google/gemini-2.5-pro`         |
| Google    | Gemini 3 Flash Preview | `google/gemini-3-flash-preview` |
| Google    | Gemini 3 Pro Preview   | `google/gemini-3-pro-preview`   |
| Google    | Gemini 3.1 Flash Lite  | `google/gemini-3.1-flash-lite`  |
| Google    | Gemini 3.1 Pro Preview | `google/gemini-3.1-pro-preview` |
| OpenAI    | GPT-4.1                | `openai/gpt-4.1`                |
| OpenAI    | GPT-4.1 Mini           | `openai/gpt-4.1-mini`           |
| OpenAI    | GPT-4.1 Nano           | `openai/gpt-4.1-nano`           |
| OpenAI    | GPT-4o                 | `openai/gpt-4o`                 |
| OpenAI    | GPT-4o Mini            | `openai/gpt-4o-mini`            |
| OpenAI    | GPT-5.3 Chat Latest    | `openai/gpt-5.3-chat-latest`    |
| OpenAI    | GPT-5.4                | `openai/gpt-5.4`                |
| OpenAI    | GPT-5.4 Mini           | `openai/gpt-5.4-mini`           |
| OpenAI    | GPT-5.4 Nano           | `openai/gpt-5.4-nano`           |
| OpenAI    | GPT-5.5                | `openai/gpt-5.5`                |
| OpenAI    | o3                     | `openai/o3`                     |
| OpenAI    | o4-mini                | `openai/o4-mini`                |

**Example configuration with a shortcut:**

```python Python theme={null}
import os

model_config = {
    "model": "openai/gpt-5.5",
    "model_source": "external",
    "external_api_token": os.environ["OPENAI_API_KEY"],
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

### Custom base URL

To use any OpenAI `chat/completions`-compatible API, specify a custom `external_base_url`:

```python Python theme={null}
import os

model_config = {
    "model": "mistral-small-latest",
    "model_source": "external",
    "external_api_token": os.environ["MISTRAL_API_KEY"],
    "external_base_url": "https://api.mistral.ai/",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

<Note>
  The external API must be [OpenAI `chat/completions`-compatible](/docs/inference/openai-compatibility).
</Note>
