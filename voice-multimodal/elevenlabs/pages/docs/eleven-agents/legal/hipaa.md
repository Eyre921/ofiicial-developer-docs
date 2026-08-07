---
title: "HIPAA"
source: https://elevenlabs.io/docs/eleven-agents/legal/hipaa.md
path: docs/eleven-agents/legal/hipaa
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# HIPAA

## Overview

ElevenLabs Agents is one of ElevenLabs' HIPAA-eligible services, and we offer Business Associate Agreements (BAAs) to eligible customers. To the extent Covered Entities and Business Associates, as defined under HIPAA, have executed a BAA and have Zero Retention Mode engaged, ElevenLabs allows such customers to develop AI-powered voice agents for the handling Protected Health Information (PHI). The application of Zero Retention Mode is designed to promote compliance with HIPAA by limiting the processing of such PHI. You can read more about [Zero Retention Mode here](/docs/eleven-api/resources/zero-retention-mode).

## Controls designed to promote HIPAA compliance

When HIPAA compliance is required for a workspace, and to the extent a BAA has been executed with ElevenLabs, the following policies are enabled:

1. **Zero Retention Mode** - You can read more about [Zero Retention Mode here](/docs/eleven-api/resources/zero-retention-mode)
2. **LLM Provider Restrictions** - Only LLM from providers with whom we have a BAA in place are available as preconfigured options
3. **Storage Limitations** - Raw audio files and transcripts containing PHI are not retained

If you want to use LLMs that aren't available preconfigured in Zero Retention Mode, you can still use them in ElevenAgents by:

1. Arranging to sign a BAA directly with the LLM provider you'd like to use
2. Using your API key with our Custom LLM integration
3. Notify ElevenLabs Support of your intention to use a Custom LLM while Zero Retention Mode is active to have the setting enabled.

To the extent Zero Retention Mode is engaged, ElevenLabs' platform is designed to ensure that PHI shared as part of a conversation is not stored or logged in any system component, including:

* Conversation transcripts
* Audio recordings
* Tool calls and results
* Data analytics
* System logs

For ElevenAgents, your BAA applies only to the extent provided therein. To the extent you wish to
forego Zero Retention Mode with respect to any ElevenLabs agent, no PHI should be submitted to the
Service in connection therewith, and such agent is no longer deemed a covered service for purposes
of the BAA. Notwithstanding anything to the contrary, while ElevenLabs' ElevenAgents Service,
coupled with Zero Retention Mode, is designed to promote compliance with HIPAA, you are fully
responsible for ensuring compliance with all obligations applicable to you and for ensuring your
use of the Services is compliant with all applicable laws.

## Enterprise customers

Execution of a BAA, as may be required by HIPAA, is only available for Enterprise tier
subscriptions. Contact your account representative to discuss further. PHI should not be submitted
to the ElevenLabs Services unless a BAA is in place and only to the extent permitted under such
BAA.

## Available LLMs

When operating in Zero Retention Mode, only the following LLMs are available:

#### Google Models

* Gemini 2.5 Flash
* Gemini 2.5 Flash Lite
* Gemini 2.0 Flash
* Gemini 2.0 Flash Lite
* Gemini 1.5 Flash
* Gemini 1.5 Pro
* Gemini 1.0 Pro

#### Anthropic Models

* Claude Sonnet 4.5
* Claude Sonnet 4
* Claude Haiku 4.5
* Claude 3.7 Sonnet
* Claude 3.5 Sonnet
* Claude 3 Haiku

#### Hosted by ElevenLabs

* Qwen3.5-397b-a17b

Qwen3.5-397b-a17b is not currently available in non-US residency workspaces that use ZRM.

#### Custom LLMs

* [Custom LLM](/docs/eleven-agents/customization/llm/custom-llm) (supports any OpenAI-API
  compatible provider and requires you to bring your own API keys)

## Technical implementation

Zero Retention Mode implements several safeguards and is designed to:

1. **LLM Allowlist** - Prevent use of LLMs except as provided above
2. **PII Redaction** - Automatically redact sensitive fields before storage
3. **Storage Prevention** - Disable uploading of raw audio files to cloud

## Developer experience

When working with Zero Retention Mode agents:

#### LLMs (except the available LLMs as described above) are disabled in the UI

![Redacted conversation analysis showing Zero Retention Mode in
action](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/01ba5fbc3d5d4a06a127f488d818428304c3f0d9500fd7931a7e4c05f8f15dab/assets/images/conversational-ai/hipaa-model.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T103420Z&X-Amz-Expires=604800&X-Amz-Signature=23b2664c47491b7d3428490bad78a2e81f400dcf1dd71f273d35fad0563f46d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Content is redacted from content history

![Redacted conversation history showing Zero Retention Mode in
action](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/af6abcc7d19b503a11e2daa6f9ca41eaab25be1b06417f448338ca3c4ef0b63f/assets/images/conversational-ai/redacted.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T103420Z&X-Amz-Expires=604800&X-Amz-Signature=70b79a37e022301667c72044f980aa8adffa2970a5d07c8646fc76da78af6ce7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Conversation analysis is limited

![Redacted conversation analysis showing HIPAA compliance in
action](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7dd246148456ae24c454a9f55d70f730fc1183b1a0b3270c9191d259af5081bb/assets/images/conversational-ai/redacted-summary.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T103420Z&X-Amz-Expires=604800&X-Amz-Signature=3b6b7a1159e2a26d63b67faf2c6087d42bb07842ac44713ddd65d0204499528d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### API restrictions are enforced

API calls attempting to use unavailable LLMs will receive an HTTP 400 error. Analytics data will be limited to non-sensitive metrics only.

## FAQ

#### Can I use any LLM if I am subject to HIPAA?

No. In such case, you can only use LLMs from the approved list. Attempts to use other LLMs will
produce an error. You can always use a custom LLM if you need a specific model not on the
allowlist.

#### Can I execute a BAA with ElevenLabs if I am subject to HIPAA?

BAAs are only available to enterprise customers. Please refer to your account executive to
discuss further.

#### Does the application of Zero Retention Mode affect conversation quality?

No. Zero Retention Mode and the execution of a BAA only affects how data is stored and which
LLMs can be used. It does not impact the quality or functionality of conversations while they
are active.

#### Can I still analyze conversation data?

Yes, but with limitations. Conversation analytics will only include non-sensitive metadata like
call duration and success rates. Specific content from conversations will not be available.

## Considerations

When building voice agents, you may consider:

1. **Use Custom LLMs** when possible, which may provide enhanced control over data processing
2. **Implement proper authentication** for all healthcare applications
3. **Validate configuration** is correct by checking redaction before launching + passing PHI

## Related resources

#### [ElevenAgents Security](/docs/eleven-agents/customization/authentication)

Learn about securing your ElevenLabs agents

#### [Custom LLM Integration](/docs/eleven-agents/customization/llm/custom-llm)

Set up your own LLM for maximum control and compliance
