---
title: "Serverless Quickstart"
source: https://docs.fireworks.ai/getting-started/quickstart
path: getting-started/quickstart
---

Make your first Serverless API call in minutes

Serverless is the fastest way to get started with using open models. This quickstart will help you make your first API call in minutes.

## Step 1: Create and export an API key

Before you begin, create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Click **Create API key** and store it in a safe location.

Once you have your API key, export it as an environment variable in your terminal:

<Tabs>
  <Tab title="macOS / Linux">
    ```bash theme={null}
    export FIREWORKS_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx FIREWORKS_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

## Step 2: Make your first Serverless API call

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    Install the [Fireworks Python SDK](/tools-sdks/python-sdk):

    <Note>
      The SDK is currently in alpha. Use the `--pre` flag when installing to get the latest version.
    </Note>

    <CodeGroup>
      ```bash pip theme={null}
      pip install --pre fireworks-ai
      ```

      ```bash poetry theme={null}
      poetry add --pre fireworks-ai
      ```

      ```bash uv theme={null}
      uv add --pre fireworks-ai
      ```
    </CodeGroup>

    Then make your first Serverless API call:

    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[{
        "role": "user",
        "content": "Say hello in Spanish",
      }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    Fireworks provides an OpenAI compatible endpoint. Install the [OpenAI Python SDK](https://github.com/openai/openai-python):

    ```bash theme={null}
    pip install openai
    ```

    Then make your first Serverless API call:

    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{
            "role": "user",
            "content": "Say hello in Spanish",
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    Fireworks provides an Anthropic compatible endpoint. Install the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python):

    ```bash theme={null}
    pip install anthropic
    ```

    Then make your first Serverless API call:

    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    response = client.messages.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": "Say hello in Spanish",
        }],
    )

    print(response.content[0].text)
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    Fireworks provides an OpenAI compatible endpoint. Install the [OpenAI JavaScript / TypeScript SDK](https://github.com/openai/openai-node):

    ```bash theme={null}
    npm install openai
    ```

    Then make your first Serverless API call:

    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Say hello in Spanish",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    Fireworks provides an Anthropic compatible endpoint. Install the [Anthropic JavaScript / TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript):

    ```bash theme={null}
    npm install @anthropic-ai/sdk
    ```

    Then make your first Serverless API call:

    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const response = await client.messages.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: "Say hello in Spanish",
        },
      ],
    });

    console.log(response.content[0].text);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Say hello in Spanish"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

You should see a response like: `"¡Hola!"`

<Tip>
  For **Priority tier** (`service_tier: "priority"`) and **Fast**, see [Serverless Serving Paths](/serverless/serving-paths).
</Tip>

## Common use cases

### Streaming responses

Stream responses token-by-token for a better user experience:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    stream = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[{"role": "user", "content": "Tell me a short story"}],
      stream=True
    )

    for chunk in stream:
      if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
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

    stream = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Tell me a short story"}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    with client.messages.stream(
        model="accounts/fireworks/models/deepseek-v3p1",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Tell me a short story"}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const stream = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [{ role: "user", content: "Tell me a short story" }],
      stream: true,
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const stream = client.messages.stream({
      model: "accounts/fireworks/models/deepseek-v3p1",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Tell me a short story" }],
    });

    stream.on("text", (text) => {
      process.stdout.write(text);
    });

    await stream.finalMessage();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $FIREWORKS_API_KEY" \
        -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
            {
            "role": "user",
            "content": "Tell me a short story"
            }
        ],
        "stream": true
        }'
    ```
  </Tab>
</Tabs>

### Function calling

