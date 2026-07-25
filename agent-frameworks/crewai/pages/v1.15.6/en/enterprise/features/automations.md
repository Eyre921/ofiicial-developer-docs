---
title: "Automations"
source: https://docs.crewai.com/v1.15.6/en/enterprise/features/automations
path: v1.15.6/en/enterprise/features/automations
---

Manage, deploy, and monitor your live crews (automations) in one place.

## Overview

Automations is the live operations hub for your deployed crews. Use it to deploy from GitHub or a ZIP file, manage environment variables, re‑deploy when needed, and monitor the status of each automation.

<Frame>
  <img alt="Automations Overview" />
</Frame>

## Deployment Methods

### Deploy from GitHub

Use this for version‑controlled projects and continuous deployment.

<Steps>
  <Step title="Connect GitHub">
    Click <b>Configure GitHub</b> and authorize access.
  </Step>

  <Step title="Select Repository & Branch">
    Choose the <b>Repository</b> and <b>Branch</b> you want to deploy from.
  </Step>

  <Step title="Enable Auto‑deploy (optional)">
    Turn on <b>Automatically deploy new commits</b> to ship updates on every push.
  </Step>

  <Step title="Add Environment Variables">
    Add secrets individually or use <b>Bulk View</b> for multiple variables.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
  <img alt="GitHub Deployment" />
</Frame>

### Deploy from ZIP

Ship quickly without Git—upload a compressed package of your project.

<Steps>
  <Step title="Choose File">
    Select the ZIP archive from your computer.
  </Step>

  <Step title="Add Environment Variables">
    Provide any required variables or keys.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
  <img alt="ZIP Deployment" />
</Frame>

## Automations Dashboard

The table lists all live automations with key details:

* **CREW**: Automation name
* **STATUS**: Online / Failed / In Progress
* **URL**: Endpoint for kickoff/status
* **TOKEN**: Automation token
* **ACTIONS**: Re‑deploy, delete, and more

Use the top‑right controls to filter and search:

* Search by name
* Filter by <b>Status</b>
* Filter by <b>Source</b> (GitHub / Studio / ZIP)

Once deployed, you can view the automation details and have the **Options** dropdown menu to `chat with this crew`, `Export React Component` and `Export as MCP`.

<Frame>
  <img alt="Automations Table" />
</Frame>

## Best Practices

* Prefer GitHub deployments for version control and CI/CD
* Use re‑deploy to roll forward after code or config updates or set it to auto-deploy on every push

## Related

<CardGroup>
  <Card title="Deploy a Crew" href="/en/enterprise/guides/deploy-crew" icon="rocket">
    Deploy a Crew from GitHub or ZIP file.
  </Card>

  <Card title="Automation Triggers" href="/en/enterprise/guides/automation-triggers" icon="trigger">
    Trigger automations via webhooks or API.
  </Card>

  <Card title="Webhook Automation" href="/en/enterprise/guides/webhook-automation" icon="webhook">
    Stream real-time events and updates to your systems.
  </Card>
</CardGroup>
