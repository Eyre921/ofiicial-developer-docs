---
title: "Serverless index creation error - max serverless indexes"
source: https://docs.pinecone.io/troubleshooting/index-creation-error-max-serverless
path: troubleshooting/index-creation-error-max-serverless
---

Resolve the Pinecone serverless index creation error caused by hitting the 20-index project limit by deleting unused indexes or upgrading your plan.

## Problem

Each project is limited to 20 serverless indexes. Trying to create more than 20 serverless indexes in a project raises the following `403 (FORBIDDEN)` error:

```console console theme={null}
This project already contains 20 serverless indexes, the maximum per project. 
Delete any unused indexes and try again, or create a new project for more serverless indexes. 
For additional help, please contact support@pinecone.io.
```

## Solution

[Delete any unused serverless indexes](/guides/manage-data/manage-indexes#delete-an-index) in the project and try again, or create a new project to hold additional serverless indexes.

Also consider using [namespaces](/guides/index-data/indexing-overview#namespaces) to partition vectors of the same dimensionality within a single index. Namespaces can help speed up queries as well as comply with [multitenancy](/guides/index-data/implement-multitenancy) requirements.
