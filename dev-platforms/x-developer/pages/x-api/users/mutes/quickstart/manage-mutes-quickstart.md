---
title: "Manage Mutes"
source: https://docs.x.com/x-api/users/mutes/quickstart/manage-mutes-quickstart
path: x-api/users/mutes/quickstart/manage-mutes-quickstart
---

This guide walks you through muting and unmuting users using the X API. Reference for the X API v2 standard tier covering quickstart.

This guide walks you through muting and unmuting users using the X API.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token (OAuth 1.0a or OAuth 2.0 PKCE)
</Note>

***

## Mute a user

<Steps>
  <Step title="Get your user ID">
    You need your authenticated user's ID. You can find it using the [user lookup endpoint](/x-api/users/lookup/introduction) or from your Access Token (the numeric part is your user ID).
  </Step>

  <Step title="Get the target user ID">
    Find the user ID of the account you want to mute using the [user lookup endpoint](/x-api/users/lookup/introduction).
  </Step>

  <Step title="Send the mute request">
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST "https://api.x.com/2/users/123456789/muting" \
        -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"target_user_id": "9876543210"}'
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

      # Mute a user
      response = client.users.mute(
          source_user_id="123456789",
          target_user_id="9876543210"
      )

      print(f"Muting: {response.data.muting}")
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

      // Mute a user
      const response = await client.users.mute("123456789", {
        targetUserId: "9876543210",
      });

      console.log(`Muting: ${response.data?.muting}`);
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response">
    ```json theme={null}
    {
      "data": {
        "muting": true
      }
    }
    ```
  </Step>
</Steps>

***

## Unmute a user

Remove a mute from a user:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.x.com/2/users/123456789/muting/9876543210" \
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

  # Unmute a user
  response = client.users.unmute(
      source_user_id="123456789",
      target_user_id="9876543210"
  )

  print(f"Muting: {response.data.muting}")
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

  // Unmute a user
  const response = await client.users.unmute("123456789", "9876543210");

  console.log(`Muting: ${response.data?.muting}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "data": {
    "muting": false
  }
}
```

***

## Mute vs Block

| Feature             | Mute | Block |
| :------------------ | :--- | :---- |
| See their Posts     | No   | No    |
| They see your Posts | Yes  | No    |
| They can follow you | Yes  | No    |
| They can DM you     | Yes  | No    |
| They know           | No   | Yes   |

***

## Next steps

<CardGroup>
  <Card title="Mutes lookup" icon="volume-xmark" href="/x-api/users/mutes/quickstart/mutes-lookup">
    Get your muted users
  </Card>

  <Card title="Blocks" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-block.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=702a65b4001948aebcc42635b8e2eac7" href="/x-api/users/blocks/quickstart">
    Block users instead
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/mute-user-by-user-id">
    Full endpoint documentation
  </Card>
</CardGroup>
