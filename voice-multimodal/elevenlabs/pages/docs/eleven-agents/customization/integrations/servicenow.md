---
title: "ServiceNow"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/servicenow.md
path: docs/eleven-agents/customization/integrations/servicenow
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ServiceNow

## Overview

Connect your ElevenLabs AI agents with ServiceNow to manage incidents, cases, tasks, and knowledge articles. This integration enables your agents to create and update IT service management records, search the knowledge base, and automate IT support workflows during conversations.

## Capabilities

| Capability                | Support                                    |
| ------------------------- | ------------------------------------------ |
| Zero retention mode (ZRM) | Not supported                              |
| Attachments in tools      | Not supported — tools operate on text only |

## Setup

This integration uses **Basic Authentication** with a ServiceNow instance username and password.

#### Identify your instance

Find your ServiceNow instance name — this is the subdomain in your ServiceNow URL (e.g., `mycompany` from `mycompany.service-now.com`).

#### Create an integration user (recommended)

In ServiceNow, create a dedicated user for the integration. Check **Web Service Access only** on the user record to restrict the account to API access. Assign the necessary roles for the objects your agent needs to access (e.g., `itil` for incident management).

#### Set a password

Set a password on the user record for the integration user. This password is used for Basic Authentication regardless of any SSO configuration.

#### Connect in ElevenLabs

In the ElevenLabs integration setup, enter your **instance name**, **username**, and **password**.

## How it works

#### Caller identification

The agent identifies the caller by searching for their user record via email or phone number.

#### Issue triage

The agent searches the knowledge base for relevant articles and checks for existing incidents related to the caller's issue.

#### Record creation

If no existing record matches, the agent creates a new incident or case with details gathered from the conversation, including priority, category, and assignment group.

#### Follow-up

The agent creates follow-up tasks, updates incident states, and adds work notes to existing records.

## Useful links

* [ServiceNow REST API documentation](https://www.servicenow.com/docs/bundle/yokohama-api/page/integrate/inbound-rest/concept/c_RESTAPI.html)
* [ServiceNow API authentication](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/integrate/authentication/concept/api-authentication.html)
