---
title: "Secure API tokens"
source: https://developers.notion.com/guides/get-started/handling-api-keys
path: guides/get-started/handling-api-keys
---

Learn how to manage and secure your Notion API tokens.

Notion API tokens authorize requests to the Notion API. This guidance applies to internal connection tokens, OAuth access tokens, and [personal access tokens](/guides/get-started/personal-access-tokens).

## Protect your tokens

Anyone who obtains a token can make requests allowed by its capabilities and content permissions. Depending on the token, this could expose or change workspace content.

For a PAT, access is limited by the token's capabilities and the permissions of the person who created it. For an internal connection, access is limited to pages shared with the connection and its capabilities.

* Don't share tokens in messages, support requests, issue trackers, or other public places.
* Don't put tokens directly in source code or configuration files.
* Store tokens in environment variables or an encrypted secret manager.
* Use separate tokens for development, staging, and production.
* Grant only the capabilities that each application needs.
* Revoke tokens that you no longer use.

## Store tokens outside your code

Use an environment variable for local development. Add `.env` files to `.gitignore` and never commit them.

```bash theme={null}
# .env file (never commit this file)
NOTION_API_KEY=ntn_abc123def456ghi789jkl012mno345pqr
```

<CodeGroup>
  ```typescript TypeScript theme={null}
  const notion = new Client({
    auth: process.env.NOTION_API_KEY,
  });
  ```
</CodeGroup>

Use a secret manager for deployed applications. Limit who can read production secrets and keep an inventory of each token's owner and purpose.

## Calling the API from a browser

The Notion API sends cross-origin resource sharing (CORS) headers, so browser code can call the API directly.

Never ship an internal connection token or a client secret in page source that strangers can load. Anyone who can view the source can use that secret to act as the connection.

For apps that other people use, create a [public connection](/guides/get-started/public-connections), which uses OAuth. Exchange the OAuth code for a token on a server you control. For a personal or local tool, putting a token in a page that only you can open is a risk you must choose whether to accept.

OAuth token endpoints under `/v1/oauth/*` do not send CORS headers on purpose. OAuth code exchange requires a client secret and must run on a server.

## Scan for exposed tokens

Enable secret scanning in your repository and CI system. Block commits that contain tokens, and alert the token owner if a token is detected.

## Replace tokens regularly

Replace long-lived tokens on a schedule and whenever someone with access to them leaves your team. PATs expire on the date chosen when the token is created, up to one year later. Replace a PAT before it expires.

## Respond to an exposed token

Revoke or replace a token immediately if it may have been exposed.

### 1. Disable the token

<Steps>
  <Step>
    Log in to Notion.
  </Step>

  <Step>
    Go to **Settings** → **Connections** → **Develop or manage connections**.
  </Step>

  <Step>
    Find the connection or personal access token that uses the exposed token.
  </Step>

  <Step>
    Select **Refresh** for an internal connection, or revoke the personal access token.
  </Step>
</Steps>

For a PAT, you can also revoke the token from <a href={personalAccessTokensUrl}>Personal access tokens</a> in the Developer portal. Create a new token if the application still needs access.

<Frame>
  <img alt="The Refresh button for an internal connection in the Developer portal." />
</Frame>

### 2. Update applications

Replace the old token in every application and environment that used it. Test the new token, and remove the old value from configuration files and documentation.

### 3. Review activity

Check recent changes to pages and databases. Look for connections you don't recognize in **Settings** → **Connections**.

## Getting help

If you need help with an exposed token or unauthorized access, contact [Notion support](https://www.notion.com/help).
