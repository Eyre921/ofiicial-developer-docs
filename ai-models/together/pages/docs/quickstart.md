---
title: "Quickstart"
source: https://docs.together.ai/docs/quickstart
path: docs/quickstart
---

Make your first request to Together AI in a few minutes.

## Step 1: Create an API key

1. [Register for an account](https://api.together.ai/) if you don't have one.

2. Go to your project's [API keys page](https://api.together.ai/settings/projects/~current/api-keys).

3. Select **Create key**, give it a name, and copy the value. New keys are only shown once, so make sure to save it somewhere safe.

4. Set the key as an environment variable in your terminal:

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export TOGETHER_API_KEY="your_api_key"
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:TOGETHER_API_KEY="your_api_key"
  ```
</CodeGroup>

The SDK reads `TOGETHER_API_KEY` automatically when you call `Together()`. Pass `api_key=` to the constructor to override it.

## Step 2: Install the SDK

Together AI publishes official SDKs for Python and TypeScript. You can also use the [OpenAI SDK](/docs/inference/openai-compatibility) pointed at our base URL, or call the [REST API](/reference/chat-completions) directly from any language.

<CodeGroup>
  ```bash Python (uv) theme={null}
  uv init --no-workspace # optional
  uv add together
  ```

  ```bash Python (pip) theme={null}
  pip install together
  ```

  ```bash TypeScript (npm) theme={null}
  npm install together-ai
  ```
</CodeGroup>

## Step 3: Run your first query

The example below sends a chat completion request to [MiniMax M3](/docs/serverless/models) and prints the response:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # reads TOGETHER_API_KEY from environment

  response = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together(); // reads TOGETHER_API_KEY from environment

  async function main() {
    const response = await together.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
    });

    console.log(response.choices[0].message.content);
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "MiniMaxAI/MiniMax-M3",
      "messages": [
        {"role": "user", "content": "What are the top 3 things to do in New York?"}
      ]
    }'
  ```
</CodeGroup>

Save the snippet to a file, then run it. (The cURL command runs directly in your terminal.)

<CodeGroup>
  ```bash Python (uv) theme={null}
  uv run main.py
  ```

  ```bash Python (pip) theme={null}
  python main.py
  ```

  ```bash TypeScript theme={null}
  npx tsx main.ts
  ```
</CodeGroup>

After a few seconds, you should see the response printed to your terminal.

## Going further

Try some of these variations to see what else the model can do:

### Stream the response

Streaming returns the response token by token as it's generated, instead of making you wait for the full reply. This is especially helpful with a [reasoning model](/docs/inference/chat/reasoning) like MiniMax M3, which works through a problem before answering and can produce a lot of output.

A reasoning model's response has two parts: the step-by-step thinking, in a `reasoning` field, and the final answer, in `content`.

Set `stream=True` (Python) or `stream: true` (TypeScript/cURL) and read both fields off each chunk's `delta`:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # reads TOGETHER_API_KEY from environment

  stream = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      stream=True,
  )

  printed_answer_header = False

  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta

      # Reasoning models return their thinking in a separate `reasoning` field.
      if getattr(delta, "reasoning", None):
          print(delta.reasoning, end="", flush=True)

      # The final answer arrives in `content`.
      if getattr(delta, "content", None):
          if not printed_answer_header:
              print("\n\n--- Answer ---\n", flush=True)
              printed_answer_header = True
          print(delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions";

  const together = new Together();

  async function main() {
    const stream = await together.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
      stream: true,
    });

    let printedAnswerHeader = false;

    for await (const chunk of stream) {
      const delta = chunk.choices[0]?.delta as ChatCompletionChunk.Choice.Delta & {
        reasoning?: string;
      };

      // Reasoning models return their thinking in a separate `reasoning` field.
      if (delta?.reasoning) process.stdout.write(delta.reasoning);

      // The final answer arrives in `content`.
      if (delta?.content) {
        if (!printedAnswerHeader) {
          process.stdout.write("\n\n--- Answer ---\n");
          printedAnswerHeader = true;
        }
        process.stdout.write(delta.content);
      }
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -N -X POST "https://api.together.ai/v1/chat/completions" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "MiniMaxAI/MiniMax-M3",
      "messages": [
        {"role": "user", "content": "What are the top 3 things to do in New York?"}
      ],
      "stream": true
    }'
  ```
</CodeGroup>

With a non-reasoning model, `reasoning` stays empty and only `content` is returned, so the same loop works unchanged.

### Add a system prompt

Prepend a `system` message to set the model's tone, role, or constraints:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {
              "role": "system",
              "content": "You are a concise travel guide. Answer in two sentences or fewer.",
          },
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          },
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        {
          role: "system",
          content:
            "You are a concise travel guide. Answer in two sentences or fewer.",
        },
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
    });

    console.log(response.choices[0].message.content);
  }

  main();
  ```
