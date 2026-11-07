---
title: "Distributed Architecture"
source: https://docs.trychroma.com/reference/architecture/distributed
path: reference/architecture/distributed
---

How Chroma scales out with independent services, object storage, SSD caches, and a shared system database.

Distributed Chroma is designed for large-scale production workloads. Its components run as independent services so the system can scale horizontally while keeping a consistent API for clients.

## Core Components

Regardless of deployment mode, Chroma is composed of five core components. Each plays a distinct role in the system and operates over the shared [Chroma data model](#chroma-data-model).

![Chroma system architecture](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/system-diagram-light.png?fit=max\&auto=format\&n=2QFLJScSYa9JT1WU\&q=85\&s=8230cb5c91cdfb4f17336accd059d2e7)

### The Gateway

The gateway is the entrypoint for client traffic.

* Exposes a consistent API across all deployment modes.
* Handles authentication, rate limiting, quota management, and request validation.
* Routes requests to downstream services.

### The Log

The log is Chroma's write-ahead log.

* Records writes before they are acknowledged to clients.
* Ensures atomicity across multi-record writes.
* Provides durability and replay semantics.

### The Query Executor

The query executor is responsible for all read operations.

* Runs vector similarity, full-text, and metadata search.
* Maintains a mix of in-memory and on-disk indexes.
* Coordinates with the log to serve consistent results.

### The Compactor

The compactor periodically builds and maintains indexes.

* Reads from the log and produces updated vector, full-text, and metadata indexes.
* Writes materialized index data to storage.
* Updates the system database with metadata about new index versions.

### The System Database

The system database is Chroma's internal catalog.

* Tracks tenants, databases, collections, and their metadata.
* Stores cluster metadata in distributed deployments.
* Is backed by a SQL database.

## Runtime And Storage

In distributed mode, Chroma's components are deployed independently.

* The log and built indexes are stored in cloud object storage.
* The system catalog is backed by a SQL database.
* Services use local SSDs as caches to reduce object storage latency and cost.

This design separates compute from storage and lets Chroma scale collections and traffic without tying the whole system to a single machine.

## Read Path

![Chroma read path](https://mintcdn.com/chroma-8943dec5/OHTRZei6ss2glLVb/images/read-path-light.png?fit=max\&auto=format\&n=OHTRZei6ss2glLVb\&q=85\&s=cac0a618b57dc23bc15ec2387d4bcac2)

**Step 1**

A request arrives at the gateway, where it is authenticated, checked against quota limits, rate limited, and transformed into a logical plan.

**Step 2**

The gateway routes the plan to the relevant query executor. In distributed Chroma, rendezvous hashing on the collection ID is used to route the query to the correct nodes and preserve cache coherence.

**Step 3**

The query executor transforms the logical plan into a physical plan, reads from its storage layer, and consults the log to serve a consistent result.

**Step 4**

The result is returned to the gateway and then to the client.

## Write Path

![Chroma write path](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/write-path-light.png?fit=max\&auto=format\&n=2QFLJScSYa9JT1WU\&q=85\&s=a791ab900059c0d1592050a45ea98578)

**Step 1**

A request arrives at the gateway and is transformed into a log of operations.

**Step 2**

The operations are forwarded to the write-ahead log for persistence.

**Step 3**

After the log persists the write, the gateway acknowledges the request.

**Step 4**

The compactor periodically reads from the log and builds new vector, full-text, and metadata index versions.

**Step 5**

New index versions are written to storage and registered in the system database.

## Tradeoffs

Distributed Chroma is built on object storage to provide durable, low-cost storage at large scale. Object storage can deliver very high throughput, but it also introduces a higher baseline latency than local disk.

To reduce that latency penalty, Chroma aggressively uses SSD caching. When a collection is first queried, a subset of the required data is fetched from object storage, which can add cold-start latency. As the SSD cache warms, queries can be served from local cache instead of repeatedly hitting object storage.
