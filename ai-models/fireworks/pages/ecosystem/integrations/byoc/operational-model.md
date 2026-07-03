---
title: "Operational Model"
source: https://docs.fireworks.ai/ecosystem/integrations/byoc/operational-model
path: ecosystem/integrations/byoc/operational-model
---

Learn how Fireworks operates Bring Your Own Cluster environments day to day.

Bring Your Own Cluster (BYOC) is designed so your team keeps ownership of the cloud or hardware environment while Fireworks operates the model serving stack inside it.

<Note>
  Bring Your Own Cluster is in Private Preview for Enterprise customers. Contact [sales@fireworks.ai](mailto:sales@fireworks.ai) to participate in the preview and confirm operational support terms for your deployment.
</Note>

## Responsibilities

In steady state, your team owns the cloud account or data center environment, Kubernetes cluster, GPU nodes, networking, and customer-side governance. Fireworks owns the serving software stack, model deployment lifecycle, scaling behavior, performance optimization, observability, upgrades, and operational support for the Fireworks-managed components.

## Shared responsibility model

BYOC is a shared operational model.

| Area                         | Customer owns                                                                           | Fireworks owns                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Cloud / hardware environment | Cloud account or data center environment, Kubernetes cluster, GPU nodes, and networking | Guidance during onboarding and validation                                                               |
| Setup access                 | A dedicated, clearly named, revocable administrative credential during setup            | Installation of the serving stack and creation of scoped runtime identities                             |
| Model serving                | Available GPU capacity and required customer-side dependencies                          | Model deployment lifecycle, routing, autoscaling, performance optimization, and upgrades                |
| Reliability                  | Underlying hardware capacity                                                            | GPU and node health monitoring, automated remediation workflows, observability, and operational support |

## Model lifecycle

Fireworks deploys, updates, and version-manages inference deployments in the cluster. Customers request model or deployment changes through Fireworks, and Fireworks applies those changes through the managed BYOC operating process.

<Warning>
  Fine-tuning is not supported in BYOC during Private Preview.
</Warning>

## Autoscaling

Serving capacity scales with demand within the GPU capacity available in your cluster. Where appropriate for the workload, Fireworks can scale deployments down when idle and scale them back up when traffic returns.

Autoscaling behavior depends on model size, traffic shape, GPU availability, and customer-defined capacity constraints.

## GPU fleet reliability

Fireworks continuously monitors GPU and node health for the serving stack. When a node or GPU becomes unhealthy, Fireworks automation detects the condition and safely remediates it, such as by removing traffic from the affected node and replacing capacity when available.

This minimizes the operational burden on your team while preserving your ownership of the underlying environment and GPU capacity.

## Capacity efficiency

Fireworks optimizes placement of workloads across the available GPUs to improve utilization. This includes consolidating compatible workloads where appropriate and balancing efficiency with reliability and performance.

## Observability and incident response

Fireworks operates the stack using metrics, logs, and dashboards for the managed serving components. Fireworks monitors the environment, investigates service-impacting issues, and coordinates with your team when an incident requires customer-side action, such as hardware capacity, cloud account or data center, networking, or policy changes.

<Note>
  Detailed Enterprise BYOC support terms are coming soon. During Private Preview, Fireworks confirms support channels, escalation paths, and any deployment-specific operational expectations during onboarding.
</Note>

## Upgrades

Fireworks updates the serving stack using managed rolling updates. Keeping the operator credential in place after setup helps Fireworks deploy upgrades, roll out model changes, and respond to incidents without requiring a new approval for every routine operational action.

Customers with strict access policies can discuss a hardened onboarding variant with Fireworks, where customer teams pre-create required cluster-scoped access structures.

## Customer coordination

BYOC operations work best when Fireworks and the customer agree on:

* Approved GPU capacity and scaling boundaries
* Customer-side change windows or approval requirements
* Contacts for networking, cloud account or data center, and capacity issues
* Support and escalation expectations
* Any environment-specific compliance requirements
