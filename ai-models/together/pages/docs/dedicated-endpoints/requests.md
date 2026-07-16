---
title: "Send requests"
source: https://docs.together.ai/docs/dedicated-endpoints/requests
path: docs/dedicated-endpoints/requests
---

After deploying a model, send requests using the shared inference API.

After [deploying model](/docs/dedicated-endpoints/manage#create-a-deployment) and [routing traffic](/docs/dedicated-endpoints/route-traffic) to it, you can send requests to the endpoint using the same [inference APIs](/docs/inference/overview) as serverless models.

Features available on the underlying model work the same way on DMI, including:

* [Function calling](/docs/inference/function-calling/overview) for tool use.
* [Structured outputs](/docs/inference/chat/structured-outputs) for JSON-shaped responses.
* [Streaming](/docs/inference/chat/overview) responses.

Dedicated model inference is served at `https://api-inference.together.ai`. There's no CLI for inference, so send requests with curl or the SDK, pointing the base URL at `https://api-inference.together.ai/v1`.

Pass the endpoint string as the `model` parameter, and use the same request shape you'd use against a serverless model. The endpoint string has the form `your-project-slug/endpoint-name`:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together(base_url="https://api-inference.together.ai/v1")

  response = client.chat.completions.create(
      model="your-project-slug/endpoint-name",
      messages=[{"role": "user", "content": "What is 2+2?"}],
      max_tokens=512,
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together({
    baseURL: 'https://api-inference.together.ai/v1',
  });

  const response = await client.chat.completions.create({
    model: 'your-project-slug/endpoint-name',
    messages: [{ role: 'user', content: 'What is 2+2?' }],
    max_tokens: 512,
  });

  console.log(response.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl -s -X POST https://api-inference.together.ai/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "your-project-slug/endpoint-name",
      "messages": [{"role": "user", "content": "What is 2+2?"}],
      "max_tokens": 512
    }' | jq .
  ```
</CodeGroup>

## Prompt caching

Prompt caching stores the result of previously processed prompt prefixes so the model can reuse them instead of recomputing. It reduces redundant compute for repeated prefixes, such as a system prompt that's shared across many requests.

Prompt caching is enabled by default for dedicated model inference. No configuration is required.

## Decoding optimizations

Decoding optimizations such as speculative decoding are set by the [config](/docs/dedicated-endpoints/configs#decoding-optimizations) your deployment runs on. To change them, deploy a different config.

## Next steps

<CardGroup>
  <Card title="Create a deployment" icon="layers-intersect" href="/docs/dedicated-endpoints/manage#create-a-deployment">
    Set the traffic split that drives routing.
  </Card>

  <Card title="Route traffic" icon="route" href="/docs/dedicated-endpoints/route-traffic">
    See how the endpoint resolves each request to a deployment.
  </Card>
</CardGroup>
