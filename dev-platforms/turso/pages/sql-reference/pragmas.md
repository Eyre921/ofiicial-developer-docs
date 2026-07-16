---
title: "PRAGMA Statements"
source: https://docs.turso.tech/sql-reference/pragmas
path: sql-reference/pragmas
---

Database configuration and metadata commands in Turso

# PRAGMA Statements

PRAGMA statements are special commands used to query or modify database configuration, retrieve metadata, and control database behavior. Unlike standard SQL, PRAGMAs are specific to SQLite and Turso.

## Syntax

```sql theme={null}
PRAGMA pragma-name;
PRAGMA pragma-name = value;
PRAGMA pragma-name(value);
```

## Database Metadata

### database\_list

Returns one row for each attached database.

```sql theme={null}
PRAGMA database_list;
-- seq | name | file
-- 0   | main | /path/to/database.db
```

### page\_count

Returns the total number of pages in the database file.

```sql theme={null}
PRAGMA page_count;
-- 42
```

### page\_size

Returns or sets the page size of the database. The page size can only be set before any tables are created.

```sql theme={null}
PRAGMA page_size;
-- 4096

PRAGMA page_size = 8192;
```

### max\_page\_count

Returns or sets the maximum number of pages allowed in the database file.

```sql theme={null}
PRAGMA max_page_count;
PRAGMA max_page_count = 1000000;
```

### freelist\_count

Returns the number of unused pages in the database file.

```sql theme={null}
PRAGMA freelist_count;
```

### encoding

Returns the text encoding used by the database.

```sql theme={null}
PRAGMA encoding;
-- UTF-8
```

### schema\_version

Returns the schema version number. This value is incremented each time the schema changes.

```sql theme={null}
PRAGMA schema_version;
-- 5
```

### application\_id

Returns or sets the application ID stored in the database header. Applications can use this 32-bit integer to identify the database file format.

```sql theme={null}
PRAGMA application_id;
PRAGMA application_id = 12345;
```

### user\_version

Returns or sets the user version number. This is a 32-bit integer available for application use.

```sql theme={null}
PRAGMA user_version;
PRAGMA user_version = 3;
```

## Schema Introspection

### table\_info

Returns one row for each column in the named table.

```sql theme={null}
PRAGMA table_info(table-name);
```

| Column      | Type    | Description                            |
| ----------- | ------- | -------------------------------------- |
| cid         | INTEGER | Column index (0-based)                 |
| name        | TEXT    | Column name                            |
| type        | TEXT    | Declared type name                     |
| notnull     | INTEGER | 1 if NOT NULL constraint exists        |
| dflt\_value | TEXT    | Default value expression, or NULL      |
| pk          | INTEGER | 1 if column is part of the PRIMARY KEY |

```sql theme={null}
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT);
PRAGMA table_info(users);
-- cid | name  | type    | notnull | dflt_value | pk
-- 0   | id    | INTEGER | 0       |            | 1
-- 1   | name  | TEXT    | 1       |            | 0
-- 2   | email | TEXT    | 0       |            | 0
```

### table\_xinfo

Similar to `table_info` but also includes hidden columns and additional metadata.

```sql theme={null}
PRAGMA table_xinfo(table-name);
```

Returns the same columns as `table_info` plus a `hidden` column (0 for normal columns, non-zero for hidden columns in virtual tables).

### table\_list

Returns one row for each table and view in the database.

```sql theme={null}
PRAGMA table_list;
-- schema | name    | type  | ncol | wr | strict
-- main   | users   | table | 3    | 0  | 0
-- main   | orders  | table | 4    | 0  | 0
```

### index\_list

Returns one row for each index on the named table.

```sql theme={null}
PRAGMA index_list(table-name);
-- seq | name           | unique | origin | partial
-- 0   | idx_email      | 1      | c      | 0
```

| Column  | Type    | Description                                                           |
| ------- | ------- | --------------------------------------------------------------------- |
| seq     | INTEGER | Index sequence number                                                 |
| name    | TEXT    | Index name                                                            |
| unique  | INTEGER | 1 if the index is UNIQUE                                              |
| origin  | TEXT    | `c` for CREATE INDEX, `u` for UNIQUE constraint, `pk` for PRIMARY KEY |
| partial | INTEGER | 1 if the index is a partial index                                     |

### index\_info

Returns one row for each column in the named index.

```sql theme={null}
PRAGMA index_info(index-name);
-- seqno | cid | name
-- 0     | 2   | email
```

### index\_xinfo

Similar to `index_info` but includes additional columns.

```sql theme={null}
PRAGMA index_xinfo(index-name);
```

### function\_list

Returns one row for each SQL function available.

```sql theme={null}
PRAGMA function_list;
-- name | builtin | type | enc | narg | flags
```

### pragma\_list

Returns the list of all supported PRAGMA commands.

```sql theme={null}
PRAGMA pragma_list;
```

## Database Configuration

### journal\_mode

Returns or sets the journal mode.

```sql theme={null}
PRAGMA journal_mode;
-- wal

PRAGMA journal_mode = wal;
```

