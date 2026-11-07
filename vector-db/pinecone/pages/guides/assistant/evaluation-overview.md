---
title: "Evaluation overview"
source: https://docs.pinecone.io/guides/assistant/evaluation-overview
path: guides/assistant/evaluation-overview
---

Overview of Pinecone Assistant response evaluation: measure correctness, completeness, and alignment scores to benchmark RAG system quality.

You can [evaluate the correctness and completeness of a response](/guides/assistant/evaluate-answers) from an assistant or RAG system.

## Use cases

Evaluate responses to:

* Measure how well the Pinecone Assistant captures the facts of the ground truth answer.
* Compare the Pinecone Assistant's answers to those of another RAG system.
* Compare the answers of your own RAG system to those of the Pinecone Assistant or another RAG system.

## SDK support

You can [evaluate responses](/reference/api/latest/assistant/metrics_alignment) directly or through the [Pinecone Python SDK](/reference/sdks/python/overview) or [Pinecone Node.js SDK](/reference/sdks/node/overview).

## Request

The request body requires the following fields:

| Field | Description |
| - | - |
| `question` | The question asked to the RAG system. |
| `answer` | The answer provided by the assistant being evaluated. |
| `ground_truth_answer` | The expected answer. |

For a runnable example, see [Evaluate answers](/guides/assistant/evaluate-answers).

## Response

### Metrics

The response returns a score from `0` to `1` for each of the following metrics:

| Metric | Description |
| - | - |
| `correctness` | Correctness of the RAG system's answer compared to the ground truth answer. |
| `completeness` | Completeness of the RAG system's answer compared to the ground truth answer. |
| `alignment` | A combined score of the correctness and completeness scores. |

### Reasoning

The response explains the reasoning behind each metric's score. This includes a list of evaluated facts with their entailment status:

| Status | Description |
| - | - |
| `entailed` | The fact is supported by the ground truth answer. |
| `contradicted` | The fact contradicts the ground truth answer. |
| `neutral` | The fact is neither supported nor contradicted by the ground truth answer. |

### Usage

The response includes the number of tokens used to calculate the metrics. This includes tokens for the prompt and completion.

## Pricing

Cost is calculated by [token usage](#usage). See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.

Response evaluation is only available for [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
