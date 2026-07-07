---
title: "webhooks"
source: https://shopify.dev/docs/api/webhooks?reference=toml.md
path: docs/api/webhooks-reference-toml
---

---
title: Webhooks
description: >
  The list of all webhook topics you can subscribe to. You can use webhook
  subscriptions to receive notifications about particular events in a shop.   >
  Caution: If your app is distributed through the Shopify App Store, it must be
  subscribed to Shopify's [mandatory compliance
  topics](/docs/apps/build/privacy-law-compliance). You can create mandatory
  compliance webhook subscriptions either using your Partner Dashboard or by
  updating your [app configuration
  file](/docs/apps/build/cli-for-apps/app-configuration#app-configuration-file-example).
api_version: 2026-07
source_url:
  html: 'https://shopify.dev/docs/api/webhooks/latest'
  md: 'https://shopify.dev/docs/api/webhooks/latest.md'
api_name: webhooks
---

# Webhooks

The list of all webhook topics you can subscribe to. You can use webhook subscriptions to receive notifications about particular events in a shop.

**Caution:**

If your app is distributed through the Shopify App Store, it must be subscribed to Shopify's [mandatory compliance topics](https://shopify.dev/docs/apps/build/privacy-law-compliance). You can create mandatory compliance webhook subscriptions either using your Partner Dashboard or by updating your [app configuration file](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#app-configuration-file-example).

## Getting started

##### Creating subscriptions using the app configuration file

You can subscribe to most topics through your [app configuration file](https://shopify.dev/docs/apps/build/webhooks/get-started?framework=remix\&deliveryMethod=pubSub) using CLI version 3.63.0 or greater.

If you create and manage your subscriptions in your app configuration file, they will be used across all shops that your app is installed on.

##### Creating subscriptions using GraphQL Admin API

You can make app-specific subscriptions to all non-compliance topics through your app configuration file, or shop-specific subscriptions by Shopify's GraphQL Admin API.

For subscriptions managed with the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql), use the `webhookSubscriptionCreate` mutation. Specify the `$topic` and `$webhookSubscription` parameters to create subscriptions.

## Creating subscriptions using app configuration file

```toml
[webhooks]
api_version = "2023-04"


[[webhooks.subscriptions]]
topics = [
  "products/create",
  "products/update",
  "products/delete"
]
uri = "pubsub://example:pub-sub-topic1"


[[webhooks.subscriptions]]
topics = ["orders/create"]
uri = "pubsub://example:pub-sub-topic2"
```

## Creating subscriptions using GraphQL Admin API

```graphql
mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {
  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {
    webhookSubscription {
      id
      topic
      format
      includeFields
      uri
    }
  }
}
```

***

## List of topics

All webhook topics you can subscribe to.

### Examples

* #### app\_purchases\_one\_time/update: Sample Payload

  #####

  ```undefined
  {
    "app_purchase_one_time": {
      "admin_graphql_api_id": "gid://shopify/AppPurchaseOneTime/1017262364",
      "name": "Webhook Test",
      "status": "PENDING",
      "admin_graphql_api_shop_id": "gid://shopify/Shop/548380009",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00"
    }
  }
  ```

* #### app\_subscriptions/approaching\_capped\_amount: Sample Payload

  #####

  ```undefined
  {
    "app_subscription": {
      "admin_graphql_api_id": "gid://shopify/AppSubscription/1029266968",
      "name": "Webhook Test",
      "balance_used": 0,
      "capped_amount": "20.0",
      "currency_code": "USD",
      "admin_graphql_api_shop_id": "gid://shopify/Shop/548380009",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00"
    }
  }
  ```

* #### app\_subscriptions/update: Sample Payload

  #####

  ```undefined
  {
    "app_subscription": {
      "admin_graphql_api_id": "gid://shopify/AppSubscription/1029266977",
      "name": "Webhook Test",
      "status": "PENDING",
      "admin_graphql_api_shop_id": "gid://shopify/Shop/548380009",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "currency": "USD",
      "capped_amount": "20.0",
      "price": "10.00",
      "interval": "every_30_days",
      "plan_handle": "plan-123"
    }
  }
  ```

* #### app/scopes\_update: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "shop_id": "gid://shopify/Shop/548380009",
    "previous": [
      "read_products"
    ],
    "current": [
      "read_products",
      "write_products"
    ],
    "updated_at": "2024-06-25T00:00:00.000Z"
  }
  ```

* #### app/uninstalled: Sample Payload

  #####

  ```undefined
  {
    "id": 548380009,
    "name": "Super Toys",
    "email": "super@supertoys.com",
    "domain": null,
    "province": "Tennessee",
    "country": "US",
    "address1": "190 MacLaren Street",
    "zip": "37178",
    "city": "Houston",
    "source": null,
    "phone": "3213213210",
    "latitude": null,
    "longitude": null,
    "primary_locale": "en",
    "address2": null,
    "created_at": null,
    "updated_at": null,
    "country_code": "US",
    "country_name": "United States",
    "currency": "USD",
    "customer_email": "super@supertoys.com",
    "timezone": "(GMT-05:00) Eastern Time (US & Canada)",
    "iana_timezone": null,
    "shop_owner": "John Smith",
    "money_format": "${{amount}}",
    "money_with_currency_format": "${{amount}} USD",
    "weight_unit": "kg",
    "province_code": "TN",
    "taxes_included": null,
    "auto_configure_tax_inclusivity": null,
    "tax_shipping": null,
    "county_taxes": null,
    "plan_display_name": "Shopify Plus",
    "plan_name": "enterprise",
    "has_discounts": false,
    "has_gift_cards": true,
    "myshopify_domain": null,
    "google_apps_domain": null,
    "google_apps_login_enabled": null,
    "money_in_emails_format": "${{amount}}",
    "money_with_currency_in_emails_format": "${{amount}} USD",
    "eligible_for_payments": true,
    "requires_extra_payments_agreement": false,
    "password_enabled": null,
    "has_storefront": true,
    "finances": true,
    "primary_location_id": 655441491,
    "checkout_api_supported": true,
    "multi_location_enabled": true,
    "setup_required": false,
    "pre_launch_enabled": false,
    "enabled_presentment_currencies": [
      "USD"
    ],
    "marketing_sms_consent_enabled_at_checkout": false,
    "transactional_sms_disabled": false
  }
  ```

* #### audit\_events/admin\_api\_activity: Sample Payload

  #####

  ```undefined
  {
    "events": [
      {
        "time": 1634678724,
        "event": {
          "context": {
            "context_type": "network_request",
            "context_identifier": "13493be9-24f2-4eea-b71d-a8acd7af7917",
            "context_metadata": {
              "client_ip": "192.168.64.1",
              "content_type": "json",
              "response_time_ms": 116.47000000812113,
              "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
              "api_request_failed": false,
              "response_code": 200
            }
          },
          "action": "api_request",
          "actor": {
            "actor_type": "app",
            "actor_identifier": 4,
            "actor_metadata": {
              "app_name": "Private app",
              "api_version_requested": "unstable",
              "api_version_served": "unstable",
              "ecosystem_category": "private"
            },
            "on_behalf_of": {
              "user_email": "dev@example.com"
            }
          },
          "subject": {
            "subject_type": "shop",
            "subject_identifier": "shop1.myshopify.io",
            "subject_metadata": {}
          },
          "timestamp": "2021-10-19T21:25:24Z",
          "additional_metadata": {
            "request_type": "GraphQL",
            "mutation_names": [],
            "query": "query orders {\n  orders(first: $first) {\n    edges {\n      node {\n        id\n      }\n    }\n  }\n}",
            "variables": {
              "first": 10
            },
            "error_codes": []
          }
        }
      }
    ]
  }
  ```

* #### bulk\_operations/finish: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/BulkOperation/147595010",
    "completed_at": "2024-01-01T07:34:56-05:00",
    "created_at": "2026-07-01T12:17:28-04:00",
    "error_code": null,
    "status": "completed",
    "type": "query"
  }
  ```

* #### carts/create: Sample Payload

  #####

  ```undefined
  {
    "id": "exampleCartId",
    "token": "exampleCartId",
    "line_items": [
      {
        "id": 704912205188288575,
        "properties": null,
        "quantity": 3,
        "variant_id": 704912205188288575,
        "key": "704912205188288575:3abdf474dce81d0025dd15b9a02ef6bf",
        "discounted_price": "19.99",
        "discounts": [],
        "gift_card": false,
        "grams": 200,
        "line_price": "59.97",
        "original_line_price": "59.97",
        "original_price": "19.99",
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": "example-shirt-s",
        "taxable": true,
        "title": "Example T-Shirt - Small",
        "total_discount": "39.98",
        "vendor": "Acme",
        "discounted_price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "line_price_set": {
          "shop_money": {
            "amount": "59.97",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "59.97",
            "currency_code": "USD"
          }
        },
        "original_line_price_set": {
          "shop_money": {
            "amount": "59.97",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "59.97",
            "currency_code": "USD"
          }
        },
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "39.98",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "39.98",
            "currency_code": "USD"
          }
        },
        "parent_relationship": null
      }
    ],
    "note": null,
    "updated_at": "2022-01-01T00:00:00.000Z",
    "created_at": "2022-01-01T00:00:00.000Z"
  }
  ```

* #### carts/update: Sample Payload

  #####

  ```undefined
  {
    "id": "exampleCartId",
    "token": "exampleCartId",
    "line_items": [
      {
        "id": 704912205188288575,
        "properties": null,
        "quantity": 3,
        "variant_id": 704912205188288575,
        "key": "704912205188288575:3abdf474dce81d0025dd15b9a02ef6bf",
        "discounted_price": "19.99",
        "discounts": [],
        "gift_card": false,
        "grams": 200,
        "line_price": "59.97",
        "original_line_price": "59.97",
        "original_price": "19.99",
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": "example-shirt-s",
        "taxable": true,
        "title": "Example T-Shirt - Small",
        "total_discount": "39.98",
        "vendor": "Acme",
        "discounted_price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "line_price_set": {
          "shop_money": {
            "amount": "59.97",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "59.97",
            "currency_code": "USD"
          }
        },
        "original_line_price_set": {
          "shop_money": {
            "amount": "59.97",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "59.97",
            "currency_code": "USD"
          }
        },
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "39.98",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "39.98",
            "currency_code": "USD"
          }
        },
        "parent_relationship": null
      }
    ],
    "note": null,
    "updated_at": "2022-01-01T00:00:00.000Z",
    "created_at": "2022-01-01T00:00:00.000Z"
  }
  ```

* #### channels/delete: Sample Payload

  #####

  ```undefined
  {
    "id": "123456789"
  }
  ```

* #### checkouts/create: Sample Payload

  #####

  ```undefined
  {
    "token": "123123123",
    "cart_token": "eeafa272cebfd4b22385bc4b645e762c",
    "email": "example@email.com",
    "gateway": null,
    "buyer_accepts_marketing": false,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "landing_site": null,
    "note": null,
    "note_attributes": [],
    "referring_site": null,
    "shipping_lines": [],
    "taxes_included": false,
    "total_weight": 1133,
    "currency": "USD",
    "completed_at": null,
    "closed_at": null,
    "user_id": null,
    "location_id": null,
    "source_identifier": null,
    "source_url": null,
    "device_id": null,
    "phone": null,
    "customer_locale": null,
    "line_items": [
      {
        "applied_discounts": [],
        "discount_allocations": [],
        "key": "139cb5712fb4c8d9957dcfad9a3028da",
        "destination_location_id": 1015975142,
        "fulfillment_service": "manual",
        "gift_card": false,
        "grams": 567,
        "origin_location_id": 1015975141,
        "presentment_title": "IPod Nano - 8GB",
        "presentment_variant_title": "Pink",
        "product_id": 632910392,
        "properties": null,
        "quantity": 1,
        "requires_shipping": true,
        "sku": "IPOD2008PINK",
        "tax_lines": [
          {
            "price": "11.94",
            "position": 1,
            "rate": 0.06,
            "title": "Tax",
            "source": "Shopify",
            "zone": "province",
            "jurisdiction_id": null,
            "jurisdiction_type": null,
            "jurisdiction_source": null,
            "reporting_taxable_amount": null,
            "reporting_non_taxable_amount": null,
            "reporting_exempt_amount": null,
            "reporting_jurisdiction_name": null,
            "reporting_jurisdiction_type": null,
            "reporting_jurisdiction_code": null,
            "tax_api_client_id": null,
            "tax_calculation_price": "11.94",
            "tax_registration_id": null,
            "compare_at": 0.06,
            "channel_liable": false
          }
        ],
        "taxable": true,
        "title": "IPod Nano - 8GB",
        "variant_id": 808950810,
        "variant_title": "Pink",
        "variant_price": "199.00",
        "vendor": "Apple",
        "user_id": null,
        "unit_price_measurement": {
          "measured_type": null,
          "quantity_value": null,
          "quantity_unit": null,
          "reference_value": null,
          "reference_unit": null
        },
        "rank": null,
        "compare_at_price": null,
        "line_price": "199.00",
        "price": "199.00"
      },
      {
        "applied_discounts": [],
        "discount_allocations": [],
        "key": "139cb5712fb4c8d9957dcfad9a3028da",
        "destination_location_id": 1015975142,
        "fulfillment_service": "manual",
        "gift_card": false,
        "grams": 567,
        "origin_location_id": 1015975141,
        "presentment_title": "IPod Nano - 8GB",
        "presentment_variant_title": "Pink",
        "product_id": 632910392,
        "properties": null,
        "quantity": 1,
        "requires_shipping": true,
        "sku": "IPOD2008PINK",
        "tax_lines": [
          {
            "price": "11.94",
            "position": 1,
            "rate": 0.06,
            "title": "Tax",
            "source": "Shopify",
            "zone": "province",
            "jurisdiction_id": null,
            "jurisdiction_type": null,
            "jurisdiction_source": null,
            "reporting_taxable_amount": null,
            "reporting_non_taxable_amount": null,
            "reporting_exempt_amount": null,
            "reporting_jurisdiction_name": null,
            "reporting_jurisdiction_type": null,
            "reporting_jurisdiction_code": null,
            "tax_api_client_id": null,
            "tax_calculation_price": "11.94",
            "tax_registration_id": null,
            "compare_at": 0.06,
            "channel_liable": false
          }
        ],
        "taxable": true,
        "title": "IPod Nano - 8GB",
        "variant_id": 808950810,
        "variant_title": "Pink",
        "variant_price": "199.00",
        "vendor": "Apple",
        "user_id": null,
        "unit_price_measurement": {
          "measured_type": null,
          "quantity_value": null,
          "quantity_unit": null,
          "reference_value": null,
          "reference_unit": null
        },
        "rank": null,
        "compare_at_price": null,
        "line_price": "199.00",
        "price": "199.00"
      }
    ],
    "name": "#981820079255243537",
    "source": null,
    "abandoned_checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token",
    "discount_codes": [],
    "tax_lines": [
      {
        "price": "23.88",
        "rate": 0.06,
        "title": "Tax",
        "channel_liable": false
      }
    ],
    "source_name": "web",
    "presentment_currency": "USD",
    "buyer_accepts_sms_marketing": false,
    "sms_marketing_phone": null,
    "total_discounts": "0.00",
    "total_line_items_price": "398.00",
    "total_price": "421.88",
    "total_tax": "23.88",
    "subtotal_price": "398.00",
    "total_duties": null,
    "reservation_token": null,
    "billing_address": {
      "first_name": "Bob",
      "address1": "123 Billing Street",
      "phone": "555-555-BILL",
      "city": "Billtown",
      "zip": "K2P0B0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Biller",
      "address2": null,
      "company": "My Company",
      "latitude": null,
      "longitude": null,
      "name": "Bob Biller",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "K2P0S0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 603851970716743426,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/603851970716743426",
      "default_address": {
        "id": null,
        "customer_id": 603851970716743426,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    }
  }
  ```

