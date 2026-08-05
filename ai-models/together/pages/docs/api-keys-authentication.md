---
title: "Authentication"
source: https://docs.together.ai/docs/api-keys-authentication
path: docs/api-keys-authentication
---

Create, manage, and authenticate with project-scoped API keys.

Together AI uses API keys to authenticate requests. Keys are scoped to [projects](/docs/projects), meaning a key only has access to the resources within its project.

<Note>
  Multi-project key scoping is in early access. Not all resources and APIs fully support project-scoped keys yet. See [Early access limitations](/docs/projects#early-access-limitations) for details.
</Note>

## Create an API key

Create independent API keys for separate use cases, systems, or workloads. For example, one for production, one for development, one for CI/CD, and one for inference.

<Steps>
  <Step title="Open the project">
    Navigate to the project you want to create a key for.
  </Step>

  <Step title="Open API key settings">
    Go to the project's [API keys settings](https://api.together.ai/settings/projects/~current/api-keys).
  </Step>

  <Step title="Create the key">
    Select **Create API Key**, give it a name and an optional expiration date, then select **Create**.
  </Step>

  <Step title="Copy the key">
    Copy the key immediately. It won't be shown again.
  </Step>
</Steps>

<Warning>
  New API keys are displayed only once at creation. Save them in a secure location, such as a secrets manager, immediately. If you lose a key, you'll need to create a new one.
</Warning>

## Best practices

* **Name your keys descriptively** (for example, `prod-inference`, `ci-pipeline`, `dev-local`) so you can identify and rotate them.
* **Set expiration dates** for keys used in temporary or testing contexts. To set the expiration date, select **the three-dot menu** next to the key and select **Set expiration**.
* **Rotate keys regularly** and revoke any that are no longer in use.
* **Never commit keys to source control.** Use environment variables or a secrets manager.

## Set as an environment variable

To use the Together Python or TypeScript SDKs, set your key as an environment variable in your shell:

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export TOGETHER_API_KEY="your_api_key"
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:TOGETHER_API_KEY="your_api_key"
  ```
</CodeGroup>

Or add it to a `.env` file in your project directory:

```dotenv .env theme={null}
TOGETHER_API_KEY=your_api_key
```

## Authenticate a request

Include your API key in the `Authorization` header of every API request:

```bash theme={null}
curl https://api.together.ai/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

## Project key scoping

API keys are scoped to projects:

* A key created in project A can only access resources in project A.
* Keys persist even if the collaborator who created them is removed from the project.
* Both project admins and member-role collaborators can create and revoke keys.

This means you can safely share a project API key with a CI/CD pipeline or external collaborator without giving them access to resources in other projects.

<Note>
  Project key scoping is in early access. Not all resources and APIs fully support this feature yet. Keys created before multi-project support was enabled are scoped to your organization's default project.
</Note>

## Playground

The [Together AI playground](https://api.together.ai/playground/) recognizes all API keys associated with your account. When you use the playground, it shows available models across all your keys and projects.

## Cost analytics and usage

Use API key IDs to segment usage and cost by key and workload. The `api_key_id` field is supported for inference and code interpreter requests, so you can track which keys are driving spend in your [project's cost analytics](https://api.together.ai/settings/projects/~current/cost-analytics).

## Limitations

**No per-key usage limits:** You can't cap spend or rate-limit individual API keys. Usage limits apply at the organization level.

## Legacy API keys

Your organization may have a legacy API key scoped to its default project. Only the organization owner can access and manage it, in [organization settings](https://api.together.ai/settings/organization/~current) under **Manage Account**.

Legacy keys are deprecated, and you should **avoid using them in production.** These keys can't be scoped to a specific project or workload, and can't be revoked (only regenerated if compromised). Use [project-scoped API keys](#create-an-api-key) instead.

## Related resources

<CardGroup>
  <Card title="Projects" icon="folder" href="/docs/projects">
    Understand how API keys are scoped to projects.
  </Card>

  <Card title="Roles and permissions" icon="shield" href="/docs/roles-permissions">
    See who can create and manage API keys.
  </Card>
</CardGroup>
