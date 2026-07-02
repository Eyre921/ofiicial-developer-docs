---
title: "Shared Agent Sessions"
source: https://docs.turso.tech/agentfs/guides/sessions
path: agentfs/guides/sessions
---

Share state between multiple agents and terminals with named sessions

Named sessions let you share a filesystem between multiple agents, terminals, or runs. All participants see the same copy-on-write view of your project.

## Creating a Session

Use `--session` to create a named session:

```bash theme={null}
agentfs run --session my-project /bin/bash
```

This creates a session called `my-project`. All changes are stored in `.agentfs/my-project.db`.

## Resuming a Session

Run the same command to resume where you left off:

```bash theme={null}
# First run - make some changes
agentfs run --session my-project /bin/bash
$ echo "hello" > test.txt
$ exit

# Second run - changes are still there
agentfs run --session my-project /bin/bash
$ cat test.txt
hello
```

## Multi-Terminal Collaboration

Multiple terminals can share the same session simultaneously:

```bash theme={null}
# Terminal 1
agentfs run --session shared-work /bin/bash

# Terminal 2 - joins the same filesystem
agentfs run --session shared-work python3 agent.py

# Terminal 3 - also sees the same files
agentfs run --session shared-work vim
```

All terminals share the same copy-on-write filesystem. Changes made in one terminal are immediately visible in others.

## Use Cases

### Iterative Development

Work on a task across multiple sessions:

```bash theme={null}
# Morning session
agentfs run --session feature-x /bin/bash
# ... work on the feature, then exit for lunch

# Afternoon session - continue where you left off
agentfs run --session feature-x /bin/bash
```

### Safe Experimentation

Create a session, try something risky, then decide whether to keep it:

```bash theme={null}
agentfs run --session experiment /bin/bash
# ... try some changes

# Option A: Happy with changes
agentfs diff experiment  # Review
# Apply changes to real filesystem (manually or via script)

# Option B: Discard everything
rm .agentfs/experiment.db
```

### Agent Supervision

Run an agent and monitor its work from another terminal:

```bash theme={null}
# Terminal 1: Run the agent
agentfs run --session agent-task python3 agent.py

# Terminal 2: Watch what it's doing
agentfs run --session agent-task /bin/bash
$ watch ls -la  # See files being created
$ tail -f agent.log  # Monitor logs
```

## Managing Sessions

List files in a session:

```bash theme={null}
agentfs fs ls my-session
```

View session changes:

```bash theme={null}
agentfs diff my-session
```

Delete a session:

```bash theme={null}
rm .agentfs/my-session.db
```

## Session Storage

Sessions are stored as SQLite databases in `.agentfs/`:

```
.agentfs/
├── my-project.db
├── experiment.db
└── shared-work.db
```

Each database contains:

* All modified files
* Deleted file markers (whiteouts)
* Tool call audit log
* Key-value store data

## Next Steps

<CardGroup>
  <Card title="Auditing" icon="list" href="/agentfs/guides/auditing">
    Inspect what happened in a session
  </Card>

  <Card title="Overlay Filesystem" icon="layer-group" href="/agentfs/guides/overlay">
    How copy-on-write works
  </Card>
</CardGroup>
