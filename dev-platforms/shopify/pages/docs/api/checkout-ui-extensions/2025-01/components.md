---
title: "**UI components**"
source: https://shopify.dev/docs/api/checkout-ui-extensions/2025-01/components.md
path: docs/api/checkout-ui-extensions/2025-01/components
---

---
title: Web components
description: >-
  Web components are the UI building blocks that you use to display data and
  trigger API functions. These components are native UI elements that follow
  Shopify's design system and render optimized interfaces for workflows in
  checkout.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components'
  md: 'https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components.md'
api_name: checkout-ui-extensions
---

# Web components

Web components are the UI building blocks that you use to display data and trigger API functions. These components are native UI elements that follow [Shopify's design system](https://shopify.dev/docs/api/polaris/using-polaris-web-components) and render optimized interfaces for workflows in [checkout](https://shopify.dev/docs/apps/build/checkout).

Your [target](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/targets) determines which components you can use because different locations in checkout have different interface requirements and constraints.

**Constraints:**

You can't override the CSS for UI components. The checkout UI will always render the merchant's own branding. Checkout UI extensions don't have access to the real checkout DOM and can't render arbitrary HTML. They can only render custom HTML elements provided by Shopify.

***

## Upgrading your extension

The latest version of checkout UI extensions adds new components and target APIs, and updates how extensions read and write metafields. Check out the [migration guide](https://shopify.dev/docs/apps/build/checkout/migrate-to-web-components) for the steps to upgrade your extension.

## Actions

Actions enable users to perform tasks and navigate through the checkout interface with interactive elements like buttons and links.

[![Button](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/button-thumbnail-BfZnAuEe.png)![Button](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/button-thumbnail-BfZnAuEe.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/button)

[Button](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/button)

[Trigger actions or events, such as submitting forms, opening dialogs, or navigating to other pages.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/button)

[![Clickable](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clickable-thumbnail-BRMP8BHA.png)![Clickable](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clickable-thumbnail-BRMP8BHA.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable)

[Clickable](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable)

[Wrap content to make it interactive when you need more styling control than Button or Link provide.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable)

[![Clickable chip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clickable-chip-thumbnail-Ba_IS1uS.png)![Clickable chip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clickable-chip-thumbnail-Ba_IS1uS.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable-chip)

[Clickable chip](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable-chip)

[Display interactive labels or categories that users can click or remove.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clickable-chip)

[![Clipboard item](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clipboard-default-CwDHUGWQ.png)![Clipboard item](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/clipboard-default-CwDHUGWQ.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clipboard-item)

[Clipboard item](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clipboard-item)

[Copy text or data to the clipboard when activated.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/clipboard-item)

[![Link](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/link-thumbnail-BaRvZ9N2.png)![Link](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/link-thumbnail-BaRvZ9N2.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/link)

[Link](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/link)

[Make text interactive, allowing users to navigate to other pages or perform specific actions.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/link)

[![Press button](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/press-button-thumbnail-BsATZaAo.png)![Press button](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/press-button-thumbnail-BsATZaAo.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/press-button)

[Press button](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/press-button)

[Enable users to toggle between active and inactive states to represent a persistent on/off or selected/unselected status.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/actions/press-button)

## Feedback and status indicators

Feedback and status indicators communicate system states, progress, and important information to users.

[![Announcement](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/announcement-thumbnail-DARYr6K-.png)![Announcement](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/announcement-thumbnail-DARYr6K-.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/announcement)

[Announcement](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/announcement)

[Provide a less disruptive alternative to modals for capturing user attention.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/announcement)

[![Badge](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/badge-thumbnail-CY6oU4DH.png)![Badge](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/badge-thumbnail-CY6oU4DH.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/badge)

[Badge](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/badge)

[Display status information or indicate completed actions through compact visual indicators.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/badge)

[![Banner](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/banner-thumbnail-CGI0HHQn.png)![Banner](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/banner-thumbnail-CGI0HHQn.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/banner)

[Banner](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/banner)

[Highlight important information or required actions prominently within the interface.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/banner)

[![Progress](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/progress-thumbnail-B43fiJD9.png)![Progress](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/progress-thumbnail-B43fiJD9.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/progress)

[Progress](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/progress)

[Visually represent the completion of a task or process.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/progress)

[![Spinner](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/spinner-thumbnail-BDWF5bu8.png)![Spinner](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/spinner-thumbnail-BDWF5bu8.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/spinner)

[Spinner](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/spinner)

[Display an animated indicator to show that content or actions are loading.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/feedback-and-status-indicators/spinner)

## Forms

Forms capture and validate user input with specialized field types optimized for different data collection needs in checkout.

[![Checkbox](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/checkbox-thumbnail-Dc8KbyEv.png)![Checkbox](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/checkbox-thumbnail-Dc8KbyEv.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/checkbox)

[Checkbox](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/checkbox)

[Enable users to make selections, such as agreeing to terms, enabling settings, or choosing multiple items from a list.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/checkbox)

[![Choice list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/choice-list-thumbnail-AaBvYPik.png)![Choice list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/choice-list-thumbnail-AaBvYPik.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/choice-list)

[Choice list](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/choice-list)

[Present multiple options for single or multiple selections.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/choice-list)

[![Consent checkbox](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/consent-checkbox-thumbnail-Bobrtc7r.png)![Consent checkbox](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/consent-checkbox-thumbnail-Bobrtc7r.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-checkbox)

[Consent checkbox](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-checkbox)

[Collect the buyer's approval for a given policy.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-checkbox)

[![Consent phone field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/consent-phone-field-thumbnail-ixRPV86k.png)![Consent phone field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/consent-phone-field-thumbnail-ixRPV86k.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-phone-field)

[Consent phone field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-phone-field)

[Capture phone numbers for text message marketing sign-up, with the value automatically saved during checkout.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/consent-phone-field)

[![Date field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/date-field-thumbnail-T6C2Li4o.png)![Date field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/date-field-thumbnail-T6C2Li4o.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-field)

[Date field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-field)

[Capture date input with a consistent interface for date selection and proper validation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-field)

[![Date picker](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/date-picker-thumbnail-BqAvVsRh.png)![Date picker](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/date-picker-thumbnail-BqAvVsRh.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-picker)

[Date picker](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-picker)

[Enable merchants to select dates using a calendar interface.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/date-picker)

[![Drop zone](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/drop-zone-thumbnail-DaIYV0G2.png)![Drop zone](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/drop-zone-thumbnail-DaIYV0G2.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/drop-zone)

[Drop zone](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/drop-zone)

[Accept file uploads through drag-and-drop or button activation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/drop-zone)

[![Email field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/email-field-thumbnail-D010x2qt.png)![Email field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/email-field-thumbnail-D010x2qt.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/email-field)

[Email field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/email-field)

[Capture email address input.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/email-field)

[![Form](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/admin/components/form-B0kMehyX.png)![Form](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/admin/components/form-B0kMehyX.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/form)

[Form](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/form)

[Wrap form controls and enable implicit submission when users press Enter.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/form)

[![Money field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/money-field-thumbnail-Bb8GnkaJ.png)![Money field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/money-field-thumbnail-Bb8GnkaJ.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/money-field)

[Money field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/money-field)

[Capture monetary values with built-in currency formatting and validation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/money-field)

[![Number field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/number-field-thumbnail-CYoZRuz8.png)![Number field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/number-field-thumbnail-CYoZRuz8.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/number-field)

[Number field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/number-field)

[Capture numeric input with built-in validation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/number-field)

[![Password field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/password-field-thumbnail-CNB0zR71.png)![Password field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/password-field-thumbnail-CNB0zR71.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/password-field)

[Password field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/password-field)

[Securely capture sensitive information.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/password-field)

[![Phone field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/phone-field-thumbnail-DIk-2zce.png)![Phone field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/phone-field-thumbnail-DIk-2zce.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/phone-field)

[Phone field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/phone-field)

[Capture phone number input with built-in formatting and validation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/phone-field)

[![Select](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/select-thumbnail-C6qegx_e.png)![Select](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/select-thumbnail-C6qegx_e.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/select)

[Select](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/select)

[Enable users to pick one option from a dropdown menu.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/select)

[![Switch](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/switch-thumbnail-Bp1WEwrj.png)![Switch](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/switch-thumbnail-Bp1WEwrj.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/switch)

[Switch](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/switch)

[Toggle options on or off.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/switch)

[![Text area](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-area-thumbnail-C05TfnLG.png)![Text area](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-area-thumbnail-C05TfnLG.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-area)

[Text area](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-area)

[Capture longer text content with a multi-line, resizable text input area.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-area)

[![Text field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-field-thumbnail-DU_Zc72d.png)![Text field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-field-thumbnail-DU_Zc72d.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-field)

[Text field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-field)

[Capture single-line text input.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/text-field)

[![URL field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/url-field-thumbnail-D-kdH9F9.png)![URL field](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/url-field-thumbnail-D-kdH9F9.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/url-field)

[URL field](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/url-field)

[Capture URLs with built-in formatting and validation.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/forms/url-field)

## Layout and structure

Layout and structure components organize content hierarchically and spatially, creating clear visual relationships in checkout interfaces.

[![Box](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/box-thumbnail-ccy-RH7a.png)![Box](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/box-thumbnail-ccy-RH7a.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/box)

[Box](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/box)

[Provide a generic, flexible container for custom designs and layouts.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/box)

[![Divider](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/divider-thumbnail-BRYBrdo5.png)![Divider](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/divider-thumbnail-BRYBrdo5.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/divider)

[Divider](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/divider)

[Create visual separation between content sections.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/divider)

[![Grid](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/grid-thumbnail-CG_HRlB3.png)![Grid](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/grid-thumbnail-CG_HRlB3.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/grid)

[Grid](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/grid)

[Organize content in a matrix of rows and columns to build responsive layouts.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/grid)

[![Query container](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/admin/components/page-ZjQ0PRv6.png)![Query container](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/admin/components/page-ZjQ0PRv6.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/query-container)

[Query container](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/query-container)

[Establish a container query context so child components can adapt based on the container's size rather than viewport width.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/query-container)

[![Scroll box](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/scroll-box-thumbnail-11IGxt0S.png)![Scroll box](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/scroll-box-thumbnail-11IGxt0S.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/scroll-box)

[Scroll box](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/scroll-box)

[Create a scrollable container for overflowing content.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/scroll-box)

[![Section](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/section-thumbnail-BPccSm6Y.png)![Section](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/section-thumbnail-BPccSm6Y.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/section)

[Section](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/section)

[Group related content into clearly-defined thematic areas.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/section)

[![Stack](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/stack-thumbnail-CGHqNUgm.png)![Stack](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/stack-thumbnail-CGHqNUgm.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/stack)

[Stack](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/stack)

[Organize elements horizontally or vertically along the block or inline axis.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/layout-and-structure/stack)

## Media and visuals

Media and visuals display images, icons, and graphical elements that enhance comprehension and visual communication in checkout.

[![Icon](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/icon-thumbnail-BVg7ao9W.png)![Icon](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/icon-thumbnail-BVg7ao9W.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/icon)

[Icon](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/icon)

[Display standardized visual symbols to represent actions, statuses, or categories consistently.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/icon)

[![Image](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/image-thumbnail-6cA3jBoq.png)![Image](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/image-thumbnail-6cA3jBoq.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/image)

[Image](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/image)

[Embed images within the interface with control over presentation and loading behavior.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/image)

[![Map](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/map-thumbnail-BGau5KHO.png)![Map](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/map-thumbnail-BGau5KHO.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/map)

[Map](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/map)

[Display an interactive map with location markers.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/map)

[![Payment icon](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/payment-icon-thumbnail-BnrdgC3i.png)![Payment icon](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/payment-icon-thumbnail-BnrdgC3i.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/payment-icon)

[Payment icon](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/payment-icon)

[Display standardized icons for payment methods.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/payment-icon)

[![Product thumbnail](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/product-thumbnail-thumbnail-CmnlDrNe.png)![Product thumbnail](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/product-thumbnail-thumbnail-CmnlDrNe.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/product-thumbnail)

[Product thumbnail](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/product-thumbnail)

[Display small preview images representing products.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/product-thumbnail)

[![QR code](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/qr-code-thumbnail-DNJ5WgA-.png)![QR code](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/qr-code-thumbnail-DNJ5WgA-.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/qr-code)

[QR code](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/qr-code)

[Generate and display QR codes for sharing links or data.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/media-and-visuals/qr-code)

## Overlays

Overlays present content in floating or layered surfaces that appear above the main interface, useful for focused tasks, contextual information, and supplementary content.

[![Modal](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/modal-thumbnail-D5PNMNOH.png)![Modal](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/modal-thumbnail-D5PNMNOH.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/modal)

[Modal](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/modal)

[Display content in a focused layer for tasks such as confirmation dialogs or settings panels.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/modal)

[![Popover](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/popover-thumbnail-BxvF9pDV.png)![Popover](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/popover-thumbnail-BxvF9pDV.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/popover)

[Popover](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/popover)

[Display contextual content in a floating container anchored to a trigger element.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/popover)

[![Sheet](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/sheet-thumbnail-B5PxIfKq.png)![Sheet](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/sheet-thumbnail-B5PxIfKq.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/sheet)

[Sheet](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/sheet)

[Display essential information at the bottom of the screen, appearing above other elements.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/sheet)

[![Tooltip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/tooltip-thumbnail-kSuIvUCJ.png)![Tooltip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/tooltip-thumbnail-kSuIvUCJ.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/tooltip)

[Tooltip](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/tooltip)

[Display additional information on hover or focus.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/overlays/tooltip)

## Typography and content

Typography and content components present textual information with appropriate hierarchy, emphasis, and styling for clear communication.

[![Abbreviation](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/abbreviation-thumbnail-BiXI2eyD.png)![Abbreviation](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/abbreviation-thumbnail-BiXI2eyD.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/abbreviation)

[Abbreviation](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/abbreviation)

[Display abbreviated text with a tooltip showing the full term on hover.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/abbreviation)

[![Chip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/chip-thumbnail-Dm3qc2FJ.png)![Chip](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/chip-thumbnail-Dm3qc2FJ.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/chip)

[Chip](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/chip)

[Display static labels, categories, or attributes that help classify and organize content.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/chip)

[![Details](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/details-thumbnail-ottKwVSH.png)![Details](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/details-thumbnail-ottKwVSH.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/details)

[Details](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/details)

[Display a collapsible section that users can expand to reveal additional content.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/details)

[![Heading](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/heading-thumbnail-kUJ6RcQy.png)![Heading](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/heading-thumbnail-kUJ6RcQy.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/heading)

[Heading](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/heading)

[Render hierarchical titles to communicate the structure and organization of page content.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/heading)

[![Ordered list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/ordered-list-thumbnail-C8dDO3g2.png)![Ordered list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/ordered-list-thumbnail-C8dDO3g2.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/ordered-list)

[Ordered list](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/ordered-list)

[Display a numbered list of items.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/ordered-list)

[![Paragraph](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/paragraph-thumbnail-DljjYJmu.png)![Paragraph](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/paragraph-thumbnail-DljjYJmu.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/paragraph)

[Paragraph](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/paragraph)

[Display blocks of text that can contain inline elements such as buttons, links, or emphasized text.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/paragraph)

[![Skeleton paragraph](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/skeleton-paragraph-thumbnail-C_eH5TVX.png)![Skeleton paragraph](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/skeleton-paragraph-thumbnail-C_eH5TVX.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/skeleton-paragraph)

[Skeleton paragraph](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/skeleton-paragraph)

[Display a placeholder for paragraph content while data is loading.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/skeleton-paragraph)

[![Text](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-thumbnail-Cn8TJc8F.png)![Text](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/text-thumbnail-Cn8TJc8F.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/text)

[Text](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/text)

[Display text with specific visual styles or tones.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/text)

[![Time](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/time-thumbnail-BInsRCaK.png)![Time](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/time-thumbnail-BInsRCaK.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/time)

[Time](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/time)

[Display dates and times in a localized format.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/time)

[![Unordered list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/unordered-list-thumbnail-CRa9rsI1.png)![Unordered list](https://cdn.shopify.com/shopifycloud/shopify-dev/development/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-10/unordered-list-thumbnail-CRa9rsI1.png)](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/unordered-list)

[Unordered list](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/unordered-list)

[Display a bulleted list of items.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/web-components/typography-and-content/unordered-list)

***

