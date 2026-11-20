---
title: "Xbox"
source: https://docs.sentry.io/platforms/xbox.md
path: platforms/xbox
---

---
title: "Xbox"
description: "Learn how to set up Sentry's Xbox SDK for error monitoring and performance tracking."
url: https://docs.sentry.io/platforms/xbox/
---

# Sentry for Xbox

##### Availability of Xbox support

Access to Sentry's error and crash reporting for consoles is a paid feature available on our Enterprise plan. We will review the pricing and details with you during the verification process.

Xbox support is exclusive to our SaaS offering, as it depends on confidential components that cannot be distributed for self-hosted use.

You can get started using Sentry by [requesting Microsoft Game Development Kit (GDK) Middleware access](https://developer.microsoft.com/en-us/games/support/request-gdkx-middleware). We'll receive your request and get back to you with the next steps.

Support is available on Xbox Series X|S as well as Xbox One, by adding the Sentry SDK to your game. Crash collection as well as non-fatal events can be captured, on devkits as well as retail devices.

## [Using with Game Engines](https://docs.sentry.io/platforms/xbox.md#using-with-game-engines)

If you're using Unity or Unreal Engine, use the engine-specific SDK instead of integrating the console SDK directly. The game engine SDKs wrap the console SDK and provide engine-specific features:

* [Sentry SDK for Unity on consoles](https://docs.sentry.io/platforms/unity/game-consoles.md) - captures C# exceptions and syncs context with native crashes
* [Sentry SDK for Unreal Engine on consoles](https://docs.sentry.io/platforms/unreal/game-consoles.md) - provides C++ and Blueprint APIs on top of the console SDK

For custom engines or native C++ games, request access to integrate the console SDK directly as described above.

## [Feature Highlights](https://docs.sentry.io/platforms/xbox.md#feature-highlights)

Xbox Series X|S support was originally introduced in Native SDK `0.7.18`.

* [**Crash-Free Session Tracking**](https://docs.sentry.io/platforms/native/configuration/releases.md#release-health)\
  Automatic session tracking with crash-free session and user rates.

* **Device Context**\
  Automatic console model, family, and manufacturer context.\
  Available since `0.13.5+20260409` (expanded console context since `0.15.3-20260707`).

* **WinGDK Support**\
  Native and Unreal integrations for Windows GDK builds.\
  Available since `0.13.7-20260417`.

* [**Native Crash Backend**](https://docs.sentry.io/platforms/native/configuration/backends/native.md)\
  Opt-in out-of-process crash handling with Windows Error Reporting (WER) support for fast-fail crashes.\
  Available since `0.14.0-20260504` (stable since `0.16.0-20260729`, WER support since `0.17.5-20261029`).

* [**Screenshots**](https://docs.sentry.io/platforms/unreal/enriching-events/screenshots.md)\
  Screenshot attachments via the Unreal renderer (native backend required) or GDK system service (devkits only).\
  Available since `0.14.0-20260504` (system-service screenshots since `0.14.2-20260518`).

* [**Session Replay**](https://docs.sentry.io/platforms/unreal/session-replay.md#xbox)\
  Experimental pre-crash video with a breadcrumb timeline. Requires Unreal on Xbox Series X|S and the software encoder.\
  Available since `0.14.2-20260518` (software-encoded replay since `0.17.3-20261013`).

* [**App-Hang Detection**](https://docs.sentry.io/platforms/native/app-hangs.md)\
  Experimental, opt-in hang reports with stack traces.\
  Available since `0.15.2-20260626` (pause control for expected inactivity since `0.16.1-20260803`).

* [**WER Integration**](https://docs.sentry.io/platforms/native/advanced-usage/windows-error-reporting.md)\
  Sync tags and attachments to WER, and WER report IDs back to Sentry's **Windows Error Reporting** context (native backend required).\
  Available since `0.16.0-20260729` (WER report IDs since `0.17.5-20261029`).

* **GPU Crash Reporting**\
  GPU crash capture for Unreal and custom engines on Xbox Series X|S. Includes GDK hang reports, `.hix` dumps, and failed commands when RHI breadcrumbs are available.\
  Available since `0.16.5-20260901` (Shipping-build capture, hang-report and `.hix` attachments, and custom-engine support since `0.17.5-20261029`).

* **App-Specific Device ID**\
  Default user IDs derived from the app-specific device ID, scoped to the Sentry project, and preserved across reinstalls and cleared local storage.\
  Available since `0.17.3-20261013`.

***

"Microsoft", "Xbox" are trademarks of the Microsoft group of companies.

