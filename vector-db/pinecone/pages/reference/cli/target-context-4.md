---
title: "CLI target context"
source: https://docs.pinecone.io/reference/cli/target-context
path: reference/cli/target-context
---

Set the Pinecone CLI target context with pc target to control which organization and project your commands run against, including in CI/CD and JSON mode.

The CLI's **target context** determines which organization and project your commands operate on. You must [authenticate](/reference/cli/authentication) before setting target context.

## Flags

| Flag                | Short | Default | Description                                                                       |
| ------------------- | ----- | ------- | --------------------------------------------------------------------------------- |
| `--org`             | `-o`  | —       | Target organization by name. Mutually exclusive with `--organization-id`.         |
| `--organization-id` | —     | —       | Target organization by ID. Mutually exclusive with `--org`.                       |
| `--project`         | `-p`  | —       | Target project by name. Mutually exclusive with `--project-id`.                   |
| `--project-id`      | —     | —       | Target project by ID. Mutually exclusive with `--project`.                        |
| `--show`            | `-s`  | `false` | Show the current target context.                                                  |
| `--clear`           | —     | `false` | Clear the stored target context.                                                  |
| `--json`            | `-j`  | `false` | Output as JSON. In non-TTY environments (CI/CD, pipes), JSON output is automatic. |

<Note>
  `--org` and `--organization-id` are mutually exclusive — use one or the other. The same applies to `--project` and `--project-id`.
</Note>

## How operations use target context

| Operation type                   | Scope                                    |
| -------------------------------- | ---------------------------------------- |
| Control plane (indexes, backups) | Target project                           |
| Data plane (vectors, namespaces) | Target project + specified index         |
| Admin API (organizations)        | No target context needed                 |
| Admin API (projects)             | Target organization                      |
| Admin API (API keys)             | Target project (unless `--id` specified) |

## Target context by auth method

### User login

After `pc auth login`, the CLI auto-targets your default organization and its first project.

```bash theme={null}
# Change target
pc target -o "my-org" -p "my-project"
```

### Service account

**Via CLI command:** After `pc auth configure --client-id --client-secret`, the CLI auto-targets the service account's organization. For the project:

* If one project exists, it's auto-targeted
* If multiple exist, you're prompted (or use `--project-id`)
* If none exist, create one and target it manually

**Via environment variables:** If using `PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET` without running `pc auth configure`, no target context is set automatically. Run `pc target` to set it.

```bash theme={null}
# Change project (org is fixed to the service account's org)
pc target -p "my-project"

# Or select interactively
pc target
```

### API key

<Warning>
  When using an API key, control plane and data plane operations use the **key's org/project scope**, not the CLI's stored target context. The `pc target --show` output does not reflect what these operations actually use.
</Warning>

API keys are scoped to a specific org and project and cannot access resources outside that scope.

Admin API operations still use your user login or service account credentials (API keys can't authenticate Admin API calls).

## Managing target context

```bash theme={null}
pc target --show   # View current target
pc target --clear  # Clear target context
```

### JSON mode and non-TTY environments

Running `pc target --json` with no targeting flags returns the current target context as a JSON object. This is a local-state read — **no authentication is required**:

```bash theme={null}
pc target --json
```

In non-TTY environments (CI/CD pipelines, shell pipes, scripts), JSON output is automatic — the same as passing `--json` explicitly. You do not need to add the flag in automation contexts.

Use `--organization-id` and `--project-id` (instead of name flags) to set context reliably in scripts, since IDs are stable and unaffected by renames:

```bash theme={null}
pc target --organization-id "org-abc123" --project-id "proj-xyz789" --json
```
