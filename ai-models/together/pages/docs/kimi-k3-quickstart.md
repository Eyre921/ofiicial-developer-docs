---
title: "Kimi K3 quickstart"
source: https://docs.together.ai/docs/kimi-k3-quickstart
path: docs/kimi-k3-quickstart
---

Call Kimi K3 on Together for long-horizon coding, vision-in-the-loop work, and deep reasoning.

Kimi K3 is Moonshot AI's flagship model and the first open-weight model in the 3-trillion-parameter class, at 2.8 trillion total parameters. It is built for frontier intelligence work: long-horizon coding, end-to-end knowledge work, and deep reasoning. It accepts both text and image inputs, thinks by default, and holds a 1.05M-token context window.

The model ID is `moonshotai/Kimi-K3`. Pricing is \$3.00 per 1M input tokens, \$15.00 per 1M output tokens, and \$0.30 per 1M cached input tokens, flat across the full context window.

Together AI is working directly with the Moonshot team on this model.

## Call Kimi K3

Thinking is on by default, so give `max_tokens` real headroom. The reasoning trace and the answer share the same completion budget, and a tight cap spends the whole allowance on reasoning and returns empty or truncated `content`.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  completion = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      messages=[
          {"role": "user", "content": "Introduce Kimi K3 in one sentence."}
      ],
      max_tokens=131072,
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const completion = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    messages: [
      { role: "user", content: "Introduce Kimi K3 in one sentence." },
    ],
    max_tokens: 131072,
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
          "model": "moonshotai/Kimi-K3",
          "messages": [
            {"role": "user", "content": "Introduce Kimi K3 in one sentence."}
          ],
          "max_tokens": 131072
       }'
  ```
</CodeGroup>

## Set the thinking effort

K3 thinks by default at `reasoning_effort="max"`. Lower the level to cut cost and latency:

* `"low"`: shallow reasoning. Use for short, high-volume calls.
* `"high"`: deep reasoning. Use for most coding and analysis work.
* `"max"`: maximum reasoning, the default. Use for the hardest planning, architecture, and multi-step agentic problems, and set `max_tokens` generously.

The levels are coarse dials rather than a strictly monotonic scale, so measure token counts on your own prompts before you tune. Invalid effort strings are accepted silently instead of returning an error, so validate the value in your own code.

To skip thinking entirely on trivial turns, pass `reasoning={"enabled": False}`. No thinking tokens are generated or billed.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # Adjust depth: "low" | "high" | "max"
  completion = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      messages=[
          {
              "role": "user",
              "content": "Prove that the square root of 2 is irrational.",
          }
      ],
      reasoning_effort="max",
      max_tokens=8192,
  )

  print(completion.choices[0].message.content)

  # Instant mode: no thinking tokens generated or billed
  fast = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      messages=[{"role": "user", "content": "What is the capital of France?"}],
      reasoning={"enabled": False},
      max_tokens=256,
  )

  print(fast.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  // Adjust depth: "low" | "medium" | "high" | "max"
  const completion = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    messages: [
      {
        role: "user",
        content: "Prove that the square root of 2 is irrational.",
      },
    ],
    reasoning_effort: "max",
    max_tokens: 8192,
  });

  console.log(completion.choices[0].message.content);

  // Instant mode: no thinking tokens generated or billed
  const fast = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    messages: [{ role: "user", content: "What is the capital of France?" }],
    reasoning: { enabled: false },
    max_tokens: 256,
  });

  console.log(fast.choices[0].message.content);
  ```
</CodeGroup>

For broader guidance on reasoning controls and prompting, see [Reasoning](/docs/inference/chat/reasoning).

## Stream the reasoning trace and the answer

K3 returns two channels. The thinking trace arrives on `reasoning_content` and the final answer arrives on `content`. Handle both, and skip chunks where `choices` is empty, since Together emits a final usage-only chunk.

