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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.6.1" sh
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

| Filename (v3.6.1)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-e12a52a68a9870219c60741e71741a06d1896e85cc7c96fffe1e75f9933d4804` |
| sentry-cli-Darwin-universal                                                                              | `sha384-25f0cea3ad39690082c8c5df7a98eac068d7fcbec933f4cb2acecf914a105106` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-8117129416afef14deec082e205abe77707f3189ed826718a338e24c5a190838` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-ea17bcce48fd8a252174db9743503b967351c1ed498c296fdfa40b4cb609bbc5` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-4554398346e78c6c7145c1e790e686b6afb18b3618a84ef1fcd5ebe5f5ec4f72` |
| sentry-cli-Linux-i686                                                                                    | `sha384-097ffb42a386363c6052e65b3eede52f081e3b391fba5c1a24ebf05e39678f25` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-e25efd0278e2576d531fa9931faf61f6f0f6cda99024b55f694fb2588297f653` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-b98dd81b23ab844fb1ddbf66a147aad11f3cb917532f87c019e37ffa6715bfd4` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-60f0119ae60453de9633c9519c55ed0b39dcacb05d7871a52a6a6c5af66041c0` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-47e886ffdfcfe03f6f710667d1236ddf58b5ff6ade2d7cead8fe392d91959861` |
| sentry\_cli-3.6.1-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-97b6a23eec09a8f897ca27168f76b966e9b46c587827b936c636bdd355d51f42` |
| sentry\_cli-3.6.1-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-a1e91d0fac5ba73ae1eedd56ba344304b4d5de43ec9e67e00c516fbc3b0a5133` |
| sentry\_cli-3.6.1-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-4977161b74072505aaa29c75240292abfc5f69add85a22181bed700141d4e82e` |
| sentry\_cli-3.6.1-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-1a377dfc9a48fbb7e16ea917715a05699cf5978e6ea59013839780e92b38c242` |
| sentry\_cli-3.6.1-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-13e292d2901dd45a71d28b1212a0f796cdc5409cbfced04e99d64ff8f9eea3c2` |
| sentry\_cli-3.6.1-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-68c5e18da7e04ab1220b4581b9422ee03ed90f3c7773f7a3bd76ef62037b3748` |
| sentry\_cli-3.6.1-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-09aa60b6cf4b7b87150d9d1ba51f9cb2da2357a971100858571154d5b2f26572` |
| sentry\_cli-3.6.1-py3-none-win32.whl                                                                     | `sha384-b44d6fb3201dd1ba8aa36226f23975217809a55ace3b9ab1208091a9337ec567` |
| sentry\_cli-3.6.1-py3-none-win\_amd64.whl                                                                | `sha384-3ac47ea4c638dfdbca5d6ca8ba5c7c19327ffc96579930102625927f14132c00` |
| sentry\_cli-3.6.1-py3-none-win\_arm64.whl                                                                | `sha384-e76da67810b9786edff49ec9a7dfeff9aca5f4e793ab7adb6bf33cc4d905d80a` |
| sentry\_cli-3.6.1.tar.gz                                                                                 | `sha384-becab1f84f1d6a7c3df19f9d147d6a94d84deba19416aa6f4e726be5fb6369d4` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

