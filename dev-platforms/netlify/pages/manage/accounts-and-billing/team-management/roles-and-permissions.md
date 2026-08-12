---
title: "Netlify Team Roles and Permissions"
source: https://docs.netlify.com/manage/accounts-and-billing/team-management/roles-and-permissions.md
path: manage/accounts-and-billing/team-management/roles-and-permissions
---

---
title: "Roles and permissions"
description: "Learn about roles, access, and permissions across the Netlify platform."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Owners can assign roles to individuals invited to a team and manage their access and permissions across the Netlify platform.

## Overview

A role defines a standard set of permissions that a person has by default once they are assigned that role. 

Since Netlify roles are optimized for cross-functional collaboration across the Netlify platform, a role can determine a person's access to different parts of the platform. An Owner can also customize project access for certain roles.

A Team Owner can manage team roles and invite or remove new members from the **Members** page in **Team Settings** unless you've set up [SCIM](/manage/security/secure-netlify-access/directory-sync) to manage access control through an identity provider. Learn more about your options to [manage a team](/manage/accounts-and-billing/team-management/manage-team-members).

To optimize content publishing workflows, a Team Owner, Developer, or Publisher can customize even more granular [editorial permissions](/manage/visual-editor/editorial-permissions/) for Visual Editor.

## Access

Owners can customize project access and Visual Editor access for most types of roles. Other roles have predetermined access that Owners can't modify, such as Billing Admins who have limited access to the Netlify platform beyond reviewing and managing the billing dashboard.

