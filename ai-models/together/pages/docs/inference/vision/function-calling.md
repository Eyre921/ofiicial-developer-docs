---
title: "Vision-language function calling"
source: https://docs.together.ai/docs/inference/vision/function-calling
path: docs/inference/vision/function-calling
---

Combine image understanding with tool use on Together AI vision-language models.

Vision language models (VLMs) can also use [function calling](/docs/inference/function-calling/overview), letting you combine image understanding with tool use. This enables use cases like extracting structured data from images, identifying objects and taking actions, or analyzing visual content to trigger specific functions.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_stock_price",
              "description": "Get the current stock price for the given stock symbol",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "symbol": {
                          "type": "string",
                          "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA",
                      },
                      "exchange": {
                          "type": "string",
                          "description": "The stock exchange (optional)",
                          "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                      },
                  },
                  "required": ["symbol"],
              },
          },
      },
  ]

  response = client.chat.completions.create(
      model="moonshotai/Kimi-K2.6",
      reasoning={"enabled": False},
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What is the stock price of the company from the image",
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://53.fs1.hubspotusercontent-na1.net/hubfs/53/image8-2.jpg",
                      },
                  },
              ],
          },
      ],
      tools=tools,
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"], indent=2
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "get_current_stock_price",
        description: "Get the current stock price for the given stock symbol",
        parameters: {
          type: "object",
          properties: {
            symbol: {
              type: "string",
              description: "The stock symbol, e.g. AAPL, GOOGL, TSLA",
            },
            exchange: {
              type: "string",
              description: "The stock exchange (optional)",
              enum: ["NYSE", "NASDAQ", "LSE", "TSX"],
            },
          },
          required: ["symbol"],
        },
      },
    },
  ];

  (async () => {
    const response = await client.chat.completions.create({
      model: "moonshotai/Kimi-K2.6",
      reasoning: { enabled: false },
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: "What is the stock price of the company from the image",
            },
            {
              type: "image_url",
              image_url: {
                url: "https://53.fs1.hubspotusercontent-na1.net/hubfs/53/image8-2.jpg",
              },
            },
          ],
        },
      ],
      tools: tools,
    });

    console.log(
      JSON.stringify(response.choices[0].message.tool_calls, null, 2)
    );
  })();
  ```

  ```bash cURL theme={null}
  curl https://api.together.ai/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "model": "moonshotai/Kimi-K2.6",
    "reasoning": {"enabled": false},
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is the stock price of the company from the image"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://53.fs1.hubspotusercontent-na1.net/hubfs/53/image8-2.jpg"
            }
          }
        ]
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_stock_price",
          "description": "Get the current stock price for the given stock symbol",
          "parameters": {
            "type": "object",
            "properties": {
              "symbol": {
                "type": "string",
                "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
              },
              "exchange": {
                "type": "string",
                "description": "The stock exchange (optional)",
                "enum": ["NYSE", "NASDAQ", "LSE", "TSX"]
              }
            },
            "required": ["symbol"]
          }
        }
      }
    ]
  }'
  ```
</CodeGroup>

The model analyzes the image to identify the company, then returns a function call with the appropriate stock symbol:

```json JSON theme={null}
[
  {
    "id": "call_85951e7547ec4b81954b35e5",
    "type": "function",
    "function": {
      "name": "get_current_stock_price",
      "arguments": "{\"symbol\": \"GOOGL\"}"
    },
    "index": -1
  }
]
```
