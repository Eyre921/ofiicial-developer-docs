---
title: "Marketplace quickstart"
source: https://docs.pinecone.io/guides/marketplace/quickstart
path: guides/marketplace/quickstart
---

Pick a template, connect a folder of documents, and publish your first Pinecone Marketplace knowledge application.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This quickstart shows you how to publish your first knowledge application in Pinecone Marketplace. You will pick a template, connect a folder of documents, configure the application, and share it with end users.

You should be able to complete this quickstart in under an hour.

## Before you begin

* A Pinecone account. If you do not have one, [sign up](https://app.pinecone.io/?sessionType=signup).
* A folder of source documents in Google Drive that you want the application to answer questions about.

## 1. Open Marketplace

Go to [marketplace.pinecone.io](https://marketplace.pinecone.io) and sign in. If you already have a Pinecone account, you can also open Marketplace from the **Marketplace ↗** entry in the Pinecone console sidebar.

## 2. Pick an app

The **Apps** tab shows the available apps. Pick the one that most closely matches your use case and select **Get started** on the card. For the full list, see [App catalog](/guides/marketplace/template-catalog).

If none of the apps match exactly, pick the closest fit. Apps are starting points; you control the operating parameters and the documents the application uses.

## 3. Choose where to deploy

Marketplace prompts you to select the Pinecone organization and project where the app's assistant will be created. The assistant counts toward that project's plan limits. Pick the project, then select **Continue**.

## 4. Configure the deployment

The setup wizard prompts you for:

* A name and short description for the knowledge application.
* Operating parameters that shape responses, such as tone, system prompt, and the layout the consumer experience uses.

The project you chose in step 3 is shown for reference. You can change the name, description, and operating parameters later from the deployment dashboard. For details, see [Configure operating parameters](/guides/marketplace/configure-operating-parameters).

## 5. Connect a data source

Connect a Google Drive folder so the application has documents to answer from. Marketplace mirrors selected files, ingests them into Pinecone, and keeps them in sync as the source folder changes.

For step-by-step instructions, see [Connect Google Drive](/guides/marketplace/connectors-overview#connect-google-drive). To upload files directly instead, see [Manual uploads](/guides/marketplace/connectors-overview#manual-uploads).

## 6. Publish

Click **Publish**. Marketplace provisions the underlying Pinecone assistants in the background, runs introspection to build a capability manifest, generates suggested starter questions, and runs an automatic evaluation. Publishing is non-blocking: you can navigate away and return when the deployment is active.

For details, see [Publish a deployment](/guides/marketplace/publish-a-deployment).

## 7. Share with end users

Choose how end users access the application:

* **Link access**: anyone with the link can use the application.
* **Google sign-in**: end users sign in with Google.

Copy the deployment URL from the dashboard and share it. End users see a clean, branded interface with chat, citations, and any visual components you configured.

For details, see [Consumer authentication overview](/guides/marketplace/consumer-auth-overview).

## If you get stuck

Use the **Support** link in the Marketplace header to reach the Pinecone support team. The header also has a theme toggle and your account menu.

## Next steps

* Review answers and feedback in [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
* Add a second knowledge domain to the same deployment to take advantage of [multi-domain routing](/guides/marketplace/multi-domain-routing).
* Iterate on operating parameters or sources, then publish a new version. See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).
