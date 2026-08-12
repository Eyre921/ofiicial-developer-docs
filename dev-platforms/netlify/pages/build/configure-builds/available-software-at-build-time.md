---
title: "Netlify Build Software"
source: https://docs.netlify.com/build/configure-builds/available-software-at-build-time.md
path: build/configure-builds/available-software-at-build-time
---

---
title: 'Available software at build time'
description: 'Learn about the software and tools that are available for your builds at build time.'
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

These are the languages and tools available to your build during the build process.

Our current build is based on Ubuntu version 24.04 (also called Noble Numbat) and includes the languages and software versions listed below.

There are multiple ways to set the software and language version used for your builds. Learn more about [managing your build dependencies](/build/configure-builds/manage-dependencies).

## Languages

<div class="software-table-wrapper">

| | Default version | Available versions | Set the version using |
| --- | --- | --- | --- |
| [Node.js](https://nodejs.org/en) | `24` | Any version that `nvm` can install | In order of precedence: `.nvmrc` file, `.node-version` file, `NODE_VERSION` build environment variable, or the 
### NavigationPath Component:

Dependency management
 section in the Netlify UI. For example, a node version set in `.nvmrc` will override the node version set in the Netlify UI. |
| [Ruby](https://www.ruby-lang.org/en/) | `3.x` | Any [official Ruby version](https://www.ruby-lang.org/en/downloads/releases/) | Build environment variable `RUBY_VERSION` or `.ruby-version` file |
| [Python](https://www.python.org/) | `3.x` | Any [official Python version](https://www.python.org/downloads/) | Build environment variable `PYTHON_VERSION`, `Pipfile` file, or `runtime.txt` file |
| [PHP](https://www.php.net/) |  | `7.4`, `8.0`, `8.1`, `8.2`, `8.3` | Build environment variable `PHP_VERSION` |
| [Go](https://go.dev/) | `1.x` | Any [official Go version](https://golang.org/dl/) | Build environment variable `GO_VERSION` |
| [Java](https://www.java.com/en/)  | `25` |  |  |
| [Elixir](https://elixir-lang.org/) | `1.9.1` |  |  |
| [Emacs](https://www.gnu.org/software/emacs/) | `26.3` |  |  |
| [Erlang](https://www.erlang.org/) | `22.2` |  |  |
| [Swift](https://developer.apple.com/swift/) | `N/A` | Any version that `swiftenv` can install `>= 5.0` | Build environment variable `SWIFT_VERSION`, or <br/> `.swift-version` file |
| [Rust](https://www.rust-lang.org/) | `N/A` | Any version that `rustup` can install | `Cargo.toml` file |

</div>

## Tools

<div class="software-table-wrapper">

|  | Available versions | Set the version using |
| --- | --- | --- |
| [Bun](https://bun.sh/) | `1.x` | Build environment variable `BUN_VERSION` |
| [Cask](https://cask.readthedocs.io/en/latest/) | `latest` | |
| [Composer](https://getcomposer.org/) | `latest` | |
| [Deno](https://deno.com/) | `1.x` | |
| [Doxygen](http://www.doxygen.org) | `1.9.8` | |
| [GNU Make](https://www.gnu.org/software/make/) | `4.3` | |
| [Hugo](https://gohugo.io/) | [Any version](https://github.com/gohugoio/hugo/releases) | Build environment variable `HUGO_VERSION` |
| [Leiningen](https://leiningen.org/) | `stable` | |
| [libvips](https://www.libvips.org) | `8.15.1` | |
| [npm](https://www.npmjs.com/) | Corresponds with the installed Node.js version. | Build environment variable `NPM_VERSION` |
| [pip](https://pip.pypa.io/en/stable/) | Corresponds with the installed Python version. | |
| [Pipenv](https://pipenv.pypa.io/en/latest/) | Corresponds with the installed Python version. Defaults to `latest` | |
| [pnpm](https://pnpm.io/) | Any version corepack can install. Defaults to `10.x` | `packageManager` field in your `package.json` file |
| [Yarn](https://classic.yarnpkg.com/lang/en/) | Any version corepack can install. Defaults to `1.x` | `packageManager` field in your `package.json` file |
| [Zola](https://www.getzola.org/) | [Any version](https://github.com/getzola/zola/releases) | Build environment variable `ZOLA_VERSION` |

</div>

## Request support for a language or tool

We love hearing from you and using your input to help us build a better web! Let us know about any missing tools and languages. 

You can reach us by opening a new request on [our Forums](https://answers.netlify.com/c/features/50).

## Report a bug

If you find an issue, let our support team know by opening a [support request](https://answers.netlify.com/c/netlify-support/48) in our Forums.

For anything else,  you can use the Docs feedback form on the bottom of this docs page as well to provide us feedback and tell us how we can improve!

