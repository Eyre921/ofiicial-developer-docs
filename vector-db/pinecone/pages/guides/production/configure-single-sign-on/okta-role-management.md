---
title: "Manage roles with Okta"
source: https://docs.pinecone.io/guides/production/configure-single-sign-on/okta-role-management
path: guides/production/configure-single-sign-on/okta-role-management
---

Automatically assign Pinecone organization and project roles from SAML attributes with Okta.

Instead of managing roles manually in Pinecone, you can have Pinecone automatically assign organization and project roles from your identity provider (IdP) on each login. This page continues [Configure SSO with Okta](/guides/production/configure-single-sign-on/okta) and shows how to set up SAML role management with Okta. These instructions can be adapted for any provider with SAML 2.0 support.

<Note>SAML role management is available on the Enterprise plan and builds on SAML SSO. Before you begin, [configure SSO with Okta](/guides/production/configure-single-sign-on/okta) and enforce SSO for your organization.</Note>

## How it works

When SAML role management is enabled, Pinecone reconciles each user's roles on every SSO login:

* Pinecone reads the roles your IdP sends in the SAML `roles` attribute.
* It replaces the user's organization and project roles with *exactly* the roles in that attribute. Roles for projects not included in the attribute are removed, and values that don't match a known role are ignored.
* Because roles come entirely from your IdP, while this mode is enabled you can no longer invite members or edit roles in the Pinecone console or through the Admin API, and the SSO **Default role** is not applied.
* To revoke a member's access, remove their roles in your IdP. At their next sign-in, Pinecone clears all of their organization and project roles and blocks the login. Active members are re-authenticated at least every 24 hours, so the change applies within a day.

<Note>
  Because SSO is enforced, deactivating or removing a member in your IdP blocks them from signing in to Pinecone right away, so their access ends immediately. Their role assignments stay in Pinecone until their next sign-in—which a removed member never reaches—so the assignments remain but grant no access on their own. To clear them, or to have Pinecone remove members automatically, use [SCIM provisioning](/guides/production/configure-single-sign-on/okta-scim-provisioning). You can also switch to **Manage roles in Pinecone** to remove the member manually, then switch back.
</Note>

To avoid losing access, configure and verify the `roles` attribute in Okta *before* you enable SAML role management in Pinecone. The steps below are in that order.

