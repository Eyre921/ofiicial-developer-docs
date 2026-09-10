---
title: "Quickstart"
source: https://docs.x.com/x-api/spaces/search/quickstart
path: x-api/spaces/search/quickstart
---

Quickstart guide for searching X Spaces by keyword with the X API v2 standard tier Spaces search endpoint, covering authentication and example calls.

This guide walks you through searching for Spaces by keyword.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token
</Note>

***

## Search for Spaces

Search for Spaces matching a keyword:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/spaces/search?\
  query=AI&\
  space.fields=title,host_ids,participant_count,state&\
  state=live" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Search for Spaces
  response = client.spaces.search(
      query="AI",
      space_fields=["title", "host_ids", "participant_count", "state"],
      state="live"
  )

  for space in response.data:
      print(f"{space.title} - {space.participant_count} participants")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Search for Spaces
  const response = await client.spaces.search({
    query: "AI",
    spaceFields: ["title", "host_ids", "participant_count", "state"],
    state: "live",
  });

  response.data?.forEach((space) => {
    console.log(`${space.title} - ${space.participant_count} participants`);
  });
  ```
</CodeGroup>

### Response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "id": "1DXxyRYNejbKM",
      "state": "live",
      "title": "Discussing AI and the Future",
      "host_ids": ["2244994945"],
      "participant_count": 245
    },
    {
      "id": "1YqJDqWYNQDGW",
      "state": "live",
      "title": "AI in Healthcare",
      "host_ids": ["783214"],
      "participant_count": 89
    }
  ],
  "meta": {
    "result_count": 2
  }
}
```

***

## Filter by state

Search only live or scheduled Spaces:

### Live Spaces only

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/spaces/search?query=tech&state=live" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Search live Spaces only
  response = client.spaces.search(query="tech", state="live")

  for space in response.data:
      print(f"LIVE: {space.title}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Search live Spaces only
  const response = await client.spaces.search({
    query: "tech",
    state: "live",
  });

  response.data?.forEach((space) => {
    console.log(`LIVE: ${space.title}`);
  });
  ```
</CodeGroup>

### Scheduled Spaces only

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/spaces/search?query=tech&state=scheduled" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Search scheduled Spaces only
  response = client.spaces.search(query="tech", state="scheduled")

  for space in response.data:
      print(f"SCHEDULED: {space.title}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Search scheduled Spaces only
  const response = await client.spaces.search({
    query: "tech",
    state: "scheduled",
  });

  response.data?.forEach((space) => {
    console.log(`SCHEDULED: ${space.title}`);
  });
  ```
</CodeGroup>

***

## Include host information

Expand host user data:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/spaces/search?\
  query=AI&\
  space.fields=title,host_ids,state&\
  expansions=host_ids&\
  user.fields=username,verified" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Search with host info
  response = client.spaces.search(
      query="AI",
      space_fields=["title", "host_ids", "state"],
      expansions=["host_ids"],
      user_fields=["username", "verified"]
  )

  for space in response.data:
      print(f"{space.title}")
  # Host info is in response.includes.users
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Search with host info
  const response = await client.spaces.search({
    query: "AI",
    spaceFields: ["title", "host_ids", "state"],
    expansions: ["host_ids"],
    userFields: ["username", "verified"],
  });

  response.data?.forEach((space) => {
    console.log(space.title);
  });
  // Host info is in response.includes?.users
  ```
</CodeGroup>

***

## Common parameters

| Parameter      | Description                           |
| :------------- | :------------------------------------ |
| `query`        | Search query (required)               |
| `state`        | Filter: `live`, `scheduled`, or `all` |
| `max_results`  | Results to return (1-100)             |
| `space.fields` | Space fields to include               |
| `expansions`   | Related objects to include            |
| `user.fields`  | User fields to include                |

***

## Next steps

<CardGroup>
  <Card title="Space lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9" href="/x-api/spaces/lookup/quickstart">
    Look up Spaces by ID
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/spaces/search-spaces">
    Full endpoint documentation
  </Card>
</CardGroup>
