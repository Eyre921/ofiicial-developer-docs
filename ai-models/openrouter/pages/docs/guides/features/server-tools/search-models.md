---
title: "Search Models"
source: https://openrouter.ai/docs/guides/features/server-tools/search-models.md
path: docs/guides/features/server-tools/search-models
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Models

> Let any model search the OpenRouter model catalog

Beta

> [!NOTE]
>
> **Beta**
>
> Server tools are currently in beta. The API and behavior may change. This tool is experimental. When it graduates, the tool type is likely to be renamed (dropping the `experimental__` prefix), which would be a breaking change for requests using the current name.

The `openrouter:experimental__search_models` server tool lets a model search and filter the OpenRouter model catalog. The model can look up models by name, capabilities, modalities, and other attributes, useful for agents that pick models dynamically, for example with the [Subagent](https://openrouter.ai/docs/guides/features/server-tools/subagent.md) tool.

## Quick Start

## Configuration

The search models tool accepts an optional `max_results` parameter:

```json lines theme={null}
{
  "type": "openrouter:experimental__search_models",
  "parameters": {
    "max_results": 5
  }
}
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `max_results` | integer | `5` | Maximum number of models to return per call. Between 1 and 20 |

### Call Arguments

The model generates the search arguments. All fields are optional; an empty call browses the full catalog:

| Field | Type | Description |
| - | - | - |
| `query` | string | Free-text search matched against model names, slugs, and descriptions |
| `input_modalities` | string\[] | Filter by supported input modalities (`text`, `image`, `file`, `audio`, `video`). Returns models that support ALL specified modalities |
| `output_modalities` | string\[] | Filter by supported output modalities (e.g. `text`, `image`, `embeddings`, `audio`). Returns models that support ALL specified modalities |
| `min_context_length` | integer | Minimum context length in tokens |
| `series` | string | Filter by model series/family group (e.g. `Claude`, `GPT`, `Gemini`) |

## Response

The tool returns matching models with their key attributes:

```json lines theme={null}
{
  "models": [
    {
      "id": "anthropic/claude-sonnet-4.5",
      "name": "Anthropic: Claude Sonnet 4.5",
      "description": "...",
      "context_length": 1000000,
      "input_modalities": ["text", "image", "file"],
      "output_modalities": ["text"],
      "series": "Claude"
    }
  ],
  "total_results": 12,
  "showing": 1
}
```

`total_results` is the number of models that matched the filters; `showing` is how many were returned after applying `max_results`.

## Pricing

There is currently no separate charge for the search models tool; you pay only for standard token usage.

## Next Steps

* [Server Tools Overview](https://openrouter.ai/docs/guides/features/server-tools.md). Learn about server tools
* [Subagent](https://openrouter.ai/docs/guides/features/server-tools/subagent.md). Delegate tasks to a worker model
* [Models](https://openrouter.ai/docs/guides/overview/models.md). Learn about the OpenRouter model catalog

