---
title: "Shell Commands"
source: https://docs.turso.tech/sql-reference/cli/shell-commands
path: sql-reference/cli/shell-commands
---

Dot commands available in the Turso interactive SQL shell

# Shell Commands

Dot commands are special commands available in the interactive shell. They start with a period (`.`) and do not require a trailing semicolon.

```
tursodb> .help
```

## Database & Navigation

### .open

Open a database file, optionally specifying a VFS backend.

```
.open <PATH> [VFS]
```

```
tursodb> .open mydata.db
tursodb> .open mydata.db memory
```

### .quit

Exit the shell. Aliases: `.q`, `.qu`, `.qui`.

```
tursodb> .quit
```

### .exit

Exit the shell with an optional return code. Aliases: `.ex`, `.exi`.

```
.exit [CODE]
```

```
tursodb> .exit
tursodb> .exit 1
```

### .cd

Change the current working directory.

```
.cd <DIRECTORY>
```

```
tursodb> .cd /tmp
```

## Schema Inspection

### .tables

List all tables in the database, optionally filtered by a pattern.

```
.tables [PATTERN]
```

```sql theme={null}
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);
```

```
tursodb> .tables
employees
departments

tursodb> .tables emp%
employees
```

### .schema

Display the CREATE statement for a table, or all tables if no argument is given.

```
.schema [TABLE]
```

```
tursodb> .schema employees
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT);

tursodb> .schema
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);
```

### .indexes

Show index names, optionally filtered by table.

```
.indexes [TABLE]
```

```sql theme={null}
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT);
CREATE INDEX idx_dept ON employees(department);
CREATE INDEX idx_name ON employees(name);
```

```
tursodb> .indexes
idx_dept
idx_name

tursodb> .indexes employees
idx_dept
idx_name
```

### .databases

List all attached databases.

```
tursodb> .databases
main: /path/to/mydata.db r/w
```

## Output Control

### .mode

Set the output display mode.

```
.mode <MODE>
```

| Mode     | Description                           |
| -------- | ------------------------------------- |
| `pretty` | Table with borders (default)          |
| `list`   | Pipe-delimited values                 |
| `line`   | One column per line with column names |

```
tursodb> .mode list
tursodb> SELECT 1 AS a, 2 AS b;
1|2

tursodb> .mode line
tursodb> SELECT 1 AS a, 2 AS b;
a = 1
b = 2

tursodb> .mode pretty
tursodb> SELECT 1 AS a, 2 AS b;
┌───┬───┐
│ a │ b │
├───┼───┤
│ 1 │ 2 │
└───┴───┘
```

### .headers

Toggle column headers on or off in `list` mode.

```
.headers <on|off>
```

```
tursodb> .mode list
tursodb> .headers on
tursodb> SELECT 1 AS x, 2 AS y;
x|y
1|2

tursodb> .headers off
tursodb> SELECT 1 AS x, 2 AS y;
1|2
```

### .nullvalue

Set the string displayed for NULL values in `list` mode.

```
.nullvalue <STRING>
```

```
tursodb> .mode list
tursodb> .nullvalue [NULL]
tursodb> SELECT 1 AS a, NULL AS b;
1|[NULL]
```

### .output

Redirect query output to a file. Call with no argument or `stdout` to restore output to the terminal.

```
.output [PATH]
```

```
tursodb> .output results.txt
tursodb> SELECT * FROM employees;
tursodb> .output
tursodb> -- Output is back to the terminal
```

### .echo

Toggle echo mode. When on, each SQL statement is printed before execution.

```
.echo <on|off>
```

```
tursodb> .echo on
tursodb> SELECT 42;
