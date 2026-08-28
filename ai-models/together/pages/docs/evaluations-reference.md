---
title: "Parameters and result formats"
source: https://docs.together.ai/docs/evaluations-reference
path: docs/evaluations-reference
---

Parameters, result formats, and template syntax for the evaluations API.

Reference for the parameters, result formats, and templates used by the evaluations API. For concepts, see [Evaluations](/docs/ai-evaluations); for the full request schema, see the [create evaluation](/reference/create-evaluation) API reference.

## Judge configuration

The `judge` object configures the model that assesses each input. It is required for every evaluation type.

| Parameter            | Type     | Default  | Description                                                                                                                                                          |
| -------------------- | -------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`              | `string` | required | Model ID, dedicated endpoint ID, or external shortcut for the judge.                                                                                                 |
| `model_source`       | `string` | required | One of `serverless`, `dedicated`, or `external`.                                                                                                                     |
| `system_template`    | `string` | required | Jinja2 template with the judge's assessment instructions.                                                                                                            |
| `external_api_token` | `string` | none     | Provider API token. Required when `model_source` is `external`.                                                                                                      |
| `external_base_url`  | `string` | none     | Custom OpenAI `chat/completions`-compatible base URL for external models.                                                                                            |
| `max_tokens`         | `int`    | `32768`  | Maximum tokens the judge can generate. Increase for reasoning models that spend output budget on chain-of-thought.                                                   |
| `temperature`        | `float`  | `0.05`   | Sampling temperature for the judge.                                                                                                                                  |
| `num_workers`        | `int`    | varies   | Concurrent judge inference workers. Defaults: `serverless` 25, `dedicated` 5 (minimum), `external` 2 with a provider shortcut or 20 when `external_base_url` is set. |

During execution, the service appends its own output-format instruction to the judge's prompt, requiring a JSON response with a `feedback` field and the verdict (a `label`, `score`, or choice). Judge responses that don't parse into a valid verdict are counted in `invalid_label_count` or `invalid_score_count` in the results.

## Model configuration

`model_to_evaluate`, `model_a`, and `model_b` each accept either a `string` naming a dataset column that already holds responses, or a model configuration object that generates fresh responses. The object uses these fields.

| Parameter            | Type     | Default  | Description                                                               |
| -------------------- | -------- | -------- | ------------------------------------------------------------------------- |
| `model`              | `string` | required | Serverless model ID, dedicated endpoint ID, or external shortcut.         |
| `model_source`       | `string` | required | One of `serverless`, `dedicated`, or `external`.                          |
| `system_template`    | `string` | required | Jinja2 template with generation instructions.                             |
| `input_template`     | `string` | required | Jinja2 template that formats the dataset input, for example `{{prompt}}`. |
| `max_tokens`         | `int`    | `1024`   | Maximum tokens for generation.                                            |
| `temperature`        | `float`  | `0.05`   | Sampling temperature for generation.                                      |
| `external_api_token` | `string` | none     | Provider API token. Required when `model_source` is `external`.           |
| `external_base_url`  | `string` | none     | Custom OpenAI-compatible base URL for external models.                    |
| `num_workers`        | `int`    | varies   | Concurrent inference workers, with the same defaults as the judge.        |

## Evaluation type parameters

Every type also requires `input_data_file_path`, the file ID of the uploaded dataset.

### Classify

| Parameter           | Type                 | Default  | Description                                                                           |
| ------------------- | -------------------- | -------- | ------------------------------------------------------------------------------------- |
| `labels`            | `list[string]`       | required | Classification categories the judge chooses from.                                     |
| `pass_labels`       | `list[string]`       | required | Labels counted as passing for the pass percentage. At least one label must be listed. |
| `model_to_evaluate` | `object` or `string` | required | Model configuration object, or a dataset column name.                                 |

### Score

| Parameter           | Type                 | Default  | Description                                                                                          |
| ------------------- | -------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `min_score`         | `float`              | required | Minimum score the judge can assign.                                                                  |
| `max_score`         | `float`              | required | Maximum score the judge can assign.                                                                  |
| `pass_threshold`    | `float`              | required | Score at or above which a sample is considered passing. Must be between `min_score` and `max_score`. |
| `model_to_evaluate` | `object` or `string` | required | Model configuration object, or a dataset column name.                                                |

### Compare

| Parameter                          | Type                 | Default  | Description                                                                                                                                                                                                              |
| ---------------------------------- | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model_a`                          | `object` or `string` | required | First model configuration object, or a dataset column name.                                                                                                                                                              |
| `model_b`                          | `object` or `string` | required | Second model configuration object, or a dataset column name.                                                                                                                                                             |
| `disable_position_bias_correction` | `boolean`            | `false`  | When `false`, the judge runs twice per sample with positions swapped and the verdicts are reconciled to cancel position bias. Set to `true` to run a single original-order pass, roughly halving judge cost and latency. |

