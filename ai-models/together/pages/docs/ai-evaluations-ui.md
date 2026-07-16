---
title: "AI evaluations UI"
source: https://docs.together.ai/docs/ai-evaluations-ui
path: docs/ai-evaluations-ui
---

Guide to using the AI Evaluations UI for model assessment

## Introduction

This guide explains how to perform evaluations using the Together AI UI.

<Info>
  For a comprehensive guide with detailed parameter descriptions and API examples, see [AI Evaluations](/docs/ai-evaluations).
</Info>

## Step 1: Upload Your Dataset

Navigate to [https://api.together.ai/evaluations](https://api.together.ai/evaluations) and click "Create Evaluation".

<Frame>
  <img alt="Create Evaluation button" />
</Frame>

Upload your dataset or select one from your library. Preview your dataset content in the "Dataset Preview" section.

<Frame>
  <img alt="Dataset upload interface" />
</Frame>

## Step 2: Customize Your Evaluation Job

### Evaluation Types

| Type         | Description                                                           |
| :----------- | :-------------------------------------------------------------------- |
| **Classify** | Categorizes input into one of the provided categories                 |
| **Score**    | Evaluates input and produces a score within a specified range         |
| **Compare**  | Compares responses from two models to determine which performs better |

### Judge Configuration

Configure the judge model that will evaluate your inputs:

| Field             | Type            | Required | Description                                   |
| :---------------- | :-------------- | :------- | :-------------------------------------------- |
| `judge model`     | string          | Yes      | The model used for evaluation                 |
| `system template` | Jinja2 template | Yes      | Instructions for the judge to assess the data |

<Frame>
  <img alt="Judge configuration interface" />
</Frame>

### Evaluation Type Parameters

**Classify parameters:**

| Field               | Type             | Description                                                                 |
| :------------------ | :--------------- | :-------------------------------------------------------------------------- |
| `labels`            | list of strings  | Categories for classification. Mark each as 'pass' or 'fail' for statistics |
| `model_to_evaluate` | object or string | Model configuration or dataset column name                                  |

**Score parameters:**

| Field               | Type             | Description                                                |
| :------------------ | :--------------- | :--------------------------------------------------------- |
| `min_score`         | float            | Minimum score the judge can assign                         |
| `max_score`         | float            | Maximum score the judge can assign                         |
| `pass_threshold`    | float            | Score at or above which is considered "passing" (optional) |
| `model_to_evaluate` | object or string | Model configuration or dataset column name                 |

**Compare parameters:**

| Field     | Type             | Description                                       |
| :-------- | :--------------- | :------------------------------------------------ |
| `model_a` | object or string | First model configuration or dataset column name  |
| `model_b` | object or string | Second model configuration or dataset column name |

### Model Evaluation Configuration

Choose how to provide responses for evaluation:

* **Configure** – Generate new responses using a model
* **Field name** – Use existing responses from your dataset

#### Option 1: Model Configuration Object

Use when generating new responses for evaluation:

| Field                | Type            | Required      | Description                                                                             |
| :------------------- | :-------------- | :------------ | :-------------------------------------------------------------------------------------- |
| `model_name`         | string          | Yes           | One of our [supported models](/docs/evaluations-supported-models)                       |
| `model_source`       | string          | Yes           | `"serverless"`, `"dedicated"`, or `"external"`                                          |
| `system_template`    | Jinja2 template | Yes           | Generation instructions (see [Templates](/docs/ai-evaluations#understanding-templates)) |
| `input_template`     | Jinja2 template | Yes           | Input format, e.g., `"{{prompt}}"`                                                      |
| `max_tokens`         | integer         | No            | Maximum tokens for generation                                                           |
| `temperature`        | float           | No            | Temperature setting for generation                                                      |
| `external_api_token` | string          | When external | API bearer token for external providers                                                 |
| `external_base_url`  | string          | No            | Custom base URL for external APIs                                                       |

#### Option 2: Column Reference

Use when evaluating pre-existing data from your dataset. Simply specify the column name containing the data to evaluate.

<Frame>
  <img alt="Model configuration interface" />
</Frame>

### Using External Models

<Info>
  When using `model_source = "external"`:

  * Enter a supported shortcut (e.g., `openai/gpt-5`). See [Supported External Models](/docs/evaluations-supported-models).
  * Provide your `external_api_token` for the provider.
  * Optionally set `external_base_url` for custom OpenAI `chat/completions`-compatible endpoints.
</Info>

For dedicated model inference, set `model_source = "dedicated"` and paste your endpoint ID into the model field. See [dedicated model inference](/docs/dedicated-endpoints/overview).

## Step 3: Monitor Job Progress

Wait for your evaluation job to complete. The UI will show the current status of your job.

<Frame>
  <img alt="Job progress monitoring" />
</Frame>

## Step 4: Review Results

Once complete, you can:

* Preview statistics and responses in the Dataset Preview
* Download the result file using the "Download" button

<Frame>
  <img alt="Results preview" />
</Frame>
