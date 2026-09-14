---
title: "Evaluating Trained Models"
source: https://docs.fireworks.ai/fine-tuning/evaluating-fine-tuned-models
path: fine-tuning/evaluating-fine-tuned-models
---

Evaluate a trained model before you create a production deployment.

After training, evaluate your model before you hold dedicated capacity for production serving. Choose an evaluation path based on the artifact you have and whether the training session is still active.

<Warning>
  These workflows are for **training evals and other non-production workloads only**. Do not send production or latency-sensitive traffic through them. For production serving after eval, create an on-demand deployment. See [Deploying Trained Models](/fine-tuning/deploying-loras).
</Warning>

## Which approach to use

Use the path that matches your current training stage:

* **Your serverless training session is still active:** use in-session sampling.
* **You have a promoted model ID:** use a preemptible deployment. This works regardless of whether the LoRA was trained with serverless, dedicated, or managed training, or imported.
* **Your dedicated training run is still active:** use its inference deployment and refresh it from sampler snapshots. See [Dedicated training and sampling](/fine-tuning/training-api/dedicated#training-and-sampling).

|                    | **In-session sampling**                                   | **Preemptible deployment**                                            |
| ------------------ | --------------------------------------------------------- | --------------------------------------------------------------------- |
| **Best for**       | Quick checks during an active serverless training session | Evaluating a promoted model without reserving dedicated GPUs          |
| **Training path**  | Serverless Training API only                              | Any training path                                                     |
| **Artifact**       | Sampler checkpoint from `save_weights_for_sampler`        | Promoted model (`accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>`) |
| **API**            | Training SDK `sampler.sample()`                           | Chat Completions or Fireworks SDK                                     |
| **Session bound?** | Yes                                                       | No                                                                    |

## In-session sampling (serverless training)

In-session sampling is available only during an active [serverless training](/fine-tuning/training-api/serverless) session, and the base model must be available in the [serverless pool](/fine-tuning/models). It does not evaluate an adapter produced by dedicated training after that run ends.

There is no serverless chat endpoint for your adapter. Open a **sampling client** bound to a sampler checkpoint. `sampler.sample()` generates completions from that checkpoint, which you score with your own metric.

Use the **sampler checkpoint** returned by `save_weights_for_sampler`, not a promoted model resource (`accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>`). Promoted models are for on-demand deployment and cannot be passed to `create_sampling_client`.

The following save-and-sample sequence comes from the [serverless quickstart](/fine-tuning/training-api/serverless#step-4-train-checkpoint-and-sample) and the cookbook [`serverless_rl` example](https://github.com/fw-ai/cookbook/blob/main/training/examples/serverless_rl/countdown_rl.py). Set up `prompt`, `tokenizer`, and `params` as shown in that example.

```python theme={null}
snapshot = training_client.save_weights_for_sampler("eval").result().path
sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
try:
    result = sampler.sample(
        prompt=prompt,
        num_samples=1,
        sampling_params=params,
    ).result()
    for seq in result.sequences or []:
        tokens = list(seq.tokens or [])
        completion = get_text_content(renderer.parse_response(tokens)[0])
        # Score `completion` against your held-out label or grader.
finally:
    sampler.close()
```

`sampler.sample(...)` is the evaluation call. Repeat it over held-out prompts, then close the sampler. The Countdown example scores with `composite_reward`; replace that with your evaluation metric.

For checkpoint and promotion details, see [Saving and loading checkpoints](/fine-tuning/training-api/serverless#saving-and-loading-checkpoints) on the serverless training page.

<Note>
  Sampler checkpoints live in the training session. If the session is gone, you cannot open a sampling client from that checkpoint. Promote checkpoints you need to retain, then evaluate the promoted model with a [preemptible deployment](#preemptible-deployment) below.
</Note>

## Preemptible deployment

If you want to evaluate a promoted model without holding dedicated on-demand capacity, create a **preemptible deployment**. It borrows idle reserved GPU capacity instead of reserving GPUs exclusively for you.

For LoRA, this includes adapters trained with serverless, dedicated, or managed training, as well as imported adapters. Point the deployment at your promoted fine-tuned model ID, not the base model.

It can be reclaimed (preempted) at any time. Fireworks does not guarantee how many GPUs are available or how long the deployment stays up, but in practice it typically lasts long enough to finish a training eval.

### How it works

Passing `--preemptible` to `firectl deployment create` opts the deployment into capacity borrowing:

* The deployment runs on reserved nodes that are currently idle.
* When the capacity owner needs those GPUs back, your deployment can be preempted.

Because it borrows idle capacity, you do not need to hold dedicated on-demand capacity for the duration of the eval.

### Requirements

`--preemptible` takes effect only on **firectl 1.7.26 or newer**. Check with `firectl version`. The flag is not present in older builds. Upgrade if you are below 1.7.26.

### Behavior

* **Training evals only.** A preemptible deployment can be preempted mid-request. Treat disappearance as a normal outcome, not an error.
* **`--preemptible` is immutable.** It is set at create time and cannot be toggled on or off afterward. To change it, delete the deployment and create a new one.
* **Clean up when done.** Delete the deployment after your eval so you stop holding the borrowed capacity.

### Create the deployment

```bash theme={null}
firectl deployment create accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID> \
  --deployment-id <YOUR_DEPLOYMENT_ID> \
  --display-name <YOUR_DISPLAY_NAME> \
  --deployment-shape <DEPLOYMENT_SHAPE> \
  --min-replica-count 1 \
  --max-replica-count 1 \
  --preemptible
```

Replace the placeholders:

* `<FINE_TUNED_MODEL_ID>`: the trained model to eval, not a base model.
* `<YOUR_DEPLOYMENT_ID>` / `<YOUR_DISPLAY_NAME>`: a name of your choice for the eval deployment.
* `<DEPLOYMENT_SHAPE>`: the deployment shape to use for that model. Find one with `firectl deployment-shape-version match --model accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>` — for fine-tuned models, the server matches shapes against the model's base model. See [Deployment shapes](/guides/ondemand-deployments#deployment-shapes).

### Worked example

```bash theme={null}
firectl deployment create accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID> \
  -a <ACCOUNT_ID> \
  --deployment-id <FINE_TUNED_MODEL_ID>-eval \
  --display-name <FINE_TUNED_MODEL_ID>-eval \
  --deployment-shape <DEPLOYMENT_SHAPE> \
  --min-replica-count 1 \
  --max-replica-count 1 \
  --preemptible
```

### Run the eval and tear down

Check that the deployment is ready, then send eval requests to the trained model:

```bash theme={null}
firectl deployment get <YOUR_DEPLOYMENT_ID> -a <ACCOUNT_ID>
```

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

When the evaluation is finished, delete the deployment to release the borrowed capacity:

```bash theme={null}
firectl deployment delete <YOUR_DEPLOYMENT_ID> -a <ACCOUNT_ID>
```

For more on preemptible capacity and guarantees, see [Preemptible deployments](/guides/ondemand-deployments#preemptible-deployments-eval-batch) in the on-demand deployments guide.

## Next steps

<CardGroup>
  <Card title="Deploying Trained Models" href="/fine-tuning/deploying-loras" icon="rocket">
    Live merge or multi-LoRA for production serving
  </Card>
</CardGroup>
