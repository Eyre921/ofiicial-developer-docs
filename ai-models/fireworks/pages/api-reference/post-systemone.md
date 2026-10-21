---
title: "System One decisions API"
source: https://docs.fireworks.ai/api-reference/post-systemone
path: api-reference/post-systemone
---

Send a state and a set of typed questions to POST /inference/v1/systemone and get a calibrated probability distribution for every question in one pass.

The System One decisions API takes a **state** (any text or JSON describing the current situation) and a set of typed **questions**, and returns a calibrated probability distribution for every question. The model reads the state once and answers every question from that single pass, so adding questions to a request is much cheaper than making separate calls.

The same API is also available in an OpenAI-compatible shape at [`POST /inference/v1/decisions`](/api-reference/post-decisions).

## Endpoint

```
POST https://api.fireworks.ai/inference/v1/systemone
```

Authenticate with your normal Fireworks API key. Set `model` to the System One model path, for example `accounts/<your-account>/models/<your-model>`. Models that don't support this API return a `400`.

## Quickstart

```bash cURL theme={null}
curl https://api.fireworks.ai/inference/v1/systemone \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "accounts/<your-account>/models/<your-model>",
  "state": {
    "user_request": "Add retry with exponential backoff to the payments webhook handler, and don'\''t retry on 4xx.",
    "last_command": "npm test -- webhooks",
    "test_output": "PASS handler.test.ts (4 tests)\nFAIL retry.test.ts\n  x does not retry on 4xx responses\n    Expected forwardEvent to be called 1 time, received 5"
  },
  "questions": {
    "task_complete": {
      "type": "noul",
      "instructions": "Is the user'\''s request fully done?"
    },
    "next_action": {
      "type": "choice",
      "instructions": "What should the agent do next?",
      "criteria": {
        "edit_code": "Change the code to fix the failing behavior",
        "rerun_tests": "Run the tests again without changing anything",
        "ask_user": "Stop and ask the user a clarifying question",
        "finish": "Report the task as done"
      }
    },
    "risk": {
      "type": "score",
      "instructions": "How risky would it be to ship the current change as is?",
      "criteria": ["safe", "minor risk", "moderate risk", "high risk", "would cause an incident"]
    }
  }
}'
```

```python Python theme={null}
import os
import requests

response = requests.post(
    "https://api.fireworks.ai/inference/v1/systemone",
    headers={"Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}"},
    json={
        "model": "accounts/<your-account>/models/<your-model>",
        "state": "Customer wrote: the package arrived late and damaged, I want my money back.",
        "questions": {
            "refund": {
                "type": "noul",
                "instructions": "Does the customer ask for a refund?",
                "criteria": {"true": "A refund is requested", "false": "No refund is requested"},
            },
            "tone": {
                "type": "choice",
                "instructions": "What is the customer's tone?",
                "criteria": {"angry": "Angry or hostile", "neutral": "Neutral", "positive": "Positive"},
            },
            "urgency": {
                "type": "score",
                "instructions": "How urgent is this ticket?",
                "criteria": ["not urgent", "somewhat urgent", "urgent", "critical"],
            },
        },
    },
)
response.raise_for_status()
print(response.json()["answers"])
```

## Request

| Field | Type | Description |
| - | - | - |
| `model` | string | **Required.** The System One model path, for example `accounts/<your-account>/models/<your-model>`. |
| `state` | string or object | **Required.** The situation to decide about. Strings are used as-is; objects are serialized as JSON. |
| `questions` | object | **Required.** Map of your question ID to a question. Up to 256 questions per request. |

### Question types

| `type` | `criteria` | Answer |
| - | - | - |
| `noul` | Optional object `{"true": "...", "false": "..."}` describing each side. Defaults to yes/no. | Probability that the statement is true. |
| `choice` | **Required.** Object mapping each option key to a description. Up to 208 options. | The most likely option, a probability per option, and a confidence. |
| `score` | **Required.** Ordered array of 2 to 10 level descriptions, lowest first. | The expected score (0 = first level), a probability per level, and a confidence. |

Every question takes an `instructions` string: the question itself, in plain language.

## Response

```json theme={null}
{
  "model": "accounts/<your-account>/models/<your-model>",
  "answers": {
    "refund": { "type": "noul", "noul": 0.98 },
    "tone": {
      "type": "choice",
      "choice": "angry",
      "probabilities": { "angry": 0.91, "neutral": 0.08, "positive": 0.01 },
      "confidence": 0.87
    },
    "urgency": {
      "type": "score",
      "score": 1.7,
      "legend": { "0": "not urgent", "1": "somewhat urgent", "2": "urgent", "3": "critical" },
      "probabilities": { "0": 0.05, "1": 0.3, "2": 0.55, "3": 0.1 },
      "confidence": 0.4
    }
  },
  "usage": { "input_tokens": 212, "cached_input_tokens": 0, "output_tokens": 0 }
}
```

Values above are illustrative.

| Field | Description |
| - | - |
| `noul` | Probability, from 0 to 1, that the statement is true. |
| `choice` | The key of the most likely option. |
| `score` | Expected level, from 0 to the number of levels minus 1, weighted by probability. |
| `probabilities` | Probability of each option key (`choice`) or level index (`score`). Sums to 1. |
| `confidence` | How concentrated the distribution is: 0 when every option is equally likely, 1 when one option has all the probability. |
| `legend` | For `score`, maps each level index back to its description. |
| `usage` | Token usage for the request. `cached_input_tokens` counts state tokens served from the prompt cache. |

## Pricing and capacity

Billing, capacity, and rate limits depend on how the model is deployed. On a [dedicated deployment](/guides/ondemand-deployments), usage is billed at the deployment's standard on-demand GPU rate and capacity scales with the deployment's size and [autoscaling settings](/deployments/autoscaling).

## Latency and caching

* **Batch your questions.** All questions in a request share one read of the state, so asking ten questions in one request is much faster and cheaper than ten requests.
* **Reuse the state.** The state is cached across requests and the questions are not. Calls that send the same large state (for example a long transcript) with different questions benefit most from caching.
* **Measure server time.** The `fireworks-server-processing-time` response header reports time spent on Fireworks servers. Anything above that is network.

## Limits

| Limit | Value |
| - | - |
| Questions per request | 256 |
| Options per `choice` question | 208 |
| Levels per `score` question | 2 to 10 |
| Context window | 256K tokens |
| Question text | 16K tokens |
| State size | 4 MiB |
| Request body | 8 MiB |
| Request duration | 5 minutes |

Current support:

* **Text only.** Requests with `images` return a `400`.
* **No reasoning.** `reasoning_effort` other than `"none"` returns a `400`.
* **Decisions only.** The model serves `/inference/v1/systemone` and `/inference/v1/decisions` only. Chat completions and completions against it return a `400`.

## Errors

Errors use the standard Fireworks error body.

| Status | Meaning |
| - | - |
| `400` | Over a limit, an unsupported field, or a model that doesn't support this API. |
| `413` | Request body over 8 MiB. |
| `422` | Malformed JSON, a missing required field, or an invalid question (unknown `type` or malformed `criteria`). |
| `429` | Rate limited. Retry after the `Retry-After` header. |
| `503` | Temporarily at capacity. Retry after the `Retry-After` header. |
| `504` | The request took longer than 5 minutes. |
| `502` | Upstream failure. Safe to retry. |
