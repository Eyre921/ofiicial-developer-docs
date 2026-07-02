---
title: "Get user subscription"
source: https://elevenlabs.io/docs/api-reference/user/subscription/get.md
path: docs/api-reference/user/subscription/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get user subscription

GET https://api.elevenlabs.io/v1/user/subscription

Gets extended information about the users subscription

Reference: https://elevenlabs.io/docs/api-reference/user/subscription/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/user/subscription:
    get:
      operationId: get
      summary: Get user subscription
      description: Gets extended information about the users subscription
      tags:
        - subpackage_user/subscription
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExtendedSubscriptionResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    ExtendedSubscriptionResponseModelMaxCreditLimitExtension:
      oneOf:
        - type: integer
        - type: string
          enum:
            - unlimited
      description: >-
        Maximum number of credits that the credit limit can be exceeded by.
        Managed by the workspace admin. `"unlimited"` means no cap, `0` means
        usage-based billing is disabled.
      title: ExtendedSubscriptionResponseModelMaxCreditLimitExtension
    Currency:
      type: string
      enum:
        - usd
        - eur
        - inr
        - pln
      title: Currency
    Price:
      type: object
      properties:
        amount:
          type: string
        currency:
          $ref: '#/components/schemas/Currency'
      required:
        - amount
        - currency
      description: Currency/amount pair.
      title: Price
    SubscriptionStatusType:
      type: string
      enum:
        - trialing
        - active
        - incomplete
        - past_due
        - free
        - free_disabled
      title: SubscriptionStatusType
    BillingPeriod:
      type: string
      enum:
        - monthly_period
        - 3_month_period
        - 6_month_period
        - annual_period
      title: BillingPeriod
    CharacterRefreshPeriod:
      type: string
      enum:
        - monthly_period
        - 3_month_period
        - 6_month_period
        - annual_period
      title: CharacterRefreshPeriod
    DiscountResponseModel:
      type: object
      properties:
        discount_percent_off:
          type:
            - number
            - 'null'
          format: double
          description: The discount applied to the invoice. E.g. [20.0f] for 20% off.
        discount_amount_off:
          type:
            - number
            - 'null'
          format: double
          description: The discount applied to the invoice. E.g. [20.0f] for 20 cents off.
      title: DiscountResponseModel
    InvoiceResponseModelPaymentIntentStatus:
      type: string
      enum:
        - canceled
        - processing
        - requires_action
        - requires_capture
        - requires_confirmation
        - requires_payment_method
        - succeeded
      description: >-
        Deprecated. Use [payment_intent_statusses] instead. The status of this
        invoice's first payment intent. None when there is no payment intent.
      title: InvoiceResponseModelPaymentIntentStatus
    InvoiceResponseModelPaymentIntentStatussesItems:
      type: string
      enum:
        - canceled
        - processing
        - requires_action
        - requires_capture
        - requires_confirmation
        - requires_payment_method
        - succeeded
      title: InvoiceResponseModelPaymentIntentStatussesItems
    InvoiceResponseModel:
      type: object
      properties:
        amount_due_cents:
          type: integer
          description: The amount due in cents.
        subtotal_cents:
          type:
            - integer
            - 'null'
          description: >-
            The subtotal amount in cents before tax (exclusive of tax and
            discounts).
        tax_cents:
          type:
            - integer
            - 'null'
          description: The tax amount in cents.
        discount_percent_off:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Deprecated. Use [discounts] instead. The discount applied to the
            invoice. E.g. [20.0f] for 20% off.
        discount_amount_off:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Deprecated. Use [discounts] instead. The discount applied to the
            invoice. E.g. [20.0f] for 20 cents off.
        discounts:
          type: array
          items:
            $ref: '#/components/schemas/DiscountResponseModel'
          description: The discounts applied to the invoice.
        next_payment_attempt_unix:
          type: integer
          description: >-
            The Unix timestamp of the next payment attempt. -1 when there is no
            next payment attempt.
        payment_intent_status:
          oneOf:
            - $ref: '#/components/schemas/InvoiceResponseModelPaymentIntentStatus'
            - type: 'null'
          description: >-
            Deprecated. Use [payment_intent_statusses] instead. The status of
            this invoice's first payment intent. None when there is no payment
            intent.
        payment_intent_statusses:
          type: array
          items:
            $ref: >-
              #/components/schemas/InvoiceResponseModelPaymentIntentStatussesItems
          description: >-
            The statuses of this invoice's payment intents. Empty list when
            there are no payment intents.
      required:
        - amount_due_cents
        - discounts
        - next_payment_attempt_unix
        - payment_intent_status
        - payment_intent_statusses
      title: InvoiceResponseModel
    PendingSubscriptionSwitchResponseModelNextTier:
      type: string
      enum:
        - free
        - starter
        - creator
        - pro
        - growing_business
        - scale_2024_08_10
        - grant_tier_1_2025_07_23
        - grant_tier_2_2025_07_23
        - trial
        - enterprise
      description: The tier to change to.
      title: PendingSubscriptionSwitchResponseModelNextTier
    PendingSubscriptionSwitchResponseModel:
      type: object
      properties:
        kind:
          type: string
          enum:
            - change
          default: change
        next_tier:
          $ref: '#/components/schemas/PendingSubscriptionSwitchResponseModelNextTier'
          description: The tier to change to.
        next_billing_period:
          $ref: '#/components/schemas/BillingPeriod'
          description: The billing period to change to.
        timestamp_seconds:
          type: integer
          description: The timestamp of the change.
      required:
        - next_tier
        - next_billing_period
        - timestamp_seconds
      title: PendingSubscriptionSwitchResponseModel
    PendingCancellationResponseModel:
      type: object
      properties:
        kind:
          type: string
          enum:
            - cancellation
          default: cancellation
        timestamp_seconds:
          type: integer
          description: The timestamp of the cancellation.
      required:
        - timestamp_seconds
      title: PendingCancellationResponseModel
    ExtendedSubscriptionResponseModelPendingChange:
      oneOf:
        - $ref: '#/components/schemas/PendingSubscriptionSwitchResponseModel'
        - $ref: '#/components/schemas/PendingCancellationResponseModel'
      description: The pending change for the user.
      title: ExtendedSubscriptionResponseModelPendingChange
    ExtendedSubscriptionResponseModel:
      type: object
      properties:
        tier:
          type: string
          description: The tier of the user's subscription.
        character_count:
          type: integer
          description: The number of characters used by the user.
        character_limit:
          type: integer
          description: >-
            The maximum number of characters allowed in the current billing
            period.
        max_character_limit_extension:
          type:
            - integer
            - 'null'
          description: >-
            Deprecated: use `max_credit_limit_extension`. Maximum number of
            characters that the character limit can be exceeded by. Managed by
            the workspace admin.
        max_credit_limit_extension:
          $ref: >-
            #/components/schemas/ExtendedSubscriptionResponseModelMaxCreditLimitExtension
          description: >-
            Maximum number of credits that the credit limit can be exceeded by.
            Managed by the workspace admin. `"unlimited"` means no cap, `0`
            means usage-based billing is disabled.
        can_extend_character_limit:
          type: boolean
          description: >-
            Whether the workspace is entitled to enter overages (usage-based
            billing).
        allowed_to_extend_character_limit:
          type: boolean
          description: >-
            Deprecated: use `max_credit_limit_extension != 0`. Whether the user
            is allowed to extend their character limit.
        next_character_count_reset_unix:
          type:
            - integer
            - 'null'
          description: The Unix timestamp of the next character count reset.
        voice_slots_used:
          type: integer
          description: The number of voice slots used by the user.
        professional_voice_slots_used:
          type: integer
          description: >-
            The number of professional voice slots used by the workspace/user if
            single seat.
        voice_limit:
          type: integer
          description: The maximum number of voice slots allowed for the user.
        max_voice_add_edits:
          type:
            - integer
            - 'null'
          description: The maximum number of voice add/edits allowed for the user.
        voice_add_edit_counter:
          type: integer
          description: The number of voice add/edits used by the user.
        professional_voice_limit:
          type: integer
          description: The maximum number of professional voices allowed for the user.
        can_extend_voice_limit:
          type: boolean
          description: Whether the user can extend their voice limit.
        can_use_instant_voice_cloning:
          type: boolean
          description: Whether the user can use instant voice cloning.
        can_use_professional_voice_cloning:
          type: boolean
          description: Whether the user can use professional voice cloning.
        currency:
          oneOf:
            - $ref: '#/components/schemas/Currency'
            - type: 'null'
          description: The currency of the user's subscription.
        current_overage:
          $ref: '#/components/schemas/Price'
          description: The current usage-based overage cost.
        status:
          $ref: '#/components/schemas/SubscriptionStatusType'
          description: The status of the user's subscription.
        billing_period:
          oneOf:
            - $ref: '#/components/schemas/BillingPeriod'
            - type: 'null'
          description: The billing period of the user's subscription.
        character_refresh_period:
          oneOf:
            - $ref: '#/components/schemas/CharacterRefreshPeriod'
            - type: 'null'
          description: The character refresh period of the user's subscription.
        next_invoice:
          oneOf:
            - $ref: '#/components/schemas/InvoiceResponseModel'
            - type: 'null'
          description: The next invoice for the user.
        open_invoices:
          type: array
          items:
            $ref: '#/components/schemas/InvoiceResponseModel'
          description: The open invoices for the user.
        has_open_invoices:
          type: boolean
          description: Whether the user has open invoices.
        pending_change:
          oneOf:
            - $ref: >-
                #/components/schemas/ExtendedSubscriptionResponseModelPendingChange
            - type: 'null'
          description: The pending change for the user.
        has_used_starter_coupon_on_account:
          type: boolean
          default: false
          description: >-
            True if any workspace owned by this user's auth account has redeemed
            the starter first-month discount coupon.
        has_used_creator_coupon_on_account:
          type: boolean
          default: false
          description: >-
            True if any workspace owned by this user's auth account has redeemed
            the creator first-month discount coupon.
      required:
        - tier
        - character_count
        - character_limit
        - max_character_limit_extension
        - max_credit_limit_extension
        - can_extend_character_limit
        - allowed_to_extend_character_limit
        - voice_slots_used
        - professional_voice_slots_used
        - voice_limit
        - voice_add_edit_counter
        - professional_voice_limit
        - can_extend_voice_limit
        - can_use_instant_voice_cloning
        - can_use_professional_voice_cloning
        - current_overage
        - status
        - open_invoices
        - has_open_invoices
      title: ExtendedSubscriptionResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Response**

