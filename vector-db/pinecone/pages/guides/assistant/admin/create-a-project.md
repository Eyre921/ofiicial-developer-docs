---
title: "Create a project"
source: https://docs.pinecone.io/guides/assistant/admin/create-a-project
path: guides/assistant/admin/create-a-project
---

Create a new Pinecone project in your organization.

This page shows you how to create a project.

If you are an [organization owner or organization manager](/guides/assistant/admin/organizations-overview#organization-roles), you can create a project in your organization:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**your profile > Organization settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

    2. Click **+ Create Project**.

    3. Enter a **Name**.

       <Note>
         A project name can contain up to 512 characters. For more information, see [Object identifiers](/reference/api/database-limits#identifier-limits).
       </Note>

    4. (Optional) Tags are key-value pairs that you can use to categorize and identify the project. To add a tag, click **+ Add tag** and enter a tag key and value.

    5. (Optional) Select **Encrypt with Customer Managed Encryption Key**. For more information, see [Configure CMEK](/guides/production/configure-cmek).

    6. Click **Create project**.

       To load an index with a [sample dataset](/guides/data/use-sample-datasets), click **Load sample data** and follow the prompts.

    <Note>
      The number of projects per organization varies by plan—see [Projects per organization](/reference/api/database-limits#projects-per-organization). To create additional projects, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).
    </Note>
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl "https://api.pinecone.io/admin/projects" \
          -H "X-Pinecone-Api-Version: 2025-10" \
      	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      	-d '{
                "name":"example-project"
              }'
      ```

      ```bash CLI theme={null}
      # Target the organization for which you want to 
      # create a project.
      pc target -o "example-org"
      # Create the project and set it as the target 
      # project for the CLI.
      pc project create -n "example-project" --target
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "example-project",
        "max_pods": 0,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-03-16T22:46:45.030Z"
      }
      ```

      ```text CLI theme={null}
      [SUCCESS] Project example-cli-project created successfully.

      ATTRIBUTE           VALUE
      Name                example-project
      ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
      Organization ID     -NM7af6f234168c4e44a
      Created At          2025-10-27 23:27:46.370088 +0000 UTC
      Force Encryption    false
      Max Pods            5

      [SUCCESS] Target project set to example-cli-project
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Next steps

* [Add users to your project](/guides/assistant/admin/manage-project-members#add-members-to-a-project)
* [Create an assistant](/guides/assistant/create-assistant)
