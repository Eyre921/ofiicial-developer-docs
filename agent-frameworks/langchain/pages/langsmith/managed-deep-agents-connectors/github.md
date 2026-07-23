---
title: "Connect GitHub repositories to Managed Deep Agents"
source: https://docs.langchain.com/langsmith/managed-deep-agents-connectors/github
path: langsmith/managed-deep-agents-connectors/github
---

Clone GitHub repositories, install the GitHub CLI, and inject credentials into a Managed Deep Agents sandbox.

The GitHub connector prepares repositories, the `gh` CLI, and credentials inside a [managed sandbox](/langsmith/managed-deep-agents-deploy#configure-a-sandbox). Use it when the agent needs to inspect or change GitHub repositories.

<Note>
  The GitHub connector requires `managed-deepagents>=0.4.0`.
</Note>

<Note>
  Managed Deep Agents is in **private [beta](/langsmith/release-stages)**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

This connector is separate from the [GitHub channel](/langsmith/managed-deep-agents-channels/github), which receives App webhooks, and Connect-with-GitHub under [identity](/langsmith/managed-deep-agents-identity).

## Add the connector

Create `connectors/github.py` or `connectors/github.ts`:

<CodeGroup>
  ```python connectors/github.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents.connectors import github

  connector = github.connector(
      repositories=[
          {
              "repo": "acme/api",
              "path": "workspace/api",
              "ref": "main",
              "depth": 1,
              "on_reuse": "fetch",
          }
      ],
  )
  ```

  ```ts connectors/github.ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { github } from "managed-deepagents";

  export default github.connector({
    repositories: [
      {
        repo: "acme/api",
        path: "workspace/api",
        ref: "main",
        depth: 1,
        onReuse: "fetch",
      },
    ],
  });
  ```
</CodeGroup>

The connector clones each repository when the sandbox is created. On reuse, `on_reuse` / `onReuse` controls whether it keeps, resets, or fetches the checkout. The default is `fetch`.

## Configure options

| Option (Python / TypeScript)               | Default | Purpose                                               |
| ------------------------------------------ | ------- | ----------------------------------------------------- |
| `repositories`                             | `[]`    | Repository checkouts and their sandbox paths.         |
| `allowlist`                                | `[]`    | Allowed repositories as `owner/repo` or `owner/*`.    |
| `install_cli` / `installCLI`               | `true`  | Install the GitHub CLI in the sandbox.                |
| `inject_credentials` / `injectCredentials` | `true`  | Expose resolved GitHub credentials to `git` and `gh`. |

Repository paths must be relative and unique. Set `write` to `true` on a checkout that needs write credentials.

For private repositories, configure GitHub credentials through [identity](/langsmith/managed-deep-agents-identity#custom-downstream-credentials). The runtime injects the resolved token as `GH_TOKEN` and configures Git credentials without storing it in thread state.

## Test and deploy

Test the project locally with [`mda dev`](/langsmith/managed-deep-agents-cli#develop-locally), then deploy it with [`mda deploy`](/langsmith/managed-deep-agents-deploy). Open deployment traces in LangSmith to inspect model calls, tool calls, errors, and latency.

The connector runs only when the project declares a managed sandbox. After startup, ask the agent to inspect the configured path or run `gh auth status`.

## Next steps

<CardGroup>
  <Card title="Connectors" icon="plug" href="/langsmith/managed-deep-agents-connectors">
    Compare connector types.
  </Card>

  <Card title="GitHub channel" icon="brand-github" href="/langsmith/managed-deep-agents-channels/github">
    Receive GitHub App webhooks.
  </Card>

  <Card title="Identity" icon="fingerprint" href="/langsmith/managed-deep-agents-identity">
    Scope callers and resolve credentials.
  </Card>

  <Card title="Configure a sandbox" icon="box" href="/langsmith/managed-deep-agents-deploy#configure-a-sandbox">
    Configure sandbox scope and lifecycle.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-connectors/github.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
