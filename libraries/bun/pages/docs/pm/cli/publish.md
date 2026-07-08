---
title: "bun publish"
source: https://bun.com/docs/pm/cli/publish
path: docs/pm/cli/publish
---

Use `bun publish` to publish a package to the npm registry

`bun publish` packs your package into a tarball, strips catalog and workspace protocols from the `package.json` (resolving versions if necessary), and publishes to the registry specified in your configuration files. Both `bunfig.toml` and `.npmrc` files are supported.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
## Publishing the package from the current working directory
bun publish
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish v1.3.3 (ca7428e9)

packed 203B package.json
packed 224B README.md
packed 30B index.ts
packed 0.64KB tsconfig.json

Total files: 4
Shasum: 79e2b4377b63f4de38dc7ea6e5e9dbee08311a69
Integrity: sha512-6QSNlDdSwyG/+[...]X6wXHriDWr6fA==
Unpacked size: 1.1KB
Packed size: 0.76KB
Tag: latest
Access: default
Registry: http://localhost:4873/

 + publish-1@1.0.0
```

To pack and publish separately, run `bun pm pack`, then `bun publish` with the path to the output tarball.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun pm pack
...
bun publish ./package.tgz
```

<Note>
  `bun publish` does not run lifecycle scripts (`prepublishOnly/prepack/prepare/postpack/publish/postpublish`) if a
  tarball path is provided. Scripts run only when `bun publish` packs the package itself.
</Note>

### `--access`

`--access` sets the access level of the package being published, either `public` or `restricted`. Unscoped packages are always public, and publishing an unscoped package with `--access restricted` is an error.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --access public
```

`--access` can also be set in the `publishConfig` field of your `package.json`.

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "publishConfig": {
    "access": "restricted"
  }
}
```

### `--tag`

Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --tag alpha
```

`--tag` can also be set in the `publishConfig` field of your `package.json`.

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "publishConfig": {
    "tag": "next"
  }
}
```

### `--dry-run`

`--dry-run` runs the publish process without publishing the package, so you can verify what would be published.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --dry-run
```

### `--tolerate-republish`

Exit with code 0 instead of 1 if the package version already exists. Useful in CI/CD where jobs may be re-run.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --tolerate-republish
```

### `--gzip-level`

Set the gzip compression level used when packing the package, from `0` to `9` (default `9`). Only applies to `bun publish` without a tarball path argument.

### `--auth-type`

If you have 2FA enabled for your npm account, `bun publish` prompts you for a one-time password, either through a browser or in the CLI. `--auth-type` tells the npm registry which method you prefer: `web` (the default) or `legacy`.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --auth-type legacy
...
This operation requires a one-time password.
Enter OTP: 123456
...
```

### `--otp`

Provide a one-time password directly to the CLI. If the password is valid, `bun publish` skips the extra one-time password prompt before publishing:

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --otp 123456
```

<Note>
  `bun publish` respects the `NPM_CONFIG_TOKEN` environment variable, useful when publishing from GitHub Actions or
  other automated workflows.
</Note>

***

## CLI Usage

```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish dist
```

### Publishing Options

<ParamField type="string">
  Set the access level of the package being published, either `public` or `restricted`. Unscoped packages are always public; publishing an unscoped package with `--access restricted` is an error.

  ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --access public
  ```

  `--access` can also be set in the `publishConfig` field of your `package.json`.

  ```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
  {
    "publishConfig": {
      "access": "restricted" // [!code ++]
    }
  }
  ```
</ParamField>

<ParamField type="string">
  Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

  ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --tag alpha
  ```

  `--tag` can also be set in the `publishConfig` field of your `package.json`.

  ```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
  {
    "publishConfig": {
      "tag": "next" // [!code ++]
    }
  }
  ```
</ParamField>

<ParamField type="boolean">
  Simulate the publish process without publishing the package, to verify its contents first.

  ```sh theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --dry-run
  ```
</ParamField>

<ParamField type="string">
  Specify the level of gzip compression to use when packing the package. Only applies to `bun publish` without a tarball
  path argument. Values range from `0` to `9` (default is `9`).
</ParamField>

<ParamField type="string">
  If you have 2FA enabled for your npm account, `bun publish` prompts you for a one-time password, either through a browser or the CLI. `--auth-type` tells the npm registry which method you prefer: `web` (the default) or `legacy`.

  ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --auth-type legacy
  ...
  This operation requires a one-time password.
  Enter OTP: 123456
  ...
  ```
</ParamField>

<ParamField type="string">
  Provide a one-time password directly to the CLI. A valid password skips the extra one-time password prompt before publishing.

  ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --otp 123456
  ```

  <Note>
    `bun publish` respects the `NPM_CONFIG_TOKEN` environment variable, so you can publish from GitHub Actions or other
    automated workflows.
  </Note>
</ParamField>

### Registry Configuration

#### Custom Registry

<ParamField type="string">
  Specify registry URL, overriding .npmrc and bunfig.toml
</ParamField>

```bash theme={"theme":{"light":"github-light","dark":"dracula"}}
bun publish --registry https://my-private-registry.com
```

#### SSL Certificates

<ParamField type="string">
  Provide Certificate Authority signing certificate
</ParamField>

<ParamField type="string">
  Path to Certificate Authority certificate file
</ParamField>

<CodeGroup>
  ```bash Inline Certificate theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --ca "-----BEGIN CERTIFICATE-----..."
  ```

  ```bash Certificate File theme={"theme":{"light":"github-light","dark":"dracula"}}
  bun publish --cafile ./ca-cert.pem
  ```
</CodeGroup>

### Publishing Options

#### Dependency Management

<ParamField type="boolean">
  Don't install devDependencies
</ParamField>

<ParamField type="string">
  Exclude dependency types: `dev`, `optional`, or `peer`
</ParamField>

<ParamField type="boolean">
  Always request the latest versions from the registry & reinstall all dependencies
</ParamField>

#### Script Control

<ParamField type="boolean">
  Skip lifecycle scripts during packing and publishing
</ParamField>

<ParamField type="boolean">
  Add packages to trustedDependencies and run their scripts
</ParamField>

<Note>
  **Lifecycle Scripts** — When you publish a pre-built tarball, Bun does not run lifecycle scripts such as
  `prepublishOnly` and `prepack`; they only run when Bun packs the package itself.
</Note>

#### File Management

<ParamField type="boolean">
  Don't update package.json or lockfile
</ParamField>

<ParamField type="boolean">
  Disallow changes to lockfile
</ParamField>

<ParamField type="boolean">
  Generate yarn.lock file (yarn v1 compatible)
</ParamField>

#### Performance

<ParamField type="string">
  Platform optimizations: `clonefile` (default), `hardlink`, `symlink`, or `copyfile`
</ParamField>

<ParamField type="number">
  Maximum concurrent network requests
</ParamField>

<ParamField type="number">
  Maximum concurrent lifecycle scripts (default: 2x CPU cores)
</ParamField>

#### Output Control

<ParamField type="boolean">
  Suppress all output
</ParamField>

<ParamField type="boolean">
  Show detailed logging
</ParamField>

<ParamField type="boolean">
  Hide progress bar
</ParamField>

<ParamField type="boolean">
  Don't print publish summary
</ParamField>
