---
title: "Versioning"
source: https://developers.notion.com/reference/admin/versioning
path: reference/admin/versioning
---

Learn about API change management and how to set the appropriate version in your connection.

The Admin API is versioned. Our API versions are named for the date the version is released. For example, our latest version is .

Set the version by including a `Notion-Version` header. Setting this header is **required**.

```bash cURL theme={null}
curl https://api.notion.com/admin/v1/legal_holds \
-H "Authorization: Bearer adm_t1CdN9S8yicG5eWLUOfhcWaOscVnFXnsJM9cWeCdTNfhbt"
-H "Notion-Version: 2026-06-01"
```

<Warning>
  **Required Header**

  The `Notion-Version` header must be included in all REST API requests. This ensures the Notion API response is consistent with what your code expects.

  The most recent `Notion-Version` is .
</Warning>
