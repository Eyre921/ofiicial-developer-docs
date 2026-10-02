---
title: "List legal holds"
source: https://developers.notion.com/reference/admin/list-legal-holds
path: reference/admin/list-legal-holds
---

openapi-adminApi.json GET /v1/legal_holds
List all legal holds belonging to your organization.

The organization bot token must have the following scopes:

* `legal-hold:read`

Returns all legal holds for your organization, both active and released.

<Info>
  The API does not guarantee a particular sort order for returned legal holds.
</Info>
