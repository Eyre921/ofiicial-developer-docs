---
title: "GitHub"
source: https://docs.trychroma.com/cloud/sync/github
path: cloud/sync/github
---

Sync GitHub repositories into Chroma Cloud.

## Walkthrough

When syncing a new version of a repository, Chroma forks the existing collection using copy-on-write and only processes the diff, so re-syncs are fast and storage-efficient.

## Direct Sync

Direct Sync is the default syncing method, which uses the Chroma Cloud GitHub app. To use your own custom GitHub app, use [Platform Sync](/cloud/sync/github#platform-sync).

1. **Prerequisites**

   This walkthrough assumes that you have a GitHub account with at least one repository.

2. **New database setup**

   If you do not already have a Chroma Cloud account, you will need to create one at [trychroma.com](https://www.trychroma.com). After creating an account, you can create a database by specifying a name:

   <img alt="Create database screen" />

   On the setup screen, select "Sync a GitHub repo":

   <img alt="Onboarding screen for syncing a GitHub repo" />

   Install the Chroma GitHub App into your GitHub account or organization:

   <img alt="GitHub app installation screen" />

   And follow the prompts to initiate sync. Choose the **repo** to sync code from, the **branch or commit hash** version of the code to index, and new **collection name** for the synced code. (The collection will be created by the syncing process, and must not exist yet.)

   <img alt="/sync repo to Chroma Collection UI" />

3. **Existing database setup**

   Open an existing database in Chroma Cloud, and select "Sync" from the menu:

   <img alt="/sync tab in Chroma Cloud UI" />

   On the Sync page, select "Create" to begin syncing code. If you have not already connected GitHub, you may be prompted to install the Chroma Cloud GitHub app again.

   <img alt="Create path for a new Sync" />

   Then, follow the prompts to initiate sync. Choose the **repo** to sync code from, the **branch or commit hash** version of the code to index, and a new **collection name** for the synced code. (The collection will be created by the syncing process, and must not exist yet.)

   <img alt="Create flow for a new Sync" />

4. **Viewing an Invocation**

   Each Sync create a new Invocation. When completed, select "View Collection" to see the new Chroma collection containing the synced code:

   <img alt="Invocation screen for a Sync" />

## Platform Sync

<Warning>
  **Team & Enterprise only**

  Platform Sync is only available on Chroma Cloud [Team and Enterprise plans](https://trychroma.com/pricing).
</Warning>

1. **Prerequisites**

   This walkthrough assumes that you have already [created a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) and installed it into at least one GitHub account or organization.

   The GitHub App must have read-only access to the "Contents" and "Metadata" permissions listed under "Repository permissions." These permissions ensure Chroma can index repositories authorized on the GitHub app.

   <img alt="GitHub App contents" />

   <img alt="GitHub App metadata" />

2. **Setup**

   If you do not already have a Chroma Cloud account, you will need to create one at [trychroma.com](https://www.trychroma.com). After creating an account, you can create a database by specifying a name:

   <img alt="Create database screen" />

   Once you have a database, you should create an API key to be able to access the Sync Function's API. You can choose to make this API key scoped to all databases on your account or only the one you just created:

   <img alt="API key issuance for Chroma Cloud" />

   The final setup step is to grant Chroma access to the repositories to which your GitHub App has access. You will need to retrieve the app's ID and private key from GitHub:

   <img alt="GitHub App ID" />

   <img alt="GitHub Secret Key" />

   With these credentials, navigate to the "Sync" -> "New GitHub sync" -> "Register your GitHub app" to configure your GitHub App with Chroma.

   <img alt="Platform setup" />

   On the "Connect your custom GitHub app" screen, submit the App ID and private key from GitHub:

   <img alt="Creating a custom github app" />

3. **Creating a source**

   To create a source, you must send an API request to the Sync Function's API:

   ```bash theme={null}
   curl -X POST https://sync.trychroma.com/api/v1/sources \
       -H "x-chroma-token: <YOUR_CHROMA_API_KEY>" \
       -H "Content-Type: application/json" \
       -d '{
           "database_name": "<YOUR_DATABASE_NAME>",
           "embedding_model": "Qwen/Qwen3-Embedding-0.6B",
           "github": {
           "repository": "chroma-core/chroma",
           "app_id": "<YOUR_GITHUB_APP_ID>"
           }
       }'
   ```

4. **Invoking the Sync Function**

   To invoke the Sync Function, you must select a source on which to create the invocation. See the previous step for details on how to create a source. Once you select the source in the UI, you can invoke the Sync Function by clicking "Create invocation":

   <img alt="Creating a custom sync invocation" />

   Alternatively, you can invoke the Sync Function by sending an API request to the Sync Function's API:

   ```bash theme={null}
   curl -X POST https://sync.trychroma.com/api/v1/sources/{source_id}/invocations \
       -H "x-chroma-token: <YOUR_CHROMA_API_KEY>" \
       -H "Content-Type: application/json" \
       -d '{
           "target_collection_name": "<YOUR_TARGET_COLLECTION_NAME>",
           "ref_identifier": {
                   // only one of these should be supplied
                   "branch": "<YOUR_BRANCH_NAME>",
                   "sha": "<YOUR_COMMIT_SHA>"
               }
       }'
   ```