* #### checkouts/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 981820079255243537,
    "presentment_currency": "USD",
    "buyer_accepts_sms_marketing": false,
    "sms_marketing_phone": null,
    "total_discounts": "0.00",
    "total_line_items_price": "398.00",
    "total_price": "398.00",
    "total_tax": "0.00",
    "subtotal_price": "398.00",
    "cart_token": "eeafa272cebfd4b22385bc4b645e762c",
    "total_duties": null,
    "reservation_token": null
  }
  ```

* #### checkouts/update: Sample Payload

  #####

  ```undefined
  {
    "token": "123123123",
    "cart_token": "eeafa272cebfd4b22385bc4b645e762c",
    "email": "example@email.com",
    "gateway": null,
    "buyer_accepts_marketing": false,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "landing_site": null,
    "note": null,
    "note_attributes": [],
    "referring_site": null,
    "shipping_lines": [],
    "taxes_included": false,
    "total_weight": 1133,
    "currency": "USD",
    "completed_at": null,
    "closed_at": null,
    "user_id": null,
    "location_id": null,
    "source_identifier": null,
    "source_url": null,
    "device_id": null,
    "phone": null,
    "customer_locale": null,
    "line_items": [
      {
        "applied_discounts": [],
        "discount_allocations": [],
        "key": "139cb5712fb4c8d9957dcfad9a3028da",
        "destination_location_id": 1015975142,
        "fulfillment_service": "manual",
        "gift_card": false,
        "grams": 567,
        "origin_location_id": 1015975141,
        "presentment_title": "IPod Nano - 8GB",
        "presentment_variant_title": "Pink",
        "product_id": 632910392,
        "properties": null,
        "quantity": 1,
        "requires_shipping": true,
        "sku": "IPOD2008PINK",
        "tax_lines": [
          {
            "price": "11.94",
            "position": 1,
            "rate": 0.06,
            "title": "Tax",
            "source": "Shopify",
            "zone": "province",
            "jurisdiction_id": null,
            "jurisdiction_type": null,
            "jurisdiction_source": null,
            "reporting_taxable_amount": null,
            "reporting_non_taxable_amount": null,
            "reporting_exempt_amount": null,
            "reporting_jurisdiction_name": null,
            "reporting_jurisdiction_type": null,
            "reporting_jurisdiction_code": null,
            "tax_api_client_id": null,
            "tax_calculation_price": "11.94",
            "tax_registration_id": null,
            "compare_at": 0.06,
            "channel_liable": false
          }
        ],
        "taxable": true,
        "title": "IPod Nano - 8GB",
        "variant_id": 808950810,
        "variant_title": "Pink",
        "variant_price": "199.00",
        "vendor": "Apple",
        "user_id": null,
        "unit_price_measurement": {
          "measured_type": null,
          "quantity_value": null,
          "quantity_unit": null,
          "reference_value": null,
          "reference_unit": null
        },
        "rank": null,
        "compare_at_price": null,
        "line_price": "199.00",
        "price": "199.00"
      },
      {
        "applied_discounts": [],
        "discount_allocations": [],
        "key": "139cb5712fb4c8d9957dcfad9a3028da",
        "destination_location_id": 1015975142,
        "fulfillment_service": "manual",
        "gift_card": false,
        "grams": 567,
        "origin_location_id": 1015975141,
        "presentment_title": "IPod Nano - 8GB",
        "presentment_variant_title": "Pink",
        "product_id": 632910392,
        "properties": null,
        "quantity": 1,
        "requires_shipping": true,
        "sku": "IPOD2008PINK",
        "tax_lines": [
          {
            "price": "11.94",
            "position": 1,
            "rate": 0.06,
            "title": "Tax",
            "source": "Shopify",
            "zone": "province",
            "jurisdiction_id": null,
            "jurisdiction_type": null,
            "jurisdiction_source": null,
            "reporting_taxable_amount": null,
            "reporting_non_taxable_amount": null,
            "reporting_exempt_amount": null,
            "reporting_jurisdiction_name": null,
            "reporting_jurisdiction_type": null,
            "reporting_jurisdiction_code": null,
            "tax_api_client_id": null,
            "tax_calculation_price": "11.94",
            "tax_registration_id": null,
            "compare_at": 0.06,
            "channel_liable": false
          }
        ],
        "taxable": true,
        "title": "IPod Nano - 8GB",
        "variant_id": 808950810,
        "variant_title": "Pink",
        "variant_price": "199.00",
        "vendor": "Apple",
        "user_id": null,
        "unit_price_measurement": {
          "measured_type": null,
          "quantity_value": null,
          "quantity_unit": null,
          "reference_value": null,
          "reference_unit": null
        },
        "rank": null,
        "compare_at_price": null,
        "line_price": "199.00",
        "price": "199.00"
      }
    ],
    "name": "#981820079255243537",
    "source": null,
    "abandoned_checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token",
    "discount_codes": [],
    "tax_lines": [
      {
        "price": "23.88",
        "rate": 0.06,
        "title": "Tax",
        "channel_liable": false
      }
    ],
    "source_name": "web",
    "presentment_currency": "USD",
    "buyer_accepts_sms_marketing": false,
    "sms_marketing_phone": null,
    "total_discounts": "0.00",
    "total_line_items_price": "398.00",
    "total_price": "421.88",
    "total_tax": "23.88",
    "subtotal_price": "398.00",
    "total_duties": null,
    "reservation_token": null,
    "billing_address": {
      "first_name": "Bob",
      "address1": "123 Billing Street",
      "phone": "555-555-BILL",
      "city": "Billtown",
      "zip": "K2P0B0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Biller",
      "address2": null,
      "company": "My Company",
      "latitude": null,
      "longitude": null,
      "name": "Bob Biller",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "K2P0S0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 603851970716743426,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/603851970716743426",
      "default_address": {
        "id": null,
        "customer_id": 603851970716743426,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    }
  }
  ```

* #### collection\_listings/add: Sample Payload

  #####

  ```undefined
  {
    "collection_listing": {
      "collection_id": 408372092144951419,
      "updated_at": null,
      "body_html": "<b>Some HTML</b>",
      "default_product_image": null,
      "handle": "mynewcollection",
      "image": null,
      "title": "My New Collection",
      "sort_order": null,
      "published_at": "2021-12-31T19:00:00-05:00"
    }
  }
  ```

* #### collection\_listings/remove: Sample Payload

  #####

  ```undefined
  {
    "collection_listing": {
      "collection_id": 408372092144951419
    }
  }
  ```

* #### collection\_listings/update: Sample Payload

  #####

  ```undefined
  {
    "collection_listing": {
      "collection_id": 408372092144951419,
      "updated_at": null,
      "body_html": "<b>Some HTML</b>",
      "default_product_image": null,
      "handle": "mynewcollection",
      "image": null,
      "title": "My New Collection",
      "sort_order": null,
      "published_at": "2021-12-31T19:00:00-05:00"
    }
  }
  ```

* #### collection\_publications/create: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "publication_id": 123456,
    "published_at": "2021-12-31T19:00:00-05:00",
    "published": true,
    "created_at": null,
    "updated_at": null,
    "collection_id": 408372092144951419
  }
  ```

* #### collection\_publications/delete: Sample Payload

  #####

  ```undefined
  {
    "id": null
  }
  ```

* #### collection\_publications/update: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "publication_id": 123456,
    "published_at": "2021-12-31T19:00:00-05:00",
    "published": true,
    "created_at": null,
    "updated_at": null,
    "collection_id": 408372092144951419
  }
  ```

* #### collections/create: Sample Payload

  #####

  ```undefined
  {
    "id": 408372092144951419,
    "handle": "mynewcollection",
    "title": "My New Collection",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "body_html": "<b>Some HTML</b>",
    "published_at": "2021-12-31T16:00:00-05:00",
    "sort_order": null,
    "template_suffix": null,
    "published_scope": "web",
    "admin_graphql_api_id": "gid://shopify/Collection/408372092144951419"
  }
  ```

* #### collections/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 408372092144951419,
    "published_scope": "web",
    "admin_graphql_api_id": "gid://shopify/Collection/408372092144951419"
  }
  ```

* #### collections/update: Sample Payload

  #####

  ```undefined
  {
    "id": 408372092144951419,
    "handle": "mynewcollection",
    "title": "My New Collection",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "body_html": "<b>Some HTML</b>",
    "published_at": "2021-12-31T16:00:00-05:00",
    "sort_order": null,
    "template_suffix": null,
    "published_scope": "web",
    "admin_graphql_api_id": "gid://shopify/Collection/408372092144951419"
  }
  ```

* #### companies/create: Sample Payload

  #####

  ```undefined
  {
    "name": "Example Company",
    "note": "This is an example company",
    "external_id": "123456789",
    "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "customer_since": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
  }
  ```

* #### companies/delete: Sample Payload

  #####

  ```undefined
  {
    "name": "Example Company",
    "note": "This is an example company",
    "external_id": "123456789",
    "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "customer_since": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
  }
  ```

* #### companies/update: Sample Payload

  #####

  ```undefined
  {
    "name": "Example Company",
    "note": "This is an example company",
    "external_id": "123456789",
    "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "customer_since": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
  }
  ```

* #### company\_contact\_roles/assign: Sample Payload

  #####

  ```undefined
  {
    "company_contact": {
      "customer_admin_graphql_api_id": "gid://shopify/Customer/12123842227812391",
      "title": "Buyer",
      "locale": "en",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951419",
      "company": {
        "name": "Example Company",
        "note": "This is an example company",
        "external_id": "123456789",
        "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "customer_since": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      }
    },
    "company_location": {
      "name": "Montreal",
      "external_id": "123456789",
      "phone": "555-555-5555",
      "locale": "en",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "note": "Head Office Location",
      "buyer_experience_configuration": null,
      "admin_graphql_api_id": "gid://shopify/CompanyLocation/408372092144951419",
      "tax_exemptions": [
        "CA_BC_CONTRACTOR_EXEMPTION",
        "CA_BC_RESELLER_EXEMPTION"
      ],
      "tax_settings": {
        "tax_registration_id": "1214214141",
        "tax_exempt": null,
        "tax_exemptions": [
          "CA_BC_CONTRACTOR_EXEMPTION",
          "CA_BC_RESELLER_EXEMPTION"
        ]
      },
      "company": {
        "name": "Example Company",
        "note": "This is an example company",
        "external_id": "123456789",
        "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "customer_since": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "billing_address": {
        "address1": "175 Sherbrooke Street West",
        "city": "Montreal",
        "province": "Quebec",
        "country": "Canada",
        "zip": "H3A 0G4",
        "recipient": "Adam Felix",
        "first_name": null,
        "last_name": null,
        "address2": null,
        "phone": "+49738001239",
        "zone_code": "QC",
        "country_code": "CA",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
        "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "shipping_address": {
        "address1": "175 Sherbrooke Street West",
        "city": "Montreal",
        "province": "Quebec",
        "country": "Canada",
        "zip": "H3A 0G4",
        "recipient": "Adam Felix",
        "first_name": null,
        "last_name": null,
        "address2": null,
        "phone": "+49738001239",
        "zone_code": "QC",
        "country_code": "CA",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
        "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "tax_registration": {
        "tax_id": "1214214141"
      }
    },
    "company_contact_role": {
      "name": "Location Admin"
    }
  }
  ```

* #### company\_contact\_roles/revoke: Sample Payload

  #####

  ```undefined
  {
    "company_contact": {
      "customer_admin_graphql_api_id": "gid://shopify/Customer/12123842227812391",
      "title": "Buyer",
      "locale": "en",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951419",
      "company": {
        "name": "Example Company",
        "note": "This is an example company",
        "external_id": "123456789",
        "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "customer_since": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      }
    },
    "company_location": {
      "name": "Montreal",
      "external_id": "123456789",
      "phone": "555-555-5555",
      "locale": "en",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "note": "Head Office Location",
      "buyer_experience_configuration": null,
      "admin_graphql_api_id": "gid://shopify/CompanyLocation/408372092144951419",
      "tax_exemptions": [
        "CA_BC_CONTRACTOR_EXEMPTION",
        "CA_BC_RESELLER_EXEMPTION"
      ],
      "tax_settings": {
        "tax_registration_id": "1214214141",
        "tax_exempt": null,
        "tax_exemptions": [
          "CA_BC_CONTRACTOR_EXEMPTION",
          "CA_BC_RESELLER_EXEMPTION"
        ]
      },
      "company": {
        "name": "Example Company",
        "note": "This is an example company",
        "external_id": "123456789",
        "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "customer_since": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "billing_address": {
        "address1": "175 Sherbrooke Street West",
        "city": "Montreal",
        "province": "Quebec",
        "country": "Canada",
        "zip": "H3A 0G4",
        "recipient": "Adam Felix",
        "first_name": null,
        "last_name": null,
        "address2": null,
        "phone": "+49738001239",
        "zone_code": "QC",
        "country_code": "CA",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
        "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "shipping_address": {
        "address1": "175 Sherbrooke Street West",
        "city": "Montreal",
        "province": "Quebec",
        "country": "Canada",
        "zip": "H3A 0G4",
        "recipient": "Adam Felix",
        "first_name": null,
        "last_name": null,
        "address2": null,
        "phone": "+49738001239",
        "zone_code": "QC",
        "country_code": "CA",
        "created_at": "2021-12-31T19:00:00-05:00",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
        "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
      },
      "tax_registration": {
        "tax_id": "1214214141"
      }
    },
    "company_contact_role": {
      "name": "Location Admin"
    }
  }
  ```

* #### company\_contacts/create: Sample Payload

  #####

  ```undefined
  {
    "customer_admin_graphql_api_id": "gid://shopify/Customer/12123842227812391",
    "title": "Buyer",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951419",
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    }
  }
  ```

* #### company\_contacts/delete: Sample Payload

  #####

  ```undefined
  {
    "customer_admin_graphql_api_id": "gid://shopify/Customer/12123842227812391",
    "title": "Buyer",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951419",
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    }
  }
  ```

* #### company\_contacts/update: Sample Payload

  #####

  ```undefined
  {
    "customer_admin_graphql_api_id": "gid://shopify/Customer/12123842227812391",
    "title": "Buyer",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951419",
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    }
  }
  ```

* #### company\_locations/create: Sample Payload

  #####

  ```undefined
  {
    "name": "Montreal",
    "external_id": "123456789",
    "phone": "555-555-5555",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "note": "Head Office Location",
    "buyer_experience_configuration": null,
    "admin_graphql_api_id": "gid://shopify/CompanyLocation/408372092144951419",
    "tax_exemptions": [
      "CA_BC_CONTRACTOR_EXEMPTION",
      "CA_BC_RESELLER_EXEMPTION"
    ],
    "tax_settings": {
      "tax_registration_id": "1214214141",
      "tax_exempt": null,
      "tax_exemptions": [
        "CA_BC_CONTRACTOR_EXEMPTION",
        "CA_BC_RESELLER_EXEMPTION"
      ]
    },
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "billing_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "shipping_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "tax_registration": {
      "tax_id": "1214214141"
    }
  }
  ```

* #### company\_locations/delete: Sample Payload

  #####

  ```undefined
  {
    "name": "Montreal",
    "external_id": "123456789",
    "phone": "555-555-5555",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "note": "Head Office Location",
    "buyer_experience_configuration": null,
    "admin_graphql_api_id": "gid://shopify/CompanyLocation/408372092144951419",
    "tax_exemptions": [
      "CA_BC_CONTRACTOR_EXEMPTION",
      "CA_BC_RESELLER_EXEMPTION"
    ],
    "tax_settings": {
      "tax_registration_id": "1214214141",
      "tax_exempt": null,
      "tax_exemptions": [
        "CA_BC_CONTRACTOR_EXEMPTION",
        "CA_BC_RESELLER_EXEMPTION"
      ]
    },
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "billing_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "shipping_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "tax_registration": {
      "tax_id": "1214214141"
    }
  }
  ```

* #### company\_locations/update: Sample Payload

  #####

  ```undefined
  {
    "name": "Montreal",
    "external_id": "123456789",
    "phone": "555-555-5555",
    "locale": "en",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "note": "Head Office Location",
    "buyer_experience_configuration": null,
    "admin_graphql_api_id": "gid://shopify/CompanyLocation/408372092144951419",
    "tax_exemptions": [
      "CA_BC_CONTRACTOR_EXEMPTION",
      "CA_BC_RESELLER_EXEMPTION"
    ],
    "tax_settings": {
      "tax_registration_id": "1214214141",
      "tax_exempt": null,
      "tax_exemptions": [
        "CA_BC_CONTRACTOR_EXEMPTION",
        "CA_BC_RESELLER_EXEMPTION"
      ]
    },
    "company": {
      "name": "Example Company",
      "note": "This is an example company",
      "external_id": "123456789",
      "main_contact_admin_graphql_api_id": "gid://shopify/CompanyContact/408372092144951652",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "customer_since": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "billing_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "shipping_address": {
      "address1": "175 Sherbrooke Street West",
      "city": "Montreal",
      "province": "Quebec",
      "country": "Canada",
      "zip": "H3A 0G4",
      "recipient": "Adam Felix",
      "first_name": null,
      "last_name": null,
      "address2": null,
      "phone": "+49738001239",
      "zone_code": "QC",
      "country_code": "CA",
      "created_at": "2021-12-31T19:00:00-05:00",
      "updated_at": "2021-12-31T19:00:00-05:00",
      "admin_graphql_api_id": "gid://shopify/CompanyAddress/141016871799219115",
      "company_admin_graphql_api_id": "gid://shopify/Company/408372092144951419"
    },
    "tax_registration": {
      "tax_id": "1214214141"
    }
  }
  ```

* #### customer\_account\_settings/update: Sample Payload

  #####

  ```undefined
  {
    "url": null,
    "customer_accounts_version": "classic",
    "login_required_at_checkout": true,
    "login_links_visible_on_storefront_and_checkout": true
  }
  ```

* #### customer\_groups/create: Sample Payload

  #####

  ```undefined
  {
    "id": 239443597569284757,
    "name": "Bob Customers",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "query": "email:bob*"
  }
  ```

* #### customer\_groups/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 239443597569284757
  }
  ```

* #### customer\_groups/update: Sample Payload

  #####

  ```undefined
  {
    "id": 239443597569284757,
    "name": "Bob Customers",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "query": "email:bob*"
  }
  ```

* #### customer\_payment\_methods/create: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",
    "token": "0eccccc666aac73efcd31094ddc4ebf0",
    "customer_id": 82850125,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/82850125",
    "instrument_type": "CustomerCreditCard",
    "payment_instrument": {
      "last_digits": "4242",
      "month": 8,
      "year": 2060,
      "name": "Jim Smith",
      "brand": "Visa"
    },
    "resource_type": "Subscriptions"
  }
  ```

* #### customer\_payment\_methods/revoke: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",
    "token": "0eccccc666aac73efcd31094ddc4ebf0",
    "customer_id": 82850125,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/82850125",
    "instrument_type": "CustomerCreditCard",
    "payment_instrument": {
      "last_digits": "4242",
      "month": 8,
      "year": 2060,
      "name": "Jim Smith",
      "brand": "Visa"
    },
    "resource_type": "Subscriptions"
  }
  ```

* #### customer\_payment\_methods/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",
    "token": "0eccccc666aac73efcd31094ddc4ebf0",
    "customer_id": 82850125,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/82850125",
    "instrument_type": "CustomerCreditCard",
    "payment_instrument": {
      "last_digits": "4242",
      "month": 8,
      "year": 2060,
      "name": "Jim Smith",
      "brand": "Visa"
    },
    "resource_type": "Subscriptions"
  }
  ```

