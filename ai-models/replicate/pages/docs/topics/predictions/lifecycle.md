---
title: "Prediction lifecycle"
source: https://replicate.com/docs/topics/predictions/lifecycle.md
path: docs/topics/predictions/lifecycle
---

Whenever you run a model, you’re creating a [prediction](/docs/topics/predictions).

Some models run very quickly and can return a result within a few milliseconds. Other models can take longer to run, especially generative models, like the kind that produce [images from text prompts](https://replicate.com/collections/text-to-image).

[](#prediction-statuses)Prediction statuses
-------------------------------------------

Predictions can have any of the following statuses:

*   `starting`: the prediction is starting up. If this status lasts longer than a few seconds, then it’s typically because a new worker is being started to run the prediction. Refer to [cold boots](/docs/topics/models/run-a-model#warm-models).
*   `processing`: the `predict()` method of the model is currently running.
*   `succeeded`: the prediction completed successfully.
*   `failed`: the prediction encountered an error during processing.
*   `canceled`: the prediction was canceled by the user or exceeded its deadline after starting.
*   `aborted`: the prediction exceeded its deadline before it could start running.

[](#timeouts)Timeouts
---------------------

Predictions time out after running for 30 minutes. If you require more than 30 minute timeouts for predictions, [contact us](https://replicate.com/support).

You can also set a deadline to automatically cancel a prediction if it doesn’t complete within a specified duration. This is useful for building applications where you need to decide when to stop waiting and move on - for example, showing a timeout message to users or switching to an alternative workflow.

What happens when a prediction exceeds its deadline depends on whether it had started running:

*   **Before starting**: The status changes to `aborted`
*   **After starting**: The status changes to `canceled`

### [](#billing-for-predictions-with-deadlines)Billing for predictions with deadlines

You’re billed based on whether the prediction had started running:

*   **Aborted** (never started): No charge
*   **Canceled** (started running): You pay for the time the prediction ran before it was canceled

This means you only pay for compute resources that were actually used.

[](#monitoring-predictions)Monitoring predictions
-------------------------------------------------

When you’re logged in, you can view a list of your predictions on the [dashboard](https://replicate.com/dashboard), with summaries of status, run time, etc.

For long-running models, you may want to poll the API or use [webhooks](/docs/topics/webhooks) to check the status of a prediction.

To learn more about how long predictions are stored with Replicate, refer to [Data retention](/docs/topics/predictions/data-retention).
