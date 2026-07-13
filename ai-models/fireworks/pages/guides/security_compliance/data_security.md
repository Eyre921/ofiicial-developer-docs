---
title: "Data Security"
source: https://docs.fireworks.ai/guides/security_compliance/data_security
path: guides/security_compliance/data_security
---

How we secure and handle your data for inference and training

At Fireworks, protecting customer data is at the core of our platform. We design all of our systems, infrastructure, and business processes to ensure customer trust through verifiable security & compliance.

This page provides an overview of our key security measures. For documentation and audit reports, see our [Trust Center](https://trust.fireworks.ai/).

## Zero Data Retention

Fireworks does not log or store prompt or generation data for open models, without explicit user opt-in. See our [Zero Data Retention Policy](https://docs.fireworks.ai/guides/security_compliance/data_handling).

## Secure Data Handling

**Data Ownership & Control:** Customers maintain ownership of their data. Customer data stored as part of an active workflow can be permanently deleted with auditable confirmation, and secure wipe processes ensure deleted assets cannot be reconstructed.

**Encryption**: Data is encrypted in transit (TLS 1.2+) and at rest (AES-256).

**Bring Your Own Bucket:** Customers may integrate their own cloud storage to retain governance and apply their own compliance frameworks.

* Datasets: [GCS Bucket Integration](/fine-tuning/secure-fine-tuning#gcs-bucket-integration) (AWS S3 coming soon)
* Models: [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)

**Bring Your Own Key:** Customers may integrate their own AWS KMS key to retain governance and apply their own encryption policies.

* Datasets and checkpoints: [Customer-Managed Encryption Keys for Fine-Tuning](/fine-tuning/cmek) (SFT supported; DPO and RFT coming soon)
* Final model weights: Coming soon

**Access Logging:** All customer data access is logged, monitored, and protected against tampering. See [Audit & Access Logs](https://docs.fireworks.ai/guides/security_compliance/audit_logs).

## Workload Isolation

Dedicated workloads run in logically isolated environments, preventing cross-customer access or data leakage.

## Secure Training

Fireworks enables secure model training, including fine-tuning and reinforcement learning, while maintaining customer control over sensitive components and data. This approach builds on our [Zero Data Retention](#zero-data-retention) policy to ensure sensitive training data never persists on our platform.

**Customer-Controlled Architecture:** For advanced training workflows like reinforcement learning, critical components remain under customer control:

* Reward models and reward functions are kept proprietary and not shared
* Rollout servers and training metrics are built and managed by customers
* Model checkpoints are managed through secure cloud storage registries

**Minimal Data Sharing:** Training data is shared via controlled bucket access with minimal sharing and step-wise retention, limiting data exposure while enabling effective training workflows.

**API-Based Integration:** Customers leverage Fireworks' training APIs while maintaining full control over sensitive components, ensuring no cross-component data leakage.

<Tip>
  For detailed guidance on secure reinforcement fine-tuning and using your own cloud storage, see [Secure Fine Tuning](/fine-tuning/secure-fine-tuning).
</Tip>

## Technical Safeguards

* **Device Trust**: Only approved, secured devices with strong authentication can access sensitive Fireworks systems.
* **Identity & Access Management**: Fine-grained access controls are enforced across all Fireworks environments, following the principle of least privilege.
* **Network Security**
  * Private network isolation for customer workloads.
  * Firewalls and security groups prevent unauthorized inbound/outbound traffic.
  * DDoS protection is in place across core services.
* **Monitoring & Detection**: Real-time monitoring and anomaly detection systems alert on suspicious activity
* **Vulnerability Management**: Continuous scanning and patching processes keep infrastructure up to date against known threats.

## Operational Security

* **Security Reviews & Testing**: Regular penetration testing validates controls.
* **Incident Response**: A formal incident response plan ensures swift containment, customer notification, and remediation if an issue arises.
* **Employee Access**: Only a minimal subset of Fireworks personnel have access to production systems, and all access is logged and periodically reviewed.
* **Third-Party Risk Management**: Vendors and subprocessors undergo rigorous due diligence and contractual security obligations.

## Compliance & Certifications

Fireworks aligns with leading industry standards to support customer compliance obligations.

## ISO Certifications

Fireworks has achieved all three ISO certifications covering security, privacy, and AI management:

| Certification | Scope                                                             | Status     |
| ------------- | ----------------------------------------------------------------- | ---------- |
| **ISO 27001** | Information Security Management Systems (ISMS)                    | ✅ Achieved |
| **ISO 27701** | Privacy Information Management (extension to ISO 27001)           | ✅ Achieved |
| **ISO 42001** | AI Management Systems — responsible AI development and deployment | ✅ Achieved |

Certificate PDFs for all three certifications are available for download from the [Fireworks Trust Center](https://trust.fireworks.ai).

These certifications are maintained through continuous monitoring and annual audits — not one-time assessments.

### What these certifications cover

**ISO 27001** verifies that Fireworks has implemented a documented, risk-managed information security program with controls covering access, encryption, incident response, and vendor management.

**ISO 27701** extends ISO 27001 to cover privacy — including how Fireworks collects, processes, and protects personal data from customers and end users.

**ISO 42001** covers the responsible development and deployment of AI systems, including risk assessment, transparency, and bias mitigation practices.

### Other programs

* **SOC 2 Type II** (certified)
* **HIPAA Support**: Fireworks is HIPAA compliant and supports healthcare and life sciences organizations in leveraging our rapid inference capabilities with confidence.
* **Regulatory Alignment**: Controls are mapped to GDPR, CCPA, and other international data protection frameworks

<Note>
  Documentation and audit reports are available in our [Trust Center](https://trust.fireworks.ai/).
</Note>
