---
title: "SIEM events"
source: https://developers.notion.com/compliance/siem-events
path: compliance/siem-events
---

A comprehensive list of webhook events available in your SIEM platform once you set up the Notion SIEM connection.

Below is a comprehensive list of webhook events that will be available in your SIEM platform once you set up the Notion SIEM connection. All events available in your SIEM platform will correspond to an audit log event. The glossary will help you understand the specific events that are being tracked and how they relate to your organization's security posture. Use this information to fine-tune your dashboards, alerts, and incident management processes.

## Event types

Events are split into the following categories:

1. **Page events**: Events users take on a single Notion page.
2. **Data source events**: Events about data sources (databases). Note: Some data source operations may emit as `page.*` events for historical reasons.
3. **Workspace events**: Events users take on an entire Notion workspace.
4. **Account events**: Events about accounts of users in the workspace.
5. **Teamspace events**: Events users take on one or more teamspaces.
6. **Form events**: Events about forms in the workspace.

## Page audience

For page events, the page audience describes the visibility level of the target page. The audience captured will be one of the following:

* **Private**: The page is not shared with other users.
* **Internal**: The page is shared with other members of the workspace only.
* **External**: The page is shared with one or more guests outside of the workspace and/or with an integration bot.
* **Public**: The page is shared to the web.

## Teamspace attribution

When available, applicable events include a top-level `team_ids` array containing the IDs of the teamspaces associated with the event. Most attributed events contain one ID; events such as moves and teamspace exports can contain multiple IDs. The field is omitted for events that are not associated with a teamspace or when attribution is unavailable.

***

## SIEM event glossary

### Page events

