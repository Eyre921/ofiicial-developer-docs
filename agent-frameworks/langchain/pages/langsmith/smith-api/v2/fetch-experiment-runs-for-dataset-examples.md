---
title: "Fetch experiment runs for dataset examples"
source: https://docs.langchain.com/langsmith/smith-api/v2/fetch-experiment-runs-for-dataset-examples
path: langsmith/smith-api/v2/fetch-experiment-runs-for-dataset-examples
---

/langsmith/langsmith-platform-openapi.json post /v2/datasets/{dataset_id}/experiment-runs
Returns a paginated page of dataset examples with runs from the requested experiments.
Response uses the canonical `{items, next_cursor}` envelope.
