---
title: "Get billing usage"
source: https://docs.together.ai/reference/billing-usage
path: reference/billing-usage
---

openapi.yaml GET /billing/usage
Returns an organization's billing usage for a month as cost-annotated line items grouped into time windows. Finalized windows are returned through the end of yesterday at daily granularity, or the last completed hour at hourly granularity (UTC).


<Note>
  This endpoint is in beta and is enabled per organization. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to request access or share feedback. Calls from an organization without access return a 404. The response shape can change while the endpoint is in beta.

  `organization_id` is optional in beta but will be required at GA, so send it now to avoid a breaking change.
</Note>

This endpoint returns usage for the API key's entire organization, not only the key's project. Any project's key can read it, including keys created by [external collaborators](/docs/roles-permissions#external-collaborators-beta), and access can't be restricted to organization admins. When project-scoped keys start enforcing their scope, you will need to swap the key you use here for one with organization-level access.

Usage data for the current month can be up to 1 hour behind. Data for prior months can be up to 24 hours behind.

When reading line items:

* `product_name` values are display names, not stable identifiers, and can change without notice.
* `attributes` vary by product. For example, `api_key_id` and `project_id` are only set on inference line items.
