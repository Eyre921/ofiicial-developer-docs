---
title: "Netlify Team Member Management"
source: https://docs.netlify.com/manage/accounts-and-billing/team-management/manage-team-members.md
path: manage/accounts-and-billing/team-management/manage-team-members
---

---
title: "Manage team members"
description: "Manage who belongs to your Netlify team, what they can access, and how they contribute to projects and review workflows."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Manage who belongs to your Netlify team, what they can access, and how they contribute to projects and review workflows. Learn how to invite members and Reviewers, assign roles, and remove members so the right people can contribute to, review, and ship projects without friction.

You can also customize [project access](/manage/accounts-and-billing/team-management/manage-project-access) for certain roles.

## Add new team members

Team [Owners](/manage/accounts-and-billing/team-management/roles-and-permissions#owner) can invite new members to the team.

As an [Owner](/manage/accounts-and-billing/team-management/roles-and-permissions#owner), to add members to a team:

1. Go to your Netlify Team dashboard.
   - From your project dashboard, in the top left, choose **Projects** next to your project name.
   ![Projects option highlighted above project overview in top left navigation](/images/choose-projects-from-project-overview.png)

2. Go to 
### NavigationPath Component:

Members
 in the left navigation.

3. Select **Add members**, follow the prompts, and confirm. 

Learn more about [roles and permissions](/manage/accounts-and-billing/team-management/roles-and-permissions) and [project access](/manage/accounts-and-billing/team-management/manage-project-access).

Depending on your team [plan](https://www.netlify.com/pricing/?category=developer#features-members), you may need to upgrade in order to add new members. For more information, please [contact sales](https://www.netlify.com/contact/).

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included in your $20/month plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

## Invite Reviewers

Team Owners can invite [Reviewers](/manage/accounts-and-billing/team-management/roles-and-permissions#reviewer) to their team for free so they can give context-rich feedback exactly where you want it using our [collaboration review tools for Deploy Previews](/deploy/deploy-types/deploy-previews#collaborative-deploy-previews).

As an [Owner](/manage/accounts-and-billing/team-management/roles-and-permissions#owner), to add Reviewers to a team:

1. Go to your Netlify Team dashboard.
   - From your project dashboard, in the top left, choose **Projects** next to your project name.
   ![Projects option highlighted above project overview in top left navigation](/images/choose-projects-from-project-overview.png)

2. Go to 
### NavigationPath Component:

Members
 in the left navigation.

3. Select **Add members**, follow the prompts, and confirm. 

These changes will take effect immediately and there are no additional costs since the Reviewer role is free.

## Search and filter members 

To filter your team's members by project access, role, or invite status:

1. Go to 
### NavigationPath Component:

Members
 in the left navigation.
2. Under the search bar, select **Edit filters**, choose your filter combination, then select **Apply filter**.

## Change team member roles, permissions, or project access

If you're a Team Owner, you can change a team member's permissions from the **Team members** list on your team's **Members** page. Team member permissions include changing a team member's role or modifying their access to projects.

If a team member is provisioned by your organization's [Directory Sync](/manage/security/secure-netlify-access/directory-sync), then keep these [guidelines](#guidelines-for-managing-directory-sync-users) in mind.

### Change team member roles

As an [Owner](/manage/accounts-and-billing/team-management/roles-and-permissions#owner), to change someone's [role](/manage/accounts-and-billing/team-management/roles-and-permissions):

1. Go to your Netlify Team dashboard.
   - From your project dashboard, in the top left, choose **Projects** next to your project name.
   ![Projects option highlighted above project overview in top left navigation](/images/choose-projects-from-project-overview.png)

2. Go to 
### NavigationPath Component:

Members
 in the left navigation.

3. From the **Team members** list, select 
### NavigationPath Component:

Options > Edit member
.

4. Follow the prompts to update the member's project access and confirm your changes. Visit our [roles documentation](/manage/accounts-and-billing/team-management/roles-and-permissions) for more information on the available roles.

These changes will take effect immediately.

### Manage project access

For help managing project access, check out our docs on [managing project access](/manage/accounts-and-billing/team-management/manage-project-access).

### Approve or block reviewers

Pending Reviewers must be approved by a Team Owner or Developer before they can [collaborate on Deploy Previews](/deploy/deploy-types/deploy-previews#collaborative-deploy-previews).

To approve a Reviewer:

1. Go to your Netlify Team dashboard.
   - From your project dashboard, in the top left, choose **Projects** next to your project name.
   ![Projects option highlighted above project overview in top left navigation](/images/choose-projects-from-project-overview.png)

2. Go to 
### NavigationPath Component:

Members
 in the left navigation.

3. Go to the **Reviewers** section of the **Members** list. The **Reviewers** list indicates whether a Reviewer is pending or approved.

4. Select 
### NavigationPath Component:

Options > Approve reviewer
.

To block a Reviewer:

1. Go to the **Reviewers** section of the **Members** list.

2. Select 
### NavigationPath Component:

Options > Block
 to remove a pending Reviewer from the **Reviewers** list and block any future Reviewer requests with the associated email address.

Reviewers have access to certain collaboration features to provide feedback, while Developers and Owners have extended capabilities to manage feedback and troubleshoot reported issues. When a Developer or Reviewer is added to a site, they are granted team-wide access for collaborating on Deploy Previews.

### Guidelines for managing Directory Sync users

Note that Directory Sync requires [Organization SSO](/manage/security/secure-netlify-access/configure-organization-saml-sso/) and requires a Netlify Enterprise plan.

If a team member is provisioned by your organization's [Directory Sync](/manage/security/secure-netlify-access/directory-sync), then keep the following guidelines in mind: 
- Organization Owners can change a SCIM provisioned person's role by [editing their directory group mapping](/manage/security/secure-netlify-access/directory-sync#change-the-user-role-for-a-directory-group).
- We recommend Organization Owners and Identity Provider admins give users the least permissions necessary. 
- Team Owners can upgrade a user's permissions for a specific project, such as an internal tool, by [editing project access](/manage/accounts-and-billing/team-management/manage-project-access#edit-a-person-s-project-access) in the Netlify project dashboard. This overrides the team default role set by SCIM Directory Sync for a specified project.
- A Team Owner can give members provisioned by SCIM access to additional projects not specified in their directory group mapping or the identity provider.
  - These updates will not be visible through the identity provider or Organization Owner's admin dashboard, but can be viewed from the [Netlify team dashboard](/manage/accounts-and-billing/team-management/manage-project-access/#check-a-members-roles-on-a-team) or [project members dashboard](/manage/accounts-and-billing/team-management/manage-project-access/#check-a-members-role-on-a-project).

## Remove a team member

To remove a team member, select 
### NavigationPath Component:

Options > Remove from team
. You can also use this option to remove yourself from a team.

Note that every team must have at least one Owner. As an Owner, you cannot remove or demote yourself unless there is an additional Owner on the team.

## Delete inactive Git Contributors

On the **Members** page for your team, you can access a list of your active and inactive [Git Contributors](/manage/accounts-and-billing/team-management/roles-and-permissions#git-contributor). To remove an inactive Git Contributor, choose the Git Contributor you would like to remove and select 
### NavigationPath Component:

Options > Delete contributor
.

Note that deleting the Git Contributor does not automatically remove the user from the associated Git repository. Unless you remove them from the repository, the user can still trigger a build.

