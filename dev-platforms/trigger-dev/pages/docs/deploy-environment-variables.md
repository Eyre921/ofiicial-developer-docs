---
title: "Environment Variables"
source: https://trigger.dev/docs/deploy-environment-variables
path: docs/deploy-environment-variables
---

Any environment variables used in your tasks need to be added so the deployed code will run successfully.

An environment variable in Node.js is accessed in your code using `process.env.MY_ENV_VAR`.

We deploy your tasks and scale them up and down when they are triggered. So any environment variables you use in your tasks need to accessible to us so your code will run successfully.

## In the dashboard

### Setting environment variables

**1. Go to the Environment Variables page**

In the sidebar select the "Environment Variables" page, then press the "Add new"
button. ![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=af652254781808a35c2bcefd4b61b59f)

**2. Add your environment variables**

You can add values for your local dev environment, staging and prod. ![Environment variables
page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=79b5fd91e809cb0c6c9298410922df96)

> [!NOTE]
>
> Specifying Dev values is optional. They will be overriden by values in your .env file when running
> locally.

### Secret environment variables

When creating an environment variable, you can mark it as a **Secret**. Secret values are hidden in the dashboard and cannot be viewed after creation.

> [!WARNING]
>
> Marking a variable as a Secret is irreversible and can only be done when creating the variable. To
> change this setting, you must delete the variable and create a new one.

### Editing environment variables

You can edit an environment variable's values. You cannot edit the key name, you must delete and create a new one.

> [!WARNING]
>
> **Rolling out.** This feature is being enabled gradually and may not be available
> for your organization yet.

> [!NOTE]
>
> An empty string is a valid value. Saving a variable with an empty value stores it as an empty
> string (your task sees the variable set to `""`), which is different from deleting the variable
> (where your task does not see it at all).

**1. Press the action button on a variable**

![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=05dd8ce39784065107f6eba1625866d0)

**2. Press edit**

![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=e865f9406555034430788bbf98fbc785)

### Deleting environment variables

Environment variables are fetched and injected before a runs begins. So if you delete one you can
cause runs to fail that are expecting variables to be set.

**1. Press the action button on a variable**

![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=05dd8ce39784065107f6eba1625866d0)

**2. Press delete**

This will immediately delete the variable. ![Environment variables
page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=642350946bd75c3c508065a198aaa005)

## Local development

When running `npx trigger.dev dev`, the CLI automatically loads environment variables from these files in order (later files override any duplicate keys from earlier ones):

* `.env`
* `.env.development`
* `.env.local`
* `.env.development.local`
* `dev.vars`

These variables are available to your tasks via `process.env`. You don't need to use the `--env-file` flag for this automatic loading.

## In your code

You can use our SDK to get and manipulate environment variables. You can also easily sync environment variables from another service into Trigger.dev.

### Directly manipulating environment variables

We have a complete set of SDK functions (and REST API) you can use to directly manipulate environment variables.

| Function | Description |
| - | - |
| [envvars.list()](/docs/management/envvars/list) | List all environment variables |
| [envvars.upload()](/docs/management/envvars/import) | Upload multiple env vars. You can override existing values. |
| [envvars.create()](/docs/management/envvars/create) | Create a new environment variable |
| [envvars.retrieve()](/docs/management/envvars/retrieve) | Retrieve an environment variable |
| [envvars.update()](/docs/management/envvars/update) | Update a single environment variable |
| [envvars.del()](/docs/management/envvars/delete) | Delete a single environment variable |

#### Initial load from .env file

To initially load environment variables from a `.env` file into your Trigger.dev cloud environment, you can use `envvars.upload()`. This is useful for one-time bulk imports when setting up a new project or environment.

