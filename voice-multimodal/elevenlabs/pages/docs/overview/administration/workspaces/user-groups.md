---
title: "User groups"
source: https://elevenlabs.io/docs/overview/administration/workspaces/user-groups.md
path: docs/overview/administration/workspaces/user-groups
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# User groups

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b3352775553098f965b4c3a92526bf71c6afb836ce32b6eccac2947b80d0fd01/assets/images/product-guides/workspaces/manage-group.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233203Z&X-Amz-Expires=604800&X-Amz-Signature=d36ae74baa857b8419e879931bb5f709f397f1fa23d9b8acff97c7f3cbbad074&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Group Management" />

## Overview

&#x20;Only Workspace admins can create, edit, and delete user groups.&#x20;

User groups allow you to manage permissions for multiple users at once.

## Creating a user group

You can create a user group from **Workspace settings**. You can then [share resources](/docs/overview/administration/workspaces/sharing-resources) with the group directly.
If access to a user group is lost, access to resources shared with that group is also lost.

## Multiple groups

User groups cannot be nested, but you can add users to multiple groups. If a user is part of multiple groups, they will have the union of all the permissions of the groups they are part of.

For example, you can create a voice and grant the **Sales** and **Marketing** groups viewer and editor roles on the voice, respectively.
If a user is part of both groups, they will have editor permissions on the voice. Losing access to the **Marketing** group will downgrade the user's permissions to viewer.

## Disabling platform features

Permissions for groups can be revoked for specific product features, such as Professional Voice Cloning or Sound Effects.
To do this, you first have to remove the relevant permissions from the **Everyone** group. Afterwards, enable the permissions for each group that should have access.