K3 emits the trace under `reasoning_content` to match Moonshot, while other Together models use the newer `reasoning` alias. Reading both keys makes one handler work across models.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      messages=[{"role": "user", "content": "Explain why the sky is blue."}],
      max_tokens=4096,
      stream=True,
  )

  in_answer = False
  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta
      thinking = getattr(delta, "reasoning_content", None) or getattr(
          delta, "reasoning", None
      )
      if thinking:
          print(thinking, end="", flush=True)
      if delta.content:
          if not in_answer:
              print("\n--- answer ---")
              in_answer = True
          print(delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions";

  const together = new Together();

  // K3 emits the trace on reasoning_content; other models use reasoning
  type ReasoningDelta = ChatCompletionChunk.Choice.Delta & {
    reasoning_content?: string;
    reasoning?: string;
  };

  const stream = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    messages: [{ role: "user", content: "Explain why the sky is blue." }],
    max_tokens: 4096,
    stream: true,
  });

  let inAnswer = false;
  for await (const chunk of stream) {
    if (!chunk.choices?.length) continue;
    const delta = chunk.choices[0]?.delta as ReasoningDelta;

    const thinking = delta?.reasoning_content || delta?.reasoning;
    if (thinking) process.stdout.write(thinking);

    if (delta?.content) {
      if (!inAnswer) {
        process.stdout.write("\n--- answer ---\n");
        inAnswer = true;
      }
      process.stdout.write(delta.content);
    }
  }
  ```
</CodeGroup>

Display layers can render either channel. JSON parsers must read `content` only. History replay requires both, as described in [Preserve the thinking history](#preserve-the-thinking-history).

## Send images

K3 has native visual understanding. Pass `content` as an array of objects and supply the image as either a public URL or a base64 data URL. Together fetches public URLs server-side.

<CodeGroup>
  ```python Python theme={null}
  import base64
  from pathlib import Path

  from together import Together

  client = Together()

  IMAGE_URL = "https://raw.githubusercontent.com/pytorch/pytorch/main/docs/source/_static/img/pytorch-logo-dark.png"

  # From a public URL
  completion = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      max_tokens=2048,
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "image_url", "image_url": {"url": IMAGE_URL}},
                  {"type": "text", "text": "Describe this image."},
              ],
          }
      ],
  )

  print(completion.choices[0].message.content)

  # From a local file
  image_data = base64.b64encode(Path("image.png").read_bytes()).decode()

  completion = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      max_tokens=2048,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/png;base64,{image_data}"
                      },
                  },
                  {"type": "text", "text": "Describe this image."},
              ],
          }
      ],
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import { readFileSync } from "fs";
  import Together from "together-ai";

  const together = new Together();

  const IMAGE_URL =
    "https://raw.githubusercontent.com/pytorch/pytorch/main/docs/source/_static/img/pytorch-logo-dark.png";

  // From a public URL
  const completion = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: [
          { type: "image_url", image_url: { url: IMAGE_URL } },
          { type: "text", text: "Describe this image." },
        ],
      },
    ],
  });

  console.log(completion.choices[0].message.content);

  // From a local file
  const imageData = readFileSync("image.png").toString("base64");

  const fromFile = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "image_url",
            image_url: { url: `data:image/png;base64,${imageData}` },
          },
          { type: "text", text: "Describe this image." },
        ],
      },
    ],
  });

  console.log(fromFile.choices[0].message.content);
  ```
</CodeGroup>

Vision limits:

* There is no limit on the number of images per request, but the whole request body must stay under 100 MB. This is the binding constraint when you inline base64.
* 4K (4096x2160) is the recommended maximum resolution. Higher resolutions cost processing time and tokens without improving understanding.
* Token cost scales with resolution.
* A public URL is fetched with a plain server-side HTTP GET, so hosts that block unfamiliar clients return an error. Fall back to base64 for those.

Moonshot also publishes [Perception Bench](https://www.kimi.com/blog/perception-bench), a visual reasoning benchmark, if you want to evaluate K3's visual understanding yourself.

## Constrain the output to a schema

Pass a JSON schema through `response_format` with `"strict": True` to constrain the final `content`.

Keep `max_tokens` generous. The whole thinking trace is spent before the first schema-constrained token is emitted, so a tight cap truncates the JSON rather than the reasoning. Parse `content` only, never `reasoning_content`.

<CodeGroup>
  ```python Python theme={null}
  import json

  from together import Together

  client = Together()

  completion = client.chat.completions.create(
      model="moonshotai/Kimi-K3",
      max_tokens=4096,
      messages=[{"role": "user", "content": "Ada Lovelace was 36 years old."}],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "person",
              "strict": True,
              "schema": {
                  "type": "object",
                  "properties": {
                      "name": {"type": "string"},
                      "age": {"type": "integer"},
                  },
                  "required": ["name", "age"],
                  "additionalProperties": False,
              },
          },
      },
  )

  person = json.loads(completion.choices[0].message.content)
  print(person)
  # -> {'name': 'Ada Lovelace', 'age': 36}
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const completion = await together.chat.completions.create({
    model: "moonshotai/Kimi-K3",
    max_tokens: 4096,
    messages: [{ role: "user", content: "Ada Lovelace was 36 years old." }],
    response_format: {
      type: "json_schema",
      json_schema: {
        name: "person",
        strict: true,
        schema: {
          type: "object",
          properties: {
            name: { type: "string" },
            age: { type: "integer" },
          },
          required: ["name", "age"],
          additionalProperties: false,
        },
      },
    },
  });

  const person = JSON.parse(completion.choices[0].message.content ?? "{}");
  console.log(person);
  // -> { name: 'Ada Lovelace', age: 36 }
  ```
</CodeGroup>

The looser `{"type": "json_object"}` mode also works when you only need syntactically valid JSON.

## Call tools

Declare functions in `tools`. When the model returns `tool_calls`, append the complete assistant message to history, append one `tool` message per call with the matching `tool_call_id`, then call again.

`tool_choice` accepts four forms:

| Value                                                       | Effect                                                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `"auto"`                                                    | The model decides. This is also what omitting the field means.                       |
| `"required"`                                                | The model must call at least one tool this turn. Declare at least one callable tool. |
| `"none"`                                                    | Tool calls are forbidden this turn.                                                  |
| `{"type": "function", "function": {"name": "get_weather"}}` | Force one specific tool.                                                             |

Set `tool_choice="required"` on the first turn to force a tool call, then switch back to `"auto"`. Changing `tool_choice` between turns does not invalidate the prefix cache.

`message.model_dump(exclude_none=True)` is the line that matters below. It round-trips the assistant turn whole, including `reasoning_content`, which K3 depends on. See [Preserve the thinking history](#preserve-the-thinking-history).

<CodeGroup>
  ```python Python theme={null}
  import json

  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get the current weather for a city.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "city": {
                          "type": "string",
                          "description": "City name, e.g. Paris",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
                  "required": ["city"],
                  "additionalProperties": False,
              },
          },
      }
  ]


  def get_weather(city, unit="celsius"):
      return {
          "city": city,
          "temperature": 21,
          "unit": unit,
          "conditions": "sunny",
      }


  messages = [{"role": "user", "content": "What's the weather in Paris?"}]
  choice_mode = "required"  # Force a tool call on turn one

  for _ in range(5):
      response = client.chat.completions.create(
          model="moonshotai/Kimi-K3",
          messages=messages,
          tools=tools,
          tool_choice=choice_mode,
          max_tokens=8192,
      )
      choice = response.choices[0]
      message = choice.message

      # Append the complete assistant message, thinking trace included
      messages.append(message.model_dump(exclude_none=True))

      if choice.finish_reason != "tool_calls" or not message.tool_calls:
          print(message.content)
          break

      for call in message.tool_calls:
          try:
              args = json.loads(call.function.arguments)
          except json.JSONDecodeError:
              args = {}
          messages.append(
              {
                  "role": "tool",
                  "tool_call_id": call.id,
                  "content": json.dumps(get_weather(**args)),
              }
          )

      choice_mode = "auto"  # Hand control back after the forced turn
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const tools = [
    {
      type: "function" as const,
      function: {
        name: "get_weather",
        description: "Get the current weather for a city.",
        parameters: {
          type: "object",
          properties: {
            city: { type: "string", description: "City name, e.g. Paris" },
            unit: { type: "string", enum: ["celsius", "fahrenheit"] },
          },
          required: ["city"],
          additionalProperties: false,
        },
      },
    },
  ];

  function getWeather(city: string, unit = "celsius") {
    return { city, temperature: 21, unit, conditions: "sunny" };
  }

  const messages: any[] = [
    { role: "user", content: "What's the weather in Paris?" },
  ];
  let choiceMode: "required" | "auto" = "required";

  for (let i = 0; i < 5; i++) {
    const response = await together.chat.completions.create({
      model: "moonshotai/Kimi-K3",
      messages,
      tools,
      tool_choice: choiceMode,
      max_tokens: 8192,
    });

    const choice = response.choices[0];
    const message = choice.message;

    // Append the complete assistant message, thinking trace included
    messages.push(message);

    if (choice.finish_reason !== "tool_calls" || !message.tool_calls?.length) {
      console.log(message.content);
      break;
    }

    for (const call of message.tool_calls) {
      let args: { city: string; unit?: string };
      try {
        args = JSON.parse(call.function.arguments);
      } catch {
        args = { city: "" };
      }
      messages.push({
        role: "tool",
        tool_call_id: call.id,
        content: JSON.stringify(getWeather(args.city, args.unit)),
      });
    }

    choiceMode = "auto"; // Hand control back after the forced turn
  }
  ```
</CodeGroup>

## Load tools dynamically

K3 can pick up a tool mid-conversation. Place a complete tool definition (full `name`, `description`, and `parameters`) inside a `system` message that carries a `tools` field and no `content`. The tool becomes available from that message's position onward.

Rules to follow:

* Dynamic declarations use exactly the same format as the top-level `tools` field.
* The system message must have empty content. Sending both `content` and `tools` on it returns `400: a system message with dynamic tools must have empty content`.
* Declarations apply per request and are not retained by the server. Keep the message in later request history yourself. Keeping it preserves both the tool's availability and the cached prefix. Dropping it means the model can no longer call that tool and the changed prefix may miss the cache.
* Append declarations at the tail of `messages`. Appending does not affect the cached prefix, while removing or modifying an earlier declaration may hurt cache hits from that point onward.
* Keep at least one tool in the top-level `tools` array whenever you send `tool_choice`.

Don't put dozens or hundreds of tool definitions into every request. They eat context and make the model more likely to pick the wrong tool. Use search-then-inject instead:

1. At conversation start, declare a single `search_tools` function backed by your own catalog, plus a few core tools, and advertise the searchable domain tags in the system prompt.
2. On the first turn, set `tool_choice="required"` to force retrieval before answering.
3. Inject the full definitions of the matching tools through a `system` message based on the retrieval results.
4. Let the model call the loaded tools directly in later generations.

Decide `reasoning_effort` before the conversation starts, since changing it mid-conversation costs you cache hits.

```python Python theme={null}
import json

