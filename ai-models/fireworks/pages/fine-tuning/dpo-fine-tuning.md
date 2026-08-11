---
title: "Preference Optimization with DPO or ORPO"
source: https://docs.fireworks.ai/fine-tuning/dpo-fine-tuning
path: fine-tuning/dpo-fine-tuning
---

Train on preferred and non-preferred response pairs using managed DPO or ORPO.

Preference optimization fine-tunes models on pairs of preferred and non-preferred responses to the same prompt. Managed jobs support two objectives:

* **DPO** compares the policy against a reference model.
* **ORPO** combines supervised and preference objectives without a separate reference model.

Use either method for:

* Aligning model outputs with brand voice, tone, or style guidelines
* Reducing hallucinations or incorrect reasoning patterns
* Improving response quality where there's no single "correct" answer
* Teaching models to follow specific formatting or structural preferences

## Fine-tuning with DPO or ORPO

<Steps>
  <Step title="Prepare dataset">
    Datasets must adhere strictly to the JSONL format, where each line represents a complete JSON-formatted training example.

    **Minimum Requirements:**

    * **Minimum examples needed:** 3
    * **Maximum examples:** Up to 3 million examples per dataset
    * **File format:** JSONL (each line is a valid JSON object)
    * **Dataset Schema:** Each training sample must include the following fields:
      * An `input` field containing a `messages` array, where each message is an object with two fields:
        * `role`: one of `system`, `user`, or `assistant`
        * `content`: a string representing the message content
      * A `preferred_output` field containing an assistant message with an ideal response
      * A `non_preferred_output` field containing an assistant message with a suboptimal response

    Here’s an example conversation dataset (one training example):

    ```json einstein_dpo.jsonl theme={null}
    {
      "input": {
        "messages": [
          {
            "role": "user",
            "content": "What is Einstein famous for?"
          }
        ],
        "tools": []
      },
      "preferred_output": [
        {
          "role": "assistant",
          "content": "Einstein is renowned for his theory of relativity, especially the equation E=mc²."
        }
      ],
      "non_preferred_output": [
        {
          "role": "assistant",
          "content": "He was a famous scientist."
        }
      ]
    }
    ```

    <Warning>
      We currently only support one-turn conversations for each example, where the preferred and non-preferred messages need to be the last assistant message.
    </Warning>

    Save this dataset as jsonl file locally, for example `einstein_dpo.jsonl`.
  </Step>

  <Step title="Create and upload the dataset">
    There are a couple ways to upload the dataset to Fireworks platform for fine tuning: `firectl`, `Restful API` , `builder SDK` or `UI`.

    <Tabs>
      <Tab title="UI">
        * You can simply navigate to the dataset tab, click `Create Dataset` and follow the wizard.

          <img alt="Dataset Pn" />
      </Tab>

      <Tab title="firectl">
        * Upload dataset using `firectl`

        ```bash theme={null}
        firectl dataset create <dataset-id> /path/to/file.jsonl
        ```
      </Tab>

      <Tab title="Restful API">
        You need to make two separate HTTP requests. One for creating the dataset entry and one for uploading the dataset. Full reference here: [Create dataset](/api-reference/create-dataset). Note that the `exampleCount` parameter needs to be provided by the client.

        ```jsx theme={null}
        // Create Dataset Entry
        const createDatasetPayload = {
          datasetId: "trader-poe-sample-data",
          dataset: { userUploaded: {} }
          // Additional params such as exampleCount
        };
        const urlCreateDataset = `${BASE_URL}/datasets`;
        const response = await fetch(urlCreateDataset, {
          method: "POST",
          headers: HEADERS_WITH_CONTENT_TYPE,
          body: JSON.stringify(createDatasetPayload)
        });
        ```

        ```jsx theme={null}
        // Upload JSONL file
        const urlUpload = `${BASE_URL}/datasets/${DATASET_ID}:upload`;
        const files = new FormData();
        files.append("file", localFileInput.files[0]);

        const uploadResponse = await fetch(urlUpload, {
          method: "POST",
          headers: HEADERS,
          body: files
        });
        ```
      </Tab>
    </Tabs>

    While all of the above approaches should work, `UI` is more suitable for smaller datasets `< 500MB` while `firectl` might work better for bigger datasets.

    Ensure the dataset ID conforms to the [resource id restrictions](/getting-started/concepts#resource-names-and-ids).
  </Step>

  <Step title="Create a DPO or ORPO Job">
    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        firectl dpo-job create \
          --loss-method DPO \
          --base-model accounts/account-id/models/base-model-id \
          --dataset accounts/my-account-id/datasets/my-dataset-id \
          --output-model new-model-id
        ```

        To try your account's reservation capacity before falling back to shared trainer capacity, add `--use-reservation`. For full-parameter DPO, policy and dedicated reference trainers try independently. The equivalent REST and Python SDK fields are `useReservation: true` and `use_reservation=True`.

        For ORPO, use the same preference dataset and select the ORPO objective:

        ```bash theme={null}
        firectl dpo-job create \
          --loss-method ORPO \
          --orpo-lambda <approved-value> \
          --base-model accounts/account-id/models/base-model-id \
          --dataset accounts/my-account-id/datasets/my-dataset-id \
          --output-model new-model-id
        ```

        Choose a base model that [Models](/fine-tuning/models) marks as DPO-enabled, and a shape published for it.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Monitor the preference job">
    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        firectl dpo-job get dpo-job-id
        ```
      </Tab>
    </Tabs>

    Once the job is complete, the `STATE` will be set to `JOB_STATE_COMPLETED`, and the fine-tuned model can be deployed.
  </Step>

  <Step title="Deploy the DPO fine-tuned model">
    Once training completes, you can create a deployment to interact with the fine-tuned model. Refer to [deploying a fine-tuned model](/fine-tuning/fine-tuning-models#deploying-a-fine-tuned-model) for more details.
  </Step>
</Steps>

## Next Steps

Explore other fine-tuning methods to improve model output for different use cases.

<CardGroup>
  <Card title="Supervised Fine Tuning - Text" icon="message" href="/fine-tuning/fine-tuning-models">
    Train models on input-output examples to improve task-specific performance.
  </Card>

  <Card title="Reinforcement Fine Tuning" icon="brain" href="/fine-tuning/reinforcement-fine-tuning-models">
    Optimize models using AI feedback for complex reasoning and decision-making.
  </Card>

  <Card title="Supervised Fine Tuning - Vision" icon="eye" href="/fine-tuning/fine-tuning-models#vision-fine-tuning">
    Fine-tune vision-language models to understand both images and text.
  </Card>
</CardGroup>