Team Owners can access all settings, web projects (sites/apps), and resources owned by the team. Only Organization Owners can access organization settings for [Enterprise plans](https://www.netlify.com/pricing/?category=enterprise) that have set up an organization.

### Project access

An Owner can choose which projects (sites/apps) people in these roles can access:
  - [Developers](#developer)
  - [Publishers](#publisher)
  - [Internal Builders](#internal-builder)
  - [Reviewers](#reviewer)

The following roles cannot be given granular project access: 
- Git Contributors
- Team Owners 
- Billing Admins

To learn more, check out our docs on [managing project access](/manage/accounts-and-billing/team-management/manage-project-access#overview).

### Note - Git Contributors

Git Contributors have no access to the Netlify platform beyond being able to trigger a deploy and access site preview links that appear in pull/merge requests, Slack, or other places. 

Git Contributors can access Deploy Preview and branch deploy links as long as the links do not require Netlify Team Login, Netlify SSO, or other forms of authentication that a Git Contributor does not have.

### Visual Editor access

By default, all Developers, Publishers, and [Internal Builders](#internal-builder) in a team can access that team's Visual Editor dashboard. Reviewers can access Deploy Preview and branch deploy links from Visual Editor. 

Within Visual Editor workspace, Owners, Developers, and Publishers can customize more granular access to Visual Editor projects, which are sites that have Visual Editor enabled and configured. Learn more about [editorial permissions](/manage/visual-editor/editorial-permissions/) for Visual Editor.

Before a site can be edited with Visual Editor, a Team Owner or Developer must enable Visual Editor for that site and complete any necessary configuration so the site works with Visual Editor.

## Roles and permissions

_Role options vary by [plan](https://www.netlify.com/pricing/#collaborate-across-larger-teams)._

This overview summarizes the permissions for each role. For a description of each role, check out the [roles overview](#roles).

### Standard roles and permissions

<div id="role-table-wrapper">

|                                       | Owner       | Developer | [Internal Builder](#internal-builder) | Git Contributor | Reviewer    |
| ------------------------------------- | :-----------: | :------------: | :-------------: | :---------------: | :-----------: |
| Create projects                          | **&check;** | **&check;**  |   **&check;**\*          |                 |             |
| Trigger builds  (Trigger from Git/deploy from Git)                      | **&check;** | **&check;**  |  **&check;**              | **&check;**     |             |
| Access and edit project configuration    | **&check;** | **&check;**  | Limited              |                 |             |
| Change project visibility (make a project public or private) | **&check;** | **&check;**  |               |                 |             |
| Delete database | **&check;** | | | | |
| Restore backup database | **&check;** | | | | |
| Collaborate using the  Netlify Drawer to share feedback on Deploy Previews and branch deploys | **&check;** | **&check;**  | **&check;**   |                 | **&check;** |
| Legacy plans only: Change levels for project add-ons (formerly called site add-ons)        | **&check;** | **&check;**  |               |                 |             |
| Change&nbsp;team&nbsp;plan            | **&check;** |              | **&check;**   |                 |             |
| Add or remove extra concurrent builds | **&check;** |              |               |                 |             |
| Add or remove members                 | **&check;** |              |               |                 |             |
| Add and approve Reviewers             | **&check;** | **&check;**  |               |                 |             |
| Modify member roles                   | **&check;** |              |               |                 |             |
| Edit team settings                     | **&check;** |              |    |                 |             |
| Deploy to sites from private repos     | **&check;** | **&check;**  | **&check;**                | **&check;**     |             |
| Install and uninstall extensions | **&check;** | | | | | 
| Delete or transfer projects              | **&check;** |              |               |                 |             |
| Delete the team                       | **&check;** |              |               |                 |             |
| Access Deploy Preview and branch deploy links for sharing feedback | **&check;**  | **&check;**   | **&check;**   |      | **&check;** |
| Access Preview Server URLs | **&check;** | **&check;** | | | **&check;** |
| Manage Preview Servers | **&check;** | **&check;** | | | |
| Publish and manage extensions on Netlify as an author | **&check;**   |   |   |      |  |

Notes:
- \* Once someone with an Internal Builder role creates a new project, that person is automatically given a Developer role for that new project. They will still have an Internal Builder role by default for other projects they have access to but didn't create.
- [Billing admins](#billing-admin) can only access the billing dashboard to change the team plan information and modify billing details. Team Owners can also modify and access these billing details.

</div>

### Database access 

Netlify Database is designed to keep your production database secure by limiting what team members and AI agents can access and change in your database.

Learn more about database permissions in our docs on [database access control](/build/data-and-storage/netlify-database/access-control/).

### Preview Server access

Preview Servers provide a live development environment where authenticated collaborators can preview content and code updates in real-time.

**Who can access Preview Server URLs:**
- Owners
- Developers
- Reviewers
- Publishers (Visual Editor role)
- [Internal Builders](#internal-builder)

**Who can manage Preview Servers:**
- Owners
- Developers

**Roles without Preview Server access:**
- Git Contributors
- Billing Admins

### Note - Visual Editor roles and Preview Servers

Publishers and [Internal Builders](#internal-builder) can access Preview Server URLs but cannot manage Preview Servers. The table above shows platform-wide roles; for more details on Publisher and [Internal Builder](#internal-builder) permissions, see [Visual Editor roles and permissions](#visual-editor-roles-and-permissions).

Learn more about [Preview Servers](/manage/preview-servers/overview).

### Visual Editor roles and permissions

These roles can access Visual Editor: 
- Publisher
- [Internal Builder](#internal-builder)
- Developer
- Team Owner
- Reviewer

There are more customizable permissions available in Visual Editor. 

Team Owners, Developers, Publishers, and other users with the **Manage Collaborators** permission can customize editorial permissions, create and manage member groups that can be assigned to projects, and choose who can access a project in Visual Editor workspace. Note that a project is a site that you can edit with Visual Editor. 

Learn more about these options in [Editorial permissions](/manage/visual-editor/editorial-permissions/).

## Roles

When you add a person to your team, you must assign them a role. For some roles, you must also choose which sites they can access.

Netlify team roles include:

- [Owners](/manage/accounts-and-billing/team-management/roles-and-permissions#owner)
- [Developers](/manage/accounts-and-billing/team-management/roles-and-permissions#developer)
- [Publishers](/manage/accounts-and-billing/team-management/roles-and-permissions#publisher)
- [Internal Builders](/manage/accounts-and-billing/team-management/roles-and-permissions#internal-builder)
- [Git Contributors](/manage/accounts-and-billing/team-management/roles-and-permissions#git-contributor)
- [Reviewers](/manage/accounts-and-billing/team-management/roles-and-permissions#reviewer)
- [Billing Admins](/manage/accounts-and-billing/team-management/roles-and-permissions#billing-admin)

### Owner

Owners can access the entire team account and are able to add or remove members, adjust settings and roles, create and delete projects, and more. If user access control is managed by [SCIM](/manage/security/secure-netlify-access/directory-sync) through an identity provider, then an identity provider admin will be able to invite and remove members.

#### Team Owner

Every team must have at least one Owner at all times and can have multiple Owners. Owners cannot remove or demote themselves unless there is at least one additional Owner on the team.

A Team Owner is a paid role on Legacy plans, which means they contribute to your [total member count](https://www.netlify.com/pricing/?category=developer#features-members).

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included starting in the base $20/month plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

#### Organization Owner

If you have an [Enterprise plan](https://www.netlify.com/pricing/?category=enterprise), you have the option of setting up an Organization. Organizations can have multiple teams and are managed by one or more Organization Owner. 

[Organization Owners](/manage/accounts-and-billing/organization-management) have the Team Owner role in all teams by default.

### Developer

### Note - Collaborators are now Developers

As a part of expanding Netlify roles, the role formerly called Collaborator is now called the Developer role. The role retains the same main permissions with some [expanded access and permissions in Visual Editor](/manage/visual-editor/editorial-permissions/). Learn more about this change in the [blog post](https://www.netlify.com/blog/new-roles-for-better-team-management).

Developers can manage site deploys and other site configuration needs.

Team Owners can [change site access](/manage/accounts-and-billing/team-management/manage-team-members#manage-site-member-access) to allow Developers to work on all sites within the team, or only on specific sites. Developers with access to a site can do things like trigger builds, edit site configuration, and more.

Developers can configure a site for use in Visual Editor. They can also edit, publish, and manage project collaborators in Visual Editor. Learn more about what [Developers can do in Visual Editor](/manage/visual-editor/editorial-permissions/#definitions).

Developers can also [approve or block Reviewers](/manage/accounts-and-billing/team-management/manage-team-members#approve-or-block-reviewers) so Reviewers can use the [Netlify Drawer](/deploy/review-deploys/netlify-drawer-for-feedback/overview) to review branch deploys or Deploy Previews.

Although Developers can [remove themselves from a team](/manage/accounts-and-billing/team-management/manage-team-members#remove-a-team-member), they can't remove other members.

Developers are paid roles on Legacy plans. They contribute to your [total member count](https://www.netlify.com/pricing/?category=developer#features-members) and are included on your bill.

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included starting in the base $20/month plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

### Publisher

A Publisher can do everything an [Internal Builder](#internal-builder) can do in Visual Editor but they can also publish content, schedule when to publish content, and manage Visual Editor project collaborators. Learn more about [Publishers](/manage/visual-editor/editorial-permissions/#definitions).

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included starting in the base $20/month plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

### Internal Builder

The Internal Builder role is designed to support common collaboration workflows for people building with AI on teams. 

In the Netlify app (`app.netlify.com`), the Internal Builder role can edit a web project using Agent Runners but cannot access Project configuration and change key settings like environment variables.

The Internal Builder can build using Agent Runners but this role cannot publish to production. For projects connected to a Git provider, the Internal Builder can open a pull request for review from their agent run. This allows other stakeholders to decide when to go live with changes.

If the Internal Builder decides to create a new project, such as for an internal dashboard or tool, they will automatically get a Developer role for that new project. This allows someone to have greater permissions for one project and a default set of collaboration permissions for other projects they did not create.

The Internal Builder role is optimized for these example personas: 
- Marketing team member who needs to build campaign landing pages quickly
- HR team member who wants to build an information site for a company trip to Mexico
- Sales rep building internal tools for their team

#### In the visual editor

In the Visual Editor, the Internal Builder role was previously called the Content Editor role. Internal Builders in the Visual Editor can edit content but they cannot publish content live to your site. Content editing includes drafting and saving text, managing images, managing SEO settings, and customizing layouts. Internal Builders can save a version of their work for review or follow-up with a Publisher. Learn more about [Internal Builders in the Visual Editor](/manage/visual-editor/editorial-permissions/#definitions).

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included starting in the base $20/month plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

### Git Contributor

When a non-team member triggers a build, a Team Owner can choose to add them to the team as a Git Contributor. Git Contributors can trigger builds, deploys, or Deploy Previews through Netlify from a private Git repository. They do not have access to the Netlify app or your team's Netlify workspace.

If you're a Team Owner, you can add new Git Contributors to your team [manually for each deploy request](/deploy/deploy-overview#add-a-non-team-member-as-a-git-contributor), or automatically by [enabling auto-approval](/deploy/deploy-overview#enable-auto-approval-for-deploy-requests) in **Team Settings**.

### Note - Team members are free on the Credit Pro plan

On the Credit Pro plan, team member seats are unlimited and included in your plan at no additional cost. [Learn more about Credit-based pricing plans](/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), or see the [April 2026 pricing update](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026/).

On the Credit Pro plan, Git Contributors are included in your plan at no additional cost. The Members page shows a list of your team's active and inactive Git Contributors.

If you are on a Legacy Pro plan, you will be charged for Git Contributors who have triggered a deploy during your team's billing period. These active Git Contributors also contribute to your [total member count](https://www.netlify.com/pricing/?category=developer#features-members). If a Git Contributor hasn't collaborated on any of your team's sites during a billing period, they will be marked as inactive and you will not be charged for them. If needed, you can [remove inactive Git Contributors](/manage/accounts-and-billing/team-management/manage-team-members#delete-inactive-git-contributors) from your team.

Reference the [Billing FAQ](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans#git-contributors-and-billing) page for Legacy plan details.

### Reviewer

Once a Team Owner or Developer [approves](/manage/accounts-and-billing/team-management/manage-team-members#approve-or-block-reviewers) a Reviewer, that person can access Deploy Preview and branch deploy links across sites in the team so they can [share site feedback on Deploy Previews](/deploy/review-deploys/netlify-drawer-for-feedback/overview) or on [branch deploys](/deploy/review-deploys/netlify-drawer-for-feedback/overview#configure-the-netlify-drawer).

A Team Owner can add an unlimited number of Reviewers [to your team for free](https://www.netlify.com/pricing/?category=developer#features-reviewers). Reviewers do not contribute to your total member count, and are not included on your bill.

Reviewers can also access read-only Deploy Preview and branch deploy links from Visual Editor, as well as [Preview Server](/manage/preview-servers/overview) URLs.

### Note - Reviewers and Preview Servers

Reviewers can access [Preview Server](/manage/preview-servers/overview) URLs to preview content and code updates, but they cannot manage Preview Servers. Preview Server management is restricted to Owners and Developers.

To learn how to give site feedback as a Reviewer, check out our [Reviewers quickstart](/deploy/review-deploys/netlify-drawer-for-feedback/netlify-reviewer-quickstart).

### Billing Admin

> **Pricing Information:** This feature is available on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

Billing Admins can change the team plan and modify billing information, but do not have access to other team or site features.

