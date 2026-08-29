---
title: "How Setup Works"
source: https://docs.fireworks.ai/ecosystem/integrations/byoc/how-setup-works
path: ecosystem/integrations/byoc/how-setup-works
---

Understand the high-level onboarding flow for Bring Your Own Cluster.

This page describes the high-level setup flow for Enterprise customers onboarding to Bring Your Own Cluster (BYOC).

<Note>
  Bring Your Own Cluster is in Private Preview for Enterprise customers. Contact [sales@fireworks.ai](mailto:sales@fireworks.ai) to participate in the preview and confirm the onboarding path for your environment.
</Note>

## Prerequisites

Before installation, Fireworks works with your team to confirm that the target environment can support BYOC.

At a high level, you need:

* A Kubernetes cluster with NVIDIA GPU nodes
* Network configuration that allows Fireworks to manage the cluster
* A customer-approved endpoint and DNS plan
* An administrative credential for the setup phase

Fireworks supports BYOC on major cloud providers and their managed Kubernetes offerings, select GPU cloud providers, and on-premises environments that provide a reachable Kubernetes endpoint, supported NVIDIA GPU nodes, and the required network setup. Fireworks confirms provider, environment, GPU capacity, and networking support during preview onboarding.

<Warning>
  Training is not supported in BYOC during Private Preview.
</Warning>

## Setup flow

<Steps>
  <Step title="Provision the cluster">
    Your team provisions the Kubernetes cluster with NVIDIA GPU nodes, or provisions it jointly with Fireworks during onboarding. You retain ownership of the cloud account or data center environment, cluster, GPU nodes, and networking.
  </Step>

  <Step title="Grant setup access">
    You grant Fireworks an administrative credential to the cluster for setup. Fireworks recommends a dedicated, clearly named, revocable credential so your team can audit and manage access through your normal governance process.
  </Step>

  <Step title="Install the serving stack">
    Fireworks installs the serving stack using managed deployment tooling such as Helm or GitOps. During installation, Fireworks creates scoped-down Kubernetes identities and roles for the components that run in the cluster.
  </Step>

  <Step title="Configure networking and DNS">
    Fireworks works with your team to configure networking and DNS so your customer endpoint is reachable through the Fireworks API experience while inference request and response handling runs in your environment.
  </Step>

  <Step title="Validate and deploy models">
    Fireworks validates the cluster, then deploys inference workloads into the environment. After validation, your applications use the same Fireworks APIs and SDKs used across the rest of the platform.
  </Step>
</Steps>

## Access model during setup

Installation requires an administrative Kubernetes credential because the platform must create cluster-scoped resources, namespaces, standard dependency resources, and node-level scheduling configuration. This is a Kubernetes permission requirement for installing and operating a platform inside a cluster.

After installation, day-to-day workloads run under scoped service identities created for each component.

## Validation

Before the cluster is used for production traffic, Fireworks validates the environment with your team. Validation typically covers:

* GPU node readiness and scheduling behavior
* Endpoint reachability
* Routing and load balancing behavior
* Autoscaling behavior within the available GPU capacity
* Observability signals used for ongoing operations

## After onboarding

Once validation is complete, Fireworks operates the serving stack and model lifecycle in the cluster. Your team continues to own the cloud account or data center environment, network policy, GPU capacity, and any customer-side approval processes.

For ongoing responsibilities, see [Operational Model](/ecosystem/integrations/byoc/operational-model).
