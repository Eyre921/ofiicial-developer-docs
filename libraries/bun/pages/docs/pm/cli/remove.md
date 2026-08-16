---
title: "bun remove"
source: https://bun.com/docs/pm/cli/remove
path: docs/pm/cli/remove
---

Remove dependencies from your project

## Basic Usage

<Note>**Alias** — `bun rm`, `bun uninstall`, `bun r`</Note>

```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun remove ts-node
```

Bun removes the package from every dependency group in `package.json` that lists it and updates `bun.lock`. Once nothing else depends on the package, Bun deletes it from `node_modules`.

## `--filter`

<Note>**Alias** — `-F`</Note>

In a monorepo, remove the package from the matching workspace(s) instead of the current directory's package, using the same patterns as [`bun add --filter`](/docs/pm/cli/add#--filter). Use `--filter '*'` to remove it from every workspace package. Workspaces that don't list the package are left untouched.

```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun remove zod --filter api
bun remove zod --filter '*'
```

***

## CLI Usage

```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun remove <package>
```

### General Information

<ParamField type="boolean">
  Print this help menu. Alias: <code>-h</code>
</ParamField>

### Configuration

<ParamField type="string">
  Specify path to config file (<code>bunfig.toml</code>). Alias: <code>-c</code>
</ParamField>

### Package.json Interaction

<ParamField type="boolean">
  Don't update <code>package.json</code> or save a lockfile
</ParamField>

<ParamField type="boolean">
  Save to <code>package.json</code> (true by default)
</ParamField>

<ParamField type="boolean">
  Add to <code>trustedDependencies</code> in the project's <code>package.json</code> and install the package(s)
</ParamField>

<ParamField type="string">
  Remove the package(s) from the matching workspaces instead of the current package. Alias: <code>-F</code>
</ParamField>

### Lockfile Behavior

<ParamField type="boolean">
  Write a <code>yarn.lock</code> file (yarn v1). Alias: <code>-y</code>
</ParamField>

<ParamField type="boolean">
  Disallow changes to lockfile
</ParamField>

<ParamField type="boolean">
  Save a text-based lockfile
</ParamField>

<ParamField type="boolean">
  Generate a lockfile without installing dependencies
</ParamField>

### Dependency Filtering

<ParamField type="boolean">
  Don't install devDependencies. Alias: <code>-p</code>
</ParamField>

<ParamField type="string">
  Exclude <code>dev</code>, <code>optional</code>, or <code>peer</code> dependencies from install
</ParamField>

### Network & Registry

<ParamField type="string">
  Provide a Certificate Authority signing certificate
</ParamField>

<ParamField type="string">
  Same as <code>--ca</code>, but as a file path to the certificate
</ParamField>

<ParamField type="string">
  Use a specific registry by default, overriding <code>.npmrc</code>, <code>bunfig.toml</code> and environment variables
</ParamField>

### Execution Control & Validation

<ParamField type="boolean">
  Perform a dry run without making changes
</ParamField>

<ParamField type="boolean">
  Always request the latest versions from the registry & reinstall all dependencies. Alias: <code>-f</code>
</ParamField>

<ParamField type="boolean">
  Skip verifying integrity of newly downloaded packages
</ParamField>

### Output & Logging

<ParamField type="boolean">
  Don't log anything
</ParamField>

<ParamField type="boolean">
  Excessively verbose logging
</ParamField>

<ParamField type="boolean">
  Disable the progress bar
</ParamField>

<ParamField type="boolean">
  Don't print a summary
</ParamField>

### Caching

<ParamField type="string">
  Store & load cached data from a specific directory path
</ParamField>

<ParamField type="boolean">
  Ignore manifest cache entirely
</ParamField>

### Script Execution

<ParamField type="boolean">
  Skip lifecycle scripts for all packages, including the project's <code>package.json</code> and trusted dependencies
</ParamField>

<ParamField type="number">
  Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)
</ParamField>

### Scope & Path

<ParamField type="boolean">
  Install globally. Alias: <code>-g</code>
</ParamField>

<ParamField type="string">
  Set a specific cwd
</ParamField>

### Advanced & Performance

<ParamField type="string">
  Platform-specific optimizations for installing dependencies. Possible values: <code>clonefile</code> (default on
  macOS), <code>hardlink</code> (default on Linux and Windows), <code>symlink</code>, <code>copyfile</code>
</ParamField>

<ParamField type="number">
  Maximum number of concurrent network requests (default 48)
</ParamField>
