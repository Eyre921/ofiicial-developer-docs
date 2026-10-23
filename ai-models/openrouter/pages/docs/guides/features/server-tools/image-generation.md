---
title: "Image Generation"
source: https://openrouter.ai/docs/guides/features/server-tools/image-generation.md
path: docs/guides/features/server-tools/image-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation

> Generate images from text prompts with any model

Beta

> [!NOTE]
>
> **Beta**
>
> Server tools are currently in beta. The API and behavior may change.

The `openrouter:image_generation` server tool enables any model to generate images from text prompts. When the model determines it needs to create an image, it calls the tool with a description. OpenRouter executes the image generation and returns the result to the model.

## How It Works

1. You include `{ "type": "openrouter:image_generation" }` in your `tools` array.
2. Based on the user's request, the model decides whether image generation is needed and crafts a prompt.
3. OpenRouter generates the image using the configured model (defaults to `openai/gpt-5-image`).
4. The generated image URL is returned to the model.
5. The model incorporates the image into its response. It may generate multiple images in a single request if needed.

## Quick Start

## Configuration

The image generation tool accepts optional `parameters` to customize the output:

```json lines theme={null}
{
  "type": "openrouter:image_generation",
  "parameters": {
    "model": "openai/gpt-5-image",
    "quality": "high",
    "aspect_ratio": "16:9",
    "size": "1024x1024",
    "background": "transparent",
    "output_format": "png"
  }
}
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `model` | string | `openai/gpt-5-image` | Which image generation model to use. See [available image models](https://openrouter.ai/models?output_modalities=image). |
| `quality` | string | N/A | Image quality level (model-dependent, e.g. `"low"`, `"medium"`, `"high"`) |
| `size` | string | N/A | Image dimensions (e.g. `"1024x1024"`, `"512x512"`) |
| `aspect_ratio` | string | N/A | Aspect ratio (e.g. `"16:9"`, `"1:1"`, `"4:3"`) |
| `background` | string | N/A | Background style (e.g. `"transparent"`, `"opaque"`) |
| `output_format` | string | N/A | Output format (e.g. `"png"`, `"jpeg"`, `"webp"`) |
| `output_compression` | number | N/A | Compression level (0-100) for lossy formats |
| `moderation` | string | N/A | Content moderation level (e.g. `"auto"`, `"low"`) |

All parameters except `model` are passed directly to the underlying image generation API. Available options depend on the specific model being used.

## Response

When the model calls the image generation tool, it receives a response like:

```json lines theme={null}
{
  "status": "ok",
  "imageUrl": "https://..."
}
```

If generation fails, the response includes an error:

```json lines theme={null}
{
  "status": "error",
  "error": "Generation failed due to content policy"
}
```

## Works with the Responses API

The image generation server tool also works with the Responses API:

## Pricing

Image generation pricing depends on the underlying model used:

* **openai/gpt-5-image** (default): See [model page](https://openrouter.ai/openai/gpt-5-image)
* **openai/gpt-5-image-mini**: See [model page](https://openrouter.ai/openai/gpt-5-image-mini)
* **openai/gpt-5.4-image-2**: See [model page](https://openrouter.ai/openai/gpt-5.4-image-2)
* Other models: See the [image models list](https://openrouter.ai/models?output_modalities=image) on OpenRouter

The cost is in addition to standard LLM token costs for processing the request and response.

## Next Steps

* [Server Tools Overview](https://openrouter.ai/docs/guides/features/server-tools.md). Learn about server tools
* [Web Search](https://openrouter.ai/docs/guides/features/server-tools/web-search.md). Search the web for real-time information
* [Datetime](https://openrouter.ai/docs/guides/features/server-tools/datetime.md). Get the current date and time
* [Tool Calling](https://openrouter.ai/docs/guides/features/tool-calling.md). Learn about user-defined tool calling

