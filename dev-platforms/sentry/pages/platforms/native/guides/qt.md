---
title: "Qt"
source: https://docs.sentry.io/platforms/native/guides/qt.md
path: platforms/native/guides/qt
---

---
title: "Qt"
description: "Learn how to use Sentry with Qt."
url: https://docs.sentry.io/platforms/native/guides/qt/
---

# Sentry for Qt

Sentry's Qt integration enables automatic reporting of errors, exceptions, and log messages.

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/native/guides/qt.md#install)

Sentry captures data by using an SDK within your application’s runtime.

The Qt integration is part of the [`sentry-native`](https://github.com/getsentry/sentry-native/) SDK, which currently supports Windows, macOS, and Linux. Both Qt 5 and Qt 6 are supported.

To build the SDK, download the latest sources from the [Releases page](https://github.com/getsentry/sentry-native/releases). The SDK is managed as a [CMake](https://cmake.org/cmake/help/latest/) project, which additionally supports several configuration options, such as the backend to use.

To enable the Qt integration set the `SENTRY_INTEGRATION_QT` option to `YES`.

If the Qt libraries are not installed in one of the predefined `CMake` [system prefix paths](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_PREFIX_PATH.html), where they can be found by `CMake`, you will need to set [`CMAKE_PREFIX_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html) explicitly.

For example (on macOS):

```shell
# Configure the cmake build into the `build` directory,
# with crashpad, and Qt integration (on macOS).
cmake -B build \
    -D SENTRY_BACKEND=crashpad \
    -D SENTRY_INTEGRATION_QT=YES

# Build the project
cmake --build build --parallel

# Install the resulting artifacts into a specific prefix
cmake --install build --prefix install

# Which will result in the following (on macOS):
exa --tree install --level 2
install
├── bin
│  └── crashpad_handler
├── include
│  └── sentry.h
└── lib
   ├── cmake
   ├── libsentry.dylib
   └── libsentry.dylib.dSYM
```

You can configure the Qt build for Windows analogous to the [regular build instructions](https://docs.sentry.io/platforms/native.md#install).

##### Bundling crashpad\_handler

When using the *Crashpad backend*, which is the default on Windows and macOS, the `crashpad_handler` binary has to be shipped alongside the application binary. See the [Crashpad documentation](https://docs.sentry.io/platforms/native/configuration/backends/crashpad.md) for more information.

## [Configure](https://docs.sentry.io/platforms/native/guides/qt.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

```cpp
#include <QtWidgets>
#include <sentry.h>

int main(int argc, char *argv[])
{
    sentry_options_t *options = sentry_options_new();
    sentry_options_set_dsn(options, "https://<key>@o<orgId>.ingest.sentry.io/<projectId>");
    // This is also the default-path. For further information and recommendations:
    // https://docs.sentry.io/platforms/native/configuration/options/#database-path
    sentry_options_set_database_path(options, ".sentry-native");
    sentry_options_set_release(options, "my-project-name@2.3.12");
    sentry_options_set_debug(options, 1);
    sentry_init(options);

    // Make sure everything flushes
    auto sentryClose = qScopeGuard([] { sentry_close(); });

    QApplication app(argc, argv);
    QWidget widget;
    widget.show();

    return app.exec();
}
```

Alternatively, the DSN can be passed as `SENTRY_DSN` environment variable during runtime. This can be especially useful for server applications.

##### Warning

Calling `sentry_close()` (formerly `sentry_shutdown()`) before exiting the application is critical. It ensures that events can be sent to Sentry before execution stops. Otherwise, event data may be lost.

## [Verify](https://docs.sentry.io/platforms/native/guides/qt.md#verify)

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

The quickest way to verify Sentry in your Native application is by capturing a message:

```c
sentry_capture_event(sentry_value_new_message_event(
  /*   level */ SENTRY_LEVEL_INFO,
  /*  logger */ "custom",
  /* message */ "It works!"
));
```

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/native/guides/qt/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/native/guides/qt.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Native Frameworks

- [Google Breakpad](https://docs.sentry.io/platforms/native/guides/breakpad.md)
- [Google Crashpad](https://docs.sentry.io/platforms/native/guides/crashpad.md)
- [Minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md)
- [WebAssembly](https://docs.sentry.io/platforms/native/guides/wasm.md)

## Topics

- [Basic Configuration](https://docs.sentry.io/platforms/native/guides/qt/configuration.md)
- [Usage](https://docs.sentry.io/platforms/native/guides/qt/usage.md)
- [Data Management](https://docs.sentry.io/platforms/native/guides/qt/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/native/guides/qt/security-policy-reporting.md)
- [Debug Information](https://docs.sentry.io/platforms/native/guides/qt/debug-information.md)
- [Enriching Events](https://docs.sentry.io/platforms/native/guides/qt/enriching-events.md)
- [Tracing](https://docs.sentry.io/platforms/native/guides/qt/tracing.md)

