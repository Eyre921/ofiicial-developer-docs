---
title: "Development branches"
source: https://trigger.dev/docs/deployment/dev-branches
path: docs/deployment/dev-branches
---

Run multiple local dev sessions in isolation by giving each one its own development branch. Use branches to keep parallel work (in separate worktrees, directories, or agents) from clashing.

Every project starts with a single development environment called `default`. A **dev branch** is an isolated environment that lives under development, with its own runs, schedules, and concurrency.

Branches are useful when you run more than one local dev session at a time. Give each session its own branch so their runs don't collide:

* Run several [git worktrees](https://git-scm.com/docs/git-worktree) or copies of your project in parallel, one branch each.
* Let multiple coding agents each work in their own branch without stepping on one another.

When you're done with a branch, you can archive it to free up a slot or just re-use it.

## Run a dev session on a branch

Log in with the CLI first:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest login
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest login
```

```bash bun theme={"theme":"css-variables"}
bunx trigger.dev@latest login
```

Then start a dev session on a branch with the `--branch` flag. If the branch doesn't exist yet, it's created:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev --branch my-feature
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev --branch my-feature
```

```bash bun theme={"theme":"css-variables"}
bunx trigger.dev@latest dev --branch my-feature
```

Without `--branch`, the session runs on the `default` branch.

> [!TIP]
>
> You can also set the branch with the `TRIGGER_DEV_BRANCH` environment variable instead of the flag.

## Archive a branch

Archive a branch from the CLI when you no longer need it. Pass the branch with `--branch` (or set `TRIGGER_DEV_BRANCH`); it's required, and the `default` branch can't be archived:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev archive --branch my-feature
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev archive --branch my-feature
```

```bash bun theme={"theme":"css-variables"}
bunx trigger.dev@latest dev archive --branch my-feature
```

You can also create and archive branches from the **Dev branches** page in the dashboard.

## Limits on active branches

Each branch has its own concurrency, so we limit how many dev branches each developer can have active per project. The `default` development environment counts toward this limit. If you are at the limit when you run `dev --branch`, the CLI automatically archives up to 3 of your branches that have no connected dev session and have been idle for over an hour, to make room. You can also archive a branch any time to free a slot.

| Plan | Active dev branches |
| - | - |
| Free | 50 |
| Hobby | 50 |
| Pro | 50 |

Need more? [Get in touch](https://trigger.dev/contact) and we'll raise the limit.
