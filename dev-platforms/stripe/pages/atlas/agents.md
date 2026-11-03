---
title: "Prepare an Atlas application with an agent or CLI"
source: https://docs.stripe.com/atlas/agents.md
path: atlas/agents
---

# Prepare an Atlas application with an agent or CLI

Use Stripe MCP or the Stripe CLI to prepare your company incorporation application.

Use an AI assistant or the Stripe CLI to prepare a Stripe Atlas application for a Delaware C corporation or limited liability company (LLC). You can enter company and founder information, check application requirements, and save progress.

> #### Finish in the Dashboard
> 
> Finish in the Stripe Dashboard to review documents, pay, sign, and submit your application. If applicable, provide personal tax identifiers, such as an SSN or ITIN, in the Dashboard. Preparing or validating a draft through an agent or the CLI doesn’t submit it or form your company.

## Before you begin

Before preparing your application, complete these requirements:

- Review [what you need to incorporate with Atlas](https://docs.stripe.com/atlas/signup.md).
- Choose a [company type](https://docs.stripe.com/atlas/company-types.md) and, when applicable, [founder equity terms](https://docs.stripe.com/atlas/equity-terms.md).
- For an AI assistant, connect to [Stripe MCP and authenticate with OAuth](https://docs.stripe.com/mcp.md#authentication).
- For the command line, install the latest [Stripe CLI](https://docs.stripe.com/cli.md) and authenticate with `stripe login`.

You make the company-type, ownership, vesting, legal, and tax decisions. Your assistant can explain the process and enter your choices. Atlas doesn’t provide legal or tax advice.

## Use an AI assistant 

The `atlas_company_formation` MCP tool lists, creates, retrieves, and advances draft applications. Ask your assistant:

> Help me prepare a Stripe Atlas application for a new company.

Use this procedure with your assistant:

1. Check for an existing application before creating one. If you have a draft, [resume it](https://docs.stripe.com/atlas/agents.md#resume-an-application).
2. Confirm that you want to create an application before your assistant creates one.
3. Provide the requested company and founder information. This can include home addresses and, depending on your client, dates of birth. Review and confirm proposed changes before saving them.
4. Ask your assistant to validate the draft, explain missing information or errors, and help you correct them.
5. Follow the returned Dashboard link to finish your application.

If creation returns an ambiguous error, ask your assistant to list and retrieve applications before retrying. Another create request starts another application.

## Use the Stripe CLI 

The [tools plugin](https://docs.stripe.com/cli/tools) uses your selected Stripe CLI account. Each operation is an individual command that returns data and guidance.

Install the plugin, find Atlas operations, and inspect the creation command:

```bash
stripe plugin install tools
stripe tools search atlas
stripe tools create_atlas_application --help
```

If you already have an application, [resume it](https://docs.stripe.com/atlas/agents.md#resume-an-application) instead of creating another. To create an application, run:

```bash
stripe tools create_atlas_application
```

Creation returns an `atlas_account` ID for the new application account. To continue:

1. Save the `atlas_account` ID.
2. Follow the returned next-operation guidance, starting with retrieving the application. Inspect each operation’s `--help` before supplying company or founder information. Review the information before saving it.
3. Validate the draft and correct missing information or errors using the returned guidance.
4. Follow the returned Dashboard link to finish your application.

## Resume an application 

Authorize the Stripe account associated with your existing application to retrieve saved progress. You don’t need to create another application.

For an AI assistant, ask it to find your existing application and authorize its account with **Atlas Company Formation** write access if needed. Then ask:

> Resume my existing Stripe Atlas application. Show me what’s saved and what I need to provide next. Ask me to confirm changes before saving them.

For the Stripe CLI, run `stripe reauth` if the application’s account isn’t already authorized in your current session. If your session has expired or been revoked, use `stripe login` instead. Use `stripe switch` to select the application’s live-mode context, then retrieve your saved progress:

```bash
stripe tools retrieve_atlas_formation
```

You can also continue your application in the Dashboard. After submission, use the Dashboard to track status and access documents.

