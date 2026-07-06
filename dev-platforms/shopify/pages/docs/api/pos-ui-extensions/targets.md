---
title: "**Extension targets**"
source: https://shopify.dev/docs/api/pos-ui-extensions/targets.md
path: docs/api/pos-ui-extensions/targets
---

---
title: Targets
description: >-
  Targets define where your POS UI extensions appear within Shopify's Point of
  Sale interface and what capabilities they receive. Targets serve specific
  purposes — some render persistent UI elements within existing screens, others
  provide interactive menu items or buttons, and some launch full-screen modal
  experiences for complex workflows.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/pos-ui-extensions/latest/targets'
  md: 'https://shopify.dev/docs/api/pos-ui-extensions/latest/targets.md'
api_name: pos-ui-extensions
---

# Targets

Targets define where your POS UI extensions appear within [Shopify's Point of Sale interface](https://shopify.dev/docs/apps/build/pos) and what capabilities they receive.

Targets serve specific purposes: some render persistent UI elements within existing screens, others provide interactive menu items or buttons, and some launch full-screen modal experiences for complex workflows.

Use this reference to explore all available targets and understand where they appear in the POS interface.

![POS tablet interface showing multiple extension target locations across different screens in the Point of Sale app.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/targets-overview-hero-EQ3LjmEr.png)

***

## Cart details

The cart details screen appears when customers select items in a transaction to modify quantities, apply discounts, or access item-specific tools. This screen provides control over individual products during transaction building.

**Use cases**: Item-specific customizations, cart monitoring, or product configuration tools that improve line item management.

[View cart details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/cart-details)

##### Cart details action (menu item)

`pos.cart.line-item-details.action.menu-item.render`

An action target that displays as a menu item on the cart line item details screen.

##### Cart details action (modal)

`pos.cart.line-item-details.action.render`

An action target that displays as a modal when a cart line item action menu item is tapped.

![POS cart screen showing product line items with the extension target slot highlighted as a menu item option on the right side.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/cart-details-menu-item-render-jLl5EgM3.png)

![POS cart screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/cart-details-modal-render-BFkDZDZj.png)

***

## Customer details

The customer details screen appears when merchants look up a customer during checkout or need to access customer history and profile information. This screen serves as the hub for customer management within POS, displaying customer data, purchase history, and contact details.

**Use cases**: Customer service capabilities, loyalty program integration, or tools for customer engagement and support during transactions.

[View customer details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/customer-details)

##### Customer details block

`pos.customer-details.block.render`

A block target that displays inline content within the customer details screen.

##### Customer details action (menu item)

`pos.customer-details.action.menu-item.render`

An action target that displays as a menu item on the customer details screen action menu.

##### Customer details action (modal)

`pos.customer-details.action.render`

An action target that displays as a modal when a customer details action menu item is tapped.

![POS customer profile screen showing customer information and order history, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/customer-details-block-render-DAsZIa2K.png)

![POS customer profile screen with the extension target slot highlighted as a menu action item on the right side.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/customer-details-menu-item-render-C5M6Rq_U.png)

![POS customer details screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/customer-details-modal-render-DRjcbJbh.png)

***

## Draft order details

The draft order details screen appears when merchants access saved orders, quotes, or incomplete transactions that need to be finalized later. This screen displays draft order information, customer details, and line items for sales that haven't been completed.

**Use cases**: Quote management, approval workflows, or integration with external systems for draft order processing and completion.

[View draft order details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/draft-order-details)

##### Draft order details block

`pos.draft-order-details.block.render`

A block target that displays inline content within the draft order details screen.

##### Draft order details action (menu item)

`pos.draft-order-details.action.menu-item.render`

An action target that displays as a menu item on the draft order details screen action menu.

##### Draft order details action (modal)

`pos.draft-order-details.action.render`

An action target that displays as a modal when a draft order details action menu item is tapped.

![POS draft order screen showing order details and line items, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/draft-order-block-render-BY_i0_jR.png)

![POS draft order screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/draft-order-menu-item-render-TUZMJLb3.png)

![POS draft order screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/draft-order-modal-render-BAswaBFY.png)

***

## Home screen (smart grid)

The smart grid is the first screen merchants see when they open [the POS app](https://apps.shopify.com/shopify-pos). It provides quick access to essential functions and serves as the starting point for merchant activities.

**Use cases**: High-frequency actions, status displays, or entry points to workflows that merchants need daily.

[View home screen targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/home-screen)

##### Home screen tile

`pos.home.tile.render`

A tile target that displays as a clickable tile on the POS home screen smart grid.

##### Home screen action (modal)

`pos.home.modal.render`

An action target that displays as a full-screen modal when a home screen tile is tapped.

![POS home screen smart grid showing app tiles, with the extension target slot displayed as a clickable tile in the grid.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/home-tile-render-BLpqYBnr.png)

![POS home screen with a full-screen modal overlay open after tapping a tile, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/home-modal-render-CENBsTmv.png)

***

## Order details

The order details screen appears when merchants access a completed transaction for customer service, refunds, or order fulfillment tasks. This screen displays transaction information including customer details, payment data, line items, and fulfillment status for completed sales.

**Use cases**: Order management, fulfillment tools, or integration with external systems for post-sale processing and customer support.

[View order details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/order-details)

##### Order details block

`pos.order-details.block.render`

A block target that displays inline content within the order details screen.

##### Order details action (menu item)

`pos.order-details.action.menu-item.render`

An action target that displays as a menu item on the order details screen action menu.

##### Order details action (modal)

`pos.order-details.action.render`

An action target that displays as a modal when an order details action menu item is tapped.

![POS order details screen showing transaction and fulfillment information, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/order-details-block-render-D9oKyw0e.png)

![POS order details screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/order-details-menu-item-render-BYfP_PnY.png)

![POS order details screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/order-details-modal-render-CQOvyY2S.png)

***

## Post-exchange

The post-exchange screen appears after merchants complete an exchange transaction. This screen displays the exchange summary including exchanged items, price adjustments, and exchange details, providing opportunities for customer service and follow-up actions.

**Use cases**: Exchange management, inventory tracking tools, or customer service features for product exchanges.

**Beta:**

Post-exchange targets are part of the POS UI extensions [feature preview](https://shopify.dev/docs/api/feature-previews). This feature preview is invite-only and requires POS UI extensions version 2025-07 or higher and POS app version 9.31.0 or later.

[View post-exchange targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/post-exchange)

##### Post-exchange block

`pos.exchange.post.block.render`

A block target that displays inline content within the post-exchange screen.

##### Post-exchange action (menu item)

`pos.exchange.post.action.menu-item.render`

An action target that displays as a menu item on the post-exchange screen action menu.

##### Post-exchange action (modal)

`pos.exchange.post.action.render`

An action target that displays as a modal when a post-exchange action menu item is tapped.

![POS post-exchange summary screen showing exchanged items and price adjustments, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-exchange-block-render-AhLKmMp4.png)

![POS post-exchange screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-exchange-menu-item-render-DIuxCL-j.png)

![POS post-exchange screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-exchange-modal-render-CHyT0RzR.png)

***

## Post-purchase

The post-purchase screen appears after merchants complete a sale, return, or exchange transaction. This screen displays the transaction summary and provides opportunities for follow-up actions, customer service, and revenue generation.

**Use cases**: Capturing additional information, customer service tools, or related transactions that improve the post-sale customer experience.

[View post-purchase targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/post-purchase)

##### Post-purchase block

`pos.purchase.post.block.render`

A block target that displays inline content within the post-purchase screen.

##### Post-purchase action (menu item)

`pos.purchase.post.action.menu-item.render`

An action target that displays as a menu item on the post-purchase screen action menu.

##### Post-purchase action (modal)

`pos.purchase.post.action.render`

An action target that displays as a modal when a post-purchase action menu item is tapped.

![POS post-purchase summary screen showing transaction details, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-purchase-block-render-D0D8LK0O.png)

![POS post-purchase screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-purchase-menu-item-render-x40yByUf.png)

![POS post-purchase screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-purchase-modal-render-DVbNAzop.png)

***

## Post-return

The post-return screen appears after merchants complete a return transaction. This screen displays the return summary including returned items, refund amounts, and return reason, providing opportunities for customer service and follow-up actions.

**Use cases**: Return-specific tools, refund processing, or customer service features for return workflows.

**Beta:**

Post-return targets are part of the POS UI extensions [feature preview](https://shopify.dev/docs/api/feature-previews). This feature preview is invite-only and requires POS UI extensions version 2025-07 or higher and POS app version 9.31.0 or later.

[View post-return targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/post-return)

##### Post-return block

`pos.return.post.block.render`

A block target that displays inline content within the post-return screen.

##### Post-return action (menu item)

`pos.return.post.action.menu-item.render`

An action target that displays as a menu item on the post-return screen action menu.

##### Post-return action (modal)

`pos.return.post.action.render`

An action target that displays as a modal when a post-return action menu item is tapped.

![POS post-return summary screen showing returned items and refund amounts, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-return-block-render-BakoLmTj.png)

![POS post-return screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-return-menu-item-render-ZuqUt75Z.png)

![POS post-return screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/post-return-modal-render-DzlpPDUg.png)

***

## Product details

The product details screen appears when merchants search for a product, scan a barcode, or browse inventory during a transaction. This screen displays product information including pricing, inventory levels, variants, and product specifications that merchants need to serve customers.

**Use cases**: Product understanding, additional product data, or product-specific tools that help merchants make informed decisions during transaction building.

[View product details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/product-details)

##### Product details block

`pos.product-details.block.render`

A block target that displays inline content within the product details screen.

##### Product details action (menu item)

`pos.product-details.action.menu-item.render`

An action target that displays as a menu item on the product details screen action menu.

##### Product details action (modal)

`pos.product-details.action.render`

An action target that displays as a modal when a product details action menu item is tapped.

![POS product details screen showing pricing and inventory information, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/product-details-block-render-BGkLbrh5.png)

![POS product details screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/product-details-menu-item-render-CtCQMWN2.png)

![POS product details screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/product-details-modal-render-zOdzHi1W.png)

***

## Register details

The register details screen displays information about the current register and cash drawer status. This screen provides access to cash management operations and register-specific tools for retail staff.

**Use cases**: Cash drawer operations, cash management workflows, register verification tools, or compliance features for cash handling and register operations.

[View register details targets →](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets/register-details)

##### Register details block

`pos.register-details.block.render`

A block target that displays inline content within the register details screen.

##### Register details action (menu item)

`pos.register-details.action.menu-item.render`

An action target that displays as a menu item on the register details screen action menu.

##### Register details action (modal)

`pos.register-details.action.render`

An action target that displays as a modal when a register details action menu item is tapped.

![POS register details screen showing cash drawer status, with the extension target slot displayed as an inline block.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/register-block-render-DmQRvcV-.png)

![POS register details screen with the extension target slot highlighted as a menu action item.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/register-menu-item-render-B2QI3bBx.png)

![POS register details screen with a full-screen modal overlay open, showing the extension target slot inside the modal.](https://shopify.dev/assets/assets/images/api/pos-ui-extensions/targets-overview-images/register-modal-render-DcWdupxp.png)

***

