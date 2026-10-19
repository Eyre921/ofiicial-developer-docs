---
title: "Decisions API (OpenAI-compatible)"
source: https://docs.fireworks.ai/api-reference/post-decisions
path: api-reference/post-decisions
---

Answer many typed questions about one input in a single call with POST /inference/v1/decisions

The Decisions API is the System One decisions API in the shape of OpenAI's Decisions API, so code written against OpenAI's SDK works against Fireworks without a translation layer. For the native request shape, see [`POST /inference/v1/systemone`](/api-reference/post-systemone).

## Endpoint

```
POST https://api.fireworks.ai/inference/v1/decisions
```

Authenticate with your normal Fireworks API key. Set `model` to the System One model path, for example `accounts/<your-account>/models/<your-model>`. Models that don't support this API return a `400`.

```bash cURL theme={null}
curl https://api.fireworks.ai/inference/v1/decisions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "accounts/<your-account>/models/<your-model>",
  "input": "Customer wrote: the package arrived late and damaged, I want my money back.",
  "questions": [
    {
      "type": "predicate",
      "name": "refund",
      "instructions": "Does the customer ask for a refund?"
    },
    {
      "type": "choice",
      "name": "tone",
      "instructions": "What is the customer'\''s tone?",
      "choices": [
        { "value": "angry", "description": "Angry or hostile" },
        { "value": "neutral", "description": "Neutral" },
        { "value": "positive", "description": "Positive" }
      ]
    },
    {
      "type": "score",
      "name": "urgency",
      "instructions": "How urgent is this ticket?",
      "levels": [
        { "label": "not urgent" },
        { "label": "somewhat urgent" },
        { "label": "urgent" },
        { "label": "critical" }
      ]
    }
  ]
}'
```

## Request

| Field | Type | Description |
| - | - | - |
| `model` | string | **Required.** The System One model path, for example `accounts/<your-account>/models/<your-model>`. |
| `input` | string or array | **Required.** The situation to decide about. A string, or an array of `{"role": "user", "content": ...}` messages whose text is joined with newlines. Content can be a string or an array of `{"type": "input_text", "text": "..."}` parts. |
| `questions` | array | **Required.** Ordered list of questions. Answers come back in the same order. |
| `safety_identifier` | string | Optional. Accepted and ignored. |

Each question:

| Field | Type | Description |
| - | - | - |
| `type` | string | **Required.** `predicate`, `choice`, or `score`. |
| `name` | string | Optional label for the question, echoed back in its answer. |
| `instructions` | string | **Required.** The question itself, in plain language. |
| `choices` | array | **Required for `choice`.** Two or more options, each `{"value": ..., "description": "..."}`. Values are strings or booleans. Up to 208 options. |
| `levels` | array | **Required for `score`.** Two or more levels in order, lowest first, each `{"label": "...", "description": "..."}`. |

`predicate`, `choice`, and `score` map to the `noul`, `choice`, and `score` question types of the [System One decisions API](/api-reference/post-systemone#question-types).

## Response

```json theme={null}
{
  "model": "accounts/<your-account>/models/<your-model>",
  "answers": [
    { "type": "predicate", "name": "refund", "probability": 0.98, "confidence": 0.96 },
    {
      "type": "choice",
      "name": "tone",
      "choice": "angry",
      "probabilities": [
        { "value": "angry", "probability": 0.91 },
        { "value": "neutral", "probability": 0.08 },
        { "value": "positive", "probability": 0.01 }
      ],
      "confidence": 0.87
    },
    {
      "type": "score",
      "name": "urgency",
      "score": 1.7,
      "probabilities": [
        { "value": 0, "label": "not urgent", "probability": 0.05 },
        { "value": 1, "label": "somewhat urgent", "probability": 0.3 },
        { "value": 2, "label": "urgent", "probability": 0.55 },
        { "value": 3, "label": "critical", "probability": 0.1 }
      ],
      "confidence": 0.4
    }
  ],
  "usage": {
    "input_tokens": 212,
    "input_tokens_details": { "cached_tokens": 0, "cache_write_tokens": 0 },
    "output_tokens": 0,
    "output_tokens_details": { "reasoning_tokens": 0 },
    "total_tokens": 212
  }
}
```

Values above are illustrative. `name` is `null` for questions that didn't set one. For `score` answers, each probability's `value` is the level index and `label` is the level's label.

## Differences from OpenAI's Decisions API

* **Text only.** `input_image` parts return a `400`.
* **208 options per `choice` question**, where OpenAI allows 255.
* `safety_identifier` is accepted but ignored.

Everything else — model, limits, caching, and errors — is identical to [`/inference/v1/systemone`](/api-reference/post-systemone).
