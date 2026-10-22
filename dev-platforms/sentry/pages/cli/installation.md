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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.8.2" sh
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

| Filename (v3.8.2)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-c80d92b6d34eb64fe7402f56cc7968fbb15aab1c763254ad428b55cc98ec7dcf` |
| sentry-cli-Darwin-universal                                                                              | `sha384-2d1b118fa46960ba5e8e0cca9a6e197366905776a0ddc5a89c7d05a3908b77db` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-084591ee1f0a43ba8696ccde30d4a79cd9a70d0fa294c5a10143a340f8f332ff` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-b6e49fca868a36d20da2ada1832a0ce2f9ac7012c128207518b09d6b6c991f4d` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-10a5c414e298c5ad660eb8dbafde19c28ab1e03d35653cd59dbed35b9e1b05e5` |
| sentry-cli-Linux-i686                                                                                    | `sha384-eebb53cf4a0ebcbb526c269c189909d61f28a91e4de0f139a96e25552dcf9eec` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-c958865f9d4000183509ea21b1f04925d5390de6d8d87386b9e69f2b305070c3` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-3c197c61120e2d53a6ecfd9e7812d123bfdc598df1d569700bf5c3b936dfe891` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-e8d50ca10a77a1ca10996a1a957cdbaa9bab9f3efcc97de7460e0e0a000b2578` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-50009f23c49d6e9ff7624204c7035855303b49c5e326708ee783c1fdf783ac83` |
| sentry\_cli-3.8.2-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-678764a9a755a86b0735d4f1b8ff128d3d36cece622b4207c846f9ae1a9ac2be` |
| sentry\_cli-3.8.2-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-181f96f8ae2588f5a074a1932496c07ff67a69220c483361f7968490012f8301` |
| sentry\_cli-3.8.2-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-5fa03ff3c701c8d10981b31a89610a0e0d3cd3ba64d961a436fcb9fc170abe92` |
| sentry\_cli-3.8.2-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-3452f4ab97b2ed3f679bd83f0e23dacb7ac273bf541d103d4a2d8a09d1b71454` |
| sentry\_cli-3.8.2-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-7fc311657ea0b151bcc8cf98f65c42278ef0f02fe69046f86ad8f1de7a914797` |
| sentry\_cli-3.8.2-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-4ed114f47204f61013b08188783277257be57e9e8b5c3955bddd46b255c39097` |
| sentry\_cli-3.8.2-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-b05c7d91edf1e5d1afc82ef7f1e36d276e3979e5c59c3c9ea3489966800dfa00` |
| sentry\_cli-3.8.2-py3-none-win32.whl                                                                     | `sha384-87af9d2f88c2ccc02df1bceea4a209a465c7c481ee3b4aec7c4e5334b9846f7e` |
| sentry\_cli-3.8.2-py3-none-win\_amd64.whl                                                                | `sha384-bc98248daeb1f65b4636014e83c1e54771aa5abf9334cb60c49ee1e708824f3b` |
| sentry\_cli-3.8.2-py3-none-win\_arm64.whl                                                                | `sha384-4a00a72e13e5469646e71d903e554f2c139f90f8727084186344849cd379d287` |
| sentry\_cli-3.8.2.tar.gz                                                                                 | `sha384-cf87052c7538522511c292e02587bc882804217426f513aef6c568f3d148a74d` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

