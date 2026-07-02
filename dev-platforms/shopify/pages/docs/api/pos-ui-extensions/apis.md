---
title: "**Extension APIs**"
source: https://shopify.dev/docs/api/pos-ui-extensions/apis.md
path: docs/api/pos-ui-extensions/apis
---

---
title: Target APIs
description: >-
  When you build a POS UI extension, Shopify automatically provides you with
  specific APIs based on where your extension runs within the POS interface.
  This system ensures extensions receive exactly the data and functionality they
  need for their particular use case, while maintaining security and
  performance.
api_version: 2025-10
source_url:
  html: 'https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis'
  md: 'https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis.md'
api_name: pos-ui-extensions
---

# Target APIs

When you build a POS UI extension, Shopify automatically provides you with specific APIs based on where your extension runs within the POS interface. This system ensures extensions receive exactly the data and functionality they need for their particular use case, while maintaining security and performance.

Your [target](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/targets) determines which APIs you receive because different locations in POS require different capabilities.

## Contextual APIs

Contextual APIs provide access to data and operations specific to your extension's current location within [the POS app](https://apps.shopify.com/shopify-pos). These APIs give you the ability to read and modify context-specific information like cart contents, selected products, customer details, or order information based on where your extension is rendered.

| Name | Description |
| - | - |
| [Cart API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/cart-api) | Add, remove, and modify cart items, apply discounts, and manage cart properties. |
| [Cart Line Item API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/cart-line-item-api) | Read and interact with the currently selected cart line item in detail views. |
| [Customer API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/customer-api) | Read customer information and build customer-specific functionality. |
| [Draft Order API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/draft-order-api) | Read and manipulate draft order data in draft order detail views. |
| [Order API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/order-api) | Read order data and build post-purchase, return, and exchange functionality. |
| [Product API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/contextual-apis/product-api) | Access the product ID and variant ID of the currently viewed or selected product. |

## Platform APIs

Platform APIs expose device-specific hardware capabilities and native POS functionality that differentiate mobile retail experiences from traditional web applications. These APIs provide access to physical device features like barcode scanners, receipt printers, camera scanning, and device connectivity status. They enable extensions to use the unique hardware and navigation patterns of POS devices to create native retail experiences.

| Name | Description |
| - | - |
| [Connectivity API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/connectivity-api) | Check device connectivity status and Internet connection availability. |
| [Device API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/device-api) | Retrieve device information including device name, ID, and hardware capabilities. |
| [Navigation API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/navigation-api) | Navigate between different screens and views within the POS interface. |
| [PinPad API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/pinpad-api) | Display a modal pinpad interface for secure PIN entry and validation. |
| [Print API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/print-api) | Send documents and receipts to connected printers or trigger the device print dialog. |
| [Scanner API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/scanner-api) | Capture barcodes and QR codes using the device camera or connected barcode scanners. |
| [Storage API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/platform-apis/storage-api) | Store and retrieve extension data in POS local storage with up to 100 entries per extension. |

## Standard APIs

Standard APIs offer core functionality that most extensions need regardless of their specific use case or location within [the POS app](https://apps.shopify.com/shopify-pos). These APIs provide essential capabilities like local data storage, session and authentication management, user notifications through toasts, and internationalization support. They serve as the foundational building blocks that enable extensions to integrate with the POS environment while maintaining consistent behavior across different contexts.

| Name | Description |
| - | - |
| [Action API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/standard-apis/action-api) | Launch modal dialogs for multi-step workflows and complex interactions. |
| [Locale API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/standard-apis/locale-api) | Retrieve the merchant's locale and localization settings for internationalization. |
| [Product Search API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/standard-apis/product-search-api) | Search the merchant's product catalog and retrieve product details, variants, and inventory data. |
| [Session API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/standard-apis/session-api) | Access session information and generate fresh authentication tokens for secure backend API requests. |
| [Toast API](https://shopify.dev/docs/api/pos-ui-extensions/2025-10/target-apis/standard-apis/toast-api) | Display toast notifications to provide feedback and information to users. |

***

