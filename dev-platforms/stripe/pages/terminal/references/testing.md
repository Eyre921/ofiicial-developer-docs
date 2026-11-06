---
title: "Test Stripe Terminal"
source: https://docs.stripe.com/terminal/references/testing.md
path: terminal/references/testing
---

# Test Stripe Terminal

Learn how to effectively test your Terminal integration.

> Much of the process for testing Stripe Terminal is similar to that for testing online Stripe payments. Also, you can’t use Stripe Terminal with mobile wallets (for example, Apple Pay or Google Pay) in a sandbox. For more information, see the [general Stripe testing guide](https://docs.stripe.com/testing.md).

The best way to achieve a successful Terminal deployment is to test every part of your integration. We provide testing tools for each stage:

1. Before ordering a reader, test your integration with the reader simulator.
2. Test your complete hardware integration with a physical test card.

## Simulated reader 

- [discoverReaders (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#discover-readers)
- [DiscoveryConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPDiscoveryConfiguration.html)
- [DiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/index.html)

- [Discover Readers](https://docs.stripe.com/api/terminal/readers/list.md)

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

The simulated reader doesn’t provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to [simulate card presentment](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment).

## Simulated test cards

- [SimulatorConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPSimulatorConfiguration.html)
- [SimulatorConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-simulator-configuration/index.html)

The simulated reader can be configured to use a simulated test card, enabling you to test different flows within your point of sale application.

Before collecting a payment method, configure the simulated reader to use one of the following test card numbers or test payment methods to produce specific responses. Configuration set during the collect step (such as the test card number) is persisted for 30 minutes. This means a subsequent confirm step uses the same configuration, even if you don’t pass it again explicitly. Any configuration passed on the confirm call takes priority over the cached values from the collect step.

### Standard test cards

| Test card number | Test payment method | Brand |
| --- | --- | --- |
| 4242424242424242 | `visa` | Visa |
| 4000056655665556 | `visa_debit` | Visa (debit) |
| 5555555555554444 | `mastercard` | Mastercard |
| 5200828282828210 | `mastercard_debit` | Mastercard (debit) |
| 5105105105105100 | `mastercard_prepaid` | Mastercard (prepaid) |
| 378282246310005 | `amex` | American Express |
| 371449635398431 | `amex2` | American Express |
| 6011111111111117 | `discover` | Discover |
| 6011000990139424 | `discover2` | Discover |
| 3056930009020004 | `diners` | Diners Club |
| 36227206271667 | `diners_14digits` | Diners Club (14 digit card) |
| 3566002020360505 | `jcb` | JCB |
| 6200000000000005 | `unionpay` | UnionPay |
| 4506445006931933 | `interac` | Interac |
| 6280000360000978 | `eftpos_au_debit` | eftpos Australia |
| 4000050360000001 | `eftpos_au_visa_debit` | eftpos Australia/Visa |
| 5555050360000080 | `eftpos_au_mastercard_debit` | eftpos Australia/Mastercard |
| 4000002500001001 | `cartes_bancaires_visa_debit` | Cartes Bancaires (CB) / Visa |
| 5555552500001001 | `cartes_bancaires_mastercard_debit` | Cartes Bancaires (CB) / Mastercard |
| 4711009900000316877 | `girocard_debit` | Girocard |

### Test cards for specific success cases

| Test card number | Test payment method | Result |
| --- | --- | --- |
| 4001007020000002 | `offline_pin_cvm` | Simulates the cardholder being prompted for and entering an *offline PIN* (Offline PIN is a card verification method for EMV chip cards. These cards store the PIN securely on the chip itself, so PIN verification can occur without a network connection). The resulting charge has [cardholder_verification_method](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method) set to `offline_pin`. |
| 4000008260000075 | `offline_pin_sca_retry` | Simulates an [SCA](https://docs.stripe.com/strong-customer-authentication.md)-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to insert their card and enter their *offline PIN.* (Offline PIN is a card verification method for EMV chip cards. These cards store the PIN securely on the chip itself, so PIN verification can occur without a network connection) The resulting charge has [cardholder_verification_method](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method) set to `offline_pin`. |
| 4001000360000005 | `online_pin_cvm` | Simulates a cardholder being prompted for and entering an *online PIN* (Online PIN is a card verification method for EMV chip cards. These cards require the terminal to contact the issuer over a network connection to verify the PIN). The resulting charge has [cardholder_verification_method](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method) set to `online_pin`. |
| 4000002760000008 | `online_pin_sca_retry` | Simulates an [SCA](https://docs.stripe.com/strong-customer-authentication.md)-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to input their *online PIN.* (Online PIN is a card verification method for EMV chip cards. These cards require the terminal to contact the issuer over a network connection to verify the PIN) The final charge has [cardholder_verification_method](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method) set to `online_pin`. |

### Test cards for specific error cases

> Using these specific cards for [saving directly without charging](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md) and [SetupIntents](https://docs.stripe.com/api/setup_intents.md) returns a [setup_intent_authentication_failure](https://docs.stripe.com/error-codes.md#setup-intent-authentication-failure) response.

| Test card number | Test payment method | Result |
| --- | --- | --- |
| 4000000000000002 | `charge_declined` | Charge is declined with a `card_declined` code. |
| 4000000000009995 | `charge_declined_insufficient_funds` | Charge is declined with a `card_declined` code. The [decline_code](https://docs.stripe.com/declines/codes.md) attribute is `insufficient_funds`. |
| 4000000000009987 | `charge_declined_lost_card` | Charge is declined with a `card_declined` code. The [decline_code](https://docs.stripe.com/declines/codes.md) attribute is `lost_card`. |
| 4000000000009979 | `charge_declined_stolen_card` | Charge is declined with a `card_declined` code. The [decline_code](https://docs.stripe.com/declines/codes.md) attribute is `stolen_card`. |
| 4000000000000069 | `charge_declined_expired_card` | Charge is declined with an `expired_card` code. |
| 4000000000000119 | `charge_declined_processing_error` | Charge is declined with a `processing_error` code. |
| 4000000000005126 | `refund_fail` | Charge succeeds but [refunding a captured charge fails](https://docs.stripe.com/refunds.md#failed-refunds) asynchronously with a `failure_reason` of `expired_or_canceled_card`. Because refunds fail asynchronously, the refund appears successful at first, only returning the `failed` status in subsequent fetches. We also notify you of refund failures using the `refund.failed` [webhook](https://docs.stripe.com/api/events/types.md#event_types-refund.failed) event. |

## Simulated card presentment 

When using the server-driven integration, use the [present_payment_method](https://docs.stripe.com/api/terminal/readers/present_payment_method.md) endpoint to simulate a cardholder tapping or inserting their card on the reader.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_xxx/present_payment_method \
  -u "<<YOUR_SECRET_KEY>>:"
```

```json
{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "process_payment_intent": {
      "payment_intent": "pi_xxx"
    },
    "status": "succeeded",
    "type": "process_payment_intent"
  },
  …
}
```

If you don’t specify parameters, the simulated payment defaults to a valid [test card](https://docs.stripe.com/terminal/references/testing.md#standard-test-cards) based on the payment method type of the PaymentIntent. Below are the default test cards for Terminal payment method types:

| Payment method type | Test card number | Test payment method |
| --- | --- | --- |
| `card_present` | 4242424242424242 | `visa` |
| `card_present` and `interac_present` | 4242424242424242 | `visa` |
| `interac_present` | 4506445006931933 | `interac` |

When providing a test card number or other type-specific details, set `type` to the corresponding payment method type. For example, use this request to present a simulated Visa test card:

```curl
curl https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_xxx/present_payment_method \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=card_present \
  -d "card_present[number]=4242424242424242"
```

If you’re testing a `SetupIntent`, follow the server-driven instructions for [collecting a payment method to save](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md?terminal-sdk-platform=server-driven#collect-payment-method), including the customer consent and `allow_redisplay` requirements for `process_setup_intent`.

With the [standard test cards](https://docs.stripe.com/terminal/references/testing.md#standard-test-cards), you can also use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to simulate failure scenarios

## Test reader update 

Use reader software update scenarios to test how your integration handles updates. This works with simulated and physical mobile readers in a sandbox.

> `testReaderUpdate` is for sandbox connections only. Don’t set it when connecting to a live mode reader.

#### iOS

- [TestReaderUpdate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTestReaderUpdate.html)
- [TestReaderUpdateType (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPTestReaderUpdateType.html)
- [BluetoothConnectionConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfiguration.html)
- [UsbConnectionConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPUsbConnectionConfiguration.html)
- [TapToPayConnectionConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTapToPayConnectionConfiguration.html)

Set the `testReaderUpdate` property on [BluetoothConnectionConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfiguration.html), [UsbConnectionConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPUsbConnectionConfiguration.html), or [TapToPayConnectionConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTapToPayConnectionConfiguration.html) to trigger a reader update scenario during connection. This works with simulated and physical mobile readers, and with simulated Tap to Pay readers in a sandbox.

Create a [TestReaderUpdate](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTestReaderUpdate.html) with one of the factory methods. You can optionally specify [UpdateComponent](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPUpdateComponent.html) values such as `.firmware`, `.config`, `.keys`, or `.incremental`.

| TestReaderUpdate | Result |
| --- | --- |
| `.available(components)` | An optional update is available. Tell the user that an update is available and highlight the `requiredAt` date. |
| `.required(components)` | A required update runs during connection. Your `MobileReaderDelegate` receives the `didStartInstallingUpdate` callback. |
| `.requiredOffline(components)` | A required update exists. If you connect [offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md?terminal-card-present-integration=terminal&terminal-sdk-platform=ios&reader-type=simulated#connect-while-offline), the connection fails because the reader version isn’t allowed. If you connect online, the reader updates and connects normally. |
| `.lowBattery()` | A required update exists, but the reader battery is too low to start the update. The connection fails. |
| `.lowBatterySucceedConnect()` | A required update exists, but the reader battery is too low to start the update. The update fails, but the connection succeeds because the reader runs a recent software version. |
| `.random()` | Randomly selects one of the preceding scenarios, or `nil` to simulate no available update. |

#### Swift

```swift
// Create a TestReaderUpdate to simulate a required update during connection
let testReaderUpdate = TestReaderUpdate.required([.firmware, .config])

let connectionConfig: BluetoothConnectionConfiguration
do {
    connectionConfig = try BluetoothConnectionConfigurationBuilder(delegate: readerDelegate, locationId: ""{{LOCATION_ID}}"")
        .setTestReaderUpdate(testReaderUpdate)
        .build()
} catch {
    // Handle the error building the connection configuration
    return
}
Terminal.shared.connectReader(selectedReader, connectionConfig: connectionConfig) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectReader failed: \(error)")
    }
}
```

> `TapToPayConnectionConfiguration` only supports the `.required(components)` scenario. Other types return an error.

#### Android

- [TestReaderUpdate (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-test-reader-update/index.html)
- [TestReaderUpdateType (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-test-reader-update/-test-reader-update-type/index.html)
- [BluetoothConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/index.html)
- [UsbConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-usb-connection-configuration/index.html)

Set the `testReaderUpdate` parameter on [BluetoothConnectionConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/index.html) or [UsbConnectionConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-usb-connection-configuration/index.html) before you call `connectReader` to trigger a reader update during connection. This works with simulated readers and physical mobile readers in a sandbox.

Create a [TestReaderUpdate](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-test-reader-update/index.html) with one of the factory methods. You can optionally specify [UpdateComponent](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader-software-update/-update-component/index.html) values such as `FIRMWARE`, `CONFIG`, `KEYS`, or `INCREMENTAL`.

| TestReaderUpdate | Result |
| --- | --- |
| `.available(components)` | An optional update is available. Tell the user that an update is available and highlight the `requiredAt` date. |
| `.required(components)` | A required update runs during connection. Your `MobileReaderListener` receives the `onStartInstallingUpdate` callback. |
| `.requiredOffline(components)` | A required update exists. If you connect [offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md?terminal-card-present-integration=terminal&terminal-sdk-platform=android&reader-type=simulated#connect-while-offline), the connection fails because the reader version isn’t allowed. If you connect online, the reader updates and connects normally. |
| `.lowBattery()` | A required update exists, but the reader battery is too low to start the update. The connection fails. |
| `.lowBatterySucceedConnect()` | A required update exists, but the reader battery is too low to start the update. The update fails, but the connection succeeds because the reader runs a recent software version. |
| `.random()` | Randomly selects one of the preceding scenarios, or `null` to simulate no available update. |

#### Kotlin

```kotlin
// Create a TestReaderUpdate to simulate a required update during connection
val testReaderUpdate = TestReaderUpdate.required(
    setOf(
        ReaderSoftwareUpdate.UpdateComponent.FIRMWARE,
        ReaderSoftwareUpdate.UpdateComponent.CONFIG
    )
)

val connectionConfig = BluetoothConnectionConfiguration(
    ""{{LOCATION_ID}}"",
    autoReconnectOnUnexpectedDisconnect = true,
    bluetoothReaderListener = readerListener,
    testReaderUpdate = testReaderUpdate
)

Terminal.getInstance().connectReader(
    selectedReader,
    connectionConfig,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            println("Successfully connected to reader: $reader")
        }

        override fun onFailure(e: TerminalException) {
            println("connectReader failed: ${e.errorMessage}")
        }
    }
)
```

#### React Native

To trigger a reader update scenario during connection, set the `testReaderUpdate` parameter on `ConnectBluetoothReaderParams`, `ConnectBluetoothProximityReaderParams`, or `ConnectUsbReaderParams` before you call `connectReader`. This works with simulated and physical mobile readers in a sandbox.

Specify a `TestReaderUpdate` object with one of the following types. For update types that support it, you can specify an array of `UpdateComponent` values such as `FIRMWARE`, `CONFIG`, `KEYS`, or `INCREMENTAL` in the `components` field.

| TestReaderUpdate | Result |
| --- | --- |
| `{ type: 'available', components }` | An optional update is available. Tell the user that an update is available and highlight the `requiredAt` date. |
| `{ type: 'required', components }` | A required update runs during connection. Your `useStripeTerminal` instance receives the `onDidStartInstallingUpdate` callback. |
| `{ type: 'requiredOffline', components }` | A required update exists. If you connect offline, the connection fails because the reader version isn’t allowed. If you connect online, the reader updates and connects normally. |
| `{ type: 'lowBattery' }` | A required update exists, but the reader battery is too low to start the update. The connection fails. |
| `{ type: 'lowBatterySucceedConnect' }` | A required update exists, but the reader battery is too low to start the update. The update fails, but the connection succeeds because the reader runs a recent software version. |
| `{ type: 'random' }` | Randomly selects one of the preceding scenarios, or simulates no update being available. |

```typescript
import {
  useStripeTerminal,
  UpdateComponent,
} from '@stripe/stripe-terminal-react-native';

const { connectReader } = useStripeTerminal();

const { reader, error } = await connectReader({
  discoveryMethod: 'bluetoothScan',
  reader: selectedReader,
  locationId: '<location_id>',
  testReaderUpdate: {
    type: 'required',
    components: [UpdateComponent.FIRMWARE, UpdateComponent.CONFIG],
  },
});

if (error) {
  console.log(`connectReader failed: ${error.message}`);
  return;
}

console.log('Successfully connected to reader:', reader);
```

> `testReaderUpdate` in `ConnectTapToPayParams` is iOS only and supports `required` and `random` types, or omit it for no update. Setting it on Android returns an error.

## Physical test cards 

Test payments with your Stripe Terminal reader using a physical test card. You can purchase readers and physical test cards from the Terminal tab in the [Stripe Dashboard](https://dashboard.stripe.com/terminal/shop). We also support physical test cards from providers, such as [B2](https://b2ps.com/product-category/b2-payment-testing-products/).

This physical test card supports both chip entry and contactless payments. It only works with Stripe’s pre-certified readers, and only against the Stripe API in a [sandbox](https://docs.stripe.com/sandboxes.md). If you attempt to use your physical test card in live mode, the Stripe API returns an error. Unless stated otherwise, use the PIN `1234` when prompted.

When creating payments using a physical test card, use amounts ending in the following decimal values to produce specific responses:

| Decimal | Result |
| --- | --- |
| **00** | Payment is approved. |
| **01** | Payment is declined with a `call_issuer` code. |
| **02** | When using readers featuring a cardholder-facing screen, insert (or tap, if supported) the test card. If the card requires a PIN, the payment declines with `offline_pin_required` and requests PIN entry if the reader supports chip entry. Enter `1234` to complete the test payment. |
| **03** | When using readers featuring a cardholder-facing screen, insert (or tap, if supported) the test card. If the card requires a PIN, the payment declines with `online_or_offline_pin_required` and requests PIN entry. Enter any 4-digit PIN to complete the test payment. |
| **05** | Payment is declined with an `generic_decline` code. |
| **55** | Payment is declined with an `incorrect_pin` code. |
| **65** | Payment is declined with an `withdrawal_count_limit_exceeded` code. |
| **75** | Payment is declined with an `pin_try_exceeded` code. |

For example, a payment processed using a physical test card for the amount *25.00 USD* succeeds; a payment processed for the amount *10.05 USD* is declined.

> Some currencies have [zero decimal](https://docs.stripe.com/currencies.md#zero-decimal). For those currencies, use the two decimal digits in the table above as the rightmost two digits.
> 
> For example, to get your payment declined with `generic_decline` code, you need an amount of *105 JPY*.

### Interac test cards (Canada only) 

To test your Interac integration, you can use the simulated `interac` test card or an *Interac physical test card*. You can order it from the [Terminal hardware shop](https://dashboard.stripe.com/terminal/shop) in the Dashboard. You can’t use the Stripe-branded physical test card as an Interac card.

The Interac test card works for both `interac_present` payments and `interac_present` refunds. You can use the same [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) you use for testing `card_present` payments. Unless stated otherwise, use the PIN `1234` when prompted. To test a declined refund, create a partial refund with an amount ending with the following decimal values: `01`, `05`, `55`, `65`, or `75`.

> The Interac test card doesn’t support contactless payments.

### eftpos test cards (Australia only) 

To test your eftpos integration, you can use the simulated `eftpos` test card or an *eftpos physical test card*. You can order it from the [Terminal hardware shop](https://dashboard.stripe.com/terminal/shop) in the Dashboard. You can’t use the Stripe-branded physical test card as an `eftpos` card.

You can use the same [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) you use for testing `card_present` payments. Unless stated otherwise, use the PIN `1234` when prompted.

## See also

- [Place orders](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md)
- [Integration checklist](https://docs.stripe.com/terminal/references/checklist.md)
- [Test additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md#testing)

