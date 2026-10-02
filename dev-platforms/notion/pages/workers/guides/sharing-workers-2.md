---
title: "Sharing Workers"
source: https://developers.notion.com/workers/guides/sharing-workers
path: workers/guides/sharing-workers
---

Share and collaborate with other workspace members on a Notion Worker.

Sharing a Worker involves two separate access decisions:

* **Access to the deployed Worker in Notion:** Manage access from the <a href={developerWorkersUrl}>Developer portal</a>. This controls who can connect to, manage, edit, and deploy the Worker. Store environment variable values and [secrets](/workers/guides/secrets) with the deployed Worker.
* **Access to the Worker's source code:** Store the source code in a team-owned Git repository, such as GitHub. Use `workers.json` to identify the Worker to be deployed. Configure continuous integration for auto-deploys on code changes.

## Share access to a Worker

Share a Worker to give workspace members access to its deployed capabilities. Sharing does not give them access to the Worker source code.

<Steps>
  <Step title="Open the Developer portal">
    Open the <a href={developerWorkersUrl}>Workers page</a> in the Developer portal.
  </Step>

  <Step title="Choose a Worker">
    Select the Worker you want to share, then select **Share**.
  </Step>

  <Step title="Choose members and access">
    Search for workspace members, choose an access level, and select **Share**.
  </Step>
</Steps>

### Access levels

* **Can connect:** View and connect this Worker to agents.
* **Full access:** Manage, edit, and deploy the Worker, and connect it to agents.

### Manage environment variables

Store environment variable values, including secrets, with the deployed Worker, not in the source code. Workspace members need **Full access** to manage or pull these values.

For local development, confirm that the target file is ignored by Git, then run `ntn workers env pull`. Commit only an `.env.example` with variable names and placeholder values. See [How to manage secrets](/workers/guides/secrets) for details.

## Collaborate on Worker source code

The source code that defines a Worker cannot be downloaded directly from Notion. Store the source code in a team-owned Git repository, such as GitHub, so your team has one place to share changes and collaborate on the code.

### Identify the deployed Worker

Commit `workers.json` with the project so developers and CI use the same Worker target. It contains the `workerId` that tells `ntn workers deploy` which deployed Worker to update. It can also contain `workspaceId` to select the workspace. The CLI can override the configured Worker with `--worker-id` when needed.

### Deploy from continuous integration

Use a continuous integration (CI) workflow, such as GitHub Actions, to deploy Worker code with `ntn workers deploy`.

For non-interactive deployments, set `NOTION_API_TOKEN` to a personal access token with the **Workers** capability and store it as a GitHub Actions secret. Set `NOTION_WORKSPACE_ID` in the workflow or `workspaceId` in `workers.json` so the command does not prompt for a workspace.

The workflow uses the token owner's permissions. Use an approved account and a separate token for each environment, and rotate tokens before they expire. See [Personal access tokens](/guides/get-started/personal-access-tokens) and the [CLI command reference](/cli/reference/commands) for details.