* #### customer.joined\_segment: Sample Payload

  #####

  ```undefined
  {
    "shop_id": "gid://shopify/Shop/1",
    "customer_id": "gid://shopify/Customer/2",
    "segment_id": "gid://shopify/Segment/3"
  }
  ```

* #### customer.left\_segment: Sample Payload

  #####

  ```undefined
  {
    "shop_id": "gid://shopify/Shop/1",
    "customer_id": "gid://shopify/Customer/2",
    "segment_id": "gid://shopify/Segment/3"
  }
  ```

* #### customer.tags\_added: Sample Payload

  #####

  ```undefined
  {
    "customerId": "gid://shopify/Customer/1",
    "tags": [
      "tag1",
      "tag2"
    ],
    "occurredAt": "2005-05-05T05:00:00.000Z"
  }
  ```

* #### customer.tags\_removed: Sample Payload

  #####

  ```undefined
  {
    "customerId": "gid://shopify/Customer/1",
    "tags": [
      "tag1",
      "tag2"
    ],
    "occurredAt": "2005-05-05T05:00:00.000Z"
  }
  ```

* #### customers\_email\_marketing\_consent/update: Sample Payload

  #####

  ```undefined
  {
    "customer_id": 706405506930370084,
    "email_address": "bob@biller.com",
    "email_marketing_consent": {
      "state": "not_subscribed",
      "opt_in_level": null,
      "consent_updated_at": null
    }
  }
  ```

* #### customers\_marketing\_consent/update: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "phone": null,
    "sms_marketing_consent": {
      "state": null,
      "opt_in_level": null,
      "consent_updated_at": null,
      "consent_collected_from": "other"
    }
  }
  ```

* #### customers\_whats\_app\_marketing\_consent/update: Sample Payload

  #####

  ```undefined
  {
    "customer_id": 706405506930370084,
    "phone_number": null,
    "whats_app_marketing_consent": {
      "state": null,
      "opt_in_level": null,
      "updated_at": null,
      "collected_from": "other"
    }
  }
  ```

* #### customers/create: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "first_name": "Bob",
    "last_name": "Biller",
    "state": "disabled",
    "note": "This customer loves ice cream",
    "verified_email": true,
    "multipass_identifier": null,
    "tax_exempt": false,
    "email": "bob@biller.com",
    "phone": null,
    "currency": "USD",
    "addresses": [],
    "tax_exemptions": [],
    "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
    "default_address": {
      "id": 12321,
      "customer_id": 706405506930370084,
      "first_name": "Bob",
      "last_name": "Biller",
      "company": null,
      "address1": "151 O'Connor Street",
      "address2": null,
      "city": "Ottawa",
      "province": "ON",
      "country": "CA",
      "zip": "K2P 2L8",
      "phone": "555-555-5555",
      "name": "Bob Biller",
      "province_code": "ON",
      "country_code": "CA",
      "country_name": "CA",
      "default": true
    }
  }
  ```

* #### customers/data\_request: Sample Payload

  #####

  ```undefined
  {
    "shop_id": 954889,
    "shop_domain": "{shop}.myshopify.com",
    "customer": {
      "id": 191167,
      "email": "john@example.com",
      "phone": "555-625-1199"
    },
    "orders_requested": [
      299938,
      280263,
      220458
    ],
    "data_request": {
      "id": 9999
    }
  }
  ```

* #### customers/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "tax_exemptions": [],
    "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084"
  }
  ```

* #### customers/disable: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "first_name": "Bob",
    "last_name": "Biller",
    "state": "disabled",
    "note": "This customer loves ice cream",
    "verified_email": true,
    "multipass_identifier": null,
    "tax_exempt": false,
    "email": "bob@biller.com",
    "phone": null,
    "currency": "USD",
    "addresses": [],
    "tax_exemptions": [],
    "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
    "default_address": {
      "id": 12321,
      "customer_id": 706405506930370084,
      "first_name": "Bob",
      "last_name": "Biller",
      "company": null,
      "address1": "151 O'Connor Street",
      "address2": null,
      "city": "Ottawa",
      "province": "ON",
      "country": "CA",
      "zip": "K2P 2L8",
      "phone": "555-555-5555",
      "name": "Bob Biller",
      "province_code": "ON",
      "country_code": "CA",
      "country_name": "CA",
      "default": true
    }
  }
  ```

* #### customers/enable: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "first_name": "Bob",
    "last_name": "Biller",
    "state": "disabled",
    "note": "This customer loves ice cream",
    "verified_email": true,
    "multipass_identifier": null,
    "tax_exempt": false,
    "email": "bob@biller.com",
    "phone": null,
    "currency": "USD",
    "addresses": [],
    "tax_exemptions": [],
    "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
    "default_address": {
      "id": 12321,
      "customer_id": 706405506930370084,
      "first_name": "Bob",
      "last_name": "Biller",
      "company": null,
      "address1": "151 O'Connor Street",
      "address2": null,
      "city": "Ottawa",
      "province": "ON",
      "country": "CA",
      "zip": "K2P 2L8",
      "phone": "555-555-5555",
      "name": "Bob Biller",
      "province_code": "ON",
      "country_code": "CA",
      "country_name": "CA",
      "default": true
    }
  }
  ```

* #### customers/merge: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_customer_kept_id": "gid://shopify/Customer/1",
    "admin_graphql_api_customer_deleted_id": "gid://shopify/Customer/2",
    "admin_graphql_api_job_id": null,
    "status": "failed",
    "errors": [
      {
        "customer_ids": [
          1
        ],
        "field": "merge_in_progress",
        "message": "John Doe is currently being merged."
      }
    ]
  }
  ```

* #### customers/purchasing\_summary: Sample Payload

  #####

  ```undefined
  {
    "customerId": "gid://shopify/Customer/1",
    "numberOfOrders": 1,
    "amountSpent": {
      "amount": "100.00",
      "currencyCode": "USD"
    },
    "lastOrderId": "gid://shopify/Order/1",
    "occurredAt": "2005-05-05T05:00:00.000Z"
  }
  ```

* #### customers/redact: Sample Payload

  #####

  ```undefined
  {
    "shop_id": 954889,
    "shop_domain": "{shop}.myshopify.com",
    "customer": {
      "id": 191167,
      "email": "john@example.com",
      "phone": "555-625-1199"
    },
    "orders_to_redact": [
      299938,
      280263,
      220458
    ]
  }
  ```

* #### customers/update: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "first_name": "Bob",
    "last_name": "Biller",
    "state": "disabled",
    "note": "This customer loves ice cream",
    "verified_email": true,
    "multipass_identifier": null,
    "tax_exempt": false,
    "email": "bob@biller.com",
    "phone": null,
    "currency": "USD",
    "addresses": [],
    "tax_exemptions": [],
    "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
    "default_address": {
      "id": 12321,
      "customer_id": 706405506930370084,
      "first_name": "Bob",
      "last_name": "Biller",
      "company": null,
      "address1": "151 O'Connor Street",
      "address2": null,
      "city": "Ottawa",
      "province": "ON",
      "country": "CA",
      "zip": "K2P 2L8",
      "phone": "555-555-5555",
      "name": "Bob Biller",
      "province_code": "ON",
      "country_code": "CA",
      "country_name": "CA",
      "default": true
    }
  }
  ```

* #### delivery\_promise\_settings/update: Sample Payload

  #####

  ```undefined
  {
    "shop_id": "gid://shopify/Shop/548380009",
    "processing_time": "P2D",
    "delivery_dates_enabled": true
  }
  ```

* #### discounts/create: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/DiscountAutomaticNode/1",
    "title": "Automatic free shipping",
    "status": "ACTIVE",
    "created_at": "2016-08-29T13:00:00-04:00",
    "updated_at": "2016-08-29T13:00:00-04:00"
  }
  ```

* #### discounts/delete: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/DiscountAutomaticNode/1",
    "deleted_at": "2018-08-29T13:00:00-04:00"
  }
  ```

* #### discounts/redeemcode\_added: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/DiscountCodeNode/1",
    "redeem_code": {
      "id": "gid://shopify/DiscountRedeemCode/1",
      "code": "code1"
    },
    "updated_at": "2018-08-29T17:00:00.000Z"
  }
  ```

* #### discounts/redeemcode\_removed: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/DiscountCodeNode/1",
    "redeem_code": {
      "id": "gid://shopify/DiscountRedeemCode/1",
      "code": "code1"
    },
    "updated_at": "2018-08-29T17:00:00.000Z"
  }
  ```

* #### discounts/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/DiscountAutomaticNode/1",
    "title": "Automatic free shipping updated",
    "status": "ACTIVE",
    "created_at": "2016-08-29T13:00:00-04:00",
    "updated_at": "2016-08-29T13:00:00-04:00"
  }
  ```

* #### disputes/create: Sample Payload

  #####

  ```undefined
  {
    "id": 285332461850802063,
    "order_id": 820982911946154508,
    "type": "chargeback",
    "amount": "11.50",
    "currency": "CAD",
    "reason": "fraudulent",
    "network_reason_code": "4837",
    "status": "under_review",
    "evidence_due_by": "2021-12-30T19:00:00-05:00",
    "evidence_sent_on": null,
    "finalized_on": null,
    "initiated_at": "2021-12-31T19:00:00-05:00"
  }
  ```

* #### disputes/update: Sample Payload

  #####

  ```undefined
  {
    "id": 285332461850802063,
    "order_id": 820982911946154508,
    "type": "chargeback",
    "amount": "11.50",
    "currency": "CAD",
    "reason": "fraudulent",
    "network_reason_code": "4837",
    "status": "under_review",
    "evidence_due_by": "2021-12-30T19:00:00-05:00",
    "evidence_sent_on": null,
    "finalized_on": null,
    "initiated_at": "2021-12-31T19:00:00-05:00"
  }
  ```

* #### domains/create: Sample Payload

  #####

  ```undefined
  {
    "id": 690933842,
    "host": "jsmith.myshopify.com",
    "ssl_enabled": true,
    "localization": {
      "country": null,
      "default_locale": "en",
      "alternate_locales": []
    }
  }
  ```

* #### domains/destroy: Sample Payload

  #####

  ```undefined
  {
    "id": 690933842,
    "host": "jsmith.myshopify.com",
    "ssl_enabled": true,
    "localization": {
      "country": null,
      "default_locale": "en",
      "alternate_locales": []
    }
  }
  ```

* #### domains/update: Sample Payload

  #####

  ```undefined
  {
    "id": 690933842,
    "host": "jsmith.myshopify.com",
    "ssl_enabled": true,
    "localization": {
      "country": null,
      "default_locale": "en",
      "alternate_locales": []
    }
  }
  ```

* #### draft\_orders/create: Sample Payload

  #####

  ```undefined
  {
    "id": 890612572568261625,
    "note": null,
    "email": "jon@doe.ca",
    "taxes_included": false,
    "currency": "USD",
    "invoice_sent_at": null,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "tax_exempt": false,
    "completed_at": null,
    "name": "#D133",
    "allow_discount_codes_in_checkout?": false,
    "b2b?": false,
    "status": "open",
    "line_items": [
      {
        "id": 4572525,
        "variant_id": 49148385,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Red",
        "sku": "IPOD2008RED",
        "vendor": "Apple",
        "quantity": 8,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Red",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/4572525"
      },
      {
        "id": 986245,
        "variant_id": 457924702,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Black",
        "sku": "IPOD2008BLACK",
        "vendor": "Apple",
        "quantity": 8,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Black",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/986245"
      },
      {
        "id": 4874623,
        "variant_id": 808950810,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Pink",
        "sku": "IPOD2008PINK",
        "vendor": "Apple",
        "quantity": 2,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Pink",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/4874623"
      }
    ],
    "api_client_id": null,
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40150",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "billing_address": {
      "first_name": "Bob",
      "address1": "123 Billing Street",
      "phone": "555-555-BILL",
      "city": "Billtown",
      "zip": "K2P0B0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Biller",
      "address2": null,
      "company": "My Company",
      "latitude": null,
      "longitude": null,
      "name": "Bob Biller",
      "country_code": "US",
      "province_code": "KY"
    },
    "invoice_url": "https://jsmith.myshopify.com/548380009/invoices/abcd1234abcd1234abcd1234abcd1234",
    "created_on_api_version_handle": null,
    "applied_discount": {
      "description": "ABC 123",
      "value": "2.0",
      "title": "ABC 123",
      "amount": "8.00",
      "value_type": "percentage"
    },
    "order_id": null,
    "shipping_line": {
      "custom": true,
      "handle": null,
      "title": "ABC 123",
      "price": "3.00"
    },
    "tax_lines": [
      {
        "rate": 0.03144408811829065,
        "title": "State tax",
        "price": "3.00"
      },
      {
        "rate": 0.03144408811829065,
        "title": "State tax",
        "price": "3.00"
      },
      {
        "rate": 0.03144408811829065,
        "title": "State tax",
        "price": "4.00"
      }
    ],
    "tags": "",
    "note_attributes": [],
    "total_price": "436.00",
    "subtotal_price": "497.00",
    "total_tax": "469.00",
    "payment_terms": {
      "id": 706405506930370084,
      "payment_terms_name": "Net 7",
      "payment_terms_type": "net",
      "due_in_days": 7,
      "created_at": "2021-01-01T00:00:00-05:00",
      "updated_at": "2021-01-01T00:00:01-05:00",
      "payment_schedules": [
        {
          "id": 606405506930370084,
          "created_at": "2021-01-01T00:00:00-05:00",
          "updated_at": "2021-01-01T00:00:01-05:00",
          "payment_terms_id": 706405506930370084,
          "reference_id": 890612572568261625,
          "reference_type": "DraftOrder",
          "issued_at": "2021-01-01T00:00:00-05:00",
          "due_at": "2021-01-02T00:00:00-05:00",
          "completed_at": "2021-01-02T00:00:00-05:00",
          "amount": "436.00",
          "currency": "USD",
          "total_price": "436.00",
          "total_price_currency": "USD",
          "balance_due": "436.00",
          "balance_due_currency": "USD",
          "total_balance": "436.00",
          "total_balance_currency": "USD",
          "outstanding_balance": "436.00",
          "outstanding_balance_currency": "USD"
        }
      ],
      "can_pay_early": true
    },
    "admin_graphql_api_id": "gid://shopify/DraftOrder/890612572568261625",
    "customer": {
      "id": 706405506930370084,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@doe.ca",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
      "default_address": {
        "id": null,
        "customer_id": 706405506930370084,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    }
  }
  ```

* #### draft\_orders/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 890612572568261625
  }
  ```

* #### draft\_orders/update: Sample Payload

  #####

  ```undefined
  {
    "id": 890612572568261625,
    "note": null,
    "email": "jon@doe.ca",
    "taxes_included": false,
    "currency": "USD",
    "invoice_sent_at": null,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "tax_exempt": false,
    "completed_at": null,
    "name": "#D142",
    "allow_discount_codes_in_checkout?": false,
    "b2b?": false,
    "status": "open",
    "line_items": [
      {
        "id": 4478735,
        "variant_id": 49148385,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Red",
        "sku": "IPOD2008RED",
        "vendor": "Apple",
        "quantity": 4,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Red",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/4478735"
      },
      {
        "id": 1181754,
        "variant_id": 457924702,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Black",
        "sku": "IPOD2008BLACK",
        "vendor": "Apple",
        "quantity": 2,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Black",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/1181754"
      },
      {
        "id": 4904786,
        "variant_id": 808950810,
        "product_id": 632910392,
        "title": "IPod Nano - 8GB",
        "variant_title": "Pink",
        "sku": "IPOD2008PINK",
        "vendor": "Apple",
        "quantity": 10,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "fulfillment_service": "manual",
        "grams": 567,
        "tax_lines": [],
        "applied_discount": null,
        "name": "IPod Nano - 8GB - Pink",
        "properties": [],
        "custom": false,
        "price": "199.00",
        "admin_graphql_api_id": "gid://shopify/DraftOrderLineItem/4904786"
      }
    ],
    "api_client_id": null,
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40150",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "billing_address": {
      "first_name": "Bob",
      "address1": "123 Billing Street",
      "phone": "555-555-BILL",
      "city": "Billtown",
      "zip": "K2P0B0",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Biller",
      "address2": null,
      "company": "My Company",
      "latitude": null,
      "longitude": null,
      "name": "Bob Biller",
      "country_code": "US",
      "province_code": "KY"
    },
    "invoice_url": "https://jsmith.myshopify.com/548380009/invoices/abcd1234abcd1234abcd1234abcd1234",
    "created_on_api_version_handle": null,
    "applied_discount": {
      "description": "ABC 123",
      "value": "8.0",
      "title": "ABC 123",
      "amount": "7.00",
      "value_type": "percentage"
    },
    "order_id": null,
    "shipping_line": {
      "custom": true,
      "handle": null,
      "title": "ABC 123",
      "price": "4.00"
    },
    "tax_lines": [
      {
        "rate": 0.03411142681997328,
        "title": "State tax",
        "price": "1.00"
      },
      {
        "rate": 0.03411142681997328,
        "title": "State tax",
        "price": "5.00"
      },
      {
        "rate": 0.03411142681997328,
        "title": "State tax",
        "price": "4.00"
      }
    ],
    "tags": "",
    "note_attributes": [],
    "total_price": "483.00",
    "subtotal_price": "416.00",
    "total_tax": "404.00",
    "payment_terms": {
      "id": 706405506930370084,
      "payment_terms_name": "Net 7",
      "payment_terms_type": "net",
      "due_in_days": 7,
      "created_at": "2021-01-01T00:00:00-05:00",
      "updated_at": "2021-01-01T00:00:01-05:00",
      "payment_schedules": [
        {
          "id": 606405506930370084,
          "created_at": "2021-01-01T00:00:00-05:00",
          "updated_at": "2021-01-01T00:00:01-05:00",
          "payment_terms_id": 706405506930370084,
          "reference_id": 890612572568261625,
          "reference_type": "DraftOrder",
          "issued_at": "2021-01-01T00:00:00-05:00",
          "due_at": "2021-01-02T00:00:00-05:00",
          "completed_at": "2021-01-02T00:00:00-05:00",
          "amount": "483.00",
          "currency": "USD",
          "total_price": "483.00",
          "total_price_currency": "USD",
          "balance_due": "483.00",
          "balance_due_currency": "USD",
          "total_balance": "483.00",
          "total_balance_currency": "USD",
          "outstanding_balance": "483.00",
          "outstanding_balance_currency": "USD"
        }
      ],
      "can_pay_early": true
    },
    "admin_graphql_api_id": "gid://shopify/DraftOrder/890612572568261625",
    "customer": {
      "id": 706405506930370084,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@doe.ca",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084",
      "default_address": {
        "id": null,
        "customer_id": 706405506930370084,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    }
  }
  ```

* #### fulfillment\_events/create: Sample Payload

  #####

  ```undefined
  {
    "id": 1234567,
    "fulfillment_id": 123456,
    "status": "in_transit",
    "message": "Item is now in transit",
    "happened_at": "2021-12-31T19:00:00-05:00",
    "city": null,
    "province": null,
    "country": "CA",
    "zip": null,
    "address1": null,
    "latitude": null,
    "longitude": null,
    "shop_id": 548380009,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "estimated_delivery_at": null,
    "order_id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/FulfillmentEvent/1234567"
  }
  ```

* #### fulfillment\_events/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 1234567,
    "fulfillment_id": 123456,
    "status": "in_transit",
    "message": "Item is now in transit",
    "happened_at": "2021-12-31T19:00:00-05:00",
    "city": null,
    "province": null,
    "country": "CA",
    "zip": null,
    "address1": null,
    "latitude": null,
    "longitude": null,
    "shop_id": 548380009,
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "estimated_delivery_at": null,
    "order_id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/FulfillmentEvent/1234567"
  }
  ```