* **page.archived**: A page was archived.
* **page.button\_automation\_created**: A [button](https://www.notion.so/help/template-buttons) automation was created on a page.
* **page.button\_automation\_updated**: A [button](https://www.notion.so/help/template-buttons) automation was updated on a page.
* **page.comments\_read**: A user viewed comments on a page.
* **page.content\_edited**: The content of an existing page was edited by a user. Page content is also known as a [block](https://www.notion.so/help/what-is-a-block). Content edit events are consolidated into one event every minute while edits are occurring.
* **page.created**: A new page nested under a parent page was created by a user.
* **page.deleted**: A page was deleted by a user. Deleted pages may be restored in the future.
* **page.discussion.comment.created**: A comment on a page was created by a user.
* **page.discussion.comment.deleted**: A comment on a page was deleted by a user.
* **page.discussion.comment.updated**: A comment on a page was edited by a user. Comment edit events are consolidated into one event every minute while edits are occurring.
* **page.exported**: A page was exported to a PDF, HTML, or Markdown file by a user.
* **page.file\_deleted**: A file was deleted from a page by a user.
* **page.file\_downloaded**: A file in a page was downloaded or opened by a user.
* **page.file\_uploaded**: A file was uploaded to a page by a user.
* **page.locked**: A page was locked to prevent further editing.
* **page.meeting\_notes.audio\_recording.downloaded**: A user downloaded an audio recording from an AI Meeting Notes block.
* **page.meeting\_notes.consent.confirmed**: A user confirmed consent to start an AI Meeting Notes transcription.
* **page.moved**: A page was relocated by a user, i.e. the page's parent page updated.
* **page.permanently\_deleted**: A page was permanently deleted from Trash. This can be done by a user, or automatically by Notion after 30 days, or within a [custom time frame](https://www.notion.com/help/custom-data-retention-settings) on Enterprise Plans.
* **page.permissions.group\_role\_added**: A workspace group's page permissions were added, which will allow them to access the page.
* **page.permissions.group\_role\_removed**: A group's page permissions were removed for a page, which will restrict them from having access to the page.
* **page.permissions.group\_role\_updated**: A workspace group's page permissions were updated, changing their type of access.
* **page.permissions.guest\_role\_added**: A guest's page permissions were added, which will allow them to access the page.
* **page.permissions.guest\_role\_removed**: A guest's page permissions were removed, which will restrict them from having access to the page.
* **page.permissions.guest\_role\_updated**: A guest's page permissions were updated, changing their type of access.
* **page.permissions.integration\_role\_added**: A user added an [integration](https://www.notion.so/help/add-and-manage-connections-with-the-api) to a page. Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.integration\_role\_removed**: A user removed the page permissions for an integration (or "connection"), which will restrict the integration from having access to the page. Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.integration\_role\_updated**: A user updated the page permissions of an integration (or "connection"). Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.member\_role\_added**: A member's page permissions were added, which will allow them to access the page.
* **page.permissions.member\_role\_removed**: A member's page permissions were removed, which will restrict them from having access to the page.
* **page.permissions.member\_role\_updated**: A member's page permissions were updated, changing their type of access.
* **page.permissions.shared\_to\_public\_role\_added**: A user enabled sharing a page to the public web.
* **page.permissions.shared\_to\_public\_role\_removed**: A user disabled sharing a page to the public web.
* **page.permissions.shared\_to\_public\_role\_updated**: A user updated the public sharing settings for a page.
* **page.permissions.shared\_with\_email\_domain\_role\_added**: A user granted page access to users with a specific email domain.
* **page.permissions.shared\_with\_email\_domain\_role\_removed**: A user removed page access for users with a specific email domain.
* **page.permissions.space\_role\_added**: Workspace-wide page permissions were added, allowing all workspace members to access the page.
* **page.permissions.space\_role\_removed**: Workspace-wide page permissions were removed, restricting access to the page.
* **page.permissions.space\_role\_updated**: Workspace-wide page permissions were updated, changing the type of access for all workspace members.
* **page.permissions.team\_guest\_role\_added**: A teamspace guest's page permissions were added, allowing them to access the page.
* **page.permissions.team\_guest\_role\_removed**: A teamspace guest's page permissions were removed, restricting them from accessing the page.
* **page.permissions.team\_guest\_role\_updated**: A teamspace guest's page permissions were updated, changing their type of access.
* **page.permissions.team\_owner\_role\_added**: A teamspace owner's page permissions were added, allowing them to access the page.
* **page.permissions.team\_owner\_role\_removed**: A teamspace owner's page permissions were removed, restricting them from accessing the page.
* **page.permissions.team\_owner\_role\_updated**: A teamspace owner's page permissions were updated, changing their type of access.
* **page.permissions.team\_role\_added**: A teamspace's page permissions were added, allowing teamspace members to access the page.
* **page.permissions.team\_role\_removed**: A teamspace's page permissions were removed, restricting teamspace members from accessing the page.
* **page.permissions.team\_role\_updated**: A teamspace's page permissions were updated, changing the type of access for teamspace members.
* **page.properties\_edited**: A user edited a page's property, like a page title or a database property.
* **page.purged**: A page was permanently removed from Trash based on workspace data retention settings.
* **page.recurrence\_automation\_created**: A recurring automation was created on a page.
* **page.recurrence\_automation\_deleted**: A recurring automation was deleted from a page.
* **page.recurrence\_automation\_updated**: A recurring automation was updated on a page.
* **page.restored\_from\_trash**: A user restored a formerly deleted page from Trash.
* **page.suggestion.accepted**: A user accepted a suggested edit on a page.
* **page.suggestion.comment.created**: A user added a comment on a suggested edit.
* **page.suggestion.comment.deleted**: A user deleted a comment on a suggested edit.
* **page.suggestion.comment.updated**: A user updated a comment on a suggested edit.
* **page.suggestion.created**: A user suggested an edit on a page.
* **page.suggestion.rejected**: A user rejected a suggested edit on a page.
* **page.transcription\_block.transcript\_deleted**: A transcript for AI Meeting Notes was permanently deleted based on workspace settings.
* **page.unarchived**: A page was unarchived.
* **page.unlocked**: A page was unlocked to allow editing.
* **page.unverified**: A page's verification was removed.
* **page.verified**: A page was verified.
* **page.viewed**: A user viewed a page.
* **page.viewed.by\_shared\_email\_domain\_user**: A user with an email domain that was granted access to the page viewed it.

### Data source events

* **database.permission.added**: A user added a page-level access rule for a data source in a database.
* **database.permission.removed**: A user removed a page-level access rule for a data source in a database.
* **database.permission.updated**: A user changed a page-level access rule for a data source in a database.
* **database.permissions.can\_create\_pages.group\_disabled**: A group's 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.group\_enabled**: A group's 'can create pages' permission was enabled for a database.
* **database.permissions.can\_create\_pages.member\_disabled**: A member's 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.member\_enabled**: A member's 'can create pages' permission was enabled for a database.
* **database.permissions.can\_create\_pages.space\_disabled**: Workspace-wide 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.space\_enabled**: Workspace-wide 'can create pages' permission was enabled for a database.
* **database.permissions.can\_create\_pages.space\_owner\_disabled**: Workspace owners' 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.space\_owner\_enabled**: Workspace owners' 'can create pages' permission was enabled for a database.
* **database.permissions.can\_create\_pages.team\_disabled**: A teamspace's 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.team\_enabled**: A teamspace's 'can create pages' permission was enabled for a database.
* **database.permissions.can\_create\_pages.team\_owner\_disabled**: Teamspace owners' 'can create pages' permission was disabled for a database.
* **database.permissions.can\_create\_pages.team\_owner\_enabled**: Teamspace owners' 'can create pages' permission was enabled for a database.
* **database.schema\_edited**: A user edited the schema of a database.

### Workspace events

* **integration.created**: A developer created an internal integration and associated it with the workspace.
* **integration.deleted**: An internal integration associated with the workspace was deleted. Deletions can occur in the My Integrations dashboard, or an admin can remove access to an internal integration for all users.
* **integration.management\_permissions.updated**: The list of people, groups, or workspace owners allowed to manage page access for an internal integration was changed.
* **integration.owner\_added**: A workspace member was added as an explicit owner of an internal integration.
* **integration.owner\_break\_glass\_added**: A workspace admin used break-glass access to add themselves as an owner of an internal integration.
* **integration.owner\_removed**: A workspace member was removed as an explicit owner of an internal integration.
* **integration.permission.updated**: An integration's capabilities (reading content, inserting a comment, etc.) were changed.
* **integration.secret\_reset**: An internal integration's installation access token was reset (or "refreshed").
* **integration.settings.updated**: An integration's basic settings, like its name or icon, were changed.
* **workspace.agent.web\_url\_viewed**: An AI agent viewed a web URL.
* **workspace.audit\_log\_exported**: A workspace owner exported the workspace's audit log.
* **workspace.content\_analytics\_exported**: The Content Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics) was exported.
* **workspace.content\_exported**: Workspace content for a page or for the entire workspace was exported by a workspace user.
* **workspace.content\_search\_exported**: The results of a [content search](https://www.notion.so/help/admin-content-search) for a workspace was exported by a workspace owner.
* **workspace.content\_search\_queried**: A workspace owner used the [admin content search](https://www.notion.so/help/admin-content-search) functionality to find workspace content. Content searches can retrieve content from public and private pages.
* **workspace.custom\_agent.created**: A custom agent was created in the workspace.
* **workspace.custom\_agent.published**: A custom agent was published in the workspace.
* **workspace.custom\_agent.setup\_mode\_used**: An action was performed in setup mode for a custom agent in the workspace.
* **workspace.custom\_emoji.created**: A custom emoji was created in the workspace.
* **workspace.custom\_emoji.deleted**: A custom emoji was deleted from the workspace.
* **workspace.custom\_emoji.updated**: A custom emoji was updated in the workspace.
* **workspace.domain\_management.claim\_request\_status\_updated**: The status of a claim and upgrade to Enterprise of a claimable workspace was updated.
* **workspace.domain\_management.deletion\_request\_status\_updated**: The status of workspace deletion of a claimable workspace was updated.
* **workspace.domain\_management.transfer\_request\_status\_updated**: A transfer request for a workspace created by a user with a verified domain was updated. See [domain management](https://www.notion.so/help/domain-management) for more information.
* **workspace.ekm.cmk.rotation.completed**: Customer-managed key (CMK) rotation on WEK was completed.
* **workspace.ekm.dek.rotation.completed**: Data encryption key (DEK) rotation was completed.
* **workspace.ekm.dek.rotation.started**: Data encryption key (DEK) rotation was started.
* **workspace.ekm.wek.generated**: A workspace encryption key (WEK) was generated.
* **workspace.ekm.wek.revoked**: A workspace encryption key (WEK) was revoked.
* **workspace.external\_account\_connected**: A public/external integration was connected to the workspace.
* **workspace.external\_account\_disconnected**: A public/external integration was disconnected from the workspace, or a workspace owner removed access to a public integration for all users in the workspace.
* **workspace.group.created**: A new group was created. A group is a defined collection of workspace members.
* **workspace.group.custom\_agent\_creation\_updated**: The custom agent creation permission for a group was enabled or disabled.
* **workspace.group.deleted**: A group was deleted from the workspace.
* **workspace.group.internal\_integration\_creation\_updated**: A permission group's ability to create internal integrations was updated.
* **workspace.group.permissions.member\_added**: A workspace owner or membership admin added a new member to a group. A group is a defined collection of workspace members.
* **workspace.group.permissions.member\_removed**: A workspace owner or membership admin removed a member from a group.
* **workspace.group.permissions.member\_role\_updated**: A group member's role was updated (Member ↔ Group owner).
* **workspace.group.personal\_access\_token\_creation\_updated**: A permission group's ability to create personal access tokens was updated.
* **workspace.group.renamed**: A group name was changed.
* **workspace.guest\_invite\_request\_resolved**: A guest invite to a page was requested for approval and the workspace owner either approved or denied the request.
* **workspace.guest\_invite\_request.created**: A guest invite request was created, requesting to invite a guest to specific pages.
* **workspace.imports.asana\_data\_fetched**: A Notion admin fetched Asana data on behalf of a workspace user for Asana data importer triage/debugging purposes.
* **workspace.imports.confluence\_data\_fetched**: A Notion admin fetched Confluence data on behalf of a workspace user for Confluence data importer triage/debugging purposes.
* **workspace.imports.monday\_data\_fetched**: A Notion admin fetched Monday.com data on behalf of a workspace user for Monday.com data importer triage/debugging purposes.
* **workspace.integration\_added**: An integration was added to the workspace for the first time. This event will only be emitted the first time an integration is added to a workspace.
* **workspace.integration\_removed**: All bots for a specific public integration were removed from the workspace.
* **workspace.integration\_webhook\_inactivated**: An integration's webhook was inactivated due to repeated delivery failures.
* **workspace.integration\_webhook\_reactivated**: An integration's webhook was reactivated after being inactive.
* **workspace.mcp\_connection.tool\_list\_updated**: The selected tools for a workspace MCP connection were updated.
* **workspace.mcp.allowlist\_disabled**: The MCP allowlist was disabled for the workspace.
* **workspace.mcp.allowlist\_enabled**: The MCP allowlist was enabled for the workspace.
* **workspace.mcp.client\_added**: An MCP client was added to the workspace's allowlist.
* **workspace.mcp.client\_removed**: An MCP client was removed from the workspace's allowlist.
* **workspace.mcp.enterprise\_managed\_connection\_disabled**: Enterprise-managed connections were disabled or removed for the workspace.
* **workspace.mcp.enterprise\_managed\_connection\_enabled**: Enterprise-managed connections were enabled for the workspace.
* **workspace.mcp.enterprise\_managed\_connection\_member\_access\_denied**: A workspace member was denied access to enterprise-managed connections.
* **workspace.mcp.enterprise\_managed\_connection\_member\_access\_restored**: A workspace member's access to enterprise-managed connections was restored.
* **workspace.mcp.enterprise\_managed\_connection\_updated**: Enterprise-managed connection settings were updated for the workspace.
* **workspace.mcp.server\_connected**: An MCP server was connected to the workspace, including via an enterprise-managed connection.
* **workspace.members\_exported**: A list of workspace members was exported.
* **workspace.membership\_request\_resolved**: A membership request from a member to add a new person to the workspace was resolved, i.e. the workspace owner either approved or denied the request.
* **workspace.permissions.guest\_removed**: A guest was removed from the workspace by a workspace owner or membership admin.
* **workspace.permissions.member\_added**: A user accepted an invite to join a new workspace and has been added to the member list.
* **workspace.permissions.member\_invited**: A user was invited to a workspace by a workspace owner or membership admin.
* **workspace.permissions.member\_removed**: A member was removed from the workspace by a workspace owner or membership admin.
* **workspace.permissions.member\_role\_updated**: A member's role in a workspace was updated. Roles include member, membership admin, and workspace owner.
* **workspace.private\_content\_transferred**: The private content of a deprovisioned workspace member was transferred to a new location. Enterprise workspace owners can [transfer content](https://www.notion.so/help/transfer-content-deprovisioned-user) from deprovisioned users.
* **workspace.public\_domain.created**: A public domain was created for the workspace.
* **workspace.public\_domain.deleted**: A public domain was deleted from the workspace.
* **workspace.public\_domain.updated**: A public domain was updated for the workspace.
* **workspace.restricted\_member\_invite\_request\_resolved**: A restricted member invite request was approved or denied by a workspace owner.
* **workspace.saml\_authorization**: A user verified workspace access via SAML SSO.
* **workspace.saml\_sso\_idp\_metadata\_url\_added**: The IdP (Identity Provider) metadata URL was added by a workspace owner.
* **workspace.saml\_sso\_idp\_metadata\_url\_removed**: The IdP (Identity Provider) metadata URL was removed by a workspace owner.
* **workspace.saml\_sso\_idp\_metadata\_url\_updated**: The IdP (Identity Provider) metadata URL was updated by a workspace owner.
* **workspace.saml\_sso\_idp\_metadata\_xml\_added**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was added by a workspace owner.
* **workspace.saml\_sso\_idp\_metadata\_xml\_removed**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was removed by a workspace owner.
* **workspace.saml\_sso\_idp\_metadata\_xml\_updated**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was updated by a workspace owner.
* **workspace.scim\_token\_generated**: A workspace owner generated a SCIM API token.
* **workspace.scim\_token\_revoked**: A workspace owner revoked a SCIM API token.
* **workspace.search\_performed**: A search was performed in the workspace.
* **workspace.settings.agent\_creation\_policy\_updated**: The agent creation policy setting was updated.
* **workspace.settings.agent\_model\_policy\_updated**: The list of AI models an agent is allowed to use was updated. `agent_type` names which allowed model list changed, and the model and provider lists are sent both before and after the change. `allowed_restricted_access_models` runs the other way from the restricted lists: a restricted-access model is off until an admin names it there, so a model entering that list was allowed and a model leaving it was restricted.
* **workspace.settings.ai\_leap\_toggled**: A workspace owner enabled or disabled the Notion AI LEAP (Learning & Early Access Program) setting.
* **workspace.settings.ai\_legal\_terms\_setting\_updated**: A user enabled or disabled Notion AI in the workspace by accepting or revoking AI legal terms.
* **workspace.settings.ai\_meeting\_notes\_availability\_updated**: The AI meeting notes availability setting was updated.
* **workspace.settings.allow\_content\_export\_setting\_updated**: A workspace owner enabled or disabled exporting.
* **workspace.settings.allow\_group\_creation\_setting\_updated**: A user enabled or disabled the ability for non-admin members to create groups.
* **workspace.settings.allow\_guests\_setting\_updated**: A workspace owner enabled or disabled the ability to add guests to the workspace.
* **workspace.settings.allow\_public\_page\_sharing\_setting\_updated**: A workspace owner enabled or disabled public page sharing for the workspace.
* **workspace.settings.allow\_teamspace\_creation\_setting\_updated**: A user enabled or disabled the ability for everyone in the workspace to create a teamspace.
* **workspace.settings.allow\_workspace\_creation\_setting\_updated**: A workspace owner restricted creation of new workspaces by users with the claimed enterprise email domain.
* **workspace.settings.analytics\_tracking\_setting\_updated**: A user enabled or disabled workspace analytics tracking within the workspace.
* **workspace.settings.delete\_from\_trash\_delay**: The [custom data retention](https://www.notion.com/help/custom-data-retention-settings) delete from trash delay setting was updated.
* **workspace.settings.disallow\_webhook\_automation\_action\_toggled**: A workspace owner enabled or disabled the use of webhook automation actions in the workspace.
* **workspace.settings.duplicate\_pages\_to\_workspaces\_setting\_updated**: A workspace owner enabled or disabled moving pages to other workspaces.
* **workspace.settings.email\_domain\_added**: A user added an allowed email domain to the workspace.
* **workspace.settings.email\_domain\_removed**: A user removed an allowed email domain from the workspace.
* **workspace.settings.enable\_saml\_sso\_config\_updated**: An organization owner enabled or disabled SAML.
* **workspace.settings.enforce\_saml\_sso\_config\_updated**: An organization owner enabled or disabled Enforce SAML.
* **workspace.settings.guest\_invite\_request\_setting\_updated**: The guest invite request approval setting was enabled or disabled.
* **workspace.settings.guest\_membership\_request\_setting\_updated**: A user enabled or disabled guest membership requests for the workspace.
* **workspace.settings.hipaa\_compliance\_updated**: A workspace owner enabled or disabled HIPAA compliance by accepting or revoking Notion's Business Associate Agreement.
* **workspace.settings.icon\_updated**: The workspace icon was changed.
* **workspace.settings.integration\_restriction\_settings\_updated**: A workspace owner enabled or disabled integration restrictions.
* **workspace.settings.internal\_integration\_creation\_policy\_updated**: The workspace policy controlling who can create internal integrations was updated.
* **workspace.settings.invite\_link\_reset**: A user reset the workspace invite link.
* **workspace.settings.invite\_link\_setting\_updated**: A user enabled or disabled the workspace invite link.
* **workspace.settings.membership\_request\_setting\_updated**: A user enabled or disabled new workspace membership requests.
* **workspace.settings.name\_updated**: A user updated the workspace's name.
* **workspace.settings.page\_access\_request\_setting\_updated**: A user enabled or disabled page access requests from non-workspace-members.
* **workspace.settings.people\_directory\_setting\_updated**: The people directory visibility setting was enabled or disabled.
* **workspace.settings.people\_hover\_cards\_setting\_updated**: The people hover cards setting was enabled or disabled.
* **workspace.settings.personal\_access\_token\_creation\_policy\_updated**: The workspace policy controlling who can create personal access tokens was updated.
* **workspace.settings.public\_homepage\_added**: A workspace owner set a public homepage.
* **workspace.settings.public\_homepage\_removed**: A workspace owner cleared the public homepage.
* **workspace.settings.public\_homepage\_updated**: A workspace owner changed the public homepage.
* **workspace.settings.public\_pages\_domain\_updated**: The domain for publicly shared pages was updated.
* **workspace.settings.purge\_delay**: The [custom data retention](https://www.notion.com/help/custom-data-retention-settings) purge delay setting was updated.
* **workspace.settings.saml\_automatic\_account\_creation\_setting\_updated**: A workspace owner enabled or disabled automatically creating accounts on SAML sign-in.
* **workspace.settings.sidebar\_editing\_setting\_updated**: A workspace owner enabled or disabled the ability for users to change the workspace sidebar.
* **workspace.teams\_read**: A user viewed the list of teamspaces in the workspace.
* **workspace.user\_analytics\_exported**: The User Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics) was exported.
* **workspace.users\_read**: A user viewed the list of users in the workspace.

### Account events

* **user.deleted**: A user account was deleted. This event will be sent to any workspace with which the account is associated.
* **user.login**: A user logged into an account.
* **user.logout**: A user logged out of an account.
* **user.settings.alias\_added**: A user added an email alias to their account.
* **user.settings.alias\_made\_primary**: A user made an email alias their primary email address.
* **user.settings.alias\_removed**: A user removed an email alias from their account.
* **user.settings.analytics\_tracking\_setting\_updated**: A user updated their analytics tracking setting.
* **user.settings.email\_updated**: The email of a user was changed.
* **user.settings.login\_method.mfa\_backup\_code\_updated**: A user updated their MFA (Multi-Factor Authentication) backup code settings.
* **user.settings.login\_method.mfa\_sms\_updated**: A user updated their MFA (Multi-Factor Authentication) SMS (Short Message Service) settings.
* **user.settings.login\_method.mfa\_totp\_updated**: A user updated their MFA (Multi-Factor Authentication) TOTP (Time-based One-Time Password) settings.
* **user.settings.login\_method.password\_added**: A user added a password to their account for login purposes.
* **user.settings.login\_method.password\_removed**: A user removed a password from their account.
* **user.settings.login\_method.password\_updated**: A user updated their password.
* **user.settings.preferred\_name\_updated**: A user updated their account's preferred name.
* **user.settings.profile\_photo\_updated**: The profile photo of a user was changed.
* **user.settings.support\_access\_granted**: A user's account was granted Notion support access.
* **user.settings.support\_access\_revoked**: A user's account was revoked Notion support access.
* **user.suspended**: An admin suspended a managed user account.
* **user.unsuspended**: An admin unsuspended a managed user account.

### Teamspace events

* **teamspace.archived**: A teamspace owner archived a teamspace.
* **teamspace.created**: A user created a teamspace.
* **teamspace.permissions.custom\_group\_role\_added**: A teamspace owner added custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom\_group\_role\_removed**: A teamspace owner removed custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom\_group\_role\_updated**: A teamspace owner updated custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom\_member\_role\_added**: A teamspace owner added custom page permissions for a specific teamspace member.
* **teamspace.permissions.custom\_member\_role\_removed**: A teamspace owner removed custom page permissions for a specific teamspace member.
* **teamspace.permissions.custom\_member\_role\_updated**: A teamspace owner updated custom page permissions for a specific teamspace member.
* **teamspace.permissions.default\_member\_role\_updated**: The default teamspace page permissions applied to teamspace members was updated.
* **teamspace.permissions.default\_workspace\_role\_added**: A teamspace owner gave page permissions to workspace users in a closed teamspace.
* **teamspace.permissions.default\_workspace\_role\_removed**: A teamspace owner removed page permissions from workspace users in a closed teamspace.
* **teamspace.permissions.default\_workspace\_role\_updated**: A teamspace owner updated the default page permissions for all workspace users in a teamspace.
* **teamspace.permissions.group\_added**: A group was added to a teamspace. A group is a defined collection of users.
* **teamspace.permissions.group\_removed**: A group was removed from the teamspace by a teamspace owner.
* **teamspace.permissions.member\_added**: A user was added to the teamspace. The user either joined an open teamspace or was added by another member. The event payload will specify "as Teamspace owner" if the user was added with teamspace owner privileges.
* **teamspace.permissions.member\_removed**: A teamspace member was removed from the teamspace. Removal can be triggered by a member leaving or being removed by a teamspace owner.
* **teamspace.permissions.member\_role\_updated**: A teamspace member's role was updated. Roles include Teamspace Member and Teamspace Owner.
* **teamspace.restored**: A previously archived teamspace was restored.
* **teamspace.settings.allow\_content\_export\_setting\_updated**: The setting to allow exporting teamspace content was enabled or disabled.
* **teamspace.settings.allow\_guests\_setting\_updated**: A teamspace owner enabled or disabled the ability to add guests (non-members) to a specific teamspace.
* **teamspace.settings.allow\_public\_page\_sharing\_setting\_updated**: The setting to allow publicly sharing a teamspace page was enabled or disabled by a workspace owner.
* **teamspace.settings.allow\_sidebar\_editing\_setting\_updated**: The setting that determines who can edit the sidebar was updated. The setting will indicate if any teamspace member can edit the sidebar or if editing is only available for teamspace owners.
* **teamspace.settings.default\_setting\_updated**: A user enabled or disabled a teamspace as a default teamspace.
* **teamspace.settings.description\_updated**: The teamspace description was updated.
* **teamspace.settings.icon\_updated**: The teamspace icon was changed.
* **teamspace.settings.member\_invitation\_setting\_updated**: A user updated settings for who can invite teamspace members.
* **teamspace.settings.name\_updated**: A user updated the teamspace's name.
* **teamspace.settings.privacy\_type\_updated**: A teamspace owner changed the teamspace privacy type.

### Form events

* **form\_response.created**: A form response was submitted.
* **form.content.updated**: A user updated a form's content.
* **form.created**: A user created a form.
* **form.permissions.shared\_to\_public\_role\_added**: A user enabled public sharing for a form.
* **form.permissions.shared\_to\_public\_role\_removed**: A user disabled public sharing for a form.
* **form.viewed**: A user viewed a form.
