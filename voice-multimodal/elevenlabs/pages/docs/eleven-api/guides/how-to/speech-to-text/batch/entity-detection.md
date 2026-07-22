---
title: "Entity detection"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection.md
path: docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Entity detection

**How-to guide** · Assumes you have completed the [Speech to Text
quickstart](/docs/eleven-api/guides/cookbooks/speech-to-text).

## Overview

Entity detection comes at an additional cost. See the [API pricing
page](https://elevenlabs.io/pricing?price.section=speech_to_text\&price.sections=speech_to_text,speech_to_text#pricing-table)
for detailed pricing information.

Entity detection is a feature that allows you to detect specific words and phrases in the transcript, providing their exact timestamps. This is useful to detect credit card numbers, names, medical conditions or SSNs which can then be redacted.

When enabled, the model will detect specific entity types in the transcript and provide their exact timestamps.

For example, the following audio:

<elevenlabs-audio-player audio-title="Entity detection example" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/stt-entity-detection-pii.mp3" />

Outputs the following transcript when we specify `"pii"` (Personally Identifiable Information) as the entity type:

```json maxLines=0
{
  "language_code": "eng",
  "language_probability": 0.9869821071624756,
  "text": "My name is Jill. My date of birth is the 12th of July 1987, and my credit card number is 4242-4242-4242-4242.",
  "words": [
    { "text": "My", "start": 0.099, "end": 0.259, "type": "word", "logprob": 0.0 },
    { "text": " ", "start": 0.259, "end": 0.299, "type": "spacing", "logprob": 0.0 },
    { "text": "name", "start": 0.299, "end": 0.42, "type": "word", "logprob": 0.0 },
    ...
  ],
  "transcription_id": "Y2ZX8AxHUzTPCIualYiE",
  "entities": [
    {
      "text": "Jill",
      "entity_type": "name",
      "start_char": 11,
      "end_char": 15
    },
    {
      "text": "12th of July 1987",
      "entity_type": "dob",
      "start_char": 41,
      "end_char": 58
    },
    {
      "text": "4242-4242-4242-4242",
      "entity_type": "credit_card",
      "start_char": 89,
      "end_char": 108
    }
  ]
}
```

The result shows the PII entities detected in the transcript, with their exact timestamps.

## Integrating entity detection

Entity detection is integrated into the Speech to Text API by passing the `entity_detection` parameter to the `convert` method.

```python maxLines=0
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_url = (
    "https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/stt-entity-detection-pii.mp3"
)
response = requests.get(audio_url)
audio_data = BytesIO(response.content)

transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v2", # Model to use
    # Entity types to detect, accepts a list of specific entity types or categories.
    # To detect all entity types, use the "all" category.
    entity_detection=["pii"],
)

print("Entities detected:", transcription.entities)
```

```typescript maxLines=0
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

const response = await fetch(
  "https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/stt-entity-detection-pii.mp3"
);
const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

const transcription = await elevenlabs.speechToText.convert({
  file: audioBlob,
  modelId: "scribe_v2", // Model to use
  // Entity types to detect, accepts a list of specific entity types or categories.
  // To detect all entity types, use the "all" category.
  entityDetection: ["pii"],
});

console.log("Entities detected:", transcription.entities);
```

## Entity types

The following entity types are supported for detection. You can detect entire groups using the category keywords `pii`, `phi`, `pci`, `other`, or `offensive_language`, or specify individual entity types by their label. To detect all entity types, use the `all` category.

#### PII (Personally Identifiable Information)

| Label                       | Description                                                                                  | Regulatory Compliance                                          |
| --------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `account_number`            | Customer account or membership identification number                                         | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `age`                       | Numbers associated with an individual's age                                                  | GDPR, HIPAA, Quebec Privacy Act, APPI                          |
| `bank_account`              | Bank account numbers and international equivalents, such as IBAN                             | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `cardinal`                  | Numerical expressions in cardinal form                                                       |                                                                |
| `credit_card`               | Credit card numbers                                                                          | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `credit_card_expiration`    | Expiration date of a credit card                                                             | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `cvv`                       | 3- or 4-digit card verification codes and equivalents                                        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `date`                      | Specific calendar dates, which can include days of the week, dates, months, or years         | HIPAA, Quebec Privacy Act                                      |
| `date_interval`             | Broader time periods, including date ranges, months, seasons, years, and decades             | HIPAA                                                          |
| `dob`                       | Dates of birth                                                                               | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `driver_license`            | Driver's permit numbers                                                                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `email_address`             | Email addresses                                                                              | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `event`                     | Names of events or holidays                                                                  |                                                                |
| `filename`                  | Names of computer files, including the extension or filepath                                 |                                                                |
| `gender`                    | Terms indicating gender identity, including slang terms                                      | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     |
| `gender_sexuality`          | Legacy alias covering both `gender` and `sexual_orientation`                                 | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     |
| `sexual_orientation`        | Terms indicating sexual orientation, including slang terms                                   | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     |
| `healthcare_number`         | Healthcare numbers and health plan beneficiary numbers                                       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `ip_address`                | Internet IP address, including IPv4 and IPv6 formats                                         | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `location`                  | Metaclass for any named location reference                                                   | GDPR, HIPAA, APPI                                              |
| `location_address`          | Full or partial physical mailing addresses                                                   | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `location_city`             | Municipality names, including villages, towns, and cities                                    | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `location_coordinate`       | Geographic positions referred to using latitude, longitude, and/or elevation coordinates     | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `location_country`          | Country names                                                                                | GDPR, APPI                                                     |
| `location_state`            | State, province, territory, or prefecture names                                              | GDPR, APPI                                                     |
| `location_zip`              | ZIP codes (including ZIP+4), postcodes, or postal codes                                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `money`                     | Names and/or amounts of currency                                                             |                                                                |
| `name`                      | Names of individuals, not including personal titles such as 'Mrs.' or 'Mr.'                  | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `name_given`                | Names given to an individual, usually at birth; often first/middle names in Western cultures | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `name_family`               | Names indicating a person's family or community; often a last name in Western cultures       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `name_medical_professional` | Names including the title of a medical professional, such as "Doctor"                        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `numerical_pii`             | Numerical PII that doesn't fall under other categories                                       | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `occupation`                | Job titles or professions                                                                    | Quebec Privacy Act, APPI                                       |
| `ordinal`                   | Numerical expressions in ordinal form                                                        |                                                                |
| `origin`                    | Terms indicating nationality, ethnicity, or provenance                                       | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive |
| `passport_number`           | Passport numbers, issued by any country                                                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `password`                  | Account passwords, PINs, access keys, or verification answers                                | CPRA, APPI                                                     |
| `percent`                   | Numerical expressions as percentages                                                         |                                                                |
| `phone_number`              | Telephone or fax numbers                                                                     | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `physical_attribute`        | Distinctive bodily attributes, including terms indicating race                               | CPRA, GDPR, GDPR Sensitive, APPI Sensitive                     |
| `ssn`                       | Social Security Numbers or international equivalent government identification numbers        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI                    |
| `time`                      | Expressions indicating clock times                                                           |                                                                |
| `url`                       | Internet addresses                                                                           | CPRA, GDPR, HIPAA, Quebec Privacy Act                          |
| `username`                  | Usernames, login names, or handles                                                           | CPRA, GDPR, APPI                                               |
| `vehicle_id`                | Vehicle identification numbers (VINs), vehicle serial numbers, and license plate numbers     | CPRA, GDPR, HIPAA, APPI                                        |

#### PHI (Protected Health Information)

| Label                  | Description                                                           | Regulatory Compliance                                 |
| ---------------------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
| `condition`            | Names of medical conditions, diseases, syndromes, deficits, disorders | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive |
| `drug`                 | Medications, vitamins, and supplements                                | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive |
| `injury`               | Bodily injuries, including mutations, miscarriages, and dislocations  | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive |
| `blood_type`           | Blood types                                                           | CPRA, GDPR, HIPAA, Quebec Privacy Act                 |
| `medical_process`      | Medical processes, including treatments, procedures, and tests        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive |
| `clinical_measurement` | Clinical measurements, vitals, and lab results                        | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI Sensitive |
| `statistics`           | Legacy alias for `clinical_measurement`                               | HIPAA, Quebec Privacy Act                             |

#### PCI (Payment Card Industry)

| Label                    | Description                                           | Regulatory Compliance                       |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------- |
| `credit_card`            | Credit card numbers                                   | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI |
| `credit_card_expiration` | Expiration date of a credit card                      | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI |
| `cvv`                    | 3- or 4-digit card verification codes and equivalents | CPRA, GDPR, HIPAA, Quebec Privacy Act, APPI |

#### Other entities

| Label                   | Description                                                    | Regulatory Compliance                                          |
| ----------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `language`              | Names of natural languages                                     | GDPR, GDPR Sensitive, APPI Sensitive                           |
| `marital_status`        | Terms indicating marital status                                | APPI Sensitive                                                 |
| `organization`          | Names of organizations or departments within an organization   | Quebec Privacy Act, APPI                                       |
| `political_affiliation` | Terms referring to a political party, movement, or ideology    | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive |
| `religion`              | Terms indicating religious affiliation                         | CPRA, GDPR, GDPR Sensitive, Quebec Privacy Act, APPI Sensitive |
| `routing_number`        | Routing number associated with a bank or financial institution |                                                                |
| `zodiac_sign`           | Names of Zodiac signs                                          |                                                                |
| `product_or_service`    | Names of commercial products or services                       |                                                                |
| `food_or_beverage`      | Names of foods, drinks, and dishes                             |                                                                |
| `document_reference`    | References to documents, case numbers, or file identifiers     |                                                                |
| `generic_id`            | Generic identifiers that don't fall under other ID categories  |                                                                |
| `measurement`           | Physical measurements and quantities with units                |                                                                |
| `time_duration`         | Expressions indicating a length or span of time                |                                                                |

#### Offensive language

| Label                     | Description                                  | Regulatory Compliance |
| ------------------------- | -------------------------------------------- | --------------------- |
| `very_offensive_language` | Strongly offensive language, including slurs |                       |
| `less_offensive_language` | Mildly offensive or inappropriate language   |                       |

## Entity redaction

In addition to detecting entities, you can redact them from the transcript text with the
`entity_redaction` parameter. It accepts the same format as `entity_detection`: `all`, a
category keyword, or a list of specific entity types. The redacted types must be a subset of
the detected types.

When redaction is enabled, matched entity text is replaced with a marker in both the
transcript text and the word-level output, and the `entities` field is not returned in the
response.

```python
transcription = elevenlabs.speech_to_text.convert(
    file=audio_file,
    model_id="scribe_v2",
    entity_detection=["pii"],
    entity_redaction=["pii"],
    entity_redaction_mode="enumerated_entity_type",
)

print(transcription.text)
# "Hi {NAME_0}, your card ending in {CREDIT_CARD_0} was declined."
```

```typescript
const transcription = await elevenlabs.speechToText.convert({
  file: audioBlob,
  modelId: "scribe_v2",
  entityDetection: ["pii"],
  entityRedaction: ["pii"],
  entityRedactionMode: "enumerated_entity_type",
});

console.log(transcription.text);
// "Hi {NAME_0}, your card ending in {CREDIT_CARD_0} was declined."
```

The `entity_redaction_mode` parameter controls the marker format:

| Mode                     | Marker                                     | Example                 |
| ------------------------ | ------------------------------------------ | ----------------------- |
| `redacted`               | `{REDACTED}` for every entity              | `Hi {REDACTED}`         |
| `entity_type`            | The entity type in braces                  | `Hi {NAME}`             |
| `enumerated_entity_type` | The entity type plus an occurrence counter | `Hi {NAME_0}` (default) |

Entity detection and redaction are not supported with the `combined` multichannel output style.

## Next steps

#### [API reference](/docs/api-reference/speech-to-text)

Full Speech to Text API reference and parameters.

#### [Multichannel transcription](/docs/eleven-api/guides/how-to/speech-to-text/batch/multichannel-transcription)

Transcribe multi-channel audio with per-channel speaker attribution.