<Warning>
  Enabling SAML role management does not validate your IdP configuration, so a user missing an organization role can be locked out on their next login. Before you enable it, verify the `roles` attribute for a current owner (see [Step 2](#2-verify-the-roles-in-the-saml-assertion)).
</Warning>

## Role attribute values

Pinecone reads roles from the `roles` attribute. Each value uses one of the following formats:

* Organization role: `pinecone:<OrgRole>`
* Project role: `pinecone:project:<projectID>:<ProjectRole>`

`<projectID>` is the project's unique ID. To find it, go to the project list in the [Pinecone console](https://app.pinecone.io/organizations/-/projects). For more information, see [Project IDs](/guides/projects/understanding-projects#project-ids).

A user can hold multiple roles by sending multiple values in the `roles` attribute.

### Organization roles

For details on what each [organization role](/guides/organizations/understanding-organizations#organization-roles) grants, see [Understanding organizations](/guides/organizations/understanding-organizations#organization-roles).

| Organization role    | Attribute value            |
| :------------------- | :------------------------- |
| Organization owner   | `pinecone:OrgOwner`        |
| Organization manager | `pinecone:OrgManager`      |
| Organization member  | `pinecone:OrgMember`       |
| Billing admin        | `pinecone:OrgBillingAdmin` |

### Project roles

For details on what each [project role](/guides/projects/understanding-projects#project-roles) grants, see [Understanding projects](/guides/projects/understanding-projects#project-roles).

| Project role         | Attribute value                                   |
| :------------------- | :------------------------------------------------ |
| Project owner        | `pinecone:project:<projectID>:ProjectOwner`       |
| Project manager      | `pinecone:project:<projectID>:ProjectManager`     |
| Project member       | `pinecone:project:<projectID>:ProjectMember`      |
| Project editor       | `pinecone:project:<projectID>:ProjectEditor`      |
| Project viewer       | `pinecone:project:<projectID>:ProjectViewer`      |
| Control plane editor | `pinecone:project:<projectID>:ControlPlaneEditor` |
| Control plane viewer | `pinecone:project:<projectID>:ControlPlaneViewer` |
| Data plane editor    | `pinecone:project:<projectID>:DataPlaneEditor`    |
| Data plane viewer    | `pinecone:project:<projectID>:DataPlaneViewer`    |

For example, to make a user an organization owner who is also an editor on one project, send these two values in the `roles` attribute:

```text theme={null}
pinecone:OrgOwner
pinecone:project:a2f7dddb-1597-4eff-9f71-535fde243f58:ProjectEditor
```

## 1. Send roles from Okta

Configure Okta to send each user's roles in a SAML attribute named `roles`, where each value is one of the [role attribute values](#role-attribute-values) above. You can populate that attribute in a few ways; choose whichever fits how you already manage users in Okta.

<Note>
  In newer versions of Okta, attribute and group statements are configured on the app's **Sign On** tab after the app is created, rather than in the app creation wizard. If you don't see the **Attribute Statements (SAML)** section, expand **Show legacy configuration** within it.
</Note>

### Option A: From a user profile attribute

Use this option to set roles directly on each user's Okta profile.

1. In Okta, go to **Directory > Profile Editor** and edit the **Okta** user profile.
2. Add an attribute named `pineconeRoles` with data type **string array**.
3. For each user, set `pineconeRoles` to their `pinecone:*` values (directly, or through a profile mapping).
4. In **Applications > Pinecone > Sign On**, add an **Attribute Statement**:

   * **Name**: `roles`
   * **Name format**: `Unspecified`
   * **Value**: `user.pineconeRoles`

### Option B: From group membership

Use this option to assign roles by adding users to Okta groups.

1. In Okta, create a group for each Pinecone role you want to assign, naming each group exactly as the role's attribute value (for example, `pinecone:OrgOwner` or `pinecone:project:<projectID>:ProjectEditor`), and add the appropriate users to each group.
2. In **Applications > Pinecone > Sign On**, send those group names in the `roles` attribute using either:

   * A **Group Attribute Statement** with **Name** `roles`, **Name format** `Unspecified`, and **Filter** **Starts with** `pinecone:`.
   * Or an **Attribute Statement** with **Name** `roles` and the expression `user.getGroups({'group.profile.name': 'pinecone:', 'operator': 'STARTS_WITH'}).![profile.name]`.

<Note>
  The `user.getGroups(...).![profile.name]` expression is for an app-level attribute statement on the **Sign On** tab, and it returns every matching group, so no `limit` argument is required. (Only the `Groups.startsWith`, `Groups.endsWith`, and `Groups.contains` functions require a `limit`.) If you configure this claim on a custom authorization server instead, use the `.![name]` projection.
</Note>

Any other approach works as well, as long as the `roles` attribute resolves to the role attribute values.

## 2. Verify the roles in the SAML assertion

Before you hand role management to Okta, confirm the `roles` attribute contains what you expect.

1. In **Applications > Pinecone > Sign On**, click **Preview the SAML Assertion**.
2. Select a user who should be an organization owner and generate the preview.
3. Confirm the assertion includes a `roles` attribute containing `pinecone:OrgOwner` (and any project roles you assigned).

<Warning>
  If no current organization owner's preview includes `pinecone:OrgOwner`, fix your Okta configuration before continuing. Enabling SAML role management without a provisioned owner can lock your organization out of role management. If the `roles` attribute is empty or missing, re-check your attribute statement expression and projection before continuing, as a malformed expression returns no roles rather than an error.
</Warning>

## 3. Enable SAML role management in Pinecone

<Note>You must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles) on the Enterprise plan, and SSO must be enforced for your organization.</Note>

1. In the Pinecone console, go to [**Settings > Access > Identity provider**](https://app.pinecone.io/organizations/-/settings/access/identity-provider).
2. Confirm that single sign-on shows the **Enforced** status. If it does not, edit your SSO configuration to enforce SSO before continuing.
3. In the **User management** section, select **Manage roles with SAML attributes**.
4. In the **Enable SAML role management** dialog, review the **Before you enable** prerequisites, then click **Enable SAML role management**.

Role assignment now comes entirely from your IdP. Roles update at the member's next SSO login. Since SAML sessions re-authenticate at least every 24 hours, an active user's role changes apply within 24 hours. Default role assignments configured during SSO setup no longer apply.

To stop syncing roles from your IdP, return to **Settings > Access > Identity provider** and select **Manage roles in Pinecone**. Existing roles are preserved, and you can edit them again in the console.
