---
title: "SCIM provisioning with Okta"
source: https://docs.pinecone.io/guides/production/configure-single-sign-on/okta-scim-provisioning
path: guides/production/configure-single-sign-on/okta-scim-provisioning
---

Automatically provision members and roles from Okta to Pinecone over SCIM.

Instead of managing members and roles manually in Pinecone, you can have your identity provider (IdP) provision them automatically over SCIM. This page continues [Configure SSO with Okta](/guides/production/configure-single-sign-on/okta) and shows how to set up SCIM provisioning with Okta. These instructions can be adapted for any provider with SCIM 2.0 support.

<Note>SCIM provisioning is available on the Enterprise plan and builds on SAML SSO. Before you begin, [configure SSO with Okta](/guides/production/configure-single-sign-on/okta) and enforce SSO for your organization.</Note>

## How it works

When SCIM provisioning is enabled, your IdP manages organization membership and roles in Pinecone in near real time:

* As members are added, updated, or removed in Okta, those changes sync to Pinecone over SCIM in near real time, not just at login.
* Okta connects to a SCIM endpoint that Pinecone provides, authenticating with a bearer token you generate in the Pinecone console.
* Pinecone reads each member's roles from the SCIM `roles` attribute and sets their organization and project roles to *exactly* those values. Values that don't match a known role are ignored.
* While SCIM is enabled, SCIM is the source of truth for roles: Pinecone no longer applies the roles in a member's SAML login assertion, even though members still sign in through SAML SSO.
* Deactivating or removing a member in Okta removes them from the organization, and clearing a member's roles revokes their access.
* Because membership and roles come entirely from your IdP, while SCIM is enabled you can no longer invite members or edit roles in the Pinecone console or through the Admin API.

<Note>
  Provisioning changes in Okta are typically reflected in Pinecone within a few minutes, but can take up to 30 minutes to fully propagate.
</Note>

<Note>
  SCIM provisioning assigns roles from user attributes only. SCIM group push is not supported. This is similar to [SAML role management](/guides/production/configure-single-sign-on/okta-role-management), except roles are provisioned continuously rather than at each login, and member deprovisioning is handled automatically.
</Note>

<Warning>
  Before you enable SCIM, provision at least one current [organization owner](/guides/organizations/understanding-organizations#organization-roles) with the `pinecone:OrgOwner` role. Pinecone blocks enabling SCIM until a current owner has been provisioned as an owner, so that handing role management to your IdP cannot lock you out.
</Warning>

<Warning>
  SCIM provisioning is not compatible with members who belong to more than one SSO-connected Pinecone organization. If a member is part of multiple SSO-connected organizations, do not provision them through SCIM; manage their roles manually instead.
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
| Control plane editor | `pinecone:project:<projectID>:ControlPlaneEditor` |
| Control plane viewer | `pinecone:project:<projectID>:ControlPlaneViewer` |
| Data plane editor    | `pinecone:project:<projectID>:DataPlaneEditor`    |
| Data plane viewer    | `pinecone:project:<projectID>:DataPlaneViewer`    |

For example, to make a user an organization manager who is also a project owner on one project, send these two values in the `roles` attribute:

```text theme={null}
pinecone:OrgManager
pinecone:project:a2f7dddb-1597-4eff-9f71-535fde243f58:ProjectOwner
```

## 1. Start SCIM setup in Pinecone

<Note>You must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles) on the Enterprise plan, and SSO must be enforced for your organization.</Note>

