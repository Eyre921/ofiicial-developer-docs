---
title: "Quickstart"
source: https://docs.x.com/x-api/lists/manage-lists/quickstart
path: x-api/lists/manage-lists/quickstart
---

This guide walks you through creating, updating, and deleting Lists. Reference for the X API v2 standard tier covering manage lists.

This guide walks you through creating, updating, and deleting Lists.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token (OAuth 1.0a or OAuth 2.0 PKCE)
</Note>

***

## Create a List

<Steps>
  <Step title="Prepare your request">
    Define the List name (required) and optional description and privacy settings:

    ```json theme={null}
    {
      "name": "Tech News",
      "description": "Top tech journalists and publications",
      "private": false
    }
    ```
  </Step>

  <Step title="Send the request">
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST "https://api.x.com/2/lists" \
        -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "Tech News",
          "description": "Top tech journalists and publications",
          "private": false
        }'
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client
      from xdk.oauth1_auth import OAuth1

      oauth1 = OAuth1(
          api_key="YOUR_API_KEY",
          api_secret="YOUR_API_SECRET",
          access_token="YOUR_ACCESS_TOKEN",
          access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
      )

      client = Client(auth=oauth1)

      # Create a new List
      response = client.lists.create(
          name="Tech News",
          description="Top tech journalists and publications",
          private=False
      )

      print(f"List created: {response.data.id} - {response.data.name}")
      ```

      ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
      import { Client, OAuth1 } from "@xdevplatform/xdk";

      const oauth1 = new OAuth1({
        apiKey: "YOUR_API_KEY",
        apiSecret: "YOUR_API_SECRET",
        accessToken: "YOUR_ACCESS_TOKEN",
        accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
      });

      const client = new Client({ oauth1 });

      // Create a new List
      const response = await client.lists.create({
        name: "Tech News",
        description: "Top tech journalists and publications",
        private: false,
      });

      console.log(`List created: ${response.data?.id} - ${response.data?.name}`);
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response">
    ```json theme={null}
    {
      "data": {
        "id": "1441162269824405510",
        "name": "Tech News"
      }
    }
    ```

    Save the `id` to update or delete the List later.
  </Step>
</Steps>

***

## Update a List

Modify a List's name, description, or privacy:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X PUT "https://api.x.com/2/lists/1441162269824405510" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Tech News & Insights",
      "description": "Updated description"
    }'
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client
  from xdk.oauth1_auth import OAuth1

  oauth1 = OAuth1(
      api_key="YOUR_API_KEY",
      api_secret="YOUR_API_SECRET",
      access_token="YOUR_ACCESS_TOKEN",
      access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
  )

  client = Client(auth=oauth1)

  # Update a List
  response = client.lists.update(
      "1441162269824405510",
      name="Tech News & Insights",
      description="Updated description"
  )

  print(f"Updated: {response.data.updated}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client, OAuth1 } from "@xdevplatform/xdk";

  const oauth1 = new OAuth1({
    apiKey: "YOUR_API_KEY",
    apiSecret: "YOUR_API_SECRET",
    accessToken: "YOUR_ACCESS_TOKEN",
    accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
  });

  const client = new Client({ oauth1 });

  // Update a List
  const response = await client.lists.update("1441162269824405510", {
    name: "Tech News & Insights",
    description: "Updated description",
  });

  console.log(`Updated: ${response.data?.updated}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "data": {
    "updated": true
  }
}
```

***

## Delete a List

<Steps>
  <Step title="Get the List ID">
    You need the ID of the List you want to delete.
  </Step>

  <Step title="Send the delete request">
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE "https://api.x.com/2/lists/1441162269824405510" \
        -H "Authorization: Bearer $USER_ACCESS_TOKEN"
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client
      from xdk.oauth1_auth import OAuth1

      oauth1 = OAuth1(
          api_key="YOUR_API_KEY",
          api_secret="YOUR_API_SECRET",
          access_token="YOUR_ACCESS_TOKEN",
          access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
      )

      client = Client(auth=oauth1)

      # Delete a List
      response = client.lists.delete("1441162269824405510")
      print(f"Deleted: {response.data.deleted}")
      ```

      ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
      import { Client, OAuth1 } from "@xdevplatform/xdk";

      const oauth1 = new OAuth1({
        apiKey: "YOUR_API_KEY",
        apiSecret: "YOUR_API_SECRET",
        accessToken: "YOUR_ACCESS_TOKEN",
        accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
      });

      const client = new Client({ oauth1 });

      // Delete a List
      const response = await client.lists.delete("1441162269824405510");
      console.log(`Deleted: ${response.data?.deleted}`);
      ```
    </CodeGroup>
  </Step>

  <Step title="Confirm deletion">
    ```json theme={null}
    {
      "data": {
        "deleted": true
      }
    }
    ```
  </Step>
</Steps>

<Warning>
  You can only delete Lists that you own.
</Warning>

***

## Next steps

<CardGroup>
  <Card title="List members" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/lists/list-members/introduction">
    Add and remove List members
  </Card>

  <Card title="List lookup" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834" href="/x-api/lists/list-lookup/quickstart">
    Retrieve List details
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/manage-lists/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/create-list">
    Full endpoint documentation
  </Card>
</CardGroup>
