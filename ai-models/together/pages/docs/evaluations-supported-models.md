---
title: "Supported models"
source: https://docs.together.ai/docs/evaluations-supported-models
path: docs/evaluations-supported-models
---

Supported models for Evaluations

This page lists all supported model sources for the Evaluations API. You can use serverless models, dedicated endpoints, or external models from providers like OpenAI, Anthropic, and Google.

## Serverless models

Set `model_source = "serverless"` to use Together's serverless inference.

<Info>
  Any Together serverless model that supports [structured outputs](/docs/inference/chat/structured-outputs) can be used.
</Info>

### Supported models

| Model                              | Model ID                                  |
| :--------------------------------- | :---------------------------------------- |
| DeepSeek-R1                        | `deepseek-ai/DeepSeek-R1`                 |
| DeepSeek-V3.1                      | `deepseek-ai/DeepSeek-V3.1`               |
| DeepSeek-V4 Pro                    | `deepseek-ai/DeepSeek-V4-Pro`             |
| Llama 3.3 70B Instruct Turbo       | `meta-llama/Llama-3.3-70B-Instruct-Turbo` |
| LFM2 24B A2B                       | `LiquidAI/LFM2-24B-A2B`                   |
| MiniMax M2.7                       | `MiniMaxAI/MiniMax-M2.7`                  |
| Kimi K2.5                          | `moonshotai/Kimi-K2.5`                    |
| Kimi K2.6                          | `moonshotai/Kimi-K2.6`                    |
| Qwen3 235B A22B Instruct 2507      | `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` |
| Qwen3 Coder 480B A35B Instruct FP8 | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` |
| Qwen3 Coder Next FP8               | `Qwen/Qwen3-Coder-Next-FP8`               |
| Qwen 3.5 397B A17B                 | `Qwen/Qwen3.5-397B-A17B`                  |
| Qwen 3.5 9B                        | `Qwen/Qwen3.5-9B`                         |
| Qwen 3.6 Plus                      | `Qwen/Qwen3.6-Plus`                       |
| Gemma 3n E4B                       | `google/gemma-3n-E4B-it`                  |
| Gemma 4 31B                        | `google/gemma-4-31B-it`                   |
| Cogito V2 1 671B                   | `deepcogito/cogito-v2-1-671b`             |
| Essential AI RNJ-1                 | `essentialai/rnj-1-instruct`              |
| GLM-5                              | `zai-org/GLM-5`                           |
| GLM-5.1                            | `zai-org/GLM-5.1`                         |
| GPT OSS 20B                        | `openai/gpt-oss-20b`                      |
| GPT OSS 120B                       | `openai/gpt-oss-120b`                     |

**Example configuration:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "deepseek-ai/DeepSeek-V3.1",
    "model_source": "serverless",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

## Dedicated models

Set `model_source = "dedicated"` to use your own dedicated endpoint.

<Info>
  A user-launched [dedicated endpoint](/docs/dedicated-endpoints/overview) must be created before running evaluations. After launching an endpoint, copy-paste the endpoint ID into the `model` field.
</Info>

**Example configuration:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "your-endpoint-id",
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
  External models require an API token from the respective provider. Set the `external_api_token` parameter with your provider's API key.
</Warning>

### Supported shortcuts

Use these shortcuts in the `model` field - the API base URL will be determined automatically:

| Provider  | Model Name             | Model String for API            |
| :-------- | :--------------------- | :------------------------------ |
| OpenAI    | GPT-5.5                | `openai/gpt-5.5`                |
| OpenAI    | GPT-5.4                | `openai/gpt-5.4`                |
| OpenAI    | GPT-5.4 Mini           | `openai/gpt-5.4-mini`           |
| OpenAI    | GPT-5.4 Nano           | `openai/gpt-5.4-nano`           |
| OpenAI    | GPT-5.3 Chat Latest    | `openai/gpt-5.3-chat-latest`    |
| OpenAI    | GPT-4.1                | `openai/gpt-4.1`                |
| OpenAI    | GPT-4.1 Mini           | `openai/gpt-4.1-mini`           |
| OpenAI    | GPT-4.1 Nano           | `openai/gpt-4.1-nano`           |
| OpenAI    | GPT-4o                 | `openai/gpt-4o`                 |
| OpenAI    | GPT-4o Mini            | `openai/gpt-4o-mini`            |
| OpenAI    | o4-mini                | `openai/o4-mini`                |
| OpenAI    | o3                     | `openai/o3`                     |
| Anthropic | Claude Opus 4.7        | `anthropic/claude-opus-4-7`     |
| Anthropic | Claude Opus 4.6        | `anthropic/claude-opus-4-6`     |
| Anthropic | Claude Opus 4.5        | `anthropic/claude-opus-4-5`     |
| Anthropic | Claude Sonnet 4.6      | `anthropic/claude-sonnet-4-6`   |
| Anthropic | Claude Sonnet 4.5      | `anthropic/claude-sonnet-4-5`   |
| Anthropic | Claude Haiku 4.5       | `anthropic/claude-haiku-4-5`    |
| Google    | Gemini 3.1 Pro Preview | `google/gemini-3.1-pro-preview` |
| Google    | Gemini 3.1 Flash Lite  | `google/gemini-3.1-flash-lite`  |
| Google    | Gemini 3 Pro Preview   | `google/gemini-3-pro-preview`   |
| Google    | Gemini 3 Flash Preview | `google/gemini-3-flash-preview` |
| Google    | Gemini 2.5 Pro         | `google/gemini-2.5-pro`         |
| Google    | Gemini 2.5 Flash       | `google/gemini-2.5-flash`       |
| Google    | Gemini 2.5 Flash Lite  | `google/gemini-2.5-flash-lite`  |

**Example configuration with shortcut:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "openai/gpt-5",
    "model_source": "external",
    "external_api_token": "your-openai-api-key",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

### Custom base URL

You can also use any OpenAI `chat/completions`-compatible API by specifying a custom `external_base_url`:

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "mistral-small-latest",
    "model_source": "external",
    "external_api_token": "your-mistral-api-key",
    "external_base_url": "https://api.mistral.ai/",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

<Info>
  The external API must be [OpenAI `chat/completions`-compatible](https://docs.together.ai/docs/inference/openai-compatibility).
</Info>
