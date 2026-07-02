---
title: "Pinned Lists Overview"
source: https://docs.x.com/x-api/lists/pinned-lists/quickstart/overview
path: x-api/lists/pinned-lists/quickstart/overview
---

The pinned Lists endpoints let you look up a user's pinned Lists and manage which Lists are. Reference for the X API v2 standard tier covering quickstart.

The pinned Lists endpoints let you look up a user's pinned Lists and manage which Lists are pinned.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token (OAuth 1.0a or OAuth 2.0 PKCE)
</Note>

***

## Available endpoints

<CardGroup>
  <Card title="Pinned Lists lookup" icon="thumbtack" href="/x-api/lists/pinned-lists/quickstart/pinned-list-lookup">
    Get your pinned Lists
  </Card>

  <Card title="Manage pinned Lists" icon="pin" href="/x-api/lists/pinned-lists/quickstart/manage-pinned-lists">
    Pin and unpin Lists
  </Card>
</CardGroup>

***

## Authentication

| Operation            | Authentication               |
| :------------------- | :--------------------------- |
| Look up pinned Lists | OAuth 1.0a or OAuth 2.0 PKCE |
| Pin/unpin Lists      | OAuth 1.0a or OAuth 2.0 PKCE |

<Warning>
  Both lookup and manage operations require user context authentication. App-only (Bearer Token) authentication is not supported.
</Warning>

***

## Quick example

<CodeGroup>
  ```bash cURL theme={null}
  # Get pinned Lists
  curl "https://api.x.com/2/users/2244994945/pinned_lists" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_USER_ACCESS_TOKEN")

  # Get pinned Lists
  response = client.lists.get_pinned("2244994945")

  for lst in response.data:
      print(f"{lst.name}")
  ```

  ```javascript JavaScript SDK theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ accessToken: "YOUR_USER_ACCESS_TOKEN" });

  // Get pinned Lists
  const response = await client.lists.getPinned("2244994945");

  response.data?.forEach((lst) => {
    console.log(lst.name);
  });
  ```
</CodeGroup>

***

## Next steps

<CardGroup>
  <Card title="List lookup" icon="list" href="/x-api/lists/list-lookup/quickstart">
    Get List details
  </Card>

  <Card title="Manage Lists" icon="pen" href="/x-api/lists/manage-lists/quickstart">
    Create and update Lists
  </Card>
</CardGroup>
