---
title: "Kimi K2.6 quickstart"
source: https://docs.together.ai/docs/kimi-k2.6-quickstart
path: docs/kimi-k2.6-quickstart
---

Get the most out of Moonshot AI's Kimi K2.6 multimodal model for vision, reasoning, and agentic tool use.

Kimi K2.6 is an open-source, multimodal agentic model from Moonshot AI. It accepts both text and image inputs and integrates visual and language understanding with strong agentic capabilities.

K2.6 supports both instant and thinking modes and excels at multi-turn function calling with images interleaved between tool calls.

## How to use Kimi K2.6

Get started with this model in a few lines of code. The model ID is `moonshotai/Kimi-K2.6` and it supports a 256K context window.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
      model="moonshotai/Kimi-K2.6",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      temperature=0.6,  # Use 0.6 for instant mode
      top_p=0.95,
      stream=True,
  )
  for tok in resp:
      if tok.choices:
          print(tok.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2.6',
    messages: [{ role: 'user', content: 'What are some fun things to do in New York?' }],
    temperature: 0.6,  // Use 0.6 for instant mode
    top_p: 0.95,
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

## Thinking mode

K2.6 supports both instant mode (fast responses) and thinking mode (step-by-step reasoning). When enabling thinking mode, you'll receive both a `reasoning` field and a `content` field. By default, the model uses thinking mode.

<Note>
  **Use the right temperature:** Set `temperature=1.0` for thinking mode and `temperature=0.6` for instant mode. The wrong temperature can significantly degrade output quality.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="moonshotai/Kimi-K2.6",
      messages=[
          {
              "role": "user",
              "content": "Which number is bigger, 9.11 or 9.9? Think carefully.",
          }
      ],
      reasoning={"enabled": True},
      temperature=1.0,  # Use 1.0 for thinking mode
      top_p=0.95,
      stream=True,
  )

  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta

      # Show reasoning tokens if present
      if hasattr(delta, "reasoning") and delta.reasoning:
          print(delta.reasoning, end="", flush=True)

      # Show content tokens if present
      if hasattr(delta, "content") and delta.content:
          print(delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  import type { 
    ChatCompletionChunk,
    ChatCompletionCreateParamsStreaming 
  } from "together-ai/resources/chat/completions";

  const together = new Together();

  // Extend types for reasoning support
  type ReasoningParams = ChatCompletionCreateParamsStreaming & {
    reasoning?: { enabled: boolean };
  };

  type ReasoningDelta = ChatCompletionChunk.Choice.Delta & { 
    reasoning?: string 
  };

  async function main() {
    const params: ReasoningParams = {
      model: "moonshotai/Kimi-K2.6",
      messages: [
        { role: "user", content: "Which number is bigger, 9.11 or 9.9? Think carefully." },
      ],
      reasoning: { enabled: true },
      temperature: 1.0,  // Use 1.0 for thinking mode
      top_p: 0.95,
      stream: true,
    };

    const stream = await together.chat.completions.create(params);

    for await (const chunk of stream) {
      const delta = chunk.choices[0]?.delta as ReasoningDelta;

      // Show reasoning tokens if present
      if (delta?.reasoning) process.stdout.write(delta.reasoning);

      // Show content tokens if present
      if (delta?.content) process.stdout.write(delta.content);
    }
  }

  main();
  ```
</CodeGroup>

## Vision capabilities

K2.6 accepts image inputs alongside text, so it can answer questions about visual content, reason across text and images, and ground tool calls in what it sees.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="moonshotai/Kimi-K2.6",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What can you see in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
              ],
          }
      ],
      temperature=0.6,
      top_p=0.95,
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "moonshotai/Kimi-K2.6",
    messages: [{
      role: "user",
      content: [
        { type: "text", text: "What can you see in this image?" },
        { type: "image_url", image_url: { url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png" }}
      ]
    }],
    temperature: 0.6,
    top_p: 0.95,
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Use cases

K2.6 excels in scenarios requiring combined visual understanding and agentic execution:

* **Coding from visual specs:** Generate code from UI designs, wireframes, or video workflows, then autonomously orchestrate tools for implementation.
* **Visual data processing pipelines:** Analyze charts, diagrams, or screenshots and chain tool calls to extract, transform, and act on visual data.
* **Multi-modal agent workflows:** Build agents that maintain coherent behavior across extended sequences of tool calls interleaved with image analysis.
* **Document intelligence:** Process complex documents with mixed text and visuals, extracting information and taking actions based on what's seen.
* **UI testing and automation:** Analyze screenshots, identify elements, and generate test scripts or automation workflows.
* **Cross-modal reasoning:** Solve problems that require understanding relationships between visual and textual information.

## Agent swarm capability

K2.6 can decompose a complex task into parallel sub-tasks and coordinate them as a swarm of domain-specific sub-agents. You enable this by exposing two tools and prompting the model to delegate: one tool to spawn a sub-agent with a focused task, and one for sub-agents to report results back to the orchestrator. Given those tools and a high-level goal, K2.6 plans the decomposition, fans out the work in parallel, and aggregates the results. This pattern shows up in coding agents like OpenCode, where the model issues several tool calls in parallel to solve a problem faster.

<Info>
  The exact tool schema for sub-agent spawning is up to your harness. Check the [Kimi GitHub repo](https://github.com/MoonshotAI/Kimi-K2) for the latest implementation guidance.
</Info>

## Prompting tips

| Tip                                                                                        | Rationale                                                                                                              |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Temperature = 1.0 for thinking, 0.6 for instant**                                        | Critical for output quality. Thinking mode needs higher temperature. Instant mode benefits from more focused sampling. |
| **top\_p = 0.95**                                                                          | Recommended default for both modes.                                                                                    |
| **Keep system prompts simple** - `"You are Kimi, an AI assistant created by Moonshot AI."` | Matches the prompt used during instruction tuning.                                                                     |
| **Leverage native tool calling with vision**                                               | Pass images in user messages alongside tool definitions. K2.6 can ground tool calls in visual context.                 |
| **Think in goals, not steps**                                                              | Give high-level objectives and let the model orchestrate sub-tasks, especially for agentic workflows.                  |
| **Chunk very long contexts**                                                               | 256K context is large, but response speed drops on >100K inputs. Provide an executive summary to focus the model.      |

## Multi-turn tool calling with images

K2.6 can perform multi-turn tool calls with images interleaved between the calls, maintaining coherent tool use across long sequences while processing visual inputs at each step.

This makes K2.6 ideal for visual workflows where the model needs to analyze images, call tools based on what it sees, receive results, analyze new images, and continue iterating.

The example below demonstrates a four-turn conversation where the model:

1. Calls the weather tool for multiple cities in parallel.
2. Follows up with restaurant recommendations based on weather context.
3. Identifies a company from an image and fetches its stock price.
4. Processes a new city image to get weather and restaurant info.

```python Python theme={null}
import json
from together import Together

client = Together()

# -----------------------------
# Tools (travel + stocks)
# -----------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit",
                    },
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_restaurant_recommendations",
            "description": "Get restaurant recommendations for a specific location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and state, e.g. San Francisco, CA",
                    },
                    "cuisine_type": {
                        "type": "string",
                        "enum": [
                            "italian",
                            "chinese",
                            "mexican",
                            "american",
                            "french",
                            "japanese",
                            "any",
                        ],
                        "description": "Cuisine preference",
                    },
                    "price_range": {
                        "type": "string",
                        "enum": ["budget", "mid-range", "upscale", "any"],
                        "description": "Price range preference",
                    },
                },
                "required": ["location"],
            },
        },
    },
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
                        "description": "Stock symbol, e.g. AAPL, GOOGL, TSLA",
                    },
                    "exchange": {
                        "type": "string",
                        "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                        "description": "Exchange (optional)",
                    },
                },
                "required": ["symbol"],
            },
        },
    },
]


