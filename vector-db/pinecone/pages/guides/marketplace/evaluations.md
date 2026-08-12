---
title: "Evaluations"
source: https://docs.pinecone.io/guides/marketplace/evaluations
path: guides/marketplace/evaluations
---

How Pinecone Marketplace runs automatic evaluations on every publish, scoring faithfulness and relevance to catch regressions in a new version.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Marketplace runs an automatic evaluation on every publish. Evaluations let you see whether a new version improved or regressed quality before opening it up to all end users.

## What an evaluation does

When a deployment publishes, Marketplace:

1. Generates a set of test questions from the connected sources.
2. Asks the new version to answer each test question.
3. Scores each response on faithfulness and relevance using an LLM judge.
4. Records the aggregate result in the version history.

Evaluations run as the final step of publishing. The version becomes active even if the evaluation flags regressions; treat the score as a signal, not a gate.

## Metrics

| Metric       | What it measures                                     |
| ------------ | ---------------------------------------------------- |
| Faithfulness | Whether the answer is grounded in the cited sources. |
| Relevance    | Whether the answer addresses the question.           |

You can drill into per-question results to see which test cases regressed and what the application returned.

## Test question generation

Test questions are generated automatically from the connected content; they are not curated by hand. To get more representative tests, keep the connected sources focused on the domain the application serves.

## Comparing versions

The deployment dashboard shows evaluation results per version. Use the comparison view to see:

* Aggregate score deltas between versions.
* Per-question pass and fail changes.
* Sources cited per response.

If a publish regresses, roll back from the version history. See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).

## End-user feedback

Evaluations measure the application against generated test cases. End-user feedback measures it against real questions. Use both together. See [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
