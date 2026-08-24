---
title: "Stripe Directory"
source: https://docs.stripe.com/directory.md
path: directory
---

# Stripe Directory

Use the Stripe Directory to find businesses and services on the Stripe network.

Stripe Directory is the single place to discover businesses across the Stripe network. Search by keyword and get structured results you or your agent can act on.

> Share your feedback with [directory@stripe.com](mailto:directory@stripe.com) as you test out this preview.

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

Results include structured data—provider slugs, MPP endpoints, and app listings—that you or your agent can use to continue the integration.

## What Stripe Directory indexes 

- **Stripe Apps**: Published apps on the [Stripe App Marketplace](https://marketplace.stripe.com) that extend your Stripe Dashboard, including billing tools, analytics, and support integrations.
- **Stripe Projects providers**: Services available through [Stripe Projects](https://projects.dev) that you can provision with a CLI command.
- **Machine payments endpoints**: Pay-per-call APIs on [mpp.dev](https://mpp.dev) you can pay programmatically with `mppx fetch`.
- **Stripe business network**: Businesses and services across the Stripe network.

## Set up Stripe Directory in your terminal 

Use the Stripe CLI directory plugin to search for businesses from your terminal.

1. Install or upgrade the [Stripe CLI](https://docs.stripe.com/cli/install).
2. Install the directory plugin:

```bash
stripe plugin install directory
```

To upgrade the plugin, run `stripe plugin upgrade directory`.

## Configure agents to use Stripe Directory 

Stripe Directory lets AI agents discover, evaluate, and integrate services autonomously.

### Structured output for agents

Use `--format json` to get structured output:

```bash
stripe directory search "serverless postgres database" --format json
```

An agent can parse the results, compare options against your requirements, and use the returned `mpp.dev` endpoint or `projects.dev` listing to set up the integration automatically.

### Install skills for your agent

Use one of these options to connect your agent to Stripe Directory.

#### Install the skill

Install a global agent skill that shows your agent how to use Stripe Directory:

```bash
npx skills add https://docs.stripe.com --skill stripe-directory -g -y
```

Alternatively, install all [Stripe skills](https://docs.stripe.com/skills.md) at the same time:

```bash
npx skills add https://docs.stripe.com -g -y
```

After installation, your agent can search the directory, interpret results, and use the returned endpoints without additional instruction.

#### Copy a starter prompt

Paste the following prompt into your agent to give it access to Stripe Directory. This option works with any agent that can run shell commands:

```text
Set up Stripe Directory so this agent can automatically use it when searching for third-party services, APIs, tools, integrations, or providers.

Primary docs:
https://docs.stripe.com/directory

Skill file:
https://docs.stripe.com/.well-known/skills/stripe-directory/SKILL.md

Tasks:
1. Read the Stripe Directory documentation and understand the intended workflow.
2. Install or verify the Stripe CLI.
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
8. Update the agent's persistent instructions/configuration so that the agent automatically searches Stripe Directory first whenever a user asks to:
    ◦ find a service
    ◦ find an API
    ◦ find a provider
    ◦ find a SaaS product
    ◦ find a developer tool
    ◦ compare vendors
    ◦ discover integrations

Expected behavior:
• Use Stripe Directory as the first source for discovery.
• Execute:
    ◦ `stripe directory search "<user query>" --format json`
• Rank the best results for the user's requirements.
• Include pricing, capabilities, integration methods, supported endpoints, and other useful metadata when available.
• Follow any additional discovery or inspection commands recommended by the Directory documentation.
• If Stripe Directory does not contain useful results, automatically fall back to other discovery methods such as web search, documentation, or existing knowledge. The goal is to provide the best answer, not to exclusively rely on Stripe Directory.
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

The usage instructions should explain the expected behavior in plain language. For example:

> Stripe Directory is now integrated. Going forward, when you ask me to find a tool, service, API, provider, or product, I'll search Stripe Directory first. If it contains relevant results, I'll use them in my recommendations. If it doesn't have good matches, I'll automatically fall back to other sources such as web search and my general knowledge so you still get the best recommendations.

If the installation also exposes an explicit command, slash command, skill, or other invocation (for example `/stripe-directory`), include that in the report as an optional way to invoke the functionality directly, along with a brief explanation of when using it explicitly is useful versus relying on the automatic behavior.
```

## Example uses 

### Integrate with Stripe Projects 

If a developer building an application needs a database provider, they can leverage Stripe Directory to not only find one but integrate with it as well.

First, the developer searches for the service:

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
│                   https://stri.pe/sl/LIsxeQPu                                │
│                                                                              │
│ Stripe Projects   Learn more using                                           │
│                   stripe projects catalog neon                               │
│                                                                              │
│ Machine Payments  —                                                          │
│ Link supported    ✅     	                                               │
╰──────────────────────────────────────────────────────────────────────────────╯
```

Since Neon is also a Stripe Projects provider, Directory returns the command to inspect the provider’s catalog listing.

```bash
stripe projects catalog neon
```

The result of that command not only provides information about the offering, but also recommends the command to integrate:

```bash
stripe projects add neon
```

### Make machine payments 

When a search result shows a `machine payments` endpoint, you or your agent can pay and consume the service immediately using `mppx`.

If you (or your agent) were looking for a service to send a letter and wanted to pay programmatically, you could search for MPP-supported services:

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
│                   https://stri.pe/sl/UFBaAJsF                                │
│                                                                              │
│ Stripe Projects   Learn more using                                           │
│                   stripe projects catalog postalform                         │
│                                                                              │
│ Machine Payments  postalform                                                 │
│                   https://mpp.dev/services#postalform                        │
│                   https://postalform.com/llms.txt                            │
│                   https://postalform.com/agents                              │
│                   Pay using mppx fetch <endpoint>                            │
│                                                                              │
│ Link supported    —                                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

Since PostalForm supports machine payments, Directory results include the next command to run to learn more and pay the service provider:

```bash
mppx fetch https://postalform.com
```

`mppx` shows the price and gets your confirmation before any money moves.

## List your company in Stripe Directory

### Add yourself to search results

To make your business discoverable in Stripe Directory, set up a public Stripe profile. Your listing appears in search results immediately after you publish your profile.

> Stripe users appear in search results only if they opt in.

1. Set up your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md). You can leave some fields blank (like phone or address) if you don’t want them visible publicly.
2. Keep the **Make your profile private** option disabled.

To maximize the likelihood that your business appears in users’ search results, take the following steps:

1. **Make sure Stripe can crawl your site**:  Our search uses your website content to match your business to relevant searches. If your site blocks Stripe crawlers, you make yourself hard to find. [Learn how to allow Stripe to crawl your site](https://docs.stripe.com/stripebot-crawler.md).
2. **Write a clear Stripe profile description**

- Describe what you do in plain language, the words your customers would actually type. Think about the problem you solve, not how you’d market it. For example, “it helps freelancers send invoices and get paid faster” would find more customers than “a next-generation financial operations platform.”
- Use entire phrases such as “appointment booking for salons” instead of scattering the words separately.
- If you offer multiple things, mention all of them–“email marketing, newsletters, and audience analytics” match a wider range of searches than “email” alone.

1. **Make your Stripe profile display name and handle accurate**:  If someone searches any of these directly, we’ll show your profile first. Make sure they all match what customers know you as.

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

