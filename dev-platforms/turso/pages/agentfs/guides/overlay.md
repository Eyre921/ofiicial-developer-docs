---
title: "Copy-on-Write Overlays"
source: https://docs.turso.tech/agentfs/guides/overlay
path: agentfs/guides/overlay
---

How copy-on-write isolation works in AgentFS

AgentFS uses an overlay filesystem to provide copy-on-write isolation. This lets agents freely modify files while keeping your original data safe.

## How Overlay Works

An overlay filesystem combines two layers:

```
┌────────────────────────────────────┐
│         Merged View (what you see) │
├────────────────────────────────────┤
│  Delta Layer (AgentFS database)    │  ← Writes go here
├────────────────────────────────────┤
│  Base Layer (original directory)   │  ← Read-only
└────────────────────────────────────┘
```

**Reading a file:**

1. Check delta layer first
2. If not found, read from base layer

**Writing a file:**

1. Copy file to delta layer (if from base)
2. Write changes to delta layer
3. Base layer is never modified

**Deleting a file:**

1. Create a "whiteout" marker in delta layer
2. File appears deleted in merged view
3. Original file in base layer is untouched

## Creating an Overlay Filesystem

### With `agentfs run`

The simplest way - automatically creates an overlay over your current directory:

```bash theme={null}
cd /path/to/project
agentfs run /bin/bash
```

### With `agentfs init --base`

Create an overlay explicitly:

```bash theme={null}
agentfs init my-overlay --base /path/to/project
```

Then mount it:

```bash theme={null}
agentfs mount my-overlay ./workspace
```

Or run a command in it:

```bash theme={null}
agentfs run --session my-overlay /bin/bash
```

## Viewing Changes

See what's different from the base:

```bash theme={null}
agentfs diff my-overlay
```

## Practical Examples

### Safe Refactoring

Let an agent refactor your code without risk:

```bash theme={null}
cd my-project
agentfs run --session refactor python3 refactor_agent.py

# Review what changed
agentfs diff refactor

# Happy? Apply changes manually or via script
# Not happy? Just delete the session
rm .agentfs/refactor.db
```

### Testing Destructive Operations

Try something dangerous safely:

```bash theme={null}
agentfs run --session test /bin/bash
$ rm -rf src/  # Yikes!
$ exit

# Original files are fine
ls src/  # Still there!

# Only the overlay was affected
agentfs fs ls test  # Shows the deletion
```

### Parallel Experiments

Run multiple experiments on the same codebase:

```bash theme={null}
# Experiment A
agentfs run --session exp-a python3 approach_a.py

# Experiment B (same base, different changes)
agentfs run --session exp-b python3 approach_b.py

# Compare results
agentfs diff exp-a
agentfs diff exp-b
```

## Storage Efficiency

The overlay only stores:

* **Modified files** - Full copy after first write
* **New files** - Stored entirely in delta
* **Deleted files** - Small whiteout marker

Original files are never duplicated. A 10GB project with 1MB of changes only uses \~1MB in the delta layer.

## Technical Details

### File Operations

| Operation           | Behavior                  |
| ------------------- | ------------------------- |
| Read existing file  | Pass through to base      |
| Write existing file | Copy to delta, then write |
| Create new file     | Write directly to delta   |
| Delete file         | Create whiteout in delta  |
| Rename file         | Delete old + create new   |

### Whiteouts

When you delete a base file, AgentFS creates a "whiteout" - a marker that hides the file:

```sql theme={null}
-- Whiteouts in the database
SELECT * FROM fs_inode WHERE whiteout = 1;
```

### Database Schema

The delta layer is stored in SQLite:

```sql theme={null}
-- Files and directories
CREATE TABLE fs_inode (
    ino INTEGER PRIMARY KEY,
    parent_ino INTEGER,
    name TEXT,
    mode INTEGER,
    size INTEGER,
    ...
    whiteout INTEGER DEFAULT 0
);

-- File contents
CREATE TABLE fs_block (
    ino INTEGER,
    block_num INTEGER,
    data BLOB
);
```

See the [AgentFS Specification](https://github.com/tursodatabase/agentfs/blob/main/SPEC.md) for the complete schema.

## Next Steps

<CardGroup>
  <Card title="Sessions" icon="clock" href="/agentfs/guides/sessions">
    Share state between agents
  </Card>

  <Card title="Syncing" icon="cloud" href="/agentfs/guides/sync">
    Sync overlays to Turso Cloud
  </Card>
</CardGroup>
