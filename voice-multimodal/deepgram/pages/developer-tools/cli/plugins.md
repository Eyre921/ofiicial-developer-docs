---
title: "Plugin System"
source: https://developers.deepgram.com/developer-tools/cli/plugins.md
path: developer-tools/cli/plugins
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Plugin System

The `dg` CLI supports plugins that add new commands and capabilities.

## Install a Plugin

```shell
dg plugin install <package-name>
```

Plugin installation follows the CLI installation method. Homebrew and system installations use an isolated plugin environment; other installations may add plugins to the CLI environment.

## List Installed Plugins

```shell
dg plugin list
```

## Update Plugins

```shell
dg plugin update <package-name>
```

## Remove a Plugin

```shell
dg plugin remove <package-name>
```

## Example Plugins

Search for available plugins:

```shell
dg plugin search <keyword>
```

## Plugin Development

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

## Register a Plugin

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
