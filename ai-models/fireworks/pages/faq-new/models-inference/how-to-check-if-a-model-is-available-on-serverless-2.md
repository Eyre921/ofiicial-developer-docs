---
title: "How to check if a model is available on serverless?"
source: https://docs.fireworks.ai/faq-new/models-inference/how-to-check-if-a-model-is-available-on-serverless
path: faq-new/models-inference/how-to-check-if-a-model-is-available-on-serverless
---

## Web UI

Go to [https://app.fireworks.ai/models?filter=LLM\&serverless=true](https://app.fireworks.ai/models?filter=LLM\&serverless=true)

## API

You can programmatically retrieve all serverless models using the [List Models API](/api-reference/list-models) with the `supports_serverless=true` filter.

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    # List all serverless models
    models = client.models.list(filter="supports_serverless=true")

    for model in models:
        print(model.name)
    ```

    You can also combine filters and customize the response:

    ```python theme={null}
    # List serverless models with pagination
    models = client.models.list(
        filter="supports_serverless=true",
        page_size=50,
    )

    for model in models:
        print(f"{model.name}: {model.display_name}")
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl "https://api.fireworks.ai/v1/accounts/fireworks/models?filter=supports_serverless%3Dtrue" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY"
    ```

    With pagination:

    ```bash theme={null}
    curl "https://api.fireworks.ai/v1/accounts/fireworks/models?filter=supports_serverless%3Dtrue&pageSize=50" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY"
    ```
  </Tab>
</Tabs>

The filter parameter uses the [AIP-160 filter syntax](https://google.aip.dev/160). The `supports_serverless` field indicates whether a model is available on serverless infrastructure.

<Tip>
  See the [List Models API reference](/api-reference/list-models) for all available parameters including `order_by`, `page_size`, and `read_mask`.
</Tip>