```ts theme={"theme":"css-variables"}
import { envvars } from "@trigger.dev/sdk";
import { readFileSync } from "fs";
import { parse } from "dotenv";

// Read and parse your .env file
const envContent = readFileSync(".env.production", "utf-8");
const parsed = parse(envContent);

// Upload to Trigger.dev (replace with your project ref and environment slug)
await envvars.upload("proj_your_project_ref", "prod", {
  variables: parsed,
  override: false, // Set to true to override existing variables
});
```

When called inside a task, you can omit the project ref and environment slug as they'll be automatically inferred from the task context:

```ts theme={"theme":"css-variables"}
import { envvars, task } from "@trigger.dev/sdk";
import { readFileSync } from "fs";
import { parse } from "dotenv";

export const setupEnvVars = task({
  id: "setup-env-vars",
  run: async () => {
    const envContent = readFileSync(".env.production", "utf-8");
    const parsed = parse(envContent);

    // projectRef and environment slug are automatically inferred from ctx
    await envvars.upload({
      variables: parsed,
      override: false,
    });
  },
});
```

> [!NOTE]
>
> This is different from `syncEnvVars` which automatically syncs variables during every deploy. Use `envvars.upload()` for one-time initial loads, and `syncEnvVars` for ongoing synchronization.

#### Getting the current environment

When using `envvars.retrieve()` inside a task, you can access the current environment information from the task context (`ctx`). The `envvars.retrieve()` function doesn't return the environment, but you can get it from `ctx.environment`:

```ts theme={"theme":"css-variables"}
import { envvars, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload, { ctx }) => {
    // Get the current environment information
    const currentEnv = ctx.environment.slug; // e.g., "dev", "prod", "staging"
    const envType = ctx.environment.type; // e.g., "DEVELOPMENT", "PRODUCTION", "STAGING", "PREVIEW"

    // Retrieve an environment variable
    // When called inside a task, projectRef and slug are automatically inferred
    const apiKey = await envvars.retrieve("API_KEY");

    console.log(`Retrieved API_KEY from environment: ${currentEnv} (${envType})`);
    console.log(`Value: ${apiKey.value}`);
  },
});
```

The context object provides:

* `ctx.environment.slug` - The environment slug (e.g., "dev", "prod")
* `ctx.environment.type` - The environment type ("DEVELOPMENT", "PRODUCTION", "STAGING", or "PREVIEW")
* `ctx.environment.id` - The environment ID
* `ctx.project.ref` - The project reference

For more information about the context object, see the [Context documentation](/docs/context).

#### Linking to a run in the dashboard

Trigger.dev sets `TRIGGER_DASHBOARD_URL` on every run, in development and deployed environments. Its value is the dashboard's address without a trailing slash, so it also points at your own instance when you self-host. Append `/runs/<runId>` to link to a run:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const reportTask = task({
  id: "report-task",
  run: async (payload, { ctx }) => {
    const runUrl = `${process.env.TRIGGER_DASHBOARD_URL}/runs/${ctx.run.id}`;

    console.log(`View this run: ${runUrl}`);
  },
});
```

The `/runs/<runId>` link checks that the viewer is a member of the run's organization, then redirects to the full run page. If you set your own `TRIGGER_DASHBOARD_URL` environment variable on the project, your value is used instead.

### Sync env vars from another service

There are two ways to pull secrets from another service into Trigger.dev: a native **Secret Sync** (currently [Infisical](https://infisical.com)), or the `syncEnvVars` build extension for any other service.

#### Infisical Secret Sync

If your secrets live in [Infisical](https://infisical.com), sync them natively, without a build extension or a redeploy. You configure the sync in the Infisical dashboard, and it pushes secrets straight to your [Environment Variables page](#in-the-dashboard) in Trigger.dev. When a secret changes in Infisical the sync updates the matching variable, and your tasks pick up the new value on their next run.

Set it up in Infisical in two steps:

1. Add a **Trigger.dev App Connection** using a Trigger.dev Personal Access Token from your account settings. Self-hosted instances are supported.
2. Create a **Secret Sync**: choose the connection, pick the target organization, project and environment (Production, Staging, Development, or Preview), and set the secret path to sync.

Follow the [Trigger.dev Secret Sync guide](https://infisical.com/docs/integrations/secret-syncs/trigger-dev) in the Infisical docs for the full walkthrough.

> [!NOTE]
>
> A Secret Sync only overwrites the keys it manages, leaving variables you set manually untouched.
> Synced variables are marked as [secret](#secret-environment-variables) by default, so they appear
> redacted on the Environment Variables page.

#### Using the `syncEnvVars` build extension

For any other service, use our `syncEnvVars` build extension in your `trigger.config` file to resolve secrets at deploy time.

> [!NOTE]
>
> To use the `syncEnvVars` build extension, you should first install the `@trigger.dev/build`
> package into your devDependencies.

In this example we're using env vars from [Infisical](https://infisical.com), but you can adapt it to any secrets manager.

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";
import { InfisicalSDK } from "@infisical/sdk";

export default defineConfig({
  build: {
    extensions: [
      syncEnvVars(async (ctx) => {
        const client = new InfisicalSDK();

        await client.auth().universalAuth.login({
          clientId: process.env.INFISICAL_CLIENT_ID!,
          clientSecret: process.env.INFISICAL_CLIENT_SECRET!,
        });

        const { secrets } = await client.secrets().listSecrets({
          environment: ctx.environment,
          projectId: process.env.INFISICAL_PROJECT_ID!,
        });

        return secrets.map((secret) => ({
          name: secret.secretKey,
          value: secret.secretValue,
        }));
      }),
    ],
  },
});
```