When both `model_a` and `model_b` are configuration objects, their inference runs execute in parallel. Under the default two-pass correction, the winner is declared only when both passes agree; disagreement is recorded as a tie. If only one pass produces a parseable verdict, that verdict decides, and the row is flagged with `is_invalid_judge_output` in the result file.

## Dataset columns

Every column in the input dataset must be used by the job. A column counts as used when it is one of the following:

* **Template-referenced:** Injected with a `{{column_name}}` placeholder in any model or judge `system_template` or `input_template`. A nested reference like `{{info.question}}` counts for its top-level column, `info`.
* **A pre-generated response column:** Named as the string value of `model_to_evaluate`, `model_a`, or `model_b`.
* **The image column:** `image_data_urls`, for [vision evaluations](/docs/run-an-evaluation#prepare-a-dataset).

A dataset with any other column fails validation shortly after the job starts running, ending in `user_error` status with the offending columns listed in `results.error`:

```text Text theme={null}
Unsupported dataset column(s): ['category', 'id']. Each column must be referenced by a model or judge template, or be a recognized field ('image_data_urls'). Remove unused columns or reference them in a template.
```

Strip metadata columns such as `id` or `category` before uploading, or keep a column by referencing it in a template, for example passing `{{ground_truth}}` to the judge as a reference answer.

## Job lifecycle

Creating a job returns a `workflow_id` and a `pending` status. The job then moves through `queued` and `running` before reaching `completed`. A job that fails ends in `error` (an internal failure) or `user_error` (a problem with the request or dataset), with the failure reason in `results.error`. Retrieving the job returns the current status, a timestamped `status_updates` entry for each transition, the request `parameters`, and, once the job completes, the aggregated `results`:

```json JSON theme={null}
{
  "workflow_id": "eval-7df2-1751287840",
  "type": "compare",
  "status": "completed",
  "status_updates": [
    { "status": "pending", "message": "Job created and pending for processing", "timestamp": "2025-06-30T12:50:40.722334754Z" },
    { "status": "queued", "message": "Job status updated", "timestamp": "2025-06-30T12:50:47.476306172Z" },
    { "status": "running", "message": "Job status updated", "timestamp": "2025-06-30T12:51:02.439097636Z" },
    { "status": "completed", "message": "Job status updated", "timestamp": "2025-06-30T12:51:57.261327077Z" }
  ],
  "parameters": { "judge": { "model": "openai/gpt-oss-120b", "model_source": "serverless", "system_template": "..." }, "model_a": "response_a", "model_b": "response_b", "input_data_file_path": "file-64febadc-ef84-415d-aabe-1e4e6a5fd9ce" },
  "created_at": "2025-06-30T12:50:40.723521Z",
  "updated_at": "2025-06-30T12:51:57.261342Z",
  "results": {
    "A_wins": 1,
    "B_wins": 13,
    "Ties": 6,
    "generation_fail_count": 0,
    "judge_fail_count": 0,
    "result_file_id": "file-95c8f0a3-e8cf-43ea-889a-e79b1f1ea1b9"
  }
}
```

## Result formats

A completed job returns aggregated results and a `result_file_id`. The aggregated fields depend on the evaluation type.

### Classify

| Field                   | Type                  | Description                                                                   |
| ----------------------- | --------------------- | ----------------------------------------------------------------------------- |
| `error`                 | `string`              | Present only when the job fails.                                              |
| `label_counts`          | `object<string, int>` | Count of each assigned label, for example `{"positive": 45, "negative": 30}`. |
| `pass_percentage`       | `float`               | Percentage of samples with labels in `pass_labels`.                           |
| `generation_fail_count` | `int`                 | Failed generations when using a model configuration.                          |
| `judge_fail_count`      | `int`                 | Samples the judge could not evaluate.                                         |
| `invalid_label_count`   | `int`                 | Judge responses that could not be parsed into a valid label.                  |
| `result_file_id`        | `string`              | File ID for the row-level results.                                            |

### Score

| Field                               | Type     | Description                                          |
| ----------------------------------- | -------- | ---------------------------------------------------- |
| `error`                             | `string` | Present only when the job fails.                     |
| `aggregated_scores.mean_score`      | `float`  | Mean of all numeric scores.                          |
| `aggregated_scores.std_score`       | `float`  | Standard deviation of scores.                        |
| `aggregated_scores.pass_percentage` | `float`  | Percentage of scores meeting the pass threshold.     |
| `failed_samples`                    | `int`    | Total samples that failed processing.                |
| `invalid_score_count`               | `int`    | Scores outside the allowed range or unparseable.     |
| `generation_fail_count`             | `int`    | Failed generations when using a model configuration. |
| `judge_fail_count`                  | `int`    | Samples the judge could not evaluate.                |
| `result_file_id`                    | `string` | File ID for per-sample scores and feedback.          |

### Compare

| Field                   | Type     | Description                                  |
| ----------------------- | -------- | -------------------------------------------- |
| `error`                 | `string` | Present only when the job fails.             |
| `A_wins`                | `int`    | Count where model A was preferred.           |
| `B_wins`                | `int`    | Count where model B was preferred.           |
| `Ties`                  | `int`    | Count where the judge found no clear winner. |
| `generation_fail_count` | `int`    | Failed generations from either model.        |
| `judge_fail_count`      | `int`    | Samples the judge could not evaluate.        |
| `result_file_id`        | `string` | File ID for the detailed pairwise decisions. |

### Result files

Pass the `result_file_id` to the [Files API](/reference/get-files-id-content) to download the full report. Each line holds the original input, any generated responses, the judge's decision and feedback, and an `evaluation_successful` field (`true` or `false`) indicating whether the row was processed successfully. The result file retains every input row; if more than 30% of rows fail generation or judging, the job itself fails instead.

For large result files, stream the download line by line instead of buffering it:

```python Python theme={null}
from together import Together

client = Together()

with client.files.with_streaming_response.content(
    id=result_file_id
) as response:
    for line in response.iter_lines():
        print(line)
```

For a compare evaluation with generated responses, a result line looks like this:

```json JSON theme={null}
{
  "prompt": "What is the capital of France?",
  "MODEL_TO_EVALUATE_OUTPUT_A": "Paris.",
  "MODEL_TO_EVALUATE_OUTPUT_B": "The capital of France is Paris, a city on the Seine known for the Eiffel Tower and the Louvre.",
  "judge_raw_output_original": "{\"feedback\": \"Response B provides the same core information but adds useful context.\", \"choice\": \"B\"}",
  "judge_raw_output_flipped": "{\"feedback\": \"Response A adds useful context about location and landmarks.\", \"choice\": \"A\"}",
  "choice_original": "B",
  "judge_feedback_original_order": "Response B provides the same core information but adds useful context.",
  "choice_flipped": "B",
  "judge_feedback_flipped_order": "Response A adds useful context about location and landmarks.",
  "final_decision": "B",
  "evaluation_successful": true,
  "is_invalid_judge_output": false
}
```

The two `choice_*` and `judge_feedback_*` pairs come from the two position-bias-correction passes; `choice_flipped` is expressed in original-order terms, so the flipped pass's raw `"A"` above records the same winner. With `disable_position_bias_correction: true`, only the original-order fields are present. Classify and score result lines follow the same pattern, with the judge's `label` or `score` and `feedback` in place of the pairwise fields.

## Templates

Both `system_template` and `input_template` support [Jinja2](https://jinja.palletsprojects.com/en/stable/) syntax. Reference a dataset column by wrapping its name in double braces to inject its value into the prompt.

Given this dataset row:

```json JSON theme={null}
{ "prompt": "What is the capital of France?" }
```

And this template:

```python Python theme={null}
input_template = "Please answer the following question: {{prompt}}"
```

The rendered input becomes:

```text Text theme={null}
Please answer the following question: What is the capital of France?
```

Reference nested fields with dot notation. Given:

```json JSON theme={null}
{ "info": { "question": "What is the capital of France?", "answer": "Paris" } }
```

Access the nested field with:

```python Python theme={null}
input_template = "Please answer: {{info.question}}"
```

Common uses include passing a reference answer to the judge, giving per-row generation instructions, and selecting which columns to send to the model being evaluated.

For more Jinja2 functionality, see the [interactive template playground](https://huggingface.co/spaces/huggingfacejs/chat-template-playground) and the [Hugging Face templates guide](https://huggingface.co/blog/chat-templates).
