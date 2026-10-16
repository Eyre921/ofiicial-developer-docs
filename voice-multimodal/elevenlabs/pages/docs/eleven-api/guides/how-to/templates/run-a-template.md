---
title: "Run your team's template"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/templates/run-a-template.md
path: docs/eleven-api/guides/how-to/templates/run-a-template
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run your team's template

> **Note**
>
> **How-to guide** · Assumes you have completed the [Templates quickstart](/docs/eleven-api/guides/cookbooks/templates).

This guide covers running a template your team built: copying its code, passing each kind of input, choosing which webhooks receive the result, pinning a version and reading the outputs.

## Before you begin

* The template is shared with your workspace. Its author sets this under **Workspace** in the template's sharing options; a template shared as **Just me** only runs for its author.
* Your workspace has a webhook subscribed to template runs. [Before you begin](/docs/eleven-api/guides/how-to/image-and-video/webhooks#before-you-begin) in the Image & Video webhooks guide sets one up.
* Your workspace is on a Pro plan or above, and your API key has the **Image & Video** permission.

## Copy the template's code

Open the template in the ElevenLabs app and select its **API** tab. In Flows, the template's author can open the same code from the **API** button in the template's sidebar.

The tab builds its snippets from the template's published inputs and outputs. Under **Choose how to get the result**, select **Webhook**, then select **Python** or **TypeScript** above the code. The tab shows a **Start a run** snippet and a **Handle the result** snippet. Copy **Start a run** to where your application starts runs, and **Handle the result** into your webhook handler. Each placeholder in **Start a run** stands for one input, and **Handle the result** reads each output by its id.

> **Note**
>
> The tab warns when the template uses a model the API does not offer. If no published version can
> run through the API, it shows no snippets; if only the latest one cannot, the snippets run the
> newest version that can. In Flows, the author selects **Show on canvas** in the warning to
> highlight those nodes, switches each one to an [available model](/docs/eleven-api/guides/cookbooks/image-and-video#available-models), and publishes again.

## Pass each input

Every input of the version you run must be given a value, keyed by the input's id. What the value looks like depends on the input's type:

| Input type                     | Value                                                                       |
| ------------------------------ | --------------------------------------------------------------------------- |
| `string`                       | The text itself.                                                            |
| `number`, `integer`, `boolean` | A JSON value of that type.                                                  |
| `image`, `video`, `audio`      | A reference to an uploaded asset, a previous generation, or base64 data.    |
| `voice`                        | A reference to a voice in your workspace.                                   |
| `array`                        | A list with one value per element, each in the form its element type takes. |

Inputs of type `object` cannot be passed through the API yet; the API tab warns about them.

```python
run = client.flows.templates.runs.create(
    template_id="Yz4DETxRv4uXyIo5PnEy",
    version_id="Kqs4nRrpndEjQ54BhbwE",
    inputs={
        "headline": "Autumn collection, 20% off",
        "duration_secs": 8,
        "product_photo": TemplateInputReference_Asset(asset_id="Rk3pQm8vTzL1yWcN0bJd"),
        "previous_shot": TemplateInputReference_Generation(generation_id="JWr5N6X9ZTqf8jD2LmQb"),
        "phone_photo": TemplateInputReference_InlineBase64(
            content_base_64=photo,
            mime_type="image/jpeg",
        ),
        "narrator": TemplateInputReference_Voice(voice_id="JBFqnCBsd6RMkjVDRZzb"),
    },
    webhook=WebhookTarget_All(),
)
```

```typescript
const run = await client.flows.templates.runs.create("Yz4DETxRv4uXyIo5PnEy", {
  versionId: "Kqs4nRrpndEjQ54BhbwE",
  inputs: {
    headline: "Autumn collection, 20% off",
    duration_secs: 8,
    product_photo: { type: "asset", assetId: "Rk3pQm8vTzL1yWcN0bJd" },
    previous_shot: { type: "generation", generationId: "JWr5N6X9ZTqf8jD2LmQb" },
    phone_photo: {
      type: "inline_base64",
      contentBase64: photo.toString("base64"),
      mimeType: "image/jpeg",
    },
    narrator: { type: "voice", voiceId: "JBFqnCBsd6RMkjVDRZzb" },
  },
  webhook: { type: "all" },
});
```

Input ids keep the spelling the template gives them in both SDKs; only the fields of a reference, such as `assetId`, are camelCased in TypeScript.

Base64 data is limited to 25 MB once decoded and is not kept after the run. To pass the same file to many runs, upload it once and pass its asset ID, as described in [References and assets](/docs/eleven-api/guides/how-to/image-and-video/references).

## Get the result

A [webhook](/docs/eleven-api/resources/webhooks) receives the finished run as a `flows_template_run` event. The API tab's **Webhook** snippets pass `{"type": "all"}`, which sends the finished run to every webhook in the workspace that is subscribed to template runs. To send it to specific webhooks, list their IDs:

```python
webhook=WebhookTarget_Ids(ids=["Q8mVr2LpXcT4nB6yJdKw"])
```

```typescript
webhook: { type: "ids", ids: ["Q8mVr2LpXcT4nB6yJdKw"] }
```

Each listed webhook must be subscribed to template runs. A run that asks for a webhook when none is subscribed is rejected, so a run never finishes with nowhere to deliver its result.

For a one-off script or batch job, `create_and_wait`, used in the [Templates quickstart](/docs/eleven-api/guides/cookbooks/templates), waits for the run to finish instead.

## Pin a version

The snippets pass the `version_id` of the newest published version the API can run. Keep it pinned: when the author publishes again, a pinned run keeps running the version you tested, while `latest` switches to the new one, which can rename or add inputs.

To move to a new version, open the API tab again, compare its inputs with the ones your code passes, and update `version_id`. To check from code instead, `flows.templates.get` returns the template's published versions the API can run, newest first, each with its inputs and outputs.

## Read the outputs

The finished run's `outputs` has one entry per output of the template, keyed by the output's id. Each output has its own `status`, so one output can fail while the others complete. A failed output carries `failure_reason` and `error_message`. A completed media output carries `content_url` and `content_mime_type`, and a completed `string` output carries `content`.

```python
run = TemplateRunResponse.model_validate(event["data"])

for output_id, output in run.outputs.items():
    if output.status == "failed":
        print(output_id, "failed:", output.failure_reason, output.error_message)
    elif output.type == "image" or output.type == "video" or output.type == "audio":
        print(output_id, output.content_url, output.content_mime_type)
    elif output.type == "string":
        print(output_id, output.content)
```

```typescript
const run = event.data;

for (const [outputId, output] of Object.entries(run.outputs)) {
  if (output.status === "failed") {
    console.error(outputId, "failed:", output.failure_reason, output.error_message);
  } else if (output.type === "image" || output.type === "video" || output.type === "audio") {
    console.log(outputId, output.content_url, output.content_mime_type);
  } else if (output.type === "string") {
    console.log(outputId, output.content);
  }
}
```

`constructEvent` in the TypeScript SDK returns the event's JSON as sent, so its fields are snake_case.

See [Delivery behavior](/docs/eleven-api/guides/how-to/image-and-video/webhooks#delivery-behavior) for retries and duplicate events.
