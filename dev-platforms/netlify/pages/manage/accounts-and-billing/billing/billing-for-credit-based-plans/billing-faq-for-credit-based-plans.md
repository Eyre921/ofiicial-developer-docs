---
title: "Netlify Billing FAQ"
source: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans.md
path: manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans
---

---
title: "Billing FAQ for Credit-based pricing plans"
description: "Get answers to frequently asked questions about Netlify billing."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

This page answers frequently asked questions about Netlify billing for our new Credit-based pricing plans.

> **Note - Credit-based plans for new accounts:** Starting on September 4, 2025, all new Netlify accounts will use the new credit-based pricing plans. 

If you've created your Netlify account with a Free, Starter, or Pro plan before September 4, 2025, then your pricing plan is now considered a Legacy pricing plan. There is no action required for you. You have the option to switch to a credit-based plan. Learn more about [Legacy pricing plans](/manage/accounts-and-billing/billing/billing-for-legacy-plans/legacy-pricing-plans/) or [Billing for legacy pricing plans](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-for-legacy-plans/).

> **Tip - Enterprise plan questions?:** For credit-based billing details specific to Enterprise plans, see [How credits work for enterprise plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work-for-enterprise-plans/). For the latest and most accurate billing information for your plan, reach out to your account manager or use this [Sales form](https://www.netlify.com/contact/sales/) to share your questions.

## Billing docs quick reference

| I want to . . . | Docs links |
|----|----|
| Review my team's credit balance and usage | [Monitor usage for Credit-based plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/monitor-usage-for-credit-based-plans) |
| Buy add-on credits | [Buy add-on credits](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/buy-add-on-credits) |
| Configure auto recharge | [Configure auto recharge](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/configure-auto-recharge) |
| Find invoices | [View payment history](/manage/accounts-and-billing/billing/manage-payments/#find-payment-history-or-invoices) |
| Change my billing information | [Change billing information](/manage/accounts-and-billing/billing/manage-payments) |

If you have questions that aren't answered by these docs or the FAQ, you can reach out to [Netlify Support](https://www.netlify.com/support/) with any pricing plan.

## FAQ quick reference

Topics covered in this FAQ include the following:
- [Plan changes](#plan-changes)
- [Credits](#credits)
- [Pricing add-ons](#pricing-add-ons)
- [Limits](#limits)
- [Payments](#payments)
- [Monitoring](#monitoring)
- [New to web development](#new-to-web-development)
- [Other questions](#other-questions)

## Plan changes

### Wait, where's the older pricing plan FAQ?

You can check out pricing plan details for your current plan from your Netlify team dashboard.

If you have a Legacy pricing plan from before September 4, 2025, then you can check out our docs for [Legacy pricing plans](/manage/accounts-and-billing/billing/billing-for-legacy-plans/legacy-pricing-plans/), including a [Legacy pricing plan FAQ](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans).

### How can I update my Legacy pricing plan to the new Credit-based pricing plan?

You can now upgrade your Legacy pricing plan to the new Credit-based pricing plans.

As a [Team Owner](/manage/accounts-and-billing/team-management/roles-and-permissions#owner), to change your team plan, go to 
### NavigationPath Component:

Usage & billing > Plan details
 and select the **Change team plan** button to choose your new plan.

![](/images/accounts-and-billing-plan-details.png)

### Where can I get a summary of what has changed?

| Resource | Link |
|---|---|
| Blog post to understand the new pricing launch | [Blog post](https://www.netlify.com/blog/new-pricing-credits) |
| Pricing page for pricing plan highlights | [Pricing page](https://www.netlify.com/pricing/) |
| Breakdown of how credits work | [How credits work](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work) |

### Can I revert to a Legacy pricing plan after switching to a Credit-based plan? Or can I transfer a project from a Legacy pricing plan to a Credit-based pricing plan?

No, you cannot revert to a Legacy plan from a Credit-based plan for a team. Once you transfer a project to a Credit-based plan, you also cannot transfer it back to a Legacy plan. This change is permanent and irreversible.

## Credits 

### What are credits exactly?

Credits are a Netlify-specific currency we developed to standardize the usage and costs of metered features and make it simpler to understand how much your team is using.

### How do credits work for production deploys, AI inference, compute, forms submissions, bandwidth, and web requests?

Each metered feature consumes a certain number of credits based on how much your projects use.  Here is a quick recap.

| Feature or resource area | Credit usage |
|---------|-------|
| Production deploys | 15 credits per production deploy |
| AI inference | 180 credits per $1 USD of AI model usage |
| Compute (or GB-hour) | 10 credits per GB-hour |
| Forms submissions | Free  |
| Bandwidth | 20 credits per GB |
| Web requests | 2 credits per 10,000 requests |

Learn more about how each feature or meter is measured using credits in our [How credits work](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work) docs.

### How are AI inference costs calculated into credits? 

AI inference costs are calculated based on the cost of the AI model used.

Learn more about [pricing for AI inference](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/pricing-for-ai-features).

### What is AI inference? 

AI inference is a usage meter that measures the costs of using AI models and agents on Netlify through Agent Runners and the AI Gateway.

Learn more about [pricing for AI inference](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/pricing-for-ai-features).

> **Tip - Want to limit Agent Runners?:** To help you control costs for Agent Runners and AI Gateway, you can [set an AI inference credit usage limit](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features/#limit-ai-feature-usage). Once the AI inference limit is reached, your team can no longer start agent runs and active agent runs stop. AI Gateway usage is also paused. Learn more in our docs on [Managing AI features](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features/#limit-ai-feature-usage).

### What happens when credits are used up?

Once your monthly credit allotment is used up for all web projects on your team, all of your web projects (sites/apps) are paused and visitors to your web projects will find a `Site not available` page at each of your web project's URLs.

In addition, while your web projects are paused, they will not receive new web requests, web traffic, or form submissions and you cannot trigger new production deploys. This means you cannot publish new updates to your web projects.

If you're on the free plan, your project has a fixed amount of credits and you can either wait till the start of your next billing cycle or upgrade to a paid plan.

### Can I buy more credits than my monthly credit balance allotment? 

If you have a Credit-based Personal or Pro plan, there are two ways to buy more credits:

- **Buy add-on credits in credit packs**: Purchase additional credits at any time in credit packs. These add-on credits roll over for future months. Learn more about [buying add-on credits](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/buy-add-on-credits).
- **Enable auto recharge**: Automatically reload your credit balance when it runs out with small increments of credits. These add-on credits roll over for future months. Learn more about [auto credit recharge](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/configure-auto-recharge).

You may want to buy add-on credits in credit packs and still enable auto recharge. For example, perhaps you're building out new functionality for your projects using Agent Runners so you buy an add-on credit pack. You may choose to set up auto recharge to ensure your projects don't run out of credits. You can also keep auto recharge off to help control costs and only buy credits beyond your monthly plan in credit packs when you need them.

### Do credits roll over or expire? 

Your monthly credit balance is reset at the start of each billing cycle. Once your web projects use up their monthly credit allotment, they will use any left over add-on credits from your last auto recharge. Add-on credits roll over to the next billing cycle but are only used once your monthly credit allotment is used up.

Excess credits from the monthly credit allotment are not rolled over to the next billing cycle. For example, if your monthly credit allotment is 300 credits and your team uses 200 credits by the end of your billing cycle, then your remaining 100 credits will not roll over to the next billing cycle. At the start of the next billing cycle, you will have your refreshed monthly credit allotment based on your pricing plan.

### What counts as a production deploy?

A production deploy is a deploy that makes your site live and available to your users at your primary domain, which can be a custom domain, such as `mycompany.com`, or a standard Netlify URL, such as `YOUR-PROJECT-NAME.netlify.app`. This is in contrast to a [Deploy Preview](/deploy/deploy-types/deploy-previews), which is a temporary version of your site/app.

Each production deploy in your team's projects consumes 15 credits.

Learn more in our [production deploy docs](/deploy/deploy-types/production-deploy).

### How do rollbacks work with this new pricing plan?

You can rollback your project to a previous production deploy without costing any credits. Learn more about how to use rollbacks in our [rollback docs](/deploy/manage-deploys/manage-deploys-overview/#rollbacks).

### What happened to build minutes? 

Build minutes are not calculated as their own metric in our Credit-based pricing plans. For Credit-based pricing plans, concurrent builds are still an add-on at $40 for the capacity to run another concurrent build for the Personal and Pro plans.

A concurrent build in Netlify refers to the number of builds that can run simultaneously on your team's account.

## Pricing add-ons

### What counts as an "Add-on" for Credit-based pricing plans? 

Add-ons are additional features that you pay for outside of your monthly credit based-plan subscription, such as paying for: 
- concurrent builds
- domain registrations and renewals

On the Credit Pro plan, team member seats are free, unlimited, and included in your plan. On Legacy Pro plans, additional team members are still a paid add-on.

### How does pricing work for adding people to my Netlify team?

If you have a Personal or Free plan, you cannot add any additional team member seats. 

If you have a Credit Pro plan, team member seats are unlimited and included in your plan at no additional cost. To add a team member, check out our [manage team members docs](/manage/accounts-and-billing/team-management/manage-team-members).

### Note - Have a Credit Pro plan before April 14, 2026?

For existing Credit Pro teams, seat charges for existing members are removed at the start of your next billing cycle. In the meantime, you can invite additional team members at no charge starting April 14, 2026. See the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/) for details.

### Note - Legacy Pro plan

The unlimited seats change applies only to the Credit Pro plan. If you are on the Legacy Pro plan, team member seats are still billed at $19/team member/month.

With any plan, you can add unlimited free [Reviewer roles](/manage/accounts-and-billing/team-management/roles-and-permissions#reviewer) to your team to give people a Netlify login that they can use to review your team's web projects and share feedback. This allows you to protect your projects with a password and still allow select people to review your projects and share feedback.

Learn more about [how roles and permissions work](/manage/accounts-and-billing/team-management/roles-and-permissions), [password protection](/manage/security/secure-access-to-sites/password-protection), and our [Reviewer role Quickstart](/deploy/review-deploys/netlify-drawer-for-feedback/netlify-reviewer-quickstart).

### How does pricing work for Git contributors? 

On the Credit Pro plan, Git Contributors are included in your plan at no additional cost. Once a [Git Contributor](/manage/accounts-and-billing/team-management/roles-and-permissions#git-contributor) is added to your team manually or through [the auto-approval setting](/deploy/deploy-overview#enable-auto-approval-for-deploy-requests), they can trigger deploys from private repositories without incurring an additional charge. Visit our documentation on [deploy permissions](/deploy/deploy-overview#deploy-permissions) for more information or check out the [Netlify pricing page](https://www.netlify.com/pricing/).

### Note - Legacy Pro plan

On the Legacy Pro plan, Git Contributors who trigger a deploy during your billing period are charged at $19/month per active contributor. Learn more in the [Legacy billing FAQ](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans#git-contributors-and-billing).

### Can I transfer projects between teams?

You can transfer projects between teams that are both on a Credit-based plan but if your project relies on a feature that requires a higher plan, you must remove or turn off that feature first in most cases.

When a site is transferred from a Legacy plan to a Credit-based plan, the following must be taken into consideration:

- If you have an Analytics subscription, it will be terminated immediately. You will not be refunded. In the new plan you will have access to analytics with a different lookback period depending on your current plan.
- Function usage will consume credits based on compute costs (GB-hours) and will be tracked at the team level. There is no longer a free tier.
- Form usage is free and unlimited. Unlike the Legacy pricing plan, there are no submission limits or tier levels for forms.
- Projects cannot be transferred from a team on a Credit-based pricing plan to a team on a Legacy plan.

### How do I add Git Contributors to my team?

You can add Git Contributors to your team manually or through the auto-approval setting in your team settings. Check out our [manage team members docs](/manage/accounts-and-billing/team-management/manage-team-members) for more information.

## Limits

### What happens when a web project reaches its credit limit?

When a web project uses up its monthly credit allotment, it enters a paused state until the start of the next billing cycle. We'll notify you by email and in-app as you approach your limits at 50%, 75%, 90%, and 100% of your monthly credit allotment. Please note that if one site/web project exceeds its limits, all sites/projects on your account will be paused.

### How can I prevent my web projects from getting paused?

You can enable auto recharge for all web projects on your team, which ensures they stay active and can receive web requests, form submissions, and more.

Learn more about how you can automatically recharge your credit balance each month with [auto recharge](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/configure-auto-recharge).

### Can I set a limit on my usage?

Netlify Credit-based pricing plans come with built-in plan limits. 

If your projects go over these limits, your projects will be paused and will no longer receive web requests, form submissions, etc. until the start of the next billing cycle unless you upgrade to a higher plan or enable [auto recharge](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/configure-auto-recharge).

To help you control costs for Agent Runners and AI Gateway, you can [set an AI inference credit usage limit](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features/#limit-ai-feature-usage). Once the AI inference limit is reached, your team can no longer start agent runs and active agent runs stop. AI Gateway usage is also paused. Learn more in our docs on [Managing AI features](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features/#limit-ai-feature-usage).

### Can I set a hard spending limit for metered features and have it shut off when the limit is reached?

For other ways to keep your costs under control, you can choose the free plan, or keep the Personal or Pro plan and [disable auto recharge if it was turned on](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/configure-auto-recharge/#disable-auto-recharge) (since it's turned off by default), or [disable one of your projects](/manage/projects/disable-project/) that is using up a lot of credits. You can also set up a [limit for using AI features](/build/build-with-ai/manage-ai-for-your-team/manage-ai-features/#limit-ai-feature-usage) for all projects on your team.

Note that auto recharge is turned off by default so you just need to keep it off. Only Team Owners can enable or disable auto recharge and Pro plans can set more than one Team Owner. 

On the free plan, your sites will automatically pause if they exceed monthly limits and you have no option to purchase add-on credits, add other people to your team, and more.

### How many projects can I have on my team?

If you have a Free, Personal, or Pro plan, you can have up to 500 projects on your team. But note that the usage limits remain the same for your team's plan no matter how many projects you have on your team. This means all your projects share the same monthly credit allotment.

### What can I do if my site usage went over a limit because of spammers?

We recommend taking measures to help prevent abuse of your project. For example, form submission spam can be reduced by adding a [reCAPTCHA 2 challenge](/manage/forms/spam-filters#recaptcha-2-challenge) and [honeypot field](/manage/forms/spam-filters#honeypot-field).

## Payments 

### Can I pay with PayPal, wire transfer, crypto, or any method other than credit card?

Netlify only accepts credit cards unless you have a Netlify Enterprise plan, in which case we do accept payment via ACH or wire transfer.

You must have a valid credit card saved to your Netlify team account to keep your web projects active with the Personal or Pro Credit-based plans.

### When will I be charged?

The start of your monthly billing cycle is customized for when you open and start your Netlify team account.

## Monitoring 

### How can I track and monitor credit usage?

You can check out your team's usage and monitoring from your Netlify team dashboard at any time. People with the Developer role can check out usage and monitoring for all projects on your team from your Netlify team dashboard but only Team Owners can make changes to your team's billing settings, such as enabling or disabling auto recharge.

Learn more in [Monitor usage for Credit-based plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/monitor-usage-for-credit-based-plans).

### When will I receive notifications about my usage?

By default, Netlify will share in-app notifications and emails when you reach 50%, 75%, 90%, and 100% of your usage to help you track consumption.

With the Pro plan, you also have the option to set up notifications in the [Netlify App for Slack](/extend/install-and-use/setup-guides/netlify-app-for-slack).

### How are payments prorated and when? 

Payments are prorated based on the number of days in your billing cycle. 

If you upgrade from a paid plan to a higher paid plan, such as from the Personal plan to the Pro plan, your invoice will reflect the unused days in your current billing cycle.

## New to web development 

### Do I have to use Git version control? 

You can deploy to Netlify and manage your project without using Git version control. You can do this by using our [drag and drop publisher](/start/quickstarts/netlify-drop-quickstart/).

However, we recommend using Git version control to take advantage of features like [rollbacks](/deploy/manage-deploys/manage-deploys-overview/#rollbacks) and to improve the security tracking of your project. Netlify can help you learn to use Git and other web development best practices.

### What's the difference between production and preview? 

A preview environment is a temporary version of your site/app that is not live and available to your users but is available for testing and early reviewers. A production environment is the live version of your web project that is available at your primary domain, which can be a custom domain, such as `mycompany.com`, or a standard Netlify URL, such as `YOUR-PROJECT-NAME.netlify.app`.

## Other questions

### How can I use Netlify's AI features?

If you have a Credit-based pricing plan, you can use any of the following Netlify AI features:
- [AI Gateway](/build/ai-gateway/overview)
- [Agent Runners](/build/build-with-ai/agent-runners/overview)
- [Ask Netlify AI](/resources/troubleshooting/ask-netlify)
- [Why did it fail? AI-powered build failure troubleshooting assistant](/resources/troubleshooting/fix-a-failed-deploy)

If you have a Legacy pricing plan, you can only use Ask Netlify AI and the **Why did it fail?** AI-assisted troubleshooting feature. Agent Runners and AI Gateway require a Credit-based pricing plan. You can use both of these features on the free Credit-based plans. Just be aware that you cannot buy extra credits on the free Credit-based plans. Once you reach your credits monthly limit, you must wait till the start of the next billing cycle or upgrade to a higher plan to [resume your projects](/manage/accounts-and-billing/billing/resume-paused-projects) after they run out of credits.

### What can I do if I've been charged the wrong amount?

If you find a problem with your billing, please contact our [support team](https://www.netlify.com/support/) and we'll do our best to make it right!

### Can I get a free trial?

We do not have a free trial but you can test out Netlify on the free plan.

### How do I cancel? 

To learn how to delete a team or delete your Netlify user, and the impact of either action, visit our Forums for a verified Support Guide on [how to cancel an account](https://answers.netlify.com/t/support-guide-how-to-cancel-an-account/10856).


