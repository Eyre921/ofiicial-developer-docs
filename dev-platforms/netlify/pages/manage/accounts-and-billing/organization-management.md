---
title: "Netlify Organization Management"
source: https://docs.netlify.com/manage/accounts-and-billing/organization-management.md
path: manage/accounts-and-billing/organization-management
---

---
title: "Organization management"
description: "Monitor usage and manage billing and projects across all of the teams in an organization."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

> **Pricing Information:** This feature is available on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

Monitor all of your organization's teams from your organization overview dashboard. Track metered feature usage, review billing, and streamline user authentication and provisioning with [Organization SSO](/manage/security/secure-netlify-access/configure-organization-saml-sso) or [SCIM Directory Sync](/manage/security/secure-netlify-access/directory-sync).

Organization Owners have access to the **Organization overview**, and have the [Team Owner role](/manage/accounts-and-billing/team-management/roles-and-permissions#owner) by default for all teams linked to their organization.

## Organization settings and information

Organization Owners can access information about the organization's [teams](/manage/accounts-and-billing/team-management/overview), [billing](/manage/accounts-and-billing/billing/overview), and other settings by selecting the organization name in the navigation and going to **Organization overview**.

![](/images/accounts-and-billing-organization-settings-and-information.png)

To access a team that is not linked to an organization, select **External teams** in the list of organizations within the navigation.

## Invite an Organization Owner

_Note that inviting Organization Owners is in [beta](/release-phases#public-beta)_.

Existing Organization Owners can invite new Organization Owners. By default, you can have up to 3 Organization Owners.

1. From your **Organization Overview**, go to **Owners**.
2. Select **Invite Organization Owner**.
3. Enter an email, then select **Send invites**.

Organization Owners must accept their email invite before they can access your organization in this role.

To further secure access to your Organization, check out our docs on [enforcing SSO for your organization](/manage/security/secure-netlify-access/configure-organization-saml-sso#enforce-organization-sso).

## Remove an Organization Owner

_Note that removing Organization Owners is in [beta](/release-phases#public-beta)_.

### Note - SCIM Directory Sync enabled?

Note that if your Organization has SCIM Directory Sync enabled and you remove an Organization Owner, that user will either be completely removed from your Organization or given a new role if that's configured through SCIM Directory Sync. At this time, SCIM Directory Sync does not support assigning the Organization Owner role.

To remove a user as an Organization Owner:

1. From your **Organization Overview**, go to **Owners**.
2. Select the Organization Owner you want to remove.
3. Choose **Remove from org**.

If you want to give this user a new role, you can invite the user to a team or site again. Learn more about [adding team members](/manage/accounts-and-billing/team-management/manage-team-members#add-new-team-members).

## Add an organization

To create an organization to manage your teams, please [contact sales](https://www.netlify.com/contact/).

## Add an organization logo

Organization Owners can upload an organization logo to display on the **Organization overview**. Select **Settings > Edit information**, then select **Upload image**. After uploading your image, select **Save**.

### Logo image guidelines

When uploading a logo, the image guidelines for organizations and teams are the same. Visit the [team management](/manage/accounts-and-billing/team-management/overview#logo-image-guidelines) doc for more information.

## Organization overview

You can find basic information about your organization, including usage information and a list of your organization's **Teams**, on your organization's **Overview** page.

### Organization usage

You can monitor usage across your organization, including the number of team members and how much build capacity, bandwidth, and build minutes your teams are using. To get started, go to your organization's **Overview** page to access the **Total usage** of metered features for all of your teams.

This includes the current amount of **Total bandwidth used** by your organization as well as how much bandwidth is available. This data updates daily. You can also access the number of **Total build minutes used**, which updates every hour.

You will need to refresh your browser to load the updated **Total bandwidth used** and **Total build minutes used** data.

To gauge how much of your organization's capacity for concurrent builds is being used across all of your teams' sites in real-time, use **Concurrent builds**.

To monitor the different usage limits for each of your organization's teams, go to the **Teams** list and choose a team.

For details about your team's metered usage, including bandwidth and build minutes, check out:

- your team's 
### NavigationPath Component:

Projects
 page for a brief usage summary
- the 
### NavigationPath Component:

Account usage insights
 section on your team's **Billing** page for more in-depth details

You can monitor which sites in your organization's teams use the most bandwidth. To compare top bandwidth usage for a team's sites, go to 
### NavigationPath Component:

Billing > Current services > Plan details
. Select your team plan to access bandwidth usage details, including the **Top bandwidth per domain**. Bandwidth usage data updates in near real-time and may require a browser refresh.

Owners and Billing Admins can find additional usage data for their organization's teams under 
### NavigationPath Component:

Billing > Account usage insights
. Learn more about [usage and insights](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-for-legacy-plans#usage-and-insights).

If you want to delete your organization and its associated teams, please [contact sales](https://www.netlify.com/contact/).

## Create a new team

1. Organization Owners can create a team in two ways:

   - Select the menu next to the team name in the navigation and then select **Create new team**.

     ![](/images/accounts-and-billing-team-switcher-on-nav.png)

   - On your **[Organization overview](/manage/accounts-and-billing/organization-management#organization-settings-and-information)**, in the **Teams** card, select **Create new team**.

     ![](/images/accounts-and-billing-org-create-team.png)

2. Choose a name for the new team and select **Create team**.

Check out our [team management docs](/manage/accounts-and-billing/team-management/overview) for more details on how to manage your team.

### Delete a team

You can only delete a team if you have more than one team in your organization.

To delete a team:

1. Go to the **Team settings** for the team you want to delete.
2. Select **Danger Zone**.
3. Select **Delete team**.

To delete your only team in an organization, [contact our Sales team](https://www.netlify.com/contact/) for help.

## Organization-level audit logs

As an Organization Owner, you can access the organization-level audit log to review the [audit logs](/manage/accounts-and-billing/team-management/team-audit-log) for all of your teams in one place.

From the **Organization overview** page, select **Audit log**. Choose a team from the list to review audit logs for that team.

![](/images/accounts-and-billing-org-audit-logs.png)

