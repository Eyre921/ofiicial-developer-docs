---
title: "Getting Started"
source: https://docs.turso.tech/sql-reference/cli/getting-started
path: sql-reference/cli/getting-started
---

Install and use the Turso interactive SQL shell

# Getting Started

The Turso CLI (`tursodb`) is an interactive SQL shell for working with Turso databases. It supports in-memory and file-based databases, multiple output modes, CSV import, database cloning, and built-in documentation.

## Quick Start

### In-Memory Database

Launch the shell with a transient in-memory database:

```bash theme={null}
tursodb
```

### Open a Database File

```bash theme={null}
tursodb mydata.db
```

### Run a Query Directly

Pass SQL as a command-line argument to run it and exit:

```bash theme={null}
tursodb mydata.db "SELECT * FROM users;"
```

### Pipe SQL from stdin

```bash theme={null}
echo "SELECT sqlite_version();" | tursodb -q
```

## Interactive Shell

When launched without a SQL argument, the shell provides an interactive REPL with command history and syntax highlighting.

### Multi-line Input

Unfinished statements (missing semicolons, unbalanced parentheses) automatically continue on the next line. The prompt indicates nesting depth:

```
tursodb> SELECT *
   ...>   FROM employees
   ...>   WHERE department = 'Engineering';
```

### Command History

Command history is saved automatically to `~/.limbo_history` and accessible with up/down arrow keys.

### Exiting

Use `.quit` or `.exit` to leave the shell. Pressing Ctrl+C twice also exits.

## Output Modes

Turso supports three output modes, selectable with the `-m` flag or the `.mode` dot command.

### Pretty (Default)

Human-readable table with borders:

```bash theme={null}
tursodb -q -m pretty
```

```
┌────┬─────────┬─────────────┬─────────┐
│ id │ name    │ department  │ salary  │
├────┼─────────┼─────────────┼─────────┤
│  1 │ Alice   │ Engineering │ 95000.0 │
├────┼─────────┼─────────────┼─────────┤
│  2 │ Bob     │ Marketing   │ 72000.0 │
└────┴─────────┴─────────────┴─────────┘
```

### List

Pipe-delimited values suitable for scripting:

```bash theme={null}
tursodb -q -m list
```

```
1|Alice|Engineering|95000.0
2|Bob|Marketing|72000.0
```

### Line

One column per line, with column names:

```bash theme={null}
tursodb -q -m line
```

```
        id = 1
      name = Alice
department = Engineering
    salary = 95000.0
```

## Non-Interactive Mode

When input is piped (not a terminal), the shell runs in non-interactive mode:

* Output defaults to `list` mode (override with `-m`)
* No startup banner, history, or syntax highlighting
* Exits with code 1 on query errors

```bash theme={null}
echo "SELECT 1 + 2;" | tursodb -q
```

## Server Modes

The CLI can also run as a server instead of an interactive shell.

### MCP Server

Start a [Model Context Protocol](https://modelcontextprotocol.io/) server, allowing AI assistants to interact with the database:

```bash theme={null}
tursodb --mcp mydata.db
```

### Sync Server

Start a sync server for database replication:

```bash theme={null}
tursodb --sync-server 0.0.0.0:8080 mydata.db
```
