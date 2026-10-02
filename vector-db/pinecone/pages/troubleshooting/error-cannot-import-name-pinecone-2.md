---
title: "Error: Cannot import name 'Pinecone' from 'pinecone'"
source: https://docs.pinecone.io/troubleshooting/error-cannot-import-name-pinecone
path: troubleshooting/error-cannot-import-name-pinecone
---

Fix the Python ImportError 'cannot import name Pinecone from pinecone' by upgrading the Pinecone Python SDK to 3.0.0 or later, with or without gRPC.

## Problem

When using an older version of the [Python SDK](https://github.com/pinecone-io/pinecone-python-client) (earlier than 3.0.0), trying to import the `Pinecone` class raises the following error:

```console console theme={null}
ImportError: cannot import name 'Pinecone' from 'pinecone'
```

## Solution

Upgrade the SDK version and try again:

```Shell Shell theme={null}
# If you're interacting with Pinecone via HTTP requests, use:
pip install pinecone --upgrade
```

```Shell Shell theme={null}
# If you're interacting with Pinecone via gRPC, use:
pip install "pinecone[grpc]" --upgrade
```
