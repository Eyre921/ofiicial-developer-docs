---
title: "Overview"
source: https://developers.notion.com/guides/get-started/overview
path: guides/get-started/overview
---

Discover what Notion connections are, when to use each type, and what you can build.

## Using Notion API

Notion connections let you connect your workspace to external tools and automate workflows through code. With the REST API, you can read, create, and update nearly everything in a workspace — pages, databases, users, comments, and more.

When you create a connection, you define what it can do: which API endpoints it can call, what content it can read or write, and how it authenticates. Each connection gets its own credentials and its own set of permissions.

## What is a Notion connection?

A Notion [connection](https://www.notion.so/help/add-and-manage-connections-with-the-api) — sometimes called an integration — connects your workspace to external apps and tools. That could be a SaaS product, an automation script, or a custom tool you've built.

Connections are added to Notion workspaces and require **explicit permission** from users to access Notion pages and databases.

<Frame>
  <img />
</Frame>

Notion already has a [library](https://www.notion.so/integrations/all) of connections you can browse. For developers who want to build their own, Notion supports internal connections, public connections, and personal access tokens — all powered by the same REST API.

## Connection types

Notion supports three authentication models:

* **Internal connections** are scoped to a single workspace and use a static API token. They're ideal for custom automations and workflows — things like syncing data, sending notifications, or building internal dashboards.
* **Public connections** use OAuth 2.0 for authentication. At creation time, you choose their [installation scope](/guides/get-started/public-connections#installation-scope): **Any workspace** (any Notion user can install; Marketplace-eligible) or **Selected workspaces only** (restricted to workspaces you select; not Marketplace-eligible).
* **Personal access tokens (PATs)** are user-scoped tokens for scripts, CLI workflows, Workers, and tools that should act as one Notion user. A PAT uses the creator's workspace membership and page permissions. See [Personal access tokens](/guides/get-started/personal-access-tokens).

<Note>
  Public connections must undergo a Notion security review before being [listed on the Marketplace](/guides/get-started/marketplace-listing). You can create and use a public connection without listing it.
</Note>

### Comparison

| Feature            | Internal connections                                               | Public connections                                                                                         | Personal access tokens                                                            |
| :----------------- | :----------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| Best for           | Team-owned automations in one workspace.                           | Apps or services used by many Notion users or workspaces.                                                  | User-owned scripts, CLI workflows, Workers, and trusted tools.                    |
| Installation scope | Single workspace.                                                  | Any workspace, or a specific set of workspaces chosen at creation time. Scope can't change after creation. | One user in one workspace.                                                        |
| User access        | Only members of the workspace where it's installed.                | Any user in a workspace where the connection is allowed to install.                                        | The member who created the token.                                                 |
| Content access     | Granted directly to the connection, not tied to any specific user. | Users choose which pages to share during the OAuth flow or via the Add connections menu.                   | Uses the creator's Notion permissions; pages do not need to be shared with a bot. |
| Authentication     | Static API token.                                                  | OAuth 2.0.                                                                                                 | Static bearer token.                                                              |

<Info>
  **Looking for SCIM or SAML SSO?**

  Enterprise identity management (user provisioning, group management, and Single Sign-On) is covered in Notion's Help Center, not in these API docs.

  <CardGroup>
    <Card title="Provision users and groups with SCIM" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/arrowChevronDoubleForward.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=e9dad4152e1d3bf11e6a8404d9504665" href="https://www.notion.so/help/provision-users-and-groups-with-scim" />

    <Card title="SAML SSO configuration" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/arrowChevronDoubleForward.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=e9dad4152e1d3bf11e6a8404d9504665" href="https://www.notion.so/help/saml-sso-configuration" />
  </CardGroup>
</Info>

## Shared concepts

All connection and token types share a few core concepts.

### Capabilities

Every connection or token has a set of capabilities that control what it can do — read content, update content, insert content, read comments, and more. You configure capabilities when you create a connection or PAT. See the [Capabilities reference](/reference/capabilities) for the full list.

<CardGroup>
  <Card title="Pages" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/page.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=2d9752eedbbf14b504929f853c3dcd12" href="/guides/data-apis/working-with-page-content">
    Create, update, and retrieve page content.
  </Card>

  <Card title="Databases" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/databaseEmbed.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=7b907de012695ed2c9dba2c6505536a0" href="/guides/data-apis/working-with-databases">
    Manage database, properties, entries, and schemas.
  </Card>

  <Card title="Views" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/viewTable.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=8b8f0d1339820228c542e78d8fb372aa" href="/guides/data-apis/working-with-views">
    Create and configure database views programmatically.
  </Card>

  <Card title="Data sources" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/pathRoundEnds.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=f1b9491091d34c2249a03218696218a3" href="/reference/data-source">
    Manage data sources, properties, entries, and schemas.
  </Card>

  <Card title="File uploads" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/arrowTrayUp.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=3b991e18c85512f06c2d7214acf94f12" href="/guides/data-apis/working-with-files-and-media">
    Upload and attach files to pages and databases.
  </Card>

  <Card title="Comments" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/comment.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=58788fe12adbfeb3cd20b7c30d100921" href="/guides/data-apis/working-with-comments">
    Handle page and inline comments.
  </Card>

  <Card title="Content queries" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/magnifyingGlass.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=532b9d39e18feeffe9c342c0ebab7da6" href="/reference/post-search">
    Search through workspace content.
  </Card>

  <Card title="Users" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/people.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=9db041f17fd02578d17a1e9a633f4c46" href="/reference/user">
    Access user profiles and permissions.
  </Card>
</CardGroup>

### Content access

Connections must have access to pages and databases before they can interact with them. The mechanism differs by type:

* **Internal connections** can be granted access in two ways: the connection owner can add pages directly from the **Content access** tab in the Developer portal, or workspace members can share pages via the **Add connections** menu in Notion.
* **Public connections** use the OAuth page picker, where users select which pages to grant access to during the authorization flow.
* **Personal access tokens** use the token creator's existing Notion permissions. If the creator can access a page in Notion, a PAT with the right capabilities can access it through the API.

See the [Internal connections](/guides/get-started/internal-connections), [Public connections](/guides/get-started/public-connections), and [Personal access tokens](/guides/get-started/personal-access-tokens) guides for specifics on how content access works for each type.

### Webhooks

Connections can subscribe to real-time events — like page updates, property changes, and new comments — via webhooks. This allows your connection to react to changes in Notion without polling the API. See the [Webhooks guide](/reference/webhooks) for details on setting up webhook subscriptions.

## Starting your connection journey

We recommend starting with an internal connection — it's the fastest way to begin building. You get an API token immediately and can focus entirely on using the API within your workspace, without worrying about OAuth or Marketplace listing. You can always create a public connection later if you need multi-workspace support.

Here's a guided path through the documentation:

<Steps>
  <Step>
    [**Quickstart**](/guides/get-started/quick-start) — Build your first connection with a hands-on tutorial.
  </Step>

  <Step>
    [**Personal access tokens**](/guides/get-started/personal-access-tokens) — Create a user-scoped token for scripts, CLI workflows, Workers, or trusted tools.
  </Step>

  <Step>
    [**Internal connections**](/guides/get-started/internal-connections) — Understand how internal connections work, including the permissions model.
  </Step>

  <Step>
    [**Public connections**](/guides/get-started/public-connections) — Learn how public connections work, including installation scope and the OAuth flow.
  </Step>

  <Step>
    [**Authorization**](/guides/get-started/authorization) — Implement the OAuth 2.0 flow for public connections.
  </Step>

  <Step>
    [**Handling API keys**](/guides/get-started/handling-api-keys) — Secure and manage your API tokens in production.
  </Step>

  <Step>
    [**Preparing for users**](/guides/get-started/preparing-for-users) — Set up databases, pages, and views automatically when users install your connection.
  </Step>

  <Step>
    [**List on the Marketplace**](/guides/get-started/marketplace-listing) — Make your public connection discoverable to all Notion users.
  </Step>
</Steps>

## Resources

Explore the links below to get started, and join the [Notion Devs Slack community](https://join.slack.com/t/notiondevs/shared_invite/zt-3u9oid9q8-HLUBmMVWYK~g9HFo4U4raA) to share your projects and connect with fellow developers.

<CardGroup>
  <Card title="API reference" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/curlyBraces.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=46f7a8b4a34544f9b03002e4ecc35ad5" href="/reference/intro" />

  <Card title="Notion SDK for JavaScript" icon="js" href="https://github.com/makenotion/notion-sdk-js" />

  <Card title="Starter templates" icon="github" href="https://github.com/makenotion/notion-sdk-typescript-starter" />

  <Card title="Postman collection" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/cube.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=ca03d98b0912c199f06d1110d9c2f64b" href="https://www.postman.com/notionhq/notion-s-api-workspace/collection/52041987-03f70d8f-b6e5-4306-805c-f95f7cdf05b9" />

  <Card title="FAQs" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/questionMarkCircle.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=20159b5b3d48676a4735f2c3f9fdda77" href="/page/frequently-asked-questions" />

  <Card title="Notion Devs Slack" icon="slack" href="https://join.slack.com/t/notiondevs/shared_invite/zt-3u9oid9q8-HLUBmMVWYK~g9HFo4U4raA" />
</CardGroup>
