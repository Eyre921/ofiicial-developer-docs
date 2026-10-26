---
title: "Minidumps"
source: https://docs.sentry.io/platforms/native/guides/minidumps.md
path: platforms/native/guides/minidumps
---

---
title: "Minidumps"
description: "Learn about how Sentry processes Minidump crash reports."
url: https://docs.sentry.io/platforms/native/guides/minidumps/
---

# Sentry for Minidumps

Sentry can process Minidump crash reports, a memory dump used on Windows and by open-source libraries like [*Breakpad*](https://docs.sentry.io/platforms/native/guides/breakpad.md) or [*Crashpad*](https://docs.sentry.io/platforms/native/guides/crashpad.md).

This page describes **standalone** usage of Minidumps with Sentry. We strongly encourage you to use our [Native SDK](https://docs.sentry.io/platforms/native.md), as Minidumps uploads are very limited in functionality.

In order to receive symbolicated stack traces, you have to upload debug information to Sentry. For more information, see [Debug Information Files](https://docs.sentry.io/platforms/native/guides/minidumps/data-management/debug-files.md).

## [What is a Minidump?](https://docs.sentry.io/platforms/native/guides/minidumps.md#what-is-a-minidump)

Minidumps are files containing the most important memory regions of a crashed process. When the process crashes, the minidump is written to the user's disk and can later be uploaded to Sentry. A minidump typically includes:

* The runtime stack of each thread that was active during the time of the crash. This allows you to reconstruct stack traces for all stacks and even infer variable values in some cases.
* Thread contexts -- that is, register values -- at the time of the crash. This is especially relevant for stack walking.
* Optionally, the process heap. By default, this is not included to keep minidumps at a reasonable size. Sentry does not read the heap so that it can be safely omitted. When using Sentry SDKs, no heap memory is included in minidumps.
* The crash reason and an optional memory address associated to with the crash. For example, memory access violations. In the case of assertions, the assertion message is also included in the dump.
* Meta data about the CPU architecture and the user’s operating system.

##### A Word on Data Privacy

Minidumps are memory dumps of the process at the moment it crashes. As such, they might contain sensitive information on the target system, such as environment variables, local pathnames or maybe even in-memory representations of input fields, including passwords. **Sentry does not store these memory dumps by default**. Once processed, they are removed immediately, and all sensitive information is stripped from the resulting issues.

You can configure Sentry to [store minidumps as attachments](https://docs.sentry.io/platforms/native/guides/minidumps.md#store-minidumps-as-attachments).

In addition to this information, you can add further metadata specific to Sentry, which can help in organizing and analyzing issues. For more information, see [Passing Additional Data](https://docs.sentry.io/platforms/native/guides/minidumps.md#passing-additional-data).

## [Creating and Uploading Minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md#creating-and-uploading-minidumps)

Depending on your operating system and programming language, there are various alternatives to create minidumps and upload them to Sentry. See the following resources for libraries that support generating minidump crash reports:

* [Native SDK](https://docs.sentry.io/platforms/native.md)
* [Google Breakpad](https://docs.sentry.io/platforms/native/guides/breakpad.md)
* [Google Crashpad](https://docs.sentry.io/platforms/native/guides/crashpad.md)
* [Windows Error Reporting (WER)](https://docs.sentry.io/platforms/native/advanced-usage/windows-error-reporting.md)
* [Rust SDK](https://docs.sentry.io/platforms/rust/native-crash-reporting.md)

If you have already integrated a library that generates minidumps and would just like to upload them to Sentry, you need to configure the *Minidump Endpoint URL*, which can be found at *Project Settings > [Client Keys (DSN)](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/keys/)*. This endpoint expects a `POST` request with the minidump in the `upload_file_minidump` field:

```bash
curl -X POST \
  'https://o<orgId>.ingest.sentry.io/api/<projectId>/minidump/?sentry_key=<key>' \
  -F upload_file_minidump=@mini.dmp
```

To send additional information, add more form fields to this request. For a full description of fields accepted by Sentry, see [Passing Additional Data](https://docs.sentry.io/platforms/native/guides/minidumps.md#passing-additional-data).

## [Passing Additional Data](https://docs.sentry.io/platforms/native/guides/minidumps.md#passing-additional-data)

You can add more information to crash reports by merely adding more fields to the upload HTTP request. All these fields will be collected in the “Extra Data” section in Sentry:

```bash
curl -X POST \
  'https://o<orgId>.ingest.sentry.io/api/<projectId>/minidump/?sentry_key=<key>' \
  -F upload_file_minidump=@mini.dmp \
  -F custom_field=value
```

Additionally, you can set all attributes corresponding to the Sentry event interface in a `sentry` field. This field either accepts JSON data or its values can be flattened with the bracket syntax. For example, to set the release and add a tag, send:

```bash
# As JSON
curl -X POST \
  'https://o<orgId>.ingest.sentry.io/api/<projectId>/minidump/?sentry_key=<key>' \
  -F upload_file_minidump=@mini.dmp \
  -F 'sentry={"release":"my-project-name@2.3.12","tags":{"mytag":"value"}}'

# flattened
curl -X POST \
  'https://o<orgId>.ingest.sentry.io/api/<projectId>/minidump/?sentry_key=<key>' \
  -F upload_file_minidump=@mini.dmp \
  -F 'sentry[release]=my-project-name@2.3.12' \
  -F 'sentry[tags][mytag]=value'
```

For the full list of supported values, see [*Event Payloads*](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/) and linked documents.

If your minidump's size exceeds the [limits](https://docs.sentry.io/platforms/native/guides/minidumps.md#size-limits) in the next section, you can compress it using `gzip`, `zstd`, `bzip2` or `xz` and refer the `upload_file_minidump` to the compressed file instead of the plain minidump.

## [Size Limits](https://docs.sentry.io/platforms/native/guides/minidumps.md#size-limits)

Event ingestion imposes limits on the size and number of fields in multipart uploads. These limits are subject to future change and defined currently as:

* *40MB* for a compressed minidump request
* *200MB* for the full body after decompression
* *200MB* for all files combined
* *200MB* for each file individually
* *1MB* for event payloads

## [Store Minidumps as Attachments](https://docs.sentry.io/platforms/native/guides/minidumps.md#store-minidumps-as-attachments)

[Minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md#what-is-a-minidump) may contain sensitive information about the target system, such as environment variables, local pathnames, or in-memory representations of input fields, including passwords. By default, Sentry only uses minidump files to create events and immediately drops them. All sensitive information is stripped from the resulting events.

All attachment types, including log files, screenshots and minidumps (if you enable Store Minidumps As Attachments), are retained for 30 or 90 days, based on [your plan's data retention period](https://docs.sentry.io/security-legal-pii/security/data-retention-periods.md#default-data-retention-by-plan) when sent to Sentry. Note that Sentry does not apply data scrubbing to attachments.

### [Enabling Minidump Storage](https://docs.sentry.io/platforms/native/guides/minidumps.md#enabling-minidump-storage)

You can enable *Store Minidumps As Attachments* in your [organization](https://sentry.io/orgredirect/organizations/:orgslug/settings/security-and-privacy/) or [project settings](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/security-and-privacy/) under **Security & Privacy**. By default, this setting is disabled. Determine the maximum number of crash reports that will be stored per issue; disabled, unlimited, or maximum per issue:

If you set a limit per issue, as in the example above, a limit of 5, Sentry will store the first 5 attachments associated with this issue, but drop any that follow. To make room for additional attachments, delete them. Sentry will then accept attachments until the limit is reached again.

## Other Native Frameworks

- [Google Breakpad](https://docs.sentry.io/platforms/native/guides/breakpad.md)
- [Google Crashpad](https://docs.sentry.io/platforms/native/guides/crashpad.md)
- [Qt](https://docs.sentry.io/platforms/native/guides/qt.md)
- [WebAssembly](https://docs.sentry.io/platforms/native/guides/wasm.md)

## Topics

- [Data Management](https://docs.sentry.io/platforms/native/guides/minidumps/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/native/guides/minidumps/security-policy-reporting.md)
- [Debug Information](https://docs.sentry.io/platforms/native/guides/minidumps/debug-information.md)
- [Enriching Events](https://docs.sentry.io/platforms/native/guides/minidumps/enriching-events.md)