#### Syncing environment variables from Vercel

To sync environment variables from your Vercel projects to Trigger.dev, you can use our build extension. Check out our [syncing environment variables from Vercel guide](/docs/guides/examples/vercel-sync-env-vars).

#### Deploy

When you run the [CLI deploy command](/docs/cli-deploy-commands) directly or using [GitHub Actions](/docs/github-actions) it will sync the environment variables from [Infisical](https://infisical.com) to Trigger.dev. This means they'll appear on the Environment Variables page so you can confirm that it's worked.

This means that you need to redeploy your Trigger.dev tasks if you change the environment variables in [Infisical](https://infisical.com).

> [!NOTE]
>
> The `process.env.INFISICAL_CLIENT_ID`, `process.env.INFISICAL_CLIENT_SECRET` and
> `process.env.INFISICAL_PROJECT_ID` will need to be supplied to the `deploy` CLI command. You can
> do this via the `--env-file .env` flag or by setting them as environment variables in your
> terminal.

#### Dev

`syncEnvVars` does not have any effect when running the `dev` command locally. If you want to inject environment variables from another service into your local environment you can do so via a `.env` file or just supplying them as environment variables in your terminal. Most services will have a CLI tool that allows you to run a command with environment variables set:

```sh theme={"theme":"css-variables"}
infisical run -- npx trigger.dev@latest dev
```

Any environment variables set in the CLI command will be available to your local Trigger.dev tasks.

### The syncEnvVars callback return type

You can return env vars as an object with string keys and values, or an array of names + values.

```ts theme={"theme":"css-variables"}
return {
  MY_ENV_VAR: "my value",
  MY_OTHER_ENV_VAR: "my other value",
};
```

or

```ts theme={"theme":"css-variables"}
return [
  {
    name: "MY_ENV_VAR",
    value: "my value",
  },
  {
    name: "MY_OTHER_ENV_VAR",
    value: "my other value",
  },
];
```

This should mean that for most secret services you won't need to convert the data into a different format.

### Using Google credential JSON files

Securely pass a Google credential JSON file to your Trigger.dev task using environment variables.

**1. Convert the Google credential file to base64**

In your terminal, run the following command and copy the resulting base64 string:

```
base64 -i path/to/your/service-account-file.json
```

**2. Set up the environment variable in Trigger.dev**

Follow [these steps](/docs/deploy-environment-variables) to set a new environment variable using the base64 string as the value.

```
GOOGLE_CREDENTIALS_BASE64="<your base64 string>"
```

**3. Use the environment variable in your code**

Add the following code to your Trigger.dev task:

```ts theme={"theme":"css-variables"}
import { google } from "googleapis";

const credentials = JSON.parse(
  Buffer.from(process.env.GOOGLE_CREDENTIALS_BASE64, "base64").toString("utf8")
);

const auth = new google.auth.GoogleAuth({
  credentials,
  scopes: ["https://www.googleapis.com/auth/cloud-platform"],
});

const client = await auth.getClient();
```

**4. Use the client in your code**

You can now use the `client` object to make authenticated requests to Google APIs

## Using `.env.production` or dotenvx with Trigger.dev

Trigger.dev does not automatically load `.env.production` files or dotenvx files during deploys.\
To use these files in your Trigger.dev environment:

### Option 1 — Manually add your environment variables

1. Open your `.env.production` (or `.env`) file
2. Copy the full contents
3. Go to your Trigger.dev project → **Environment Variables**
4. Click **Add variables**
5. Paste the contents directly into the editor

Trigger.dev will automatically parse and create each key/value pair.

This is the simplest way to bring dotenvx or `.env.production` variables into your Trigger.dev environment.

### Option 2 — Sync variables automatically using `syncEnvVars`

If you'd prefer an automated flow, you can use the `syncEnvVars` build extension to programmatically load and return your variables:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";
import dotenvx from "@dotenvx/dotenvx";
import { readFileSync } from "fs";

export default defineConfig({
  project: "<project id>",
  build: {
    extensions: [
      syncEnvVars(async () => {
        const envContent = readFileSync(".env.production", "utf-8");
        const parsed = dotenvx.parse(envContent);
        return parsed ?? {};
      }),
    ],
  },
});
```

This will read your .env.production file using dotenvx and sync the variables to Trigger.dev during every deploy.

**Summary**

* Trigger.dev does not automatically detect .env.production or dotenvx files
* You can paste them manually into the dashboard
* Or sync them automatically using a build extension

## Multi-tenant applications

If you're building a multi-tenant application where each tenant needs different environment variables (like tenant-specific API keys or database credentials), you don't need a separate project for each tenant. Instead, use a single project and load tenant-specific secrets at runtime.

> [!NOTE]
>
> This is different from [syncing environment variables at deploy time](#sync-env-vars-from-another-service).
> Here, secrets are loaded dynamically during task execution, not synced to Trigger.dev's environment variables.

### Recommended approach

Use a secrets service (Infisical, AWS Secrets Manager, HashiCorp Vault, etc.) to store tenant-specific secrets, then retrieve them at the start of each task run based on the tenant identifier in your payload or context.

**Important:** Never pass secrets in the task payload, as payloads are logged and visible in the dashboard.

### Example implementation

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

export const processTenantData = task({
  id: "process-tenant-data",
  run: async (payload: { tenantId: string; data: unknown }) => {
    // Retrieve tenant-specific secret at runtime
    const client = new SecretsManagerClient({ region: "us-east-1" });
    const response = await client.send(
      new GetSecretValueCommand({
        SecretId: `tenants/${payload.tenantId}/supabase-key`,
      })
    );

    const supabaseKey = JSON.parse(response.SecretString!).SUPABASE_SERVICE_KEY;

    // Your task logic using the tenant-specific secret
    // ...
  },
});
```

You can use any secrets service - see the [sync env vars section](#sync-env-vars-from-another-service) for an example with Infisical.

### Benefits

* **Single codebase** - Deploy once, works for all tenants
* **Secure** - Secrets never appear in payloads or logs
* **Scalable** - No project limit constraints
* **Flexible** - Easy to add new tenants without redeploying

This approach allows you to support unlimited tenants with a single Trigger.dev project, avoiding the [project limit](/docs/limits#projects) while maintaining security and separation of tenant data.
