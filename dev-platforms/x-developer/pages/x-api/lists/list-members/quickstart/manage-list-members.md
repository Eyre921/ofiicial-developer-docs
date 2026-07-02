---
title: "Manage List Members"
source: https://docs.x.com/x-api/lists/list-members/quickstart/manage-list-members
path: x-api/lists/list-members/quickstart/manage-list-members
---

This guide walks you through adding and removing members from a List. Reference for the X API v2 standard tier covering quickstart.

This guide walks you through adding and removing members from a List.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token (OAuth 1.0a or OAuth 2.0 PKCE)
  * A List that you own
</Note>

***

## Add a member to a List

<Steps>
  <Step title="Get the List ID and user ID">
    You need the ID of your List and the user ID of the person you want to add. Find user IDs using the [user lookup endpoint](/x-api/users/lookup/introduction).
  </Step>

  <Step title="Add the member">
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST "https://api.x.com/2/lists/1441162269824405510/members" \
        -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"user_id": "2244994945"}'
      ```

      ```python Python SDK theme={null}
      from xdk import Client
      from xdk.oauth1_auth import OAuth1

      oauth1 = OAuth1(
          api_key="YOUR_API_KEY",
          api_secret="YOUR_API_SECRET",
          access_token="YOUR_ACCESS_TOKEN",
          access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
      )

      client = Client(auth=oauth1)

      # Add a member to a List
      response = client.lists.add_member(
          list_id="1441162269824405510",
          user_id="2244994945"
      )

      print(f"Is member: {response.data.is_member}")
      ```

      ```javascript JavaScript SDK theme={null}
      import { Client, OAuth1 } from "@xdevplatform/xdk";

      const oauth1 = new OAuth1({
        apiKey: "YOUR_API_KEY",
        apiSecret: "YOUR_API_SECRET",
        accessToken: "YOUR_ACCESS_TOKEN",
        accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
      });

      const client = new Client({ oauth1 });

      // Add a member to a List
      const response = await client.lists.addMember("1441162269824405510", {
        userId: "2244994945",
      });

      console.log(`Is member: ${response.data?.is_member}`);
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response">
    ```json theme={null}
    {
      "data": {
        "is_member": true
      }
    }
    ```
  </Step>
</Steps>

***

## Remove a member from a List

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.x.com/2/lists/1441162269824405510/members/2244994945" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client
  from xdk.oauth1_auth import OAuth1

  oauth1 = OAuth1(
      api_key="YOUR_API_KEY",
      api_secret="YOUR_API_SECRET",
      access_token="YOUR_ACCESS_TOKEN",
      access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
  )

  client = Client(auth=oauth1)

  # Remove a member from a List
  response = client.lists.remove_member(
      list_id="1441162269824405510",
      user_id="2244994945"
  )

  print(f"Is member: {response.data.is_member}")
  ```

  ```javascript JavaScript SDK theme={null}
  import { Client, OAuth1 } from "@xdevplatform/xdk";

  const oauth1 = new OAuth1({
    apiKey: "YOUR_API_KEY",
    apiSecret: "YOUR_API_SECRET",
    accessToken: "YOUR_ACCESS_TOKEN",
    accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
  });

  const client = new Client({ oauth1 });

  // Remove a member from a List
  const response = await client.lists.removeMember(
    "1441162269824405510",
    "2244994945"
  );

  console.log(`Is member: ${response.data?.is_member}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "data": {
    "is_member": false
  }
}
```

***

## Important notes

<Note>
  * You can only manage members of Lists you own
  * Adding a user to a List does not require their permission
  * Users can see which public Lists they've been added to
</Note>

***

## Next steps

<CardGroup>
  <Card title="List members lookup" icon="users" href="/x-api/lists/list-members/quickstart/list-members-lookup">
    Get List members
  </Card>

  <Card title="Manage Lists" icon="pen" href="/x-api/lists/manage-lists/quickstart">
    Create and update Lists
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/lists/add-list-member">
    Full endpoint documentation
  </Card>
</CardGroup>
