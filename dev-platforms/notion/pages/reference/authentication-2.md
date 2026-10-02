---
title: "Authentication"
source: https://developers.notion.com/reference/authentication
path: reference/authentication
---

Learn how to authenticate your connection requests using bearer tokens.

Requests use the HTTP `Authorization` header to both authenticate and authorize operations. The Notion API accepts bearer tokens in this header. Bearer tokens are provided when you create an [internal connection](/guides/get-started/internal-connections), create a [personal access token](/guides/get-started/personal-access-tokens), or complete the OAuth flow for a [public connection](/guides/get-started/public-connections).

<CodeGroup>
  ```curl cURL theme={null}
  curl 'https://api.notion.com/v1/users' \
    -H 'Authorization: Bearer '"$NOTION_ACCESS_TOKEN"'' \
    -H "Notion-Version: 2026-03-11"
  ```
</CodeGroup>

Inside Notion, users will see updates made by connections attributed according to the token type. Internal connections use their bot identity, public connections act for the user who authorized them, and PATs act as the user who created the token.

Using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), a bearer token can be passed once to initialize a `Client` and the client can be used to send multiple authenticated requests.

<CodeGroup>
  ```javascript Notion SDK for JS theme={null}
  const { Client } = require('@notionhq/client');

  const client = new Client({ auth: process.env.NOTION_ACCESS_TOKEN });
  ```
</CodeGroup>

Learn more in the [Authorization guide](/guides/get-started/authorization).
