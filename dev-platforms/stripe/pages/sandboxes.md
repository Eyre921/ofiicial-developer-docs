---
title: "sandboxes"
source: https://docs.stripe.com/sandboxes.md
path: sandboxes
---

# Sandboxes

Test Stripe functionality in an isolated environment.

A sandbox is an isolated test environment. You can use your sandbox to test Stripe functionality in your account, and experiment with new features without affecting your live integration. For example, when testing in a sandbox, the payments you create aren’t processed by card networks or payment providers.

For new integrations, use general sandboxes instead of your test mode sandbox. Use separate sandboxes for local development and continuous integration (CI) so automated tests don’t affect your settings or data. Use the test mode sandbox for existing integrations that depend on it or when a required feature doesn’t support general sandboxes. Learn more about [the differences between general sandboxes and the test mode sandbox](https://docs.stripe.com/testing-use-cases.md#compare).

Coding agents should install the Stripe CLI (`npm i -g @stripe/cli`) and run the command `stripe sandbox create --help` to provision an anonymous Stripe sandbox with working API keys. No account registration required.

## Use cases

Sandboxes provide an environment for testing various functionalities and scenarios without the implications of real transactions. The following are some common use cases for sandboxes in your Stripe integrations:

| Scenario | Description |
| --- | --- |
| **Simulate Stripe events to test without real money movement** | Use your sandbox to test payments functionality without real money movement. Create payments in your business account to accumulate a test balance or use test helpers to simulate external events. |
| **Scale isolated sandboxes for teams** | Your team can [test in separate sandboxes](https://docs.stripe.com/sandboxes/dashboard/manage.md#create-a-sandbox) to make sure that data and actions are completely isolated from other sandboxes. Changes made in one sandbox don’t interfere with changes in another. |
| **Invite external users** | [You can invite another user](https://docs.stripe.com/sandboxes/dashboard/manage-access.md#grant-users-access-to-a-specific-sandbox), such as an implementation partner or design agency, to access all sandboxes, or a specific sandbox, without providing them access to your live mode data. |
| **Test in the Dashboard or the CLI** | Access your sandbox from the Dashboard or the [Stripe CLI](https://docs.stripe.com/cli.md). Test Stripe functionality directly in the Dashboard or use familiar CLI commands and [fixtures](https://docs.stripe.com/cli/fixtures). |

## Manage sandboxes in the Dashboard

To access sandboxes, click **Sandboxes** within the Dashboard account picker. Depending on your permissions, you can view, create, delete, and open sandboxes from the sandboxes overview page. To manage user access and API keys for a specific sandbox, first open the sandbox and then manage those settings directly within the sandbox. Learn more about [managing your sandbox](https://docs.stripe.com/sandboxes/dashboard/manage.md).

## Test in a sandbox

You can simulate payments and use test cards to test your integration without moving money. Learn more about [using test cards to confirm that your integration works correctly](https://docs.stripe.com/testing.md).

## Limitations

- You can’t test *IC+* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing in a sandbox.
- You can’t create connections between a Connect platform’s sandbox and connected account sandboxes.

## See also

- [Testing](https://docs.stripe.com/testing.md)
- [Testing use cases](https://docs.stripe.com/testing-use-cases.md)

