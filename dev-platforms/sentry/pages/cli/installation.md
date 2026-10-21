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

# Installation | Sentry Docs

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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.8.1" sh
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

| Filename (v3.8.1)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-b117c50c99371e68c21544fada0f5f90a713acda8b090fdeef648417b231ce51` |
| sentry-cli-Darwin-universal                                                                              | `sha384-fb8413278fc45bb0e149db0cb201d6e1a2f20883fde4dc96b45961ab22946c3e` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-6bee493e528e303d395221c17c38307dbe0974f6914a3700b8ff1986bcd629c6` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-95b4530ca3723d79def0928731534b75db0213130e8681892f19c4e57ab258f9` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-a8599f00dc0ecefaaed42927a851f1c77ae8161722087278f6d26a098b63ad3e` |
| sentry-cli-Linux-i686                                                                                    | `sha384-a7ecdca1601386b9aa6574d19f7a8032fbd2d30587b1288a61d7cd79a41ca46a` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-f08a638e6e979a3c4f9c230bdd496dd88e7a0a0847d3e704ad8a733b189bb029` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-2b8d6444dfb4a0bb1baf9fbc5a97fcb9cdea47677029131e0f8aa7038c7e6d4b` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-782c7fdec49aaef0fa511f7952a527cccf07388a855fd98b443f39c558835cc6` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-24d59d33f6c38d4e5a1ebf17f28c8d16a24c9640e226956b7da2fa575e2e5033` |
| sentry\_cli-3.8.1-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-4c342458a4cd9e5d8fca905e86e8d7a47bc552085cd72f7d9703d21301fe4c60` |
| sentry\_cli-3.8.1-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-bdeb656b09e5da5f15610443aef8301fc06dd57977d3f2dbe42a6c1cefd699f7` |
| sentry\_cli-3.8.1-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-0b25ce873efa7838c575ce911418ed483f2f2461f1c3bbe985dc0cf76321e40d` |
| sentry\_cli-3.8.1-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-68bd6e02874f7072b9e48ad9a7a94485662899ca332cae63dccb1924f2eb39ef` |
| sentry\_cli-3.8.1-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-4ee8d6a6622b15208146ab8b097494c815b62915e694fc6315be219479252751` |
| sentry\_cli-3.8.1-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-db89e17725938d5bf0ce52f7feb76cf794af5c50db452bb76185fd07fb01d748` |
| sentry\_cli-3.8.1-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-38b80d013d5f3726cd0742dfb78bebb1e7e077410efc5ac8c5b8c55027dda45f` |
| sentry\_cli-3.8.1-py3-none-win32.whl                                                                     | `sha384-ca476d4d5e0fa007326606aa83da16c83dbf3a3172e26e55cb41b8e5f1aeaf46` |
| sentry\_cli-3.8.1-py3-none-win\_amd64.whl                                                                | `sha384-64ac907d4a62c7b48d9356ef3a3a5b6c293fe065bad459a16f05e410a5e60664` |
| sentry\_cli-3.8.1-py3-none-win\_arm64.whl                                                                | `sha384-7e41303b513885e62810da7a3b248103ec9bcc65617f1be0c7ecdbc0e5727ace` |
| sentry\_cli-3.8.1.tar.gz                                                                                 | `sha384-ae8d2639fd0ca17da33842400440259ae6cd6b36fe774e9e9da88cd06751c581` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