```json
{
  "tier": "starter",
  "character_count": 1000,
  "character_limit": 10000,
  "max_character_limit_extension": 10000,
  "max_credit_limit_extension": 10000,
  "can_extend_character_limit": true,
  "allowed_to_extend_character_limit": true,
  "voice_slots_used": 1,
  "professional_voice_slots_used": 0,
  "voice_limit": 10,
  "voice_add_edit_counter": 0,
  "professional_voice_limit": 1,
  "can_extend_voice_limit": true,
  "can_use_instant_voice_cloning": true,
  "can_use_professional_voice_cloning": true,
  "current_overage": {
    "amount": "0",
    "currency": "usd"
  },
  "status": "active",
  "open_invoices": [
    {
      "amount_due_cents": 1000,
      "discounts": [
        {
          "discount_percent_off": 20
        }
      ],
      "next_payment_attempt_unix": 1738356858,
      "payment_intent_status": "processing",
      "payment_intent_statusses": [
        "processing",
        "succeeded"
      ],
      "subtotal_cents": 900,
      "tax_cents": 100
    }
  ],
  "has_open_invoices": true,
  "next_character_count_reset_unix": 1738356858,
  "currency": "usd",
  "billing_period": "monthly_period",
  "character_refresh_period": "monthly_period",
  "next_invoice": {
    "amount_due_cents": 1000,
    "discounts": [
      {
        "discount_percent_off": 20
      }
    ],
    "next_payment_attempt_unix": 1738356858,
    "payment_intent_status": "processing",
    "payment_intent_statusses": [
      "processing",
      "succeeded"
    ],
    "subtotal_cents": 900,
    "tax_cents": 100
  },
  "has_used_starter_coupon_on_account": false,
  "has_used_creator_coupon_on_account": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.user.subscription.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.user.subscription.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user/subscription"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/user/subscription")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user/subscription")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user/subscription');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user/subscription");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user/subscription")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
