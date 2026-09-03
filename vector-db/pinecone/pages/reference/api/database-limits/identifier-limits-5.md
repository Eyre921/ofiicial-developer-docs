---
title: "Identifier limits"
source: https://docs.pinecone.io/reference/api/database-limits/identifier-limits
path: reference/api/database-limits/identifier-limits
---

Maximum length and allowed characters for Pinecone identifiers, including organization, project, index, namespace, and record names.

An identifier is a string of characters used to identify "named" [objects in Pinecone](/guides/get-started/concepts). The following Pinecone objects use strings as identifiers:

| Object                                                    | Field       | Max # characters | Allowed characters                                                                                                                        |
| --------------------------------------------------------- | ----------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](/guides/get-started/concepts#organization) | `name`      | 512              | <ul><li>UTF-8 except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
| [Project](/guides/get-started/concepts#project)           | `name`      | 512              | <ul><li>UTF-8 except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
| [Index](/guides/get-started/concepts#index)               | `name`      | 45               | <ul><li>`a-z`, `0-9`, and `-`</li><li>Must be lowercase</li><li>Cannot start or end with `-`</li><li>Cannot be empty</li></ul>            |
| [Namespace](/guides/get-started/concepts#namespace)       | `namespace` | 512              | <ul><li>ASCII except `\0`</li><li>For the default namespace, use `""` (or `"__default__"`, in API versions `2025-04` and later)</li></ul> |
| [Record](/guides/get-started/concepts#record)             | `id`        | 512              | <ul><li>ASCII except `\0`</li><li>Cannot be empty</li></ul>                                                                               |
