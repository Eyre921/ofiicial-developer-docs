---
title: "Manage projects"
source: https://docs.pinecone.io/guides/assistant/admin/manage-projects
path: guides/assistant/admin/manage-projects
---

View project details, rename projects, add project tags, and delete Pinecone projects using the console or the Admin API with an access token.

This page shows you how to view project details, rename a project, and delete a project.

<Note>
  You must be an [organization owner](/guides/assistant/admin/organizations-overview#organization-roles) or [project owner](/guides/assistant/admin/projects-overview#project-roles) to edit project details or delete a project.
</Note>

## View project details

You can view the details of a project, as in the following example:

<Note>
  An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
</Note>

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  curl -X GET "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -H "accept: application/json"
  ```

  ```bash CLI theme={null}
  PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Fetch the project details.
  pc project describe -i $PROJECT_ID
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-27T23:27:46.370088Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-27 23:27:46.370088 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</CodeGroup>

<Tip>
  You can view project details using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/projects/-/indexes).
</Tip>

## Rename a project

You can change the name of your project:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

    2. Click the **ellipsis (...) menu > Configure** icon next to the project you want to update.

    3. Enter a new **Project Name**.

       <Note>
         A project name can contain up to 512 characters.
       </Note>

    4. Click **Save Changes**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PROJECT_ID="YOUR_PROJECT_ID"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X PATCH "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
           -H "accept: application/json" \
           -H "Content-Type: application/json" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -d '{
                 "name": "updated-example-project"
               }'
      ```

      ```bash CLI theme={null}
      PROJECT_ID="YOUR_PROJECT_ID"

      # Target the project to update.
      pc target -o "example-org" "example-project"
      # Update the project name.
      pc project update -i $PROJECT_ID -n "updated-example-project"
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "updated-example-project",
        "max_pods": 5,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-10-27T23:27:46.370088Z"
      }
      ```

      ```text CLI theme={null}
      [SUCCESS] Project 32c8235a-5220-4a80-a9f1-69c24109e6f2 updated successfully.
      ATTRIBUTE           VALUE
      Name                updated-example-project
      ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
      Organization ID     -NM7af6f234168c4e44a
      Created At          2025-10-27 23:27:46.370088 +0000 UTC
      Force Encryption    false
      Max Pods            5
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Add project tags

Project tags are key-value pairs that you can use to categorize and identify a project.

To add project tags, use the Pinecone console.

1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).
2. Click the **ellipsis (...) menu > Configure** icon next to the project you want to update.
3. Click **+ Add tag** and enter a tag key and value. Repeat for each tag you want to add.
4. Click **Save Changes**.

<Tip>
  You can also [add tags to indexes](/guides/manage-data/manage-indexes#configure-index-tags).
</Tip>

## Delete a project

To delete a project, you must first [delete all data](/guides/manage-data/delete-data), [indexes](/guides/manage-data/manage-indexes#delete-an-index), [collections](/guides/indexes/pods/back-up-a-pod-based-index#delete-a-collection), [backups](/guides/manage-data/back-up-an-index#delete-a-backup) and [assistants](/guides/assistant/manage-assistants#delete-an-assistant) associated with the project. Then, you can delete the project itself:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).
    2. For the project you want to delete, click the **ellipsis (...) menu > Delete**.
    3. Enter the project name to confirm the deletion.
    4. Click **Delete Project**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
      PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

      curl -X DELETE "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
      ```

      ```bash CLI theme={null}
      PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

      # Target the organization that contains the project.
      pc target -o "example-org" 
      # Delete the project. Use --skip-confirmation to skip 
      # the confirmation prompt.
      pc project delete -i $PINECONE_PROJECT_ID
      ```
    </CodeGroup>
  </Tab>
</Tabs>
