---
title: "Processing locations"
source: https://docs.pinecone.io/guides/indexes/processing-locations
path: guides/indexes/processing-locations
---

Learn where each hosted embedding and reranking model processes your text, and how to keep integrated embedding in the US.

A model's processing location is where it processes the text you send it. Every hosted model uses one of two locations:

* `global` means any of the provider's regions, including regions outside the United States.
* `us` means only regions in the United States.

Some models offer both, so you choose one with `processing_location` when you [declare an embedded field](/guides/search/integrated-embedding#declare-an-embedded-field).

## Locations by model

The Processing location column of the [model gallery](/models/overview) lists each model's location. Currently only `text-embedding-3-small` and `text-embedding-3-large` let you choose, between `global` (the default) and `us`. `gemini-embedding-2` processes in `global` and accepts `processing_location` only when it's set to `global`. Every other model rejects it.

The processing location doesn't follow your index's [cloud region](/guides/indexes/index-configuration#cloud-regions). An index in a region outside the US, such as `eu-west-1`, still defaults to `global`. On the Standard and Enterprise plans, it also accepts `us`.

## Set the processing location

`processing_location` is a property of an embedded field on a document index, set on `embed` next to `dimension`, so it requires API version `2026-07`. One value covers both stored text and queries. To keep both in the US, set it to `us`:

```json US processing theme={null}
{
  "chunk_text": {
    "type": "string",
    "embed": {
      "model": "text-embedding-3-large",
      "processing_location": "us"
    }
  }
}
```

These rules apply:

* The processing location is currently fixed at creation, like the rest of the embedding configuration. When you describe the index, the field's `embed.processing_location` shows the location the model uses now.
* On the Starter and Builder plans, `text-embedding-3-small` and `text-embedding-3-large` are limited to `global`. On the Standard and Enterprise plans, you can set `processing_location` to `us`.
* If your organization moves to the Builder plan, an index created with `us` keeps working but processes text in `global`, and describing or listing the index shows `global`. If you upgrade again, the index goes back to `us`.
* An index created with `us` can't be kept when you [downgrade to the Starter plan](/admin/billing/downgrade-billing-plan#before-you-downgrade). Recreate it with `global` and re-upsert your data before you downgrade.
* A location the model doesn't currently offer, such as `eu`, is rejected with a `400`.
* The [List models](/reference/api/latest/inference/list-available-models) operation lists `processing_location`, with its accepted values, in a model's `supported_parameters` on API version `2026-07` and later.
