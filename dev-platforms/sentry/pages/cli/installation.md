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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.8.0" sh
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

| Filename (v3.8.0)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-1dda212b0e168b9c4dc48d7d3aa24c1c37de9c6edf786e6ae661236e529969cd` |
| sentry-cli-Darwin-universal                                                                              | `sha384-2c26914636c47ab9bf9e710484ad7b44d371cbec8bd29cafb36b3cf877bf4285` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-279c795b15de7a76106d30b6611b7942b1a97323307327bafc18335f10384c4d` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-eaea24b5b47b61a96d9a2e353268ea41fd9a8c5b7979694330df614d4af672bf` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-f5cf9d6b3101f740f2d60c371c0a76330cb5072206216641edce72353e8cf503` |
| sentry-cli-Linux-i686                                                                                    | `sha384-ecbbc8e9b8050831cc1196edfc8df6d72660c4fdc7d844722ab6bc2a3a778173` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-13f8cb34ae01a6a272d7d7c22e277a105286615b4020de900ea95a8de47cdbb6` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-174786337bf2d3cd3386c14aab122ba3d3bbd49b98e124666b03f63f54e4104f` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-f10b90a1e62a81a5184a076ac097c6a31a56a0b493648d066948adb0691d6370` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-2257cf6805a616f5c3ee291a549ebbba021190048b646adc006beb4e8cdef7fd` |
| sentry\_cli-3.8.0-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-a189d9f29e224269b1183a6717727d5d3022f8ae8e4d07add4722d7120ce7140` |
| sentry\_cli-3.8.0-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-51aa27ef49081e56b8da50e4ff6420bce53af6ed914c5cb90929255c9f2e71ac` |
| sentry\_cli-3.8.0-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-275f9141cb3ac8fa0041b57c06a96983c1ec1a838717c90472add9e6ef0111fa` |
| sentry\_cli-3.8.0-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-3cf62b1fa957fe75579cb932a94a831bcee3ace9d4c7601148b16fc718408b0e` |
| sentry\_cli-3.8.0-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-6e1de5aaa2ce1e417840fa27dab3ee66fd19439c763f557a528445f4360b4a2e` |
| sentry\_cli-3.8.0-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-e4b6f175eb68b639c0536038733a6f767cc030d158ec6b76b2d4be08f1d9e55b` |
| sentry\_cli-3.8.0-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-9881d84e8a253fa2350ec82a70d14d6bf62e209289e532927746fd438d471e40` |
| sentry\_cli-3.8.0-py3-none-win32.whl                                                                     | `sha384-c425e144d253bcccc1cbaf7b3267058ac9e41decdc0a5981f27eff0f0c627acb` |
| sentry\_cli-3.8.0-py3-none-win\_amd64.whl                                                                | `sha384-10556ba78d255375fbecfacab46e5a4b60ac629a35f1df88e436fad8e9e91b1b` |
| sentry\_cli-3.8.0-py3-none-win\_arm64.whl                                                                | `sha384-1c67ad4b879606c057ea7f46c296753cd62e4acdf58e4730f160df310af5267f` |
| sentry\_cli-3.8.0.tar.gz                                                                                 | `sha384-cf9e4d68080dbdd8c3ba8d541f2097bb9648ab56b7abde8b5681461b4a40e4f7` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

