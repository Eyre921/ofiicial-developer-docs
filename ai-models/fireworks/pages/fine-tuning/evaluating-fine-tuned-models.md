---
title: "Evaluating Fine Tuned Models"
source: https://docs.fireworks.ai/fine-tuning/evaluating-fine-tuned-models
path: fine-tuning/evaluating-fine-tuned-models
---

Run training evals on a fine-tuned adapter before you create a production deployment.

After training, run evals on the adapter before you create a production deployment. The preemptible deployment on this page is for **training evals only**. It is not a production serving setup, and Fireworks does not offer serverless LoRA inference for a customer fine-tune.

<Warning>
  Do not send production traffic through a preemptible deployment. For production serving after eval, create an on-demand deployment. See [Deploying Fine Tuned Models](/fine-tuning/deploying-loras).
</Warning>

## Preemptible deployment

If you want to eval a fine-tuned model without holding dedicated on-demand capacity, create a **preemptible deployment**. It borrows idle reserved GPU capacity instead of reserving GPUs exclusively for you.

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

* `<FINE_TUNED_MODEL_ID>`: the fine-tuned model to eval, not a base model.
* `<YOUR_DEPLOYMENT_ID>` / `<YOUR_DISPLAY_NAME>`: a name of your choice for the eval deployment.
* `<DEPLOYMENT_SHAPE>`: the deployment shape to use for that model.

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

Check that the deployment is ready, then send eval requests to the fine-tuned model:

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

## Next steps

<CardGroup>
  <Card title="Deploying Fine Tuned Models" href="/fine-tuning/deploying-loras" icon="rocket">
    Live merge or multi-LoRA for production serving
  </Card>
</CardGroup>
