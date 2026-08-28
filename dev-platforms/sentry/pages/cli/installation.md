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
curl -sL https://sentry.io/get-cli/ | SENTRY_CLI_VERSION="3.7.0" sh
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

| Filename (v3.7.0)                                                                                        | Integrity Checksum                                                        |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| sentry-cli-Darwin-arm64                                                                                  | `sha384-c66564094fbe56ee3b359f7574541f858b8d1df0328a0a759da972fbf1886048` |
| sentry-cli-Darwin-universal                                                                              | `sha384-10ccaaa39e6eee2b52034546f5f617533fdc76c64aa75c3038887045da1a367d` |
| sentry-cli-Darwin-x86\_64                                                                                | `sha384-fcd74786b4d95c6b7531662607897aadd5ab5d64c5d0468a6f4bd97ad04bedb8` |
| sentry-cli-Linux-aarch64                                                                                 | `sha384-69cc0e951f663a332fd3bb3069e443cb3748abbfce497ae2caac6d5a9ec7ae65` |
| sentry-cli-Linux-armv7                                                                                   | `sha384-2131a93688800965abe550e029d19993038352f788bc3eeecf4582947154121b` |
| sentry-cli-Linux-i686                                                                                    | `sha384-1d57c92d15265425dbf43df9b9e6395ff9bb5c2eaf60adb541dadc3f866715fa` |
| sentry-cli-Linux-x86\_64                                                                                 | `sha384-cec71d46a7cc394c94b6e75f1601985c710d457376c546ef3975567b3671563b` |
| sentry-cli-Windows-aarch64.exe                                                                           | `sha384-170b971f2596b612ed207823aa86bc251f9adfb687a476c9e8021339288b0747` |
| sentry-cli-Windows-i686.exe                                                                              | `sha384-013ea91a57e636ff9e7f54c77e192a59df9f3cabb090421c7f5bd8408e9d3437` |
| sentry-cli-Windows-x86\_64.exe                                                                           | `sha384-8643986aec8d8cf8d69cd476d67427578e5dbbda378eba506d199681082abe5a` |
| sentry\_cli-3.7.0-py3-none-macosx\_10\_15\_x86\_64.whl                                                   | `sha384-f12295ba4d9210615028cd55d73e9f676c26ec4830bbefb96d0a5b10a1387a22` |
| sentry\_cli-3.7.0-py3-none-macosx\_11\_0\_arm64.whl                                                      | `sha384-ea6077c21c2f56e8bf9f6e8aa0867e7b183ea9f19ffd652e707e7845586b7815` |
| sentry\_cli-3.7.0-py3-none-macosx\_11\_0\_universal2.whl                                                 | `sha384-ef76fdec961327086c86f9356356513364510ed17bb5bd63e9b0fbbc0a8f4211` |
| sentry\_cli-3.7.0-py3-none-manylinux\_2\_17\_aarch64.manylinux2014\_aarch64.musllinux\_1\_2\_aarch64.whl | `sha384-20001dd777cd5841b59461b4af77c72a6f7bc25cdae03054c51d38ddcc55776b` |
| sentry\_cli-3.7.0-py3-none-manylinux\_2\_17\_armv7l.manylinux2014\_armv7l.musllinux\_1\_2\_armv7l.whl    | `sha384-d0cf0f045dd14e2dbf70e1b14d1b3b24da0cdda3f6672b79880b8424aeaf80d4` |
| sentry\_cli-3.7.0-py3-none-manylinux\_2\_17\_i686.manylinux2014\_i686.musllinux\_1\_2\_i686.whl          | `sha384-015c1061fedf283658cfa4c3e4ad35c2d920ed3bc094a8f48ed77d2c34941f99` |
| sentry\_cli-3.7.0-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.musllinux\_1\_2\_x86\_64.whl | `sha384-1d4d79404265774e6fd3662ea6e88149b375f9663d4c9226c9aa25b75cc0ae63` |
| sentry\_cli-3.7.0-py3-none-win32.whl                                                                     | `sha384-851f069d2555f2904ef4f5a6613e441f274d858bf52527283a48e46e0cae73bd` |
| sentry\_cli-3.7.0-py3-none-win\_amd64.whl                                                                | `sha384-4a0faeb93f5e5b247289906a86ac28bc89c10934d6768ae9f0323750b3c07d98` |
| sentry\_cli-3.7.0-py3-none-win\_arm64.whl                                                                | `sha384-cdbcaddeb03faef76b9b16a15d8b3a9d5a238093b0f7a42c983b90988cb90eec` |
| sentry\_cli-3.7.0.tar.gz                                                                                 | `sha384-d09fb5bd33e43030c15bb5e600d5a0fefb3b197dfb2118ea6fdf5cd2f082a1f5` |

If you would like to verify checksums for historic versions of the `sentry-cli`, please refer to our release registry directly, which can be found at [https://release-registry.services.sentry.io/apps/sentry-cli/{version}](https://release-registry.services.sentry.io/apps/sentry-cli/latest). For example, <https://release-registry.services.sentry.io/apps/sentry-cli/1.74.4>.

