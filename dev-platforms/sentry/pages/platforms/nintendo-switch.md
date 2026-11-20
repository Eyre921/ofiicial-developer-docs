---
title: "Nintendo Switch"
source: https://docs.sentry.io/platforms/nintendo-switch.md
path: platforms/nintendo-switch
---

---
title: "Nintendo Switch"
description: "Learn how to set up Sentry's Nintendo Switch SDK for error monitoring and performance tracking."
url: https://docs.sentry.io/platforms/nintendo-switch/
---

# Sentry for Nintendo Switch

You can get started using Sentry on Nintendo Switch without any changes to your game, on devkits as well as retail devices.

It can be done directly on Nintendo's CRPORTAL. The two environments available are [lp1 for retail devices](https://crash-report.wc.lp1.er.srv.nintendo.net/sentry/get_started) and [dd1 for devkits](https://crash-report.wc.dd1.er.srv.nintendo.net/sentry/get_started). In both cases you can configure Nintendo's servers to start forwarding your crashes directly to Sentry.

If you want to add additional context to your crash dumps, or you want to capture non-fatal events, Sentry offers an SDK specifically for Nintendo Switch. It allows for adding additional context such as [breadcrumbs](https://docs.sentry.io/product/issues/issue-details/breadcrumbs.md) and [tags](https://docs.sentry.io/product/issues/issue-details.md#tags). To get access to the SDK, please reach out via the [Nintendo Developer Authorization](https://developer.nintendo.com/group/development/getting-started/g1kr9vj6/middleware/sentry) form.

Support for Switch 2 as well as the original Switch is available.

## [Using with Game Engines](https://docs.sentry.io/platforms/nintendo-switch.md#using-with-game-engines)

If you're using Unity or Unreal Engine, use the engine-specific SDK instead of integrating the console SDK directly. The game engine SDKs wrap the console SDK and provide engine-specific features:

* [Sentry SDK for Unity on consoles](https://docs.sentry.io/platforms/unity/game-consoles.md) - captures C# exceptions and syncs context with native crashes
* [Sentry SDK for Unreal Engine on consoles](https://docs.sentry.io/platforms/unreal/game-consoles.md) - provides C++ and Blueprint APIs on top of the console SDK

For custom engines or native C++ games, request access to integrate the console SDK directly as described above.

## [Feature Highlights](https://docs.sentry.io/platforms/nintendo-switch.md#feature-highlights)

Nintendo Switch support was originally introduced in Native SDK `0.8.2`. Switch 2 support followed in `0.12.5+20260203` for native and Unreal, and `0.16.5-20260901` for Unity.

* **Screenshots**\
  Screenshot attachments through Nintendo crash-report forwarding.

* **Device Context**\
  Automatic console model, family, and manufacturer context.\
  Available since `0.11.3+20251020` (expanded console context since `0.15.3-20260707`).

* **Unity Network Checks**\
  Detect offline status without triggering system connection dialogs.\
  Available since `0.16.5-20260907`.

* \**Default user IDs*\
  Default user IDs set based on a unique device identifier, scoped to the Sentry project, and preserved when local storage is cleared.\
  Available since `0.17.3-20261013`.

* [**Crash-Free Session Tracking**](https://docs.sentry.io/platforms/native/configuration/releases.md#release-health)\
  Track crashed sessions through Nintendo crash reports without requiring persistent storage or a subsequent game launch.\
  Available since `0.17.5-20261029`.

***

"Nintendo", "Nintendo Switch" are trademarks or registered trademarks of Nintendo.