# -----------------------------
# Local tool implementations (mock)
# -----------------------------
def get_current_weather(location, unit="fahrenheit"):
    loc = location.lower()
    data = {
        "chicago": ("Chicago", "13", "cold and snowy"),
        "san francisco": ("San Francisco", "65", "mild and partly cloudy"),
        "new york": ("New York", "28", "cold and windy"),
    }
    for k, (city, temp, cond) in data.items():
        if k in loc:
            return json.dumps(
                {
                    "location": city,
                    "temperature": temp,
                    "unit": unit,
                    "condition": cond,
                }
            )
    return json.dumps(
        {
            "location": location,
            "temperature": "unknown",
            "unit": unit,
            "condition": "unknown",
        }
    )


def get_restaurant_recommendations(
    location, cuisine_type="any", price_range="any"
):
    loc = location.lower()
    by_city = {
        "san francisco": {
            "italian": ["Tony's Little Star Pizza", "Perbacco"],
            "chinese": ["R&G Lounge", "Z&Y Restaurant"],
            "american": ["Zuni Café", "House of Prime Rib"],
            "seafood": ["Swan Oyster Depot", "Fisherman's Wharf restaurants"],
        },
        "chicago": {
            "italian": ["Gibsons Italia", "Piccolo Sogno"],
            "american": ["Alinea", "Girl & Goat"],
            "pizza": ["Lou Malnati's", "Giordano's"],
            "steakhouse": ["Gibsons Bar & Steakhouse"],
        },
        "new york": {
            "italian": ["Carbone", "Don Angie"],
            "american": ["The Spotted Pig", "Gramercy Tavern"],
            "pizza": ["Joe's Pizza", "Prince Street Pizza"],
            "fine_dining": ["Le Bernardin", "Eleven Madison Park"],
        },
    }
    restaurants = next((v for k, v in by_city.items() if k in loc), {})
    return json.dumps(
        {
            "location": location,
            "cuisine_filter": cuisine_type,
            "price_filter": price_range,
            "restaurants": restaurants,
        }
    )


