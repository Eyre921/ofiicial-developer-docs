---
title: "Evaluations"
source: https://docs.together.ai/docs/ai-evaluations
path: docs/ai-evaluations
---

Use LLMs to classify, score, and compare model outputs on Together AI.

<Tip>Using a coding agent? Install the [together-evaluations](https://github.com/togethercomputer/skills/tree/main/skills/together-evaluations) skill to let your agent write correct evaluation code automatically. [Learn more](/docs/agent-skills).</Tip>

The Together AI evaluations API allows you to use LLMs as a judge to assess the outputs of other models. You describe how the judge should assess each input, and the service runs the judgments across your dataset and returns aggregated results.

You can evaluate Together AI [serverless models](/docs/evaluations-supported-models#serverless-models), models on your own [dedicated model inference](/docs/dedicated-endpoints/overview) endpoints, or external provider models such as OpenAI, Anthropic, and Google. Evaluations run from the [CLI or the SDKs](/docs/run-an-evaluation), or from the [web console](https://api.together.ai/evaluations).

## Evaluation types

Every evaluation uses one of three types. Choose the type that matches the question you are trying to answer.

### Classify

`classify` evaluations assign each input to one of the labels you define, such as `Toxic` and `Non-toxic`. You mark one or more labels as passing to get a pass percentage across the dataset.

Use `classify` when you need a categorical judgment, for example when moderating content, enforcing policy compliance, detecting intent, or filtering and curating a dataset.

### Score

`score` evaluations rate each input on a numeric scale that you define, such as 1 to 10. You set a pass threshold to get the percentage of inputs that meet a quality bar, along with the mean and standard deviation of scores.

Use `score` when quality is a matter of degree rather than a category, for example when rating helpfulness, factuality, or writing quality.

### Compare

`compare` evaluations judge two candidate responses for the same input and pick the better one, reporting how often each side wins and how often the judge finds a tie. By default, the judge runs twice with the candidate positions swapped to cancel out position bias.

Use `compare` when you're running an A/B test between two models, two prompts, or two configurations of the same model.

## Datasets and templates

Every evaluation runs over a dataset you upload as JSONL or CSV, where each row holds the same fields. Rows can carry a prompt to generate from, pre-generated responses to judge, or an `image_data_urls` column for vision inputs.

Jinja2 templates connect your dataset to the models. The `input_template` injects dataset columns into the prompt sent to the model being evaluated, and the `system_template` gives the judge or the generating model its instructions. Every dataset column must be used by the job (referenced in a template, holding pre-generated responses, or carrying images); jobs with unused columns fail validation. For the column rules, template syntax, and every parameter, see the [evaluations reference](/docs/evaluations-reference).

## Model sources

Both the judge and the models being evaluated can come from three sources:

* **Serverless:** A Together AI serverless model from the evaluations allowlist.
* **Dedicated:** A [dedicated model inference](/docs/dedicated-endpoints/overview) endpoint you have deployed, referenced by its endpoint ID (`ep_abc123`). The endpoint needs a running deployment.
* **External:** A model from an external provider, addressed with a shortcut or a custom OpenAI-compatible base URL.

For the full list of supported serverless models and external shortcuts, see [Supported models](/docs/evaluations-supported-models).

## Pricing

Evaluations bill only the serverless inference used by the job, at standard [serverless rates](https://www.together.ai/pricing). External models are billed by their provider through the API key you supply. Jobs run their requests concurrently; completion time depends on dataset size, model size, and current capacity. Small jobs (under 1,000 samples) typically complete in under an hour.

## Next steps

<CardGroup>
  <Card title="Run an evaluation" icon="player-play" href="/docs/run-an-evaluation">
    Prepare a dataset, launch a job, and download results with the API.
  </Card>

  <Card title="Parameters and results" icon="file-text" href="/docs/evaluations-reference">
    Parameters, result formats, and template syntax.
  </Card>

  <Card title="Supported models" icon="cpu" href="/docs/evaluations-supported-models">
    Serverless models and external provider shortcuts.
  </Card>
</CardGroup>
