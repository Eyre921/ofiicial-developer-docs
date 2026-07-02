---
title: "Netlify Build Ignoring"
source: https://docs.netlify.com/build/configure-builds/ignore-builds.md
path: build/configure-builds/ignore-builds
---

---
title: "Ignore builds"
description: "Use default ignore builds behavior to avoid builds when they aren't required, or set an ignore command that determines when a site requires rebuilding."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

With continuous deployment, Netlify attempts to ignore builds when they're not required, only building when your site requires it.

Depending on your [**Branches** settings](/deploy/deploy-overview#branch-deploy-controls), any time there is a change in a linked repository, Netlify tries to determine whether there are changes in the site's [base directory](/build/configure-builds/overview#definitions-1) by comparing the last known version of the files in that directory. If no change is detected, the build system cancels and essentially skips the build, returning early from the build process.

To override the default behavior described above, you can use the `ignore` attribute in the [Netlify configuration file](/build/configure-builds/file-based-configuration). This setting allows you to specify a Node.js or Bash command that runs from the base directory and determines whether or not the site needs rebuilding.

## Custom `ignore` command

The `ignore` command provides custom, programmatic control over builds. It can prevent bot-triggered builds, for example, or limit production deploys to certain days of the week. It can also account for times when you may still want to run a build when there's a change outside of a base directory, for example, if there's a change to `package.json` in the root directory.

Things to note when constructing an `ignore` command:
- An exit code of `1` indicates the contents have changed and the build process continues as usual. An exit code of `0` indicates that there are no changes and the build should stop.
- The command is run with Bash. You can also [use Node.js](/build/configure-builds/ignore-builds#skip-builds-based-on-branch-name).
- If the command references a separate file, the file path must start with `./`.
- The `ignore` command won't cancel a build triggered by a [build hook](/build/configure-builds/build-hooks), regardless of exit code.
- Netlify can run an `ignore` command even if a [base directory](/build/configure-builds/overview#definitions-1) isn't set.
- All paths in your `ignore` command should be absolute paths relative to the [base directory](/build/configure-builds/overview#definitions), which is the root by default (`/`).

### `ignore` examples
Want to customize the default ignore behavior? Check out the examples of custom `ignore` commands below. For more `ignore` examples, head over to our verified Support Guide on [using the `ignore` command](https://answers.netlify.com/t/support-guide-how-to-use-the-ignore-command/37517).

#### Mimic default behavior
The Bash example below is an `ignore` command that roughly approximates the default ignore builds behavior. You can add to or adjust it to update the default check. The commands use read-only [environment variables for Git metadata](/build/configure-builds/environment-variables#git-metadata) as well as the `CI` and `NETLIFY` [build environment variables](/build/configure-builds/environment-variables).

``` toml
[build]
  ignore = "git diff --quiet $CACHED_COMMIT_REF $COMMIT_REF"
```

For this next example, consider a monorepo project set up like this, where `packages/blog-1` is the [package directory](/build/configure-builds/overview#definitions) and the base directory is the repository root (`/`), by default.

```
/
├─ package.json
└─ packages/
   ├─ blog-1/
   │  ├─ package.json
   │  └─ netlify.toml
   ├─ common/
   │  └─ package.json
   └─ blog-2/
      ├─ package.json
      └─ netlify.toml   
```

The following `ignore` command example adapts the default behavior so that the build proceeds only if there are changes within the `blog-1` or `common` directories.

``` toml
[build]
  ignore = "git diff --quiet $CACHED_COMMIT_REF $COMMIT_REF packages/blog-1 packages/common"
```

#### Skip builds based on branch name
The `ignore` command has access to a Node.js environment. This means if you want to prevent builds based on logic that's hard to handle in Bash, you can use Node.js.

This example skips builds for a specific branch by adding a Node.js script to the `ignore` command in `netlify.toml`.

``` toml
[build]
  ignore = "node ignore_build.js"
```

`ignore_build.js` executes before any build logs run. If the branch name is `debug`, the exit code is set to `0`, which stops the build.

``` js
// ignore_build.js
process.exitCode = process.env.BRANCH.includes("debug") ? 0 : 1
```

There are a few things you should keep in mind when using Node.js with an `ignore` command.
- [Node.js dependencies](/build/configure-builds/manage-dependencies#javascript-dependencies) from the site's `package.json` are not available.
- `ignore` commands use Node.js 18. This Node.js version can't be customized. This means if your site has a [custom Node.js version](/build/configure-builds/manage-dependencies#node-js-and-javascript), the custom version is not used in the `ignore` command.

## More build configuration resources

- [Common framework configurations](/build/frameworks/overview)
- [Monorepos](/build/configure-builds/monorepos)
- [JavaScript SPAs](/build/configure-builds/javascript-spas)

