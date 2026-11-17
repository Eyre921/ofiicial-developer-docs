---
title: "Webhook providers"
source: https://trigger.dev/docs/webhooks/providers
path: docs/webhooks/providers
---

Every built-in webhook provider, with its SDK function, the credential it verifies with, and a setup page for each provider.

**Each built-in provider has a source function that verifies its signature scheme, so you declare the endpoint with one function call and set one credential.** Every provider below has a page with the source, where to register the URL, and how to set the credential.

| Provider | Source | Credential |
| - | - | - |
| [Attio](/docs/webhooks/providers/attio) | `webhooks.attio()` | Issued by the provider |
| [Autumn](/docs/webhooks/providers/autumn) | `webhooks.autumn()` | Issued by the provider |
| [Cal.com](/docs/webhooks/providers/cal-com) | `webhooks.calCom()` | You generate it |
| [Calendly](/docs/webhooks/providers/calendly) | `webhooks.calendly()` | You choose it (OAuth apps: issued by the provider) |
| [Clerk](/docs/webhooks/providers/clerk) | `webhooks.clerk()` | Issued by the provider |
| [Discord](/docs/webhooks/providers/discord) | `webhooks.discord()` | Provider's public key |
| [DocuSign](/docs/webhooks/providers/docusign) | `webhooks.docusign()` | Issued by the provider |
| [ElevenLabs](/docs/webhooks/providers/elevenlabs) | `webhooks.elevenlabs()` | Issued by the provider |
| [Firecrawl](/docs/webhooks/providers/firecrawl) | `webhooks.firecrawl()` | Issued by the provider |
| [GitHub](/docs/webhooks/providers/github) | `webhooks.github()` | You generate it |
| [GitLab](/docs/webhooks/providers/gitlab) | `webhooks.gitlab()` | You generate it |
| [Granola](/docs/webhooks/providers/granola) | `webhooks.granola()` | Issued by the provider |
| [Hookdeck](/docs/webhooks/providers/hookdeck) | `webhooks.hookdeck()` | Issued by the provider |
| [Infisical](/docs/webhooks/providers/infisical) | `webhooks.infisical()` | You generate it |
| [Jira](/docs/webhooks/providers/jira) | `webhooks.jira()` | You generate it |
| [Langfuse](/docs/webhooks/providers/langfuse) | `webhooks.langfuse()` | Issued by the provider |
| [Linear](/docs/webhooks/providers/linear) | `webhooks.linear()` | Issued by the provider |
| [Loops](/docs/webhooks/providers/loops) | `webhooks.loops()` | Issued by the provider |
| [Metronome](/docs/webhooks/providers/metronome) | `webhooks.metronome()` | Issued by the provider |
| [Mux](/docs/webhooks/providers/mux) | `webhooks.mux()` | Issued by the provider |
| [OpenAI](/docs/webhooks/providers/openai) | `webhooks.openai()` | Issued by the provider |
| [PagerDuty](/docs/webhooks/providers/pagerduty) | `webhooks.pagerduty()` | Issued by the provider |
| [Plain](/docs/webhooks/providers/plain) | `webhooks.plain()` | Issued by the provider |
| [PlanetScale](/docs/webhooks/providers/planetscale) | `webhooks.planetscale()` | Issued by the provider |
| [Recall.ai](/docs/webhooks/providers/recall-ai) | `webhooks.recallai()` | Issued by the provider |
| [Replicate](/docs/webhooks/providers/replicate) | `webhooks.replicate()` | Issued by the provider |
| [Resend](/docs/webhooks/providers/resend) | `webhooks.resend()` | Issued by the provider |
| [Retell AI](/docs/webhooks/providers/retell) | `webhooks.retell()` | Your API key with the webhook badge |
| [Sentry](/docs/webhooks/providers/sentry) | `webhooks.sentry()` | Issued by the provider |
| [Shopify](/docs/webhooks/providers/shopify) | `webhooks.shopify()` | Issued by the provider |
| [Slack](/docs/webhooks/providers/slack) | `webhookSource()` (`@trigger.dev/slack`) | Issued by the provider |
| [Square](/docs/webhooks/providers/square) | `webhooks.square()` | Issued by the provider |
| [Stripe](/docs/webhooks/providers/stripe) | `webhooks.stripe()` | Issued by the provider |
| [Supabase](/docs/webhooks/providers/supabase) | `webhooks.supabase()` | You generate it |
| [Tailscale](/docs/webhooks/providers/tailscale) | `webhooks.tailscale()` | Issued by the provider |
| [Typeform](/docs/webhooks/providers/typeform) | `webhooks.typeform()` | You generate it |
| [Vapi](/docs/webhooks/providers/vapi) | `webhooks.vapi()` | You generate it |
| [Vercel](/docs/webhooks/providers/vercel) | `webhooks.vercel()` | Issued by the provider |
| [WhatsApp](/docs/webhooks/providers/whatsapp) | `webhooks.whatsapp()` | Issued by the provider |
| [WorkOS](/docs/webhooks/providers/workos) | `webhooks.workos()` | Issued by the provider |
| [Zendesk](/docs/webhooks/providers/zendesk) | `webhooks.zendesk()` | Issued by the provider |

For a provider that isn't listed, define a [custom provider](/docs/webhooks/custom-providers). For providers that sign with Svix or Standard Webhooks, `webhooks.svix()` and `webhooks.standardWebhooks()` also work; see [Verification](/docs/webhooks/verification#svix-and-standard-webhooks).