* #### fulfillment\_holds/added: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1"
    },
    "fulfillment_hold": {
      "id": "gid://shopify/FulfillmentHold/1",
      "reason": "other",
      "reason_notes": "Waiting for some more details from the customer before this can be fulfilled.",
      "held_by_requesting_app": false,
      "handle": "test_handle",
      "held_by_app": {
        "id": "gid://shopify/App/12345"
      }
    }
  }
  ```

* #### fulfillment\_holds/released: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1"
    },
    "fulfillment_hold": {
      "id": "gid://shopify/FulfillmentHold/1",
      "reason": "other",
      "reason_notes": "Waiting for some more details from the customer before this can be fulfilled.",
      "held_by_requesting_app": false,
      "handle": "fulfillment_hold_1",
      "held_by_app": {
        "id": "gid://shopify/App/12345"
      }
    }
  }
  ```

* #### fulfillment\_orders/cancellation\_request\_accepted: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "closed"
    },
    "message": "Order has not been shipped yet."
  }
  ```

* #### fulfillment\_orders/cancellation\_request\_rejected: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "in_progress",
      "request_status": "cancellation_rejected"
    },
    "message": "Order has already been shipped."
  }
  ```

* #### fulfillment\_orders/cancellation\_request\_submitted: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "in_progress",
      "request_status": "cancellation_request"
    },
    "fulfillment_order_merchant_request": {
      "id": "gid://shopify/FulfillmentOrderMerchantRequest/1",
      "message": "Customer cancelled their order"
    }
  }
  ```

* #### fulfillment\_orders/cancelled: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "cancelled"
    },
    "replacement_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/2",
      "status": "open"
    }
  }
  ```

* #### fulfillment\_orders/fulfillment\_request\_accepted: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "in_progress",
      "request_status": "accepted"
    },
    "message": "We will ship the item tomorrow."
  }
  ```

* #### fulfillment\_orders/fulfillment\_request\_rejected: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open",
      "request_status": "rejected"
    },
    "message": "Can't fulfill due to no inventory on product."
  }
  ```

* #### fulfillment\_orders/fulfillment\_request\_submitted: Sample Payload

  #####

  ```undefined
  {
    "original_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open",
      "request_status": "unsubmitted"
    },
    "submitted_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open",
      "request_status": "unsubmitted"
    },
    "fulfillment_order_merchant_request": {
      "id": "gid://shopify/FulfillmentOrderMerchantRequest/1",
      "message": "Fragile"
    }
  }
  ```

* #### fulfillment\_orders/fulfillment\_service\_failed\_to\_complete: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "closed"
    },
    "message": "We broke the last item."
  }
  ```

* #### fulfillment\_orders/hold\_released: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open"
    }
  }
  ```

* #### fulfillment\_orders/line\_items\_prepared\_for\_local\_delivery: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open",
      "preparable": true,
      "delivery_method": {
        "method_type": "local"
      }
    }
  }
  ```

* #### fulfillment\_orders/line\_items\_prepared\_for\_pickup: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open",
      "preparable": true,
      "delivery_method": {
        "method_type": "pickup"
      }
    }
  }
  ```

* #### fulfillment\_orders/manually\_reported\_progress\_stopped: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open"
    },
    "progress_stopped_by_app": {
      "id": "gid://shopify/App/12345"
    },
    "progress_stopped_by_user": {
      "id": "gid://shopify/StaffMember/12345"
    }
  }
  ```

* #### fulfillment\_orders/merged: Sample Payload

  #####

  ```undefined
  {
    "merge_intents": [
      {
        "fulfillment_order_id": 1,
        "fulfillment_order_line_items": [
          {
            "id": 1,
            "quantity": 1
          }
        ]
      },
      {
        "fulfillment_order_id": 2,
        "fulfillment_order_line_items": [
          {
            "id": 2,
            "quantity": 1
          }
        ]
      }
    ],
    "fulfillment_order_merges": {
      "fulfillment_order": {
        "id": "gid://shopify/FulfillmentOrder/1",
        "status": "open"
      }
    }
  }
  ```

* #### fulfillment\_orders/moved: Sample Payload

  #####

  ```undefined
  {
    "original_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "closed",
      "assigned_location_id": "gid://shopify/Location/0"
    },
    "moved_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/2",
      "status": "open",
      "assigned_location_id": "gid://shopify/Location/1"
    },
    "destination_location_id": "gid://shopify/Location/1",
    "fulfillment_order_line_items_requested": [
      {
        "id": "gid://shopify/FulfillmentOrderLineItem/1",
        "quantity": 1
      }
    ],
    "source_location": {
      "id": "gid://shopify/Location/0"
    }
  }
  ```

* #### fulfillment\_orders/order\_routing\_complete: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open"
    }
  }
  ```

* #### fulfillment\_orders/placed\_on\_hold: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "on_hold",
      "fulfillment_holds": [
        {
          "id": "gid://shopify/FulfillmentHold/1",
          "reason": "other",
          "reason_notes": "example",
          "held_by_requesting_app": false,
          "handle": "example-hold-1",
          "held_by_app": {
            "id": "gid://shopify/App/12345"
          }
        },
        {
          "id": "gid://shopify/FulfillmentHold/2",
          "reason": "inventory_out_of_stock",
          "reason_notes": "Stacked hold",
          "held_by_requesting_app": false,
          "handle": "example-hold-2",
          "held_by_app": {
            "id": "gid://shopify/App/12345"
          }
        }
      ]
    },
    "remaining_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/2",
      "status": "open"
    },
    "held_fulfillment_order_line_items": [
      {
        "id": "gid://shopify/FulfillmentOrderLineItem/3",
        "quantity": 4
      }
    ],
    "created_fulfillment_hold": {
      "id": "gid://shopify/FulfillmentHold/1",
      "reason": "other",
      "reason_notes": "example",
      "held_by_requesting_app": false,
      "handle": "example-hold-1",
      "held_by_app": {
        "id": "gid://shopify/App/12345"
      }
    }
  }
  ```

* #### fulfillment\_orders/progress\_reported: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "in_progress"
    },
    "progress_report": {
      "reason_notes": "Items are being prepared for shipment",
      "progress_reported_by_app": {
        "id": "gid://shopify/App/12345"
      },
      "progress_reported_by_user": {
        "id": "gid://shopify/StaffMember/12345"
      }
    },
    "initial_status": "open"
  }
  ```

* #### fulfillment\_orders/rescheduled: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "scheduled",
      "fulfill_at": "2021-12-31T19:00:00-05:00"
    }
  }
  ```

* #### fulfillment\_orders/scheduled\_fulfillment\_order\_ready: Sample Payload

  #####

  ```undefined
  {
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open"
    }
  }
  ```

* #### fulfillment\_orders/split: Sample Payload

  #####

  ```undefined
  {
    "split_line_items": [
      {
        "id": "gid://shopify/FulfillmentOrderLineItem/1",
        "quantity": 1
      }
    ],
    "fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/1",
      "status": "open"
    },
    "remaining_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/2",
      "status": "open"
    },
    "replacement_fulfillment_order": {
      "id": "gid://shopify/FulfillmentOrder/3",
      "status": "open"
    }
  }
  ```

* #### fulfillments/create: Sample Payload

  #####

  ```undefined
  {
    "id": 123456,
    "order_id": 820982911946154508,
    "status": "pending",
    "created_at": "2021-12-31T19:00:00-05:00",
    "service": null,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "tracking_company": "UPS",
    "shipment_status": null,
    "location_id": null,
    "origin_address": null,
    "email": "jon@example.com",
    "destination": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "line_items": [
      {
        "id": 487817672276298554,
        "variant_id": null,
        "title": "Aviator sunglasses",
        "quantity": 1,
        "sku": "SKU2006-001",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Aviator sunglasses",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 100,
        "price": "89.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "tax_lines": []
      },
      {
        "id": 789012345678901234,
        "variant_id": null,
        "title": "Lens Protection Plan (2 Year)",
        "quantity": 1,
        "sku": "LENS-PROTECT-2YR",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": null,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Lens Protection Plan (2 Year)",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": false,
        "fulfillable_quantity": 1,
        "grams": 0,
        "price": "19.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "tax_lines": []
      },
      {
        "id": 890123456789012345,
        "variant_id": null,
        "title": "Premium Leather Case",
        "quantity": 1,
        "sku": "CASE-LEATHER-PREM",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": null,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Premium Leather Case",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": false,
        "fulfillable_quantity": 1,
        "grams": 0,
        "price": "24.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "tax_lines": []
      },
      {
        "id": 976318377106520349,
        "variant_id": null,
        "title": "Mid-century lounger",
        "quantity": 1,
        "sku": "SKU2006-020",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Mid-century lounger",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 1000,
        "price": "159.99",
        "total_discount": "5.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "5.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "5.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [
          {
            "amount": "5.00",
            "discount_application_index": 0,
            "amount_set": {
              "shop_money": {
                "amount": "5.00",
                "currency_code": "USD"
              },
              "presentment_money": {
                "amount": "5.00",
                "currency_code": "USD"
              }
            }
          },
          {
            "amount": "5.00",
            "discount_application_index": 2,
            "amount_set": {
              "shop_money": {
                "amount": "5.00",
                "currency_code": "USD"
              },
              "presentment_money": {
                "amount": "5.00",
                "currency_code": "USD"
              }
            }
          }
        ],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "tax_lines": []
      },
      {
        "id": 315789986012684393,
        "variant_id": null,
        "title": "Coffee table",
        "quantity": 1,
        "sku": "SKU2006-035",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Coffee table",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 500,
        "price": "119.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "tax_lines": []
      }
    ],
    "tracking_number": "1z827wk74630",
    "tracking_numbers": [
      "1z827wk74630"
    ],
    "tracking_url": "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1z827wk74630",
    "tracking_urls": [
      "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1z827wk74630"
    ],
    "receipt": {},
    "name": "#9999.1",
    "admin_graphql_api_id": "gid://shopify/Fulfillment/123456"
  }
  ```

* #### fulfillments/update: Sample Payload

  #####

  ```undefined
  {
    "id": 123456,
    "order_id": 820982911946154508,
    "status": "pending",
    "created_at": "2021-12-31T19:00:00-05:00",
    "service": null,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "tracking_company": "UPS",
    "shipment_status": null,
    "location_id": null,
    "origin_address": null,
    "email": "jon@example.com",
    "destination": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "line_items": [
      {
        "id": 487817672276298554,
        "variant_id": null,
        "title": "Aviator sunglasses",
        "quantity": 1,
        "sku": "SKU2006-001",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Aviator sunglasses",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 100,
        "price": "89.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "tax_lines": []
      },
      {
        "id": 789012345678901234,
        "variant_id": null,
        "title": "Lens Protection Plan (2 Year)",
        "quantity": 1,
        "sku": "LENS-PROTECT-2YR",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": null,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Lens Protection Plan (2 Year)",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": false,
        "fulfillable_quantity": 1,
        "grams": 0,
        "price": "19.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "tax_lines": []
      },
      {
        "id": 890123456789012345,
        "variant_id": null,
        "title": "Premium Leather Case",
        "quantity": 1,
        "sku": "CASE-LEATHER-PREM",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": null,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Premium Leather Case",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": false,
        "fulfillable_quantity": 1,
        "grams": 0,
        "price": "24.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "tax_lines": []
      },
      {
        "id": 976318377106520349,
        "variant_id": null,
        "title": "Mid-century lounger",
        "quantity": 1,
        "sku": "SKU2006-020",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Mid-century lounger",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 1000,
        "price": "159.99",
        "total_discount": "5.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "5.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "5.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [
          {
            "amount": "5.00",
            "discount_application_index": 0,
            "amount_set": {
              "shop_money": {
                "amount": "5.00",
                "currency_code": "USD"
              },
              "presentment_money": {
                "amount": "5.00",
                "currency_code": "USD"
              }
            }
          },
          {
            "amount": "5.00",
            "discount_application_index": 2,
            "amount_set": {
              "shop_money": {
                "amount": "5.00",
                "currency_code": "USD"
              },
              "presentment_money": {
                "amount": "5.00",
                "currency_code": "USD"
              }
            }
          }
        ],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "tax_lines": []
      },
      {
        "id": 315789986012684393,
        "variant_id": null,
        "title": "Coffee table",
        "quantity": 1,
        "sku": "SKU2006-035",
        "variant_title": null,
        "vendor": null,
        "fulfillment_service": "manual",
        "product_id": 788032119674292922,
        "requires_shipping": true,
        "taxable": true,
        "gift_card": false,
        "name": "Coffee table",
        "variant_inventory_management": null,
        "properties": [],
        "product_exists": true,
        "fulfillable_quantity": 1,
        "grams": 500,
        "price": "119.99",
        "total_discount": "0.00",
        "fulfillment_status": null,
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "tax_lines": []
      }
    ],
    "tracking_number": "1z827wk74630",
    "tracking_numbers": [
      "1z827wk74630"
    ],
    "tracking_url": "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1z827wk74630",
    "tracking_urls": [
      "https://www.ups.com/WebTracking?loc=en_US&requester=ST&trackNums=1z827wk74630"
    ],
    "receipt": {},
    "name": "#9999.1",
    "admin_graphql_api_id": "gid://shopify/Fulfillment/123456"
  }
  ```

* #### inventory\_items/create: Sample Payload

  #####

  ```undefined
  {
    "id": 271878346596884015,
    "sku": "example-sku",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "requires_shipping": true,
    "cost": null,
    "country_code_of_origin": null,
    "province_code_of_origin": null,
    "harmonized_system_code": null,
    "tracked": true,
    "country_harmonized_system_codes": [],
    "weight_value": 0.0,
    "weight_unit": "lb",
    "admin_graphql_api_id": "gid://shopify/InventoryItem/271878346596884015"
  }
  ```

* #### inventory\_items/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 271878346596884015,
    "country_code_of_origin": null,
    "province_code_of_origin": null,
    "harmonized_system_code": null,
    "country_harmonized_system_codes": [],
    "admin_graphql_api_id": "gid://shopify/InventoryItem/271878346596884015"
  }
  ```

* #### inventory\_items/update: Sample Payload

  #####

  ```undefined
  {
    "id": 271878346596884015,
    "sku": "example-sku",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "requires_shipping": true,
    "cost": null,
    "country_code_of_origin": null,
    "province_code_of_origin": null,
    "harmonized_system_code": null,
    "tracked": true,
    "country_harmonized_system_codes": [],
    "weight_value": 0.0,
    "weight_unit": "lb",
    "admin_graphql_api_id": "gid://shopify/InventoryItem/271878346596884015"
  }
  ```

* #### inventory\_levels/connect: Sample Payload

  #####

  ```undefined
  {
    "inventory_item_id": 271878346596884015,
    "location_id": 24826418,
    "available": 10,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/InventoryLevel/24826418?inventory_item_id=271878346596884015"
  }
  ```

* #### inventory\_levels/disconnect: Sample Payload

  #####

  ```undefined
  {
    "inventory_item_id": 271878346596884015,
    "location_id": 24826418
  }
  ```

* #### inventory\_levels/update: Sample Payload

  #####

  ```undefined
  {
    "inventory_item_id": 271878346596884015,
    "location_id": 24826418,
    "available": 10,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "admin_graphql_api_id": "gid://shopify/InventoryLevel/24826418?inventory_item_id=271878346596884015"
  }
  ```

