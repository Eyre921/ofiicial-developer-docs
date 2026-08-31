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

Plugins are installed in an isolated virtual environment.

## List Installed Plugins

```shell
dg plugin list
```

## Update Plugins

```shell
dg plugin update
dg plugin update <package-name>
```

## Uninstall a Plugin

```shell
dg plugin uninstall <package-name>
```

## Example Plugins

Search for available plugins:

```shell
dg plugin search <keyword>
```

## Plugin Development

Plugins are Python packages that expose CLI commands:

```python
# my-dg-plugin/my_plugin/__init__.py
from deepgram_cli.plugins import hookimpl
import click

@hookimpl
def register_commands(cli_group):
    @cli_group.command()
    def mycommand():
        """My custom command"""
        click.echo("Hello from my plugin!")
```

## Plugin Configuration

Plugins can read from your Deepgram config:

```python
from deepgram_cli.config import get_config

config = get_config()
api_key = config.get("api_key")
```

## Trusted Plugins

Mark a plugin as trusted (skips confirmation prompts):

```shell
dg plugin trust <package-name>
```

## Security

* Plugins run with your user permissions
* Plugins have access to your API key
* Only install plugins from trusted sources
* Review plugin code before installing
