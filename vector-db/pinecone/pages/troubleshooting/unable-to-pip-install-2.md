---
title: "Unable to pip install"
source: https://docs.pinecone.io/troubleshooting/unable-to-pip-install
path: troubleshooting/unable-to-pip-install
---

Resolve install issues for the Pinecone Python SDK: pick the right Python 3.x command, install pinecone or pinecone with gRPC, and upgrade to the latest.

Python `3.x` uses `pip3`. Use the following commands in your terminal to install the latest version of the [Pinecone Python SDK](/reference/sdks/python/overview):

```Shell Shell theme={null}
# If you are connecting to Pinecone via gRPC:
pip3 install -U pinecone[grpc]
```

```Shell Shell theme={null}
# If you are connecting to Pinecone via HTTP:
pip3 install -U pinecone
```