* #### inventory\_shipments/add\_items: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "items_added": [
      {
        "id": "gid://shopify/InventoryShipmentLineItem/82243",
        "quantity": 10
      },
      {
        "id": "gid://shopify/InventoryShipmentLineItem/57116",
        "quantity": 7
      }
    ],
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/create: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "status": "DRAFT",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "tracking": {
      "arrives_at": "2023-10-02T03:24:44-04:00",
      "tracking_number": "8375692728",
      "tracking_url": "https://exampletracking.shopify.com/track/8375692728",
      "company": "Purolator"
    },
    "line_items": [
      {
        "id": "gid://shopify/InventoryShipmentLineItem/82243",
        "quantity": 10
      },
      {
        "id": "gid://shopify/InventoryShipmentLineItem/57116",
        "quantity": 7
      }
    ]
  }
  ```

* #### inventory\_shipments/delete: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/mark\_in\_transit: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "status": "IN_TRANSIT",
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/receive\_items: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "status": "PARTIALLY_RECEIVED",
    "items_received": [
      {
        "id": "gid://shopify/InventoryShipmentLineItem/82243",
        "old_accepted_quantity": 5,
        "old_rejected_quantity": 2,
        "new_accepted_quantity": 11,
        "new_rejected_quantity": 3,
        "remaining_quantity_to_receive": 6
      },
      {
        "id": "gid://shopify/InventoryShipmentLineItem/57116",
        "old_accepted_quantity": 21,
        "old_rejected_quantity": 9,
        "new_accepted_quantity": 37,
        "new_rejected_quantity": 14,
        "remaining_quantity_to_receive": 16
      }
    ],
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/remove\_items: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "items_removed": [
      {
        "id": "gid://shopify/InventoryShipmentLineItem/82243"
      },
      {
        "id": "gid://shopify/InventoryShipmentLineItem/57116"
      }
    ],
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/update\_item\_quantities: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryShipment/3921201",
    "items_updated": [
      {
        "id": "gid://shopify/InventoryShipmentLineItem/82243",
        "old_quantity": 10,
        "new_quantity": 23
      },
      {
        "id": "gid://shopify/InventoryShipmentLineItem/57116",
        "old_quantity": 7,
        "new_quantity": 42
      }
    ],
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_shipments/update\_tracking: Sample Payload

  #####

  ```undefined
  {
    "shipment_id": "gid://shopify/InventoryShipment/3921201",
    "updated_tracking": {
      "tracking_number": "8375692728",
      "tracking_url": "https://exampletracking.shopify.com/track/8375692728",
      "company": "Purolator",
      "arrives_at": "2023-10-02T03:24:44-04:00"
    },
    "happened_at": "2023-09-01T08:19:56-04:00"
  }
  ```

* #### inventory\_transfers/add\_items: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "items_added": [
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/72243",
        "quantity": 14
      },
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/81958",
        "quantity": 22
      }
    ]
  }
  ```

* #### inventory\_transfers/cancel: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "status": "CANCELED"
  }
  ```

* #### inventory\_transfers/complete: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "status": "TRANSFERRED"
  }
  ```

* #### inventory\_transfers/ready\_to\_ship: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "status": "READY_TO_SHIP",
    "line_items": [
      {
        "id": "gid://shopify/InventoryTransferLineItem/72243",
        "quantity": 10
      },
      {
        "id": "gid://shopify/InventoryTransferLineItem/81958",
        "quantity": 8
      }
    ]
  }
  ```

* #### inventory\_transfers/remove\_items: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "items_removed": [
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/72243"
      },
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/81958"
      }
    ]
  }
  ```

* #### inventory\_transfers/update\_item\_quantities: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    },
    "status": "IN_PROGRESS",
    "items_updated": [
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/72243",
        "old_quantity": 10,
        "new_quantity": 23
      },
      {
        "line_item_id": "gid://shopify/InventoryTransferLineItem/81958",
        "old_quantity": 8,
        "new_quantity": 15
      }
    ]
  }
  ```

* #### inventory\_transfers/updated: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/InventoryTransfer/2921201",
    "happened_at": "2023-09-01T08:19:56-04:00",
    "origin": {
      "id": "gid://shopify/Location/346779"
    },
    "destination": {
      "id": "gid://shopify/Location/482156"
    }
  }
  ```

* #### locales/create: Sample Payload

  #####

  ```undefined
  {
    "locale": "fr-CA",
    "published": true
  }
  ```

* #### locales/destroy: Sample Payload

  #####

  ```undefined
  {
    "locale": "fr-CA",
    "published": true
  }
  ```

* #### locales/update: Sample Payload

  #####

  ```undefined
  {
    "locale": "fr-CA",
    "published": true
  }
  ```

* #### locations/activate: Sample Payload

  #####

  ```undefined
  {
    "id": 866550311766439020,
    "name": "Example Shop",
    "address1": "34 Example Street",
    "address2": "Next to example",
    "city": "ottawa",
    "zip": "k1n5t5",
    "province": "ontario",
    "country": "CA",
    "phone": "555-555-5555",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "country_code": "CA",
    "country_name": "Canada",
    "province_code": "ON",
    "legacy": false,
    "active": true,
    "admin_graphql_api_id": "gid://shopify/Location/866550311766439020"
  }
  ```

* #### locations/create: Sample Payload

  #####

  ```undefined
  {
    "id": 866550311766439020,
    "name": "Example Shop",
    "address1": "34 Example Street",
    "address2": "Next to example",
    "city": "ottawa",
    "zip": "k1n5t5",
    "province": "ontario",
    "country": "CA",
    "phone": "555-555-5555",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "country_code": "CA",
    "country_name": "Canada",
    "province_code": "ON",
    "legacy": false,
    "active": true,
    "admin_graphql_api_id": "gid://shopify/Location/866550311766439020"
  }
  ```

* #### locations/deactivate: Sample Payload

  #####

  ```undefined
  {
    "id": 866550311766439020,
    "name": "Example Shop",
    "address1": "34 Example Street",
    "address2": "Next to example",
    "city": "ottawa",
    "zip": "k1n5t5",
    "province": "ontario",
    "country": "CA",
    "phone": "555-555-5555",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "country_code": "CA",
    "country_name": "Canada",
    "province_code": "ON",
    "legacy": false,
    "active": true,
    "admin_graphql_api_id": "gid://shopify/Location/866550311766439020"
  }
  ```

* #### locations/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 866550311766439020
  }
  ```

* #### locations/update: Sample Payload

  #####

  ```undefined
  {
    "id": 866550311766439020,
    "name": "Example Shop",
    "address1": "34 Example Street",
    "address2": "Next to example",
    "city": "ottawa",
    "zip": "k1n5t5",
    "province": "ontario",
    "country": "CA",
    "phone": "555-555-5555",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "country_code": "CA",
    "country_name": "Canada",
    "province_code": "ON",
    "legacy": false,
    "active": true,
    "admin_graphql_api_id": "gid://shopify/Location/866550311766439020"
  }
  ```

* #### markets\_backup\_region/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/MarketRegion/238945671234567891",
    "code": "US"
  }
  ```

* #### markets/create: Sample Payload

  #####

  ```undefined
  {
    "id": 188558248,
    "name": "United States",
    "type": "region",
    "status": "active"
  }
  ```

* #### markets/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 188558248
  }
  ```

* #### markets/update: Sample Payload

  #####

  ```undefined
  {
    "id": 188558248,
    "name": "United States",
    "type": "region",
    "status": "active"
  }
  ```

* #### metafield\_definitions/create: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "shop_id": 548380009,
    "namespace": "example-type",
    "key": "example-key",
    "name": "Example Field",
    "description": null,
    "owner_type": "Customer",
    "deleting": false,
    "type_name": "single_line_text_field",
    "options": [],
    "api_client_id": null,
    "created_at": null,
    "updated_at": null,
    "validation_status": "all_valid",
    "pinned_position": 0,
    "standard_template_id": null,
    "merchant_writeable": null,
    "storefront_readable": null,
    "customer_access": null,
    "namespace_owner_api_client_id": null,
    "unique_values": false,
    "smart_collection_condition": false,
    "option_linkable": false,
    "admin_filterable": false,
    "admin_filterable_status": null,
    "app_config_managed": false,
    "access_only": false,
    "admin_filter_status": "not_filterable",
    "use_as_collection_condition": false
  }
  ```

* #### metafield\_definitions/delete: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/MetafieldDefinition/1",
    "type": "ShopifyMetafields::Types::SingleLineTextFieldType",
    "created_by_app_id": null
  }
  ```

* #### metafield\_definitions/update: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "shop_id": 548380009,
    "namespace": "example-type",
    "key": "example-key",
    "name": "Example Field",
    "description": null,
    "owner_type": "Customer",
    "deleting": false,
    "type_name": "single_line_text_field",
    "options": [],
    "api_client_id": null,
    "created_at": null,
    "updated_at": null,
    "validation_status": "all_valid",
    "pinned_position": 0,
    "standard_template_id": null,
    "merchant_writeable": null,
    "storefront_readable": null,
    "customer_access": null,
    "namespace_owner_api_client_id": null,
    "unique_values": false,
    "smart_collection_condition": false,
    "option_linkable": false,
    "admin_filterable": false,
    "admin_filterable_status": null,
    "app_config_managed": false,
    "access_only": false,
    "admin_filter_status": "not_filterable",
    "use_as_collection_condition": false
  }
  ```

* #### metaobjects/create: Sample Payload

  #####

  ```undefined
  {
    "type": "example-type",
    "handle": "example-metaobject",
    "created_at": "1975-10-31T00:55:12-05:00",
    "updated_at": "1985-07-13T01:55:12-04:00",
    "display_name": "Example Metaobject",
    "id": "gid://shopify/Metaobject/123",
    "definition_id": "gid://shopify/MetaobjectDefinition/222",
    "fields": {
      "example-key": "example-value"
    },
    "created_by_staff_id": "gid://shopify/StaffMember/444",
    "created_by_app_id": "gid://shopify/ApiClient/333",
    "capabilities": {
      "publishable": {
        "status": "draft"
      }
    }
  }
  ```

* #### metaobjects/delete: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/Metaobject/123",
    "type": "example-type",
    "handle": "example-metaobject",
    "created_by_app_id": "gid://shopify/ApiClient/333"
  }
  ```

* #### metaobjects/update: Sample Payload

  #####

  ```undefined
  {
    "type": "example-type",
    "handle": "example-metaobject",
    "created_at": "1975-10-31T00:55:12-05:00",
    "updated_at": "1985-07-13T01:55:12-04:00",
    "display_name": "Example Metaobject",
    "id": "gid://shopify/Metaobject/123",
    "definition_id": "gid://shopify/MetaobjectDefinition/222",
    "fields": {
      "example-key": "example-value"
    },
    "created_by_staff_id": "gid://shopify/StaffMember/444",
    "created_by_app_id": "gid://shopify/ApiClient/333",
    "capabilities": {
      "publishable": {
        "status": "draft"
      }
    }
  }
  ```

* #### order\_transactions/create: Sample Payload

  #####

  ```undefined
  {
    "id": 120560818172775265,
    "order_id": 820982911946154508,
    "kind": "authorization",
    "gateway": "visa",
    "status": "success",
    "message": null,
    "created_at": "2021-12-31T19:00:00-05:00",
    "test": false,
    "authorization": "1001",
    "location_id": null,
    "user_id": null,
    "parent_id": null,
    "processed_at": null,
    "device_id": null,
    "error_code": null,
    "source_name": "web",
    "payment_details": {
      "credit_card_bin": null,
      "avs_result_code": null,
      "cvv_result_code": null,
      "credit_card_number": "•••• •••• •••• 1234",
      "credit_card_company": "Visa",
      "buyer_action_info": null,
      "credit_card_name": null,
      "credit_card_wallet": null,
      "credit_card_expiration_month": null,
      "credit_card_expiration_year": null,
      "payment_method_name": "visa"
    },
    "receipt": {},
    "amount": "419.95",
    "currency": "USD",
    "payment_id": "#9999.1",
    "total_unsettled_set": {
      "presentment_money": {
        "amount": "419.95",
        "currency": "USD"
      },
      "shop_money": {
        "amount": "419.95",
        "currency": "USD"
      }
    },
    "manual_payment_gateway": true,
    "amount_rounding": null,
    "admin_graphql_api_id": "gid://shopify/OrderTransaction/120560818172775265"
  }
  ```

* #### orders/cancelled: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/create: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508
  }
  ```

* #### orders/edited: Sample Payload

  #####

  ```undefined
  {
    "order_edit": {
      "id": 78912328793123782,
      "app_id": null,
      "created_at": "2021-12-31T19:00:00-05:00",
      "committed_at": "2021-12-31T19:00:00-05:00",
      "notify_customer": false,
      "order_id": 820982911946154508,
      "staff_note": "",
      "user_id": null,
      "line_items": {
        "additions": [
          {
            "id": 78643924236718232,
            "delta": 1
          }
        ],
        "removals": [
          {
            "id": 487817672276298554,
            "delta": 1
          }
        ]
      },
      "discounts": {
        "line_item": {
          "additions": [],
          "removals": []
        }
      },
      "shipping_lines": {
        "additions": [],
        "removals": []
      }
    }
  }
  ```

* #### orders/fulfilled: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/link\_requested: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/paid: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/partially\_fulfilled: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### orders/risk\_assessment\_changed: Sample Payload

  #####

  ```undefined
  {
    "provider_id": null,
    "provider_title": null,
    "risk_level": "medium",
    "created_at": null,
    "order_id": null,
    "admin_graphql_api_order_id": null
  }
  ```

* #### orders/shopify\_protect\_eligibility\_changed: Sample Payload

  #####

  ```undefined
  {
    "order_id": 1,
    "status": "active",
    "eligibility": {
      "status": "eligible"
    }
  }
  ```

* #### orders/updated: Sample Payload

  #####

  ```undefined
  {
    "id": 820982911946154508,
    "admin_graphql_api_id": "gid://shopify/Order/820982911946154508",
    "app_id": null,
    "browser_ip": null,
    "buyer_accepts_marketing": true,
    "cancel_reason": "customer",
    "cancelled_at": "2021-12-31T19:00:00-05:00",
    "cart_token": null,
    "checkout_token": null,
    "client_details": null,
    "closed_at": null,
    "confirmation_number": null,
    "confirmed": false,
    "contact_email": "jon@example.com",
    "created_at": "2021-12-31T19:00:00-05:00",
    "currency": "USD",
    "current_shipping_price_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_subtotal_price": "414.95",
    "current_subtotal_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_additional_fees_set": null,
    "current_total_discounts": "0.00",
    "current_total_discounts_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "current_total_duties_set": null,
    "current_total_price": "414.95",
    "current_total_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "current_total_tax": "0.00",
    "current_total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "customer_locale": "en",
    "device_id": null,
    "discount_codes": [],
    "duties_included": false,
    "email": "jon@example.com",
    "estimated_taxes": false,
    "financial_status": "voided",
    "fulfillment_status": null,
    "landing_site": null,
    "landing_site_ref": null,
    "location_id": null,
    "merchant_business_entity_id": "MTU0ODM4MDAwOQ",
    "merchant_of_record_app_id": null,
    "name": "#9999",
    "note": null,
    "note_attributes": [],
    "number": 234,
    "order_number": 1234,
    "order_status_url": "https://jsmith.myshopify.com/548380009/orders/123456abcd/authenticate?key=abcdefg",
    "original_total_additional_fees_set": null,
    "original_total_duties_set": null,
    "payment_gateway_names": [
      "visa",
      "bogus"
    ],
    "phone": null,
    "po_number": null,
    "presentment_currency": "USD",
    "processed_at": "2021-12-31T19:00:00-05:00",
    "reference": null,
    "referring_site": null,
    "source_identifier": null,
    "source_name": "web",
    "source_url": null,
    "subtotal_price": "404.95",
    "subtotal_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "tags": "tag1, tag2",
    "tax_exempt": false,
    "tax_lines": [],
    "taxes_included": false,
    "test": true,
    "token": "123456abcd",
    "total_cash_rounding_payment_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_cash_rounding_refund_adjustment_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_discounts": "20.00",
    "total_discounts_set": {
      "shop_money": {
        "amount": "20.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "20.00",
        "currency_code": "USD"
      }
    },
    "total_line_items_price": "414.95",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "414.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "414.95",
        "currency_code": "USD"
      }
    },
    "total_outstanding": "414.95",
    "total_price": "404.95",
    "total_price_set": {
      "shop_money": {
        "amount": "404.95",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "404.95",
        "currency_code": "USD"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "10.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "10.00",
        "currency_code": "USD"
      }
    },
    "total_tax": "0.00",
    "total_tax_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "total_tip_received": "0.00",
    "total_weight": 0,
    "updated_at": "2021-12-31T19:00:00-05:00",
    "user_id": null,
    "billing_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "customer": {
      "id": 115310627314723954,
      "created_at": null,
      "updated_at": null,
      "first_name": "John",
      "last_name": "Smith",
      "state": "disabled",
      "note": null,
      "verified_email": true,
      "multipass_identifier": null,
      "tax_exempt": false,
      "email": "john@example.com",
      "phone": null,
      "currency": "USD",
      "tax_exemptions": [],
      "admin_graphql_api_id": "gid://shopify/Customer/115310627314723954",
      "default_address": {
        "id": 715243470612851245,
        "customer_id": 115310627314723954,
        "first_name": "John",
        "last_name": "Smith",
        "company": null,
        "address1": "123 Elm St.",
        "address2": null,
        "city": "Ottawa",
        "province": "Ontario",
        "country": "Canada",
        "zip": "K2H7A8",
        "phone": "123-123-1234",
        "name": "John Smith",
        "province_code": "ON",
        "country_code": "CA",
        "country_name": "Canada",
        "default": true
      }
    },
    "discount_applications": [],
    "fulfillments": [],
    "line_items": [
      {
        "id": 487817672276298554,
        "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
        "attributed_staffs": [
          {
            "id": "gid://shopify/StaffMember/902541635",
            "quantity": 1
          }
        ],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 100,
        "name": "Aviator sunglasses",
        "price": "89.99",
        "price_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": null,
        "sku": "SKU2006-001",
        "taxable": true,
        "title": "Aviator sunglasses",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 789012345678901234,
        "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Lens Protection Plan (2 Year)",
        "price": "19.99",
        "price_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "LENS-PROTECT-2YR",
        "taxable": true,
        "title": "Lens Protection Plan (2 Year)",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 890123456789012345,
        "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 0,
        "name": "Premium Leather Case",
        "price": "24.99",
        "price_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "product_exists": false,
        "product_id": null,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 234567890123456789,
        "sku": "CASE-LEATHER-PREM",
        "taxable": true,
        "title": "Premium Leather Case",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 976318377106520349,
        "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 1000,
        "name": "Mid-century lounger",
        "price": "159.99",
        "price_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-020",
        "taxable": true,
        "title": "Mid-century lounger",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      },
      {
        "id": 315789986012684393,
        "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
        "attributed_staffs": [],
        "current_quantity": 1,
        "fulfillable_quantity": 1,
        "fulfillment_service": "manual",
        "fulfillment_status": null,
        "gift_card": false,
        "grams": 500,
        "name": "Coffee table",
        "price": "119.99",
        "price_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "product_exists": true,
        "product_id": 788032119674292922,
        "properties": [],
        "quantity": 1,
        "requires_shipping": true,
        "sales_line_item_group_id": 142831562,
        "sku": "SKU2006-035",
        "taxable": true,
        "title": "Coffee table",
        "total_discount": "0.00",
        "total_discount_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "variant_id": null,
        "variant_inventory_management": null,
        "variant_title": null,
        "vendor": null,
        "tax_lines": [],
        "duties": [],
        "discount_allocations": []
      }
    ],
    "payment_terms": null,
    "refunds": [],
    "shipping_address": {
      "first_name": "Steve",
      "address1": "123 Shipping Street",
      "phone": "555-555-SHIP",
      "city": "Shippington",
      "zip": "40003",
      "province": "Kentucky",
      "country": "United States",
      "last_name": "Shipper",
      "address2": null,
      "company": "Shipping Company",
      "latitude": null,
      "longitude": null,
      "name": "Steve Shipper",
      "country_code": "US",
      "province_code": "KY"
    },
    "shipping_lines": [
      {
        "id": 271878346596884015,
        "carrier_identifier": null,
        "code": null,
        "current_discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "discounted_price": "0.00",
        "discounted_price_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "is_removed": false,
        "phone": null,
        "price": "10.00",
        "price_set": {
          "shop_money": {
            "amount": "10.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "10.00",
            "currency_code": "USD"
          }
        },
        "requested_fulfillment_service_id": null,
        "source": "shopify",
        "title": "Generic Shipping",
        "tax_lines": [],
        "discount_allocations": []
      }
    ],
    "returns": [],
    "line_item_groups": []
  }
  ```

