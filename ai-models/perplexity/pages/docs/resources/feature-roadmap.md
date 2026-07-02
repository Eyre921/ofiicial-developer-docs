---
title: "API Roadmap"
source: https://docs.perplexity.ai/docs/resources/feature-roadmap
path: docs/resources/feature-roadmap
---

Upcoming and in-progress features for the Perplexity API.

<Info>
  This page tracks upcoming and in-progress work only. Once a feature ships, it is removed from this roadmap and documented in the [changelog](/docs/resources/changelog).
</Info>

## Upcoming and In Progress

<AccordionGroup>
  <Accordion title="Sandbox API" description="Isolated Python and Bash execution environments">
    We are introducing a Sandbox API for isolated environments for executing Python and Bash code. Each sandbox runs in its own container with dedicated resources, supporting file operations, background processes, and state persistence via pause/resume.

    * **Dedicated per-sandbox containers** for stronger isolation
    * **Python and Bash execution** with file and process support
    * **Pause/resume state persistence** for iterative workflows
  </Accordion>

  <Accordion title="Sonar API Performance Upgrade" description="Lower latency on existing endpoints">
    We are rolling out performance improvements while preserving compatibility.

    * **Same endpoint contracts** with backward compatibility
    * **Latency improvements** for common request patterns
    * **Automatic rollout** with no migration required for most users
  </Accordion>

  <Accordion title="Video Upload Capabilities" description="Multimodal video processing">
    We're expanding multimodal support to include direct video uploads.

    * **Video content analysis** for uploaded files
    * **Frame-level reasoning** for time-specific insights
    * **Visual scene understanding** across longer media
    * **Multimodal retrieval** across text, image, and video context
  </Accordion>

  <Accordion title="File Search and Connectors" description="Expanded data access">
    We're working on deeper file and data-source access for API organizations.

    * **Repository and connector search** across organization data
    * **Multi-format support** across common document types
    * **External data source integration** for enterprise workflows
  </Accordion>

  <Accordion title="Async API Webhook Support" description="Event-driven completion notifications">
    We plan to add webhook callbacks for async workflows so long-running jobs can notify your systems automatically.

    * **Job completion webhooks** for async requests
    * **Failure webhooks** with retry-safe delivery semantics
    * **Signature verification** for secure callback handling
  </Accordion>

  <Accordion title="Model and SDK Expansion" description="New model surface area and SDK ergonomics">
    We will continue to expand model coverage and improve SDK ergonomics.

    * **Additional model releases** and lifecycle clarity
    * **SDK quality-of-life improvements** for Python and TypeScript
    * **More production-ready examples** for common integration patterns
  </Accordion>

  <Accordion title="Context Management and Memory" description="Improved context handling across calls">
    We're addressing context persistence limits by improving memory-oriented workflows.

    * **Session-aware state handling**
    * **Reduced manual context stitching** across requests
    * **Improved control over long-running conversational workflows**
  </Accordion>

  <Accordion title="Better Error Handling" description="Clearer troubleshooting and recovery">
    We are improving how failures are reported and diagnosed across APIs.

    * **More actionable error messages**
    * **Stronger remediation guidance in docs**
    * **Clearer retry and backoff recommendations**
  </Accordion>

  <Accordion title="Voice-to-Voice API" description="Real-time audio interactions">
    We're building voice-native interaction capabilities for real-time experiences.

    * **Direct voice input and streamed audio output**
    * **Multi-language support**
    * **Low-latency conversation loops**
  </Accordion>

  <Accordion title="Dedicated API Console" description="Standalone developer console separate from the Perplexity app">
    We're building a dedicated API console — a standalone interface for developers that is separate from the Perplexity website. It will serve as the primary hub for API key management, usage visibility, and team controls.

    * **Standalone from the Perplexity app** — purpose-built for API developers
    * **API key management** with fine-grained permissions and rotation
    * **Usage and cost visibility** at the key and team level
    * **Organization controls** for team access and collaboration
  </Accordion>

  <Accordion title="Developer Analytics Dashboard" description="Operational usage insights">
    We're expanding analytics visibility for API teams.

    * **Query and latency analytics**
    * **Error trend monitoring**
    * **Cost and usage forecasting**
  </Accordion>

  <Accordion title="Finance Tools Integration" description="Financial data and analysis">
    We're expanding financial research capabilities with richer structured access.

    * **Market and filing workflows**
    * **Better controls for finance-specific retrieval**
    * **More end-to-end examples for analyst use cases**
  </Accordion>

  <Accordion title="Documentation Overhaul" description="Higher quality docs and guides">
    Documentation improvements remain in progress.

    * **Clearer API selection guides**
    * **More opinionated implementation guides**
    * **Higher-fidelity, production-oriented examples**
  </Accordion>

  <Accordion title="Labs Features via API" description="Experimental capabilities">
    We intend to bring selected experimental features into developer previews.

    * **Early access feature channels**
    * **Prototype integrations for feedback**
    * **Faster developer feedback loops for roadmap planning**
  </Accordion>
</AccordionGroup>

<Note>
  For shipped updates and release dates, see the [changelog](/docs/resources/changelog).
</Note>
