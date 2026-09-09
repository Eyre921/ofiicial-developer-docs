---
title: "Kimi K2 family"
source: https://docs.fireworks.ai/models/kimi-k2
path: models/kimi-k2
---

Using Kimi K2 family models in agentic and tool-calling workflows on Fireworks.

## Using the Kimi K2 family in agentic workflows

### Always set `max_tokens`

Models in the **Kimi K2 family** can produce very long reasoning traces before arriving at a final answer. In agentic workflows where output is parsed and passed to downstream steps, always set `max_tokens` explicitly:

```python theme={null}
response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct",
    messages=messages,
    max_tokens=512,
    tools=tools,
)
```

Starting points by output type:

| Output type         | Suggested `max_tokens` |
| ------------------- | ---------------------- |
| Tool call responses | 256–512                |
| Short text          | 512–1024               |
| Structured JSON     | 1024–2048              |
| Long-form reasoning | 4096+                  |

### Tool schema design

Kimi K2 family models perform best when tools have clearly distinct names, descriptions, and parameter schemas. When tools have overlapping surface areas the model may select the wrong one.

```python theme={null}
# Less clear — overlapping descriptions
tools = [
    {"type": "function", "function": {"name": "read", "description": "Read data from a source", "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "exec", "description": "Execute an operation on a source", "parameters": {"type": "object", "properties": {}}}},
]

# More clear — distinct names and explicit scope
tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a file at a given path. Use this to inspect existing content before making changes. Do not use this to run code.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "execute_command",
            "description": "Run a shell command and return its output. Use this to run scripts, tests, or system operations. Do not use this to read file contents.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]
```

Best practices:

* Name tools by their primary action, not their domain (`read_file` not `file_tool`).
* Write descriptions that distinguish tools from each other, including what each tool is *not* for.
* Avoid optional parameters that make two tools look identical with only a flag difference.

### Timeouts for agentic loops

Inference for Kimi K2 family models can be slow on large inputs. For multi-step agents, set your client read timeout to at least 10–30 minutes per call. See [Reliability and error handling](/guides/reliability).