* #### payment\_schedules/due: Sample Payload

  #####

  ```undefined
  {
    "amount": "0.00",
    "balance_due": "0.00",
    "completed_at": "2021-01-02T00:00:00-05:00",
    "created_at": "2021-01-01T00:00:00-05:00",
    "currency": "USD",
    "due_at": "2021-01-02T00:00:00-05:00",
    "id": 606405506930370084,
    "issued_at": "2021-01-01T00:00:00-05:00",
    "payment_terms_id": 706405506930370084,
    "presentment_currency": "USD",
    "total_balance": "0.00",
    "total_price": "0.00",
    "updated_at": "2021-01-01T00:00:01-05:00",
    "admin_graphql_api_id": "gid://shopify/PaymentSchedule/606405506930370084"
  }
  ```

* #### payment\_terms/create: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "payment_terms_name": "Net 7",
    "payment_terms_type": "net",
    "due_in_days": 7,
    "created_at": "2021-01-01T00:00:00-05:00",
    "updated_at": "2021-01-01T00:00:01-05:00",
    "payment_schedules": [
      {
        "amount": "0.00",
        "balance_due": "0.00",
        "completed_at": "2021-01-02T00:00:00-05:00",
        "created_at": "2021-01-01T00:00:00-05:00",
        "currency": "USD",
        "due_at": "2021-01-02T00:00:00-05:00",
        "id": 606405506930370084,
        "issued_at": "2021-01-01T00:00:00-05:00",
        "payment_terms_id": 706405506930370084,
        "presentment_currency": "USD",
        "total_balance": "0.00",
        "total_price": "0.00",
        "updated_at": "2021-01-01T00:00:01-05:00",
        "admin_graphql_api_id": "gid://shopify/PaymentSchedule/606405506930370084"
      }
    ],
    "admin_graphql_api_id": "gid://shopify/PaymentsPaymentFlexibilityPaymentTermsPaymentTerms/706405506930370084"
  }
  ```

* #### payment\_terms/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084
  }
  ```

* #### payment\_terms/update: Sample Payload

  #####

  ```undefined
  {
    "id": 706405506930370084,
    "payment_terms_name": "Net 7",
    "payment_terms_type": "net",
    "due_in_days": 7,
    "created_at": "2021-01-01T00:00:00-05:00",
    "updated_at": "2021-01-01T00:00:01-05:00",
    "payment_schedules": [
      {
        "amount": "0.00",
        "balance_due": "0.00",
        "completed_at": "2021-01-02T00:00:00-05:00",
        "created_at": "2021-01-01T00:00:00-05:00",
        "currency": "USD",
        "due_at": "2021-01-02T00:00:00-05:00",
        "id": 606405506930370084,
        "issued_at": "2021-01-01T00:00:00-05:00",
        "payment_terms_id": 706405506930370084,
        "presentment_currency": "USD",
        "total_balance": "0.00",
        "total_price": "0.00",
        "updated_at": "2021-01-01T00:00:01-05:00",
        "admin_graphql_api_id": "gid://shopify/PaymentSchedule/606405506930370084"
      }
    ],
    "admin_graphql_api_id": "gid://shopify/PaymentsPaymentFlexibilityPaymentTermsPaymentTerms/706405506930370084"
  }
  ```

* #### product\_feeds/create: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/ProductFeed/",
    "country": "CA",
    "language": "EN",
    "status": ""
  }
  ```

* #### product\_feeds/full\_sync: Sample Payload

  #####

  ```undefined
  {
    "metadata": {
      "action": "CREATE",
      "type": "FULL",
      "resource": "PRODUCT",
      "fullSyncId": "gid://shopify/ProductFullSync/1123511235",
      "truncatedFields": [],
      "occurred_at": "2022-01-01T00:00:00.000Z"
    },
    "productFeed": {
      "id": "gid://shopify/ProductFeed/12345",
      "shop_id": "gid://shopify/Shop/12345",
      "language": "EN",
      "country": "CA"
    },
    "product": {
      "id": "gid://shopify/Product/12345",
      "title": "Coffee",
      "description": "The best coffee in the world",
      "onlineStoreUrl": "https://example.com/products/coffee",
      "createdAt": "2021-12-31T19:00:00-05:00",
      "updatedAt": "2021-12-31T19:00:00-05:00",
      "status": "ACTIVE",
      "isPublished": true,
      "publishedAt": "2021-12-31T19:00:00-05:00",
      "productType": "Coffee",
      "vendor": "Cawfee Inc",
      "handle": "",
      "images": {
        "edges": [
          {
            "node": {
              "id": "gid://shopify/ProductImage/394",
              "url": "https://cdn.shopify.com/s/files/1/0262/9117/5446/products/IMG_0022.jpg?v=1675101331",
              "height": 3024,
              "width": 4032
            }
          }
        ]
      },
      "options": [
        {
          "name": "Title",
          "values": [
            "151cm",
            "155cm",
            "158cm"
          ]
        }
      ],
      "seo": {
        "title": "seo title",
        "description": "seo description"
      },
      "tags": [
        "tag1",
        "tag2"
      ],
      "variants": {
        "edges": [
          {
            "node": {
              "id": "gid://shopify/ProductVariant/1",
              "title": "151cm",
              "price": {
                "amount": "100.00",
                "currencyCode": "CAD"
              },
              "compareAtPrice": null,
              "sku": "12345",
              "barcode": null,
              "quantityAvailable": 10,
              "availableForSale": true,
              "weight": 2.3,
              "weightUnit": "KILOGRAMS",
              "requireShipping": true,
              "inventoryPolicy": "DENY",
              "createdAt": "2021-12-31T19:00:00-05:00",
              "updatedAt": "2021-12-31T19:00:00-05:00",
              "image": {
                "id": "gid://shopify/ProductImage/394",
                "url": "https://cdn.shopify.com/s/files/1/0262/9117/5446/products/IMG_0022.jpg?v=1675101331",
                "height": 3024,
                "width": 4032
              },
              "selectedOptions": [
                {
                  "name": "Title",
                  "value": "151cm"
                }
              ]
            }
          }
        ]
      }
    },
    "products": null
  }
  ```

* #### product\_feeds/full\_sync\_finish: Sample Payload

  #####

  ```undefined
  {
    "metadata": {
      "action": "CREATE",
      "type": "FULL",
      "resource": "PRODUCT",
      "fullSyncId": "gid://shopify/ProductFullSync/1123511235",
      "truncatedFields": [],
      "occurred_at": "2022-01-01T00:00:00.000Z"
    },
    "productFeed": {
      "id": "gid://shopify/ProductFeed/12345",
      "shop_id": "gid://shopify/Shop/12345",
      "language": "EN",
      "country": "CA"
    },
    "fullSync": {
      "createdAt": "2021-12-31 19:00:00 -0500",
      "errorCode": null,
      "status": "completed",
      "count": 12,
      "url": null
    }
  }
  ```

* #### product\_feeds/incremental\_sync: Sample Payload

  #####

  ```undefined
  {
    "metadata": {
      "action": "CREATE",
      "type": "INCREMENTAL",
      "resource": "PRODUCT",
      "truncatedFields": [],
      "occured_at": "2021-12-31T19:00:00-05:00"
    },
    "productFeed": {
      "id": "gid://shopify/ProductFeed/12345",
      "shop_id": "gid://shopify/Shop/12345",
      "language": "EN",
      "country": "CA"
    },
    "product": {
      "id": "gid://shopify/Product/12345",
      "title": "Coffee",
      "description": "The best coffee in the world",
      "onlineStoreUrl": "https://example.com/products/coffee",
      "createdAt": "2021-12-31T19:00:00-05:00",
      "updatedAt": "2021-12-31T19:00:00-05:00",
      "status": "ACTIVE",
      "isPublished": true,
      "publishedAt": "2021-12-31T19:00:00-05:00",
      "productType": "Coffee",
      "vendor": "Cawfee Inc",
      "handle": "",
      "images": {
        "edges": [
          {
            "node": {
              "id": "gid://shopify/ProductImage/394",
              "url": "https://cdn.shopify.com/s/files/1/0262/9117/5446/products/IMG_0022.jpg?v=1675101331",
              "height": 3024,
              "width": 4032
            }
          }
        ]
      },
      "options": [
        {
          "name": "Title",
          "values": [
            "151cm",
            "155cm",
            "158cm"
          ]
        }
      ],
      "seo": {
        "title": "seo title",
        "description": "seo description"
      },
      "tags": [
        "tag1",
        "tag2"
      ],
      "variants": {
        "edges": [
          {
            "node": {
              "id": "gid://shopify/ProductVariant/1",
              "title": "151cm",
              "price": {
                "amount": "100.00",
                "currencyCode": "CAD"
              },
              "compareAtPrice": null,
              "sku": "12345",
              "barcode": null,
              "quantityAvailable": 10,
              "availableForSale": true,
              "weight": 2.3,
              "weightUnit": "KILOGRAMS",
              "requireShipping": true,
              "inventoryPolicy": "DENY",
              "createdAt": "2021-12-31T19:00:00-05:00",
              "updatedAt": "2021-12-31T19:00:00-05:00",
              "image": {
                "id": "gid://shopify/ProductImage/394",
                "url": "https://cdn.shopify.com/s/files/1/0262/9117/5446/products/IMG_0022.jpg?v=1675101331",
                "height": 3024,
                "width": 4032
              },
              "selectedOptions": [
                {
                  "name": "Title",
                  "value": "151cm"
                }
              ]
            }
          }
        ]
      }
    },
    "products": null
  }
  ```

* #### product\_feeds/update: Sample Payload

  #####

  ```undefined
  {
    "id": "gid://shopify/ProductFeed/",
    "country": "CA",
    "language": "EN",
    "status": ""
  }
  ```

* #### product\_listings/add: Sample Payload

  #####

  ```undefined
  {
    "product_listing": {
      "product_id": 788032119674292922,
      "created_at": null,
      "updated_at": "2021-12-31T19:00:00-05:00",
      "body_html": "An example T-Shirt",
      "handle": "example-t-shirt",
      "product_type": "Shirts",
      "title": "Example T-Shirt",
      "vendor": "Acme",
      "available": true,
      "tags": "example, mens, t-shirt",
      "published_at": "2021-12-31T19:00:00-05:00",
      "variants": [
        {
          "id": 642667041472713922,
          "title": "Small",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Small"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 1,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 75,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-30T19:00:00-05:00"
        },
        {
          "id": 757650484644203962,
          "title": "Medium",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Medium"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 2,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 50,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-31T19:00:00-05:00"
        }
      ],
      "images": [],
      "options": [
        {
          "id": 527050010214937811,
          "name": "Title",
          "product_id": 788032119674292922,
          "position": 1,
          "values": [
            "Small",
            "Medium"
          ]
        }
      ]
    }
  }
  ```

* #### product\_listings/remove: Sample Payload

  #####

  ```undefined
  {
    "product_listing": {
      "product_id": 788032119674292922
    }
  }
  ```

* #### product\_listings/update: Sample Payload

  #####

  ```undefined
  {
    "product_listing": {
      "product_id": 788032119674292922,
      "created_at": null,
      "updated_at": "2021-12-31T19:00:00-05:00",
      "body_html": "An example T-Shirt",
      "handle": "example-t-shirt",
      "product_type": "Shirts",
      "title": "Example T-Shirt",
      "vendor": "Acme",
      "available": true,
      "tags": "example, mens, t-shirt",
      "published_at": "2021-12-31T19:00:00-05:00",
      "variants": [
        {
          "id": 642667041472713922,
          "title": "Small",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Small"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 1,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 75,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-30T19:00:00-05:00"
        },
        {
          "id": 757650484644203962,
          "title": "Medium",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Medium"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 2,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 50,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-31T19:00:00-05:00"
        }
      ],
      "images": [],
      "options": [
        {
          "id": 527050010214937811,
          "name": "Title",
          "product_id": 788032119674292922,
          "position": 1,
          "values": [
            "Small",
            "Medium"
          ]
        }
      ]
    }
  }
  ```

* #### product\_publications/create: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "publication_id": 123456,
    "published_at": "2021-12-31T19:00:00-05:00",
    "published": true,
    "created_at": null,
    "updated_at": null,
    "product_id": 788032119674292922
  }
  ```

* #### product\_publications/delete: Sample Payload

  #####

  ```undefined
  {
    "id": null
  }
  ```

* #### product\_publications/update: Sample Payload

  #####

  ```undefined
  {
    "id": null,
    "publication_id": 123456,
    "published_at": "2021-12-31T19:00:00-05:00",
    "published": true,
    "created_at": null,
    "updated_at": null,
    "product_id": 788032119674292922
  }
  ```

* #### products/create: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/Product/788032119674292922",
    "body_html": "An example T-Shirt",
    "created_at": null,
    "handle": "example-t-shirt",
    "id": 788032119674292922,
    "product_type": "Shirts",
    "published_at": "2021-12-31T19:00:00-05:00",
    "template_suffix": null,
    "title": "Example T-Shirt",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "vendor": "Acme",
    "status": "active",
    "published_scope": "web",
    "tags": "example, mens, t-shirt",
    "variants": [
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
        "barcode": null,
        "compare_at_price": "24.99",
        "created_at": "2021-12-29T19:00:00-05:00",
        "id": 642667041472713922,
        "inventory_policy": "deny",
        "position": 1,
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": null,
        "taxable": true,
        "title": "Small",
        "updated_at": "2021-12-30T19:00:00-05:00",
        "option1": "Small",
        "option2": null,
        "option3": null,
        "image_id": null,
        "inventory_item_id": null,
        "inventory_quantity": 75,
        "old_inventory_quantity": 75
      },
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/757650484644203962",
        "barcode": null,
        "compare_at_price": "24.99",
        "created_at": "2021-12-29T19:00:00-05:00",
        "id": 757650484644203962,
        "inventory_policy": "deny",
        "position": 2,
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": null,
        "taxable": true,
        "title": "Medium",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "option1": "Medium",
        "option2": null,
        "option3": null,
        "image_id": null,
        "inventory_item_id": null,
        "inventory_quantity": 50,
        "old_inventory_quantity": 50
      }
    ],
    "options": [],
    "images": [],
    "image": null,
    "media": [],
    "variant_gids": [
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/757650484644203962",
        "updated_at": "2022-01-01T00:00:00.000Z"
      },
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
        "updated_at": "2021-12-31T00:00:00.000Z"
      }
    ],
    "has_variants_that_requires_components": false,
    "category": null
  }
  ```

* #### products/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 788032119674292922
  }
  ```

