---
title: "Data Privacy Compliance"
source: https://developers.deepgram.com/trust-security/data-privacy-compliance.md
path: trust-security/data-privacy-compliance
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Data Privacy Compliance

Deepgram maintains and meets the requirements for multiple data privacy compliance frameworks and certifications. To request Deepgram compliance documentation, talk to your Account Executive.

## SOC 2

Deepgram has achieved SOC 2 Type 1 and Type 2 certification. An independent auditor has evaluated the security controls and procedures we use to protect the data we process in the cloud and has assessed the operational effectiveness of our systems.

<h2> SOC 2 Certificates </h2>
For access to SOC 2 certificates, please [contact us](https://deepgram.com/contact-us).

## GDPR

Deepgram is GDPR ready. We provide information to our customers to help them understand how features and functionality of our platform may affect their GDPR compliance obligations.

For customers requiring data processing within the European Union, Deepgram provides an EU-specific endpoint at `api.eu.deepgram.com`. See our [Regional Endpoints](/reference/regional-endpoints) documentation for more information.

## Australian Privacy Principles (APP 8)

Deepgram is built for Australia's privacy requirements. We support customers operating under the Australian Privacy Principles, including [APP 8](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-8-app-8-cross-border-disclosure-of-personal-information)'s cross-border disclosure accountability standard for any personal information in customer content.

For customers who require data residency in Australia, Deepgram also provides an AU-specific endpoint at `api.au.deepgram.com`. It runs exclusively on Australian infrastructure (AWS `ap-southeast-2`, Sydney). Storage and inference both happen in-country — not storage alone.

Additionally, Deepgram supports customers operating under Australia's strictest frameworks — including the My Health Records Act — whose compliance obligations require that all processing activities, including access, occur in Australia. Opting out of MIP (`mip_opt_out=true`) satisfies that requirement: no customer content is accessed or otherwise processed across Australian borders for any purpose.

Voice Agent customers using a third-party LLM for the `think` step should confirm that provider's residency and processing guarantees independently. Deepgram runs `listen` and `speak` on Australian infrastructure; the `think` step runs on the third-party provider's infrastructure, which may process data outside Australia.

To review these commitments in contract form, [contact us](https://deepgram.com/contact-us) for the AU Data Processing Agreement.

## HIPAA

Deepgram is considered a Business Associate as defined by the US [HIPAA](https://www.hhs.gov/hipaa/index.html) legislation.

For Deepgram customers who qualify as a Covered Entity under US HIPAA legislation and related legislation and regulations and who provide ePHI (electronic Protected Health Information) to us, Deepgram may qualify as a business associate. We can provide our Business Associate Agreement to such customers upon request.

<h2> Business Associate Agreement </h2>
To secure a BAA (Business Associate Agreement) with Deepgram, please [contact us](https://deepgram.com/contact-us).

## CCPA

We are compliant with the California Consumer Privacy Act of 2018 (CCPA), which secures privacy rights for California consumers and gives them more control over the personal information that businesses collect about them. You can view [our privacy policy](https://deepgram.com/privacy/) on [our website](https://deepgram.com/).

## PCI

We are PCI compliant, and perform a yearly review of our standing within the framework.
