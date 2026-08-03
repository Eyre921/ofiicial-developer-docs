---
title: "Supported Entity Types"
source: https://developers.deepgram.com/docs/supported-entity-types.md
path: docs/supported-entity-types
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Supported Entity Types

Deepgram can [detect](/docs/detect-entities), [format](/docs/smart-format), and [redact](/docs/redaction) over 50 unique entity types. The complete inventory of supported entity types is listed in the charts below, divided into four groups: PII (Personally Identifiable Information), PHI (Protected Health Information), PCI (Payment Card Industry), and Other Entities.

When using [redaction](/docs/redaction), you can redact entire groups using `redact=pii`, `redact=phi`, or `redact=pci`. For example, `redact=phi` will redact all entity types listed in the PHI section below.

Note that some entities, such as `name` and `location`, also have subtypes. For instance, `location_city` is a subtype of `location`. This means that, in a phrase such as *I live in Boston*, the location name *Boston* will be detected as both `location` and `location_city`, with the more specific label (in this case, `location_city`) appearing in the output. Other entity types are groupings of related categories. For example, `healthcare_number` captures health plan beneficiary numbers and medical record numbers, both of which are outlined as identifiers in the HIPAA Safe Harbor provision. Similarly, `numerical_pii` covers a broad range of entity types such as MAC addresses and cookie IDs.

While entity types have English names, international variants are also redacted. For example, `ssn` covers American Social Security Numbers, as well as many equivalent identification numbers used in different regions worldwide, such as the Canadian Social Insurance Number or the German Sozialversicherungsnummer.

## Redacting Certain Entities

Deepgram's redaction functionality supports over 50 unique entity types for both pre-recorded (batch) and streaming requests. Individual entity classes can be redacted by specifying `redact=entity_class` one or more times.

You can also use redaction groups (`pci`, `pii`, `phi`, `numbers`) to redact multiple related entity types at once. See the **Redaction Groups** column in the tables below to see which groups include each entity type.

`redact=true` and `redact=numbers` redact any sequence of three or more consecutive numerals, in addition to the entity types listed in the `numbers` group below. `redact=aggressive_numbers` extends digit-sequence redaction to single- and two-digit numbers as well.

Digit-sequence redaction is independent of entity recognition. Numerals that match an entity type in the `numbers` group are tagged with the specific entity (`[CREDIT_CARD_1]`, `[SSN_1]`, etc.). Sequences caught only by the digit-length rule are replaced with a generic `[REDACTED]` placeholder.

Some entity types (`cardinal`, `ordinal`, `percent`) are not included in any redaction group. To redact these, you must specify them individually (e.g. `redact=cardinal`).

## Supported Entity Types

### **PII** (Personally Identifiable Information)

