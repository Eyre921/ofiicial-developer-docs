---
title: "Installation"
source: https://docs.turso.tech/cli/installation
path: cli/installation
---

Learn how to install the Turso CLI on Mac, Linux and Windows.

## macOS

To install the Turso CLI on macOS, we recommend that you use Homebrew:

```bash theme={null}
brew install tursodatabase/tap/turso
```

If you don't use Homebrew, you can use the following command to execute a shell script that installs the CLI:

```bash theme={null}
curl -sSfL https://get.tur.so/install.sh | bash
```

## Linux

Run the following command to execute a shell script that installs the CLI:

```bash theme={null}
curl -sSfL https://get.tur.so/install.sh | bash
```

## Windows

Installing the Turso CLI on Windows requires that you have [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) installed.

Once WSL is installed, run the following in PowerShell:

```bash theme={null}
wsl
```

You can then execute the script to install the Turso CLI:

```bash theme={null}
curl -sSfL https://get.tur.so/install.sh | bash
```

## Verify installation

You must open a new shell to verify the installation with the following command:

```bash theme={null}
turso
```
