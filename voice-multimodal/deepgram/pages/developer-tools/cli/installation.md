---
title: "CLI installation"
source: https://developers.deepgram.com/developer-tools/cli/installation.md
path: developer-tools/cli/installation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# CLI installation

## macOS and Linux

```shell
curl -fsSL https://deepgram.com/install.sh | sh
```

The script detects your OS, uses an available Python package manager, and installs the `dg` command on your PATH. The CLI requires Python 3.10 or later.

## Windows

In PowerShell:

```powershell
iwr https://deepgram.com/install.ps1 -useb | iex
```

## Package managers

### Homebrew

On macOS and Linux:

```shell
# Install and trust only the Deepgram formula
brew install deepgram/tap/deepgram
```

The fully qualified name installs the CLI from Deepgram's official tap (`deepgram/homebrew-tap`) without trusting the rest of the tap. To upgrade later, run `brew upgrade deepgram`.

Homebrew also installs `ffmpeg` and `portaudio`, so `dg listen --mic`, `dg debug probe`, and raw audio piping work with no further setup.

Run `dg --version` to see the installed version; the install script and `pip` install the latest release from PyPI. `brew upgrade deepgram` upgrades the `deepgram` formula itself, not a stray `deepctl` one.

### pip

```shell
pip install deepctl
```

### pipx

```shell
pipx install deepctl
```

### uv

```shell
uv tool install deepctl
```

### npm

```shell
npm install -g @deepgram/cli
```

This installs `@deepgram/cli`, a Node launcher package that provisions a Python backend for you. `dg --version` reports the same `deepctl, version <version>` string as any other install method.

Node.js 20 or later runs the launcher. The launcher itself needs one of `uv` or Python 3.10 to 3.14 with `venv` already on the machine to build that Python backend; see the [npm package's README](https://www.npmjs.com/package/@deepgram/cli) for the one-time setup it performs. Setup installs prebuilt wheels only, so it fails with "no matching distribution" on Intel Macs and Windows on ARM64, where `cryptography` ships no wheel; install with Homebrew, pipx, or uv instead on those platforms.

## Try without installing

Run the CLI once from a temporary environment:

```shell
# Run with uv
uvx deepctl --help
# Run with pipx
pipx run deepctl --help
```

## Verify installation

```shell
dg --version
dg --help
```

`dg`, `deepctl`, and `deepgram` are the same command. `dg --version` prints the installed version, in the form `deepctl, version <version>`.

## Update

`dg update` detects how the CLI was installed (pip, pipx, uv, npm, Homebrew, or a virtual environment) and runs the matching upgrade:

```shell
# Check and install the latest release
dg update
# Check without installing
dg update --check-only
# Skip the confirmation prompt
dg update -y
# Reinstall even when already current
dg update --force
```

To upgrade through the install script, pass `--force`: `curl -fsSL https://deepgram.com/install.sh | sh -s -- --force`. On Windows, set `$env:DEEPCTL_FORCE='1'` before running the PowerShell line. Without `--force`, a re-run keeps the installed version.

Each package manager also upgrades the CLI directly:

```shell
# Homebrew
brew upgrade deepgram
# pip
pip install --upgrade deepctl
# uv
uv tool upgrade deepctl
# pipx
pipx upgrade deepctl
```

If `dg update` prints `Please update using apt` for a CLI you installed with `pip` as root, run `pip install --upgrade deepctl`.

The CLI also checks for updates on a schedule set by `update.check_frequency` (`daily`, `weekly`, or `never`); turn the check off with `update.check_enabled: false`. See [Configuration & Environment](/developer-tools/cli/configuration).

## Uninstall

```shell
# Homebrew
brew uninstall deepgram
# pip
pip uninstall deepctl
# uv
uv tool uninstall deepctl
# pipx
pipx uninstall deepctl
```

## Requirements

* Python 3.10 or later
* `ffmpeg` for audio processing (Homebrew installs it automatically)
* `dg listen --mic` on Linux with pip, pipx, or uv: install the PortAudio library (`sudo apt install libportaudio2` on Debian and Ubuntu). Homebrew installs it.

## Telemetry

By default, `dg` has no telemetry destination built in, so a command sends nothing: not usage data, not a hostname, nothing, because there's nowhere for it to go. `dg <command> --help` ends with the current state, for example `This version of dg sends no telemetry.`

Telemetry activates only if you set `DEEPCTL_TELEMETRY_DSN` to a loopback address (`localhost` or a loopback IP), which exists for tests and local sinks. A non-loopback value is ignored rather than allowed to redirect reports anywhere else, so there's no way to point a production `dg` at a remote destination. Even with a loopback DSN set, it reports only unhandled exceptions the CLI itself can't catch, never ordinary command usage, timing, or a hostname. A reported exception's payload is small and fixed: the exception type and one stack frame (module, function, and line number only; a module the CLI doesn't own is reported as `<other>`, never by its real name), four tags (`cli.os`, `cli.arch`, `cli.python`), the CLI version, and a timestamp. It carries no message text, no local variables, no source lines, and no user data.

With a DSN set, several settings turn it back off:

* `DEEPCTL_TELEMETRY=log` writes the report to stderr instead of sending it over the network.
* `DEEPCTL_TELEMETRY=off`, `DEEPCTL_TELEMETRY_DISABLED=1`, `DO_NOT_TRACK=1`, or `CI=true` all disable it.
* `--no-telemetry` disables it too; with no DSN set, the flag has no effect, since there's nothing to turn off.
* `telemetry.enabled: false` in your deepctl `config.yaml` ([Configuration & Environment](/developer-tools/cli/configuration) lists its path on each OS) disables it as well.

`dg <command> --help` always ends with the current setting, for example `Telemetry is on: unexpected errors only, with no flag values, paths or keys.` or `Telemetry is off.`