1. In the Pinecone console, go to [**Settings > Access > Identity provider**](https://app.pinecone.io/organizations/-/settings/access/identity-provider).
2. Confirm that single sign-on shows the **Enforced** status. If it does not, edit your SSO configuration to enforce SSO before continuing.
3. In the **User management** section, select **Manage roles with SCIM provisioning**.
4. In the **Set up SCIM provisioning** dialog, review the instructions and click **Get started**.

## 2. Generate a SCIM token

1. Choose the token's permissions and expiry. By default the token grants all user permissions and expires in 90 days; you can also choose **Token never expires**.
2. Click **Generate token**.
3. Copy the **bearer token**. The **SCIM endpoint** is shown on the next screen of the dialog. You'll add both to Okta in [Step 3](#3-connect-okta-to-the-scim-endpoint).

<Warning>
  The bearer token is shown only once. Copy it before closing the dialog. You can have at most two active tokens per organization; rotate or revoke them later from the **Manage** dialog.
</Warning>

## 3. Connect Okta to the SCIM endpoint

1. In [Okta](https://login.okta.com/), navigate to **Applications > Pinecone > General**.

2. In the **App Settings** section, click **Edit**, set **Provisioning** to **SCIM**, and click **Save**.

3. Open the **Provisioning** tab and click **Configure API Integration**.

4. Select **Enable API Integration** and enter the following:

   * **SCIM connector base URL**: The **SCIM endpoint** you copied in [Step 2](#2-generate-a-scim-token).
   * **Unique identifier field for users**: `userName`.
   * **Authentication Mode**: `HTTP Header`.
   * **Authorization**: The **bearer token** you copied in [Step 2](#2-generate-a-scim-token).

5. Click **Test API Credentials** to verify the connection, then click **Save**.

6. Under **Provisioning > To App**, click **Edit** and enable **Create Users**, **Update User Attributes**, and **Deactivate Users**.

7. Still under **Provisioning > To App**, scroll to **Pinecone Attribute Mappings** and check the source for `userName`. If it's set to `user.login` or an Active Directory attribute, change it to `user.email` and click **Save**.

<Warning>
  The SCIM `userName` must be the same email address your members sign in with through SAML SSO. If your members are sourced from Active Directory or LDAP, `user.login` is often a local domain login such as `user@example.local` rather than an email address. When the two values differ, Pinecone treats the provisioned member and the member who signs in as two different people. The result is duplicate accounts, and sign-in fails with a `jit_disabled` error. Fix the mapping before you enable SCIM in [Step 6](#6-enable-scim-in-pinecone).
</Warning>

<Note>
  If the **Provisioning** tab or **Configure API Integration** button does not appear, SCIM provisioning is not enabled on the app.

  If **Test API Credentials** fails, re-copy the SCIM endpoint and bearer token from Pinecone, and confirm the token has not expired or been revoked.
</Note>

## 4. Send role values to Pinecone

Okta does not send a member's Pinecone roles by default. You define one app attribute per role you want to assign, then map a value to it for the right members. Pinecone reads only each value, so the same approach scales to as many roles as you need.

1. In Okta, go to **Directory > Profile Editor** and open the **Pinecone** app profile.

2. For each role you want to assign, click **Add Attribute** and configure:

   * **Data type**: `string`
   * **External name**: `roles.^[type=='<label>'].value`, where `<label>` is any unique label for the role (for example, `orgOwner` or `projManager`). Pinecone reads only the value, so the label is only used to keep attributes distinct in Okta.
   * **External namespace**: `urn:ietf:params:scim:schemas:core:2.0:User`

3. Go to **Provisioning > To App > Pinecone Attribute Mappings** (or **Mappings** in the Profile Editor) and map each attribute to the role value for the members who should hold it. Set the mapping to apply **on create and update**. Source the value however you manage users, for example:

   * From a custom user profile attribute that holds the `pinecone:*` value.
   * From group membership with an expression such as `isMemberOfGroupName('Pinecone Owners') ? 'pinecone:OrgOwner' : ''`.

4. Click **Preview** for a representative user and confirm the `roles` attribute resolves to the expected `pinecone:*` values (including `pinecone:OrgOwner` for a current owner).

For example, an organization manager who is also a project owner on one project needs two attributes: one mapped to `pinecone:OrgManager` and one mapped to `pinecone:project:<projectID>:ProjectOwner`. Project values include the project's [unique ID](/guides/projects/understanding-projects#project-ids), not its name.

<Note>
  Send roles in the user's `roles` attribute. SCIM group push is not supported.

  Limit synced attributes to those that are used by Pinecone, including `userName`, `roles`, and optionally, `name`. Mapping irrelevant profile attributes (like `addresses`) risks producing a payload that doesn't conform to the SCIM spec and will be rejected with an invalid payload error.
</Note>

## 5. Provision members and verify

1. Assign your members to the Pinecone app in Okta so it pushes them over SCIM. For members who were already assigned, use **Provisioning > To App > Force Sync** or **Apply updates now** so their attributes resync.
2. Confirm the members and roles arrived. In Okta, check **Reports > System Log** (or the app's provisioning activity) for SCIM errors if members don't appear.
3. Verify that at least one current Pinecone [organization owner](/guides/organizations/understanding-organizations#organization-roles) was provisioned with `pinecone:OrgOwner`.

## 6. Enable SCIM in Pinecone

1. Back in the Pinecone **Set up SCIM provisioning** dialog, click **Enable SCIM**. Pinecone verifies that an organization owner has been provisioned with `pinecone:OrgOwner` before activating.
2. If Pinecone blocks activation because no owner is provisioned, return to Okta, assign `pinecone:OrgOwner` to a current owner (see [Step 4](#4-send-role-values-to-pinecone)), let it sync, and click **Enable SCIM** again.

Once enabled, your IdP is the source of truth for membership and roles. Members and their roles sync automatically as you provision them in Okta.

To rotate or revoke tokens or view the SCIM endpoint, select **Manage** next to the SCIM option. To stop provisioning, select **Manage roles in Pinecone** (or **Disable SCIM** from the **Manage** dialog), which revokes all SCIM tokens and reverts to manual role management. Existing role assignments are preserved until you change them.
