---
title: "Understanding collections"
source: https://docs.pinecone.io/guides/indexes/pods/understanding-collections
path: guides/indexes/pods/understanding-collections
---

Legacy documentation for Pinecone collections, a pod-only feature for creating static index snapshots. Collections are not available for serverless indexes.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

A collection is a static copy of a pod-based index that only consumes storage. It is a non-queryable representation of a set of records. You can [create a collection](/guides/indexes/pods/back-up-a-pod-based-index) of a pod-based index, and you can [create a new pod-based index from a collection](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.

<Note>
  Once a collection is created, it cannot be moved to a different project.
</Note>

## Use cases

Creating a collection is useful when performing tasks like the following:

* Protecting an index from manual or system failures.
* Temporarily shutting down an index.
* Copying the data from one index into a different index.
* Making a backup of your index.
* Experimenting with different index configurations.

## Performance

Collections operations perform differently, depending on the pod type of the index:

* Creating a `p1` or `s1` index from a collection takes approximately 10 minutes.
* Creating a `p2` index from a collection can take several hours when the number of vectors is on the order of 1,000,000.

## Limitations

Collection limitations are as follows:

* You can only perform operations on collections in the current Pinecone project.

## Pricing

See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.
