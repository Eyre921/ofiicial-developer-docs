---
title: "Plugin system"
source: https://developers.deepgram.com/developer-tools/cli/plugins.md
path: developer-tools/cli/plugins
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Plugin system

A plugin adds commands to `dg`. It is a Python package published to PyPI under the `deepctl-` prefix; `dg plugin install` fetches it and `dg` picks up its commands on the next run.

## Install a plugin

```shell
dg plugin install <package-name>
```

Homebrew and system installations keep plugins in an isolated environment at `~/.deepctl/plugins/venv`; other installations may add them to the CLI environment. For a plugin not yet on PyPI, pass a git URL such as `git+https://github.com/<user>/deepctl-plugin-<name>.git`.

| Option              | Effect                                                                   |
| ------------------- | ------------------------------------------------------------------------ |
| `--version`, `-v`   | Install a specific version (on `dg plugin install`, `-v` is `--version`) |
| `--upgrade`, `-U`   | Upgrade if already installed                                             |
| `--pre`             | Include pre-release versions                                             |
| `--force-reinstall` | Reinstall even when installed                                            |
| `--index-url`       | Base URL of the Python package index                                     |
| `--extra-index-url` | Extra package index URLs                                                 |
| `--git URL`         | Install from a git repository URL                                        |
| `--editable`, `-e`  | Install in editable mode                                                 |

## List installed plugins

```shell
# Installed plugins
dg plugin list
# With details (on dg plugin list, -v is --verbose)
dg plugin list -v
```

## Update plugins

```shell
dg plugin update <package-name>
# Include pre-release versions
dg plugin update <package-name> --pre
```

## Remove a plugin

```shell
dg plugin remove <package-name>
# Skip the confirmation
dg plugin remove <package-name> -y
```

`dg plugin install`, `update`, and `remove` also refresh installed skills; a skills failure prints a warning on stderr and leaves the command's exit code unchanged. See [Skills](/developer-tools/cli/skills).

## Find plugins

Plugins are PyPI packages named `deepctl-plugin-<name>`; search PyPI for the prefix. The reference plugin is [`deepctl-plugin-example`](https://pypi.org/project/deepctl-plugin-example/). Install it with `dg plugin install deepctl-plugin-example` to get `dg example`. Its source is at [packages/deepctl-plugin-example](https://github.com/deepgram/cli/tree/main/packages/deepctl-plugin-example) in the CLI repository.

## Plugin development

A plugin exposes a `BaseCommand` class through the `deepctl.plugins` entry-point group. Copy the [example plugin](https://github.com/deepgram/cli/tree/main/packages/deepctl-plugin-example); it shows `get_arguments()` for options and flags, the `requires_auth`, `requires_project`, and `ci_friendly` attributes, and a `handle()` method that returns structured data for the output formatter.

```python
from typing import Any

# BaseCommand is the plugin contract; the other three are what dg hands every command
from deepctl_core import AuthManager, BaseCommand, Config, DeepgramClient


class MyCommand(BaseCommand):
    # name becomes the subcommand: dg mycommand
    name = "mycommand"
    help = "My plugin command"
    # requires_auth=False lets the command run before dg login
    requires_auth = False

    # handle() runs when the user invokes the command; return structured data for the output formatter,
    # or print and return None as this sample does
    def handle(
        self,
        config: Config,
        auth_manager: AuthManager,
        client: DeepgramClient,
        **kwargs: Any,
    ) -> None:
        print("Hello from my plugin!")
```

## Register a plugin

Name the package with the `deepctl-` prefix, depend on `deepctl-core`, and add the command to your package's `pyproject.toml`:

```toml
# Package metadata: the deepctl- prefix and the deepctl-core dependency
[project]
name = "deepctl-plugin-mycommand"
version = "0.1.0"
dependencies = ["deepctl-core>=0.1.10"]

# Register the command: the key is the dg subcommand, the value is the BaseCommand subclass
[project.entry-points."deepctl.plugins"]
mycommand = "my_plugin.command:MyCommand"
```

The entry-point key (`mycommand`) is the command name `dg` registers; the value is the import path of your `BaseCommand` subclass. The example plugin's [pyproject.toml](https://github.com/deepgram/cli/blob/main/packages/deepctl-plugin-example/pyproject.toml) is a complete reference.

## Publish to PyPI

1. Build the distribution: `python -m build` produces a wheel and an sdist in `dist/`.
2. Upload it: `python -m twine upload dist/*`. The [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) covers creating a PyPI account and API token.
3. Test the install path end to end: `dg plugin install deepctl-plugin-mycommand`, then `dg mycommand`.

Anyone can then install the package by name. Share it in the [Developer Spotlight](https://github.com/orgs/deepgram/discussions/categories/developer-spotlight) on GitHub Discussions.

## Security

* Plugins run with your user permissions
* Plugins have access to your API key
* Only install plugins from trusted sources
* Review plugin code before installing
