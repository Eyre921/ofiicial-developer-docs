---
title: "Stripe Directory"
source: https://docs.stripe.com/directory.md
path: directory
---

# Stripe Directory

Find the best external providers for a task and follow their supported path to provision or use them.

Stripe Directory helps developers and AI agents find the best external providers for a task and follow the best supported path to provision or use them. Search by keyword phrases to get structured, actionable results.

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

Results include structured data—such as provider slugs, MPP endpoints, and app listings—that help you or your agent choose and take the best supported next step to achieve the goal.

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

## Use Stripe Directory with AI Agents 

Stripe Directory helps AI agents find and evaluate external providers, services, APIs, businesses, and integrations needed to complete a user’s task.

Use Directory when an agent needs to:

- Find, compare, choose, provision, integrate with, pay for, or otherwise engage a provider, vendor, partner, API, business, or software service.
- Set up or integrate an external service, such as infrastructure, storage, hosting, authentication, communications, analytics, or observability.
- Assess a named organization and identify its supported engagement path.
- Find a service that can be provisioned or consumed programmatically.

Directory discovers and evaluates options, then gives the agent structured results and supported routes needed to choose the best next action to complete the task. This can include the appropriate Stripe Projects, Stripe app, machine-payments, or provider workflow to execute that action.

### Structured output for agents

Agents can request JSON output when they need to read and act on Directory results programmatically:

```bash
stripe directory search "serverless postgres database" --format json
```

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

After installation, your agent can search the directory, interpret results, and use the returned endpoints without additional instruction.

#### Copy a starter prompt

Paste the following prompt into an agent that can run shell commands:

```text
Set up Stripe Directory so this agent can use it as the first discovery layer when a task needs an external provider, service, business, API, tool, vendor, or partner.

Primary docs:
https://docs.stripe.com/directory

Skill file:
https://docs.stripe.com/.well-known/skills/stripe-directory/SKILL.md

Tasks:
1. Read the Stripe Directory documentation and understand the intended workflow.
2. Install or verify the Stripe CLI and upgrade to the latest version.
3. Install or upgrade the Directory plugin:
    ◦ `stripe plugin install directory`
    ◦ If already installed: `stripe plugin upgrade directory`
4. Verify the installation by running:
    ◦ `stripe directory search "web browsing api" --format json`
   Confirm that structured results are returned successfully.
5. Install the official Stripe Directory skill:
    ◦ `npx skills add https://docs.stripe.com --skill stripe-directory -g -y`
6. If the skill installer is unavailable or fails, manually install the skill from:
    ◦ https://docs.stripe.com/.well-known/skills/stripe-directory/SKILL.md
7. Integrate the skill into this agent so it is available by default in future conversations.
8. Update the agent's persistent instructions or configuration so that the agent
automatically searches Stripe Directory first whenever a user asks to:
   ◦ find, compare, or choose an external business, provider, vendor, partner, API,
  software service, or developer tool
   ◦ set up, provision, integrate with, or consume an external service
   ◦ assess a named organization or identify the best way to engage it
   ◦ find a service to pay for, donate to, or use programmatically

Expected behavior:
• Use Stripe Directory as the first source for discovery.
• Execute:
    ◦ `stripe directory search "<user query>" --format json`
• Rank the best results for the user's requirements.
• Include pricing, capabilities, integration methods, supported endpoints, and other useful metadata when available.
• Follow any additional discovery or inspection commands recommended by the Directory documentation.
• If Stripe Directory doesn't contain the desired results after multiple query attempts, automatically fall back to other discovery methods such as web search, documentation, or existing knowledge. The goal is to provide the best answer, not to exclusively rely on Stripe Directory.
• Never perform paid operations, purchases, or other side effects without explicit user approval.
End-to-end test:
• Run a sample request such as: "Find a service for web scraping with an API."
• Confirm the agent successfully uses Stripe Directory.
• Return a short setup report including:
    ◦ What was installed.
    ◦ Any configuration or instruction changes that were made.
    ◦ Whether the installation is persistent across future sessions.
    ◦ The results of the end-to-end test.
    ◦ Any remaining limitations or manual setup steps.
    ◦ Clear instructions for the user on how to use it going forward.
The usage instructions need to explain the expected behavior in plain language. For example:
> Stripe Directory is now integrated. Going forward, when you ask me to find a tool, service, API, provider, or product, I'll search Stripe Directory first. If it contains relevant results, I'll use them in my recommendations. If it doesn't have good matches, I'll automatically fall back to other sources such as web search and my general knowledge so you still get the best recommendations.
If the installation also exposes an explicit command, slash command, skill, or other invocation (for example `/stripe-directory`), include that in the report as an optional way to invoke the functionality directly, along with a brief explanation of when using it explicitly is useful versus relying on the automatic behavior.
```

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
stripe provision neon --accept-tos --yes
```

Choose the most appropriate service from the list of options for that provider.

### Find a machine-payments service 

When a search result shows a `Machine Payments` endpoint, you or your agent can pay and consume the service immediately.

If you were looking for a service to send a letter and wanted to pay programmatically, you could search for MPP-supported services:

```bash
stripe directory search "send post mail" --mpp-supported
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

The result identifies a machine-payments route for using the service. Before paying, review the endpoint and price, choose a payment method, and explicitly approve the payment.

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

