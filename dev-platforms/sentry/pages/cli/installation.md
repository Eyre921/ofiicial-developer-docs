---
title: "Installation"
source: https://docs.sentry.io/cli/installation.md
path: cli/installation
---

---
title: "Installation"
description: "Learn about the different methods available to install `sentry-cli`."
url: https://docs.sentry.io/cli/installation/
---

# Installation

##### Looking for the new Sentry CLI?

These docs cover `sentry-cli`, used in CI/CD pipelines and build processes. If you're looking for the interactive developer CLI with issue management, AI-powered analysis, and API access for humans and agents, check out the new [Sentry CLI](https://cli.sentry.dev/).

Depending on your platform, there are different methods available to install `sentry-cli`.

## [Manual Download](https://docs.sentry.io/cli/installation.md#manual-download)

You can find the list of releases on [the GitHub release page](https://github.com/getsentry/sentry-cli/releases/). We provide executables for Linux, OS X and Windows. It’s a single file download and upon receiving the file you can rename it to just `sentry-cli` or `sentry-cli.exe` to use it.

## [Automatic Installation](https://docs.sentry.io/cli/installation.md#automatic-installation)

If you are on macOS or Linux, you can use the automated downloader which will fetch the latest release version for you and install it:

```bash
curl -sL https://sentry.io/get-cli/ | sh
```

We do however, encourage you to pin the specific version of the CLI, so your builds are always reproducible. To do that, you can use the exact same method, with an additional version specifier:

```bash
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.6.0" sh
```

This will automatically download the correct version of `sentry-cli` for your operating system and install it. If necessary, it will prompt for your admin password for `sudo`. For a different installation location or for systems without `sudo` (like Windows), you can `export INSTALL_DIR=/custom/installation/path` before running this command.

To verify it's installed correctly you can bring up the help:

```bash
sentry-cli --help
```

## [Installation via NPM](https://docs.sentry.io/cli/installation.md#installation-via-npm)

There is also the option to install `sentry-cli` via npm for specialized use cases. This, for instance, is useful for build servers. The package is called `@sentry/cli` and in the post installation it will download the appropriate release binary:

```bash
npm install @sentry/cli
```

*Other available variations of the above snippet: yarn, pnpm*

You can then find it in the `.bin` folder:

```bash
./node_modules/.bin/sentry-cli --help
```

In case you want to install this with npm system wide with sudo you will need to pass `--unsafe-perm` to it:

```bash
sudo npm install -g @sentry/cli --unsafe-perm
```

This installation is not recommended however.

### [Downloading From a Custom Source](https://docs.sentry.io/cli/installation.md#downloading-from-a-custom-source)

By default, this package will download sentry-cli from the CDN managed by [Fastly](https://www.fastly.com/). To use a custom CDN, set the npm config property `sentrycli_cdnurl`. The downloader will append `"/<version>/sentry-cli-<dist>"`.

```bash
npm install @sentry/cli --sentrycli_cdnurl=https://mymirror.local/path
```

Or add property into your `.npmrc` file (<https://docs.npmjs.com/files/npmrc>)

```bash
sentrycli_cdnurl=https://mymirror.local/path
```

Another option is to use the environment variable `SENTRYCLI_CDNURL`.

```bash
SENTRYCLI_CDNURL=https://mymirror.local/path npm install @sentry/cli
```

### [Available Installation Options](https://docs.sentry.io/cli/installation.md#available-installation-options)

Options listed below control how `sentry-cli` install script behaves, when installed through `npm`.

`SENTRYCLI_CDNURL`:

If set, the script will use given URL for fetching the binary. Defaults to `https://downloads.sentry-cdn.com/sentry-cli`.

`SENTRYCLI_USE_LOCAL`:

If set to `1`, `sentry-cli` binary will be discovered from your `$PATH` and copied locally instead of being downloaded from external servers. It will still verify the version number, which has to match.

`SENTRYCLI_SKIP_DOWNLOAD`:

If set to `1`, the script will skip downloading the binary completely.

`SENTRYCLI_SKIP_CHECKSUM_VALIDATION`:

If set to `1`, the script will skip the checksum validation phase. You can manually verify the checksums by visiting [Build Checksums](https://docs.sentry.io/cli/installation.md#build-checksums) page.

`SENTRYCLI_NO_PROGRESS_BAR`:

If set to `1`, the script will not display download progress bars. This is a default behavior for CI environments.

`SENTRYCLI_LOG_STREAM`:

If set, the script will change where it writes its output. Possible values are `stdout` and `stderr`. Defaults to `stdout`.

## [Installation via Homebrew](https://docs.sentry.io/cli/installation.md#installation-via-homebrew)

If you are on OS X, you can install `sentry-cli` via homebrew:

```bash
brew install getsentry/tools/sentry-cli
```

## [Installation via Scoop](https://docs.sentry.io/cli/installation.md#installation-via-scoop)

If you are on Windows, you can install `sentry-cli` via [Scoop](https://scoop.sh):

```powershell
> scoop install sentry-cli
```

## [Docker Image](https://docs.sentry.io/cli/installation.md#docker-image)

For unsupported distributions and CI systems, we offer a Docker image that comes with `sentry-cli` preinstalled. It is recommended to use the `latest` tag, but you can also pin to a specific version. By default, the command runs inside the `/work` directory. Mount relevant project folders and build outputs there to allow `sentry-cli` to scan for resources:

```bash
docker pull getsentry/sentry-cli
docker run --rm -v $(pwd):/work getsentry/sentry-cli --help
```

## [Updating and Uninstalling](https://docs.sentry.io/cli/installation.md#updating-and-uninstalling)

You can use `sentry-cli update` and `sentry-cli uninstall` to update or uninstall the `sentry-cli` binary. These commands may be unavailable in certain situations, generally when `sentry-cli` has been installed by a tool like homebrew or yarn, either directly or as a dependency of another package. In those cases, the same tool will need to be used for updating and removal. If you find that `sentry-cli update` and `sentry-cli uninstall` aren't working and you don't know how the package was installed, running `which sentry-cli` will often provide a clue as to which tool to use.

## [Build Checksums](https://docs.sentry.io/cli/installation.md#build-checksums)

When downloading an executable from a remote server, it's often a good practice to verify, that what has been downloaded, is in fact what we expect it to be. To make sure that this is the case, we can use checksum validation. A checksum is the value calculated from the contents of a file, in a form of hash, in our case SHA256, and it acts as the data integrity check, as it's always producing the same output, for a given input.

Below is the table of SHA256 checksums for all available build targets that our CLI supports. To calculate the hash of a downloaded file, you can use `sha256sum` utility, which is preinstalled in OSX and most Linux distributions.

| Filename (v3.6.0)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-912252729231a1e35dcbd948a5ea23ef5f163e59c4f183d7847fb22d1aedbd49` |
| sentry-cli-Darwin-universal                                                                              | `sha384-6aa4a42c8cf8591fe5e24cb62370dcfa40d84973bbb0f4725138eb47bb986e32` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-8c2470b92ae409d42f1d6697774457bbfa0222049b527b907a2f8a26e5b4e98e` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-987ab96a45610f00659a0ee633e64343495312e8c39250242dab12aa296240a2` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-98c6008651dda9ce2a8cec7fe635a3f00a563f49faf36b62afccc6af106befb0` |
| sentry-cli-Linux-i686                                                                                    | `sha384-7d0095ccd85d9ec9f3a4242dc86b317fe626da4aeac524eccd55856ec127e0d0` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-e2bff5d8b546f3fb72c616da656ecb347c7c144f36a5294b0749dcc2001f68d5` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-e6c355e99781e5480ee7dcc11b75e27fe92a43e7490af0fe299100163a03b1ca` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-5ad9cf27de932e7a519cbbf1d4f73d28151e8c3da6119bc9e66659dad3558bcc` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-8a617dff234dcda4ce600cef3b14874454dd907f63395a9c470c5a7120c867f6` |
| sentry\_cli-3.6.0-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-0e4e1e38b75196f82142164263f8a0878677b722bd1a2394bc9e46aa967f5a30` |
| sentry\_cli-3.6.0-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-72707eefc9f183eca478ef5fd98182bba5f1ddc030c37ad41f335a9854f2c69f` |
| sentry\_cli-3.6.0-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-7f6c328ded34622b3394786a82e6a24f27eed350b7f58f42bf58b6f775289061` |
| sentry\_cli-3.6.0-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-aa2c07a688a1dff95666c738bb5de12b5846467d2588f0593ff3a0c9c3151fc7` |
| sentry\_cli-3.6.0-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-9a25ec6ec3b096f1109eb2ee972721ac04aa8562505b1084d795ab8c83fab46e` |
| sentry\_cli-3.6.0-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-dc91bbed308abf932fcd4a72f9b84172acf35cb52bff7d0d978635fb02e3ef10` |
| sentry\_cli-3.6.0-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-86a6d763cb8205cc4896054d4834453ace36366c12c9f6a5e575d27e4e6c9cf0` |
| sentry\_cli-3.6.0-py3-none-win32.whl                                                                     | `sha384-22ebe33877f44c72c541bd161b9552f4d77bcc56abca25d4aa9e8bc5c6311419` |
| sentry\_cli-3.6.0-py3-none-win\_amd64.whl                                                                | `sha384-8a1b172923c84d2a2cc37b3f79e3e75e326118c6cc194499a33862a2576269e1` |
| sentry\_cli-3.6.0-py3-none-win\_arm64.whl                                                                | `sha384-bdc641937b42f444184f925d43a278c2c446483c8f1923d0bc41c9a68cee39dc` |
| sentry\_cli-3.6.0.tar.gz                                                                                 | `sha384-a7149c0c95337c7e431fc8597383ab3f80c51848032352954d3495f0e23ae058` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

