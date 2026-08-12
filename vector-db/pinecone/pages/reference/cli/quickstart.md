---
title: "CLI quickstart"
source: https://docs.pinecone.io/reference/cli/quickstart
path: reference/cli/quickstart
---

Pinecone CLI quickstart for installing pc, authenticating, and managing indexes, vectors, and data imports directly from your terminal.

The Pinecone CLI (`pc`) lets you manage Pinecone resources directly from your terminal.

## Install

<Tabs>
  <Tab title="macOS (Homebrew)">
    ```bash theme={null}
    brew tap pinecone-io/tap
    brew install pinecone-io/tap/pinecone
    ```
  </Tab>

  <Tab title="Other platforms">
    Pre-built binaries for macOS, Linux, and Windows are available on the [GitHub Releases page](https://github.com/pinecone-io/cli/releases).

    | Platform | Architectures                          |
    | :------- | :------------------------------------- |
    | macOS    | Intel (x86\_64), Apple Silicon (ARM64) |
    | Linux    | x86\_64, ARM64, i386                   |
    | Windows  | x86\_64, i386                          |
  </Tab>
</Tabs>

## Authenticate

```bash theme={null}
pc auth login
```

Visit the URL in your terminal to sign in. The CLI automatically sets your default organization and project.

To target a different org/project:

```bash theme={null}
pc target -o "my-org" -p "my-project"
```

<Tip>
  For CI/CD or automation, you can also authenticate with a [service account](/reference/cli/authentication#service-account) or [API key](/reference/cli/authentication#api-key).
</Tip>

## Manage indexes

```bash theme={null}
# List indexes
pc index list

# Create an index
pc index create -n my-index -d 3 -m cosine -c aws -r us-east-1

# Get index details
pc index describe -i my-index

# Get index statistics
pc index stats -i my-index
```

## Work with vectors

```bash theme={null}
# Upsert vectors (from file or inline JSON)
pc index vector upsert -i my-index \
  --body '{"vectors": [{"id": "vec1", "values": [0.1, 0.2, 0.3], "metadata": {"genre": "comedy"}}]}'

# Import from a large dataset in object storage (S3, GCS, Azure)
pc index import start -i my-index --uri s3://my-bucket/data/

# Check the progress of an import operation
pc index import list --i my-index
pc index import describe --i my-index --id import-123

# Query (vector can be inline or in a file)
pc index vector query -i my-index \
  --vector '[0.1, 0.2, 0.3]' \
  --top-k 10 \
  --include-metadata

# Fetch by ID (from file or inline JSON)
pc index vector fetch -i my-index --ids '["vec1","vec2"]'

# List vector IDs from an index
pc index vector list -i my-index
```

## Manage namespaces

```bash theme={null}
# List namespaces
pc index namespace list -i my-index

# Create a namespace
pc index namespace create -i my-index --name tenant-a

# Delete a namespace
pc index namespace delete -i my-index --name tenant-a
```

## Back up and restore

```bash theme={null}
# Create a backup
pc index backup create -i my-index --name "my-index-backup"

# List backups (show index, backup name, backup ID, etc.)
pc index backup list -i my-index

# Restore from backup (by ID, not name)
pc index restore -i c84725e5-5956-41ba-ab62-21ac7b5f2a2f -n restored-index
```

## JSON output

Add `-j` to any command for JSON output:

```bash theme={null}
pc index list -j
pc index describe -i my-index -j
```

## Getting help

Use `-h` or `--help` with any command to see available options:

```bash theme={null}
pc -h
pc index -h
pc index create -h
```

## Next steps

* [Command reference](/reference/cli/command-reference) — Full list of commands and flags
* [Authentication](/reference/cli/authentication) — Service accounts, API keys, and auth priority
* [Target context](/reference/cli/target-context) — How org/project targeting works
