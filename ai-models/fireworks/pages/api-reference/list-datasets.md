---
title: "List Datasets"
source: https://docs.fireworks.ai/api-reference/list-datasets
path: api-reference/list-datasets
---

get /v1/accounts/{account_id}/datasets
List metadata for existing datasets in your Fireworks account.

> [!NOTE]
>
> Dataset creation, uploads, updates, validation, and downloads are retired on Fireworks. `ListDatasets`, [Get Dataset](/api-reference/get-dataset), and [Delete Dataset](/api-reference/delete-dataset) remain available to inspect metadata for and delete existing dataset records. For new training runs, load your data directly with the [Training API](/fine-tuning/training-api/introduction).