def get_current_stock_price(symbol, exchange=None):
    mock = {
        "AAPL": {"price": "193.42", "currency": "USD", "exchange": "NASDAQ"},
        "TSLA": {"price": "247.19", "currency": "USD", "exchange": "NASDAQ"},
        "GOOGL": {"price": "152.07", "currency": "USD", "exchange": "NASDAQ"},
        "MSFT": {"price": "421.55", "currency": "USD", "exchange": "NASDAQ"},
        "NVDA": {"price": "612.30", "currency": "USD", "exchange": "NASDAQ"},
    }
    sym = symbol.upper()
    data = mock.get(
        sym,
        {
            "price": "unknown",
            "currency": "USD",
            "exchange": exchange or "unknown",
        },
    )
    return json.dumps({"symbol": sym, **data})


# -----------------------------
# Multi-turn runner (supports images + tools)
# -----------------------------
TOOL_FNS = {
    "get_current_weather": lambda a: get_current_weather(
        a.get("location"), a.get("unit", "fahrenheit")
    ),
    "get_restaurant_recommendations": lambda a: get_restaurant_recommendations(
        a.get("location"),
        a.get("cuisine_type", "any"),
        a.get("price_range", "any"),
    ),
    "get_current_stock_price": lambda a: get_current_stock_price(
        a.get("symbol"), a.get("exchange")
    ),
}


def run_turn(messages, user_content):
    messages.append({"role": "user", "content": user_content})

    resp = client.chat.completions.create(
        model="moonshotai/Kimi-K2.6",
        messages=messages,
        tools=tools,
    )

    msg = resp.choices[0].message
    tool_calls = msg.tool_calls or []

    if tool_calls:
        messages.append(
            {
                "role": "assistant",
                "content": msg.content or "",
                "tool_calls": [tc.model_dump() for tc in tool_calls],
            }
        )

        for tc in tool_calls:
            fn = tc.function.name
            args = json.loads(tc.function.arguments or "{}")
            print(f"🔧 Calling {fn} with args: {args}")
            out = TOOL_FNS.get(
                fn, lambda _: json.dumps({"error": f"Unknown tool: {fn}"})
            )(args)
            messages.append(
                {
                    "tool_call_id": tc.id,
                    "role": "tool",
                    "name": fn,
                    "content": out,
                }
            )

        final = client.chat.completions.create(
            model="moonshotai/Kimi-K2.6", messages=messages
        )
        content = final.choices[0].message.content
        messages.append({"role": "assistant", "content": content})
        return content

    messages.append({"role": "assistant", "content": msg.content})
    return msg.content


# -----------------------------
# Example conversation (multi-turn, includes images)
# -----------------------------
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. Use tools when needed. "
            "If the user provides an image, infer what you can from it, and call tools when helpful."
        ),
    }
]

print("TURN 1:")
print(
    "User: What is the current temperature of New York, San Francisco and Chicago?"
)
a1 = run_turn(
    messages,
    "What is the current temperature of New York, San Francisco and Chicago?",
)
print("Assistant:", a1)

print("\nTURN 2:")
print(
    "User: Based on the weather, which city is best for outdoor activities and give restaurants there."
)
a2 = run_turn(
    messages,
    "Based on the weather, which city would be best for outdoor activities? And recommend some restaurants there.",
)
print("Assistant:", a2)