</CodeGroup>

### Get structured JSON output

Pass a [JSON schema](/docs/inference/chat/structured-outputs) via `response_format` to get parseable JSON back:

<CodeGroup>
  ```python Python theme={null}
  from pydantic import BaseModel
  from together import Together

  client = Together()


  class Activity(BaseModel):
      name: str
      neighborhood: str
      why: str


  class Itinerary(BaseModel):
      city: str
      activities: list[Activity]


  response = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {"role": "user", "content": "Suggest 3 things to do in New York."},
      ],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "Itinerary",
              "schema": Itinerary.model_json_schema(),
          },
      },
  )

  itinerary = Itinerary.model_validate_json(response.choices[0].message.content)
  print(itinerary)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";

  const together = new Together();

  const Itinerary = z.object({
    city: z.string(),
    activities: z.array(
      z.object({
        name: z.string(),
        neighborhood: z.string(),
        why: z.string(),
      }),
    ),
  });

  async function main() {
    const response = await together.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        { role: "user", content: "Suggest 3 things to do in New York." },
      ],
      response_format: {
        type: "json_schema",
        json_schema: { name: "Itinerary", schema: z.toJSONSchema(Itinerary) },
      },
    });

    const itinerary = Itinerary.parse(
      JSON.parse(response.choices[0].message.content!),
    );
    console.log(itinerary);
  }

  main();
  ```
</CodeGroup>

### Analyze an image

MiniMax M3 also accepts images. Add an `image_url` block to the user message to ask questions about a picture:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Describe this image in one sentence.",
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Describe this image in one sentence." },
            {
              type: "image_url",
              image_url: {
                url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png",
              },
            },
          ],
        },
      ],
    });

    console.log(response.choices[0].message.content);
  }

  main();
  ```
</CodeGroup>

### Use the OpenAI SDK

If you're already using the OpenAI SDK, you can point it at Together's base URL (`https://api.together.ai/v1`) and keep the rest of your code the same:

<CodeGroup>
  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["TOGETHER_API_KEY"],
      base_url="https://api.together.ai/v1",
  )

  response = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: "https://api.together.ai/v1",
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "MiniMaxAI/MiniMax-M3",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
    });

    console.log(response.choices[0].message.content);
  }

  main();
  ```
</CodeGroup>

See [OpenAI compatibility](/docs/inference/openai-compatibility) for the full list of supported endpoints and parameters.

## Next steps

<CardGroup>
  <Card title="Choose a model" icon="sparkles" href="/docs/serverless/models">
    Browse the catalog of models for chat, coding, vision, and reasoning.
  </Card>

  <Card title="Dedicated model inference" icon="server-2" href="/docs/dedicated-endpoints/overview">
    Reserve GPUs for steady traffic or fine-tuned models.
  </Card>

  <Card title="Fine-tune a model" icon="adjustments-horizontal" href="/docs/fine-tuning/overview">
    Train a model on your own data with LoRA, DPO, or full fine-tuning.
  </Card>

  <Card title="GPU clusters" icon="cpu" href="/docs/gpu-clusters-overview">
    Run large-scale training and custom workloads on dedicated GPU clusters.
  </Card>
</CardGroup>
