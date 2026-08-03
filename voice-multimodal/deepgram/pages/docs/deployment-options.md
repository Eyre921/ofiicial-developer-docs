---
title: "Deployment Options"
source: https://developers.deepgram.com/docs/deployment-options.md
path: docs/deployment-options
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deployment Options

Deepgram offers the following deployment options:

| **Option**  | **Description**                                                                                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hosted      | A multi-tenant cloud service running on Deepgram's cloud with standard authentication and customization features.                                                                                                                                                                                          |
| Self-Hosted | A dedicated service deployed to customer-requisitioned cloud instances, such as Amazon Web Services (AWS) or Google Cloud Platform (GCP), or customer data centers. Self-hosting is available for Premium customers who have unique [business requirements](/docs/self-hosted-introduction#why-self-host). |

## Operational Differences

| **Operation**                              | **Hosted**                | **Self-Hosted**                                                                                                                                          |
| ------------------------------------------ | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Deployment Location**                    | Deepgram’s infrastructure | Customer-requisitioned cloud instance, such as AWS or GCPCustomer data center                                                                            |
| **Infrastructure & Backup Responsibility** | Deepgram                  | Customer                                                                                                                                                 |
| **Updates**                                | Automatic rolling updates | Deepgram makes regular updates available for customer to apply. In case of critical updates (for example, security patches), Deepgram notifies customer. |
| **Service & Uptime Reporting**             | Monitored by Deepgram     | Monitored by customer                                                                                                                                    |

---

What’s Next

* [Self-Hosted Introduction](https://developers.deepgram.com/docs/self-hosted-introduction)