from together import Together

client = Together()

CATALOG = {
    "convert_currency": {
        "type": "function",
        "function": {
            "name": "convert_currency",
            "description": "Convert an amount from one currency to another.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "from_currency": {"type": "string"},
                    "to_currency": {"type": "string"},
                },
                "required": ["amount", "from_currency", "to_currency"],
                "additionalProperties": False,
            },
        },
    },
}

search_tools = {
    "type": "function",
    "function": {
        "name": "search_tools",
        "description": "Search the tool catalog. Tags: finance, travel, files.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
            "additionalProperties": False,
        },
    },
}

messages = [{"role": "user", "content": "Convert 100 USD to EUR."}]

# 1. Force retrieval before answering
first = client.chat.completions.create(
    model="moonshotai/Kimi-K3",
    messages=messages,
    tools=[search_tools],
    tool_choice="required",
    max_tokens=8192,
)
call = first.choices[0].message.tool_calls[0]
messages.append(first.choices[0].message.model_dump(exclude_none=True))
messages.append(
    {
        "role": "tool",
        "tool_call_id": call.id,
        "content": json.dumps(list(CATALOG)),
    }
)

# 2. Inject matching definitions at the tail: tools field, no content
messages.append({"role": "system", "tools": [CATALOG["convert_currency"]]})

