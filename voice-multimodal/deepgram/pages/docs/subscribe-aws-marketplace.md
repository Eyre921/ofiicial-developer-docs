---
title: "Subscribe on AWS Marketplace"
source: https://developers.deepgram.com/docs/subscribe-aws-marketplace.md
path: docs/subscribe-aws-marketplace
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Subscribe on AWS Marketplace

Before you can deploy Deepgram on Amazon SageMaker AI, you must subscribe to the product in the AWS Marketplace. Subscribing creates a billing agreement but does not start any charges — you are not billed for the product until you deploy an [Amazon SageMaker AI Endpoint resource](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console.html).

Subscribe through the console or the Marketplace API, then note the **Model Package ARN** you will pass to [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) or [Deploy with Terraform](/docs/terraform-deploy-sagemaker).

## Prerequisites

* An AWS account
* AWS IAM permissions to SageMaker and Marketplace
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html): AWSMarketplaceManageSubscriptions
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html): AmazonSageMakerFullAccess
* The Deepgram product you want to deploy. See [Supported Products](/docs/supported-products-sagemaker).

## Subscribe through the AWS Marketplace console

Login to the [AWS Management Console](https://console.aws.amazon.com/) for the account you'd like to deploy in

Navigate to the [AWS Marketplace console, pre-filtered for Deepgram SageMaker Model products](https://us-east-1.console.aws.amazon.com/marketplace/search#!mpSearch/search?text=deepgram\&filter%3AFULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL)

Click on the Deepgram product you're interested in deploying (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click on the **View Purchase Options** button

Ensure the **Offer Type** of **Public Offer** is selected (*if required*)

Scroll down and click the **Subscribe** button

Once the subscription is active, continue to [Find the Model Package ARN](#find-the-model-package-arn).

## Subscribe through the Marketplace API

If you provision infrastructure as code, you can subscribe to a Deepgram SageMaker product entirely through the AWS Marketplace API instead of the console. This section is an alternative to [subscribing through the console](#subscribe-through-the-aws-marketplace-console) — use whichever method fits your workflow, then continue to [Find the Model Package ARN](#find-the-model-package-arn).

The steps below use the AWS CLI, but AWS also publishes [SDKs for many languages](https://aws.amazon.com/developer/tools/) — including Python (Boto3), Node.js, Java, Go, and .NET — that expose the same Marketplace Discovery and Agreement Service APIs. Use whichever SDK fits your stack to build your own subscription automations and scripts.

Subscribing creates a billing agreement on your AWS account. You are not charged until you deploy a SageMaker Endpoint and send it traffic — the usage-based pricing term has no upfront cost — but `AcceptAgreementRequest` (the last step below) is not a dry run. It creates a real, active agreement.

### Additional permissions

The [AWSMarketplaceManageSubscriptions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html) policy referenced in [Prerequisites](#prerequisites) covers product discovery (`SearchListings`, `GetOffer`, `GetOfferTerms`, `ListPurchaseOptions`, and similar) but does **not** include the AWS Marketplace Agreement Service actions this flow also needs: `CreateAgreementRequest`, `AcceptAgreementRequest`, `DescribeAgreement`, `SearchAgreements`, and `GetAgreementTerms`. Either attach [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html) or add those five actions to a custom policy alongside `AWSMarketplaceManageSubscriptions`.

#### Find the product ID

List Deepgram's SageMaker-deployable products, filtered by fulfillment type and seller:

```bash
aws marketplace-discovery search-listings \
  --region us-east-1 \
  --filters '[
    {"filterType": "FULFILLMENT_OPTION_TYPE", "filterValues": ["SAGEMAKER_MODEL"]},
    {"filterType": "PUBLISHER", "filterValues": ["6efa21f9-9a33-4cae-ba44-756436fa71dd"]}
  ]' \
  --query 'listingSummaries[].{name:listingName,productId:associatedEntities[0].product.productId}'
```

```json
[
  {
    "name": "Deepgram Voice AI Nova-3 Monolingual Speech-to-Text (STT) Streaming",
    "productId": "prod-tnv5pm6nlcm44"
  },
  {
    "name": "Deepgram Voice AI- Aura-2 Text-to-Speech- English",
    "productId": "prod-..."
  }
]
```

`6efa21f9-9a33-4cae-ba44-756436fa71dd` is Deepgram's AWS Marketplace seller profile ID. Note the `productId` for the listing you want to deploy (eg. `prod-tnv5pm6nlcm44` for Nova-3 Monolingual Streaming).

Calls the [`SearchListings`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Find the standard offer for that product

```bash
aws marketplace-discovery list-purchase-options \
  --region us-east-1 \
  --filters '[{"filterType": "PRODUCT_ID", "filterValues": ["prod-tnv5pm6nlcm44"]}]' \
  --query 'purchaseOptions[].{offerId:purchaseOptionId,name:purchaseOptionName,badges:badges}'
```

This can return more than one purchase option — for example, a private offer your account manager extended to you, alongside the standard public offer. **The standard public offer has no `PRIVATE_PRICING` badge and no custom `purchaseOptionName`** (AWS labels it `"Offer created on <timestamp>"`). Use a private offer's ID instead if your account has negotiated pricing.

Calls the [`ListPurchaseOptions`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Get the offer's proposal ID and pricing model

```bash
aws marketplace-discovery get-offer --region us-east-1 --offer-id <offer-id-from-previous-step>
```

Note the `agreementProposalId` and `pricingModel.pricingModelType` from the response — you need both for the next steps.

Calls the [`GetOffer`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Get the offer's terms

```bash
aws marketplace-discovery get-offer-terms --region us-east-1 --offer-id <offer-id>
```

The response lists one or more terms, each with an `id`. For a `USAGE`-priced Deepgram SageMaker product, expect `LegalTerm`, `SupportTerm`, and `UsageBasedPricingTerm` — collect all three `id` values. Deepgram's public SageMaker listings also include a `FreeTrialPricingTerm` (14 days); collect its `id` too if you want to claim the trial. See [Required terms by pricing model](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-agreement-api-buyer.html#car-required-terms-by-pricing-model) if the offer uses a different pricing model.

Calls the [`GetOfferTerms`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Generate a quote

```bash
aws marketplace-agreement create-agreement-request \
  --region us-east-1 \
  --agreement-proposal-identifier <agreementProposalId-from-step-3> \
  --intent NEW \
  --requested-terms '[
    {"id": "<LegalTerm id>"},
    {"id": "<SupportTerm id>"},
    {"id": "<UsageBasedPricingTerm id>"},
    {"id": "<FreeTrialPricingTerm id>"}
  ]'
```

Returns an `agreementRequestId` and a `chargeSummary`. For usage-based pricing, `newAgreementValue` is `"0.00"` — you're only quoted for the mandatory terms, not future usage.

Calls the [`CreateAgreementRequest`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_CreateAgreementRequest.html) action of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

`FreeTrialPricingTerm` can be accepted only once per product. If your account has already used the trial for this product, omit that term's `id` from `requestedTerms` — including it again returns a `ValidationException`. If your account already has an active agreement for this product at all, the whole call fails with `ValidationException` / `UNSUPPORTED_ACTION` ("This action is not supported when an active agreement exists on the same resourceId"). Check first with the [`SearchAgreements`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html) action: `aws marketplace-agreement search-agreements --region us-east-1 --catalog AWSMarketplace --filters '[{"name":"PartyType","values":["Acceptor"]},{"name":"AgreementType","values":["PurchaseAgreement"]},{"name":"ResourceIdentifier","values":["<productId>"]}]'` — if an agreement with `"status": "ACTIVE"` already exists, you're already subscribed; skip to [Find the Model Package ARN](#find-the-model-package-arn).

#### Accept the quote to subscribe

```bash
aws marketplace-agreement accept-agreement-request \
  --region us-east-1 \
  --agreement-request-id <agreementRequestId-from-previous-step>
```

Returns the new `agreementId`. This is the subscribe action — it's equivalent to clicking **Subscribe** in the console.

Calls the [`AcceptAgreementRequest`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptAgreementRequest.html) action of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

#### Confirm the subscription is active

```bash
aws marketplace-agreement describe-agreement --region us-east-1 --agreement-id <agreementId>
```

`status` moves from `ACTIVE` immediately, but the underlying entitlement can take a few minutes to provision — the same delay you'd see waiting on the console's subscription page. Poll `aws marketplace-agreement get-agreement-entitlements --region us-east-1 --agreement-id <agreementId>` until it clears `PENDING`/`PROVISIONING_IN_PROGRESS` before continuing to [Find the Model Package ARN](#find-the-model-package-arn).

Calls the [`DescribeAgreement`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_DescribeAgreement.html) and [`GetAgreementEntitlements`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementEntitlements.html) actions of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

## Find the Model Package ARN

The AWS CLI, Boto3, and Terraform deployment paths all reference the **Model Package ARN** for the product version and AWS Region you plan to deploy. The AWS Marketplace surfaces the ARN through the CLI configuration view.

In the AWS Management Console, navigate to the [AWS Marketplace **Manage subscriptions** console](https://us-east-1.console.aws.amazon.com/marketplace/subscriptions)

On the **Active subscriptions** tab, find the subscription for the Deepgram product you want to deploy (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click the **Configure** button in the **Actions** column on the right-hand side

In the **Setup** box, under **Service**, choose **AWS command line interface (CLI)**

Under the **Version** header, select the product version from the dropdown. If the listing has more than one version, read the version name and the release notes to understand the set of languages (or features) each version provides, and choose the version that matches your needs

Scroll down. On the right-hand side of the page, a list of **Model ARNs** is shown. Note the correct Model Package ARN for the AWS Region you plan to deploy to

## Private offers

If you have received a SageMaker private offer for a management account of an AWS organization, you may use [AWS License Manager](https://aws.amazon.com/blogs/awsmarketplace/manage-your-aws-marketplace-license-entitlements-in-aws-license-manager/) to grant usage of the SageMaker private offer to member accounts within your AWS organization as a Marketplace license entitlement after accepting the offer in the payer account. If you choose not to centrally manage license entitlements with AWS License Manager, you will need to accept the private offer in each linked account individually after you have accepted the offer in the payer account to be able to launch a SageMaker Endpoint with private pricing in the linked account.

For pricing and how to request a private offer, see [Private offers](/docs/amazon-sagemaker#private-offers) on the overview page.

## Switch offers

Only one offer (public or private) can be subscribed to for each SageMaker product listing at any one time. If you already have a subscription for a listing and try to subscribe to a different offer for it (for example, subscribing to a new private offer when you previously subscribed to the public offer), the **Accept offer** button is greyed out and an *Existing subscription detected* warning ("You already have a subscription for this product.") may appear at the top of the page. To switch offers, cancel the existing subscription first:

In the warning message, click **View Subscription** to open the **Manage subscriptions** page of the AWS Marketplace console.

Find the product you're already subscribed to in the table. Click the hyperlinked agreement ID shown next to the product name.

Click the **Actions** dropdown, then click **Cancel subscription** and confirm the cancellation.

Once the subscription is cancelled, subscribe to the new offer.

## Next steps

* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) with the AWS CLI or Boto3
* [Deploy with Terraform](/docs/terraform-deploy-sagemaker)
* [Requesting SageMaker Quota](/docs/request-sagemaker-quota)
