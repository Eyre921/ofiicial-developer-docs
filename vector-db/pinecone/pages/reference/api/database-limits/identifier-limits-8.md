---
title: "Identifier limits"
source: https://docs.pinecone.io/reference/api/database-limits/identifier-limits
path: reference/api/database-limits/identifier-limits
---

Maximum length and allowed characters for Pinecone identifiers, including organization, project, index, namespace, and record names.

An identifier is a string of characters used to identify "named" [objects in Pinecone](/guides/get-started/architecture#resource-hierarchy). The following Pinecone objects use strings as identifiers:

| Object | Field | Max # characters | Allowed characters |
| - | - | - | - |
| [Organization](/admin/organizations/organizations-overview) | `name` | 512 | <ul><li>UTF-8 except `\0`</li><li>Can't be empty</li></ul> |
| [Project](/admin/projects/projects-overview) | `name` | 512 | <ul><li>UTF-8 except `\0`</li><li>Can't be empty</li></ul> |
| [Index](/guides/indexes/index-data-overview#indexes) | `name` | 45 | <ul><li>`a-z`, `0-9`, and `-`</li><li>Must be lowercase</li><li>Can't start or end with `-`</li><li>Can't be empty</li></ul> |
| [Namespace](/guides/indexes/index-data-overview#namespaces) | `namespace` | 512 | <ul><li>ASCII except `\0`</li><li>For the default namespace, use `""` (or `"__default__"`, in API versions `2025-04` and later)</li></ul> |
| [Namespace alias](/guides/data/namespace-aliases/overview) | `name` | 512 | <ul><li>ASCII graphic characters</li><li>No spaces or `/ ? # % & = \ ; +`</li><li>`.`, `..`, and `__default__` are reserved</li><li>Must be unique in the index and can't match a namespace name</li></ul> |
| [Record](/guides/indexes/data-modeling#records-in-legacy-indexes) | `id` | 512 | <ul><li>ASCII except `\0`</li><li>Can't be empty</li></ul> |