# 3. The model calls the freshly loaded tool directly
second = client.chat.completions.create(
    model="moonshotai/Kimi-K3",
    messages=messages,
    tools=[search_tools],
    tool_choice="auto",
    max_tokens=8192,
)
print(second.choices[0].message.tool_calls)
# -> convert_currency({"amount":100,"from_currency":"USD","to_currency":"EUR"})
```

## Work with the 1.05M context and the cache

K3 accepts up to 1.05M input tokens on Together, and context caching is automatic. There is no cache ID, TTL, or extra parameter. Keep your long prefix (system prompt, knowledge base, repo dump) byte-stable across requests so later calls hit the cache. Moonshot reports cache hit rates above 90% in coding workloads, which pulls effective input cost toward the \$0.30 floor.

Moonshot recommends placing fixed bulk context such as knowledge documents at the very beginning of the `messages` array, ahead of the system message, then appending questions and replies after it.

Read the usage counters defensively. The `*_details` objects come back as plain dicts on some responses, and `completion_tokens_details` is absent entirely when you disable reasoning.

```python Python theme={null}
def _get(obj, key, default=None):
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


usage = completion.usage
reasoning_tokens = _get(
    _get(usage, "completion_tokens_details"), "reasoning_tokens", 0
)
cached_tokens = _get(
    _get(usage, "prompt_tokens_details"),
    "cached_tokens",
    _get(usage, "cached_tokens", 0),
)

