---
title: "Personal access tokens"
source: https://developers.notion.com/guides/get-started/personal-access-tokens
path: guides/get-started/personal-access-tokens
---

Create and use personal access tokens for user-scoped API and Workers access.

Personal access tokens (PATs) let one Notion user call the Notion API or work with Notion Workers. A PAT belongs to one workspace. For Notion API requests, it uses the workspace membership and page permissions of the person who created it.

Use a PAT when API requests should act as you and you don't need an [internal connection](/guides/get-started/internal-connections) or the [OAuth flow for a public connection](/guides/get-started/public-connections).

## When to use a PAT

Use a PAT for personal or developer-owned workflows that one Notion user should own:

* Local scripts, notebooks, and command-line tools that automate work in your own workspace.
* Development and testing against the Notion API before you create a shared connection.
* Third-party tools that ask you to paste a Notion token and should act with your Notion permissions.
* [Notion Workers](/workers/get-started/overview) development and deployment with the Notion CLI.

Don't use a PAT to authenticate a product used by many Notion users. Create a [public connection](/guides/get-started/public-connections) so each user can authorize access with OAuth. For a team-owned automation that should not depend on one person's permissions, use an [internal connection](/guides/get-started/internal-connections).

## How PATs work

Create PATs in the <a href={developerPortalUrl}>Developer portal</a>. For each PAT, you choose:

* A token name.
* The workspace the token belongs to.
* Capabilities for the token.

You can give a PAT either or both of these capabilities:

| Capability     | What it allows                                                                                                                     |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Notion API** | Read, create, update, and search content; read and create comments; and read supported user information through Notion's REST API. |
| **Workers**    | Deploy and manage [Notion Workers](/workers/get-started/overview) with the Notion CLI.                                             |

The workspace's PAT creation policy controls who can use the Notion API capability. Workspace members can receive the Workers capability when Notion Workers is available to the workspace.

PATs authenticate requests the same way other Notion API tokens do:

<CodeGroup>
  ```http HTTP theme={null}
  GET /v1/users/me HTTP/1.1
  Authorization: Bearer {PERSONAL_ACCESS_TOKEN}
  Notion-Version: 2026-03-11
  ```

  ```javascript JavaScript theme={null}
  // Save this example in an .mjs file.
  import { Client } from "@notionhq/client"

  const notion = new Client({
    auth: process.env.NOTION_PAT,
  })
  ```
</CodeGroup>

## Permissions and content access

A PAT acts as the user who created it:

* It can access pages, data sources, databases, comments, files, and other resources that the creator can access.
* It does not need pages to be shared with a bot through **Add connections**.
* If the creator loses access to a page or leaves the workspace, the PAT loses that access too.
* API behavior that depends on an authenticated user, such as `"me"` filters or workspace-level private page creation, uses the PAT creator.

An internal connection operates as a separate bot user and can access only pages shared with that connection. A PAT uses a real user's permissions, so it is best for work owned by that user rather than team-owned automations.

<Info>
  [List all users](/reference/get-users) is not available to PATs. A PAT can use [Retrieve token's bot user](/reference/get-self) to retrieve the authorized user, and [Retrieve a user](/reference/get-user) can retrieve that same user.
</Info>

## Workspace admin controls

Workspace admins can manage PATs from **Settings → Connections**:

* View all PATs created in the workspace, including active, expired, and revoked tokens.
* Search and filter tokens by name, creator, and status.
* See who created a token and, for revoked tokens, who revoked it.
* Revoke active or expired PATs.
* Configure who can create PATs with Notion API access.

Admins cannot view or copy another member's token value. The token creator can copy it only when they create the PAT; Notion does not show it again.

If an admin changes the workspace policy so a member is no longer allowed to create PATs with Notion API access, that member's existing PATs stop working for Notion API requests. Those requests return an `unauthorized` error until the policy allows the member again or the member uses a different valid token.

Organization owners can also use [List personal access tokens](/reference/admin/list-personal-access-tokens) and [Revoke a personal access token](/reference/admin/revoke-personal-access-token) to automate these tasks with the Admin API.

### Who can create PATs

[Guests and restricted members](https://www.notion.com/help/whos-who-in-a-workspace) cannot create PATs or log in with the Notion CLI (`ntn login`). Only full workspace members can create tokens, subject to the workspace's PAT creation policy below. Workspace owners can always create PATs with Notion API access.

| Plan       | Default PAT creation policy           | Admin controls                                                                                                       |
| :--------- | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| Free       | Workspace owners only.                | Not configurable.                                                                                                    |
| Plus       | All workspace members.                | Not configurable.                                                                                                    |
| Business   | Workspace owners only.                | Admins can choose **Workspace owners only** or **All workspace members**.                                            |
| Enterprise | Workspace owners and selected groups. | Admins can choose **Workspace owners only**, **Workspace owners and selected groups**, or **All workspace members**. |

On Enterprise, admins manage selected groups in the PAT creator settings. If no groups are selected, only workspace owners can create PATs with Notion API access.

## Create a PAT

<Steps>
  <Step>
    Open <a href={personalAccessTokensUrl}>Personal access tokens</a> in the Developer portal.
  </Step>

  <Step>
    Select **New token**.
  </Step>

  <Step>
    Name the token, then choose its capabilities and expiration. If a workspace picker appears, select the workspace the token belongs to.
  </Step>

  <Step>
    Select **Create token**, then copy the token value and store it securely. You can't view it again.
  </Step>
</Steps>

Choose an **Expiration** of **7 days**, **30 days**, **90 days**, **180 days**, or **1 year**. The form shows the exact expiration date before and after you create the token. If you don't choose an expiration, the token expires after 1 year. Create a new PAT and update your scripts or tools before then. Expired tokens return an `unauthorized` error.

## Revoke a PAT

Revoke a PAT immediately if it is exposed, no longer needed, or associated with a tool you no longer trust.

* Token creators can revoke their own PATs from the Developer portal.
* Workspace admins can revoke any PAT in their workspace from **Settings → Connections → All personal access tokens**.

After revocation, the token immediately stops working for scripts, tools, Workers, and API requests that use it.

## Security best practices

Keep PATs as secure as passwords:

* Store PATs in environment variables or a secret manager.
* Do not commit PATs to source control.
* Use a separate PAT per script, tool, or environment so you can revoke one token without breaking unrelated workflows.
* Grant only the capabilities the workflow needs.
* Revoke tokens you no longer use.

For more guidance, see [Best practices for handling API keys](/guides/get-started/handling-api-keys).
