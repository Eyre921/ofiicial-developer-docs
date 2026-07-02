---
title: "Audit Filesystem Changes"
source: https://docs.turso.tech/agentfs/guides/auditing
path: agentfs/guides/auditing
---

Inspect and analyze what an agent did during a session

AgentFS records every file operation and tool call, giving you complete visibility into agent behavior. This is essential for debugging, compliance, and understanding how agents work.

## Viewing the Timeline

See a chronological list of tool calls:

```bash theme={null}
agentfs timeline my-session
```

Output:

```
ID   TOOL                 STATUS       DURATION STARTED
4    execute_code         pending            -- 2024-01-05 09:44:20
3    api_call             error           300ms 2024-01-05 09:44:15
2    read_file            success          50ms 2024-01-05 09:44:10
1    web_search           success        1200ms 2024-01-05 09:43:45
```

### Filtering Results

Show only specific tool types:

```bash theme={null}
agentfs timeline my-session --filter web_search
```

Show only errors:

```bash theme={null}
agentfs timeline my-session --status error
```

Limit number of entries:

```bash theme={null}
agentfs timeline my-session --limit 20
```

### JSON Output

For programmatic analysis:

```bash theme={null}
agentfs timeline my-session --format json
```

```json theme={null}
[
  {
    "id": 1,
    "name": "web_search",
    "status": "success",
    "started_at": 1704447825,
    "completed_at": 1704447826,
    "duration_ms": 1200,
    "parameters": {"query": "AI agents"},
    "result": {"results": ["result1", "result2"]}
  }
]
```

## Inspecting Files

List all files in a session:

```bash theme={null}
agentfs fs ls my-session
```

Output:

```
d artifacts
f config.json
f output.txt
```

List a subdirectory:

```bash theme={null}
agentfs fs ls my-session /artifacts
```

Read file contents:

```bash theme={null}
agentfs fs cat my-session /output.txt
```

## Viewing Changes (Diff)

See what changed compared to the original filesystem:

```bash theme={null}
agentfs diff my-session
```

This shows:

* New files created
* Modified files
* Deleted files

## Querying with SQL

Since AgentFS uses SQLite, you can run arbitrary queries:

<Tabs>
  <Tab title="Turso">
    ```bash theme={null}
    tursodb .agentfs/my-session.db
    ```
  </Tab>

  <Tab title="SQLite">
    ```bash theme={null}
    sqlite3 .agentfs/my-session.db
    ```
  </Tab>
</Tabs>

Example queries:

```sql theme={null}
-- Find all tool calls that took longer than 1 second
SELECT name, duration_ms
FROM toolcalls
WHERE duration_ms > 1000;

-- Count tool usage by type
SELECT name, COUNT(*) as count
FROM toolcalls
GROUP BY name
ORDER BY count DESC;

-- Find files modified in the last hour
SELECT path, mtime
FROM fs_inode
WHERE mtime > strftime('%s', 'now', '-1 hour');

-- Get total bytes written
SELECT SUM(size) as total_bytes
FROM fs_inode
WHERE mode & 0170000 = 0100000;  -- regular files only
```

## Use Cases

### Debugging Agent Failures

When an agent fails, use the timeline to understand what happened:

```bash theme={null}
# See recent activity
agentfs timeline my-session --limit 20

# Focus on errors
agentfs timeline my-session --status error

# Check what files were created/modified
agentfs fs ls my-session
```

### Performance Analysis

Find slow operations:

```sql theme={null}
SELECT name, AVG(duration_ms) as avg_ms, COUNT(*) as count
FROM toolcalls
GROUP BY name
ORDER BY avg_ms DESC;
```

### Compliance Auditing

Export a complete record of agent activity:

```bash theme={null}
agentfs timeline my-session --format json > audit-log.json
```

## Next Steps

<CardGroup>
  <Card title="Overlay Filesystem" icon="layer-group" href="/agentfs/guides/overlay">
    Understanding copy-on-write
  </Card>

  <Card title="Syncing" icon="cloud" href="/agentfs/guides/sync">
    Sync sessions to Turso Cloud
  </Card>
</CardGroup>