print("\nTURN 3:")
print("User: What is the stock price of the company from the image?")
a3 = run_turn(
    messages,
    [
        {
            "type": "text",
            "text": "What is the stock price of the company from the image?",
        },
        {
            "type": "image_url",
            "image_url": {
                "url": "https://53.fs1.hubspotusercontent-na1.net/hubfs/53/image8-2.jpg"
            },
        },
    ],
)
print("Assistant:", a3)

print("\nTURN 4:")
print(
    "User: I want to go to this new city now in the image, what’s the weather like and what’s one Italian spot?"
)
a4 = run_turn(
    messages,
    [
        {
            "type": "text",
            "text": "I want to go to this new city now in the image, what’s the weather like and what’s one Italian spot?",
        },
        {
            "type": "image_url",
            "image_url": {
                "url": "https://azure-na-images.contentstack.com/v3/assets/blt738d1897c3c93fa6/bltfa5d0fb785639f6f/685040c8f7cdb0fdfa0e6392/MG_1_1_New_York_City_1.webp"
            },
        },
    ],
)
print("Assistant:", a4)
```

### Sample output

Here's what the conversation looks like in practice:

```plain theme={null}
TURN 1:
User: What is the current temperature of New York, San Francisco and Chicago?
🔧 Calling get_current_weather with args: {'location': 'New York, NY'}
🔧 Calling get_current_weather with args: {'location': 'San Francisco, CA'}
🔧 Calling get_current_weather with args: {'location': 'Chicago, IL'}
Assistant: Here are the current temperatures for each city:

| City | Temperature | Condition |
|------|-------------|-----------|
| **New York** | 28°F (-2°C) | Cold and windy |
| **San Francisco** | 65°F (18°C) | Mild and partly cloudy |
| **Chicago** | 13°F (-11°C) | Cold and snowy |

Quite a contrast! San Francisco is enjoying mild weather, while Chicago is 
experiencing frigid, snowy conditions. Stay warm if you're in the Midwest! 🧥

TURN 2:
User: Based on the weather, which city is best for outdoor activities and give restaurants there.
🔧 Calling get_restaurant_recommendations with args: {'location': 'San Francisco, CA', 'cuisine_type': 'any', 'price_range': 'any'}
Assistant: Here are some excellent restaurant recommendations in San Francisco:

### 🍝 Italian
- **Tony's Little Star Pizza** – Known for amazing deep-dish pizza in North Beach
- **Perbacco** – Upscale Northern Italian spot in the Financial District

### 🥟 Chinese
- **R&G Lounge** – Famous in Chinatown, known for their salt & pepper crab
- **Z&Y Restaurant** – Authentic Sichuan cuisine

### 🥩 American
- **Zuni Café** – Iconic SF institution, known for their roasted chicken
- **House of Prime Rib** – Classic steakhouse experience

With the beautiful 65°F weather, I'd especially recommend dining at 
Fisherman's Wharf or enjoying food at Crissy Field with Golden Gate views!

TURN 3:
User: What is the stock price of the company from the image?
🔧 Calling get_current_stock_price with args: {'symbol': 'GOOGL'}
Assistant: As of now, **Alphabet Inc.** (Google's parent company) stock price is:

| Metric | Value |
|--------|-------|
| **Ticker Symbol** | GOOGL (Class A) |
| **Current Price** | **$152.07 USD** |
| **Exchange** | NASDAQ |

TURN 4:
User: I want to go to this new city now in the image, what's the weather and an Italian spot?
🔧 Calling get_current_weather with args: {'location': 'New York, NY'}
🔧 Calling get_restaurant_recommendations with args: {'location': 'New York, NY', 'cuisine_type': 'italian'}
Assistant: Here's what you need to know:

## 🌡️ Current Weather
**28°F (-2°C) — Cold and windy**

Bundle up! Dress warmly with layers, a coat, and definitely a hat and gloves.

## 🍝 Italian Restaurant Recommendation

**Carbone** – Located in Greenwich Village, this is one of NYC's hottest 
Italian-American restaurants, known for their famous spicy rigatoni vodka 
and old-school vibes. Given the 28°F temperatures, Carbone's cozy, 
bustling atmosphere would be a perfect refuge from the cold! 🧥🍷
```

Notice how K2.6 maintains context across all turns: it identifies Google from the logo image to call the stock price tool (Turn 3), and recognizes New York City from the skyline image to call the appropriate weather and restaurant tools (Turn 4).
