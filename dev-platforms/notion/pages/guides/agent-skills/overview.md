---
title: "Agent Skills API"
source: https://developers.notion.com/guides/agent-skills/overview
path: guides/agent-skills/overview
---

Learn how to download AI skills stored in Notion.

The Agent Skills API exposes skills stored in Notion as directories of files. You can either download individual skills following the [Agent Skills standard](https://agentskills.io/home), or groups of related skills following the [Agent Plugins standard](https://agent-plugins.org).

Teams use Notion as a [skills library](https://www.notion.com/help/create-and-manage-skills) to edit, review, and share skills. Each skill's main `SKILL.md` file is a Notion page. Supporting files and folders can be attached through its **Files** property.

For some examples of how to use the API, see:

* the [notion-skills-github-sync](https://github.com/makenotion/notion-skills-github-sync) sample repo, which sets up a recurring script that syncs skills from Notion into a GitHub plugin marketplace, which can further be synced into Claude, ChatGPT, or other agents.
* the Vercel [skills CLI](https://github.com/vercel-labs/skills), which uses the Skills API to help users install skills for local agents.

<CardGroup>
  <Card title="List plugins" href="/reference/agent-skills/list-skills-plugins" icon="list">
    List available plugins
  </Card>

  <Card title="Get a plugin" href="/reference/agent-skills/get-plugin-directory" icon="folder-tree">
    Download a single plugin
  </Card>

  <Card title="Get a skill" href="/reference/agent-skills/get-skill-directory" icon="file-code">
    Download a single skill
  </Card>
</CardGroup>

## Requirements

* You have a [connection](/guides/get-started/authorization) token or [personal access token](/guides/get-started/personal-access-tokens) with the **Read content** capability.
* The connection has access to the skill databases you expect to see. Skills not shared with the connection are omitted.
* Requests send `Notion-Version: 2026-03-11`.

## Sync workflow

Here is an example of a common usage pattern for this API: syncing all plugins from a workspace to a local directory.

<Steps>
  <Step title="List plugins">
    Call [List plugins](/reference/agent-skills/list-skills-plugins) and page through the results. Each entry has an `id`, `name`, `description`, and `version_id`.

    ```bash cURL theme={null}
    curl -X GET "https://api.notion.com/v1/ai/plugins?page_size=100" \
      -H "Authorization: Bearer $NOTION_API_KEY" \
      -H "Notion-Version: 2026-03-11"
    ```

    ```json Response theme={null}
    {
      "object": "list",
      "results": [
        {
          "id": "b2d0a1f4-9c3e-4c07-9a1d-5f6e7c8b9a01",
          "name": "Engineering",
          "description": "Skills for engineering workflows.",
          "version_id": "ba9d2c7735c0029282f9f8e7bef99b438c51ad416f82ca8a8d6ce56c5a1fa95c"
        },
        {
          "id": "1a7f3c92-4de8-4b15-8c60-2e9d4f0a6b73",
          "name": "Weekly status update",
          "description": "Write the Monday status update from last week's project pages.",
          "version_id": "43dd93dd612651c00ebbaa9ca5fad10d845e2b145aba8ac219033654d6a58c93"
        }
      ],
      "next_cursor": null,
      "has_more": false,
      "type": "plugin",
      "request_id": "b7c1fd7e-2c84-4f55-877e-d3ad7db2ac4b"
    }
    ```

    The first result is a tagged plugin holding every skill tagged **Engineering**. The second is an untagged skill, which becomes a plugin of its own.
  </Step>

  <Step title="Compare version_id values">
    Compare each plugin's `version_id` against the value you stored the last time
    you downloaded it. Equal values mean the plugin has not changed and you can
    skip it. Only after all pages have been fetched successfully, remove local
    directories for plugin IDs missing from the complete list. An incomplete or
    failed listing must not delete local plugins.
  </Step>

  <Step title="Fetch changed plugin directories">
    For each plugin whose `version_id` changed, call [Get a plugin directory](/reference/agent-skills/get-plugin-directory) to receive a signed URL.

    ```bash cURL theme={null}
    curl -X GET "https://api.notion.com/v1/ai/plugins/$PLUGIN_ID" \
      -H "Authorization: Bearer $NOTION_API_KEY" \
      -H "Notion-Version: 2026-03-11"
    ```

    ```json Response theme={null}
    {
      "id": "b2d0a1f4-9c3e-4c07-9a1d-5f6e7c8b9a01",
      "version_id": "ba9d2c7735c0029282f9f8e7bef99b438c51ad416f82ca8a8d6ce56c5a1fa95c",
      "url": "https://s3.us-west-2.amazonaws.com/notion-temporary-files/public-api/plugin-directories/b2d0a1f4-9c3e-4c07-9a1d-5f6e7c8b9a01/ba9d2c7735c0029282f9f8e7bef99b438c51ad416f82ca8a8d6ce56c5a1fa95c/engineering.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=3600&X-Amz-Signature=...",
      "request_id": "91a4ee8c-61f6-4c27-bd41-09aa35299929"
    }
    ```
  </Step>

  <Step title="Download and extract the archive">
    Set `SIGNED_URL` to the `url` from the previous response, then download and extract the gzipped tar archive into your plugins directory.

    ```bash cURL theme={null}
    mkdir -p ./plugins
    curl --fail --location "$SIGNED_URL" -o plugin.tar.gz &&
      tar -xzf plugin.tar.gz -C ./plugins
    ```

    ```
    plugins/engineering/
    ├── plugin.json
    └── skills/
        ├── code-review/
        │   ├── SKILL.md
        │   └── checklist.pdf
        └── incident-postmortem/
            └── SKILL.md
    ```
  </Step>
</Steps>

For a complete example of a sync script, see [notion-skills-github-sync](https://github.com/makenotion/notion-skills-github-sync).
