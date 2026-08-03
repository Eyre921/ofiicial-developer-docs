---
title: "Create a shared volume"
source: https://docs.together.ai/reference/clusters_storages-create
path: reference/clusters_storages-create
---

openapi.yaml POST /compute/clusters/storage/volumes
Instant Clusters supports long-lived, resizable in-DC shared storage with user data persistence.
You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.
All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.