print(
    f"prompt={usage.prompt_tokens} cached={cached_tokens} "
    f"completion={usage.completion_tokens} thinking={reasoning_tokens}"
)
# -> prompt=86 cached=64 completion=133 thinking=111
```

## Preserve the thinking history

K3 was trained in preserved thinking history mode, so the trace is state that the next turn depends on. Return the complete assistant message on every turn, `reasoning_content` included. If you keep only `content`, generation quality becomes unstable.

Together accepts the trace back under either `reasoning_content` (what K3 emits) or the newer `reasoning` alias.

```python Python theme={null}
from together import Together

client = Together()

prompt = (
    "Pick a random 5-digit number and commit to it. " "Reply with exactly: OK"
)

# Turn 1: let K3 think
first = client.chat.completions.create(
    model="moonshotai/Kimi-K3",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=4000,
)

# Replay the assistant turn whole: model_dump keeps reasoning_content
history = [
    {"role": "user", "content": prompt},
    first.choices[0].message.model_dump(exclude_none=True),
    {
        "role": "user",
        "content": "What number did you pick? Reply with just the number.",
    },
]

second = client.chat.completions.create(
    model="moonshotai/Kimi-K3",
    messages=history,
    max_tokens=4000,
)
print(second.choices[0].message.content)
```

Drop the trace from the replay and the model answers with a freshly invented number instead, because the commitment lived in the reasoning rather than in `content`.

<Warning>
  Don't switch an ongoing session over to K3 from another model. K3 inherits a history that contains no K3 thinking at all, and quality degrades. Start K3 sessions on K3.
</Warning>

## Sampling parameters

Most sampling parameters are fixed server-side. Omit them and let the defaults apply.

| Parameter                                              | Behavior on Together                                                                                                 |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| `temperature`                                          | Fixed at 1.0.                                                                                                        |
| `top_p`                                                | Fixed at 0.95. Any other value returns `400`.                                                                        |
| `n`                                                    | Fixed at 1. Best-of-n has to live in your own harness.                                                               |
| `presence_penalty`, `frequency_penalty`                | Fixed at 0.                                                                                                          |
| `logprobs`                                             | Not supported. Returns `400`.                                                                                        |
| `top_k`, `min_p`, `repetition_penalty`, `stop`, `seed` | Accepted.                                                                                                            |
| `max_tokens`                                           | No ceiling below the 1.05M context limit. Cap it yourself for short answers.                                         |
| `reasoning_effort`                                     | `"low"`, `"medium"`, `"high"`, or `"max"` (default). Invalid strings are accepted silently, so validate client-side. |
| `reasoning`                                            | `{"enabled": False}` disables thinking entirely.                                                                     |

## Architecture

Two architectural changes form K3's backbone, both aimed at moving information through longer sequences and deeper into the network:

* **Kimi Delta Attention (KDA):** A hybrid linear attention mechanism that provides an efficient foundation for scaling attention across very long contexts. This is Moonshot's first model to support a 1.05M context window.
* **Attention Residuals (AttnRes):** Selectively retrieves representations across model depth rather than accumulating them uniformly.

On top of that, Moonshot pushed mixture-of-experts (MoE) sparsity further with the Stable LatentMoE framework, activating 16 of 896 experts. At roughly 2% of experts active per token, routing and optimization become first-order problems, so four supporting techniques keep training stable at 2.8T scale:

* **Quantile Balancing:** Derives expert allocation directly from router-score quantiles, which eliminates heuristic updates and a sensitive balancing hyperparameter.
* **Per-Head Muon:** Extends the Muon optimizer to optimize attention heads independently for more adaptive learning at scale.
* **Sigmoid Tanh Unit (SiTU):** Improves activation control.
* **Gated MLA:** Improves attention selectivity.

K3 continues a sustained scaling push: in nine of the twelve months from July 2025 to July 2026, Kimi models set the upper bound of open-model scale. At 2.8T parameters, K3 is the largest open-weight model released to date.

## Use cases

K3 is strongest where a task runs long and needs little supervision:

* **Long-horizon coding:** Sustained engineering sessions, navigation of massive repositories, and orchestration of terminal tools.
* **Vision in the loop:** Iterating between code and live screenshots for game development, frontend engineering, and CAD, using visual feedback rather than a written description of the render.
* **Research pipelines:** Reviewing literature, implementing a numerical pipeline, cross-validating results, and producing an interactive deliverable in one run.
* **End-to-end knowledge work:** Deep research reports with interactive charts, timelines, and slides rather than a paragraph of prose.
* **Large-repository refactoring:** Cross-file, multi-step engineering work held together by the 1.05M context window.
* **Agentic tool orchestration:** Long tool-calling loops with reasoning between steps and tools loaded on demand.

## Limitations

* **Cost on short, high-volume calls:** Thinking defaults to `"max"`, so a pipeline that never sets `reasoning_effort` pays the maximum reasoning bill on every call. Reasoning tokens bill as output at \$15.00 per 1M. Drop trivial calls to `"low"` or disable reasoning outright.
* **Excessive proactiveness:** K3's training emphasizes long, difficult tasks, so it may make decisions on your behalf when it hits a minor issue or ambiguous intent mid-task. State hard constraints explicitly in the system prompt or in `AGENTS.md`.
* **Mid-session model swaps:** Switching an in-flight session to K3 from another model leaves it without any K3 thinking history and destabilizes output.
* **Cache fragility:** Restructuring earlier messages or editing an earlier tool declaration breaks the prefix cache and reprices the affected input from \$0.30 to \$3.00 per 1M tokens.

## Usage tips

| Tip                                                  | Rationale                                                                                                                 |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Give `max_tokens` real headroom**                  | The trace shares the completion budget with the answer. A tight cap returns empty or truncated `content`.                 |
| **Return the complete assistant message every turn** | `message.model_dump(exclude_none=True)` keeps `reasoning_content` in history, which K3 was trained to depend on.          |
| **Read both `reasoning_content` and `reasoning`**    | K3 emits the trace on `reasoning_content`. Other Together models use the `reasoning` alias. One handler then covers both. |
| **Parse `content` only**                             | Never run JSON parsing over the thinking trace.                                                                           |
| **Set `reasoning_effort` deliberately**              | `"max"` is the default and the most expensive setting. Match the level to the task.                                       |
| **Keep prefixes byte-stable**                        | Caching is automatic, so stable prefixes are what pull effective input cost toward \$0.30 per 1M tokens.                  |
| **Put bulk context first**                           | Place knowledge documents at the very start of `messages`, ahead of the system message, then append the conversation.     |
| **Inject dynamic tools at the tail**                 | Appending is cache-safe. Editing an earlier declaration invalidates everything after it.                                  |
| **Omit the fixed sampling parameters**               | `top_p`, `n`, and the penalties are fixed server-side and return `400` on any other value.                                |
| **Think in goals, not steps**                        | K3 is agentic. Give high-level objectives and let it orchestrate sub-tasks and tool calls.                                |

## Next steps

<CardGroup>
  <Card title="Reasoning" icon="brain" href="/docs/inference/chat/reasoning">
    Control reasoning depth and handle reasoning output across models.
  </Card>

  <Card title="Function calling" icon="tool" href="/docs/inference/function-calling/overview">
    Build tool-calling loops against any function-calling model.
  </Card>

  <Card title="Vision" icon="photo" href="/docs/inference/vision/overview">
    Send images to vision models and read the results.
  </Card>

  <Card title="Serverless models" icon="stack-2" href="/docs/serverless/models">
    Browse every model, context length, and price on serverless inference.
  </Card>
</CardGroup>
