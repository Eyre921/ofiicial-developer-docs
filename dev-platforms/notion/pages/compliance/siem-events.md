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
* **page.button_automation_created**: A [button](https://www.notion.so/help/template-buttons) automation was created on a page.
* **page.button_automation_updated**: A [button](https://www.notion.so/help/template-buttons) automation was updated on a page.
* **page.comments_read**: A user viewed comments on a page.
* **page.content_edited**: The content of an existing page was edited by a user. Page content is also known as a [block](https://www.notion.so/help/what-is-a-block). Content edit events are consolidated into one event every minute while edits are occurring.
* **page.created**: A new page nested under a parent page was created by a user.
* **page.deleted**: A page was deleted by a user. Deleted pages may be restored in the future.
* **page.discussion.comment.created**: A comment on a page was created by a user.
* **page.discussion.comment.deleted**: A comment on a page was deleted by a user.
* **page.discussion.comment.updated**: A comment on a page was edited by a user. Comment edit events are consolidated into one event every minute while edits are occurring.
* **page.exported**: A page was exported to a PDF, HTML, or Markdown file by a user.
* **page.file_deleted**: A file was deleted from a page by a user.
* **page.file_downloaded**: A file in a page was downloaded or opened by a user.
* **page.file_uploaded**: A file was uploaded to a page by a user.
* **page.locked**: A page was locked to prevent further editing.
* **page.meeting_notes.audio_recording.downloaded**: A user downloaded an audio recording from an AI Meeting Notes block.
* **page.meeting_notes.consent.confirmed**: A user confirmed consent to start an AI Meeting Notes transcription.
* **page.moved**: A page was relocated by a user, i.e. the page's parent page updated.
* **page.permanently_deleted**: A page was permanently deleted from Trash. This can be done by a user, or automatically by Notion after 30 days, or within a [custom time frame](https://www.notion.com/help/custom-data-retention-settings) on Enterprise Plans.
* **page.permissions.group_role_added**: A workspace group's page permissions were added, which will allow them to access the page.
* **page.permissions.group_role_removed**: A group's page permissions were removed for a page, which will restrict them from having access to the page.
* **page.permissions.group_role_updated**: A workspace group's page permissions were updated, changing their type of access.
* **page.permissions.guest_role_added**: A guest's page permissions were added, which will allow them to access the page.
* **page.permissions.guest_role_removed**: A guest's page permissions were removed, which will restrict them from having access to the page.
* **page.permissions.guest_role_updated**: A guest's page permissions were updated, changing their type of access.
* **page.permissions.integration_role_added**: A user added an [integration](https://www.notion.so/help/add-and-manage-connections-with-the-api) to a page. Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.integration_role_removed**: A user removed the page permissions for an integration (or "connection"), which will restrict the integration from having access to the page. Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.integration_role_updated**: A user updated the page permissions of an integration (or "connection"). Integrations of any type — internal or public/external — will trigger this event.
* **page.permissions.member_role_added**: A member's page permissions were added, which will allow them to access the page.
* **page.permissions.member_role_removed**: A member's page permissions were removed, which will restrict them from having access to the page.
* **page.permissions.member_role_updated**: A member's page permissions were updated, changing their type of access.
* **page.permissions.shared_to_public_role_added**: A user enabled sharing a page to the public web.
* **page.permissions.shared_to_public_role_removed**: A user disabled sharing a page to the public web.
* **page.permissions.shared_to_public_role_updated**: A user updated the public sharing settings for a page.
* **page.permissions.shared_with_email_domain_role_added**: A user granted page access to users with a specific email domain.
* **page.permissions.shared_with_email_domain_role_removed**: A user removed page access for users with a specific email domain.
* **page.permissions.space_role_added**: Workspace-wide page permissions were added, allowing all workspace members to access the page.
* **page.permissions.space_role_removed**: Workspace-wide page permissions were removed, restricting access to the page.
* **page.permissions.space_role_updated**: Workspace-wide page permissions were updated, changing the type of access for all workspace members.
* **page.permissions.team_guest_role_added**: A teamspace guest's page permissions were added, allowing them to access the page.
* **page.permissions.team_guest_role_removed**: A teamspace guest's page permissions were removed, restricting them from accessing the page.
* **page.permissions.team_guest_role_updated**: A teamspace guest's page permissions were updated, changing their type of access.
* **page.permissions.team_owner_role_added**: A teamspace owner's page permissions were added, allowing them to access the page.
* **page.permissions.team_owner_role_removed**: A teamspace owner's page permissions were removed, restricting them from accessing the page.
* **page.permissions.team_owner_role_updated**: A teamspace owner's page permissions were updated, changing their type of access.
* **page.permissions.team_role_added**: A teamspace's page permissions were added, allowing teamspace members to access the page.
* **page.permissions.team_role_removed**: A teamspace's page permissions were removed, restricting teamspace members from accessing the page.
* **page.permissions.team_role_updated**: A teamspace's page permissions were updated, changing the type of access for teamspace members.
* **page.properties_edited**: A user edited a page's property, like a page title or a database property.
* **page.property.permissions.role_added**: A user added someone to a person property that controls access to a property on a page.
* **page.property.permissions.role_removed**: A user removed someone from a person property that controls access to a property on a page.
* **page.purged**: A page was permanently removed from Trash based on workspace data retention settings.
* **page.recurrence_automation_created**: A recurring automation was created on a page.
* **page.recurrence_automation_deleted**: A recurring automation was deleted from a page.
* **page.recurrence_automation_updated**: A recurring automation was updated on a page.
* **page.restored_from_trash**: A user restored a formerly deleted page from Trash.
* **page.suggestion.accepted**: A user accepted a suggested edit on a page.
* **page.suggestion.comment.created**: A user added a comment on a suggested edit.
* **page.suggestion.comment.deleted**: A user deleted a comment on a suggested edit.
* **page.suggestion.comment.updated**: A user updated a comment on a suggested edit.
* **page.suggestion.created**: A user suggested an edit on a page.
* **page.suggestion.rejected**: A user rejected a suggested edit on a page.
* **page.transcription_block.transcript_deleted**: A transcript for AI Meeting Notes was permanently deleted based on workspace settings.
* **page.unarchived**: A page was unarchived.
* **page.unlocked**: A page was unlocked to allow editing.
* **page.unverified**: A page's verification was removed.
* **page.verified**: A page was verified.
* **page.viewed**: A user viewed a page.
* **page.viewed.by_shared_email_domain_user**: A user with an email domain that was granted access to the page viewed it.

### Data source events

* **database.permission.added**: A user added a page-level access rule for a data source in a database.
* **database.permission.removed**: A user removed a page-level access rule for a data source in a database.
* **database.permission.updated**: A user changed a page-level access rule for a data source in a database.
* **database.permissions.can_create_pages.group_disabled**: A group's 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.group_enabled**: A group's 'can create pages' permission was enabled for a database.
* **database.permissions.can_create_pages.member_disabled**: A member's 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.member_enabled**: A member's 'can create pages' permission was enabled for a database.
* **database.permissions.can_create_pages.space_disabled**: Workspace-wide 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.space_enabled**: Workspace-wide 'can create pages' permission was enabled for a database.
* **database.permissions.can_create_pages.space_owner_disabled**: Workspace owners' 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.space_owner_enabled**: Workspace owners' 'can create pages' permission was enabled for a database.
* **database.permissions.can_create_pages.team_disabled**: A teamspace's 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.team_enabled**: A teamspace's 'can create pages' permission was enabled for a database.
* **database.permissions.can_create_pages.team_owner_disabled**: Teamspace owners' 'can create pages' permission was disabled for a database.
* **database.permissions.can_create_pages.team_owner_enabled**: Teamspace owners' 'can create pages' permission was enabled for a database.
* **database.property.permissions.default_access_updated**: A user changed the default access level for a database property.
* **database.property.permissions.exception_added**: A user added an access exception for a database property.
* **database.property.permissions.exception_removed**: A user removed an access exception for a database property.
* **database.property.permissions.exception_updated**: A user changed an access exception for a database property.
* **database.schema_edited**: A user edited the schema of a database.

### Workspace events

* **integration.created**: A developer created an internal integration and associated it with the workspace.
* **integration.deleted**: An internal integration associated with the workspace was deleted. Deletions can occur in the My Integrations dashboard, or an admin can remove access to an internal integration for all users.
* **integration.management_permissions.updated**: The list of people, groups, or workspace owners allowed to manage page access for an internal integration was changed.
* **integration.owner_added**: A workspace member was added as an explicit owner of an internal integration.
* **integration.owner_break_glass_added**: A workspace admin used break-glass access to add themselves as an owner of an internal integration.
* **integration.owner_removed**: A workspace member was removed as an explicit owner of an internal integration.
* **integration.permission.updated**: An integration's capabilities (reading content, inserting a comment, etc.) were changed.
* **integration.secret_reset**: An internal integration's API token was reset (or "refreshed").
* **integration.settings.updated**: An integration's basic settings, like its name or icon, were changed.
* **workspace.agent.created**: A user created an AI agent chat.
* **workspace.agent.deleted**: A user deleted an AI agent chat.
* **workspace.agent.file_downloaded**: A user downloaded a file from an AI agent chat.
* **workspace.agent.file_uploaded**: A user submitted an uploaded file to an AI agent chat.
* **workspace.agent.file_viewed**: A user viewed a file from an AI agent chat.
* **workspace.agent.permission.updated**: A user updated permissions for an AI agent chat.
* **workspace.agent.viewed**: A user viewed an AI agent chat.
* **workspace.agent.web_url_viewed**: An AI agent viewed a web URL.
* **workspace.audit_log_exported**: A workspace owner exported the workspace's audit log.
* **workspace.content_analytics_exported**: The Content Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics) was exported.
* **workspace.content_exported**: Workspace content for a page or for the entire workspace was exported by a workspace user.
* **workspace.content_search_exported**: The results of a [content search](https://www.notion.so/help/admin-content-search) for a workspace was exported by a workspace owner.
* **workspace.content_search_queried**: A workspace owner used the [admin content search](https://www.notion.so/help/admin-content-search) functionality to find workspace content. Content searches can retrieve content from public and private pages.
* **workspace.custom_agent.created**: A custom agent was created in the workspace.
* **workspace.custom_agent.credit_limit_increase_request.approved**: A request to increase a Custom Agent's credit limit was approved.
* **workspace.custom_agent.credit_limit_increase_request.rejected**: A request to increase a Custom Agent's credit limit was rejected.
* **workspace.custom_agent.published**: A custom agent was published in the workspace.
* **workspace.custom_agent.setup_mode_used**: An action was performed in setup mode for a custom agent in the workspace.
* **workspace.custom_emoji.created**: A custom emoji was created in the workspace.
* **workspace.custom_emoji.deleted**: A custom emoji was deleted from the workspace.
* **workspace.custom_emoji.updated**: A custom emoji was updated in the workspace.
* **workspace.domain_management.claim_request_status_updated**: The status of a claim and upgrade to Enterprise of a claimable workspace was updated.
* **workspace.domain_management.deletion_request_status_updated**: The status of workspace deletion of a claimable workspace was updated.
* **workspace.domain_management.transfer_request_status_updated**: A transfer request for a workspace created by a user with a verified domain was updated. See [domain management](https://www.notion.so/help/domain-management) for more information.
* **workspace.ekm.cmk.rotation.completed**: Customer-managed key (CMK) rotation on WEK was completed.
* **workspace.ekm.dek.rotation.completed**: Data encryption key (DEK) rotation was completed.
* **workspace.ekm.dek.rotation.started**: Data encryption key (DEK) rotation was started.
* **workspace.ekm.wek.generated**: A workspace encryption key (WEK) was generated.
* **workspace.ekm.wek.revoked**: A workspace encryption key (WEK) was revoked.
* **workspace.external_account_connected**: A public/external integration was connected to the workspace.
* **workspace.external_account_disconnected**: A public/external integration was disconnected from the workspace, or a workspace owner removed access to a public integration for all users in the workspace.
* **workspace.group.ai_credit_overage_updated**: AI credit overage access for a group was updated.
* **workspace.group.created**: A new group was created. A group is a defined collection of workspace members.
* **workspace.group.custom_agent_creation_updated**: The custom agent creation permission for a group was enabled or disabled.
* **workspace.group.custom_mcp_server_creation_updated**: A permission group's ability to create connections to custom MCP servers was updated.
* **workspace.group.deleted**: A group was deleted from the workspace.
* **workspace.group.internal_integration_creation_updated**: A permission group's ability to create internal integrations was updated.
* **workspace.group.notion_mcp_personal_access_token_updated**: A permission group's ability to use personal access tokens with Notion MCP was updated.
* **workspace.group.permissions.member_added**: A workspace owner or membership admin added a new member to a group. A group is a defined collection of workspace members.
* **workspace.group.permissions.member_removed**: A workspace owner or membership admin removed a member from a group.
* **workspace.group.permissions.member_role_updated**: A group member's role was updated (Member ↔ Group owner).
* **workspace.group.personal_access_token_creation_updated**: A permission group's ability to create personal access tokens was updated.
* **workspace.group.renamed**: A group name was changed.
* **workspace.guest_invite_request_resolved**: A guest invite to a page was requested for approval and the workspace owner either approved or denied the request.
* **workspace.guest_invite_request.created**: A guest invite request was created, requesting to invite a guest to specific pages.
* **workspace.imports.asana_data_fetched**: A Notion admin fetched Asana data on behalf of a workspace user for Asana data importer triage/debugging purposes.
* **workspace.imports.confluence_data_fetched**: A Notion admin fetched Confluence data on behalf of a workspace user for Confluence data importer triage/debugging purposes.
* **workspace.imports.monday_data_fetched**: A Notion admin fetched Monday.com data on behalf of a workspace user for Monday.com data importer triage/debugging purposes.
* **workspace.integration_added**: An integration was added to the workspace for the first time. This event will only be emitted the first time an integration is added to a workspace.
* **workspace.integration_removed**: All bots for a specific public integration were removed from the workspace.
* **workspace.integration_webhook_inactivated**: An integration's webhook was inactivated due to repeated delivery failures.
* **workspace.integration_webhook_reactivated**: An integration's webhook was reactivated after being inactive.
* **workspace.mcp_connection.tool_list_updated**: The selected tools for a workspace MCP connection were updated.
* **workspace.mcp.allowlist_disabled**: The MCP allowlist was disabled for the workspace.
* **workspace.mcp.allowlist_enabled**: The MCP allowlist was enabled for the workspace.
* **workspace.mcp.client_added**: An MCP client was added to the workspace's allowlist.
* **workspace.mcp.client_removed**: An MCP client was removed from the workspace's allowlist.
* **workspace.mcp.enterprise_managed_connection_disabled**: Enterprise-managed connections were disabled or removed for the workspace.
* **workspace.mcp.enterprise_managed_connection_enabled**: Enterprise-managed connections were enabled for the workspace.
* **workspace.mcp.enterprise_managed_connection_member_access_denied**: A workspace member was denied access to enterprise-managed connections.
* **workspace.mcp.enterprise_managed_connection_member_access_restored**: A workspace member's access to enterprise-managed connections was restored.
* **workspace.mcp.enterprise_managed_connection_updated**: Enterprise-managed connection settings were updated for the workspace.
* **workspace.mcp.server_connected**: An MCP server was connected to the workspace, including via an enterprise-managed connection.
* **workspace.members_exported**: A list of workspace members was exported.
* **workspace.membership_request_resolved**: A membership request from a member to add a new person to the workspace was resolved, i.e. the workspace owner either approved or denied the request.
* **workspace.permissions.guest_removed**: A guest was removed from the workspace by a workspace owner or membership admin.
* **workspace.permissions.member_added**: A user accepted an invite to join a new workspace and has been added to the member list.
* **workspace.permissions.member_invited**: A user was invited to a workspace by a workspace owner or membership admin.
* **workspace.permissions.member_removed**: A member was removed from the workspace by a workspace owner or membership admin.
* **workspace.permissions.member_role_updated**: A member's role in a workspace was updated. Roles include member, membership admin, and workspace owner.
* **workspace.private_content_transferred**: The private content of a deprovisioned workspace member was transferred to a new location. Enterprise workspace owners can [transfer content](https://www.notion.so/help/transfer-content-deprovisioned-user) from deprovisioned users.
* **workspace.public_domain.created**: A public domain was created for the workspace.
* **workspace.public_domain.deleted**: A public domain was deleted from the workspace.
* **workspace.public_domain.updated**: A public domain was updated for the workspace.
* **workspace.restricted_member_invite_request_resolved**: A restricted member invite request was approved or denied by a workspace owner.
* **workspace.saml_authorization**: A user verified workspace access via SAML SSO.
* **workspace.saml_sso_idp_metadata_url_added**: The IdP (Identity Provider) metadata URL was added by a workspace owner.
* **workspace.saml_sso_idp_metadata_url_removed**: The IdP (Identity Provider) metadata URL was removed by a workspace owner.
* **workspace.saml_sso_idp_metadata_url_updated**: The IdP (Identity Provider) metadata URL was updated by a workspace owner.
* **workspace.saml_sso_idp_metadata_xml_added**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was added by a workspace owner.
* **workspace.saml_sso_idp_metadata_xml_removed**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was removed by a workspace owner.
* **workspace.saml_sso_idp_metadata_xml_updated**: The IdP (Identity Provider) metadata XML (Extensible Markup Language) was updated by a workspace owner.
* **workspace.scim_token_generated**: A workspace owner generated a SCIM API token.
* **workspace.scim_token_revoked**: A workspace owner revoked a SCIM API token.
* **workspace.search_performed**: A search was performed in the workspace.
* **workspace.settings.agent_creation_policy_updated**: The agent creation policy setting was updated.
* **workspace.settings.agent_model_policy_updated**: The list of AI models an agent is allowed to use was updated. `agent_type` names which allowed model list changed, and the model and provider lists are sent both before and after the change. `allowed_restricted_access_models` runs the other way from the restricted lists: a restricted-access model is off until an admin names it there, so a model entering that list was allowed and a model leaving it was restricted. For `personal_agent`, `previous_require_auto` and `require_auto` say whether Notion Agent was required to use Auto before and after the change. While it's required, members can't pick a model.
* **workspace.settings.ai_credit_overage_policy_updated**: The AI credit overage policy setting was updated.
* **workspace.settings.ai_leap_toggled**: A workspace owner enabled or disabled the Notion AI LEAP (Learning & Early Access Program) setting.
* **workspace.settings.ai_legal_terms_setting_updated**: A user enabled or disabled Notion AI in the workspace by accepting or revoking AI legal terms.
* **workspace.settings.ai_meeting_notes_availability_updated**: The AI meeting notes availability setting was updated.
* **workspace.settings.allow_chatgpt_subscription_sharing_setting_updated**: A workspace owner enabled or disabled ChatGPT subscription sharing.
* **workspace.settings.allow_content_export_setting_updated**: A workspace owner enabled or disabled exporting.
* **workspace.settings.allow_custom_agents_by_notion_support_updated**: Notion Support added or removed the workspace restriction on Custom Agents. Removing the restriction preserves the workspace’s own Custom Agents policy.
* **workspace.settings.allow_custom_mcp_servers_setting_updated**: Custom MCP servers were enabled or disabled for the workspace. Disabling also disconnects custom MCP servers that were already added.
* **workspace.settings.allow_group_creation_setting_updated**: A user enabled or disabled the ability for non-admin members to create groups.
* **workspace.settings.allow_guests_setting_updated**: A workspace owner enabled or disabled the ability to add guests to the workspace.
* **workspace.settings.allow_public_page_sharing_setting_updated**: A workspace owner enabled or disabled public page sharing for the workspace.
* **workspace.settings.allow_teamspace_creation_setting_updated**: A user enabled or disabled the ability for everyone in the workspace to create a teamspace.
* **workspace.settings.allow_workspace_creation_setting_updated**: A workspace owner restricted creation of new workspaces by users with the claimed enterprise email domain.
* **workspace.settings.analytics_tracking_setting_updated**: A user enabled or disabled workspace analytics tracking within the workspace.
* **workspace.settings.custom_agent_default_model_updated**: The default model for new Custom Agents was updated. `previous_model` and `model` contain the prior and current model, or `Auto` when no workspace default is set.
* **workspace.settings.custom_mcp_server_creation_policy_updated**: The workspace policy controlling who can create connections to custom MCP servers was updated.
* **workspace.settings.delete_from_trash_delay**: The [custom data retention](https://www.notion.com/help/custom-data-retention-settings) delete from trash delay setting was updated.
* **workspace.settings.disallow_webhook_automation_action_toggled**: A workspace owner enabled or disabled the use of webhook automation actions in the workspace.
* **workspace.settings.duplicate_pages_to_workspaces_setting_updated**: A workspace owner enabled or disabled moving pages to other workspaces.
* **workspace.settings.email_domain_added**: A user added an allowed email domain to the workspace.
* **workspace.settings.email_domain_removed**: A user removed an allowed email domain from the workspace.
* **workspace.settings.enable_saml_sso_config_updated**: An organization owner enabled or disabled SAML.
* **workspace.settings.enforce_saml_sso_config_updated**: An organization owner enabled or disabled Enforce SAML.
* **workspace.settings.external_agent_access_policy_updated**: The external agent access policy changed. Includes the previous and updated policy, without credentials.
* **workspace.settings.guest_invite_request_setting_updated**: The guest invite request approval setting was enabled or disabled.
* **workspace.settings.guest_membership_request_setting_updated**: A user enabled or disabled guest membership requests for the workspace.
* **workspace.settings.hipaa_compliance_updated**: A workspace owner enabled or disabled HIPAA compliance by accepting or revoking Notion's Business Associate Agreement.
* **workspace.settings.icon_updated**: The workspace icon was changed.
* **workspace.settings.integration_restriction_settings_updated**: A workspace owner enabled or disabled integration restrictions.
* **workspace.settings.internal_integration_creation_policy_updated**: The workspace policy controlling who can create internal integrations was updated.
* **workspace.settings.invite_link_reset**: A user reset the workspace invite link.
* **workspace.settings.invite_link_setting_updated**: A user enabled or disabled the workspace invite link.
* **workspace.settings.mcp_server_added_to_allowlist**: That an MCP server URL or pattern was added to the approved connections allowlist.
* **workspace.settings.mcp_server_allowlist_setting_updated**: That enforcement of the MCP server URL allowlist was enabled or disabled.
* **workspace.settings.mcp_server_removed_from_allowlist**: That an MCP server URL or pattern was removed from the approved connections allowlist.
* **workspace.settings.meeting_notes_consent_setting_updated**: The setting requiring consent before AI meeting notes transcription was updated.
* **workspace.settings.member_add_policy_updated**: A user updated who can add members to the workspace.
* **workspace.settings.membership_request_setting_updated**: A user enabled or disabled new workspace membership requests.
* **workspace.settings.name_updated**: A user updated the workspace's name.
* **workspace.settings.notion_mcp_personal_access_token_policy_updated**: The workspace policy controlling who can use personal access tokens with Notion MCP was updated.
* **workspace.settings.page_access_request_setting_updated**: A user enabled or disabled page access requests from non-workspace-members.
* **workspace.settings.people_directory_setting_updated**: The people directory visibility setting was enabled or disabled.
* **workspace.settings.people_hover_cards_setting_updated**: The people hover cards setting was enabled or disabled.
* **workspace.settings.personal_access_token_creation_policy_updated**: The workspace policy controlling who can create personal access tokens was updated.
* **workspace.settings.public_homepage_added**: A workspace owner set a public homepage.
* **workspace.settings.public_homepage_removed**: A workspace owner cleared the public homepage.
* **workspace.settings.public_homepage_updated**: A workspace owner changed the public homepage.
* **workspace.settings.public_pages_domain_updated**: The domain for publicly shared pages was updated.
* **workspace.settings.purge_delay**: The [custom data retention](https://www.notion.com/help/custom-data-retention-settings) purge delay setting was updated.
* **workspace.settings.saml_automatic_account_creation_setting_updated**: A workspace owner enabled or disabled automatically creating accounts on SAML sign-in.
* **workspace.settings.sidebar_editing_setting_updated**: A workspace owner enabled or disabled the ability for users to change the workspace sidebar.
* **workspace.teams_read**: A user viewed the list of teamspaces in the workspace.
* **workspace.user_analytics_exported**: The User Analytics table of [Workspace Analytics](https://www.notion.so/help/workspace-analytics) was exported.
* **workspace.users_read**: A user viewed the list of users in the workspace.

### Account events

* **user.deleted**: A user account was deleted. This event will be sent to any workspace with which the account is associated.
* **user.login**: A user logged into an account.
* **user.logout**: A user logged out of an account.
* **user.settings.alias_added**: A user added an email alias to their account.
* **user.settings.alias_made_primary**: A user made an email alias their primary email address.
* **user.settings.alias_removed**: A user removed an email alias from their account.
* **user.settings.analytics_tracking_setting_updated**: A user updated their analytics tracking setting.
* **user.settings.email_updated**: The email of a user was changed.
* **user.settings.login_method.mfa_backup_code_updated**: A user updated their MFA (Multi-Factor Authentication) backup code settings.
* **user.settings.login_method.mfa_sms_updated**: A user updated their MFA (Multi-Factor Authentication) SMS (Short Message Service) settings.
* **user.settings.login_method.mfa_totp_updated**: A user updated their MFA (Multi-Factor Authentication) TOTP (Time-based One-Time Password) settings.
* **user.settings.login_method.password_added**: A user added a password to their account for login purposes.
* **user.settings.login_method.password_removed**: A user removed a password from their account.
* **user.settings.login_method.password_updated**: A user updated their password.
* **user.settings.preferred_name_updated**: A user updated their account's preferred name.
* **user.settings.profile_photo_updated**: The profile photo of a user was changed.
* **user.settings.support_access_granted**: A user's account was granted Notion support access.
* **user.settings.support_access_revoked**: A user's account was revoked Notion support access.
* **user.suspended**: An admin suspended a managed user account.
* **user.unsuspended**: An admin unsuspended a managed user account.

### Teamspace events

* **teamspace.archived**: A teamspace owner archived a teamspace.
* **teamspace.created**: A user created a teamspace.
* **teamspace.permissions.custom_group_role_added**: A teamspace owner added custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom_group_role_removed**: A teamspace owner removed custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom_group_role_updated**: A teamspace owner updated custom permissions for a group that is added to the teamspace.
* **teamspace.permissions.custom_member_role_added**: A teamspace owner added custom page permissions for a specific teamspace member.
* **teamspace.permissions.custom_member_role_removed**: A teamspace owner removed custom page permissions for a specific teamspace member.
* **teamspace.permissions.custom_member_role_updated**: A teamspace owner updated custom page permissions for a specific teamspace member.
* **teamspace.permissions.default_member_role_updated**: The default teamspace page permissions applied to teamspace members was updated.
* **teamspace.permissions.default_workspace_role_added**: A teamspace owner gave page permissions to workspace users in a closed teamspace.
* **teamspace.permissions.default_workspace_role_removed**: A teamspace owner removed page permissions from workspace users in a closed teamspace.
* **teamspace.permissions.default_workspace_role_updated**: A teamspace owner updated the default page permissions for all workspace users in a teamspace.
* **teamspace.permissions.group_added**: A group was added to a teamspace. A group is a defined collection of users.
* **teamspace.permissions.group_removed**: A group was removed from the teamspace by a teamspace owner.
* **teamspace.permissions.member_added**: A user was added to the teamspace. The user either joined an open teamspace or was added by another member. The event payload will specify "as Teamspace owner" if the user was added with teamspace owner privileges.
* **teamspace.permissions.member_removed**: A teamspace member was removed from the teamspace. Removal can be triggered by a member leaving or being removed by a teamspace owner.
* **teamspace.permissions.member_role_updated**: A teamspace member's role was updated. Roles include Teamspace Member and Teamspace Owner.
* **teamspace.restored**: A previously archived teamspace was restored.
* **teamspace.settings.allow_content_export_setting_updated**: The setting to allow exporting teamspace content was enabled or disabled.
* **teamspace.settings.allow_guests_setting_updated**: A teamspace owner enabled or disabled the ability to add guests (non-members) to a specific teamspace.
* **teamspace.settings.allow_public_page_sharing_setting_updated**: The setting to allow publicly sharing a teamspace page was enabled or disabled by a workspace owner.
* **teamspace.settings.allow_sidebar_editing_setting_updated**: The setting that determines who can edit the sidebar was updated. The setting will indicate if any teamspace member can edit the sidebar or if editing is only available for teamspace owners.
* **teamspace.settings.default_setting_updated**: A user enabled or disabled a teamspace as a default teamspace.
* **teamspace.settings.description_updated**: The teamspace description was updated.
* **teamspace.settings.icon_updated**: The teamspace icon was changed.
* **teamspace.settings.member_invitation_setting_updated**: A user updated settings for who can invite teamspace members.
* **teamspace.settings.name_updated**: A user updated the teamspace's name.
* **teamspace.settings.privacy_type_updated**: A teamspace owner changed the teamspace privacy type.

### Form events

* **form_response.created**: A form response was submitted.
* **form.content.updated**: A user updated a form's content.
* **form.created**: A user created a form.
* **form.permissions.shared_to_public_role_added**: A user enabled public sharing for a form.
* **form.permissions.shared_to_public_role_removed**: A user disabled public sharing for a form.
* **form.viewed**: A user viewed a form.
