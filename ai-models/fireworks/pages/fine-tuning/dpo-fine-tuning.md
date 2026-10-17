---
title: "Preference Optimization with DPO or ORPO"
source: https://docs.fireworks.ai/fine-tuning/dpo-fine-tuning
path: fine-tuning/dpo-fine-tuning
---

Train Fireworks-hosted models on preferred and non-preferred response pairs using managed DPO or ORPO preference optimization, with LoRA or full-parameter.

Preference optimization trains models on pairs of preferred and non-preferred responses to the same prompt. Managed jobs support two objectives:

* **DPO** compares the policy against a reference model.
* **ORPO** combines supervised and preference objectives without a separate reference model.

Use either method for:

* Aligning model outputs with brand voice, tone, or style guidelines
* Reducing hallucinations or incorrect reasoning patterns
* Improving response quality where there's no single "correct" answer
* Teaching models to follow specific formatting or structural preferences

## Training with DPO or ORPO

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

  <Step title="Upload the dataset">
    Upload the dataset with the Fireworks UI, `firectl`, or the REST API.

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
      <Tab title="UI">
        In the `Training` tab, click `New job` and choose **Direct Preference**, which is how the UI labels DPO. Select your base model and preference dataset, then follow the wizard.
      </Tab>

      <Tab title="firectl">
        ```bash theme={null}
        firectl dpo-job create \
          --loss-method DPO \
          --base-model accounts/account-id/models/base-model-id \
          --dataset accounts/my-account-id/datasets/my-dataset-id \
          --output-model new-model-id
        ```

        For ORPO, use the same preference dataset and select the ORPO objective:

        ```bash theme={null}
        firectl dpo-job create \
          --loss-method ORPO \
          --orpo-lambda <approved-value> \
          --base-model accounts/account-id/models/base-model-id \
          --dataset accounts/my-account-id/datasets/my-dataset-id \
          --output-model new-model-id
        ```
      </Tab>

      <Tab title="REST API">
        ```bash theme={null}
        curl -X POST "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/dpoJobs" \
          -H "Authorization: Bearer $FIREWORKS_API_KEY" \
          -H "Content-Type: application/json" \
          -d '{
            "dataset": "accounts/<ACCOUNT_ID>/datasets/<DATASET_ID>",
            "trainingConfig": {
              "baseModel": "accounts/fireworks/models/<BASE_MODEL_ID>",
              "outputModel": "accounts/<ACCOUNT_ID>/models/<OUTPUT_MODEL_ID>",
              "loraRank": 8
            },
            "lossConfig": {"method": "DPO"}
          }'
        ```

        For ORPO, set `"method": "ORPO"`. If `lossConfig` is omitted, the job uses DPO.
      </Tab>

      <Tab title="Python SDK">
        ```python theme={null}
        from fireworks import Fireworks

        client = Fireworks()  # reads FIREWORKS_API_KEY and FIREWORKS_ACCOUNT_ID

        job = client.dpo_jobs.create(
            dataset="accounts/<ACCOUNT_ID>/datasets/<DATASET_ID>",
            training_config={
                "base_model": "accounts/fireworks/models/<BASE_MODEL_ID>",
                "output_model": "accounts/<ACCOUNT_ID>/models/<OUTPUT_MODEL_ID>",
                "lora_rank": 8,
            },
            loss_config={"method": "DPO"},  # "ORPO" for ORPO
        )
        print(job.name)
        ```
      </Tab>
    </Tabs>

    `firectl` trains a LoRA adapter with rank 8 by default. With the REST API or the Python SDK, always set the rank to train a LoRA adapter: `trainingConfig.loraRank` in the job body, or `training_config={"lora_rank": 8}` in `dpo_jobs.create(...)`. An omitted rank is sent as 0, which requests full-parameter training.

    Reservation placement is off unless you request it: add `--use-reservation` with firectl, set `useReservation: true` in the REST body, or pass `use_reservation=True` to `dpo_jobs.create(...)` in the Python SDK. With a matching active reservation, the job runs only on that reservation, not on shared capacity; without one, the setting is ignored. For full-parameter DPO, policy and dedicated reference trainers try independently.

    Choose a base model that [Models](/fine-tuning/models) marks as DPO-enabled, and a shape published for it.
  </Step>

  <Step title="Monitor the preference job">
    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        firectl dpo-job get dpo-job-id
        ```
      </Tab>

      <Tab title="REST API">
        ```bash theme={null}
        curl "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/dpoJobs/<DPO_JOB_ID>" \
          -H "Authorization: Bearer $FIREWORKS_API_KEY"
        ```
      </Tab>

      <Tab title="Python SDK">
        ```python theme={null}
        job = client.dpo_jobs.get("<DPO_JOB_ID>")
        print(job.state)
        ```
      </Tab>
    </Tabs>

    Once the job is complete, the state is `JOB_STATE_COMPLETED`, and the trained model can be deployed.
  </Step>

  <Step title="Deploy the DPO trained model">
    Once training completes, you can create a deployment to interact with the trained model. Refer to [deploying a trained model](/fine-tuning/fine-tuning-models#deploying-a-trained-model) for more details. Deployments scale to zero when idle, and the first request after that returns 503 while the deployment scales back up; see [Scaling from zero behavior](/deployments/autoscaling#scaling-from-zero-behavior).
  </Step>
</Steps>

## Next Steps

Explore other training methods to improve model output for different use cases.

<CardGroup>
  <Card title="Supervised Fine-Tuning - Text" icon="message" href="/fine-tuning/fine-tuning-models">
    Train models on input-output examples to improve task-specific performance.
  </Card>

  <Card title="Reinforcement Learning" icon="brain" href="/fine-tuning/training-api/cookbook/rl">
    Optimize models against a reward function on the Training API.
  </Card>

  <Card title="Supervised Fine-Tuning - Vision" icon="eye" href="/fine-tuning/fine-tuning-models#vision-training">
    Train vision-language models to understand both images and text.
  </Card>
</CardGroup>
