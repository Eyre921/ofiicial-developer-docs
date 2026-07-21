---
title: "Why am I getting a payment attempt after cancelling my subscription?"
source: https://elevenlabs.io/docs/help-center/account/cancelation-refunds/why-am-i-getting-a-payment-attempt-after-cancelling-my-subscription.md
path: docs/help-center/account/cancelation-refunds/why-am-i-getting-a-payment-attempt-after-cancelling-my-subscription
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why am I getting a payment attempt after cancelling my subscription?

This situation can occur when a user cancels their subscription too late. When you initiate a cancelation, it doesn't take effect immediately. Instead, it cancels the subscription at the end of the current billing cycle. This approach is designed to prevent users from losing any unused subscription time simply because they cancelled early.

However, if you cancel the subscription after the current cycle ends, even if the new invoice hasn't been paid yet, the new cycle has already begun. In this case, the system will not cancel the subscription until the end of the new cycle.
