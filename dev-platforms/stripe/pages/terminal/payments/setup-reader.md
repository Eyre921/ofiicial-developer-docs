---
title: "Select a reader"
source: https://docs.stripe.com/terminal/payments/setup-reader.md
path: terminal/payments/setup-reader
---

# Select a reader

Learn about Stripe's pre-certified card readers and Tap to Pay.

Stripe Terminal readers offer end-to-end encryption and remote management tools. Use this page to find the right reader for your integration.
![Stripe Reader T600 countertop smart payment terminal with touchscreen](https://b.stripecdn.com/docs-statics-srv/assets/t600-countertop.a9d30a7f21371ab3f1aab1082b7282fb.png)

[Stripe Reader T600](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md)
![Stripe Reader S700/S710 smart payment terminal with touchscreen](https://b.stripecdn.com/docs-statics-srv/assets/S700-Docs-thumb.b808fd5c893fcfbe579b3ad4ab6a0e71.png)

[Stripe Reader S700/S710](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md)
![BBPOS WisePOS E smart payment terminal with touchscreen](https://b.stripecdn.com/docs-statics-srv/assets/WisePOSE-Docs-thumb.15c000aa50c765237f887bf9fd96bf29.png)

[BBPOS WisePOS E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)
![Stripe Reader M2 US-only screenless mobile card reader](https://b.stripecdn.com/docs-statics-srv/assets/M2-Docs-thumb.276dbca641bd8b5f215a7efdb5dc9ffd.png)

[Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)
![BBPOS WisePad 3 non-US mobile card reader with display](https://b.stripecdn.com/docs-statics-srv/assets/WP3-Docs-thumb.e1fe0fe8f4f9c6aff284fa7d97615617.png)

[BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)
![Tap to Pay on iPhone and Tap to Pay on Android](https://b.stripecdn.com/docs-statics-srv/assets/TTP-Docs-thumb.df093c1dc1ebd17ce694c11ece1ae1f4.png)

[Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md)
![Verifone smart readers](https://b.stripecdn.com/docs-statics-srv/assets/verifone-thumbnail.b8b8950b17a9b45fcf848a1b7b58e482.png)

[Verifone](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md) (Public preview)

## Choose by use case 

To narrow your options, start with your physical environment and integration needs.

| Use case | Recommended reader | Why |
| --- | --- | --- |
| Countertop checkout | [Stripe Reader T600](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md), [Stripe Reader S700/S710](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md), or [Verifone](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md) | Smart readers with touchscreen, tipping, on-screen inputs, and server-driven or SDK integration. The T600 is a continuously powered countertop and pole-mount reader with an 8-inch customer-facing display. The S710 adds cellular connectivity, and is commonly used in retail, restaurants, and hospitality. |
| Mobile or field payments | [Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md) (US) or [BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md) (outside US) | Compact mobile readers that pair with a phone or tablet running your app. Commonly used for delivery, curbside, and event payments. For an all-in-one device without a separate phone or tablet, consider [Stripe Reader S700/S710](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md) with [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md). |
| No additional hardware | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md) | Accept contactless payments directly on a compatible iPhone or Android device. |
| Self-service kiosk or unattended terminal | [Verifone UX700](https://docs.stripe.com/terminal/payments/setup-reader/ux700.md) | A compact smart reader with a 5.5-inch display and weatherproof protection for self-service use cases such as restaurant ordering kiosks. |

## Key decision factors 

If your use case isn’t listed, use these dimensions to narrow your choice:

### Device category 

- **Smart readers (sPOS)**: Internet-connected touchscreen devices that support Terminal SDK, JavaScript SDK, and server-driven integrations. The options include Stripe Reader T600, Stripe Reader S700 and S710, BBPOS WisePOS E, and supported Verifone readers.

- **Mobile readers (mPOS)**: Connect to a phone or tablet running a Terminal mobile SDK through Bluetooth or USB on Android. The options include Stripe Reader M2 in the United States and BBPOS WisePad 3 outside the United States.

- **Tap to Pay**: Accepts contactless payments on a compatible iPhone or Android device without a separate reader.

### Connection type 

- **Internet (WiFi or Ethernet)**: Smart readers connect to Stripe over the internet. Your point-of-sale communicates with the reader through the Stripe API (server-driven integration) or over the local network using a Terminal SDK.

- **Bluetooth or USB**: Mobile readers connect to your tablet or mobile device that runs the Terminal iOS, Android, or React Native SDK. USB connections are supported on Android.

- **Cellular**: Stripe Reader S710 supports 4G LTE connectivity in locations without reliable WiFi.

### Integration platform 

- **Mobile SDKs (iOS, Android, and React Native)**: Support smart readers, mobile readers, and Tap to Pay. Mobile readers require one of these SDKs. [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md) also run on the Android and React Native SDKs where your custom app runs directly on a compatible smart reader.

- **Server-driven integration (Stripe API)**: Supports Terminal smart readers only and doesn’t require a Terminal client SDK.

- **JavaScript SDK**: Supports Terminal smart readers only and runs in a web-based point-of-sale application.

- **Apps on Devices**: Run your custom app directly on a compatible smart reader using the Android or React Native SDK. Available on Stripe Reader T600, Stripe Reader S700/S710, and Verifone V660p. See [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md).

- **Standalone mode**: Uses a no-code Stripe app pre-installed on compatible smart readers, including Stripe Reader S700/S710 and Verifone V660p. Availability varies by reader. See [Standalone mode](https://docs.stripe.com/terminal/payments/ready-made-apps.md).

## Compare reader capabilities 

This table compares the key capabilities across all readers.

|  | [Stripe Reader T600](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md) | [Stripe Reader S700/S710](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md) | [BBPOS WisePOS E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md) | [Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md) | [BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md) | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md) | [Verifone](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Device category | sPOS | sPOS | sPOS | mPOS | mPOS | Phone/tablet | sPOS |
| Connection | Internet | Internet | Internet | Bluetooth, USB | Bluetooth, USB | N/A | Internet |
| Country availability | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) | US only | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) | [Multiple](https://docs.stripe.com/terminal/payments/setup-reader.md#availability) |
| Contactless and digital wallets | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| EMV chip cards | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | ✓ Supported |
| Magstripe cards | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | - Unsupported | ✓ Supported |
| Server-driven integration | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| JavaScript SDK | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| Mobile SDKs (iOS, Android, React Native) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| Standalone mode | Coming soon | ✓ Supported | - Unsupported | - Unsupported | - Unsupported | - Unsupported | V660p only |
| Stripe Terminal mobile app (Private preview) | - Unsupported | - Unsupported | - Unsupported | - Unsupported | - Unsupported | ✓ Supported | - Unsupported |
| Offline payments1 | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | iPhone only (Private preview) | ✓ Supported |
| On-reader tipping | ✓ Supported | ✓ Supported | ✓ Supported | Receipt tipping only | ✓ Supported | In-app | ✓ Supported |
| On-screen input collection | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | - Unsupported | In-app | ✓ Supported |
| Custom splash screen | ✓ Supported | ✓ Supported | ✓ Supported | - Unsupported | ✓ Supported | - Unsupported | ✓ Supported |
| Custom apps on-device (paid) | ✓ Supported | ✓ Supported | - Unsupported | - Unsupported | - Unsupported | In-app | ✓ Supported |
| Cellular connectivity | - Unsupported | S710 only | - Unsupported | - Unsupported | - Unsupported | - Unsupported | - Unsupported |

1 Offline mode requires the Terminal mobile SDK.

## Global availability 

Reader availability varies by country. Not all Verifone models (V660p, UX700, P630, and M425) are available in every country.

| Country | [Smart readers](https://docs.stripe.com/terminal/smart-readers.md) | [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md) | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md) |
| --- | --- | --- | --- |
| US | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone P630, UX700, V660p
- Verifone M425 (Public preview) | - Stripe Reader M2 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| AU | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| - BE
- IT
- NL
- NO
- ES
- SE | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| NZ | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| CA | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630, M425 (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| - IE
- GB | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| SG | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| - AT
- CH
- CZ
- DK
- FI
- LU
- PT | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| PL | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| FR | - Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| DE | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| JP | - Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android (Public preview)
- Tap to Pay on iPhone |
| MY | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone (Public preview) |
| MX | - Stripe Reader S710 (Public preview) | - BBPOS WisePad 3 (Public preview) | - Tap to Pay on Android (Public preview)
- Tap to Pay on iPhone (Public preview) |
| - BG
- HR
- CY
- EE
- HU
- LV
- LI
- LT
- MT
- RO
- SK
- SI | - BBPOS WisePOS E
- Stripe Reader T600
- Stripe Reader S710 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
| - GI |  |  | - Tap to Pay on Android |
| HK | - Stripe Reader S710 (Public preview)
- Stripe Reader T600 (Public preview) | - BBPOS WisePad 3 (Public preview) | - Tap to Pay on Android
- Tap to Pay on iPhone |

## Order readers 

You can [order readers](https://dashboard.stripe.com/terminal/shop) from the Dashboard and have them shipped to a location of your choice. As a [Connect](https://docs.stripe.com/terminal/features/connect.md) platform, you can order readers centrally and assign them to your connected accounts, or enable your connected accounts to order their own readers directly.

- [Browse readers and accessories](https://dashboard.stripe.com/terminal/shop).
- For Tap to Pay, see [compatible iPhones](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#supported-devices) and [Android devices](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices).
- Use the [Terminal Hardware Ordering API](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#use-the-hardware-orders-api) to automate ordering at scale.

If you don’t have a physical reader yet, you can use the [simulated reader](https://docs.stripe.com/terminal/payments/setup-integration.md) to build and test your Terminal integration.

> Stripe readers aren’t liquid-proof so make sure your devices remain dry. If your device has experienced liquid ingress, stop using the device and let it dry thoroughly before attempting to reuse or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Integration platform comparison 

Choose an integration platform based on your preferred reader, desired features, and technology stack.

| Platform | Works with | Best for |
| --- | --- | --- |
| [iOS SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios) | All readers | Native iOS apps with mobile readers, smart readers or Tap-to-pay on iPhone readers. |
| [Android SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android) | All readers | Native Android apps with mobile readers, smart readers, Tap-to-pay on Android readers, or [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md). |
| [React Native SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) (Public preview) | All readers | Cross-platform mobile apps with a single codebase supporting both iOS and Android Terminal integrations. |
| [Server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven) | Smart readers only | Existing server infrastructure without a client-side SDK. Manage readers entirely through the Stripe API. |
| [JavaScript SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=js) | Smart readers only | Browser-based POS systems. |
| [Standalone mode](https://docs.stripe.com/terminal/payments/ready-made-apps.md) (Public preview) | S700/S710, Verifone V660p | Accepting payments without a connected POS. A prebuilt Stripe payment app runs on the reader and doesn’t require code or a separate POS. |

## Device specifications 

For detailed hardware specifications (dimensions, weight, battery, memory, connectivity, and accessories), see the individual reader pages:

- [Stripe Reader T600](https://docs.stripe.com/terminal/readers/stripe-reader-t600.md#device-specifications)
- [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md#device-specifications)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#device-specifications)
- [Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md#device-specifications)
- [BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md#device-specifications)
- [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md)
- [Verifone V660p](https://docs.stripe.com/terminal/payments/setup-reader/v660p.md#device-specifications), [UX700](https://docs.stripe.com/terminal/payments/setup-reader/ux700.md#device-specifications), [P630](https://docs.stripe.com/terminal/payments/setup-reader/p630.md#device-specifications), and [M425](https://docs.stripe.com/terminal/payments/setup-reader/m425.md#device-specifications)

## Connect a reader 

Before processing payments, you must [connect](https://docs.stripe.com/terminal/payments/connect-reader.md) a Terminal reader to your point-of-sale application using a Terminal SDK. With a [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), you manage readers through the Stripe API and don’t need an SDK connection.

A reader connects to one SDK instance at a time. To use a reader with a different device, disconnect it before connecting to the new one.

## Pre-certification 

Terminal readers are pre-certified for PCI and EMV compliance. They accept payment details (EMV, contactless, and swiped) and encrypt sensitive card information, so your application never handles raw card data.

## Reader software updates 

Stripe periodically releases reader software updates that include improvements and required security patches. Your application must support automatic updates. Failing to install a required update can prevent a reader from accepting payments.

- Smart readers update automatically when powered on, sufficiently charged, and not in use.
- Mobile reader updates are handled by the Terminal SDK when [connected](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) to your point of sale. Required updates install automatically during connection. Optional updates, however, must be triggered by your application.

## Next steps

- [Design your integration](https://docs.stripe.com/terminal/designing-integration.md)
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [Order readers](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md)