Connect your models to external tools and APIs:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        messages=[
            {"role": "user", "content": "What's the weather in Paris?"}
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "City name, e.g. San Francisco",
                            }
                        },
                        "required": ["location"],
                    },
                },
            },
        ],
    )

    print(response.choices[0].message.tool_calls)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        messages=[
            {"role": "user", "content": "What's the weather in Paris?"}
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "City name, e.g. San Francisco",
                            }
                        },
                        "required": ["location"],
                    },
                },
            },
        ],
    )

    print(response.choices[0].message.tool_calls)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    response = client.messages.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "What's the weather in Paris?"}
        ],
        tools=[
            {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name, e.g. San Francisco",
                        }
                    },
                    "required": ["location"],
                },
            },
        ],
    )

    for block in response.content:
        if block.type == "tool_use":
            print(f"Tool: {block.name}, Input: {block.input}")
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const tools = [
      {
        type: "function",
        function: {
          name: "get_weather",
          description: "Get the current weather for a location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "City name, e.g. San Francisco",
              },
            },
            required: ["location"],
          },
        },
      },
    ];

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/kimi-k2-instruct-0905",
      messages: [{ role: "user", content: "What's the weather in Paris?" }],
      tools: tools,
    });

    console.log(response.choices[0].message.tool_calls);
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const response = await client.messages.create({
      model: "accounts/fireworks/models/kimi-k2-instruct-0905",
      max_tokens: 1024,
      messages: [{ role: "user", content: "What's the weather in Paris?" }],
      tools: [
        {
          name: "get_weather",
          description: "Get the current weather for a location",
          input_schema: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "City name, e.g. San Francisco",
              },
            },
            required: ["location"],
          },
        },
      ],
    });

    for (const block of response.content) {
      if (block.type === "tool_use") {
        console.log(`Tool: ${block.name}, Input:`, block.input);
      }
    }
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/kimi-k2-instruct-0905",
        "messages": [
          {
            "role": "user",
            "content": "What'\''s the weather in Paris?"
          }
        ],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_weather",
              "description": "Get the current weather for a location",
              "parameters": {
                "type": "object",
                "properties": {
                  "location": {
                    "type": "string",
                    "description": "City name, e.g. San Francisco"
                  }
                },
                "required": ["location"]
              }
            }
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

[Learn more about function calling →](/guides/function-calling)

### Structured outputs (JSON mode)

Get reliable JSON responses that match your schema:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[
        {
          "role": "user",
          "content": "Extract the name and age from: John is 30 years old",
        }
      ],
      response_format={
        "type": "json_schema",
        "json_schema": {
          "name": "person",
          "schema": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "age": { "type": "number" }
            },
            "required": ["name", "age"],
          },
        },
      },
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[
            {
                "role": "user",
                "content": "Extract the name and age from: John is 30 years old",
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "person",
                "schema": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}, "age": {"type": "number"}},
                    "required": ["name", "age"],
                },
            },
        },
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    response = client.messages.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        max_tokens=1024,
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": { "type": "string" },
                        "age": { "type": "number" }
                    },
                    "required": ["name", "age"],
                },
            }
        },
        messages=[
            {
                "role": "user",
                "content": "Extract the name and age from: John is 30 years old",
            }
        ],
    )

    print(response.content[0].text)
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Extract the name and age from: John is 30 years old",
        },
      ],
      response_format: {
        type: "json_schema",
        json_schema: {
          name: "person",
          schema: {
            type: "object",
            properties: {
              name: { type: "string" },
              age: { type: "number" },
            },
            required: ["name", "age"],
          },
        },
      },
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const response = await client.messages.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      max_tokens: 1024,
      output_config: {
        format: {
          type: "json_schema",
          schema: {
            type: "object",
            properties: {
              name: { type: "string" },
              age: { type: "number" },
            },
            required: ["name", "age"],
          },
        },
      },
      messages: [
        {
          role: "user",
          content: "Extract the name and age from: John is 30 years old",
        },
      ],
    });

    console.log(response.content[0].text);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Extract the name and age from: John is 30 years old"
          }
        ],
        "response_format": {
          "type": "json_schema",
          "json_schema": {
            "name": "person",
            "schema": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "age": {
                  "type": "number"
                }
              },
              "required": ["name", "age"]
            }
          }
        }
      }'
    ```
  </Tab>
</Tabs>

[Learn more about structured outputs →](/structured-responses/structured-response-formatting)

### Reasoning

Some models support reasoning, where the model shows its thought process before giving the final answer:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
        model="accounts/fireworks/models/glm-5p2",
        messages=[
            {"role": "user", "content": "What is 25 * 37? Show your work."}
        ],
        reasoning_effort="medium",
    )

    msg = response.choices[0].message
    if msg.reasoning_content:
        print("Reasoning:", msg.reasoning_content)
    print("Answer:", msg.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/glm-5p2",
        messages=[
            {"role": "user", "content": "What is 25 * 37? Show your work."}
        ],
        extra_body={"reasoning_effort": "medium"},
    )

    msg = response.choices[0].message
    # Reasoning content is returned in a separate field
    reasoning = getattr(msg, "reasoning_content", None)
    if reasoning is None and hasattr(msg, "model_extra"):
        reasoning = msg.model_extra.get("reasoning_content")

    if reasoning:
        print("Reasoning:", reasoning)
    print("Answer:", msg.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    The Anthropic SDK uses the `thinking` parameter to enable reasoning:

    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    response = client.messages.create(
        model="accounts/fireworks/models/glm-5p2",
        max_tokens=16000,
        thinking={"type": "enabled", "budget_tokens": 4096},
        messages=[
            {"role": "user", "content": "What is 25 * 37? Show your work."}
        ],
    )

    for block in response.content:
        if block.type == "thinking":
            print("Thinking:", block.thinking)
        elif block.type == "text":
            print("Answer:", block.text)
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/glm-5p2",
      messages: [
        { role: "user", content: "What is 25 * 37? Show your work." },
      ],
      reasoning_effort: "medium",
    });

    const msg = response.choices[0].message;
    if (msg.reasoning_content) {
      console.log("Reasoning:", msg.reasoning_content);
    }
    console.log("Answer:", msg.content);
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    The Anthropic SDK uses the `thinking` parameter to enable reasoning:

    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const response = await client.messages.create({
      model: "accounts/fireworks/models/glm-5p2",
      max_tokens: 16000,
      thinking: { type: "enabled", budget_tokens: 4096 },
      messages: [
        { role: "user", content: "What is 25 * 37? Show your work." },
      ],
    });

    for (const block of response.content) {
      if (block.type === "thinking") {
        console.log("Thinking:", block.thinking);
      } else if (block.type === "text") {
        console.log("Answer:", block.text);
      }
    }
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/glm-5p2",
        "messages": [
          {
            "role": "user",
            "content": "What is 25 * 37? Show your work."
          }
        ],
        "reasoning_effort": "medium"
      }'
    ```
  </Tab>
