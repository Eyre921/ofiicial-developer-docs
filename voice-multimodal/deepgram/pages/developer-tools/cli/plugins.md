---
title: "Plugin system"
source: https://developers.deepgram.com/developer-tools/cli/plugins.md
path: developer-tools/cli/plugins
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Plugin system

The `dg` CLI supports plugins that add new commands and capabilities.

## Install a plugin

```shell
dg plugin install <package-name>
```

Plugin installation follows the CLI installation method. Homebrew and system installations use an isolated plugin environment; other installations may add plugins to the CLI environment.

## List installed plugins

```shell
dg plugin list
```

## Update plugins

```shell
dg plugin update <package-name>
```

## Remove a plugin

```shell
dg plugin remove <package-name>
```

## Example plugins

Search for available plugins:

```shell
dg plugin search <keyword>
```

## Plugin development

Plugins are Python packages that expose a `BaseCommand` class through the `deepctl.plugins` entry-point group:

```python
from typing import Any

from deepctl_core import AuthManager, BaseCommand, Config, DeepgramClient


class MyCommand(BaseCommand):
    name = "mycommand"
    help = "My plugin command"
    requires_auth = False

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

Add the command to your package's `pyproject.toml`:

```toml
[project.entry-points."deepctl.plugins"]
mycommand = "my_plugin.command:MyCommand"
```

## Security

* Plugins run with your user permissions
* Plugins have access to your API key
* Only install plugins from trusted sources
* Review plugin code before installing
