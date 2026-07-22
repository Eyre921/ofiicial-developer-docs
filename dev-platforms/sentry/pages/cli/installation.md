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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.6.2" sh
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

| Filename (v3.6.2)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-5a497deb1e388cc6445c09ddd6d2da4fc2aae8295405d6393c2e0ee635ca3687` |
| sentry-cli-Darwin-universal                                                                              | `sha384-d1339bc39b2c681496d70fc0cb5263a6f4ff93939de21b1f34cffb310643ef1c` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-efe0a5289cdd0ea8ff727b1228a1bea6c840f2da38152e8f9f5ced05bd6659cd` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-ff112ecf694b7d6b3629a6228ed4e3f7a0d51401bdf48a5051a79d8749dccd06` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-70a92a11d2d4d0c08202158120c0c054e83b6a5b5aff467e4a04cb19ca5440d9` |
| sentry-cli-Linux-i686                                                                                    | `sha384-d1acfe1ab476c81dd2cc101e541e00403da7dcdf1cf21f4f2cfbe7353637b1de` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-3a4bbf2c0d06378d4e59b337647483751a0a2b1603db5fd4991847d0cfd6478c` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-93ee7916c05c113a35daccf107c034af96f279561c103aa832668e4eecca3fb4` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-e1f1a2d82425d0655bc8461fd37ded91f490c82fc60429066b9d844825d319e3` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-5c90cb0045cef3d3c36113c2aa21a7dcae11627d2d6e3098b679dea5b6681be3` |
| sentry\_cli-3.6.2-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-b5f93ed3249a1a52e8fe203d7e2886206bc13899a0621d80fce157b5f5062737` |
| sentry\_cli-3.6.2-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-6010960e0728cc43c4ec8222e73b0cba53c12e4f2efa40706bf253b7e2d51b0f` |
| sentry\_cli-3.6.2-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-cd6552bb35ff5ff734e953a8b7f8e7934c9cafdd482a0d0695e66e3ffb6ecce0` |
| sentry\_cli-3.6.2-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-8a1901112725926ce56151c94076bcd053473c84c813defbc391008bc2a8308c` |
| sentry\_cli-3.6.2-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-54ac0c40efb8d1f708a738b52db53782272a444314be37517fa1021a4aba2016` |
| sentry\_cli-3.6.2-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-5be2fee0e7dc5f2d2ee1ea095ee63f7410f4d4bb54a2e9f1ec7dcd9f60417667` |
| sentry\_cli-3.6.2-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-ecc607560ddefe9ecf4343455c972b5fdbe77713a11ffa07288ff174afe824b3` |
| sentry\_cli-3.6.2-py3-none-win32.whl                                                                     | `sha384-df9b862f170f11b161535a8d07f4c263399b548eba83bf4c391f944b68ad3b4a` |
| sentry\_cli-3.6.2-py3-none-win\_amd64.whl                                                                | `sha384-ff25968b7a0d4bb1f1398c7981df8c5a9526a8632545e5c651f6e1cda02ab2b5` |
| sentry\_cli-3.6.2-py3-none-win\_arm64.whl                                                                | `sha384-5b32e20bcf91d5cd02ee627c0cd31cdc8a0f559bf8c63341104d677ad013828f` |
| sentry\_cli-3.6.2.tar.gz                                                                                 | `sha384-ffee0c936bd671fc3b60f7c2a90e1c45c3b64fd6caff803a6090592c5707e4b2` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