* #### products/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/Product/788032119674292922",
    "body_html": "An example T-Shirt",
    "created_at": null,
    "handle": "example-t-shirt",
    "id": 788032119674292922,
    "product_type": "Shirts",
    "published_at": "2021-12-31T19:00:00-05:00",
    "template_suffix": null,
    "title": "Example T-Shirt",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "vendor": "Acme",
    "status": "active",
    "published_scope": "web",
    "tags": "example, mens, t-shirt",
    "variants": [
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
        "barcode": null,
        "compare_at_price": "24.99",
        "created_at": "2021-12-29T19:00:00-05:00",
        "id": 642667041472713922,
        "inventory_policy": "deny",
        "position": 1,
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": null,
        "taxable": true,
        "title": "Small",
        "updated_at": "2021-12-30T19:00:00-05:00",
        "option1": "Small",
        "option2": null,
        "option3": null,
        "image_id": null,
        "inventory_item_id": null,
        "inventory_quantity": 75,
        "old_inventory_quantity": 75
      },
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/757650484644203962",
        "barcode": null,
        "compare_at_price": "24.99",
        "created_at": "2021-12-29T19:00:00-05:00",
        "id": 757650484644203962,
        "inventory_policy": "deny",
        "position": 2,
        "price": "19.99",
        "product_id": 788032119674292922,
        "sku": null,
        "taxable": true,
        "title": "Medium",
        "updated_at": "2021-12-31T19:00:00-05:00",
        "option1": "Medium",
        "option2": null,
        "option3": null,
        "image_id": null,
        "inventory_item_id": null,
        "inventory_quantity": 50,
        "old_inventory_quantity": 50
      }
    ],
    "options": [],
    "images": [],
    "image": null,
    "media": [],
    "variant_gids": [
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/757650484644203962",
        "updated_at": "2022-01-01T00:00:00.000Z"
      },
      {
        "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
        "updated_at": "2021-12-31T00:00:00.000Z"
      }
    ],
    "has_variants_that_requires_components": false,
    "category": null
  }
  ```

* #### profiles/create: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "admin_graphql_api_id": "gid://shopify/DeliveryProfile/1",
    "name": "Example Delivery Profile",
    "default": false,
    "profile_type": null,
    "version": 1
  }
  ```

* #### profiles/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "admin_graphql_api_id": "gid://shopify/DeliveryProfile/1",
    "name": "Example Delivery Profile",
    "default": false,
    "profile_type": null,
    "version": 1
  }
  ```

* #### profiles/update: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "admin_graphql_api_id": "gid://shopify/DeliveryProfile/1",
    "name": "Example Delivery Profile",
    "default": false,
    "profile_type": null,
    "version": 1
  }
  ```

* #### refunds/create: Sample Payload

  #####

  ```undefined
  {
    "id": 890088186047892319,
    "order_id": 820982911946154508,
    "created_at": "2021-12-31T19:00:00-05:00",
    "note": "Things were damaged",
    "user_id": 548380009,
    "processed_at": "2021-12-31T19:00:00-05:00",
    "duties": [],
    "total_duties_set": {
      "shop_money": {
        "amount": "0.00",
        "currency_code": "USD"
      },
      "presentment_money": {
        "amount": "0.00",
        "currency_code": "USD"
      }
    },
    "return": null,
    "refund_shipping_lines": [],
    "restock": false,
    "admin_graphql_api_id": "gid://shopify/Refund/890088186047892319",
    "order_adjustments": [],
    "refund_line_items": [
      {
        "id": 487817672276298627,
        "quantity": 1,
        "line_item_id": 487817672276298554,
        "location_id": null,
        "restock_type": "no_restock",
        "subtotal": 89.99,
        "total_tax": 0.0,
        "subtotal_set": {
          "shop_money": {
            "amount": "89.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "89.99",
            "currency_code": "USD"
          }
        },
        "total_tax_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "line_item": {
          "id": 487817672276298554,
          "variant_id": null,
          "title": "Aviator sunglasses",
          "quantity": 1,
          "sku": "SKU2006-001",
          "variant_title": null,
          "vendor": null,
          "fulfillment_service": "manual",
          "product_id": 788032119674292922,
          "requires_shipping": true,
          "taxable": true,
          "gift_card": false,
          "name": "Aviator sunglasses",
          "variant_inventory_management": null,
          "properties": [],
          "product_exists": true,
          "fulfillable_quantity": 1,
          "grams": 100,
          "price": "89.99",
          "total_discount": "0.00",
          "fulfillment_status": null,
          "price_set": {
            "shop_money": {
              "amount": "89.99",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "89.99",
              "currency_code": "USD"
            }
          },
          "total_discount_set": {
            "shop_money": {
              "amount": "0.00",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "0.00",
              "currency_code": "USD"
            }
          },
          "discount_allocations": [],
          "duties": [],
          "admin_graphql_api_id": "gid://shopify/LineItem/487817672276298554",
          "tax_lines": []
        }
      },
      {
        "id": 789012345678901307,
        "quantity": 1,
        "line_item_id": 789012345678901234,
        "location_id": null,
        "restock_type": "no_restock",
        "subtotal": 19.99,
        "total_tax": 0.0,
        "subtotal_set": {
          "shop_money": {
            "amount": "19.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "19.99",
            "currency_code": "USD"
          }
        },
        "total_tax_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "line_item": {
          "id": 789012345678901234,
          "variant_id": null,
          "title": "Lens Protection Plan (2 Year)",
          "quantity": 1,
          "sku": "LENS-PROTECT-2YR",
          "variant_title": null,
          "vendor": null,
          "fulfillment_service": "manual",
          "product_id": null,
          "requires_shipping": true,
          "taxable": true,
          "gift_card": false,
          "name": "Lens Protection Plan (2 Year)",
          "variant_inventory_management": null,
          "properties": [],
          "product_exists": false,
          "fulfillable_quantity": 1,
          "grams": 0,
          "price": "19.99",
          "total_discount": "0.00",
          "fulfillment_status": null,
          "price_set": {
            "shop_money": {
              "amount": "19.99",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "19.99",
              "currency_code": "USD"
            }
          },
          "total_discount_set": {
            "shop_money": {
              "amount": "0.00",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "0.00",
              "currency_code": "USD"
            }
          },
          "discount_allocations": [],
          "duties": [],
          "admin_graphql_api_id": "gid://shopify/LineItem/789012345678901234",
          "tax_lines": []
        }
      },
      {
        "id": 890123456789012418,
        "quantity": 1,
        "line_item_id": 890123456789012345,
        "location_id": null,
        "restock_type": "no_restock",
        "subtotal": 24.99,
        "total_tax": 0.0,
        "subtotal_set": {
          "shop_money": {
            "amount": "24.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "24.99",
            "currency_code": "USD"
          }
        },
        "total_tax_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "line_item": {
          "id": 890123456789012345,
          "variant_id": null,
          "title": "Premium Leather Case",
          "quantity": 1,
          "sku": "CASE-LEATHER-PREM",
          "variant_title": null,
          "vendor": null,
          "fulfillment_service": "manual",
          "product_id": null,
          "requires_shipping": true,
          "taxable": true,
          "gift_card": false,
          "name": "Premium Leather Case",
          "variant_inventory_management": null,
          "properties": [],
          "product_exists": false,
          "fulfillable_quantity": 1,
          "grams": 0,
          "price": "24.99",
          "total_discount": "0.00",
          "fulfillment_status": null,
          "price_set": {
            "shop_money": {
              "amount": "24.99",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "24.99",
              "currency_code": "USD"
            }
          },
          "total_discount_set": {
            "shop_money": {
              "amount": "0.00",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "0.00",
              "currency_code": "USD"
            }
          },
          "discount_allocations": [],
          "duties": [],
          "admin_graphql_api_id": "gid://shopify/LineItem/890123456789012345",
          "tax_lines": []
        }
      },
      {
        "id": 976318377106520422,
        "quantity": 1,
        "line_item_id": 976318377106520349,
        "location_id": null,
        "restock_type": "no_restock",
        "subtotal": 159.99,
        "total_tax": 0.0,
        "subtotal_set": {
          "shop_money": {
            "amount": "159.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "159.99",
            "currency_code": "USD"
          }
        },
        "total_tax_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "line_item": {
          "id": 976318377106520349,
          "variant_id": null,
          "title": "Mid-century lounger",
          "quantity": 1,
          "sku": "SKU2006-020",
          "variant_title": null,
          "vendor": null,
          "fulfillment_service": "manual",
          "product_id": 788032119674292922,
          "requires_shipping": true,
          "taxable": true,
          "gift_card": false,
          "name": "Mid-century lounger",
          "variant_inventory_management": null,
          "properties": [],
          "product_exists": true,
          "fulfillable_quantity": 1,
          "grams": 1000,
          "price": "159.99",
          "total_discount": "5.00",
          "fulfillment_status": null,
          "price_set": {
            "shop_money": {
              "amount": "159.99",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "159.99",
              "currency_code": "USD"
            }
          },
          "total_discount_set": {
            "shop_money": {
              "amount": "5.00",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "5.00",
              "currency_code": "USD"
            }
          },
          "discount_allocations": [
            {
              "amount": "5.00",
              "discount_application_index": 0,
              "amount_set": {
                "shop_money": {
                  "amount": "5.00",
                  "currency_code": "USD"
                },
                "presentment_money": {
                  "amount": "5.00",
                  "currency_code": "USD"
                }
              }
            },
            {
              "amount": "5.00",
              "discount_application_index": 2,
              "amount_set": {
                "shop_money": {
                  "amount": "5.00",
                  "currency_code": "USD"
                },
                "presentment_money": {
                  "amount": "5.00",
                  "currency_code": "USD"
                }
              }
            }
          ],
          "duties": [],
          "admin_graphql_api_id": "gid://shopify/LineItem/976318377106520349",
          "tax_lines": []
        }
      },
      {
        "id": 315789986012684466,
        "quantity": 1,
        "line_item_id": 315789986012684393,
        "location_id": null,
        "restock_type": "no_restock",
        "subtotal": 119.99,
        "total_tax": 0.0,
        "subtotal_set": {
          "shop_money": {
            "amount": "119.99",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "119.99",
            "currency_code": "USD"
          }
        },
        "total_tax_set": {
          "shop_money": {
            "amount": "0.00",
            "currency_code": "USD"
          },
          "presentment_money": {
            "amount": "0.00",
            "currency_code": "USD"
          }
        },
        "line_item": {
          "id": 315789986012684393,
          "variant_id": null,
          "title": "Coffee table",
          "quantity": 1,
          "sku": "SKU2006-035",
          "variant_title": null,
          "vendor": null,
          "fulfillment_service": "manual",
          "product_id": 788032119674292922,
          "requires_shipping": true,
          "taxable": true,
          "gift_card": false,
          "name": "Coffee table",
          "variant_inventory_management": null,
          "properties": [],
          "product_exists": true,
          "fulfillable_quantity": 1,
          "grams": 500,
          "price": "119.99",
          "total_discount": "0.00",
          "fulfillment_status": null,
          "price_set": {
            "shop_money": {
              "amount": "119.99",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "119.99",
              "currency_code": "USD"
            }
          },
          "total_discount_set": {
            "shop_money": {
              "amount": "0.00",
              "currency_code": "USD"
            },
            "presentment_money": {
              "amount": "0.00",
              "currency_code": "USD"
            }
          },
          "discount_allocations": [],
          "duties": [],
          "admin_graphql_api_id": "gid://shopify/LineItem/315789986012684393",
          "tax_lines": []
        }
      }
    ],
    "transactions": [
      {
        "id": 245135271310201194,
        "order_id": 820982911946154508,
        "kind": "refund",
        "gateway": "bogus",
        "status": "success",
        "message": "This is a refund",
        "created_at": "2019-12-31T19:00:00-05:00",
        "test": false,
        "authorization": null,
        "location_id": null,
        "user_id": null,
        "parent_id": null,
        "processed_at": null,
        "device_id": null,
        "error_code": null,
        "source_name": "web",
        "receipt": {},
        "amount": "75.00",
        "currency": null,
        "payment_id": "#9999.",
        "total_unsettled_set": {
          "presentment_money": {
            "amount": "0.0",
            "currency": "XXX"
          },
          "shop_money": {
            "amount": "0.0",
            "currency": "XXX"
          }
        },
        "manual_payment_gateway": false,
        "amount_rounding": null,
        "admin_graphql_api_id": "gid://shopify/OrderTransaction/245135271310201194"
      },
      {
        "id": 839212141605670573,
        "order_id": 820982911946154508,
        "kind": "refund",
        "gateway": "bogus",
        "status": "success",
        "message": null,
        "created_at": "2020-01-01T19:00:00-05:00",
        "test": false,
        "authorization": null,
        "location_id": null,
        "user_id": null,
        "parent_id": null,
        "processed_at": null,
        "device_id": null,
        "error_code": null,
        "source_name": "web",
        "receipt": {},
        "amount": "10.00",
        "currency": null,
        "payment_id": "#9999.",
        "total_unsettled_set": {
          "presentment_money": {
            "amount": "0.0",
            "currency": "XXX"
          },
          "shop_money": {
            "amount": "0.0",
            "currency": "XXX"
          }
        },
        "manual_payment_gateway": false,
        "amount_rounding": null,
        "admin_graphql_api_id": "gid://shopify/OrderTransaction/839212141605670573"
      }
    ]
  }
  ```

* #### returns/approve: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "status": "open",
    "order": {
      "id": 4783296544821,
      "admin_graphql_api_id": "gid://shopify/Order/4783296544821"
    },
    "total_return_line_items": 2,
    "name": null,
    "return_line_items": [],
    "return_shipping_fees": [
      {
        "id": 987654321547866,
        "admin_graphql_api_id": "gid://shopify/ReturnShippingFee/987654321547866",
        "price": {
          "shop_money": {
            "amount": "10.0",
            "currency_code": "XXX"
          },
          "presentment_money": {
            "amount": "10.0",
            "currency_code": "XXX"
          }
        }
      }
    ],
    "exchange_line_items": [
      {
        "id": 987654321283476,
        "admin_graphql_api_id": "gid://shopify/ExchangeLineItem/987654321283476",
        "line_item": null
      }
    ],
    "total_exchange_line_items": 1
  }
  ```

* #### returns/cancel: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "order_id": 4783296544821,
    "status": "canceled"
  }
  ```

* #### returns/close: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "order_id": 4783296544821,
    "status": "closed"
  }
  ```

* #### returns/decline: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "status": "declined",
    "order": {
      "id": 4783296544821,
      "admin_graphql_api_id": "gid://shopify/Order/4783296544821"
    },
    "decline": {
      "reason": "return_period_ended",
      "note": "As discussed on the phone, the 30-day return window has ended."
    }
  }
  ```

* #### returns/reopen: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "order_id": 4783296544821,
    "status": "open"
  }
  ```

* #### returns/request: Sample Payload

  #####

  ```undefined
  {
    "id": 123134564567890,
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "status": "requested",
    "order": {
      "id": 4783296544821,
      "admin_graphql_api_id": "gid://shopify/Order/4783296544821"
    },
    "total_return_line_items": 2,
    "name": null,
    "return_line_items": [],
    "return_shipping_fees": [],
    "exchange_line_items": [],
    "total_exchange_line_items": 0
  }
  ```

* #### returns/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/Return/123134564567890",
    "return_line_items": {
      "removals": [
        {
          "admin_graphql_api_id": "gid://shopify/ReturnLineItem/987654321",
          "delta": 2
        }
      ]
    },
    "restocking_fees": {
      "updates": [],
      "removals": []
    },
    "return_shipping_fees": {
      "updates": [],
      "removals": []
    }
  }
  ```

* #### reverse\_deliveries/attach\_deliverable: Sample Payload

  #####

  ```undefined
  {
    "id": 9080907654321,
    "admin_graphql_api_id": "gid://shopify/ReverseDelivery/9080907654321",
    "return": {
      "id": 123134564567890,
      "admin_graphql_api_id": "gid://shopify/Return/123134564567890"
    },
    "shipping_deliverable": {
      "tracking": {
        "carrier_name": "USPS",
        "tracking_number": "123345345",
        "tracking_url": null
      },
      "label": {
        "public_file_url": null,
        "created_at": null
      }
    }
  }
  ```

* #### reverse\_fulfillment\_orders/dispose: Sample Payload

  #####

  ```undefined
  {
    "id": 11111111,
    "admin_graphql_api_id": "gid://shopify/ReverseFulfillmentOrder/11111111",
    "dispositions": [
      {
        "reverse_fulfillment_order_line_item": {
          "id": 2222222,
          "admin_graphql_api_id": "gid://shopify/ReverseFulfillmentOrderLineItem/2222222"
        },
        "reverse_delivery_line_item": null,
        "type": "restocked",
        "location": {
          "id": 3333333,
          "admin_graphql_api_id": "gid://shopify/Location/3333333"
        },
        "quantity": 1
      },
      {
        "reverse_fulfillment_order_line_item": {
          "id": 2222223,
          "admin_graphql_api_id": "gid://shopify/ReverseFulfillmentOrderLineItem/2222223"
        },
        "reverse_delivery_line_item": null,
        "type": "restocked",
        "location": {
          "id": 3333333,
          "admin_graphql_api_id": "gid://shopify/Location/3333333"
        },
        "quantity": 1
      }
    ],
    "total_dispositions": 2
  }
  ```

