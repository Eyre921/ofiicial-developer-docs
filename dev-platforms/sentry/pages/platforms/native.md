---
title: "Native"
source: https://docs.sentry.io/platforms/native.md
path: platforms/native
---

---
title: "Native"
url: https://docs.sentry.io/platforms/native/
---

# Sentry for Native

The Sentry Native SDK is intended for C and C++. However, since it builds as a dynamic library and exposes C-bindings, it can be used by any language that supports interoperability with C, such as the Foreign Function Interface (FFI).

It also provides native crash reporting for other Sentry SDKs:

* [*Android (NDK)*](https://docs.sentry.io/platforms/android/configuration/using-ndk.md)
* [*Flutter*](https://docs.sentry.io/platforms/dart/guides/flutter.md)
* [*Godot*](https://docs.sentry.io/platforms/godot.md)
* [*.NET*](https://docs.sentry.io/platforms/dotnet.md)
* [*Unity*](https://docs.sentry.io/platforms/unity.md)
* [*Unreal Engine*](https://docs.sentry.io/platforms/unreal.md)

Sentry's console SDKs also build on the Native SDK. See the [Nintendo Switch](https://docs.sentry.io/platforms/nintendo-switch.md), [PlayStation](https://docs.sentry.io/platforms/playstation.md), and [Xbox](https://docs.sentry.io/platforms/xbox.md) documentation to get access.

Sentry also offers higher-level SDKs for platforms with built-in support for native crashes:

* [*Android*](https://docs.sentry.io/platforms/android.md)
* [*Apple (Cocoa)*](https://docs.sentry.io/platforms/apple.md)
* [*Electron*](https://docs.sentry.io/platforms/javascript/guides/electron.md)

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/native.md#install)

Sentry captures data by using an SDK within your application’s runtime.

The Native SDK currently supports **Windows**, **macOS**, and **Linux**. The Native SDK also acts as an **Android** NDK support library in downstream SDKs via the [Android SDK](https://docs.sentry.io/platforms/android/configuration/using-ndk.md), but currently does not directly support the platform. **Nintendo Switch**, **PlayStation**, and **Xbox** are supported via Sentry's console SDKs. See the [Nintendo Switch](https://docs.sentry.io/platforms/nintendo-switch.md), [PlayStation](https://docs.sentry.io/platforms/playstation.md), and [Xbox](https://docs.sentry.io/platforms/xbox.md) documentation to get access.

To build the SDK, download the latest sources from the [Releases page](https://github.com/getsentry/sentry-native/releases). The SDK is managed as a [CMake](https://cmake.org/cmake/help/latest/) project, which additionally supports several configuration options, such as the backend to use.

For example, `CMake` can be used like this:

**macOS**

```shell
# When using CMake 4 ensure you have valid SDKROOT defined in your environment.
export SDKROOT=$(xcrun --sdk macosx --show-sdk-path)
# Configure the CMake build into the `build` directory with the desired backend.
# Specifying `RelWithDebInfo` as the `CMAKE_BUILD_TYPE` is optional because it
# is the default in sentry-native for all generators supporting it.
cmake -B build -D SENTRY_BACKEND=native -D CMAKE_BUILD_TYPE=RelWithDebInfo
# build the project
cmake --build build --parallel
# install the resulting artifacts into a specific prefix
cmake --install build --prefix install
# which will result in the following:
eza --tree install --level 2
install
├── bin
│  └── sentry-crash
├── include
│  └── sentry.h
└── lib
   ├── cmake
   ├── libsentry.dylib
   └── libsentry.dylib.dSYM
```

**Linux**

```shell
# Configure the CMake build into the `build` directory with the desired backend.
# Specifying `RelWithDebInfo` as the `CMAKE_BUILD_TYPE` is optional because it
# is the default in sentry-native for all generators supporting it.
cmake -B build -D SENTRY_BACKEND=native -D CMAKE_BUILD_TYPE=RelWithDebInfo
# build the project
cmake --build build --parallel
# install the resulting artifacts into a specific prefix
cmake --install build --prefix install
# which will result in the following:
tree install -L 2
install
├── bin
│   └── sentry-crash
├── include
│   └── sentry.h
└── lib
    ├── cmake
    └── libsentry.so

5 directories, 3 files
```

**Windows**

```shell
# The msbuild generator ignores the CMAKE_BUILD_TYPE because it contains all
# build-types.
cmake -B build -D SENTRY_BACKEND=native
# The actual build step then requires we specify which build-type we want
# to apply via the `--config` parameter. Please be aware that in msbuild
# projects, the `--parallel` option has no effect.
cmake --build build --config RelWithDebInfo
# install the resulting artifacts (again requiring build-type!)
cmake --install build --prefix install --config RelWithDebInfo
# which will result in the following output (ignoring non-essential lines):
tree /f install
├───bin
│       sentry-crash.exe
│       sentry-wer.dll
│       sentry-wer.pdb
│       sentry.dll
│       sentry.pdb
│
├───include
│       sentry.h
│
└───lib
    │   sentry.lib
    │
    └───cmake
```

(For further details on the `SDKROOT` usage with CMake please consult the [macOS build section in the SDK README](https://github.com/getsentry/sentry-native?tab=readme-ov-file#building-and-installation))

##### Bundling out-of-process backends

The out-of-process *Native* and *Crashpad* backends require shipping `sentry-crash` or `crashpad_handler`, respectively, alongside the application binary. See the [Native](https://docs.sentry.io/platforms/native/configuration/backends/native.md) and [Crashpad](https://docs.sentry.io/platforms/native/configuration/backends/crashpad.md) backend documentation for more information.

## [Configure](https://docs.sentry.io/platforms/native.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

```c
#include <sentry.h>

int main(void) {
  sentry_options_t *options = sentry_options_new();
  sentry_options_set_dsn(options, "https://<key>@o<orgId>.ingest.sentry.io/<projectId>");
  // This is also the default-path. For further information and recommendations:
  // https://docs.sentry.io/platforms/native/configuration/options/#database-path
  sentry_options_set_database_path(options, ".sentry-native");
  sentry_options_set_release(options, "my-project-name@2.3.12");
  sentry_options_set_debug(options, 1);
  sentry_init(options);

  /* ... */

  // make sure everything flushes
  sentry_close();
}
```

Alternatively, the DSN can be passed as `SENTRY_DSN` environment variable during runtime. This can be especially useful for server applications.

##### Warning

Calling `sentry_close()` before exiting the application is critical. It ensures that events can be sent to Sentry before execution stops. Otherwise, event data may be lost.

## [Verify](https://docs.sentry.io/platforms/native.md#verify)

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

The quickest way to verify Sentry in your Native application is by capturing a message:

```c
sentry_capture_event(sentry_value_new_message_event(
  /*   level */ SENTRY_LEVEL_INFO,
  /*  logger */ "custom",
  /* message */ "It works!"
));
```

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/native/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/native.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Frameworks

- [Google Breakpad](https://docs.sentry.io/platforms/native/guides/breakpad.md)
- [Google Crashpad](https://docs.sentry.io/platforms/native/guides/crashpad.md)
- [Minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md)
- [Qt](https://docs.sentry.io/platforms/native/guides/qt.md)
- [WebAssembly](https://docs.sentry.io/platforms/native/guides/wasm.md)

## Topics

- [Basic Configuration](https://docs.sentry.io/platforms/native/configuration.md)
- [Usage](https://docs.sentry.io/platforms/native/usage.md)
- [Advanced Usage](https://docs.sentry.io/platforms/native/advanced-usage.md)
- [Data Management](https://docs.sentry.io/platforms/native/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/native/security-policy-reporting.md)
- [App Hangs](https://docs.sentry.io/platforms/native/app-hangs.md)
- [Debug Information](https://docs.sentry.io/platforms/native/debug-information.md)
- [Enriching Events](https://docs.sentry.io/platforms/native/enriching-events.md)
- [Tracing](https://docs.sentry.io/platforms/native/tracing.md)
- [Logs](https://docs.sentry.io/platforms/native/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/native/metrics.md)
- [User Feedback](https://docs.sentry.io/platforms/native/user-feedback.md)