</Tabs>

[Learn more about reasoning →](/guides/reasoning)

### Vision models

Analyze images with vision-language models:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/fireworks/models/kimi-k2p6",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "What's in this image?"},
            {
              "type": "image_url",
              "image_url": {
                "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"
              },
            },
          ],
        }
      ],
    )

    print(response.choices[0].message.content)
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

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p6",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"
                        },
                    },
                ],
            }
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    The Anthropic SDK uses its native image format with `type: "image"` and a `source` object:

    ```python theme={null}
    import os
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference"
    )

    response = client.messages.create(
        model="accounts/fireworks/models/kimi-k2p6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png",
                        },
                    },
                ],
            }
        ],
    )

    for block in response.content:
        if block.type == "text":
            print(block.text)
    ```
  </Tab>

  <Tab title="JavaScript (OpenAI SDK)">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/kimi-k2p6",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What's in this image?" },
            {
              type: "image_url",
              image_url: {
                url: "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png",
              },
            },
          ],
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="JavaScript (Anthropic SDK)">
    ```javascript theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const client = new Anthropic({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference",
    });

    const response = await client.messages.create({
      model: "accounts/fireworks/models/kimi-k2p6",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What's in this image?" },
            {
              type: "image",
              source: {
                type: "url",
                url: "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png",
              },
            },
          ],
        },
      ],
    });

    for (const block of response.content) {
      if (block.type === "text") {
        console.log(block.text);
      }
    }
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/kimi-k2p6",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "What'\''s in this image?"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"
                }
              }
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

[Learn more about vision models →](/guides/querying-vision-language-models)

## Learn more about Serverless

For the model lifecycle policy, billing details, and serverless-specific request/response behavior, see the [Serverless overview](/serverless/overview).

## Next steps

Ready to scale to production, explore other modalities, or customize your models?

<CardGroup>
  <Card title="Deploy and autoscale on Dedicated GPUs" href="/guides/ondemand-deployments" icon="server">
    Deploy with high performance on dedicated GPUs with fast autoscaling and minimal cold starts
  </Card>

  <Card title="Train Models" href="/fine-tuning/finetuning-intro" icon="sliders">
    Improve model quality with supervised and reinforcement learning
  </Card>

  <Card title="Embeddings & Reranking" href="/guides/querying-embeddings-models" icon="brackets-curly">
    Use embeddings & reranking in search & context retrieval
  </Card>

  <Card title="Batch Inference" href="/guides/batch-inference" icon="list-check">
    Run async inference jobs at scale, faster and cheaper
  </Card>

  <Card title="Browse 100+ Models" href="https://fireworks.ai/models" icon="books">
    Explore all available models across modalities
  </Card>

  <Card title="API Reference" href="/api-reference/introduction" icon="code">
    Complete API documentation
  </Card>
</CardGroup>
