---
title: "Introduction"
source: https://docs.turso.tech/cli/introduction
path: cli/introduction
---

The Turso CLI gives you everything you need from the command line to manage your database, API tokens, inviting users, and launching the database shell. If you're waiting for a migration to run, there's also a relax command.

You can also programmatically manage your Turso account, including groups, databases, organizations and invites using the [Platform API](/api-reference).

<Steps>
  <Step title="Install">
    Begin by installing the Turso CLI:

    <CodeGroup>
      ```bash macOS theme={null}
      brew install tursodatabase/tap/turso
      ```

      ```bash Linux theme={null}
      curl -sSfL https://get.tur.so/install.sh | bash
      ```

      ```bash Windows (WSL) theme={null}
      curl -sSfL https://get.tur.so/install.sh | bash
      ```
    </CodeGroup>
  </Step>

  <Step title="Authenticate">
    Now signup or login:

    <CodeGroup>
      ```bash Signup theme={null}
      turso auth signup
      ```

      ```bash Login theme={null}
      turso auth login
      ```

      ```bash Signup (WSL) theme={null}
      turso auth signup --headless
      ```

      ```bash Login (WSL) theme={null}
      turso auth login --headless
      ```
    </CodeGroup>
  </Step>

  <Step title="Operate">
    The Turso CLI provides the following commands:

    | Command                     | Description                                                          |
    | --------------------------- | -------------------------------------------------------------------- |
    | [`auth`](/cli/auth)         | Authenticate and manage API tokens.                                  |
    | [`contact`](/cli/contact)   | Submit your feedback, ideas and create a meeting with the team.      |
    | [`db`](/cli/db)             | Create and manage databases, access tokens and connect to the shell. |
    | `dev`                       | Run Turso [locally](/local-development) for development.             |
    | [`group`](/cli/group)       | Create groups for databases with a shared location.                  |
    | [`org`](/cli/org)           | Manage billing and invite members.                                   |
    | [`plan`](/cli/plan)         | `overages`, `select`, `show`, `upgrade`                              |
    | [`quickstart`](/quickstart) | Get started with Turso in 5 minutes.                                 |
    | `relax`                     | Take some time out and relax with Turso.                             |
    | `update`                    | Update to the Turso CLI to the latest version with one command.      |
  </Step>
</Steps>
