---
title: "Expo"
source: https://docs.sentry.io/platforms/react-native/guides/expo.md
path: platforms/react-native/guides/expo
---

---
title: "Expo"
description: "Learn how to set up an Expo project with Sentry's React Native SDK, including the Sentry Expo config plugin, Expo Router tracing, Expo Updates context, and the EAS dashboard integration."
url: https://docs.sentry.io/platforms/react-native/guides/expo/
---

# Sentry for Expo

Use this guide to get fully set up with Sentry's React Native SDK in an [Expo](https://expo.dev/) project. The same `@sentry/react-native` SDK powers both bare React Native and Expo apps. This guide covers the Expo-specific setup (config plugin, Metro, EAS) and integrations.

If you don't already have an account and Sentry project established, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Prerequisites](https://docs.sentry.io/platforms/react-native/guides/expo.md#prerequisites)

* [Expo SDK 50](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/) or newer. The `@sentry/react-native` SDK requires Expo SDK 50+.
  * On [Expo SDK 49](https://docs.expo.dev/guides/using-sentry/) or older, the legacy `sentry-expo` package was used. It's now deprecated — [migrate to `@sentry/react-native`](https://docs.sentry.io/platforms/react-native/guides/expo/migration/sentry-expo.md) to keep receiving updates.
* [Sign up for an account](https://sentry.io/signup/).

## [Automatic Install](https://docs.sentry.io/platforms/react-native/guides/expo.md#automatic-install)

Use the Sentry Wizard to patch your project automatically, as shown below. Alternatively, you can follow the [Manual Install](https://docs.sentry.io/platforms/react-native/guides/expo.md#manual-install) if you prefer. You only need to patch the project once. Then, you can add the patched files to your version control system.

```bash
npx @sentry/wizard@latest -i reactNative
```

The following tasks will be performed by the Sentry Wizard

* Install the `@sentry/react-native` package.
* Add the `@sentry/react-native/metro` to the **metro.config.js** Metro configuration.
* Add the `@sentry/react-native/expo` to the **app.json** Expo configuration.
* Enable the Sentry React Native Gradle build step for Android to auto-upload generated source maps and debug symbols.
* Wrap the *Bundle React Native code and images* Xcode project build phase script to upload generated source maps and collect bundled node modules.
* Add *Upload Debug Symbols to Sentry* Xcode project build phase.
* Run `pod install`.
* Store build credentials in **ios/sentry.properties**, **android/sentry.properties** and **.env.local**.
* Configure Sentry for the supplied DSN in your **layout.tsx** file.

## [Manual Install](https://docs.sentry.io/platforms/react-native/guides/expo.md#manual-install)

If you don't use the Wizard, install the `@sentry/react-native` package:

```bash
npx expo install @sentry/react-native
```

*Other available variations of the above snippet: npm, yarn, pnpm*

### [Initialize the SDK](https://docs.sentry.io/platforms/react-native/guides/expo.md#initialize-the-sdk)

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Session Replay\[ ]Logs

Import the `@sentry/react-native` package and call `init` with your DSN:

```javascript
import { Stack } from "expo-router";
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Adds more context data to events (IP address, cookies, user, etc.)
  // For more information, visit: https://docs.sentry.io/platforms/react-native/data-management/data-collected/
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance
  // Set tracesSampleRate to 1.0 to capture 100% of transactions for tracing.
  // We recommend adjusting this value in production.
  // Learn more at
  // https://docs.sentry.io/platforms/react-native/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs
  // Enable logs to be sent to Sentry
  // Learn more at https://docs.sentry.io/platforms/react-native/logs/
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  // ___PRODUCT_OPTION_START___ profiling
  // profilesSampleRate is relative to tracesSampleRate.
  // Here, we'll capture profiles for 100% of transactions.
  profilesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ profiling
  // ___PRODUCT_OPTION_START___ session-replay
  // Record session replays for 100% of errors and 10% of sessions
  replaysOnErrorSampleRate: 1.0,
  replaysSessionSampleRate: 0.1,
  integrations: [Sentry.mobileReplayIntegration()],
  // ___PRODUCT_OPTION_END___ session-replay
});

function RootLayout() {
  return <Stack />;
}

export default Sentry.wrap(RootLayout);
```

### [Wrap Your App](https://docs.sentry.io/platforms/react-native/guides/expo.md#wrap-your-app)

Wrap the root component of your application with `Sentry.wrap`:

```javascript
export default Sentry.wrap(RootLayout);
```

### [Add the Sentry Expo Plugin](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-the-sentry-expo-plugin)

To ensure bundles and source maps are automatically uploaded during the native application builds, add the Sentry plugin to your Expo app configuration. Add it to the `plugins` array in `app.json`, or wrap your config with `withSentry` in `app.config.js`/`app.config.ts`:

**app.json/app.config.json**

```javascript
{
  "expo": {
    "plugins": [
      [
        "@sentry/react-native/expo",
        {
          "url": "https://sentry.io/",
          "note": "Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.",
          "project": "<your-project-slug>",
          "organization": "<your-org-slug>"
        }
      ]
    ]
  }
}
```

**app.config.js**

```javascript
const { withSentry } = require("@sentry/react-native/expo");

const config = {
  name: "Expo Example",
  slug: "expo-example",
};

module.exports = withSentry(config, {
  url: "https://sentry.io/",
  // Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.
  project: "<your-project-slug>",
  organization: "<your-org-slug>",
});
```

**app.config.ts**

```typescript
import { ExpoConfig } from "expo/config";
import { withSentry } from "@sentry/react-native/expo";

const config: ExpoConfig = {
  name: "Expo Example",
  slug: "expo-example",
};

export default withSentry(config, {
  url: "https://sentry.io/",
  // Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.
  project: "<your-project-slug>",
  organization: "<your-org-slug>",
});
```

`npx expo install` adds the bare `@sentry/react-native` to the plugins array. Both `@sentry/react-native` and `@sentry/react-native/expo` are valid plugin paths. Expo resolves them the same way.

Add your auth token to a `.env.local` file in the root of your project:

```properties
# DO NOT COMMIT YOUR AUTH TOKEN
SENTRY_AUTH_TOKEN=<your-sentry-auth-token>
```

Do not commit your auth token. Add `.env.local` to your `.gitignore`. For EAS builds, add `SENTRY_AUTH_TOKEN` as an [EAS secret](https://docs.expo.dev/eas/environment-variables/) instead of using a `.env.local` file.

### [Add Sentry Metro Plugin](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-sentry-metro-plugin)

To ensure unique Debug IDs get assigned to the generated bundles and source maps, add Sentry Serializer to the Metro configuration:

```javascript
// const { getDefaultConfig } = require("expo/metro-config");
const { getSentryExpoConfig } = require("@sentry/react-native/metro");

// const config = getDefaultConfig(__dirname);
const config = getSentryExpoConfig(__dirname);

module.exports = config;
```

### [Add Privacy Manifest](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-privacy-manifest)

The SDK needs access to certain information about the device and the application for its essential functionality. Some of the APIs required for this are considered privacy-relevant. Add the privacy manifest to your Xcode project to ensure your app is compliant with Apple's guidelines. Read the [Apple Privacy Manifest](https://docs.sentry.io/platforms/react-native/guides/expo/data-management/apple-privacy-manifest.md) guide for more info on how to add records required for the Sentry SDKs.

## [Verify Setup](https://docs.sentry.io/platforms/react-native/guides/expo.md#verify-setup)

To verify that everything is working as expected, build the `Release` version of your application and send a test event to Sentry by adding:

```javascript
<Button
  title="Try!"
  onPress={() => {
    Sentry.captureException(new Error("First error"));
  }}
/>;
```

## [Expo-Specific Features](https://docs.sentry.io/platforms/react-native/guides/expo.md#expo-specific-features)

* [Expo Updates](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/expo-updates.md) — Automatic OTA update context, searchable tags, performance spans for update checks and downloads, and emergency launch alerts
* [EAS Build Hooks](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/eas-build-hooks.md) — Capture build failures and lifecycle events from EAS Build
* [Sentry Android Gradle Plugin](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/gradle.md) — Advanced Android build configuration
* [Expo Router tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing/instrumentation/expo-router.md) — Navigation transitions, performance spans, prefetch instrumentation, and per-route `ErrorBoundary` capture
* [Expo Image and Asset tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing/instrumentation/expo-resources.md) — Automatic spans for `expo-image` and `expo-asset`
* [Upload source maps for native builds and Expo Updates](https://docs.sentry.io/platforms/react-native/guides/expo/sourcemaps/uploading/expo.md)

## [Notes](https://docs.sentry.io/platforms/react-native/guides/expo.md#notes)

* Don't commit your auth token. Store it in `.env.local` as `SENTRY_AUTH_TOKEN` for local builds, and as an [EAS secret](https://docs.expo.dev/eas/environment-variables/) for EAS builds.
* Source maps for the `Release` version of your application are uploaded automatically during the native application build.
* During development, the source code is resolved using the Metro Server and source maps aren't used. This currently doesn't work on web.

## [Integrate Sentry with your EAS dashboard](https://docs.sentry.io/platforms/react-native/guides/expo.md#integrate-sentry-with-your-eas-dashboard)

Once the SDK is set up, you can also connect Sentry to [Expo Application Services (EAS)](https://expo.dev/eas) so crash reports and [Session Replays](https://docs.sentry.io/platforms/react-native/guides/expo/session-replay.md) for your deployments show up directly in your EAS dashboard, with direct links to Sentry stack traces and full debugging context.

If you change your organization slug, you'll need to update your configuration for this integration. Learn more in our [troubleshooting guide](https://docs.sentry.io/integrations/troubleshooting.md).

### [Install the integration](https://docs.sentry.io/platforms/react-native/guides/expo.md#install-the-integration)

Sentry owner, manager, or admin permissions are required to install this integration.

1. Log in to your Expo dashboard and open **Account Settings > Overview** (`https://expo.dev/accounts/[your-account]/settings`).
2. Locate the **Connections** section and click **Connect** next to Sentry.
3. Log in to Sentry and accept the integration into your organization. You'll be redirected back to Account Settings > Overview.

### [Link your projects](https://docs.sentry.io/platforms/react-native/guides/expo.md#link-your-projects)

After connecting your accounts, link your Expo project to your Sentry project:

1. Open **Projects > \[Your Project] > Configuration > Project settings** in the Expo dashboard.
2. Click **Link** and select your Sentry project from the dropdown.

### [View Sentry data in EAS](https://docs.sentry.io/platforms/react-native/guides/expo.md#view-sentry-data-in-eas)

To see your Sentry issues and replays in the Expo dashboard, first make sure you've created an [EAS Update channel](https://docs.expo.dev/eas-update/how-it-works/) and assigned builds to it to create an [EAS deployment](https://docs.expo.dev/eas-update/deployment/). Then:

1. Open **Projects > \[Your Project] > Updates > Deployments > \[Deployment]** to view Sentry data from a release.

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/react-native/guides/expo/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/react-native/guides/expo/enriching-events.md)
- [Features](https://docs.sentry.io/platforms/react-native/guides/expo/features.md)
- [Extended Configuration](https://docs.sentry.io/platforms/react-native/guides/expo/configuration.md)
- [Manual Setup](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup.md)
- [Tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing.md)
- [Integrations](https://docs.sentry.io/platforms/react-native/guides/expo/integrations.md)
- [Profiling](https://docs.sentry.io/platforms/react-native/guides/expo/profiling.md)
- [Data Management](https://docs.sentry.io/platforms/react-native/guides/expo/data-management.md)
- [Logs](https://docs.sentry.io/platforms/react-native/guides/expo/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/react-native/guides/expo/session-replay.md)
- [Source Maps](https://docs.sentry.io/platforms/react-native/guides/expo/sourcemaps.md)
- [Application Metrics](https://docs.sentry.io/platforms/react-native/guides/expo/metrics.md)
- [Debug Symbols](https://docs.sentry.io/platforms/react-native/guides/expo/upload-debug.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/react-native/guides/expo/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/react-native/guides/expo/overhead.md)
- [Build Distribution](https://docs.sentry.io/platforms/react-native/guides/expo/build-distribution.md)
- [User Feedback](https://docs.sentry.io/platforms/react-native/guides/expo/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/react-native/guides/expo/feature-flags.md)
- [Migration Guide](https://docs.sentry.io/platforms/react-native/guides/expo/migration.md)
- [Size Analysis](https://docs.sentry.io/platforms/react-native/guides/expo/size-analysis.md)
- [Troubleshooting](https://docs.sentry.io/platforms/react-native/guides/expo/troubleshooting.md)