* #### scheduled\_product\_listings/add: Sample Payload

  #####

  ```undefined
  {
    "scheduled_product_listing": {
      "product_id": 788032119674292922,
      "created_at": null,
      "updated_at": "2021-12-31T19:00:00-05:00",
      "body_html": "An example T-Shirt",
      "handle": "example-t-shirt",
      "product_type": "Shirts",
      "title": "Example T-Shirt",
      "vendor": "Acme",
      "available": true,
      "tags": "example, mens, t-shirt",
      "variants": [
        {
          "id": 642667041472713922,
          "title": "Small",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Small"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 1,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 75,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-30T19:00:00-05:00"
        },
        {
          "id": 757650484644203962,
          "title": "Medium",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Medium"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 2,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 50,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-31T19:00:00-05:00"
        }
      ],
      "publish_at": null,
      "images": [],
      "options": [
        {
          "id": 527050010214937811,
          "name": "Title",
          "product_id": 788032119674292922,
          "position": 1,
          "values": [
            "Small",
            "Medium"
          ]
        }
      ]
    }
  }
  ```

* #### scheduled\_product\_listings/remove: Sample Payload

  #####

  ```undefined
  {
    "scheduled_product_listing": {
      "product_id": 788032119674292922
    }
  }
  ```

* #### scheduled\_product\_listings/update: Sample Payload

  #####

  ```undefined
  {
    "scheduled_product_listing": {
      "product_id": 788032119674292922,
      "created_at": null,
      "updated_at": "2021-12-31T19:00:00-05:00",
      "body_html": "An example T-Shirt",
      "handle": "example-t-shirt",
      "product_type": "Shirts",
      "title": "Example T-Shirt",
      "vendor": "Acme",
      "available": true,
      "tags": "example, mens, t-shirt",
      "variants": [
        {
          "id": 642667041472713922,
          "title": "Small",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Small"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 1,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 75,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-30T19:00:00-05:00"
        },
        {
          "id": 757650484644203962,
          "title": "Medium",
          "option_values": [
            {
              "option_id": 527050010214937811,
              "name": "Title",
              "value": "Medium"
            }
          ],
          "price": "19.99",
          "formatted_price": "$19.99",
          "compare_at_price": "24.99",
          "grams": 0,
          "requires_shipping": true,
          "sku": null,
          "barcode": null,
          "taxable": true,
          "position": 2,
          "available": true,
          "inventory_policy": "deny",
          "inventory_quantity": 50,
          "inventory_management": null,
          "fulfillment_service": "manual",
          "weight": 0.0,
          "weight_unit": "lb",
          "image_id": null,
          "created_at": "2021-12-29T19:00:00-05:00",
          "updated_at": "2021-12-31T19:00:00-05:00"
        }
      ],
      "publish_at": null,
      "images": [],
      "options": [
        {
          "id": 527050010214937811,
          "name": "Title",
          "product_id": 788032119674292922,
          "position": 1,
          "values": [
            "Small",
            "Medium"
          ]
        }
      ]
    }
  }
  ```

* #### segments/create: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "name": "Customers who have one order",
    "query": "number_of_orders = 1",
    "creationDate": "2022-01-01T00:00:00.000Z",
    "lastEditDate": "2022-01-01T00:00:00.000Z"
  }
  ```

* #### segments/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 1
  }
  ```

* #### segments/update: Sample Payload

  #####

  ```undefined
  {
    "id": 1,
    "name": "Customers who have one order",
    "query": "number_of_orders = 1",
    "creationDate": "2005-05-05T05:00:00.000Z",
    "lastEditDate": "2022-01-01T00:00:00.000Z"
  }
  ```

* #### selling\_plan\_groups/create: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SellingPlanGroup/1039518922",
    "id": 1039518922,
    "name": "Subscribe & Save",
    "merchant_code": "sub-n-save",
    "admin_graphql_api_app": "gid://shopify/App/2525000003",
    "app_id": null,
    "description": null,
    "options": [
      "Delivery every"
    ],
    "position": null,
    "summary": "1 delivery frequency,  discount",
    "selling_plans": [
      {
        "name": "Pay every month deliver every month",
        "options": [
          "month"
        ],
        "position": null,
        "description": null,
        "billing_policy": {
          "interval": "month",
          "interval_count": 1,
          "min_cycles": null,
          "max_cycles": null
        },
        "delivery_policy": {
          "interval": "month",
          "interval_count": 1,
          "anchors": [],
          "cutoff": null,
          "pre_anchor_behavior": "asap"
        },
        "pricing_policies": []
      }
    ],
    "product_variants": [],
    "products": []
  }
  ```

* #### selling\_plan\_groups/delete: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SellingPlanGroup/1039518920",
    "id": 1039518920
  }
  ```

* #### selling\_plan\_groups/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SellingPlanGroup/1039518932",
    "id": 1039518932,
    "name": "Subscribe & Save",
    "merchant_code": "sub-n-save",
    "admin_graphql_api_app": "gid://shopify/App/2525000003",
    "app_id": null,
    "description": null,
    "options": [
      "Delivery every"
    ],
    "position": null,
    "summary": "1 delivery frequency,  discount",
    "selling_plans": [
      {
        "name": "Pay every month deliver every month",
        "options": [
          "month"
        ],
        "position": null,
        "description": null,
        "billing_policy": {
          "interval": "month",
          "interval_count": 1,
          "min_cycles": null,
          "max_cycles": null
        },
        "delivery_policy": {
          "interval": "month",
          "interval_count": 1,
          "anchors": [],
          "cutoff": null,
          "pre_anchor_behavior": "asap"
        },
        "pricing_policies": []
      }
    ],
    "product_variants": [],
    "products": []
  }
  ```

* #### shop/redact: Sample Payload

  #####

  ```undefined
  {
    "shop_id": 954889,
    "shop_domain": "{shop}.myshopify.com"
  }
  ```

* #### shop/update: Sample Payload

  #####

  ```undefined
  {
    "id": 548380009,
    "name": "Super Toys",
    "email": "super@supertoys.com",
    "domain": null,
    "province": "Tennessee",
    "country": "US",
    "address1": "190 MacLaren Street",
    "zip": "37178",
    "city": "Houston",
    "source": null,
    "phone": "3213213210",
    "latitude": null,
    "longitude": null,
    "primary_locale": "en",
    "address2": null,
    "created_at": null,
    "updated_at": null,
    "country_code": "US",
    "country_name": "United States",
    "currency": "USD",
    "customer_email": "super@supertoys.com",
    "timezone": "(GMT-05:00) Eastern Time (US & Canada)",
    "iana_timezone": null,
    "shop_owner": "John Smith",
    "money_format": "${{amount}}",
    "money_with_currency_format": "${{amount}} USD",
    "weight_unit": "kg",
    "province_code": "TN",
    "taxes_included": null,
    "auto_configure_tax_inclusivity": null,
    "tax_shipping": null,
    "county_taxes": null,
    "plan_display_name": "Shopify Plus",
    "plan_name": "enterprise",
    "has_discounts": false,
    "has_gift_cards": true,
    "myshopify_domain": null,
    "google_apps_domain": null,
    "google_apps_login_enabled": null,
    "money_in_emails_format": "${{amount}}",
    "money_with_currency_in_emails_format": "${{amount}} USD",
    "eligible_for_payments": true,
    "requires_extra_payments_agreement": false,
    "password_enabled": null,
    "has_storefront": true,
    "finances": true,
    "primary_location_id": 655441491,
    "checkout_api_supported": true,
    "multi_location_enabled": true,
    "setup_required": false,
    "pre_launch_enabled": false,
    "enabled_presentment_currencies": [
      "USD"
    ],
    "marketing_sms_consent_enabled_at_checkout": false,
    "transactional_sms_disabled": false
  }
  ```

* #### subscription\_billing\_cycle\_edits/create: Sample Payload

  #####

  ```undefined
  {
    "subscription_contract_id": 1978600657,
    "cycle_start_at": "2022-10-01T00:00:00-04:00",
    "cycle_end_at": "2022-11-01T00:00:00-04:00",
    "cycle_index": 1,
    "contract_edit": null,
    "billing_attempt_expected_date": "2022-11-01T00:00:00-04:00",
    "skipped": false,
    "edited": false
  }
  ```

* #### subscription\_billing\_cycle\_edits/delete: Sample Payload

  #####

  ```undefined
  {
    "subscription_contract_id": 9972124661,
    "cycle_start_at": "2022-10-01T00:00:00-04:00",
    "cycle_end_at": "2022-11-01T00:00:00-04:00",
    "cycle_index": 1,
    "contract_edit": null,
    "billing_attempt_expected_date": "2022-11-01T00:00:00-04:00",
    "skipped": false,
    "edited": false
  }
  ```

* #### subscription\_billing\_cycle\_edits/update: Sample Payload

  #####

  ```undefined
  {
    "subscription_contract_id": 8688363084,
    "cycle_start_at": "2022-10-01T00:00:00-04:00",
    "cycle_end_at": "2022-11-01T00:00:00-04:00",
    "cycle_index": 1,
    "contract_edit": null,
    "billing_attempt_expected_date": "2022-11-01T00:00:00-04:00",
    "skipped": false,
    "edited": false
  }
  ```

* #### subscription\_billing\_cycles/skip: Sample Payload

  #####

  ```undefined
  {
    "subscription_contract_id": 2605256554,
    "cycle_start_at": "2022-10-01T00:00:00-04:00",
    "cycle_end_at": "2022-11-01T00:00:00-04:00",
    "cycle_index": 1,
    "contract_edit": null,
    "billing_attempt_expected_date": "2022-11-01T00:00:00-04:00",
    "skipped": true,
    "edited": true
  }
  ```

* #### subscription\_billing\_cycles/unskip: Sample Payload

  #####

  ```undefined
  {
    "subscription_contract_id": 2812021189,
    "cycle_start_at": "2022-10-01T00:00:00-04:00",
    "cycle_end_at": "2022-11-01T00:00:00-04:00",
    "cycle_index": 1,
    "contract_edit": null,
    "billing_attempt_expected_date": "2022-11-01T00:00:00-04:00",
    "skipped": false,
    "edited": true
  }
  ```

* #### subscription\_contracts/activate: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/4488765614",
    "id": 4488765614,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "active",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "3080372819"
  }
  ```

* #### subscription\_contracts/cancel: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/9264106522",
    "id": 9264106522,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "cancelled",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "4690720903"
  }
  ```

* #### subscription\_contracts/create: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/402440842",
    "id": 402440842,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "active",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "7232252373"
  }
  ```

* #### subscription\_contracts/expire: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/3953017108",
    "id": 3953017108,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "expired",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "6918683624"
  }
  ```

* #### subscription\_contracts/fail: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/9633163704",
    "id": 9633163704,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "failed",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "6529913781"
  }
  ```

* #### subscription\_contracts/pause: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/3334363200",
    "id": 3334363200,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "paused",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "1475081618"
  }
  ```

* #### subscription\_contracts/update: Sample Payload

  #####

  ```undefined
  {
    "admin_graphql_api_id": "gid://shopify/SubscriptionContract/7879037765",
    "id": 7879037765,
    "billing_policy": {
      "interval": "week",
      "interval_count": 4,
      "min_cycles": 1,
      "max_cycles": 2
    },
    "currency_code": "CAD",
    "customer_id": 1,
    "admin_graphql_api_customer_id": "gid://shopify/Customer/1",
    "delivery_policy": {
      "interval": "week",
      "interval_count": 2
    },
    "status": "active",
    "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
    "origin_order_id": 1,
    "revision_id": "7859577360"
  }
  ```

* #### tax\_services/create: Sample Payload

  #####

  ```undefined
  {
    "id": 1063370,
    "name": "Tax Service",
    "url": "https://taxes.shopify.com",
    "active": true
  }
  ```

* #### tax\_services/update: Sample Payload

  #####

  ```undefined
  {
    "id": 1063370,
    "name": "Tax Service",
    "url": "https://taxes.shopify.com",
    "active": true
  }
  ```

* #### tender\_transactions/create: Sample Payload

  #####

  ```undefined
  {
    "id": 220982911946154508,
    "order_id": 820982911946154508,
    "amount": "419.95",
    "currency": "USD",
    "user_id": null,
    "test": false,
    "processed_at": null,
    "remote_reference": "1001",
    "payment_details": null,
    "payment_method": "unknown"
  }
  ```

* #### themes/create: Sample Payload

  #####

  ```undefined
  {
    "id": 512162865275216980,
    "name": "Comfort",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "role": "main",
    "theme_store_id": 1234,
    "previewable": true,
    "processing": false,
    "admin_graphql_api_id": "gid://shopify/Theme/512162865275216980"
  }
  ```

* #### themes/delete: Sample Payload

  #####

  ```undefined
  {
    "id": 512162865275216980
  }
  ```

* #### themes/publish: Sample Payload

  #####

  ```undefined
  {
    "id": 512162865275216980,
    "name": "Comfort",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "role": "main",
    "theme_store_id": 1234,
    "previewable": true,
    "processing": false,
    "admin_graphql_api_id": "gid://shopify/Theme/512162865275216980"
  }
  ```

* #### themes/update: Sample Payload

  #####

  ```undefined
  {
    "id": 512162865275216980,
    "name": "Comfort",
    "created_at": "2021-12-31T19:00:00-05:00",
    "updated_at": "2021-12-31T19:00:00-05:00",
    "role": "main",
    "theme_store_id": 1234,
    "previewable": true,
    "processing": false,
    "admin_graphql_api_id": "gid://shopify/Theme/512162865275216980"
  }
  ```

* #### variants/in\_stock: Sample Payload

  #####

  ```undefined
  {
    "id": 642667041472713922,
    "product_id": 788032119674292922,
    "title": "Small",
    "price": "19.99",
    "position": 1,
    "inventory_policy": "deny",
    "compare_at_price": "24.99",
    "option1": "Small",
    "option2": null,
    "option3": null,
    "created_at": "2021-12-29T19:00:00-05:00",
    "updated_at": "2021-12-30T19:00:00-05:00",
    "taxable": true,
    "barcode": null,
    "sku": null,
    "inventory_quantity": 75,
    "old_inventory_quantity": 75,
    "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
    "image_id": null
  }
  ```

* #### variants/out\_of\_stock: Sample Payload

  #####

  ```undefined
  {
    "id": 642667041472713922,
    "product_id": 788032119674292922,
    "title": "Small",
    "price": "19.99",
    "position": 1,
    "inventory_policy": "deny",
    "compare_at_price": "24.99",
    "option1": "Small",
    "option2": null,
    "option3": null,
    "created_at": "2021-12-29T19:00:00-05:00",
    "updated_at": "2021-12-30T19:00:00-05:00",
    "taxable": true,
    "barcode": null,
    "sku": null,
    "inventory_quantity": 0,
    "old_inventory_quantity": 0,
    "admin_graphql_api_id": "gid://shopify/ProductVariant/642667041472713922",
    "image_id": null
  }
  ```

***

## Customize

##### Filter events

Manage the number of event messages your app receives by filtering events. Unlike payload modifications, filters are made up of rules, applied to a webhook subscription, which act as a gate for whether or not webhooks are delivered when an event occurs.

[Navigate to - Webhooks filters guide](https://shopify.dev/docs/apps/build/webhooks/delivery-filtering)

[Navigate to - Shopify API Search Syntax](https://shopify.dev/docs/api/usage/search-syntax)

##### Modify payloads

Shopify provides you with a way to modify the payload you receive when you subscribe to webhook topics. Unlike filters, which always return the same payload, this feature enables you to specify what subset of information is most relevant to your use case from a webhook.

[Navigate to - Webhooks payload modification guide](https://shopify.dev/docs/apps/build/webhooks/delivery-structure)

##### Use alongside Events

For topics with Events support, you can run both an Events subscription and a webhook in the same `shopify.app.toml`. Events gives you field-level triggers and custom GraphQL payloads. Use webhooks for topics that don't yet have Events support.

**Info:**

Events require Shopify CLI 3.92 or higher. Run `shopify version` to check your version.

[Compare - Events and webhooks](https://shopify.dev/docs/apps/build/events-webhooks)

[Reference - Events reference](https://shopify.dev/docs/api/events)

## Filter events

```toml
[[webhooks.subscriptions]]
topics = ["products/update"]
uri = "https://example.com/webhooks"
filter = "id:* AND status:active AND (product_type:Music OR product_type:Movies) AND -invalid_field:* AND variants.taxable:true AND variants.weight:<5 AND variants.price:>=100 AND variants.title:Album*"
```

## Modify payloads

```toml
[[webhooks.subscriptions]]
topics = ["customers/delete"]
uri = "https://example.com/webhooks"
include_fields = ["id", "email_marketing_consent", "updated_at"]
```

## customers/update payload

##### Modified

```toml
{
  "id": 706405506930370000,
  "updated_at": "2021-12-31T19:00:00-05:00",
  "email_marketing_consent": null
}
```

##### Original

```toml
{
  "id": 706405506930370000,
  "email": "bob@biller.com",
  "created_at": "2021-12-31T19:00:00-05:00",
  "updated_at": "2021-12-31T19:00:00-05:00",
  "first_name": "Bob",
  "last_name": "Biller",
  "orders_count": 0,
  "state": "disabled",
  "total_spent": "0.00",
  "last_order_id": null,
  "note": "This customer loves ice cream",
  "verified_email": true,
  "multipass_identifier": null,
  "tax_exempt": false,
  "tags": "",
  "last_order_name": null,
  "currency": "USD",
  "phone": null,
  "addresses": [],
  "tax_exemptions": [],
  "email_marketing_consent": null,
  "sms_marketing_consent": null,
  "admin_graphql_api_id": "gid://shopify/Customer/706405506930370084"
}
```

## shopify.app.toml

```toml
[webhooks]
api_version = "{% api_version %}"


[[webhooks.subscriptions]]
topics = ["orders/create"]
uri = "https://your-app.example.com/webhooks/orders"


[events]
api_version = "unstable"


[[events.subscription]]
handle = "product-price-watcher"
topic = "Product"
actions = ["update"]
triggers = ["product.variants.price"]
uri = "https://your-app.example.com/events"
```

***

