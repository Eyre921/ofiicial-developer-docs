---
title: "Audit log events"
source: https://developers.notion.com/compliance/audit-log-events
path: compliance/audit-log-events
---

A comprehensive list of events tracked in the Notion audit log for compliance and security monitoring.

## Event types

Events are split into the following categories:

1. **Page events**: Events users take on a single Notion page.
2. **Data source events**: Events about data sources (databases).
3. **Workspace events**: Events users take on an entire Notion workspace.
4. **Account events**: Events about accounts of users in the workspace.
5. **Teamspace events**: Events users take on one or more teamspaces.
6. **Form events**: Events about forms in the workspace.
7. **Organization events**: Events about organization-level settings.

***

## Page events

* **AI Meeting Notes audio recording downloaded**: That a meeting notes audio recording was downloaded.
* **AI Meeting Notes consent confirmed**: That meeting notes consent was confirmed.
* **Automation created**: That an automation was created.
* **Automation deleted**: That an automation was deleted from a page.
* **Automation edited**: That a user edited an automation.
* **Comment added**: That a discussion comment was created on a page.
* **Comment deleted**: That a discussion comment was deleted from a page.
* **Comment updated**: That a user edited a comment.
* **Email domain permission on page changed**: That a user granted page access to users with a specific email domain.
* **File deleted**: That a file was deleted from a page.
* **File downloaded**: That a user opened or downloaded a file from a certain page.
* **File uploaded**: That a file was uploaded.
* **Page archived**: That a page was archived.
* **Page comments read**: That comments on a page were read.
* **Page created**: That a user created a new page nested under another page.
* **Page deleted from Trash**: That a page was permanently deleted.
* **Page edited**: That a user edited the content of a page.
* **Page exported**: That a user exported a page.
* **Page lock status changed**: That a page's lock status was updated.
* **Page moved**: That a user moved a page.
* **Page moved to Trash**: That a user moved a page to Trash.
* **Page permanently deleted**: That a page was permanently removed from Trash. This can be done by a user, but it can also be done automatically by Notion after 30 days, or within a [custom time frame](https://www.notion.com/help/custom-data-retention-settings) on Enterprise Plans.
* **Page permission updated**: That a member or guest's page permissions were updated.
* **Page properties edited**: That a user edited a page's property, like a page title or a database property.
* **Page restored**: That a user restored a formerly deleted page from Trash.
* **Page shared to web**: That a user enabled sharing (or disabled sharing) a page to the web.
* **Page unarchived**: That a page was unarchived.
* **Page verification status changed**: That a page's verification status was updated.
* **Page viewed**: That a user viewed a page.
* **Page viewed by user on shared email domain**: That a user with an email domain that was granted access viewed a page.
* **Private content transferred**: That the private pages of a user who left the workspace were transferred to a current user. Learn more [here](https://www.notion.so/help/transfer-content-deprovisioned-user).
* **Suggestion accepted**: That a suggestion was accepted on a page.
* **Suggestion added**: That a suggestion was created on a page.
* **Suggestion comment added**: That a comment was created on a suggestion.
* **Suggestion comment deleted**: That a comment was deleted from a suggestion.
* **Suggestion comment updated**: That a user updated a comment on a suggested edit in a page.
* **Suggestion rejected**: That a suggestion was rejected on a page.
* **Transcript deleted from transcription block**: That a transcription block's transcript was deleted.

***

## Data source events

* **Data source created**: That a collection was created.
* **Data source deleted from Trash**: That a collection was permanently deleted.
* **Data source moved**: That a collection was moved.
* **Data source moved to Trash**: That a collection was deleted.
* **Data source page-level access rule updated**: That a collection's permissions were updated.
* **Data source permanently deleted**: That a collection was purged.
* **Data source restored from Trash**: That a collection was restored.
* **Database can create pages permission was updated**: That a database's can create pages permission was updated.
* **Database schema edited**: That a database schema was edited.

***

## Workspace events

* **A managed user was logged out by an admin**: That an admin has logged out a single managed user account.
* **A managed user’s password was cleared by an admin**: That an admin has cleared a single managed user account's password.
* **Ability for managed users to edit their profile information updated**: That the ability for managed users to edit their profile information was updated.
* **Ability for managed users to grant support access updated**: That the ability for managed users to grant support access was updated.
* **Ability for managed users to join external workspaces updated**: That the ability for managed users to join external workspaces was updated.
* **Added allowed email domain**: That a user added an allowed email domain to the workspace.
* **Admin added themselves as integration owner**: That a workspace admin used admin privileges to add themselves as an integration owner.
* **Agent creation settings updated**: That the custom agent creation policy was updated.
* **Agent viewed web URL**: That an AI agent viewed a web URL.
* **AI LEAP (Learning & Early Access Program) toggled**: That the AI LEAP (Learning & Early Access Program) setting was toggled.
* **AI Meeting Notes availability updated**: That the AI meeting notes availability setting was updated.
* **All managed users logged out**: That an admin has logged out every managed user account.
* **All managed users’ passwords cleared**: That an admin has cleared all managed user accounts' passwords.
* **Asana data fetched**: That a Notion admin fetched Asana data on behalf of a workspace user for Asana data importer triage/debugging.
* **Audit Log exported**: That the audit log was exported.
* **Auto-create accounts on sign-in toggled**: That a workspace owner has enabled automatically creating accounts on sign-in.
* **Claimable workspace deletion status change**: That the status of workspace deletion of a claimable workspace has changed.
* **Claimable workspace transfer status change**: That the status of ownership transfer on a claimable workspace has changed.
* **Claimable workspace upgrade status change**: That the status of a claim and upgrade to Enterprise of a claimable workspace has changed.
* **CMK rotation on WEK completed**: That customer-managed key rotation was completed.
* **Confluence data fetched**: That a Notion admin fetched Confluence data on behalf of a workspace user for Confluence data importer triage/debugging.
* **Content Analytics exported**: That a user exported the Content Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics).
* **Content search queried**: That a workspace owner has used the [content search](https://www.notion.so/help/admin-content-search) functionality to find workspace content.
* **Content search results exported**: That a workspace owner has exported the results from a [content search](https://www.notion.so/help/admin-content-search) query.
* **Custom agent created**: That a custom agent was created.
* **Custom agent creation setting updated**: That a group's custom agent creation setting was updated.
* **Custom agent performed action in setup mode**: That an action was performed in setup mode for a custom agent in the workspace.
* **Custom agent published**: That a custom agent was published.
* **Custom emoji created**: That a custom emoji was created.
* **Custom emoji deleted**: That a custom emoji was deleted.
* **Custom emoji updated**: That a custom emoji was updated.
* **DEK rotation completed**: That data encryption key rotation was completed.
* **DEK rotation started**: That data encryption key rotation was started.
* **Delete from Trash delay updated**: That the [custom data retention](https://www.notion.com/help/custom-data-retention-settings) delete from trash delay setting was updated.
* **Disable guests toggled**: That a workspace owner has enabled or disabled the ability to add guests to a workspace.
* **Disable teamspace guests toggled**: That the disable team guests setting was toggled.
* **Export toggled**: That a workspace owner has disabled or enabled exporting.
* **External AI tool name changed**: That an external agent's display name was changed.
* **External membership requests toggled**: That external membership requests for the workspace were enabled or disabled.
* **External/Public integration connected**: That a public/external integration was connected to the workspace.
* **External/Public integration disconnected**: That a public/external integration was disconnected from the workspace, or a workspace owner removed access to a public integration for all users.
* **Group created**: That a workspace group was created.
* **Group creation setting updated**: That a user enabled or disabled the ability for non-admin members to create groups.
* **Group deleted**: That a workspace group was deleted.
* **Group member role updated**: That a workspace group member's role was updated.
* **Group renamed**: That a workspace group was renamed.
* **Guest invite request created**: That a guest invite request was created.
* **Guest invite request resolved**: That a guest invite to a page was requested for approval and the workspace owner either approved or denied the request.
* **Guest invite requests toggled**: That the guest invite request approval setting was enabled or disabled.
* **Guest membership requests toggled**: That guest membership requests for the workspace were enabled or disabled.
* **Guest removed**: That a guest has been removed from a workspace.
* **HIPAA Compliance updated for workspace.**: That a workspace owner has enabled or disabled HIPAA compliance by accepting or revoking Notion's Business Associate Agreement.
* **IDP metadata URL updated**: That a workspace owner has set or updated the IdP metadata URL.
* **IDP metadata XML removed**: That a workspace owner has removed IdP metadata XML.
* **IDP metadata XML updated**: That a workspace owner has updated the IdP metadata XML.
* **Integration added to approved connections**: That an integration was added to the workspace's list of approved connections.
* **Integration added to workspace**: That a new integration has been added to a workspace.
* **Integration creation settings updated**: That the internal integration creation policy was updated.
* **Integration installation toggled**: That a workspace owner has disabled or enabled integration restrictions.
* **Integration owner added**: That an owner was added to an internal integration.
* **Integration owner removed**: That an owner was removed from an internal integration.
* **Integration page access permissions updated**: That the list of people or groups allowed to manage page access for an integration was updated.
* **Integration permissions updated**: That an integration's capabilities (reading content, inserting a comment, etc.) have been changed.
* **Integration removed from approved connections**: That an integration was removed from the workspace's list of approved connections.
* **Integration removed from workspace**: That an integration has been deleted.
* **Integration secret reset**: That an integration's installation access token has been refreshed.
* **Integration settings updated**: That an integration's basic settings, like its name or icon, have been changed.
* **Integration webhook subscription failing**: That an integration's webhook was inactivated due to repeated delivery failures.
* **Integration webhook subscription restored**: That an integration's webhook was reactivated after being inactive.
* **Internal integration creation setting updated**: That a group's internal integration creation setting was updated.
* **Invite link reset**: That a user has reset an invite link.
* **Invite link toggled**: That a user either enabled or disabled the invite link.
* **MCP allowlist disabled**: That the MCP allowlist was disabled.
* **MCP allowlist enabled**: That the MCP allowlist was enabled.
* **MCP client added to allowlist**: That an MCP client was added to the allowlist.
* **MCP client removed from allowlist**: That an MCP client was removed from the allowlist.
* **MCP server connected**: That an MCP server was connected to the workspace.
* **Member added to group**: That a workspace owner or membership admin has added a user to a group.
* **Member invited**: That a workspace owner or Membership admin invited a user to the workspace. The new user's role will be specified as `Workspace owner` if they are invited as a workspace owner, or as `Membership admin` if they are invited as a membership admin.
* **Member joined**: That a user has joined the workspace.
* **Member removed**: That a workspace owner or membership admin has removed a user from the workspace.
* **Member removed from group**: That a workspace owner or membership admin has removed a user from a group.
* **Member role updated**: That a workspace owner has updated a user's role.
* **Membership request resolved**: That a user has resolved a workspace membership request.
* **Membership requests toggled**: That a user has enabled or disabled new workspace membership requests.
* **Monday.com data fetched**: That a Notion admin fetched Monday.com data on behalf of a workspace user for Monday.com data importer triage/debugging.
* **Notion AI toggled for workspace.**: That a user has enabled or disabled Notion AI in a workspace.
* **Page access requests toggled**: That a user has enabled or disabled page access requests from non-workspace-members.
* **Pages to other workspaces toggled**: That a workspace owner has either disabled or enabled moving pages to other workspaces.
* **People cards toggled**: That the people hover card setting was toggled.
* **People directory toggled**: That the people directory setting was toggled.
* **Permanently delete delay updated**: That the [custom data retention](https://www.notion.com/help/custom-data-retention-settings) purge delay setting was updated.
* **Personal access token creation setting updated**: That a group's personal access token creation setting was updated.
* **Personal access token creation settings updated**: That the personal access token creation policy was updated.
* **Public domain created**: That a public domain was created for the workspace.
* **Public domain deleted**: That a public domain was deleted from the workspace.
* **Public domain updated**: That a public domain was updated for the workspace.
* **Public home page link cleared**: That a workspace owner has cleared public home page.
* **Public home page set**: That a workspace owner has changed public home page.
* **Public page sharing toggled**: That a workspace owner has switched public page sharing on/off.
* **Removed allowed email domain**: That a user removed an allowed email domain from a workspace.
* **Restricted member invite request resolved**: That a restricted member invite request was resolved.
* **SAML authorization for workspace**: That a user was authorized via SAML.
* **SAML enable setting toggled**: That an organization owner has disabled or enabled SAML.
* **SAML enforce setting toggled**: That an organization owner has disabled or enabled Enforce SAML.
* **SCIM token generated**: That a workspace owner generated a SCIM API token.
* **SCIM token revoked**: That a workspace owner revoked a SCIM API token.
* **Search performed**: That a search was performed in the workspace.
* **Session duration for managed users updated**: That the session duration for managed users was updated.
* **Teamspace content exported**: That a user has exported content from specific teamspaces in the workspace.
* **Temporary member expiry date updated**: That a workspace owner or admin updated a temporary member's expiry date.
* **Toggled ability for users to use ‘Send webhook’ action in automations**: That a workspace owner has enabled or disabled the ability for users to use 'Send webhook' action in automations.
* **User Analytics exported**: That a user exported the User Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics).
* **WEK generated**: That a workspace encryption key was generated.
* **WEK revoked**: That a workspace encryption key was revoked.
* **Workspace analytics tracking toggled**: That a user enabled or disabled workspace analytics within the workspace.
* **Workspace consolidation completed**: That the source or target workspace has finished consolidation.
* **Workspace consolidation failed**: That workspace consolidation has failed for the source or target workspace.
* **Workspace consolidation started**: That a Notion employee has initiated workspace consolidation from this source or to this target workspace.
* **Workspace content exported**: That a user has exported content from a page or the entire workspace.
* **Workspace creation setting updated**: That a workspace owner has restricted creation of new workspaces by users with the claimed enterprise email domain.
* **Workspace domain changed**: That the domain of a workspace is changed.
* **Workspace icon changed**: That the workspace icon was changed.
* **Workspace members exported**: That workspace members were exported.
* **Workspace name changed**: That a user updated the workspace's name.
* **Workspace sidebar editing toggled**: That a workspace owner has enabled or disabled the ability for users to change the Workspace sidebar.
* **Workspace teams read**: That workspace teams were read.
* **Workspace users read**: That workspace users were read.

***

## Account events

* **Email changed**: That the email of a user was changed.
* **Granted support access**: That a user's account was granted Notion support access.
* **Login**: When and from where a user has logged in.
* **Logout**: That a user logged out.
* **MFA backup code toggled**: That a user updated their MFA backup code settings.
* **MFA SMS toggled**: That a user updated their MFA via SMS text messages settings. Learn more [here](https://www.notion.so/help/two-step-verification).
* **MFA TOTP toggled**: That a user updated their MFA via a TOTP (time-sensitive one time passcode) app. Learn more [here](https://www.notion.so/help/two-step-verification).
* **Name changed**: That a user has updated their account's preferred name.
* **Password changed**: That a user changed their password.
* **Password cleared**: That a user cleared their password.
* **Password set**: That a user created a password.
* **Picture changed**: That the profile photo of the user was changed.
* **Revoked support access**: That a user's account was revoked Notion support access.
* **User alias added**: That a user added an email alias.
* **User alias made primary**: That a user made an email alias primary.
* **User alias removed**: That a user removed an email alias.
* **User analytics tracking toggled**: That a user updated their analytics tracking setting.
* **User deleted**: That a specific user account has been deleted.
* **User reactivated**: That an admin has unsuspended a managed user account.
* **User suspended**: That an admin has suspended a managed user account.

***

## Teamspace events

* **Custom permissions updated for a group in the teamspace**: That a teamspace owner modified access to a group. Learn more [here](https://www.notion.so/help/guides/grant-access-teamspaces).
* **Custom permissions updated for a member in the teamspace**: That a teamspace owner modified access to a teamspace member. Learn more [here](https://www.notion.so/help/guides/grant-access-teamspaces).
* **Enabled teamspaces**: That a user has enabled the teamspaces feature on a workspace.
* **Everyone in workspace default page permission updated**: That the default page permissions of everyone at workspace have been changed.
* **Group added to teamspace**: That a user added a permission group to the teamspace.
* **Group removed from teamspace**: That a teamspace owner has removed a permission group from the teamspace.
* **Member added to teamspace**: That a user added another user to the teamspace. Will specify "as Teamspace owner" if user is invited as a teamspace owner.
* **Member joined teamspace**: That a user joined an open teamspace.
* **Member left teamspace**: That a user left a teamspace.
* **Member removed from teamspace**: That a teamspace owner has removed a teamspace member from the teamspace.
* **Member teamspace role updated**: That a user has updated a teamspace member's role in the teamspace.
* **Teamspace archived**: That a teamspace owner archived a teamspace.
* **Teamspace created**: That a user created the teamspace.
* **Teamspace creation setting toggled**: That a user has enabled or disabled the ability for everyone in the workspace to create a teamspace.
* **Teamspace default toggled**: That a user enabled or disabled a teamspace as a default teamspace.
* **Teamspace description changed**: That the teamspace description has been changed.
* **Teamspace disable guests toggled**: That a teamspace owner has enabled or disabled the ability to add guests to a teamspace.
* **Teamspace export toggled**: That a teamspace owner has disabled or enabled exporting for a teamspace.
* **Teamspace Guests default permission updated**: That the default page permissions of teamspace guests have been changed.
* **Teamspace icon changed**: That the teamspace icon has been changed.
* **Teamspace invite access changed**: That a user has updated settings for who can invite teamspace members.
* **Teamspace Members default permission updated**: That the default page permissions of teamspace members have been changed.
* **Teamspace name changed**: That a user updated the teamspace's name.
* **Teamspace privacy type changed**: That a teamspace owner has changed the teamspace privacy type.
* **Teamspace public page sharing toggled**: That a teamspace owner has switched public page sharing on/off for a teamspace.
* **Teamspace restored**: That a teamspace was restored.
* **Teamspace sidebar editing toggled**: That a teamspace owner has enabled or disabled the ability for users to change the teamspace sidebar section.

***

## Form events

* **Form created**: That a user created a form.
* **Form edited**: That a user updated a form's content.
* **Form permission updated**: That a form's permissions were updated.
* **Form response created**: That a form response was submitted.
* **Form viewed**: That a form was viewed.

***

## Organization events

* **“Allow access to webhooks in database automations and buttons” toggled for the organization**: That the webhook automation action setting was toggled for an organization.
* **“Allow any user to request to be added as a member of the workspace” toggled for the organization**: That the "Allow any user to request to be added as a member of the workspace" setting was toggled for an organization.
* **“Allow members to request adding other members” toggled for the organization**: That the "Allow members to request adding other members" setting was toggled for an organization.
* **“Allow page access requests from non-members” toggled for the organization**: That the "Allow page access requests from non-members" setting was toggled for an organization.
* **“Allow page guests to request to be added as members to the workspace” toggled for the organization**: That the "Allow page guests to request to be added as members to the workspace" setting was toggled for an organization.
* **“Disable export” toggled for the organization**: That the disable export setting was toggled for an organization.
* **”Guest can create private pages” toggled for the organization**: That the guest private page creation setting was toggled for an organization.
* **“People cards” toggled for the organization**: That the people hover card setting was toggled for an organization.
* **“People directory” toggled for the organization**: That the people directory setting was toggled for an organization.
* **“Workspace support access consent” toggled for the organization**: That the workspace support access consent setting was toggled for an organization.
* **A managed user was logged out by an admin**: That an admin has logged out a single managed user account in the organization.
* **A managed user’s password was cleared by an admin**: That an admin has cleared a single managed user account's password in the organization.
* **Ability for managed users to edit their profile information updated**: That the ability for managed users to edit their profile information was updated for an organization.
* **Ability for managed users to grant support access updated**: That the ability for managed users to grant support access was updated for an organization.
* **Ability for managed users to join external workspaces updated**: That the ability for managed users to join external workspaces was updated for an organization.
* **AI toggled for the organization**: That the AI feature setting was toggled for an organization.
* **All managed users logged out**: That an admin has logged out every managed user account in the organization.
* **All managed users’ passwords cleared**: That an admin has cleared all managed user accounts' passwords in the organization.
* **Auto-create accounts on sign-in toggled**: That automatic account creation on sign-in was toggled for an organization.
* **Custom admin role assigned**: That a custom admin role was assigned to a member.
* **Custom admin role created**: That a custom admin role was created.
* **Custom admin role deleted**: That a custom admin role was deleted.
* **Custom admin role revoked**: That a custom admin role was revoked from a member.
* **Custom admin role updated**: That a custom admin role was edited.
* **Default new workspace region updated**: That the workspace region was updated for managed users.
* **Disable duplicating pages to other workspaces toggled for the organization**: That the disable duplicating pages to other workspaces setting was toggled for an organization.
* **Disable guests toggled for the organization**: That the disable guests setting was toggled for an organization.
* **Disable publishing sites and forms toggled for the organization**: That the disable publishing sites and forms setting was toggled for an organization.
* **IDP metadata URL updated**: That the IdP (Identity Provider) metadata URL was updated for an organization.
* **IDP metadata XML removed**: That the IdP (Identity Provider) metadata XML was removed for an organization.
* **IDP metadata XML updated**: That the IdP (Identity Provider) metadata XML was updated for an organization.
* **Integration installation toggled for organization**: That the integration installation restriction was updated for an organization.
* **IP allowlist created**: That an IP restriction was created for an organization.
* **IP allowlist deleted**: That an IP restriction was deleted from an organization.
* **IP allowlist updated**: That an IP restriction was updated for an organization.
* **IP restriction enforcement mode changed**: That the IP restriction enforcement mode was changed for an organization.
* **IP restrictions toggled**: That IP restriction was enabled or disabled for an organization.
* **Legal hold content summary exported**: That a legal hold content summary was exported.
* **Legal hold created for organization**: That a legal hold was created.
* **Legal hold export content created**: That a legal hold export content was created.
* **Legal hold member added**: That a member was added to a legal hold.
* **Legal hold member removed**: That a member was removed from a legal hold.
* **Legal hold name updated for organization**: That a legal hold's name was updated.
* **Legal hold released for organization**: That a legal hold was released.
* **Organization audit log exported**: That an organization's audit log was exported.
* **Organization created**: That an organization was created.
* **Organization name changed**: That an organization's name was changed.
* **Organization owner added**: That an owner was added to an organization.
* **Organization owner removed**: That an owner was removed from an organization.
* **Organization token created**: That an organization token was created.
* **Organization token updated**: That an organization token was updated.
* **Organization unverified an email domain**: That an email domain was unverified for an organization.
* **Organization verified an email domain**: That an email domain was verified for an organization.
* **Organization’s request to claim a domain had its status updated**: That an organization's request to claim a domain had its status updated.
* **Page view analytics toggled for the organization**: That the page view analytics setting was toggled for an organization.
* **Session duration for managed users updated**: That the session duration for managed users was updated for an organization.
* **Toggled enable SAML for all spaces in the organization**: That an organization owner has disabled or enabled SAML for all spaces in the organization.
* **Toggled enforce SAML for all spaces in the organization**: That an organization owner has disabled or enabled Enforce SAML for all spaces in the organization.
* **Toggled require SAML authorization for workspace access**: That the required auth step setting was updated for an organization.
* **Workspace added to organization**: That a workspace was added to an organization.
* **Workspace creation setting updated**: That the workspace creation setting was updated for an organization.
* **Workspace removed from organization**: That a workspace was removed from an organization.