Turso supports WAL (Write-Ahead Logging) mode. Rollback journal modes (DELETE, TRUNCATE, PERSIST, MEMORY) are not supported.

<Info>
  **Turso Extension**: Turso supports an experimental MVCC journal mode for concurrent writes:

  ```sql theme={null}
  PRAGMA journal_mode = mvcc;
  ```

  When MVCC mode is active, you can use `BEGIN CONCURRENT` for optimistic concurrent write transactions. See [Transactions](/sql-reference/statements/transactions#begin-concurrent) for details.
</Info>

### cache\_size

Returns or sets the suggested maximum number of database pages held in memory.

```sql theme={null}
PRAGMA cache_size;
PRAGMA cache_size = 2000;          -- positive: number of pages
PRAGMA cache_size = -2000;         -- negative: kilobytes of memory
```

### cache\_spill

Enables or disables cache spilling (writing dirty pages to the WAL before the cache is full).

```sql theme={null}
PRAGMA cache_spill;
PRAGMA cache_spill = 0;    -- disable
PRAGMA cache_spill = 1;    -- enable
```

### synchronous

Controls the fsync behavior for durability guarantees.

```sql theme={null}
PRAGMA synchronous;
PRAGMA synchronous = OFF;    -- no fsync (fastest, risk of corruption on crash)
PRAGMA synchronous = FULL;   -- fsync after every transaction (safest)
```

Only `OFF` and `FULL` are supported in Turso.

### temp\_store

Controls where temporary tables and indexes are stored.

```sql theme={null}
PRAGMA temp_store;
PRAGMA temp_store = 0;    -- DEFAULT
PRAGMA temp_store = 1;    -- FILE
PRAGMA temp_store = 2;    -- MEMORY
```

### busy\_timeout

Sets the busy timeout in milliseconds. When a table is locked, Turso waits up to this many milliseconds before returning SQLITE\_BUSY.

```sql theme={null}
PRAGMA busy_timeout;
PRAGMA busy_timeout = 5000;   -- 5 seconds
```

### query\_only

When enabled, prevents any changes to the database.

```sql theme={null}
PRAGMA query_only = 1;    -- enable read-only mode
PRAGMA query_only = 0;    -- disable read-only mode
```

### foreign\_keys

Enables or disables foreign key constraint enforcement.

```sql theme={null}
PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys = OFF;
```

Foreign key enforcement is off by default for SQLite compatibility.

### legacy\_file\_format

Returns the legacy file format flag.

```sql theme={null}
PRAGMA legacy_file_format;
```

### ignore\_check\_constraints

When enabled, CHECK constraints are not enforced.

```sql theme={null}
PRAGMA ignore_check_constraints = 1;   -- disable CHECK constraints
PRAGMA ignore_check_constraints = 0;   -- enable CHECK constraints
```

### data\_sync\_retry

Controls whether Turso retries a disk sync (fsync) after a failure instead of treating it as fatal.

```sql theme={null}
PRAGMA data_sync_retry = 1;   -- retry on sync failure
PRAGMA data_sync_retry = 0;   -- do not retry (default)
```

### require\_where

<Info>
  **Turso Extension**: a safety pragma with no SQLite equivalent.
</Info>

When enabled, Turso rejects any `UPDATE` or `DELETE` that does not include a `WHERE` clause, guarding against accidental full-table modifications. `i_am_a_dummy` is an alias that enables the same behavior.

```sql theme={null}
PRAGMA require_where = 1;
DELETE FROM users;            -- rejected: no WHERE clause
DELETE FROM users WHERE id = 1;  -- allowed

PRAGMA i_am_a_dummy = 1;      -- equivalent to require_where = 1
```

## Integrity Checks

### integrity\_check

Performs a thorough integrity check of the entire database.

```sql theme={null}
PRAGMA integrity_check;
-- ok

PRAGMA integrity_check(N);    -- check only the first N errors
```

Returns `ok` if no problems are found, otherwise returns one row per error.

### quick\_check

Performs a faster but less thorough integrity check than `integrity_check`.

```sql theme={null}
PRAGMA quick_check;
```

## WAL Operations

### wal\_checkpoint

Forces a WAL checkpoint.

```sql theme={null}
PRAGMA wal_checkpoint;
```

A checkpoint writes pages from the WAL file back to the database file.

## MVCC Tuning

<Info>
  **Turso Extension**: these pragmas apply only when MVCC mode is enabled (`PRAGMA journal_mode = mvcc`).
</Info>

### mvcc\_checkpoint\_threshold

Sets the amount of committed work that accumulates before Turso triggers an MVCC checkpoint.

```sql theme={null}
PRAGMA mvcc_checkpoint_threshold = 1000;
```

### mvcc\_gc\_threshold

Sets the threshold that controls how aggressively Turso garbage-collects obsolete MVCC row versions.

```sql theme={null}
PRAGMA mvcc_gc_threshold = 1000;
```

## Change Data Capture

<Info>
  **Turso Extension**: Change Data Capture (CDC) is a Turso-specific feature that tracks all data changes for replication, auditing, and reactive applications.
</Info>

### capture\_data\_changes\_conn

Enables CDC for the current connection. Changes are captured to a designated table.

```sql theme={null}
PRAGMA capture_data_changes_conn('mode');
PRAGMA capture_data_changes_conn('mode,table_name');
```

The legacy name `unstable_capture_data_changes_conn` is still accepted for backwards compatibility.

| Parameter   | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| mode        | Capture mode: `off`, `id`, `before`, `after`, `full`         |
| table\_name | Custom table name for storing changes (default: `turso_cdc`) |

#### Capture Modes

| Mode     | Description                                               |
| -------- | --------------------------------------------------------- |
| `off`    | Disable CDC for this connection                           |
| `id`     | Capture only the primary key/rowid of changed rows        |
| `before` | Capture row state before changes (for updates/deletes)    |
| `after`  | Capture row state after changes (for inserts/updates)     |
| `full`   | Capture both before and after states, plus update details |

#### CDC Table Structure

The CDC table contains the following columns:

| Column       | Type    | Description                                      |
| ------------ | ------- | ------------------------------------------------ |
| change\_id   | INTEGER | Auto-incrementing unique identifier              |
| change\_time | INTEGER | Unix epoch timestamp                             |
| change\_type | INTEGER | 1 (INSERT), 0 (UPDATE), -1 (DELETE)              |
| table\_name  | TEXT    | Name of the changed table                        |
| id           | varies  | Primary key/rowid of the changed row             |
| before       | BLOB    | Row data before the change (modes: before, full) |
| after        | BLOB    | Row data after the change (modes: after, full)   |
| updates      | BLOB    | Updated column details (mode: full)              |

#### CDC Examples

```sql theme={null}
-- Enable full CDC
PRAGMA capture_data_changes_conn('full');

-- Make changes
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO users VALUES (1, 'Alice');
UPDATE users SET name = 'Alicia' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- Query the changes
SELECT change_type, table_name, id FROM turso_cdc;
-- 1  | users | 1    (INSERT)
-- 0  | users | 1    (UPDATE)
-- -1 | users | 1    (DELETE)

-- Use a custom table name
PRAGMA capture_data_changes_conn('full,audit_log');

-- Disable CDC
PRAGMA capture_data_changes_conn('off');
```

CDC respects transaction boundaries. Changes are only recorded when a transaction commits. If a transaction rolls back, no CDC entries are created.

## Encryption

<Info>
  **Turso Extension**: At-rest encryption is a Turso-specific feature. This feature is experimental and must be [enabled before use](/sql-reference/experimental-features).
</Info>

### cipher

Sets the encryption cipher for the database.

```sql theme={null}
PRAGMA cipher = 'aegis256';
```

Supported ciphers:

| Cipher       | Key Size | Description                       |
| ------------ | -------- | --------------------------------- |
| `aes128gcm`  | 16 bytes | AES-128 in Galois/Counter Mode    |
| `aes256gcm`  | 32 bytes | AES-256 in Galois/Counter Mode    |
| `aegis128l`  | 16 bytes | AEGIS-128L                        |
| `aegis256`   | 32 bytes | AEGIS-256 (recommended)           |
| `aegis128x2` | 16 bytes | AEGIS-128 with 2x parallelization |
| `aegis128x4` | 16 bytes | AEGIS-128 with 4x parallelization |
| `aegis256x2` | 32 bytes | AEGIS-256 with 2x parallelization |
| `aegis256x4` | 32 bytes | AEGIS-256 with 4x parallelization |

### hexkey

Sets the encryption key as a hexadecimal string.

```sql theme={null}
PRAGMA hexkey = '2d7a30108d3eb3e45c90a732041fe54778bdcf707c76749fab7da335d1b39c1d';
```

#### Encryption Example

```sql theme={null}
-- Set cipher and key before creating tables
PRAGMA cipher = 'aegis256';
PRAGMA hexkey = '2d7a30108d3eb3e45c90a732041fe54778bdcf707c76749fab7da335d1b39c1d';

CREATE TABLE secrets (id INTEGER PRIMARY KEY, data TEXT);
INSERT INTO secrets VALUES (1, 'sensitive data');
```

Alternatively, specify encryption parameters in the database URI:

```
file:database.db?cipher=aegis256&hexkey=2d7a30...
```

To open an existing encrypted database, the cipher and key must be provided as URI parameters.

## Custom Types

<Info>
  **Turso Extension**: Custom types are a Turso-specific feature.
</Info>

### list\_types

Lists all available types (built-in and custom) with their metadata.

```sql theme={null}
PRAGMA list_types;
-- type    | parent | encode | decode | default | operators
-- INTEGER |        |        |        |         |
-- REAL    |        |        |        |         |
-- TEXT    |        |        |        |         |
-- BLOB    |        |        |        |         |
-- ANY     |        |        |        |         |
```

See [CREATE TYPE](/sql-reference/statements/create-type) for creating custom types.

## See Also

* [Transactions](/sql-reference/statements/transactions) for transaction control
* [CREATE TYPE](/sql-reference/statements/create-type) for custom type definitions
* [Compatibility](/sql-reference/compatibility) for the full list of supported PRAGMAs
