---
title: "Google Breakpad"
source: https://docs.sentry.io/platforms/native/guides/breakpad.md
path: platforms/native/guides/breakpad
---

---
title: "Google Breakpad"
description: "Learn about Sentry's integration with Google Breakpad."
url: https://docs.sentry.io/platforms/native/guides/breakpad/
---

# Sentry for Google Breakpad

[Breakpad](https://chromium.googlesource.com/breakpad/breakpad/) is an open-source multiplatform crash reporting system written in C++ by Google and the predecessor of Crashpad. It supports macOS, Windows and Linux, and features an uploader to submit minidumps to a configured URL right when the process crashes.

This page describes **standalone** usage of Breakpad with Sentry. Unless you have integrated Breakpad already, we strongly encourage you to use our [Native SDK](https://docs.sentry.io/platforms/native.md) instead. Native Breakpad events are very limited in functionality, and Breakpad uses in-process crash reporting, which is less robust and has several disadvantages over out-of-process crash reporting.

## [Integration](https://docs.sentry.io/platforms/native/guides/breakpad.md#integration)

Build and integration depend on the target platform. Please refer to [Breakpad Integration Overview](https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/getting_started_with_breakpad.md#integration-overview) for official instructions on how to integrate with your program. Generally, you will need to add the Breakpad headers to the include path and then start a platform dependent `ExceptionHandler`.

For official platform documentation, visit:

* [Linux Starter Guide](https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/linux_starter_guide.md)
* [Mac Starter Guide](https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/mac_breakpad_starter_guide.md)
* [Windows Starter Guide](https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/windows_client_integration.md)

## [Linux Example](https://docs.sentry.io/platforms/native/guides/breakpad.md#linux-example)

First, initialize the `ExceptionHandler` and pass it a callback that is invoked when a minidump is generated. This can be used to move it to a known location or register it for uploading:

```cpp
#include "client/linux/handler/exception_handler.h"

using namespace google_breakpad;

namespace {

bool callback(const MinidumpDescriptor &descriptor,
              void *context,
              bool succeeded) {
    // if succeeded is true, descriptor.path() contains a path
    // to the minidump file. Context is the context passed to
    // the exception handler's constructor.
    return succeeded;
}

}

int main(int argc, char *argv[]) {
    MinidumpDescriptor descriptor("path/to/cache");
    ExceptionHandler eh(
      descriptor,
      /* filter */ nullptr,
      callback,
      /* context */ nullptr,
      /* install handler */ true,
      /* server FD */ -1
    );

    // run your program here
    return 0;
}
```

Next, implement a minidump upload to Sentry. Since the exception handler callback should perform as little action as possible, this upload is ideally started at the next application start. You can use the `HttpUpload` class, which is provided as part of the Breakpad client:

```cpp
#include <string>
#include "common/linux/http_upload.h"

bool UploadMinidump(std::string &path) {
  // Add additional arguments for Sentry
  std::map<string, string> parameters;

  std::map<string, string> files;
  files["upload_file_minidump"] = path;

  return HTTPUpload::SendRequest(
    "https://o<orgId>.ingest.sentry.io/api/<projectId>/minidump/?sentry_key=<key>",
    parameters,
    files,
    /* proxy */ "",
    /* proxy password */ "",
    /* certificate */ "",
    /* response body */ nullptr,
    /* response code */ nullptr,
    /* error */ nullptr
  );
}
```

## Other Native Frameworks

- [Google Crashpad](https://docs.sentry.io/platforms/native/guides/crashpad.md)
- [Minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md)
- [Qt](https://docs.sentry.io/platforms/native/guides/qt.md)
- [WebAssembly](https://docs.sentry.io/platforms/native/guides/wasm.md)

## Topics

- [Data Management](https://docs.sentry.io/platforms/native/guides/breakpad/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/native/guides/breakpad/security-policy-reporting.md)
- [Debug Information](https://docs.sentry.io/platforms/native/guides/breakpad/debug-information.md)

