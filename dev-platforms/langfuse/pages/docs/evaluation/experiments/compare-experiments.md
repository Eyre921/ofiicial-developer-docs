---
title: "Compare versions and inspect failures"
source: https://langfuse.com/docs/evaluation/experiments/compare-experiments.md
path: docs/evaluation/experiments/compare-experiments
---

---
title: Compare experiments
sidebarTitle: Compare Experiments
description: Compare application versions against a baseline, inspect individual regressions, and review failures in Langfuse.
---

# Compare experiments

Compare experiment runs to decide whether a prompt, model, retrieval, or code change is ready to ship. Start with aggregate scores, then inspect cases that got worse and open their traces to understand the cause.

Experiment runs can use Langfuse datasets or local data. See [Evaluate an existing application](/resources/engineering/evaluate-existing-application) to create two comparable runs in Python or TypeScript, or explore the [example project](/docs/demo).

## Choose comparable runs [#choose-runs]

Open [Experiments](https://cloud.langfuse.com/project/~/experiments), select the runs to compare, and open the comparison view. Choose the reviewed release run as the baseline.

  ![Three experiment runs selected in the Experiments table with the Compare button available](/images/docs/experiment-comparison-selection.png)

For a release decision, use the same dataset version and evaluator definitions for baseline and candidate. Record the application commit, prompt or model version, and evaluator version in experiment metadata. A dataset version fixes the test data; it does not make model outputs deterministic.

You can compare runs from different data sources, but first check that the cases represent the same inputs and expected outputs. A missing case is not a passing case. For local data, preserve case identifiers in your test artifacts so your CI policy can match cases explicitly.

## Inspect scores and outputs [#inspect-results]

Review score, cost, and latency differences to identify tradeoffs. An improvement in average quality can hide a regression on a critical case.

| Case                    | Baseline | Candidate | Decision                   |
| ----------------------- | -------- | --------- | -------------------------- |
| Standard refund policy  | Pass     | Fail      | Investigate the regression |
| Sale-item refund policy | Fail     | Pass      | Review the improvement     |

Both runs above have 50% accuracy. The average alone does not tell you whether the candidate is safe to release.

Use score thresholds in the comparison view to narrow the results, then inspect the baseline and candidate outputs side by side. Check the score explanation against the output. If an evaluator failed or returned no result, resolve that error before treating the comparison as complete.

  ![Experiment comparison showing inputs, outputs, evaluation scores, cost, and latency differences across three runs](/images/docs/experiment-comparison.png)

## Investigate and review failures [#review-failures]

Open the trace for a failing item. Inspect the application output and the intermediate retrievals, model calls, or tools that produced it. For example, an incorrect refund window might come from outdated retrieved policy text or from the model ignoring the correct policy.

  ![Experiment item trace open beside the comparison table, showing inputs, output, scores, and annotation controls](/images/docs/experiment-comparison-peek-view.png)

Separate application failures from evaluator mistakes. A good paraphrase can fail a string check; a fluent answer can still contain an unsupported claim. Use [human scores](/docs/evaluation/evaluation-methods/scores-via-ui) to record the review outcome and failure reason. Use [annotation queues](/docs/evaluation/evaluation-methods/annotation-queues) when review needs to be shared across a team.

If you change the evaluator after review, re-score both versions with the same updated definition. Keep the original experiment metadata so the decision can be reproduced.

## Turn the decision into a CI policy [#ci-policy]

Approve a baseline explicitly and record its identity with the dataset and evaluator versions. Do not automatically replace it with every successful candidate. A useful policy combines minimum aggregate scores with checks for newly failing critical cases and incomplete results.

See [Experiments in CI/CD](/docs/evaluation/experiments/experiments-ci-cd#approved-baseline) for an example. The baseline approval and gate policy live in your repository; choosing a baseline in the comparison UI does not configure a CI gate.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/evaluation/experiments/compare-experiments.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

