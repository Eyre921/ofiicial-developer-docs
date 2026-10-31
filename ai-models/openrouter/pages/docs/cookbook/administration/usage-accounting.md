---
title: "Usage Accounting"
source: https://openrouter.ai/docs/cookbook/administration/usage-accounting.md
path: docs/cookbook/administration/usage-accounting
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage Accounting

The OpenRouter API provides built-in **Usage Accounting** that allows you to track AI model usage without making additional API calls. This feature provides detailed information about token counts, costs, and caching status directly in your API responses.

## Usage Information

OpenRouter automatically returns detailed usage information with every response, including:

1. Input and output token counts using the model's native tokenizer
2. Cost in credits
3. Reasoning token counts (if applicable)
4. Cached token counts (if available)

This information is included in the terminal `response.completed` or `response.incomplete` event for streaming responses, or in the terminal response for non-streaming requests. No additional parameters are required. The examples on this page use the [Responses API](https://openrouter.ai/docs/api_reference/responses/overview.md).

> [!NOTE]
>
> **Deprecated Parameters**
>
> On Chat Completions, the `usage: { include: true }` and `stream_options: { include_usage: true }` parameters are deprecated and have no effect. The Responses API has no equivalent parameter. Full usage details are always included automatically in every response on both APIs.

## Response Format

Every response includes a `usage` object with detailed token information. The field names follow the API you call.

### Responses API

```json lines theme={null}
{
  "object": "response",
  "usage": {
    "input_tokens": 194,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 100
    },
    "output_tokens": 2,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 196,
    "cost": 0.95,
    "is_byok": false,
    "cost_details": {
      "upstream_inference_cost": null,
      "upstream_inference_input_cost": 18,
      "upstream_inference_output_cost": 1
    }
  }
}
```

### Chat Completions

```json lines theme={null}
{
  "object": "chat.completion.chunk",
  "usage": {
    "completion_tokens": 2,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "cost": 0.95,
    "cost_details": {
      "upstream_inference_cost": 19
    },
    "prompt_tokens": 194,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 100,
      "audio_tokens": 0
    },
    "total_tokens": 196
  }
}
```

`cached_tokens` is the number of tokens that were *read* from the cache. `cache_write_tokens` is the number of tokens that were *written* to the cache (only returned for models with explicit caching and cache write pricing).

## Cost Breakdown

The usage response includes detailed cost information:

* `cost`: The total amount charged to your account
* `cost_details.upstream_inference_cost`: The actual cost charged by the upstream AI provider, split into `upstream_inference_input_cost` and `upstream_inference_output_cost` on the Responses API (`upstream_inference_prompt_cost` and `upstream_inference_completions_cost` on Chat Completions)

## Benefits

1. **Efficiency**: Get usage information without making separate API calls
2. **Accuracy**: Token counts are calculated using the model's native tokenizer
3. **Transparency**: Track costs and cached token usage in real-time
4. **Detailed Breakdown**: Separate counts for input, output, reasoning, and cached tokens

## Best Practices

1. Use the usage data to monitor token consumption and costs
2. Consider tracking usage in development to optimize token usage before production
3. Use the cached token information to optimize your application's performance

## Alternative: Getting Usage via Generation ID

You can also retrieve usage information asynchronously by using the generation ID returned from your API calls. This is particularly useful when you want to fetch usage statistics after the completion has finished or when you need to audit historical usage.

To use this method:

1. Make your Responses API request as normal
2. Note the `id` field in the response
3. Use that ID to fetch usage information via the `/generation` endpoint

For more details on this approach, see the [Get a Generation](https://openrouter.ai/docs/api/api-reference/generations/get-request-&-usage-metadata-for-a-generation.md) documentation.

> [!NOTE]
>
> When obtaining usage information via generation ID, the `upstream_inference_cost` field is only available for BYOK (Bring Your Own Key) requests. For all other requests it will be 0 or null.

## Examples

### Basic Usage with Token Tracking

### Streaming with Usage Information

This example shows how to handle usage information in streaming mode:

