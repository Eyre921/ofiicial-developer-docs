---
title: "High risk merchant lists"
source: https://docs.stripe.com/disputes/match.md
path: disputes/match
---

# Terminated merchant files

Learn about the Mastercard (MATCH) and Visa (VMSS) databases.

Visa and Mastercard operate global databases known as terminated merchant files (TMF), specifically Mastercard’s MATCH and Visa’s VMSS. Acquirers must screen all applicants against these databases before approval and report any merchant they terminate for fraud, severe policy violations, or excessive chargebacks.

A TMF listing creates a severe industry-wide restriction, as most processors automatically reject listed businesses or principal owners. Listings remain active for 5 years. Only the specific acquiring bank that initiated the listing can request a removal or correction.

## MATCH

Member Alert to Control High-Risk Merchants (MATCH) is Mastercard’s global database of businesses terminated by acquirers because of severe rule violations, fraud, or high chargebacks.

### MATCH qualification and reporting

Acquirers must review every terminated account against MATCH criteria. If the merchant qualifies, the acquirer must add them to the database within 1 business day of termination or eligibility.

#### MATCH Qualitative Criteria

Acquirers categorize MATCH listings using 11 standard reason codes based on rule violations.

| Code | Reason | Description |
| --- | --- | --- |
| 1 | Account Data Compromise | An occurrence that results in the unauthorized access to or disclosure of account data. |
| 2 | Common Point of Purchase | Account data is stolen at the merchant and then used for fraudulent purchases at other merchant locations. |
| 3 | Laundering | The merchant was engaged in laundering activity. Laundering means that a merchant presented  transaction records to its acquirer that weren’t valid transactions for sales of goods or services between that merchant and an actual cardholder. |
| 7 | Fraud Conviction | There was a criminal fraud conviction of a principal owner or partner of the merchant. |
| 8 | Mastercard Questionable Merchant Audit Program | The merchant was determined to be a questionable merchant as per the criteria set forth in the Mastercard questionable merchant audit program. |
| 9 | Bankruptcy/Liquidation/Insolvency | The merchant was unable or is likely to become unable to discharge its financial obligations. |
| 10 | Violation of Standards | The merchant was in violation of one or more standards that describe procedures to be employed by the merchant in transactions that cards are used in, including, by way of example and not limitation, the standards for honoring all cards, displaying the marks, charges to cardholders, minimum and maximum transaction amount restrictions, and prohibited transactions set forth in chapter 5 of the Mastercard Rules manual. |
| 11 | Merchant Collusion | The merchant participated in fraudulent collusive activity. |
| 12 | PCIDSS Non-Compliance | The merchant failed to comply with Payment Card Industry (PCI) Data Security Standard (DSS) requirements. |
| 13 | Illegal Transactions | The merchant was engaged in illegal Transactions. |
| 14 | Identity Theft | The acquirer has reason to believe that the identity of the listed merchant or its principal owners was unlawfully assumed for the purpose of unlawfully entering into a merchant Agreement. |

#### MATCH quantitative criteria

Mastercard defines specific numeric thresholds for the two most common MATCH reason codes: Excessive Chargebacks and Excessive Fraud. Merchants can trigger these codes based strictly on transaction volume, even without intentional rule violations.

| Code | Reason | Description |
| --- | --- | --- |
| 4 | Excessive Chargebacks | Merchants trigger this code when monthly Mastercard chargebacks exceed 1% of total monthly Mastercard sales transactions and total 5,000 USD or more. Both thresholds must be met in the same month to qualify. |
| 5 | Excessive Fraud | Merchants trigger this code when monthly fraud-to-sales dollar volume reaches 8% or greater, and the merchant processes 10 or more fraudulent transactions totaling 5,000 USD or more. All conditions must be met within the same calendar month. |

### Network differences and timing rules

The dispute data used to calculate Code 04 relies entirely on Mastercard transactions. Other networks can still request a MATCH listing if a merchant breaches their specific monitoring thresholds or incurs network fines.

All calculations measure chargebacks and sales transactions processed within the same calendar month, regardless of when the original purchase occurred.

Furthermore, closing a processing account doesn’t prevent a listing. Acquirers must add a merchant to MATCH if they meet the criteria, even if the violation occurs or the relationship officially ends months after account closure.

#### Sample qualification scenario

Consider a merchant that records 125 Mastercard transactions and 6 Mastercard chargebacks totaling 6,250 USD in a single calendar month. This activity represents a 4.8% dispute ratio. Because both thresholds are crossed, the ratio exceeds 1% and the total volume exceeds 5,000 USD, the business qualifies for a MATCH listing upon termination. Winning or reversing the chargebacks later doesn’t alter this status. Mastercard doesn’t require a minimum count of individual chargebacks to trigger an excessive chargeback listing.

### Information added to MATCH

The card networks require that the following information be added to MATCH:

- Business Legal Name and DBA
- Business Address
- Business Phone Number
- Business Tax ID
- Business URL
- Principal Owner Name
- Principal Owner Address
- Principal Owner Phone Number
- Principal Owner Tax ID
- Account Opening Date and Termination Date
- MATCH Reason Code

Stripe doesn’t disclose MATCH database information to users.

### MATCH entry removal

An acquirer can only remove a MATCH listing under two conditions.

First, the acquirer must have added the merchant to the database in error.

Second, if the merchant was listed under Reason Code 12 for PCI DSS noncompliance, the acquirer can remove the listing after verifying that the merchant has achieved full compliance.

Merchants who meet either removal condition must contact the specific acquirer that issued the listing.

If the listing acquirer is unknown, merchants can email Mastercard directly at matchbusinessowner@mastercard.com to request their listing details.

### Stripe MATCH processing limitations

A MATCH listing generally disqualifies a merchant from processing with Stripe. Because Mastercard dictates the database rules, Stripe can’t remove a merchant that met the excessive chargeback criteria, even if the business has resolved its dispute issues. Stripe can only consider processing for a listed merchant if they provide proof of an extenuating circumstance, such as being a verified victim of identity theft under Reason Code 14.

## VMSS

Visa Merchant Screening Service (VMSS) is Visa’s global database of merchants terminated by acquirers because of severe rule violations, fraud, or high chargebacks.

### VMSS qualification and reporting

Acquirers must review every terminated account against VMSS criteria. If the merchant qualifies, the acquirer must report the business and its principal owners to the VMSS database.

#### VMSS qualitative criteria

Acquirers categorize VMSS listings using 13 standard reason codes based on rule violations, illegal activity, and collusion.

The Identity Theft reason code applies when an unauthorized user opens an account using stolen credentials. This specific listing flags potential identity fraud for future acquirers without penalizing the actual identity theft victim.

| Code | Reason | Description |
| --- | --- | --- |
| 23 | Transaction Laundering | The merchant or third party agent misrepresented the source of submitted transactions (unauthorized aggregation), or submitted transactions on behalf of another merchant (factoring). |
| 24 | Illegal Transactions | The merchant or third party agent submitted unlawful or prohibited transactions into the payment system. |
| 25 | Visa Risk Compliance Program Identification | The merchant or third party agent was terminated at the acquirer’s discretion after identification in a Visa risk compliance program and didn’t adequately remediate. |
| 26 | Merchant Collusion | The merchant or third party agent colluded to commit fraud. |
| 27 | Common Point of Purchase (CPP) | The merchant or third party agent was identified as a location where account data from legitimate transactions was compromised for use in subsequent fraudulent activity (including skimming) and didn’t adequately remediate. |
| 28 | Fraud Conviction | The principal owners of a merchant outlet or third party agent were convicted of a fraud crime. |
| 29 | Bankruptcy/Liquidation/Insolvency | The merchant or third party agent can’t fulfill its financial obligations because of potential or actual bankruptcy, insolvency, or suspension of business operations. |
| 30 | Violation of Merchant or Third Party Agent Agreement | The merchant or third party agent breached their agreement. |
| 31 | Violation of the Visa Rules | The merchant or third party agent violated the Visa rules exposing the acquirer of the payment system to undue risk. |
| 32 | Account Information Security Program Noncompliance | The merchant or third party agent was non-compliant with the Payment Card Industry Data Security Standard (PCI DSS) or the Payment Application Data Security Standard (PA-DSS) requirements. |
| 33 | Account Data Compromise | The merchant or third party agent suffered a data breach, directly or indirectly resulting in an unauthorized disclosure of payment account or transaction information. |
| 34 | Merchant Identity Theft | The merchant application was submitted using principal owner or corporate officer information belonging to individuals that were never a party to the merchant agreement. |
| 35 | Disqualification from the Visa Payment System | Visa disqualified the merchant or third party agent from participating in the Visa payment system. |

#### VMSS quantitative criteria

Visa defines specific numeric thresholds for its two most common reason codes: excessive chargebacks and excessive fraud. Merchants can trigger these listings based strictly on transaction metrics, even without intentional rule violations.

| Code | Reason | Description |
| --- | --- | --- |
| 21 | Excessive Fraud | The merchant or third party agent submitted excessive fraudulent transactions (an amount of 250,000 USD fraud and 1.8 percent, which translates to 180 basis points of a fraud-to-sales amount ratio in any single month) into the payment system, and didn’t adequately remediate. |
| 22 | Excessive Disputes | The merchant or third party agent generated excessive disputes (1,000 dispute count and 1.8 percent, which translates to 180 basis points dispute-to-sales amount ratio in any single month) into payment system and didn’t adequately remediate. |

### VMSS entry removal

Listings remain active in the VMSS database for 5 years.

Visa doesn’t  allow merchants to appeal listings directly, nor do they allow banks to delete an entry only because a merchant resolves their chargeback issues. The bank that issued the listing can only modify or delete the file if they confirm that the original entry was made in error.

Merchants who don’t know which acquiring bank placed them on the database might attempt to contact Visa directly through the Visa “Contact Us” page to see if they can locate the listing source.

### Stripe VMSS processing limitations

A VMSS listing generally disqualifies a merchant from processing with Stripe. Stripe can’t remove a merchant that met Visa’s excessive chargeback criteria, regardless of any subsequent dispute remediation.

