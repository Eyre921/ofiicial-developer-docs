---
title: "Edge Functions Usage and Billing"
source: https://docs.netlify.com/build/edge-functions/usage-and-billing.md
path: build/edge-functions/usage-and-billing
---

---
title: "Edge Functions usage and billing"
description: "Monitor your Edge Functions service usage. Check the number of invocations this billing period."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

You can check your team's Edge Functions service usage under 
### NavigationPath Component:

Billing > Current services > Plan details
. This shows your current usage level and tracks the following metric:

- **Invocations:** metric that counts each time an edge function is invoked on a site owned by your team during the current billing period. If a [cached response](/build/edge-functions/optional-configuration#response-caching) is available and served, no edge function invocation is made and no usage is incurred against your Edge Functions allotment.

For paid plans, [Edge Functions pricing](https://www.netlify.com/pricing/?category=developer#features-edge-functions) is metered on a team basis and scales with usage. When usage reaches the plan limit, the team will automatically add an extra usage package. For legacy pricing plans, Free tier accounts are also metered based on usage and [have a limit](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans#free-tier-limits).

## More usage and billing resources

- [Billing FAQ for legacy plans](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans)
- [Billing for legacy plans](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-for-legacy-plans)
- [Billing FAQ for credit-based plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans)
- [How credits work](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work)
