---
title: "List Members Overview"
source: https://docs.x.com/x-api/lists/list-members/quickstart/overview
path: x-api/lists/list-members/quickstart/overview
---

The List members endpoints let you look up members of a List and manage List membership. Reference for the X API v2 standard tier covering quickstart.

The List members endpoints let you look up members of a List and manage List membership.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token (for lookups)
  * User Access Token (for managing members)
</Note>

***

## Available endpoints

<CardGroup>
  <Card title="List members lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/lists/list-members/quickstart/list-members-lookup">
    Get members of a List
  </Card>

  <Card title="Manage List members" icon="user-plus" href="/x-api/lists/list-members/quickstart/manage-list-members">
    Add and remove members
  </Card>
</CardGroup>

***

## Authentication

| Operation          | Authentication                              |
| :----------------- | :------------------------------------------ |
| Look up members    | Bearer Token, OAuth 1.0a, or OAuth 2.0 PKCE |
| Add/remove members | OAuth 1.0a or OAuth 2.0 PKCE                |

***

## Quick example

<CodeGroup>
  ```bash cURL theme={null}
  # Get List members
  curl "https://api.x.com/2/lists/84839422/members" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Get List members
  for page in client.lists.get_members("84839422"):
      for user in page.data:
          print(f"{user.username}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Get List members
  const paginator = client.lists.getMembers("84839422");

  for await (const page of paginator) {
    page.data?.forEach((user) => {
      console.log(user.username);
    });
  }
  ```
</CodeGroup>

***

## Next steps

<CardGroup>
  <Card title="List lookup" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5" href="/x-api/lists/list-lookup/quickstart">
    Get List details
  </Card>

  <Card title="List Posts" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f" href="/x-api/lists/list-tweets/quickstart">
    Get Posts from a List
  </Card>
</CardGroup>
