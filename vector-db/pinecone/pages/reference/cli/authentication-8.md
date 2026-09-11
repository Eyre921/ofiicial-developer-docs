---
title: "CLI authentication"
source: https://docs.pinecone.io/reference/cli/authentication
path: reference/cli/authentication
---

Authenticate the Pinecone CLI using user login, service accounts, or API keys, including auth priority and Admin API access rules.

This document describes how to authenticate the Pinecone CLI to manage your Pinecone resources.

## Authentication methods

| Method                              | Admin API | Control/data plane | Best for                         |
| ----------------------------------- | --------- | ------------------ | -------------------------------- |
| [User login](#user-login)           | ✅         | ✅                  | Interactive use                  |
| [Service account](#service-account) | ✅         | ✅                  | Automation with Admin API access |
| [API key](#api-key)                 | ❌         | ✅                  | Simple automation, CI/CD         |

### User login

Authenticate through a web browser. The token refreshes automatically and stays valid for up to 120 days (re-auth required after 30 days of inactivity).

```bash theme={null}
pc auth login
```

The CLI auto-targets your default organization and its first project. Change with `pc target -o "my-org" -p "my-project"`.

### Service account

Authenticate with credentials from a [service account](/guides/organizations/manage-service-accounts).

```bash theme={null}
pc auth configure --client-id "ID" --client-secret "SECRET"

# Or via environment variables
export PINECONE_CLIENT_ID="your-client-id"
export PINECONE_CLIENT_SECRET="your-client-secret"
```

The CLI auto-targets the service account's organization. For projects: auto-selects if one exists, prompts if multiple exist, or set manually with `pc target -p "my-project"`.

### API key

Authenticate with an [API key](/guides/projects/manage-api-keys). API keys can't access the Admin API.

```bash theme={null}
pc auth configure --api-key "YOUR_API_KEY"

# Or via environment variable
export PINECONE_API_KEY="your-api-key"
```

<Warning>
  API keys are scoped to a specific project. When set, control/data plane operations use the **key's project**, ignoring any [target context](/reference/cli/target-context) you've set.
</Warning>

## Auth priority

When multiple credentials exist, the CLI chooses based on operation type. Within each credential type, environment variables take precedence over stored configuration.

**Control/data plane operations:**

1. API key
2. User login token (via [managed keys](#managed-keys))
3. Service account (via [managed keys](#managed-keys))

**Admin API operations:**

1. User login token
2. Service account

<Note>
  User login and service account are mutually exclusive when configured via CLI commands—each clears the other. However, service account env vars don't clear a stored user login token.
</Note>

**Example scenarios:**

* If `PINECONE_API_KEY` is set, the CLI uses it for control/data plane operations, regardless of any stored API key.
* If you're logged in via `pc auth login` and also have `PINECONE_CLIENT_ID`/`PINECONE_CLIENT_SECRET` set, the user login token is used for everything—the service account env vars are ignored.
* If you have an API key configured and are also logged in, the API key is used for control/data plane operations, but user login is used for Admin API operations (since API keys can't access Admin API).

## Managed keys

When using user login or service account (without a default API key), the CLI automatically creates and manages API keys for control/data plane operations. This happens transparently on first use.

* **Stored locally:** `~/.config/pinecone/secrets.yaml` (permissions 0600)
* **Stored remotely:** Visible in console as `pinecone-cli-{id}` with origin `cli_created`

```bash theme={null}
# List locally tracked managed keys
pc auth local-keys list

# Delete managed keys (local + remote)
pc auth local-keys prune

# Delete only CLI-created managed keys
pc auth local-keys prune --origin cli

# Delete only user-created managed keys
pc auth local-keys prune --origin user

# Delete a specific API key by ID
pc api-key delete --id "KEY_ID"
```

<Note>
  When you run `pc api-key create --store` for a project that already has a CLI-created managed key, the CLI automatically deletes the old remote key before storing the new one.
</Note>

## Logging out

```bash theme={null}
pc auth logout
```

Clears all local auth data: tokens, credentials, API keys, managed keys, and [target context](/reference/cli/target-context).

<Note>
  `pc auth logout` doesn't delete managed keys from Pinecone's servers. Run `pc auth local-keys prune` first for full cleanup.
</Note>

## Local storage

Auth data is stored in `~/.config/pinecone/` with 0600 permissions:

| File           | Contents                                                         |
| -------------- | ---------------------------------------------------------------- |
| `secrets.yaml` | OAuth token, service account credentials, API keys, managed keys |
| `state.yaml`   | Target org/project                                               |
| `config.yaml`  | CLI settings (color, environment)                                |

## Check status

```bash theme={null}
pc auth status
```

Shows your current authentication method, target organization and project, token expiration (for user login), and environment configuration.
