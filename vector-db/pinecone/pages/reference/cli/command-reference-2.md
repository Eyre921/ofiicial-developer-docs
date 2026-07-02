---
title: "CLI command reference"
source: https://docs.pinecone.io/reference/cli/command-reference
path: reference/cli/command-reference
---

CLI command reference: This document provides a complete reference for all Pinecone CLI commands.

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

<AccordionGroup>
  <Accordion title="pc login (Authenticate via user login)">
    **Description**

    Authenticate via a web browser. After login, set a [target org and project](/reference/cli/target-context) with `pc target` before accessing data. This command defaults to an initial organization and project to which
    you have access (these values display in the terminal), but you can change them with `pc target`.

    **Usage**

    ```bash theme={null}
    pc login
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Log in via browser
    pc login

    # Then set target context
    pc target -o "my-org" -p "my-project"
    ```

    <Note>
      This is an alias for `pc auth login`. Both commands perform the same operation.
    </Note>
  </Accordion>

  <Accordion title="pc logout (Clear credentials / log out)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash theme={null}
    pc logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Clear all credentials and context
    pc logout
    ```

    <Note>
      This is an alias for `pc auth logout`. Both commands perform the same operation. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc target (Set target organization and project)">
    **Description**

    Set the target organization and project for the CLI. Supports interactive organization and project selection or direct specification via flags.  For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash theme={null}
    pc target [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                    |
    | :------------------ | :--------- | :----------------------------- |
    | `--clear`           |            | Clear target context           |
    | `--json`            | `-j`       | Output in JSON format          |
    | `--org`             | `-o`       | Organization name              |
    | `--organization-id` |            | Organization ID                |
    | `--project`         | `-p`       | Project name                   |
    | `--project-id`      |            | Project ID                     |
    | `--show`            | `-s`       | Display current target context |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Interactive targeting after login
    pc login
    pc target

    # Set specific organization and project
    pc target -o "my-org" -p "my-project"

    # Show current context
    pc target --show

    # Clear all context
    pc target --clear
    ```
  </Accordion>

  <Accordion title="pc version (Show CLI version)">
    **Description**

    Displays version information for the CLI, including the version number, commit SHA, and build date.

    **Usage**

    ```bash theme={null}
    pc version
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Display version information
    pc version
    ```
  </Accordion>

  <Accordion title="pc whoami (Show current user)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash theme={null}
    pc whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc whoami
    ```

    <Note>
      This is an alias for `pc auth whoami`. Both commands perform the same operation.
    </Note>
  </Accordion>
</AccordionGroup>

### Authentication

<AccordionGroup>
  <Accordion title="pc auth clear (Clear specific credentials)">
    **Description**

    Selectively clears specific authentication data without affecting other credentials. At least one flag is required.

    **Usage**

    ```bash theme={null}
    pc auth clear [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                                         |
    | :------------------ | :--------- | :-------------------------------------------------- |
    | `--api-key`         |            | Clear only the default (manually specified) API key |
    | `--service-account` |            | Clear only service account credentials              |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Clear only the default (manually specified) API key
    pc auth clear --api-key
    pc auth status

    # Clear service account
    pc auth clear --service-account
    ```

    <Note>
      More surgical than `pc auth logout`. Does not clear user login token or managed keys. For those, use `pc auth logout` or `pc auth local-keys prune`.
    </Note>
  </Accordion>

  <Accordion title="pc auth configure (Configure service account or API key)">
    **Description**

    Configures service account credentials or a default (manually specified) API key.

    Service accounts automatically target the organization and prompt for project selection, unless there is only one project. A default API key overrides any previously specified target organization/project context. When setting a service account, this operation clears the user login token, if one exists.
    For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash theme={null}
    pc auth configure [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                          |
    | :---------------------- | :--------- | :--------------------------------------------------- |
    | `--api-key`             |            | Default API key to use for authentication            |
    | `--client-id`           |            | Service account client ID                            |
    | `--client-secret`       |            | Service account client secret                        |
    | `--client-secret-stdin` |            | Read client secret from stdin                        |
    | `--json`                | `-j`       | Output in JSON format                                |
    | `--project-id`          | `-p`       | Target project ID (optional, interactive if omitted) |
    | `--prompt-if-missing`   |            | Prompt for missing credentials                       |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Service account setup (auto-targets org and prompts for project)
    pc auth configure --client-id my-id --client-secret my-secret

    # Service account with specific project
    pc auth configure \
      --client-id my-id \
      --client-secret my-secret \
      -p proj-123

    # Default API key (overrides any target context)
    pc auth configure --api-key pcsk_abc123
    ```

    <Note>
      `pc auth configure --api-key "YOUR_API_KEY"` does the same thing as `pc config set-api-key "YOUR_API_KEY"`. To learn about targeting a project after authenticating with a service account, see [CLI target context](/reference/cli/target-context).
    </Note>
  </Accordion>

  <Accordion title="pc auth local-keys list (List managed keys)">
    **Description**

    Displays all [managed API keys](/reference/cli/authentication#managed-keys) stored locally by the CLI, with various details.

    **Usage**

    ```bash theme={null}
    pc auth local-keys list [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                |
    | :--------- | :--------- | :----------------------------------------- |
    | `--json`   | `-j`       | Output in JSON format                      |
    | `--reveal` |            | Show the actual API key values (sensitive) |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all locally managed keys
    pc auth local-keys list

    # Show key values
    pc auth local-keys list --reveal

    # After storing a key
    pc api-key create -n "my-key" --store
    pc auth local-keys list
    ```
  </Accordion>

  <Accordion title="pc auth local-keys prune (Delete managed keys)">
    **Description**

    Deletes locally stored [managed API keys](/reference/cli/authentication#managed-keys) from local storage and Pinecone's servers. Filters by origin (`cli`/`user`/`all`) or project ID.

    **Usage**

    ```bash theme={null}
    pc auth local-keys prune [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--dry-run`           |            | Preview deletions without applying                          |
    | `--id`                |            | Prune keys for specific project ID only                     |
    | `--json`              | `-j`       | Output in JSON format                                       |
    | `--origin`            | `-o`       | Filter by origin - `cli`, `user`, or `all` (default: `all`) |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Preview deletions
    pc auth local-keys prune --dry-run

    # Delete CLI-created keys only
    pc auth local-keys prune -o cli --skip-confirmation

    # Delete for specific project
    pc auth local-keys prune --id proj-abc123

    # Before/after check
    pc auth local-keys list
    pc auth local-keys prune -o cli
    pc auth local-keys list
    ```

    <Note>
      This deletes keys from both local storage and Pinecone servers. Use `--dry-run` to preview before committing.
    </Note>
  </Accordion>

  <Accordion title="pc auth login (Authenticate via user login)">
    **Description**

    Authenticate via user login in the web browser. After login, [set a target org and project](/reference/cli/target-context).

    **Usage**

    ```bash theme={null}
    pc auth login
    pc login  # shorthand
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Login and set target
    pc auth login
    pc target -o "my-org" -p "my-project"
    pc index list
    ```

    <Note>
      Tokens refresh automatically and remain valid for up to 120 days. If you're inactive for more than 30 days, you must re-authenticate. Logging in clears any existing service account credentials. This command does the same thing as `pc login`.
    </Note>
  </Accordion>

  <Accordion title="pc auth logout (Clear authentication credentials)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash theme={null}
    pc auth logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Clear all credentials and context
    pc auth logout
    ```

    <Note>
      This command does the same thing as `pc logout`. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc auth status (Show authentication status)">
    **Description**

    Shows details about all configured authentication methods.

    **Usage**

    ```bash theme={null}
    pc auth status [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Check status after login
    pc auth login
    pc auth status

    # JSON output for scripting
    pc auth status --json
    ```
  </Accordion>

  <Accordion title="pc auth whoami (Show current user information)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash theme={null}
    pc auth whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc auth whoami
    ```

    <Note>
      This command does the same thing as `pc whoami`.
    </Note>
  </Accordion>
</AccordionGroup>

### Indexes

<AccordionGroup>
  <Accordion title="pc index configure (Update index configuration)">
    **Description**

    Modifies the configuration of an existing index.

    **Usage**

    ```bash theme={null}
    pc index configure [flags]
    ```

    **Flags**

    | Long flag                | Short flag | Description                                                     |
    | :----------------------- | :--------- | :-------------------------------------------------------------- |
    | `--index-name`           | `-i`       | Name of index to configure (required)                           |
    | `--deletion-protection`  |            | Enable or disable deletion protection - `enabled` or `disabled` |
    | `--tags`                 |            | Custom user tags (key=value pairs)                              |
    | `--json`                 | `-j`       | Output in JSON format                                           |
    | **Dedicated read nodes** |            |                                                                 |
    | `--read-mode`            |            | Read capacity mode - `ondemand` or `dedicated`                  |
    | `--read-node-type`       |            | Node type for dedicated read - `b1` or `t1`                     |
    | `--read-shards`          |            | Number of shards for dedicated read capacity                    |
    | `--read-replicas`        |            | Number of replicas for dedicated read capacity                  |
    | **Integrated embedding** |            |                                                                 |
    | `--model`                |            | Embedding model name                                            |
    | `--field-map`            |            | Field mapping for embedding (key=value pairs)                   |
    | `--read-parameters`      |            | Read parameters for embedding model (key=value pairs)           |
    | `--write-parameters`     |            | Write parameters for embedding model (key=value pairs)          |
    | **Pods**                 |            |                                                                 |
    | `--pod-type`             | `-t`       | Type of pod to use; can only upgrade when configuring           |
    | `--replicas`             | `-r`       | Number of replicas of the index to configure                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Enable deletion protection
    pc index configure --index-name my-index --deletion-protection enabled

    # Add tags
    pc index configure --index-name my-index --tags environment=production,team=ml

    # Switch to dedicated read capacity
    pc index configure --index-name my-index \
      --read-mode dedicated \
      --read-node-type b1 \
      --read-shards 2 \
      --read-replicas 2

    # Verify changes
    pc index describe --index-name my-index
    ```

    <Note>
      Configuration changes may take some time to take effect.
    </Note>
  </Accordion>

  <Accordion title="pc index create (Create a new index)">
    **Description**

    Creates a new index in your Pinecone project. Supports serverless, pod-based, integrated (with embedding model), and BYOC (Bring Your Own Cloud) index types.

    **Usage**

    ```bash theme={null}
    pc index create [flags]
    ```

    **Flags**

    | Long flag                | Short flag | Description                                                                    |
    | :----------------------- | :--------- | :----------------------------------------------------------------------------- |
    | `--name`                 | `-n`       | Index name (required)                                                          |
    | `--dimension`            | `-d`       | Vector dimension (required for standard indexes, optional for integrated)      |
    | `--metric`               | `-m`       | Similarity metric - `cosine`, `euclidean`, or `dotproduct` (default: `cosine`) |
    | `--cloud`                | `-c`       | Cloud provider - `aws`, `gcp`, or `azure`                                      |
    | `--region`               | `-r`       | Cloud region                                                                   |
    | `--vector-type`          | `-v`       | Vector type - `dense` or `sparse` (serverless only)                            |
    | `--source-collection`    |            | Name of the source collection from which to create the index                   |
    | `--schema`               |            | Metadata schema to control which fields are indexed (comma-separated)          |
    | `--deletion-protection`  |            | Deletion protection - `enabled` or `disabled`                                  |
    | `--tags`                 |            | Custom user tags (key=value pairs)                                             |
    | `--json`                 | `-j`       | Output in JSON format                                                          |
    | **Integrated indexes**   |            |                                                                                |
    | `--model`                |            | Integrated embedding model name                                                |
    | `--field-map`            |            | Field mapping for integrated embedding (key=value pairs)                       |
    | `--read-parameters`      |            | Read parameters for embedding model (key=value pairs)                          |
    | `--write-parameters`     |            | Write parameters for embedding model (key=value pairs)                         |
    | **BYOC indexes**         |            |                                                                                |
    | `--byoc-environment`     |            | BYOC environment to use for the index                                          |
    | **Dedicated read nodes** |            |                                                                                |
    | `--read-mode`            |            | Read capacity mode - `ondemand` or `dedicated` (default: `ondemand`)           |
    | `--read-node-type`       |            | Node type for dedicated read - `b1` or `t1`                                    |
    | `--read-shards`          |            | Number of shards (each shard provides 250 GB storage)                          |
    | `--read-replicas`        |            | Number of replicas for higher throughput                                       |
    | **Pod-based indexes**    |            |                                                                                |
    | `--environment`          |            | Environment of the index to create (for example, `us-east-1-aws`)              |
    | `--pod-type`             |            | Type of pod to use (for example, `p1.x1`, `s1.x2`)                             |
    | `--shards`               |            | Number of shards (default: `1`)                                                |
    | `--replicas`             |            | Number of replicas (default: `1`)                                              |
    | `--metadata-config`      |            | Comma-separated list of metadata fields to index for search                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Create serverless index
    pc index create -n my-index -d 1536 -m cosine -c aws -r us-east-1

    # Create sparse vector index
    pc index create -n sparse-index -m dotproduct -c aws -r us-east-1 --vector-type sparse

    # With integrated embedding model
    pc index create \
      -n my-index \
      -m cosine \
      -c aws \
      -r us-east-1 \
      --model multilingual-e5-large \
      --field-map text=chunk_text

    # With dedicated read capacity
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r us-east-1 \
      --read-mode dedicated \
      --read-node-type b1 \
      --read-shards 2 \
      --read-replicas 2

    # With deletion protection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r us-west-2 \
      --deletion-protection enabled

    # From collection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r eu-west-1 \
      --source-collection my-collection

    # Create pod-based index
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      --environment us-east-1-aws \
      --pod-type p1.x1 \
      --shards 1 \
      --replicas 1
    ```

    <Note>
      For a list of valid regions for a serverless index, see [Create a serverless index](/guides/index-data/create-an-index).
    </Note>
  </Accordion>

  <Accordion title="pc index delete (Delete an index)">
    **Description**

    Permanently deletes an index and all its data. This operation cannot be undone.

    **Usage**

    ```bash theme={null}
    pc index delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                |
    | :-------------------- | :--------- | :--------------------------------------------------------- |
    | `--index-name`        | `-i`       | Name of index to delete (required)                         |
    | `--skip-confirmation` |            | Skip the deletion confirmation prompt                      |
    | `--json`              | `-j`       | Output in JSON format (also skips the confirmation prompt) |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete an index (prompts for confirmation)
    pc index delete --index-name my-index

    # Skip the confirmation prompt
    pc index delete --index-name my-index --skip-confirmation

    # List before and after
    pc index list
    pc index delete --index-name test-index --skip-confirmation
    pc index list
    ```

    <Note>
      This command prompts for confirmation before deleting. Pass `--skip-confirmation` (or `--json`) to bypass the prompt in non-interactive contexts.
    </Note>
  </Accordion>

  <Accordion title="pc index describe (Show index details)">
    **Description**

    Displays detailed configuration and status information for a specific index.

    **Usage**

    ```bash theme={null}
    pc index describe [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description           |
    | :------------- | :--------- | :-------------------- |
    | `--index-name` | `-i`       | Index name (required) |
    | `--json`       | `-j`       | Output in JSON format |

    The `--name`/`-n` flag is a deprecated alias for `--index-name`/`-i`.

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe an index
    pc index describe -i my-index

    # JSON output
    pc index describe -i my-index -j

    # Check newly created index
    pc index create -n test-index -d 1536 -m cosine -c aws -r us-east-1
    pc index describe -i test-index
    ```
  </Accordion>

  <Accordion title="pc index stats (Show index statistics)">
    **Description**

    Displays statistics for an index, including total vector count and namespace breakdown. Optionally filter results with a metadata filter.

    **Usage**

    ```bash theme={null}
    pc index stats [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                                    |
    | :------------- | :--------- | :------------------------------------------------------------- |
    | `--index-name` | `-i`       | Index name (required)                                          |
    | `--filter`     | `-f`       | Metadata filter (inline JSON, `./path.json`, or `-` for stdin) |
    | `--json`       | `-j`       | Output in JSON format                                          |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Get stats for an index
    pc index stats -i my-index

    # Get stats with a metadata filter
    pc index stats -i my-index --filter '{"genre":{"$eq":"rock"}}'

    # Filter from file
    pc index stats -i my-index --filter ./filter.json

    # JSON output
    pc index stats -i my-index -j
    ```
  </Accordion>

  <Accordion title="pc index list (List all indexes)">
    **Description**

    Displays all indexes in your current target project, including various details.

    **Usage**

    ```bash theme={null}
    pc index list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                         |
    | :-------- | :--------- | :-------------------------------------------------- |
    | `--json`  | `-j`       | Output in JSON format (includes full index details) |
    | `--wide`  | `-w`       | Show additional columns (host, embed, tags)         |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all indexes
    pc index list

    # Show additional details
    pc index list --wide

    # JSON output for scripting
    pc index list -j

    # After creating indexes
    pc index create -n test-1 -d 768 -m cosine -c aws -r us-east-1
    pc index list
    ```
  </Accordion>
</AccordionGroup>

### Namespaces

<AccordionGroup>
  <Accordion title="pc index namespace create (Create a namespace)">
    **Description**

    Creates a new namespace within an index. Namespaces allow you to partition vectors within an index.

    **Usage**

    ```bash theme={null}
    pc index namespace create [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                         |
    | :------------- | :--------- | :-------------------------------------------------- |
    | `--index-name` | `-i`       | Index name (required)                               |
    | `--name`       |            | Namespace name (required)                           |
    | `--schema`     |            | Metadata schema for the namespace (comma-separated) |
    | `--json`       | `-j`       | Output in JSON format                               |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Create a namespace
    pc index namespace create -i my-index --name tenant-a

    # Create with metadata schema (comma-separated list of filterable metadata fields)
    pc index namespace create -i my-index --name tenant-b --schema "category,brand"

    # JSON output
    pc index namespace create -i my-index --name tenant-c -j
    ```
  </Accordion>

  <Accordion title="pc index namespace delete (Delete a namespace)">
    **Description**

    Deletes a namespace and all its vectors from an index. This operation cannot be undone.

    **Usage**

    ```bash theme={null}
    pc index namespace delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                            |
    | :-------------------- | :--------- | :--------------------------------------------------------------------- |
    | `--index-name`        | `-i`       | Index name (required)                                                  |
    | `--name`              |            | Namespace name (required); use `__default__` for the default namespace |
    | `--skip-confirmation` |            | Skip the deletion confirmation prompt                                  |
    | `--json`              | `-j`       | Output in JSON format (also skips the confirmation prompt)             |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete a namespace (prompts for confirmation)
    pc index namespace delete -i my-index --name tenant-a

    # Delete the default namespace
    pc index namespace delete -i my-index --name __default__

    # Skip the confirmation prompt
    pc index namespace delete -i my-index --name tenant-a --skip-confirmation
    ```

    <Warning>
      Deleting a namespace removes all vectors in that namespace. This operation cannot be undone.
    </Warning>
  </Accordion>

  <Accordion title="pc index namespace describe (Show namespace details)">
    **Description**

    Displays detailed information about a specific namespace, including record count and schema configuration.

    **Usage**

    ```bash theme={null}
    pc index namespace describe [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                                            |
    | :------------- | :--------- | :--------------------------------------------------------------------- |
    | `--index-name` | `-i`       | Index name (required)                                                  |
    | `--name`       |            | Namespace name (required); use `__default__` for the default namespace |
    | `--json`       | `-j`       | Output in JSON format                                                  |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe a namespace
    pc index namespace describe -i my-index --name tenant-a

    # Describe the default namespace
    pc index namespace describe -i my-index --name __default__

    # JSON output
    pc index namespace describe -i my-index --name tenant-a -j
    ```
  </Accordion>

  <Accordion title="pc index namespace list (List namespaces)">
    **Description**

    Lists all namespaces within an index, including vector counts.

    **Usage**

    ```bash theme={null}
    pc index namespace list [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                    |
    | :------------------- | :--------- | :----------------------------- |
    | `--index-name`       | `-i`       | Index name (required)          |
    | `--limit`            | `-l`       | Maximum number of results      |
    | `--pagination-token` | `-p`       | Pagination token for next page |
    | `--prefix`           |            | Filter namespaces by prefix    |
    | `--json`             | `-j`       | Output in JSON format          |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all namespaces
    pc index namespace list -i my-index

    # Filter by prefix
    pc index namespace list -i my-index --prefix "tenant-"

    # Limit results
    pc index namespace list -i my-index --limit 10

    # JSON output
    pc index namespace list -i my-index -j
    ```
  </Accordion>
</AccordionGroup>

### Vectors

<AccordionGroup>
  <Accordion title="pc index vector delete (Delete vectors)">
    **Description**

    Deletes vectors from an index by ID, filter, or deletes all vectors in a namespace.

    **Usage**

    ```bash theme={null}
    pc index vector delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                               |
    | :-------------------- | :--------- | :------------------------------------------------------------------------ |
    | `--index-name`        | `-i`       | Index name (required)                                                     |
    | `--namespace`         |            | Namespace to delete from (default: `__default__`)                         |
    | `--ids`               |            | Vector IDs to delete (inline JSON array, `./path.json`, or `-` for stdin) |
    | `--filter`            |            | Metadata filter (inline JSON, `./path.json`, or `-` for stdin)            |
    | `--all-vectors`       |            | Delete all vectors in the namespace                                       |
    | `--skip-confirmation` |            | Skip the confirmation prompt shown for `--all-vectors`                    |
    | `--json`              | `-j`       | Output in JSON format (also skips the confirmation prompt)                |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete specific vectors
    pc index vector delete -i my-index --ids '["id1"]'

    # Delete multiple vectors (inline JSON array, or JSON array in a file)
    pc index vector delete -i my-index --ids '["id1", "id2"]'

    # Delete by filter
    pc index vector delete -i my-index --filter '{"genre":"classical"}'

    # Delete all vectors in a namespace (prompts for confirmation)
    pc index vector delete -i my-index --namespace old-data --all-vectors

    # Delete all vectors without the prompt
    pc index vector delete -i my-index --namespace old-data --all-vectors --skip-confirmation
    ```

    <Note>
      Only `--all-vectors` prompts for confirmation. Targeted deletes with `--ids` or `--filter` proceed without a prompt. Pass `--skip-confirmation` (or `--json`) to bypass the `--all-vectors` prompt.
    </Note>

    <Warning>
      Vector deletion is permanent and cannot be undone.
    </Warning>
  </Accordion>

  <Accordion title="pc index vector fetch (Fetch vectors by ID or filter)">
    **Description**

    Retrieves vectors by their IDs or by a metadata filter, returning the vector values and metadata.

    **Usage**

    ```bash theme={null}
    pc index vector fetch [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                                              |
    | :------------------- | :--------- | :----------------------------------------------------------------------- |
    | `--index-name`       | `-i`       | Index name (required)                                                    |
    | `--namespace`        |            | Namespace to fetch from (default: `__default__`)                         |
    | `--ids`              |            | Vector IDs to fetch (inline JSON array, `./path.json`, or `-` for stdin) |
    | `--filter`           | `-f`       | Metadata filter (inline JSON, `./path.json`, or `-` for stdin)           |
    | `--limit`            | `-l`       | Maximum number of vectors to fetch                                       |
    | `--pagination-token` | `-p`       | Pagination token for next page                                           |
    | `--body`             |            | Request body JSON (inline, `./path.json`, or `-` for stdin)              |
    | `--json`             | `-j`       | Output in JSON format                                                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Fetch specific vectors by ID
    pc index vector fetch -i my-index --ids '["123","456","789"]'

    # Fetch from a file
    pc index vector fetch -i my-index --ids ./ids.json

    # Fetch by metadata filter
    pc index vector fetch -i my-index --filter '{"genre":{"$eq":"rock"}}'

    # Fetch from a namespace
    pc index vector fetch -i my-index --namespace tenant-a --ids '["doc-123"]'

    # JSON output
    pc index vector fetch -i my-index --ids '["vec1"]' -j
    ```

    <Note>
      Use either `--ids` or `--filter`, not both. When using `--ids`, pagination flags are not applicable.
    </Note>
  </Accordion>

  <Accordion title="pc index vector list (List vector IDs)">
    **Description**

    Lists vector IDs in a namespace with optional pagination.

    **Usage**

    ```bash theme={null}
    pc index vector list [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                     |
    | :------------------- | :--------- | :---------------------------------------------- |
    | `--index-name`       | `-i`       | Index name (required)                           |
    | `--namespace`        |            | Namespace to list from (default: `__default__`) |
    | `--limit`            | `-l`       | Maximum number of IDs to return                 |
    | `--pagination-token` | `-p`       | Pagination token for next page                  |
    | `--json`             | `-j`       | Output in JSON format                           |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List vector IDs
    pc index vector list -i my-index

    # List from a namespace with limit
    pc index vector list -i my-index --namespace tenant-a --limit 50

    # JSON output
    pc index vector list -i my-index -j
    ```
  </Accordion>

  <Accordion title="pc index vector query (Query vectors)">
    **Description**

    Queries an index for similar vectors using dense vectors, sparse vectors, or vector ID.

    **Usage**

    ```bash theme={null}
    pc index vector query [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                                                       |
    | :------------------- | :--------- | :-------------------------------------------------------------------------------- |
    | `--index-name`       | `-i`       | Index name (required)                                                             |
    | `--namespace`        |            | Namespace to query (default: `__default__`)                                       |
    | `--id`               |            | Query by vector ID                                                                |
    | `--vector`           | `-v`       | Query vector values (inline JSON array, `./path.json`, or `-` for stdin)          |
    | `--sparse-indices`   |            | Sparse vector indices (inline JSON uint32 array, `./path.json`, or `-` for stdin) |
    | `--sparse-values`    |            | Sparse vector values (inline JSON array, `./path.json`, or `-` for stdin)         |
    | `--top-k`            | `-k`       | Number of results to return (default: 10)                                         |
    | `--filter`           | `-f`       | Metadata filter (inline JSON, `./path.json`, or `-` for stdin)                    |
    | `--include-values`   |            | Include vector values in results                                                  |
    | `--include-metadata` |            | Include metadata in results                                                       |
    | `--body`             |            | Request body JSON (inline, `./path.json`, or `-` for stdin)                       |
    | `--json`             | `-j`       | Output in JSON format                                                             |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Query by vector ID
    pc index vector query -i my-index --id "doc-123" -k 10 --include-metadata

    # Query by vector values
    pc index vector query -i my-index --vector '[0.1, 0.2, 0.3]' -k 25

    # Query with metadata filter
    pc index vector query -i my-index \
      --vector '[0.1, 0.2, 0.3]' \
      --filter '{"genre":{"$eq":"sci-fi"}}' \
      --include-metadata

    # Query from file (file contains a JSON array that specifies the query vector)
    pc index vector query -i my-index --vector ./embedding.json -k 20

    # Query with sparse vectors (inline)
    pc index vector query -i my-index \
      --sparse-indices '[0, 5, 12]' \
      --sparse-values '[0.5, 0.3, 0.8]' \
      -k 15

    # Query with sparse vectors from files
    # indices.json: [0, 5, 12]
    # values.json: [0.5, 0.3, 0.8]
    pc index vector query -i my-index \
      --sparse-indices ./indices.json \
      --sparse-values ./values.json \
      -k 15

    # Query from stdin (extract embedding from a document)
    # doc.json: {"id": "doc-123", "embedding": [0.1, 0.2, 0.3], "text": "..."}
    jq -c '.embedding' doc.json | pc index vector query -i my-index --vector - -k 10
    ```

    <Note>
      Use `--id`, `--vector`, or sparse vectors (`--sparse-indices` and `--sparse-values`) to specify what to query against. These options are mutually exclusive.
    </Note>
  </Accordion>

  <Accordion title="pc index vector update (Update vectors)">
    **Description**

    Updates a vector's values, sparse values, or metadata by ID, or updates metadata for multiple vectors matching a filter.

    **Usage**

    ```bash theme={null}
    pc index vector update [flags]
    ```

    **Flags**

    | Long flag          | Short flag | Description                                                                    |
    | :----------------- | :--------- | :----------------------------------------------------------------------------- |
    | `--index-name`     | `-i`       | Index name (required)                                                          |
    | `--namespace`      |            | Namespace containing the vector (default: `__default__`)                       |
    | `--id`             |            | Vector ID to update                                                            |
    | `--values`         |            | New vector values (inline JSON array, `./path.json`, or `-` for stdin)         |
    | `--sparse-indices` |            | New sparse indices (inline JSON uint32 array, `./path.json`, or `-` for stdin) |
    | `--sparse-values`  |            | New sparse values (inline JSON array, `./path.json`, or `-` for stdin)         |
    | `--metadata`       |            | New or updated metadata (inline JSON, `./path.json`, or `-` for stdin)         |
    | `--filter`         |            | Metadata filter for bulk update (inline JSON, `./path.json`, or `-` for stdin) |
    | `--dry-run`        |            | Preview how many records would be updated without applying changes             |
    | `--body`           |            | Request body JSON (inline, `./path.json`, or `-` for stdin)                    |
    | `--json`           | `-j`       | Output in JSON format                                                          |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Update metadata for a single vector
    pc index vector update -i my-index --id "vec1" --metadata '{"category":"updated"}'

    # Update values for a single vector
    pc index vector update -i my-index --id "vec1" --values '[0.2, 0.3, 0.4]'

    # Update sparse values
    # indices.json: [0, 5, 12]
    # values.json: [0.5, 0.3, 0.8]
    pc index vector update -i my-index --id "vec1" \
      --sparse-indices ./indices.json \
      --sparse-values ./values.json

    # Bulk update metadata by filter (preview first)
    pc index vector update -i my-index \
      --filter '{"genre":{"$eq":"sci-fi"}}' \
      --metadata '{"genre":"fantasy"}' \
      --dry-run

    # Apply the bulk update
    pc index vector update -i my-index \
      --filter '{"genre":{"$eq":"sci-fi"}}' \
      --metadata '{"genre":"fantasy"}'
    ```

    <Note>
      Use either `--id` for single vector updates or `--filter` for bulk updates. These options are mutually exclusive.
    </Note>
  </Accordion>

  <Accordion title="pc index vector upsert (Upsert vectors)">
    **Description**

    Inserts or updates vectors in an index from a JSON or JSONL file, or inline JSON. The CLI automatically batches vectors for efficient uploading. Files can contain any number of vectors—the CLI splits them into batches and sends multiple API requests as needed.

    **Usage**

    ```bash theme={null}
    pc index vector upsert [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                                                        |
    | :------------- | :--------- | :--------------------------------------------------------------------------------- |
    | `--index-name` | `-i`       | Index name (required)                                                              |
    | `--namespace`  |            | Namespace to upsert into (default: `__default__`)                                  |
    | `--body`       |            | Request body JSON or JSONL (inline, `./path.json[l]`, or `-` for stdin) (required) |
    | `--batch-size` | `-b`       | Size of batches to upsert (default: 500)                                           |
    | `--json`       | `-j`       | Output in JSON format                                                              |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Upsert from JSON file (with "vectors" array)
    # vectors.json: {"vectors": [{"id": "vec1", "values": [0.1, 0.2, 0.3], "metadata": {"genre": "comedy"}}]}
    pc index vector upsert -i my-index --body ./vectors.json

    # Upsert with inline JSON
    pc index vector upsert -i my-index --body '{"vectors": [{"id": "vec1", "values": [0.1, 0.2, 0.3], "metadata": {"genre": "comedy"}}]}'

    # Upsert from JSONL file (one vector per line)
    # vectors.jsonl: {"id": "vec1", "values": [0.1, 0.2, 0.3]}
    #                {"id": "vec2", "values": [0.4, 0.5, 0.6]}
    pc index vector upsert -i my-index --body ./vectors.jsonl

    # Upsert from stdin (same format as JSON or JSONL file)
    cat vectors.json | pc index vector upsert -i my-index --body -

    # Custom batch size (default: 500, max: 1000 per API request)
    pc index vector upsert -i my-index --body ./vectors.json --batch-size 1000
    ```

    <Note>
      **Batch size limits:** The API accepts up to 1000 vectors per request. The CLI defaults to batches of 500 vectors, but you can adjust this with `--batch-size` (up to 1000). Large files are automatically split into multiple batches.

      **File size:** There's no explicit file size limit—the CLI reads the entire file into memory and batches it automatically. Very large files are supported as long as they fit in available system memory.
    </Note>
  </Accordion>
</AccordionGroup>

### Records

<AccordionGroup>
  <Accordion title="pc index record search (Search records in an index)">
    **Description**

    Search an index namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query.

    Searching with text is supported only for indexes with an integrated embedding configured. Searching with a query vector or record ID is supported for all indexes.

    Exactly one primary query mode must be provided:

    * `--inputs` — query text (requires an index with integrated embedding)
    * `--id` — use an existing record's vector as the query
    * `--vector` — provide a dense vector directly (all index types)
    * `--sparse-indices` + `--sparse-values` — sparse vector (all index types)

    Combine `--vector` with `--sparse-indices`/`--sparse-values` for hybrid search. Use `--body` to pass a full request object; flags take precedence over `--body` when both specify the same field.

    **Usage**

    ```bash theme={null}
    pc index record search [flags]
    ```

    **Flags**

    | Long flag          | Short flag | Description                                                                                                                                                     |
    | :----------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `--index-name`     | `-i`       | Name of the index to search (required)                                                                                                                          |
    | `--inputs`         |            | Query inputs for text search (inline JSON, `./path.json`, or `-` for stdin); requires integrated embedding. Mutually exclusive with `--id` and `--vector`.      |
    | `--id`             |            | Use an existing record's vector by ID for the query. Mutually exclusive with `--inputs` and `--vector`.                                                         |
    | `--vector`         | `-v`       | Dense vector values to search against (inline JSON float32 array, `./path.json`, or `-` for stdin). Mutually exclusive with `--inputs` and `--id`.              |
    | `--sparse-indices` |            | Sparse vector indices (inline JSON int32 array, `./path.json`, or `-` for stdin). Must be used together with `--sparse-values`.                                 |
    | `--sparse-values`  |            | Sparse vector values (inline JSON float32 array, `./path.json`, or `-` for stdin). Must be used together with `--sparse-indices`.                               |
    | `--top-k`          | `-k`       | Number of results to return (required)                                                                                                                          |
    | `--namespace`      |            | Namespace to search                                                                                                                                             |
    | `--filter`         |            | Metadata filter (inline JSON, `./path.json`, or `-` for stdin)                                                                                                  |
    | `--rerank`         |            | Re-score results using an inference model (inline JSON, `./path.json`, or `-` for stdin). Required fields: `model` (string), `rank_fields` (string array).      |
    | `--match-terms`    |            | Keyword terms filter for sparse integrated indexes (inline JSON, `./path.json`, or `-` for stdin). Required field: `terms` (string array). Requires `--inputs`. |
    | `--fields`         |            | Fields to return in results (inline JSON string array, `./path.json`, or `-` for stdin)                                                                         |
    | `--body`           |            | Full request body JSON (inline, `./path.json`, or `-` for stdin). Flags take precedence when both specify the same field.                                       |
    | `--json`           | `-j`       | Output in JSON format                                                                                                                                           |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Examples**

    ```bash theme={null}
    # Text search (integrated embedding indexes only)
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --top-k 10
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --namespace my-namespace --top-k 5
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --filter '{"category":"health"}' --top-k 10
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --fields '["_id","chunk_text","category"]' --top-k 10
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --rerank '{"model":"bge-reranker-v2-m3","rank_fields":["chunk_text"]}' --top-k 10
    pc index record search --index-name my-index --inputs '{"text":"disease prevention"}' --match-terms '{"terms":["vaccine","prevention"]}' --top-k 10

    # Search by record ID for query vector (all index types)
    pc index record search --index-name my-index --id rec-123 --top-k 10

    # Vector search (all index types)
    pc index record search --index-name my-index --vector '[0.1,0.2,0.3]' --top-k 10
    pc index record search --index-name my-index --sparse-indices '[1,5,9]' --sparse-values '[0.4,0.8,0.2]' --top-k 10
    pc index record search --index-name my-index --vector '[0.1,0.2,0.3]' --sparse-indices '[1,5,9]' --sparse-values '[0.4,0.8,0.2]' --top-k 10

    # Full request body (must include top_k in the body)
    pc index record search --index-name my-index --body ./search.json
    ```

    ```text CLI theme={null}
    Usage: 5 (read units)
    ID          SCORE       FIELDS
    rec-001     0.912340    {"category":"health","chunk_text":"vaccine research..."}
    rec-002     0.887210    {"category":"health","chunk_text":"disease prevention..."}
    ```
  </Accordion>

  <Accordion title="pc index record upsert (Upsert records into an integrated index)">
    **Description**

    Upsert records into an integrated index namespace from a JSON or JSONL payload.

    The `--body` flag accepts a JSON object containing a `"records"` array of `IntegratedRecord` objects, a raw JSON array of records, or a JSONL stream of records (one object per line). The value can be inline JSON, a path to a `.json` or `.jsonl` file, or `-` to read from stdin.

    Records are sent in batches. The default batch size is 96 (the API maximum). Use `--batch-size` to send smaller batches.

    **Usage**

    ```bash theme={null}
    pc index record upsert [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                                                             |
    | :------------- | :--------- | :-------------------------------------------------------------------------------------- |
    | `--index-name` | `-i`       | Name of the index to upsert into (required)                                             |
    | `--body`       |            | Request body JSON or JSONL (inline JSON, `./path.json[l]`, or `-` for stdin) (required) |
    | `--namespace`  |            | Namespace to upsert into                                                                |
    | `--batch-size` | `-b`       | Number of records per batch (default: `96`, max: `96`)                                  |
    | `--json`       | `-j`       | Output in JSON format                                                                   |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Examples**

    ```bash theme={null}
    # Upsert from a JSON file
    pc index record upsert --index-name my-index --body ./records.json

    # Upsert from a JSONL file into a specific namespace
    pc index record upsert --index-name my-index --namespace my-namespace --body ./records.jsonl

    # Upsert from stdin
    cat records.jsonl | pc index record upsert --index-name my-index --namespace my-namespace --body -
    ```
  </Accordion>
</AccordionGroup>

### Collections

<AccordionGroup>
  <Accordion title="pc index collection create (Create a collection from a pod-based index)">
    **Description**

    Creates a static copy of a pod-based index as a collection. Collections can be used to store a snapshot of an index's data for backup or migration purposes.

    **Usage**

    ```bash theme={null}
    pc index collection create [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                                 |
    | :--------- | :--------- | :---------------------------------------------------------- |
    | `--name`   | `-n`       | Name to give the collection (required)                      |
    | `--source` | `-s`       | Name of the pod-based index to use as the source (required) |
    | `--json`   | `-j`       | Output in JSON format                                       |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Create a collection from a pod-based index
    pc index collection create --name my-collection --source my-index
    ```

    ```text CLI theme={null}
    ATTRIBUTE     VALUE
    Name          my-collection
    State         Initializing
    Dimension     1536
    Size          0
    VectorCount   0
    Environment   us-east-1-aws
    ```
  </Accordion>

  <Accordion title="pc index collection delete (Delete a collection)">
    **Description**

    Deletes a collection permanently. This action cannot be undone.

    **Usage**

    ```bash theme={null}
    pc index collection delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                |
    | :-------------------- | :--------- | :--------------------------------------------------------- |
    | `--name`              | `-n`       | Name of the collection to delete (required)                |
    | `--skip-confirmation` |            | Skip the deletion confirmation prompt                      |
    | `--json`              | `-j`       | Output in JSON format (also skips the confirmation prompt) |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete a collection (prompts for confirmation)
    pc index collection delete --name my-collection

    # Skip the confirmation prompt
    pc index collection delete --name my-collection --skip-confirmation
    ```

    <Note>
      This command prompts for confirmation before deleting. Pass `--skip-confirmation` (or `--json`) to bypass the prompt in non-interactive contexts.
    </Note>
  </Accordion>

  <Accordion title="pc index collection describe (Describe a collection by name)">
    **Description**

    Returns detailed information about a single collection, including its state, dimension, size, vector count, and environment.

    **Usage**

    ```bash theme={null}
    pc index collection describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                   |
    | :-------- | :--------- | :-------------------------------------------- |
    | `--name`  | `-n`       | Name of the collection to describe (required) |
    | `--json`  | `-j`       | Output in JSON format                         |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe a collection
    pc index collection describe --name my-collection
    ```

    ```text CLI theme={null}
    ATTRIBUTE     VALUE
    Name          my-collection
    State         Ready
    Dimension     1536
    Size          104857600
    VectorCount   10000
    Environment   us-east-1-aws
    ```
  </Accordion>

  <Accordion title="pc index collection list (List collections in your project)">
    **Description**

    Lists all collections in your current project, sorted alphabetically by name.

    **Usage**

    ```bash theme={null}
    pc index collection list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all collections
    pc index collection list
    ```

    ```text CLI theme={null}
    NAME             DIMENSION   SIZE        STATUS   VECTORS   ENVIRONMENT
    my-collection    1536        104857600   Ready    10000     us-east-1-aws
    ```
  </Accordion>
</AccordionGroup>

### Backups

<AccordionGroup>
  <Accordion title="pc index backup create (Create a backup)">
    **Description**

    Creates a backup of a serverless index. Backups are static copies that only consume storage.

    **Usage**

    ```bash theme={null}
    pc index backup create [flags]
    ```

    **Flags**

    | Long flag       | Short flag | Description                                                          |
    | :-------------- | :--------- | :------------------------------------------------------------------- |
    | `--index-name`  | `-i`       | Name of the index to back up (required)                              |
    | `--name`        |            | Human-readable label for the backup (the backup ID is always a UUID) |
    | `--description` | `-d`       | Description for the backup                                           |
    | `--json`        | `-j`       | Output in JSON format                                                |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Create a backup
    pc index backup create -i my-index

    # Create with name and description
    pc index backup create -i my-index --name "nightly-backup" -d "Nightly backup before deployment"

    # JSON output
    pc index backup create -i my-index -j
    ```
  </Accordion>

  <Accordion title="pc index backup delete (Delete a backup)">
    **Description**

    Permanently deletes a backup. This operation cannot be undone.

    **Usage**

    ```bash theme={null}
    pc index backup delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                |
    | :-------------------- | :--------- | :--------------------------------------------------------- |
    | `--id`                | `-i`       | Backup ID to delete (required)                             |
    | `--skip-confirmation` |            | Skip the deletion confirmation prompt                      |
    | `--json`              | `-j`       | Output in JSON format (also skips the confirmation prompt) |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete a backup by ID (prompts for confirmation)
    pc index backup delete -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f

    # Skip the confirmation prompt
    pc index backup delete -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f --skip-confirmation
    ```

    <Note>
      This command prompts for confirmation before deleting. Pass `--skip-confirmation` (or `--json`) to bypass the prompt in non-interactive contexts.
    </Note>

    <Warning>
      Backup deletion is permanent and cannot be undone.
    </Warning>
  </Accordion>

  <Accordion title="pc index backup describe (Show backup details)">
    **Description**

    Displays detailed information about a specific backup.

    **Usage**

    ```bash theme={null}
    pc index backup describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                      |
    | :-------- | :--------- | :------------------------------- |
    | `--id`    | `-i`       | Backup ID to describe (required) |
    | `--json`  | `-j`       | Output in JSON format            |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe a backup
    pc index backup describe -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f

    # JSON output
    pc index backup describe -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f -j
    ```
  </Accordion>

  <Accordion title="pc index backup list (List backups)">
    **Description**

    Lists backups in the current project, optionally filtered by index name.

    **Usage**

    ```bash theme={null}
    pc index backup list [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                    |
    | :------------------- | :--------- | :----------------------------- |
    | `--index-name`       | `-i`       | Filter backups by index name   |
    | `--limit`            | `-l`       | Maximum number of results      |
    | `--pagination-token` | `-p`       | Pagination token for next page |
    | `--json`             | `-j`       | Output in JSON format          |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all backups in the project
    pc index backup list

    # List backups for a specific index
    pc index backup list --index-name my-index

    # Limit results
    pc index backup list --limit 10

    # JSON output
    pc index backup list -j
    ```
  </Accordion>

  <Accordion title="pc index restore (Restore an index from a backup)">
    **Description**

    Creates a new index from a backup.

    **Usage**

    ```bash theme={null}
    pc index restore [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                          |
    | :---------------------- | :--------- | :--------------------------------------------------- |
    | `--id`                  | `-i`       | Backup ID (UUID) to restore from (required)          |
    | `--name`                | `-n`       | Name for the new index (required)                    |
    | `--deletion-protection` |            | Enable deletion protection - `enabled` or `disabled` |
    | `--tags`                | `-t`       | Tags to apply to the new index (key=value pairs)     |
    | `--json`                | `-j`       | Output in JSON format                                |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Restore an index from a backup
    pc index restore -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f -n restored-index

    # Restore with tags and deletion protection
    pc index restore -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f -n restored-index \
      --tags env=prod,team=search \
      --deletion-protection enabled

    # JSON output
    pc index restore -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f -n restored-index -j
    ```
  </Accordion>

  <Accordion title="pc index restore describe (Show restore job details)">
    **Description**

    Displays the status and details of a restore job.

    **Usage**

    ```bash theme={null}
    pc index restore describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                           |
    | :-------- | :--------- | :------------------------------------ |
    | `--id`    | `-i`       | Restore job ID to describe (required) |
    | `--json`  | `-j`       | Output in JSON format                 |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe a restore job
    pc index restore describe -i rj-abc123

    # JSON output
    pc index restore describe -i rj-abc123 -j
    ```
  </Accordion>

  <Accordion title="pc index restore list (List restore jobs)">
    **Description**

    Lists all restore jobs in the current project.

    **Usage**

    ```bash theme={null}
    pc index restore list [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                    |
    | :------------------- | :--------- | :----------------------------- |
    | `--limit`            | `-l`       | Maximum number of results      |
    | `--pagination-token` | `-p`       | Pagination token for next page |
    | `--json`             | `-j`       | Output in JSON format          |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List restore jobs
    pc index restore list

    # Limit results
    pc index restore list --limit 10

    # JSON output
    pc index restore list -j
    ```
  </Accordion>
</AccordionGroup>

### Imports

<AccordionGroup>
  <Accordion title="pc index import start (Start an import from a storage URI)">
    **Description**

    Start an import that loads vector data from a storage provider into a serverless index. The URI must begin with the scheme of a supported provider (for example, `s3://`).

    For private buckets, configure a storage integration in the Pinecone console and pass the integration ID with `--integration-id`.

    Use `--error-mode` to control behavior when records fail: `continue` skips failing records and keeps going; `abort` stops the import on first error. Defaults to `continue`.

    **Usage**

    ```bash theme={null}
    pc index import start [flags]
    ```

    **Flags**

    | Long flag          | Short flag | Description                                                           |
    | :----------------- | :--------- | :-------------------------------------------------------------------- |
    | `--index-name`     | `-i`       | Name of the index to import into (required)                           |
    | `--uri`            | `-u`       | URI of the data to import, for example `s3://bucket/path/` (required) |
    | `--integration-id` |            | Storage integration ID for private buckets                            |
    | `--error-mode`     |            | How to handle record errors: `continue` (default) or `abort`          |
    | `--json`           | `-j`       | Output in JSON format                                                 |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Examples**

    ```bash theme={null}
    # Start an import from a public S3 bucket
    pc index import start --index-name my-index --uri s3://my-bucket/data/

    # Start an import from a private bucket using a storage integration
    pc index import start --index-name my-index --uri s3://my-bucket/data/ --integration-id intg-123

    # Abort on the first error instead of continuing
    pc index import start --index-name my-index --uri s3://my-bucket/data/ --error-mode abort

    # JSON output
    pc index import start --index-name my-index --uri s3://my-bucket/data/ -j
    ```

    ```text CLI theme={null}
    Import imp-abc123 started.
    ATTRIBUTE    VALUE
    Import ID    imp-abc123
    ```
  </Accordion>

  <Accordion title="pc index import describe (Describe an import operation)">
    **Description**

    Show the current status and details of an import operation, including
    percent complete, records imported, and any error messages.

    **Usage**

    ```bash theme={null}
    pc index import describe [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                        |
    | :------------- | :--------- | :------------------------------------------------- |
    | `--index-name` | `-i`       | Name of the index the import belongs to (required) |
    | `--id`         |            | ID of the import to describe (required)            |
    | `--json`       | `-j`       | Output in JSON format                              |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe an import operation
    pc index import describe --index-name my-index --id import-123

    # JSON output
    pc index import describe --index-name my-index --id import-123 -j
    ```

    ```text CLI theme={null}
    ATTRIBUTE         VALUE
    Import ID         import-123
    Status            InProgress
    URI               s3://my-bucket/data/
    Percent Complete  45.0%
    Records Imported  450
    Created At        2024-01-15 12:00:00
    Finished At       -
    Error             None
    ```
  </Accordion>

  <Accordion title="pc index import list (List import operations for an index)">
    **Description**

    List bulk import operations for the given index, with optional pagination.

    **Usage**

    ```bash theme={null}
    pc index import list [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                               |
    | :------------------- | :--------- | :-------------------------------------------------------- |
    | `--index-name`       | `-i`       | Name of the index to list imports for (required)          |
    | `--limit`            | `-l`       | Maximum number of imports to return                       |
    | `--pagination-token` | `-p`       | Pagination token to continue a previous listing operation |
    | `--json`             | `-j`       | Output in JSON format                                     |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Examples**

    ```bash theme={null}
    # List all imports for an index
    pc index import list --index-name my-index

    # List imports with a page size limit
    pc index import list --index-name my-index --limit 10

    # Continue paginating from a previous call
    pc index import list --index-name my-index --pagination-token eyJ...

    # JSON output
    pc index import list --index-name my-index -j
    ```

    ```text CLI theme={null}
    IMPORT ID     STATUS      URI                     PERCENT  RECORDS  CREATED              FINISHED
    imp-abc123    Completed   s3://my-bucket/data/    100.0%   1000     2024-01-15 12:00:00  2024-01-15 12:05:00
    imp-def456    InProgress  s3://other-bucket/data/ 45.0%    450      2024-01-15 13:00:00  -
    ```
  </Accordion>

  <Accordion title="pc index import cancel (Cancel an in-progress import operation)">
    **Description**

    Cancel an import operation that is currently pending or in progress.
    Already-completed or failed imports cannot be canceled.

    **Usage**

    ```bash theme={null}
    pc index import cancel [flags]
    ```

    **Flags**

    | Long flag      | Short flag | Description                                        |
    | :------------- | :--------- | :------------------------------------------------- |
    | `--index-name` | `-i`       | Name of the index the import belongs to (required) |
    | `--id`         |            | ID of the import to cancel (required)              |
    | `--json`       | `-j`       | Output in JSON format                              |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Cancel an import operation
    pc index import cancel --index-name my-index --id import-123

    # JSON output
    pc index import cancel --index-name my-index --id import-123 -j
    ```

    ```text CLI theme={null}
    Import import-123 canceled.
    ```
  </Accordion>
</AccordionGroup>

### Projects

<AccordionGroup>
  <Accordion title="pc project create (Create a new project)">
    **Description**

    Creates a new project in your [target organization](/reference/cli/target-context), using the specified configuration.

    **Usage**

    ```bash theme={null}
    pc project create [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                                    |
    | :------------------- | :--------- | :------------------------------------------------------------- |
    | `--force-encryption` |            | Enable encryption with CMEK                                    |
    | `--json`             | `-j`       | Output in JSON format                                          |
    | `--name`             | `-n`       | Project name (required)                                        |
    | `--target`           |            | Automatically target the project in the CLI after it's created |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Basic project creation
    pc project create -n "demo-project"
    ```
  </Accordion>

  <Accordion title="pc project delete (Delete a project)">
    **Description**

    Permanently deletes a project and all its resources. This operation cannot be undone.

    **Usage**

    ```bash theme={null}
    pc project delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--id`                | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`              | `-j`       | Output in JSON format                                       |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete target project
    pc project delete

    # Delete specific project
    pc project delete -i proj-abc123

    # Skip confirmation
    pc project delete -i proj-abc123 --skip-confirmation
    ```

    <Note>
      Must delete all indexes and collections in the project first. If the deleted project is your current target, set a new target after deleting it.
    </Note>
  </Accordion>

  <Accordion title="pc project describe (Show project details)">
    **Description**

    Displays detailed information about a specific project, including various details.

    **Usage**

    ```bash theme={null}
    pc project describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | Project ID (required) |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe a project
    pc project describe -i proj-abc123

    # JSON output
    pc project describe -i proj-abc123 --json

    # Find ID and describe
    pc project list
    pc project describe -i proj-abc123
    ```
  </Accordion>

  <Accordion title="pc project list (List all projects)">
    **Description**

    Displays all projects in your [target organization](/reference/cli/target-context), including various details.

    **Usage**

    ```bash theme={null}
    pc project list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all projects
    pc project list

    # JSON output
    pc project list --json

    # List after login
    pc auth login
    pc auth target -o "my-org"
    pc project list
    ```
  </Accordion>

  <Accordion title="pc project update (Update project settings)">
    **Description**

    Modifies the configuration of the [target project](/reference/cli/target-context), or a specific project ID.

    **Usage**

    ```bash theme={null}
    pc project update [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                         |
    | :------------------- | :--------- | :---------------------------------- |
    | `--force-encryption` | `-f`       | Enable/disable encryption with CMEK |
    | `--id`               | `-i`       | Project ID (required)               |
    | `--json`             | `-j`       | Output in JSON format               |
    | `--name`             | `-n`       | New project name                    |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Update name
    pc project update -i proj-abc123 -n "new-name"
    ```
  </Accordion>
</AccordionGroup>

### Organizations

<AccordionGroup>
  <Accordion title="pc organization delete (Delete an organization)">
    **Description**

    Permanently deletes an organization and all its resources. This operation cannot be undone.

    **Usage**

    ```bash theme={null}
    pc organization delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                |
    | :-------------------- | :--------- | :------------------------- |
    | `--id`                | `-i`       | Organization ID (required) |
    | `--json`              | `-j`       | Output in JSON format      |
    | `--skip-confirmation` |            | Skip confirmation prompt   |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete an organization
    pc organization delete -i org-abc123

    # Skip confirmation
    pc organization delete -i org-abc123 --skip-confirmation
    ```

    <Note>
      This is a highly destructive action. Deletion is permanent. If the deleted organization is your current [target](/reference/cli/target-context), set a new target after deleting.
    </Note>
  </Accordion>

  <Accordion title="pc organization describe (Show organization details)">
    **Description**

    Displays detailed information about a specific organization, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash theme={null}
    pc organization describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  | `-j`       | Output in JSON format      |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe an organization
    pc organization describe -i org-abc123

    # JSON output
    pc organization describe -i org-abc123 --json

    # Find ID and describe
    pc organization list
    pc organization describe -i org-abc123
    ```
  </Accordion>

  <Accordion title="pc organization list (List organizations)">
    **Description**

    Displays all organizations that the authenticated user has access to, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash theme={null}
    pc organization list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List all organizations
    pc organization list

    # JSON output
    pc organization list --json

    # List after login
    pc auth login
    pc organization list
    ```
  </Accordion>

  <Accordion title="pc organization update (Update organization settings)">
    **Description**

    Modifies the configuration of the [target organization](/reference/cli/target-context), or a specific organization ID.

    **Usage**

    ```bash theme={null}
    pc organization update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  | `-j`       | Output in JSON format      |
    | `--name`  | `-n`       | New organization name      |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Update name
    pc organization update -i org-abc123 -n "new-name"

    # Verify changes
    pc organization update -i org-abc123 -n "Acme Corp"
    pc organization describe -i org-abc123
    ```
  </Accordion>
</AccordionGroup>

### API keys

<AccordionGroup>
  <Accordion title="pc api-key create (Create a new API key)">
    **Description**

    Creates a new API key for the current [target project](/reference/cli/target-context) or a specific project ID. Optionally stores the key locally for CLI use.

    **Usage**

    ```bash theme={null}
    pc api-key create [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                                             |
    | :-------- | :--------- | :-------------------------------------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified)                             |
    | `--json`  | `-j`       | Output in JSON format                                                                   |
    | `--name`  | `-n`       | Key name (required)                                                                     |
    | `--roles` |            | Roles to assign (default: `ProjectEditor`)                                              |
    | `--store` |            | Store the key locally for CLI use (automatically replaces any existing CLI-managed key) |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Basic key creation
    pc api-key create -n "my-key"

    # Create and store locally
    pc api-key create -n "my-key" --store

    # Create with specific role
    pc api-key create -n "my-key" --store --roles ProjectEditor

    # Create for specific project
    pc api-key create -n "my-key" -i proj-abc123
    ```

    <Note>
      API keys are scoped to a specific organization and project.
    </Note>
  </Accordion>

  <Accordion title="pc api-key delete (Delete an API key)">
    **Description**

    Permanently deletes an API key. Applications using this key immediately lose access.

    **Usage**

    ```bash theme={null}
    pc api-key delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description              |
    | :-------------------- | :--------- | :----------------------- |
    | `--id`                | `-i`       | API key ID (required)    |
    | `--skip-confirmation` |            | Skip confirmation prompt |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Delete an API key
    pc api-key delete -i key-abc123

    # Skip confirmation
    pc api-key delete -i key-abc123 --skip-confirmation

    # Delete and clean up local storage
    pc api-key delete -i key-abc123
    pc auth local-keys prune --skip-confirmation
    ```

    <Note>
      Deletion is permanent. Applications using this key immediately lose access to Pinecone.
    </Note>
  </Accordion>

  <Accordion title="pc api-key describe (Show API key details)">
    **Description**

    Displays detailed information about a specific API key, including its name, ID, project ID, and roles.

    **Usage**

    ```bash theme={null}
    pc api-key describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Describe an API key
    pc api-key describe -i key-abc123

    # JSON output
    pc api-key describe -i key-abc123 --json

    # Find ID and describe
    pc api-key list
    pc api-key describe -i key-abc123
    ```

    <Note>
      Does not display the actual key value.
    </Note>
  </Accordion>

  <Accordion title="pc api-key list (List all API keys)">
    **Description**

    Displays a list of all of the [target project's](/reference/cli/target-context) API keys, as found in  Pinecone (regardless of whether they are stored locally by the CLI). Displays various details about each key, including name, ID, project ID, and roles.

    **Usage**

    ```bash theme={null}
    pc api-key list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                 |
    | :-------- | :--------- | :---------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`  | `-j`       | Output in JSON format                                       |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # List keys for target project
    pc api-key list

    # List for specific project
    pc api-key list -i proj-abc123

    # JSON output
    pc api-key list --json
    ```

    <Note>
      Does not display key values.
    </Note>
  </Accordion>

  <Accordion title="pc api-key update (Update API key settings)">
    **Description**

    Updates the name and roles of an API key.

    **Usage**

    ```bash theme={null}
    pc api-key update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  | `-j`       | Output in JSON format |
    | `--name`  | `-n`       | New key name          |
    | `--roles` | `-r`       | Roles to assign       |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    # Update name
    pc api-key update -i key-abc123 -n "new-name"

    # Update roles
    pc api-key update -i key-abc123 -r ProjectEditor

    # Verify changes
    pc api-key update -i key-abc123 -n "production-key"
    pc api-key describe -i key-abc123
    ```

    <Note>
      Cannot change the actual key. If you need a different key, create a new one.
    </Note>
  </Accordion>
</AccordionGroup>

### Config

<AccordionGroup>
  <Accordion title="pc config list (List all configuration settings and their current values)">
    **Description**

    Lists all CLI configuration settings and their current values. Sensitive values like `api-key` are masked by default; use `--reveal` to see the full value. Hidden settings such as `environment` are included when `--all` is passed.

    **Usage**

    ```bash theme={null}
    pc config list [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                               |
    | :--------- | :--------- | :-------------------------------------------------------- |
    | `--reveal` |            | Reveal the full value for sensitive settings like api-key |
    | `--json`   | `-j`       | Output in JSON format                                     |
    | `--all`    |            | Include hidden settings such as environment               |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc config list
    pc config list --all
    pc config list --reveal
    pc config list --json
    ```

    ```text CLI theme={null}
    KEY         VALUE             ENV VAR NAME        ENV VAR OVERRIDE  DESCRIPTION
    api-key     ****abcd****      PINECONE_API_KEY     false             Default API key for authenticating with Pinecone
    color       true                                                     Enable colored output
    ```
  </Accordion>

  <Accordion title="pc config get <key> (Get the current value of a configuration setting)">
    **Description**

    Gets the current value of a configuration setting. Valid keys are: `api-key`, `color`, `environment`. Sensitive values like `api-key` are masked by default; use `--reveal` to see the full value.

    **Usage**

    ```bash theme={null}
    pc config get <key> [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                               |
    | :--------- | :--------- | :-------------------------------------------------------- |
    | `--reveal` |            | Reveal the full value for sensitive settings like api-key |
    | `--json`   | `-j`       | Output in JSON format                                     |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc config get api-key
    pc config get api-key --reveal
    pc config get environment
    pc config get color
    ```
  </Accordion>

  <Accordion title="pc config describe <key> (Show detailed information about a configuration setting)">
    **Description**

    Displays detailed information about a specific CLI configuration setting, including its current value, whether an environment variable is overriding it, and valid values. Valid keys are: `api-key`, `color`, `environment`.

    **Usage**

    ```bash theme={null}
    pc config describe <key> [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                               |
    | :--------- | :--------- | :-------------------------------------------------------- |
    | `--reveal` |            | Reveal the full value for sensitive settings like api-key |
    | `--json`   | `-j`       | Output in JSON format                                     |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc config describe api-key
    pc config describe color
    pc config describe color --json
    ```

    ```text CLI theme={null}
    KEY               api-key
    VALUE             ****abcd****
    ENV VAR NAME      $PINECONE_API_KEY
    ENV VAR OVERRIDE  false
    SENSITIVE         true
    DESCRIPTION       Default API key for authenticating with Pinecone
    ```
  </Accordion>

  <Accordion title="pc config set <key> <value> (Set a configuration value)">
    **Description**

    Sets a CLI configuration value. Valid keys are: `api-key`, `color`, `environment`. The value is persisted to the local config file.

    **Usage**

    ```bash theme={null}
    pc config set <key> <value> [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc config set api-key pcsk_...
    pc config set environment staging
    pc config set color false
    ```
  </Accordion>

  <Accordion title="pc config unset <key> (Reset a configuration value to its default)">
    **Description**

    Resets a CLI configuration value to its default. Valid keys are: `api-key`, `color`, `environment`.

    **Usage**

    ```bash theme={null}
    pc config unset <key> [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  | `-j`       | Output in JSON format |

    **Global Flags**

    | Long flag   | Short flag | Description                         |
    | :---------- | :--------- | :---------------------------------- |
    | `--help`    | `-h`       | Show help information               |
    | `--quiet`   | `-q`       | Suppress output                     |
    | `--timeout` |            | Timeout (default 60s, 0 to disable) |

    **Example**

    ```bash theme={null}
    pc config unset api-key
    pc config unset color
    ```
  </Accordion>
</AccordionGroup>