| Label                       | Description                                                                                                                                | Regulatory Compliance                                          | Redaction Groups        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------------- |
| account\_number             | Customer account or membership identification number                                                                                       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| age                         | Numbers associated with an individual’s age                                                                                                | GDPR, HIPAA, Quebec Privacy Act, APPI                          | `numbers`, `pii`        |
| bank\_account               | Bank account numbers and international equivalents, such as IBAN                                                                           | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`               |
| cardinal                    | Numerical expressions in cardinal form                                                                                                     |                                                                |                         |
| credit\_card                | Credit card numbers                                                                                                                        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pci`        |
| credit\_card\_expiration    | Expiration date of a credit card                                                                                                           | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pci`        |
| cvv                         | 3- or 4-digit card verification codes and equivalents                                                                                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pci`        |
| date                        | Specific calendar dates, which can include days of the week, dates, months, or years                                                       | HIPAA, Quebec Privacy Act                                      | `numbers`, `pii`        |
| date\_interval              | Broader time periods, including date ranges, months, seasons, years, and decades                                                           | HIPAA                                                          | `numbers`, `pii`        |
| dob                         | Dates of birth                                                                                                                             | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| email\_address              | Email addresses                                                                                                                            | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| event                       | Names of events or holidays                                                                                                                |                                                                | `pii`                   |
| filename                    | Names of computer files, including the extension or filepath                                                                               |                                                                | `pii`                   |
| gender\_sexuality           | Terms indicating gender identity or sexual orientation, including slang terms                                                              | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     | `pii`                   |
| healthcare\_number          | Healthcare numbers and health plan beneficiary numbers                                                                                     | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| ip\_address                 | Internet IP address, including IPv4 and IPv6 formats                                                                                       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| location                    | Metaclass for any named location reference                                                                                                 | GDPR, HIPAA, APPI                                              | `numbers`, `pii`        |
| location\_address           | Full or partial physical mailing addresses                                                                                                 | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| location\_city              | Municipality names, including villages, towns, and cities                                                                                  | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| location\_coordinate        | Geographic positions referred to using latitude, longitude, and/or elevation coordinates                                                   | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| location\_country           | Country names                                                                                                                              | GDPR, APPI                                                     | `pii`                   |
| location\_state             | State, province, territory, or prefecture names                                                                                            | GDPR, APPI                                                     | `pii`                   |
| location\_zip               | Zip codes (including Zip+4), postcodes, or postal codes                                                                                    | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| money                       | Names and/or amounts of currency                                                                                                           |                                                                | `numbers`, `pii`        |
| name                        | Names of individuals, not including personal titles such as ‘Mrs.’ or ‘Mr.’                                                                | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| name\_given                 | Names given to an individual, usually at birth; often first / middle names in Western cultures and middle / last names in Eastern cultures | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| name\_family                | Names indicating a person’s family or community; often a last name in Western cultures and first name in Eastern cultures                  | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| name\_medical\_professional | Names including the title of a medical professional, such a "Doctor"                                                                       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `pii`                   |
| numerical\_pii              | Numerical PII that doesn’t fall under other categories                                                                                     | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| occupation                  | Job titles or professions                                                                                                                  | Quebec Privacy Act, APPI                                       | `pii`                   |
| ordinal                     | Numerical expressions in ordinal form                                                                                                      |                                                                |                         |
| origin                      | Terms indicating nationality, ethnicity, or provenance                                                                                     | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive | `pii`                   |
| passport\_number            | Passport numbers, issued by any country                                                                                                    | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| password                    | Account passwords, PINs, access keys, or verification answers                                                                              | CPRA, APPI                                                     | `numbers`, `pii`, `pin` |
| percent                     | Numerical expressions as percentages                                                                                                       |                                                                |                         |
| phone\_number               | Telephone or fax numbers                                                                                                                   | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| physical\_attribute         | Distinctive bodily attributes, including terms indicating race                                                                             | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     | `pii`                   |
| ssn                         | Social Security Numbers or international equivalent government identification numbers                                                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    | `numbers`, `pii`        |
| time                        | Expressions indicating clock times                                                                                                         |                                                                | `numbers`, `pii`        |
| url                         | Internet addresses                                                                                                                         | CPRA, GDPR, HIPAA, Quebec Privacy Act                          | `pii`                   |
| username                    | Usernames, login names, or handles                                                                                                         | CPRA, GDPR, APPI                                               | `pii`                   |
| vehicle\_id                 | Vehicle identification numbers (VINs), vehicle serial numbers, and license plate numbers                                                   | CPRA, GDPR, HIPAA, APPI                                        | `numbers`, `pii`        |

### **PHI** (Protected Health Information)

| Label            | Description                                                           | Regulatory Compliance                                 | Redaction Groups |
| ---------------- | --------------------------------------------------------------------- | ----------------------------------------------------- | ---------------- |
| condition        | Names of medical conditions, diseases, syndromes, deficits, disorders | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive | `phi`            |
| drug             | Medications, vitamins, and supplements                                | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive | `phi`            |
| injury           | Bodily injuries, including mutations, miscarriages, and dislocations  | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive | `phi`            |
| blood\_type      | Blood types                                                           | CPRA, GDPR, HIPAA, Quebec Privacy Act                 | `phi`            |
| medical\_process | Medical processes, including treatments, procedures, and tests        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive | `phi`            |
| statistics       | Medical statistics                                                    | HIPAA, Quebec Privacy Act                             | `numbers`, `phi` |

### **PCI** (Payment Card Industry)

| Label                    | Description                                           | Regulatory Compliance                       | Redaction Groups               |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------- | ------------------------------ |
| credit\_card             | Credit card numbers                                   | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI | `numbers`, `pci`               |
| credit\_card\_expiration | Expiration date of a credit card                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI | `numbers`, `pci`, `expiration` |
| cvv                      | 3- or 4-digit card verification codes and equivalents | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI | `numbers`, `pci`               |

### **Other Entities**

| Label                  | Description                                                    | Regulatory Compliance                                          | Redaction Groups |
| ---------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | ---------------- |
| language               | Names of natural languages                                     | GDPR, GDPR Sensitive, APPI Sensitive                           | `pii`            |
| marital\_status        | Terms indicating marital status                                | APPI Sensitive                                                 | `pii`            |
| organization           | Names of organizations or departments within an organization   | Quebec Privacy Act, APPI                                       | `pii`            |
| political\_affiliation | Terms referring to a political party, movement, or ideology    | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive | `pii`            |
| religion               | Terms indicating religious affiliation                         | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive | `pii`            |
| routing\_number        | Routing number associated with a bank or financial institution |                                                                | `numbers`        |
| zodiac\_sign           | Names of Zodiac signs                                          |                                                                | `pii`            |

---
