---
title: "Manage namespace aliases"
source: https://docs.pinecone.io/guides/manage-data/namespace-aliases/manage-aliases
path: guides/manage-data/namespace-aliases/manage-aliases
---

Create, list, describe, repoint, and delete namespace aliases in a Pinecone index with the REST API, with a request example for each alias operation.

<Note>
  Creating and managing aliases requires API version `2026-07` or later and is available through the REST API. Reading through an alias works on any API version, including the current SDKs.
</Note>

Create, list, describe, repoint, and delete [namespace aliases](/guides/manage-data/namespace-aliases/overview) in an index. Each operation is a single REST call to your [index host](/guides/manage-data/target-an-index). To swap the data an application reads with no downtime, see [Swap a namespace](/guides/manage-data/namespace-aliases/swap-a-namespace).

You need a project role that can manage namespaces, such as [`DataPlaneEditor`](/guides/production/manage-rbac), `ProjectOwner`, or `ProjectManager`. Managing aliases needs the same access as managing namespaces directly.

## Operations

| Action | Operation |
| :- | :- |
| Create an alias | `POST /namespace-aliases` with `{"name", "target_namespace"}` |
| List aliases in the index | `GET /namespace-aliases` |
| Describe one alias | `GET /namespace-aliases/{alias_name}` |
| Repoint an alias | `PATCH /namespace-aliases/{alias_name}` with `{"target_namespace"}` |
| Delete an alias | `DELETE /namespace-aliases/{alias_name}` |

Each alias is returned as `{name, target_namespace, created_at, updated_at}`. `updated_at` advances on every repoint.

## Errors

Every rejection carries a machine-readable reason in `details[0].reason`. SDKs and agents branch on the reason, not the message text.

| Reason | When |
| :- | :- |
| `ALIAS_NAME_INVALID` | The alias name breaks the naming rules. |
| `ALIAS_ALREADY_EXISTS` | An alias with this name exists. `details[0].metadata.target_namespace` is its current target. |
| `NAME_IN_USE_BY_NAMESPACE` | The name is taken by a namespace. |
| `TARGET_NAMESPACE_NOT_FOUND` | The target namespace doesn't exist. |
| `TARGET_NAMESPACE_NOT_ACTIVE` | The target namespace is still initializing, importing, or restoring. The same request works once it's active. |
| `TARGET_IS_ALIAS` | The target is an alias. Aliases can't chain. |
| `ALIASES_PER_INDEX_EXCEEDED` | The index has 1,000 aliases already. |
| `ALIAS_NOT_FOUND` | Describe, repoint, or delete on a name that isn't an alias. |

You also get a reason when a request addresses an alias name where it shouldn't:

| Reason | When |
| :- | :- |
| `NAME_IN_USE_BY_ALIAS` | An upsert addressed an alias name. Write to the target namespace instead. |
| `WRITE_TO_ALIAS` | An update or delete addressed an alias name. Same fix. |
| `NAMESPACE_OPERATION_ON_ALIAS` | A namespace describe or delete addressed an alias name. Use the alias endpoints. |
| `NAMESPACE_TARGETED_BY_ALIAS` | A namespace delete while an alias still points at it. Repoint or delete the alias first. |

## Create an alias

Specify a `name` for the alias and the `target_namespace` it points at. The target must be an existing, ready namespace in the same index. A namespace that's still initializing, importing, or restoring is refused.

If a create returns a 409 with reason `ALIAS_ALREADY_EXISTS` and `details[0].metadata.target_namespace` matches the target you asked for, an earlier call already succeeded and the alias is live, so a retry can treat it as done. A different target is a real conflict.

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespace-aliases" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "name": "example-alias",
        "target_namespace": "example-namespace-v1"
      }'
```

## List aliases

List the aliases in an index to see what each one targets.

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/namespace-aliases" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```

The response lists the aliases in the index, ordered by name, with a `total_count`. When more aliases remain, the response includes a `pagination.next` token. Pass it as `paginationToken` on the next request to get the following page. Use `limit` to set the page size, and filter the list by `prefix` and `target_namespace`.

```json curl theme={null}
{
  "namespace_aliases": [
    {
      "name": "example-alias",
      "target_namespace": "example-namespace-v1",
      "created_at": "2026-09-01T12:00:00Z",
      "updated_at": "2026-09-01T12:00:00Z"
    }
  ],
  "total_count": 1
}
```

## Describe an alias

Describe a single alias to see its current target and when it last changed.

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/namespace-aliases/example-alias" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```

Create, describe, and repoint return the alias object:

```json curl theme={null}
{
  "name": "example-alias",
  "target_namespace": "example-namespace-v1",
  "created_at": "2026-09-01T12:00:00Z",
  "updated_at": "2026-09-01T12:00:00Z"
}
```

## Repoint an alias

Point the alias at a different namespace. The repoint is atomic, and when the call returns success, all reads resolve to the new target. Repointing to a namespace that doesn't exist or isn't ready is rejected, and the alias keeps its current target.

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X PATCH "https://$INDEX_HOST/namespace-aliases/example-alias" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "target_namespace": "example-namespace-v2"
      }'
```

## Delete an alias

Deleting an alias never touches the target namespace or its data. A delete that returns a 404 means the alias is already gone, so a retry can safely treat it as done.

<Warning>
  Any application still reading through the alias name will start getting empty results, not an error. Move your readers to the namespace name, or to a different alias, before you delete.
</Warning>

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X DELETE "https://$INDEX_HOST/namespace-aliases/example-alias" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```

## See also

* [Namespace aliases overview](/guides/manage-data/namespace-aliases/overview)
* [Swap a namespace](/guides/manage-data/namespace-aliases/swap-a-namespace)
