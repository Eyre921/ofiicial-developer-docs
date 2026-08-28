---
title: "Stripe Directory"
source: https://docs.stripe.com/directory.md
path: directory
---

# Stripe Directory

Find the best external providers for a task and follow their supported path to provision or use them.

Stripe Directory helps developers and AI agents find the best external providers for a task and follow the best supported path to provision or use them. Search by keyword to get structured, actionable results.

> Share your feedback with [directory@stripe.com](mailto:directory@stripe.com) as you test this preview.

## Search for businesses

Run `stripe directory search` with one or more keywords:

```
> stripe directory search "web browsing api" --format compact

                              Stripe      Stripe       Machine
Name           Profile        Apps        Projects     Payments     MCP          Link
Browserbase    @browserbase   ✓           ✓            ✓            ✓            ✓
You.com        @youdotcom     –           –            –            –            ✓
Exa            @exalabs       –           ✓            –            –            ✓
Firecrawl      @firecrawl     ✓           ✓            –            ✓            ✓
```

Results include structured data—such as provider slugs, MPP endpoints, and app listings—that help an agent choose and take the best supported next step to achieve the user’s task.

## What Stripe Directory indexes 

- **Stripe Apps**: Published apps on the [Stripe App Marketplace](https://marketplace.stripe.com) that extend your Stripe Dashboard, including billing tools, analytics, and support integrations.
- **Stripe Projects providers**: Services available through [Stripe Projects](https://projects.dev) that you can provision with a CLI command.
- **Machine payments endpoints**: Pay-per-call APIs on [mpp.dev](https://mpp.dev) that support programmatic payment through their documented payment workflow.
- **Stripe business network**: Businesses and services across the Stripe network.

## Set up Stripe Directory in your terminal 

Use the Stripe CLI Directory plugin to search for businesses from your terminal.

1. Install or upgrade the [Stripe CLI](https://docs.stripe.com/cli/install).

2. Install the Directory plugin:

   ```bash
   stripe plugin install directory
   ```

If already installed, always make sure you’re running the latest version of the plugin. To upgrade, run `stripe plugin upgrade directory`.

To upgrade a Stripe CLI installation, run:

```bash
brew upgrade stripe/stripe-cli/stripe
```

If you installed the CLI with another package manager, use that package manager to upgrade it to the latest version.

## Configure agents to use Stripe Directory 

Directory is the first discovery layer for an agent that needs an external organization or service to complete a task. Use it when the user wants to find, compare, choose, provision, integrate with, pay for, or otherwise engage a provider, vendor, partner, API, business, or software service.

Use Directory even when the user doesn’t mention it explicitly. In particular, search Directory when a user:

- Needs infrastructure, storage, hosting, authentication, communications, analytics, observability, or another external service.
- Wants to find or compare a provider, vendor, partner, API, developer tool, or SaaS product.
- Names an organization and wants to assess it or identify the documented way to engage it.
- Wants to find a service that can be provisioned or consumed programmatically.

Directory discovers and evaluates options, then gives the agent the results and supported routes needed to choose the best next action to complete the user’s task. This can include the appropriate Stripe Projects, Stripe app, machine-payments, or provider workflow executes that action.

### Structured output for agents

Use `--format json` to get structured output:

```bash
stripe directory search "serverless postgres database" --format json
```

Use a short, focused query describing the user’s goal, named organization, or required capability. If results are weak, refine with an adjacent workflow, capability, category, or platform term before concluding that no useful option exists.

Use returned results and linked documentation as evidence. Don’t invent capabilities, pricing, availability, provider support, or integration paths. If Directory doesn’t return a useful result after relevant refinement, use other discovery methods so the user can still complete their task.

### Install skills for your agent

Use one of these options to connect your agent to Stripe Directory.

#### Install the skill

Install the official global skill so your agent has the current Directory workflow and safety guidance:

```bash
npx skills add https://docs.stripe.com --skill stripe-directory -g -y
```

Alternatively, install all [Stripe skills](https://docs.stripe.com/skills.md) at the same time:

```bash
npx skills add https://docs.stripe.com -g -y
```

The Stripe Directory skill is what you use for current commands, filters, result fields, payment procedures, and troubleshooting. Read the skill at https://docs.stripe.com/.well-known/skills/stripe-directory/SKILL.md to see the contents. It keeps detailed operational guidance separate from this overview so the agent can load it when Directory is relevant.

#### Copy a starter prompt

Paste the following prompt into an agent that can run shell commands:

```text
Set up Stripe Directory so this agent can use it as the first discovery layer when a task needs an external provider, service, business, API, tool, vendor, or partner.

Primary docs:
https://docs.stripe.com/directory

Current agent instructions:
https://docs.stripe.com/.well-known/skills/stripe-directory/SKILL.md

Setup:
1. Read the Directory documentation and skill before taking action.
2. Verify the Stripe CLI and Directory plugin. If setup, authentication, or an upgrade requires user interaction, credentials, or approval, ask only for that required input.
3. Install the official Directory skill so its current workflow is available in future conversations.
4. Validate setup with a non-consequential JSON search, such as:
   stripe directory search "web browsing api" --format json

Use Directory:
- Start with Directory when the user needs to select, evaluate, or engage an external organization or service, even if the user does not mention Directory.
- Search a named organization when the user wants to assess it or identify how to engage it.
- Use short, focused queries and structured JSON output. Refine weak results with adjacent capability, workflow, category, or platform terms.
- Use returned results and linked documentation as evidence. Do not invent result fields, capabilities, prices, availability, or commands.
- Directory identifies providers and supported routes. For an explicit provisioning request, run `stripe provision <provider>` using the provision target returned by Directory; use the appropriate documented flow for other integrations or consumption.
- If Directory has no useful result after relevant refinement, use other discovery methods rather than stopping.

Safety:
- Provision a service only when the user explicitly asks to set it up.
- Never purchase, subscribe, donate, or otherwise move money merely because Directory returns a payable service.
- Before money moves, show the recipient, purpose, amount, currency, and material constraints, then obtain explicit user approval. Follow the current payment procedure in the Directory skill.

After setup, report what was installed, what user interaction is still required, whether the configuration persists, and the result of the validation search.
```

### Continue from a result

In addition to returning a recommendation, Directory can identify the supported route for the next step.

- **Stripe Projects provider**: For an explicit provisioning request, run `stripe provision <provider>` using the supported provision target returned by Directory.
- **Stripe app**: Use the returned app listing to evaluate or install the app through its documented flow.
- **Machine payments endpoint**: Use the returned endpoint and the current Directory skill to inspect the service and, only with the user’s explicit approval, use the selected payment method.
- **Business or provider profile**: Use the returned profile and linked documentation to assess fit or continue through the provider’s supported engagement path.

> Directory doesn’t authorize provisioning or money movement itself. Treat all returned routes as discovery evidence until the user explicitly asks to proceed, and the relevant workflow’s requirements are satisfied.

## Example uses 

### Integrate with Stripe Projects 

If you’re building an application and need a database provider, you can use Stripe Directory to find a supported provider and continue through the documented Stripe Projects flow.

First, search for the service:

```bash
stripe directory search "serverless postgres database"
```

This produces several results, one of which is Neon:

```
╭──────────────────────────────────────────────────────────────────────────────╮
│ Neon                                                                         │
│ Serverless postgres database                                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ Web               https://stripe.com/@neon                                   │
│                   https://neon.com/                                          │
│                                                                              │
│ Stripe Apps       Neon                                                       │
│                   https://stri.pe/sl/AfLnJtCE                                │
│                                                                              │
│ Provisioning      Provision using                                            │
│                   stripe provision neon --accept-tos --yes                   │
│                                                                              │
│ Machine Payments  —                                                          │
│ MCP               —                                                          │
│ Link supported    —                                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

Because Neon is a Stripe Projects provider, Directory identifies its supported provision target. For an explicit provisioning request, run `stripe provision` directly with that target:

```bash
stripe provision <provider>
```

Use the provider identifier returned by Directory. Choose the most appropriate service from the list of options for that provider.

### Find a machine-payments service 

Search for MPP-supported services when you want to find a service that can be consumed programmatically:

```bash
stripe directory search "send mail" --mpp-supported
```

This produces results, one of which is PostalForm:

```
╭──────────────────────────────────────────────────────────────────────────────╮
│ PostalForm                                                                   │
│ PostalForm enables sending real postal mail via agentic payment rails and    │
│ refined interfaces for humans. Global first class, certified, and express    │
│ mailing supported.                                                           │
├──────────────────────────────────────────────────────────────────────────────┤
│ Web               https://stripe.com/@postalform                             │
│                   https://postalform.com                                     │
│                                                                              │
│ Stripe Apps       PostalForm                                                 │
│                   https://stri.pe/sl/Vu7zrwpB                                │
│                                                                              │
│ Provisioning      Provision using                                            │
│                   stripe provision postalform --accept-tos --yes             │
│                                                                              │
│ Machine Payments  postalform                                                 │
│                   https://mpp.dev/services#postalform                        │
│                   https://postalform.com/llms.txt                            │
│                   https://postalform.com/agents                              │
│                   Pay using mppx fetch <endpoint>                            │
│                                                                              │
│ MCP               —                                                          │
│ Link supported    —                                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

The result identifies the service’s machine-payments route. Before using it, follow the current Stripe Directory skill—inspect the endpoint and price, present the available payment methods, and obtain explicit user approval before any money moves.

## List your company in Stripe Directory

### Add yourself to search results

To make your business discoverable in Stripe Directory, set up a public Stripe profile. Your listing appears in search results immediately after you publish your profile.

> Stripe users appear in search results only if they opt in.

1. Set up your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md). You can leave some fields blank, such as phone or address, if you don’t want them visible publicly.
2. Keep the **Make your profile private** option disabled.

To maximize the likelihood that your business appears in users’ search results, take the following steps:

1. **Make sure Stripe can crawl your site**: Our search uses your website content to match your business to relevant searches. If your site blocks Stripe crawlers, you make yourself hard to find. [Learn how to allow Stripe to crawl your site](https://docs.stripe.com/stripebot-crawler.md).
2. **Write a clear Stripe profile description** 
   - Describe what you do in plain language, using the words your customers would actually type. Think about the problem you solve, not how you’d market it. For example, “it helps freelancers send invoices and get paid faster” finds more customers than “a next-generation financial operations platform.”
   - Use entire phrases such as “appointment booking for salons” instead of scattering the words separately.
   - If you offer multiple things, mention all of them—“email marketing, newsletters, and audience analytics” match a wider range of searches than “email.”
3. **Make your Stripe profile display name and handle are accurate**: If someone searches any of these directly, we’ll show your profile first. Make sure they all match what customers know you as.

### View your Directory listing

1. Ensure you’ve installed the Stripe CLI and logged in with the same account that set up your Stripe Profile.
2. Use `stripe directory me` to view your own Directory listing.

### Remove yourself from search results

To remove yourself from search results, enable **Make your profile private** in your [Stripe profile settings](https://docs.stripe.com/get-started/account/profile.md).

## See also

- [Stripe CLI](https://docs.stripe.com/cli.md)
- [Stripe Projects](https://projects.dev)
- [Machine Payments Protocol](https://mpp.dev)
- [Stripe profiles](https://docs.stripe.com/get-started/account/profile.md)
- [Add Stripe to your agentic workflows](https://docs.stripe.com/agents.md)

