---
title: "Installing the CLI"
source: https://docs.trychroma.com/docs/cli/install
path: docs/cli/install
---

Install the Chroma CLI to run a local server, browse collections, and interact with Chroma Cloud.

The Chroma CLI lets you run a Chroma server locally on your machine, install sample apps, browse your collections, interact with your Chroma Cloud DBs, and much more!

When you install our Python or JavaScript package globally, you will automatically get the Chroma CLI.

If you don't use one of our packages, you can still install the CLI as a standalone program with `cURL` (or `iex` on Windows).

## Python

You can install Chroma using `pip`:

```bash theme={null}
pip install chromadb
```

If your machine does not allow for global `pip` installs, you can get the Chroma CLI with `pipx`:

```bash theme={null}
pipx install chromadb
```

## JavaScript

<CodeGroup>
  ```bash npm theme={null}
  npm install -g chromadb
  ```

  ```bash pnpm theme={null}
  pnpm add -g chromadb
  ```

  ```bash bun theme={null}
  bun add -g chromadb
  ```

  ```bash yarn theme={null}
  yarn global add chromadb
  ```
</CodeGroup>

## Install Globally

<CodeGroup>
  ```bash cURL theme={null}
  curl -sSL https://raw.githubusercontent.com/chroma-core/chroma/main/rust/cli/install/install.sh | bash
  ```

  ```bash Windows theme={null}
  iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/chroma-core/chroma/main/rust/cli/install/install.ps1'))
  ```
</CodeGroup>
