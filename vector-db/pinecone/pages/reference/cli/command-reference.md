---
title: "CLI command reference"
source: https://docs.pinecone.io/reference/cli/command-reference
path: reference/cli/command-reference
---

Complete Pinecone CLI command reference covering syntax, subcommands, flags, help output, and exit codes for auth, index, and project.

This document provides a complete reference for all Pinecone CLI commands.

## Command structure

The Pinecone CLI uses a hierarchical command structure. Each command consists of a primary command followed by one or more subcommands and optional flags.

```bash theme={null}
pc <command> <subcommand> [flags]
pc <command> <subcommand> <subcommand> [flags]
```

For example:

```bash theme={null}
# Top-level command with flags
pc target -o "organization-name" -p "project-name"

# Command (index) and subcommand (list)
pc index list

# Command (index) and subcommand (create) with flags
pc index create \
  --name my-index \
  --dimension 1536 \
  --metric cosine \
  --cloud aws \
  --region us-east-1

# Command (auth) and nested subcommands (local-keys prune) with flags
pc auth local-keys prune --id proj-abc123 --skip-confirmation
```

## Getting help

The CLI provides help for commands at every level:

```bash theme={null}
# top-level help
pc --help
pc -h

# command help
pc auth --help
pc index --help
pc project --help

# subcommmand help
pc index create --help
pc project create --help
pc auth configure --help

# nested subcommand help
pc auth local-keys prune --help
```

## Exit codes

All commands return exit code `0` for success and `1` for error.

## Available commands

This section describes all commands offered by the Pinecone CLI.

### Top-level commands

> [accordion] pc login (Authenticate via user login)
>
> **Description**
>
> Authenticate via a web browser. After login, set a [target org and project](/reference/cli/target-context) with `pc target` before accessing data. This command defaults to an initial organization and project to which
> you have access (these values display in the terminal), but you can change them with `pc target`.
>
> **Usage**
>
> ```bash theme={null}
> pc login
> ```
>
> **Flags**
>
> None
>
> **Global Flags**
>
> | Long flag | Short flag | Description |
> | :- | :- | :- |
> | `--help` | `-h` | Show help information |
> | `--quiet` | `-q` | Suppress output |
> | `--timeout` | | Timeout (default 60s, 0 to disable) |
>
> **Example**
>
> ```bash theme={null}
> # Log in via browser
> pc login
>
> # Then set target context
> pc target -o "my-org" -p "my-project"
> ```
>
> > [!NOTE]
> >
> > This is an alias for `pc auth login`. Both commands perform the same operation.

> [accordion] pc logout (Clear credentials / log out)
>
> **Description**
>
> Clears all authentication data from local storage, including:
>
> * User login token
> * Service account credentials (client ID and secret)
> * Default (manually specified) API key
> * Locally managed keys (for all projects)
> * Target organization and project context
>
> **Usage**
>
> ```bash theme={null}
> pc logout
> ```
>
> **Flags**
>
> None
>
> **Global Flags**
>
> | Long flag | Short flag | Description |
> | :- | :- | :- |
> | `--help` | `-h` | Show help information |
> | `--quiet` | `-q` | Suppress output |
> | `--timeout` | | Timeout (default 60s, 0 to disable) |
>
> **Example**
>
> ```bash theme={null}
> # Clear all credentials and context
> pc logout
> ```
>
> > [!NOTE]
> >
> > This is an alias for `pc auth logout`. Both commands perform the same operation. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.

> [accordion] pc target (Set target organization and project)
>
> **Description**
>
> Set the target organization and project for the CLI. Supports interactive organization and project selection or direct specification via flags.  For details, see [CLI target context](/reference/cli/target-context).
>
> **Usage**
>
> ```bash theme={null}
> pc target [flags]
> ```
>
> **Flags**
>
> | Long flag | Short flag | Description |
> | :- | :- | :- |
> | `--clear` | | Clear target context |
> | `--json` | `-j` | Output in JSON format |
> | `--org` | `-o` | Organization name |
> | `--organization-id` | | Organization ID |
> | `--project` | `-p` | Project name |
> | `--project-id` | | Project ID |
> | `--show` | `-s` | Display current target context |
>
> **Global Flags**
>
> | Long flag | Short flag | Description |
> | :- | :- | :- |
> | `--help` | `-h` | Show help information |
> | `--quiet` | `-q` | Suppress output |
> | `--timeout` | | Timeout (default 60s, 0 to disable) |
>
> **Example**
>
> ```bash theme={null}
> # Interactive targeting after login
> pc login
> pc target
>
> # Set specific organization and project
> pc target -o "my-org" -p "my-project"
>
> # Show current context
> pc target --show
>
> # Clear all context
> pc target --clear
> ```

> [accordion] pc version (Show CLI version)
>
> **Description**
>
> Displays version information for the CLI, including the version number, commit SHA, and build date.
>
> **Usage**
>
> ```bash theme={null}
> pc version
> ```
>
> **Flags**
>
> None
>
> **Global Flags**
>
> | Long flag | Short flag | Description |
> | :- | :- | :- |
> | `--help` | `-h` | Show help information |
> | `--quiet` | `-q` | Suppress output |
> | `--timeout` | | Timeout (default 60s, 0 to disable) |
>
> **Example**
>
> ```bash theme={null}
> # Display version information
> pc # Pinecone Docs

> This file is very large and may be truncated. For an index of this content, please refer to https://docs.pinecone.io/llms.txt instead.

> Official documentation for Pinecone's trusted AI knowledge platform, including Pinecone Database, Pinecone Assistant, and Pinecone Nexus.
