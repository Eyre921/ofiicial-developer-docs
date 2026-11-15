---
title: "Get Dataset"
source: https://docs.fireworks.ai/api-reference/get-dataset
path: api-reference/get-dataset
---

get /v1/accounts/{account_id}/datasets/{dataset_id}
Retrieve metadata for an existing dataset in your Fireworks account.

> [!NOTE]
>
> Dataset creation, uploads, updates, validation, and downloads are retired on Fireworks. `GetDataset`, [List Datasets](/api-reference/list-datasets), and [Delete Dataset](/api-reference/delete-dataset) remain available to inspect metadata for and delete existing dataset records. For new training runs, load your data directly with the [Training API](/fine-tuning/training-api/introduction).
