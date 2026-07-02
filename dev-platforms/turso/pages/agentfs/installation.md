---
title: "Installation"
source: https://docs.turso.tech/agentfs/installation
path: agentfs/installation
---

Install the AgentFS CLI on Linux, macOS, and Windows

## Quick Install

The fastest way to install AgentFS:

```bash theme={null}
curl -fsSL https://github.com/tursodatabase/agentfs/releases/latest/download/agentfs-installer.sh | sh
```

This installs the `agentfs` binary to `~/.cargo/bin`.

## Platform-Specific Instructions

<Tabs>
  <Tab title="macOS">
    ```bash theme={null}
    curl -fsSL https://github.com/tursodatabase/agentfs/releases/latest/download/agentfs-installer.sh | sh
    ```

    After installation, restart your terminal or run:

    ```bash theme={null}
    source ~/.zshrc  # or ~/.bashrc
    ```
  </Tab>

  <Tab title="Linux">
    **Using the installer:**

    ```bash theme={null}
    curl -fsSL https://github.com/tursodatabase/agentfs/releases/latest/download/agentfs-installer.sh | sh
    ```

    After installation, restart your terminal or run:

    ```bash theme={null}
    source ~/.bashrc  # or ~/.zshrc
    ```

    **Requirements:**

    * FUSE must be available for filesystem mounting
    * On Ubuntu/Debian: `sudo apt install fuse3`
    * On Fedora: `sudo dnf install fuse3`
  </Tab>

  <Tab title="Windows">
    **Using PowerShell:**

    ```powershell theme={null}
    irm https://github.com/tursodatabase/agentfs/releases/latest/download/agentfs-installer.ps1 | iex
    ```

    Or download the binary directly from the [releases page](https://github.com/tursodatabase/agentfs/releases).
  </Tab>
</Tabs>

## Verify Installation

```bash theme={null}
agentfs --version
```

## Shell Completions

Enable tab completion for your shell:

```bash theme={null}
# Auto-detect shell
agentfs completions install

# Or specify shell explicitly
agentfs completions install bash
agentfs completions install zsh
agentfs completions install fish
```

Restart your shell after installing completions.

## Building from Source

Requires Rust 1.70+:

```bash theme={null}
git clone https://github.com/tursodatabase/agentfs.git
cd agentfs/cli
cargo install --path .
```

## Next Steps

<CardGroup>
  <Card title="Agentic Coding" icon="robot" href="/agentfs/guides/sandbox">
    Run AI coding agents safely
  </Card>

  <Card title="CLI Reference" icon="terminal" href="/agentfs/reference/cli">
    Full command reference
  </Card>
</CardGroup>
