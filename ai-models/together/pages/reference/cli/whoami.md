---
title: "Whoami"
source: https://docs.together.ai/reference/cli/whoami
path: reference/cli/whoami
---

Show the project and organization for the API key used by the Together CLI.

Use `tg whoami` to confirm the project and organization for the API key the CLI uses. This helps when you manage multiple API keys or switch between projects and need to verify the active context before running a command that creates or modifies resources.

```bash theme={null}
tg whoami
```

Sample output:

```bash theme={null}
$ tg whoami
     Project: My Project (proj_xxxxxxxxxxxxxxxx)
Organization: Acme, Inc. (org_xxxxxxxxxxxxxxxx)
```

The command reads the API key from the `TOGETHER_API_KEY` environment variable or `--api-key` flag and reports the project and organization that key is scoped to.

## JSON output

Pass `--json` to get the full structured response, which includes the API key ID and the project slug:

```bash theme={null}
$ tg whoami --json
{
  "api_key_id": "key_xxxxxxxxxxxxxxxx",
  "organization_id": "org_xxxxxxxxxxxxxxxx",
  "organization_name": "Acme, Inc.",
  "project_id": "proj_xxxxxxxxxxxxxxxx",
  "project_name": "My Project",
  "project_slug": "my-project"
}
```

The `project_slug` is the DNS-friendly project identifier used when constructing the `model` value (`<project_slug>/<endpoint_slug>`) for dedicated endpoint inference calls.
