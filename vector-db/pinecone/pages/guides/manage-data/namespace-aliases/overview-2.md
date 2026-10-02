---
title: "Namespace aliases overview"
source: https://docs.pinecone.io/guides/manage-data/namespace-aliases/overview
path: guides/manage-data/namespace-aliases/overview
---

A namespace alias is a stable name for a namespace that you can repoint at any time, switching the data your application reads without a code change or redeploy.

<Note>
  Creating and managing aliases requires API version `2026-07` or later and is available through the REST API and the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Reading through an alias works on any API version, including the current SDKs.
</Note>

A **namespace alias** is a stable, repointable name inside an index that points at a [namespace](/guides/index-data/indexing-overview#namespaces). An alias holds no data of its own. It's a pointer. Your application reads through the alias name, and you can atomically repoint the alias to a different namespace in the same index at any time, with no application config change and no redeploy.

Without an alias, changing what data an application reads means loading it into a new namespace, then editing the namespace name in your application and redeploying. With an alias, you point your application at the alias once, and every later cutover is a single API call.

Writes (upsert, update, and delete) always address a namespace name directly, never the alias, so your ingest target and your live read target stay separate during a cutover.

To put an alias to work, see [Swap a namespace](/guides/manage-data/namespace-aliases/swap-a-namespace) and [Manage aliases](/guides/manage-data/namespace-aliases/manage-aliases).

## How aliases work

An alias lives on the [index host](/guides/manage-data/target-an-index), scoped to a single index alongside the namespaces it can point to, so alias operations use the same host as your namespace and data operations. You can pass an alias name wherever a read request takes a namespace name (the `namespace` field in the body, the `namespace` query parameter, or the `{namespace}` path segment), and Pinecone resolves it to the target namespace server-side. Resolution covers every read endpoint: query, vector fetch, fetch by metadata, and list; record search; and document search, fetch, and list.

Everything else addresses the namespace directly. Writes (upsert, update, and delete) sent to an alias name are rejected, and so are namespace operations like describing or deleting a namespace. An alias is a separate resource with its own endpoints under `/namespace-aliases`, so you never manage a namespace through its alias, or an alias through the namespace endpoints. In each case the error names the alias and the namespace it points at, so you know to send the request to the namespace directly.

An alias name must be unique within the index and can't match a namespace name. Because the name appears in the request path, it also has to be URL-safe: ASCII graphic characters, no spaces or `/ ? # % & = \ ; +`, with `.`, `..`, and `__default__` reserved. An alias name can be up to 512 characters, the same limit as a namespace. So the two match on length, but an alias is stricter on allowed characters, since a namespace accepts almost any ASCII. An omitted or empty target is rejected, and an alias is ready the moment you create it, with no provisioning step to wait on.

## What aliases guarantee

* Writes always address a namespace directly, so your ingest target and live read target never blur.
* You can't delete a namespace while an alias points to it, and a failed repoint leaves the alias on its current target.
* Within an index, a name is either a namespace or an alias, never both.
* Reads report the namespace that served them, so you can confirm what an alias resolved to.

## Limits

* An alias can only target a namespace in the same index, so it shares the index's dimension and metric.
* An index can have up to 1,000 aliases.
* An alias is metadata only, so it costs nothing to keep. Reads through an alias bill as reads of the target namespace.
* Aliases are a separate resource from namespaces. They don't appear in namespace listings (`GET /namespaces`) or in `describe_index_stats`; list them with `GET /namespace-aliases`.
* Deleting an alias makes reads through that name return empty results, not an error, so move readers to a live name before you delete.
* Restoring an index from a backup creates a new index, so the original's aliases don't carry over.
* You manage aliases through the REST API or the Pinecone console, and reads through an alias work in the SDKs.
* Alias changes aren't in the audit log export.

## See also

* [Swap a namespace](/guides/manage-data/namespace-aliases/swap-a-namespace)
* [Manage aliases](/guides/manage-data/namespace-aliases/manage-aliases)
* [Manage namespaces](/guides/manage-data/manage-namespaces)
