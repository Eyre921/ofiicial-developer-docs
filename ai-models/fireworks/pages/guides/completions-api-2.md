---
title: "Completions API"
source: https://docs.fireworks.ai/guides/completions-api
path: guides/completions-api
---

Use the completions API for raw text generation with custom prompt templates

The completions API provides raw text generation without automatic message formatting. Use this when you need full control over prompt formatting or when working with base models.

## When to use completions

**Use the completions API for:**

* Custom prompt templates with specific formatting requirements
* Base models (non-instruct/non-chat variants)
* Fine-grained control over token-level formatting
* Legacy applications that depend on raw completion format

**For most use cases, use [chat completions](/guides/querying-text-models) instead.** Chat completions handles message formatting automatically and works better with instruct-tuned models.

## Basic usage

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      prompt="Once upon a time"
    )

    print(response.choices[0].text)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        prompt="Once upon a time"
    )

    print(response.choices[0].text)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      prompt: "Once upon a time",
    });

    console.log(response.choices[0].text);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "prompt": "Once upon a time"
      }'
    ```
  </Tab>
</Tabs>

<Note>
  Most models automatically prepend the beginning-of-sequence (BOS) token (e.g., `<s>`) to your prompt. Verify this with the `raw_output` parameter if needed.
</Note>

## Custom prompt templates

The completions API is useful when you need to implement custom prompt formats:

```python theme={null}
# Custom few-shot prompt template
prompt = """Task: Classify the sentiment of the following text.

Text: I love this product!
Sentiment: Positive

Text: This is terrible.
Sentiment: Negative

Text: The weather is nice today.
Sentiment:"""

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt=prompt,
    max_tokens=10,
    temperature=0
)

print(response.choices[0].text)  # Output: " Positive"
```

## Common parameters

All [chat completions parameters](/guides/querying-text-models) work with completions:

* `temperature` - Control randomness (0-2)
* `max_tokens` - Limit output length
* `top_p`, `top_k`, `min_p` - Sampling parameters
* `stream` - Stream responses token-by-token
* `frequency_penalty`, `presence_penalty` - Reduce repetition

See the [API reference](/api-reference/post-completions) for complete parameter documentation.

## Querying deployments

Use completions with [on-demand deployments](/guides/ondemand-deployments) by specifying the deployment identifier:

```python theme={null}
response = client.completions.create(
    model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    prompt="Your prompt here"
)
```

## Next steps

<CardGroup>
  <Card title="Chat Completions" href="/guides/querying-text-models" icon="messages">
    Use chat completions for most use cases
  </Card>

  <Card title="Streaming" href="/guides/querying-text-models#streaming-responses" icon="bolt">
    Stream responses for real-time UX
  </Card>

  <Card title="API Reference" href="/api-reference/post-completions" icon="code">
    Complete API documentation
  </Card>
</CardGroup>
