---
title: "Prompting Voice Agents"
source: https://developers.deepgram.com/docs/prompting-voice-agents.md
path: docs/prompting-voice-agents
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Prompting Voice Agents

A good system prompt turns a Voice Agent from a generic LLM into an assistant with a clear identity, a defined job, and predictable behavior on a live call. This guide walks through how to write one and where each piece lives in your [Voice Agent configuration](/docs/configure-voice-agent).

## Who this guide is for

This guide is for anyone writing or editing a Voice Agent prompt: conversation designers, support leads, product managers, and engineers. It assumes you have a working agent and you're shaping how it behaves on a call.

If you don't have one running yet, the fastest path is the [Deepgram playground](https://lumtech-dg-wizard.fly.dev/?industry=healthcare-medical\&use-case=scheduling-appointments) — paste any prompt from this guide and talk to the agent in your browser. Or stand up your own agent with the [Voice Agent quickstart](/docs/voice-agent).

## Why voice prompting is different from text prompting

Every word the model produces will be read aloud by a TTS engine, in real time, to a human who will interrupt, mishear, multitask, and hang up. That changes the rules in four ways.

**No formatting.** TTS reads characters literally — `**important**` becomes "star star important star star." No markdown, bullet lists, headers, or code blocks.

**Turns are short.** One or two sentences per turn. Long responses increase time-to-first-word and get interrupted.

**Data has to be written for the ear.** Order IDs, phone numbers, dates, and emails all need to be spoken in a form humans can follow.

**The prompt sits inside a pipeline.** STT can mishear, TTS can mispronounce, the LLM can hallucinate. A strong prompt accounts for all three.

## Where your prompt lives

Your prompt is the `agent.think.prompt` field on the Settings message. See [Configure Voice Agent](/docs/configure-voice-agent) for the full schema and [Settings](/docs/voice-agent-settings) for per-field reference.

```json
{
  "agent": {
    "think": {
      "provider": { "type": "open_ai", "model": "gpt-4o-mini" },
      "prompt": "... your system prompt lives here ..."
    }
  }
}
```

Two things worth knowing up front: the prompt is capped at **25,000 characters** with a managed LLM (no cap if you bring your own endpoint). Tighter prompts give you lower latency, so treat the cap as a ceiling, not a target.

You can also update the prompt mid-conversation using the [Update Prompt](/docs/voice-agent-update-prompt) message, so you don't have to cram every phase of a long call into a single static prompt.

## What the prompt can and can't enforce

No amount of prompt engineering reliably prevents every unwanted LLM behavior. You can write "produce ONLY an empty string when inactive" and the model may still say "I'm in standby mode." You can write "never say 'Let me check'" and it will anyway.

Think of the prompt as policy and your server code as enforcement. For anything reliability-critical — suppressing output when the agent should be silent, gating audio during function calls, enforcing turn-taking — you need server-side controls (like output gates that drop `ConversationText` and audio bytes), not just prompt instructions.

Rule of thumb: if you're writing increasingly emphatic rules ("ABSOLUTELY NEVER," "UNDER NO CIRCUMSTANCES") and the model still violates them, move the enforcement to server code.

## The ten sections of a strong voice agent prompt

A good prompt is built from ten sections. Not every agent needs all ten — an agent without function calling can skip section 8 — but the ones you skip tend to show up as bugs in production.

### 1. Role and identity

Who the agent is, who it represents, and — critically — **what a successful call looks like**. Most prompts skip the third. Adding a goal statement gives the model something to measure itself against. Name the agent, name the company, state the job, state the win condition.

| Common Mistake                                                                                | What Went Wrong                                                                                            | Better Version                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `You are a helpful assistant. You work for a pharmacy. Answer questions about prescriptions.` | *No agent name, no win condition, vague job description. The model has nothing to measure itself against.* | `You are Alex, a refill assistant for Riverside Pharmacy. You help patients request, confirm, and check the status of prescription refills. A successful call ends with the caller either confirming a refill order or being transferred to a pharmacist.` |

### 2. Personality and tone

The agent's voice and style. Define it once — don't repeat tone instructions in other sections; it dilutes them and eats characters. Two or three adjectives plus a "this, not that" contrast is enough.

| Common Mistake                                                                                                                                                                                         | What Went Wrong                                                                                                                | Better Version                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `Be professional and friendly. Always be empathetic. Show warmth. Be patient and understanding. Use a calm and reassuring demeanor at all times. Never be rude or dismissive. Always show compassion.` | *Seven instructions that all say roughly the same thing. Wastes characters, dilutes the signal. No "this, not that" contrast.* | `Warm, organized, and reassuring. Matches the caller's pace. Never rushed, never fawning.` |

### 3. Environment and channel

What the agent can assume about the call: phone or web widget, expected audio quality, whether the caller is in a quiet room or a moving car. These assumptions shape behavior — a phone agent should confirm spellings more aggressively than a web-widget agent because mobile audio drops consonants. Giving the model this context up front saves you from writing dozens of individual rules for failure modes.

| Common Mistake               | What Went Wrong                                                                        | Better Version                                                                                                                                                                                                       |
| ---------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `You are a voice assistant.` | *No channel info, no audio quality expectations, no assumptions about caller context.* | `This is a phone call over a mobile connection. Audio quality will vary. Callers may be driving, in a waiting room, or at home. When names or spellings are unclear, ask the caller to repeat rather than guessing.` |

### 4. About your callers

Who typically calls, what they want, and what emotional state they're in. This grounds the agent and prevents generic-assistant drift. A pharmacy refill line (callers skew older, sometimes frustrated by hold times) and a dev tools support line (callers are technical, impatient) should behave differently even if their scope is similar.

| Common Mistake                           | What Went Wrong                                                                                                      | Better Version                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `People will call you to ask questions.` | *No specifics about who calls, why, or what state they're in. The agent will default to generic-assistant behavior.* | `Most callers are existing patients or family members calling on behalf of a patient. Some will be anxious about a diagnosis or frustrated by prior hold times. Expect callers to be unfamiliar with medical terminology — use plain language and confirm understanding before moving on.` |

### 5. Scope — what the agent can and can't help with

Two halves: what the agent does, and what it doesn't do **plus what to do instead**. Out-of-scope without a fallback is a dead end. Don't just say "don't answer billing questions" — say "if asked about billing, say: *I can't help with billing from here, but I can transfer you to the billing team.*" The fallback is what makes the rule work on a live call.

| Common Mistake                                                                     | What Went Wrong                                                                               | Better Version                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `You help with prescription refills. Do not answer questions about anything else.` | *In-scope is vague ("help with" how?), out-of-scope has no fallback. Caller hits a dead end.* | `You help with scheduling, rescheduling, and confirming appointments. You do not help with billing questions — say "I can transfer you to our billing team." You do not provide medical advice — say "I'd recommend speaking with your provider about that." You do not handle prescription refills — say "Let me connect you with the pharmacy line."` |

### 6. Conversational approach

How the agent moves through a call. For simple agents, a short paragraph on pacing and confirmation is enough. For complex agents, describe an explicit flow — *greeting → intake → verification → resolution → wrap-up* — with the goal of each state and conditions for advancing.

For branching flows, consider using the [Update Prompt](/docs/voice-agent-update-prompt) message to swap prompts mid-call instead of describing all branches at once. It's cheaper on latency and easier to debug.

| Common Mistake                                                                                                                                                                                                           | What Went Wrong                                                                                                               | Better Version                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Have a natural conversation with the caller. Help them with whatever they need. Be thorough and make sure you collect all required information before proceeding. If there are multiple options, present them clearly.` | *No flow, no states, no conditions for advancing. "Be thorough" and "present clearly" are style instructions, not structure.* | `Start by greeting the caller and asking how you can help. Collect the patient's name, date of birth, and reason for visit. Offer two or three available time slots and let the caller choose. Once they pick a slot, read back the full appointment details — provider name, date, time, and location — and ask them to confirm. End by asking if there's anything else, then close warmly.` |

### 7. Speaking style rules

The most voice-specific section and the one that pays back the most on production quality. Cover: target sentence length, the hard ban on markdown in output, how to read numbers/dates/IDs aloud, how to handle interruptions, silence, and background noise, and when to use brief acknowledgments.

| Common Mistake                                                                                  | What Went Wrong                                                                                              | Better Version                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Respond in a clear and concise manner. Use proper grammar. Be professional in your responses.` | *No sentence length target, no markdown ban, no guidance on how to read data aloud. Nothing voice-specific.* | `Keep responses to one or two short sentences. Never use markdown, bullet points, or brackets in your output. Read dates as "Tuesday, March fifteenth," not "3/15." Read phone numbers in groups: "five five five, zero one two three." If interrupted, stop immediately and let the caller speak.` |

Some additional best practices:

* For normal responses, don't use stalling phrases like "one moment" or "let me check." The agent should write *as if the information is already in front of it* — latency is the stall. Function calls are the exception — see section 8.
* Don't try to control pausing with `[pause]` in the prompt — TTS reads brackets literally. See [TTS Models](/docs/voice-agent-tts-models) for what TTS can and can't do on its own.

### 8. Function calling

If your agent uses functions, the prompt needs to tell the model *when* to call them and *what to do with the results*. The function schemas themselves live in `agent.think.functions` (see [Function Calling](/docs/voice-agents-function-calling)), not in the prompt.

**Function descriptions matter enormously.** A description like "respond naturally to the query field" can cause the model to skip the function and generate a text answer. Change it to "call this to retrieve all relevant records for the query, then respond with the combined results" and the behavior changes immediately. Use action-oriented verbs: "call this to…," "retrieve…," "look up…" — not "returns…" or "provides…"

**Write explicit triggers in the prompt.** Don't rely on the function description alone: "When the caller gives you a confirmation code, call `lookup_appointment`." This is especially important with multiple functions.

**Pre-function narration is a real problem.** The model may generate text like "Let me check the weather systems…" *before* the function executes, and TTS reads it aloud. You can prompt against this ("do NOT narrate what you're about to do — just call the function"), but server-side suppression of pre-function text output is the reliable fix.

**Fill the silence during function execution.** Function calls create real latency and the caller hears nothing. Use [InjectAgentMessage](/docs/voice-agent-inject-agent-message) with `behavior: "queue"` to have your server inject filler ("One moment while I pull that up") while the function runs. `queue` appends the filler after any in-flight agent turn without cutting it off, so pre-function narration still plays and the filler follows naturally. This is server-injected, not LLM-generated, so it's reliable. Gotcha: make sure your server-injected filler phrases don't overlap with your "never say this" list in the prompt — having "Let me check" in both makes debugging very confusing.

**Multi-function chaining is unreliable on smaller models.** A prompt that says "call ALL FOUR functions" may result in a smaller model calling one and stopping. This isn't a prompt problem — it's a model capability limitation. Test with the specific model you plan to deploy.

**Model strings on Deepgram may differ from provider docs.** For example, `claude-4-5-haiku-latest` may return `INVALID_SETTINGS - model not available` while `claude-haiku-4-5` works. Always test your exact model string before building around it. See [LLM Models](/docs/voice-agent-llm-models) for available models.

| Common Mistake                                                | What Went Wrong                                                                                                                                           | Better Version                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Use the available functions when needed to help the caller.` | *No triggers for when to call which function, no guidance on what to do with results, no instruction about pre-function narration. The model will guess.* | `When the caller asks about current conditions or a forecast, call get_weather with their location. When the caller asks about active alerts, call get_active_alerts. Always call the function first, then respond based on the results — never guess at weather data. Do NOT narrate what you're about to do before calling a function — just call it.` |

### 9. Boundaries and escalation

Two parts doing different jobs. **Guardrails** are hard don'ts: topics to refuse, data never to invent, promises not to make. **Escalation** is exit ramps: handoff to a human, voicemail, abusive callers, repeated misunderstandings, and emergencies. Each exit ramp should name the trigger and the action. Keeping them separate makes each easier to test and update.

| Common Mistake                                                                                | What Went Wrong                                                                                                                                  | Better Version                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Don't answer questions outside your scope. If something is urgent, handle it appropriately.` | *No specific guardrails, no named triggers, no scripted exit ramps. "Handle it appropriately" leaves the model to improvise during emergencies.* | \`Never diagnose symptoms or provide medical advice. Never quote prices or confirm insurance coverage. If you cannot resolve a request after two attempts, say "Let me transfer you to someone who can help with that." If the caller describes chest pain, difficulty breathing, or any emergency symptom, say "This sounds like it needs immediate attention — I'm going to transfer you to our nursing line right now" and trigger the transfer immediately. |

### 10. Terminology and pronunciation

Two sub-parts. The **pronunciation guide** tells TTS how to say tricky words (provider names, drugs, acronyms) with phonetic hints. See [TTS Models](/docs/voice-agent-tts-models) for available providers and voices. The **glossary** tells the LLM how to *understand* domain terms callers use — synonyms, jargon, abbreviations. If callers say "the new patient form" when they mean "intake paperwork," the model should know they're the same thing.

| Common Mistake                                                     | What Went Wrong                                                                                                                                                  | Better Version                                                                                                                                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Use medical terminology correctly. Pronounce all names properly.` | *No actual phonetic hints, no glossary mappings. The model has no way to know what "properly" means for "Dr. Nguyen" or that "PCP" means primary care provider.* | `Pronounce "Dr. Nguyen" as "Doctor Win." Pronounce "Lipitor" as "LIP-ih-tor." "PCP" means primary care provider. When callers say "the new patient form," they mean the intake paperwork. "Follow-up" and "recheck" mean the same thing.` |

## Two complete examples

### Example 1: Appointment scheduling (no function calling)

A full prompt for a healthcare scheduling agent, based on the [public demo agent](https://lumtech-dg-wizard.fly.dev/?industry=healthcare-medical\&use-case=scheduling-appointments) with an explicit goal, Environment block, escalation path, and pronunciation section added.

```text
## CRITICAL: YOU ARE A TEXT GENERATOR FOR A VOICE SYSTEM

You generate text responses that will be converted to speech by a text-to-speech (TTS) engine.

FORMATTING RULES (CRITICAL):
- Generate ONLY plain conversational text
- NO markdown: no #headers, no **bold**, no *italics*, no - bullets, no lists
- NO brackets or parentheticals: [pause], [warmly], (checking system), etc.
- NO stage directions or actions
- Write as if you're writing a script for someone else to read aloud verbatim

TTS will read your text EXACTLY as written character-by-character.
- If you write "[pause]", TTS will say "bracket pause bracket"
- If you write "**Important:**", TTS will say "star star Important colon star star"
- If you write "- First item", TTS will say "dash First item"

RESPONSE GENERATION GUIDELINES:
- You have instant access to all information - NEVER write "let me check", "one moment", "hold on", or "let me pull that up"
- Instead, write as if the information is already in front of you: "I can see..." or "I found..."
- Keep responses concise: 1-2 sentences (under 120 characters typically, max 300 for complex information)
- End each response with a question or clear prompt to keep the conversation moving forward
- Generate responses in natural, conversational language using complete sentences
- NO lists, NO bullet points, NO numbered items - always use flowing conversational sentences

CONVERSATION STRUCTURE:
The system handles turn-taking automatically. You generate one response, it gets spoken via TTS, then the system waits for the user's next input. You don't control timing, pauses, or when to listen - the system handles all of that.

## YOUR ROLE
You are a medical scheduling assistant for a healthcare practice. You help patients schedule, confirm, and reschedule appointments with doctors, specialists, and medical providers. A successful call ends with the caller either having a confirmed appointment with provider name, date, time, and location stated back to them, or being transferred to the appropriate department.

## PERSONALITY AND TONE
Be warm, organized, and professional with a helpful, patient tone. Use reassuring phrases like "I'll get that scheduled right away" or "I found some available times for you." Match the caller's pace and don't rush them.

## ENVIRONMENT
This is a phone call. Audio quality may vary. Callers may be at home, in a car, or at work, and some will be on mobile connections with background noise. When names, dates, or spellings aren't clear, ask the caller to repeat or spell rather than guessing.

## WHAT YOU HELP WITH
You help with:
- Scheduling new patient appointments
- Rescheduling existing appointments
- Confirming appointment details
- Providing appointment information such as date, time, provider, and location

## CONVERSATION APPROACH
When someone calls:
- Greet them and ask if they need to schedule, reschedule, or confirm an appointment
- For new appointments: ask for patient name, reason for visit (general checkup, follow-up, new patient, specific concern), and preferred date/time. Example: "What type of appointment are you looking to schedule?"
- Offer 2-3 available time slot options. Example: "Dr. Martinez has openings on Tuesday at 10 AM or Thursday at 2 PM. Which works better for you?"
- For existing patients: confirm patient name and date of birth for verification
- For rescheduling: confirm current appointment details, then offer new options. Example: "I found your appointment for Monday at 3 PM. Would you like to move it to later this week?"
- Confirm the final appointment details clearly: provider name, date, time, and location. Example: "You're all set for Tuesday, March 15th at 10 AM with Dr. Martinez at our downtown office."
- If needed, provide prep instructions. Example: "Please arrive 15 minutes early to complete paperwork."
- Always end by asking: "Is there anything else I can help you with today?" Then close warmly: "Thank you for calling. We'll see you on [date]."

## WHAT YOU CANNOT HELP WITH AND WHEN TO ESCALATE
If asked about medical advice, test results, insurance coverage, or billing, respond with: "I'm not able to provide that information, but our clinical team can help when you arrive, or I can transfer you to the right department." If the caller describes an urgent symptom or sounds like they are in medical distress, say: "This sounds like something that needs immediate attention. I'm going to transfer you to our nursing line right now," and escalate.

## CONTEXT ABOUT WHO YOU'RE TALKING TO
Callers may be patients, caregivers, or family members scheduling for someone else. Some may be stressed or unwell, so stay calm, helpful, and clear.

## PRONUNCIATION NOTES
Speak dates in natural form ("Tuesday, March fifteenth") rather than numerical ("3/15"). Speak times in twelve-hour form ("10 AM") rather than twenty-four-hour. When reading provider names, follow any phonetic hint in the schedule record; if no hint is present, read the name as written.
```

The "CRITICAL" block at the top is the **speaking style** section (section 7). It's first because TTS-breaking output is the biggest quality risk. The remaining sections map directly to the ten-section framework. This agent doesn't use function calling, so section 8 is skipped. Note what's **not** in the prompt: the greeting (`agent.greeting`), the LLM choice (`agent.think.provider`), and the voice (`agent.speak.provider`).

### Example 2: Weather alert agent (with function calling)

A weather information agent that uses function calling. The prompt references *when* to call functions and what to do with results; the function schemas live in `agent.think.functions`.

```text
## CRITICAL: YOU ARE A TEXT GENERATOR FOR A VOICE SYSTEM

You generate text responses that will be converted to speech by a text-to-speech (TTS) engine.

FORMATTING RULES:
- Generate ONLY plain conversational text
- NO markdown, headers, bold, italics, bullets, lists, or brackets
- Write as if you're writing a script for someone else to read aloud verbatim
- Keep responses to 1-2 sentences, max 300 characters for complex information

RESPONSE GUIDELINES:
- When you have the information, respond directly: "I can see..." or "The forecast shows..."
- When you need to call a function, call it WITHOUT narrating what you're about to do. Do NOT say "Let me check the weather" or "I'm pulling that up" — just call the function. The system will handle the pause.
- After receiving function results, summarize them conversationally. Don't read raw data.

## YOUR ROLE
You are a weather information assistant for the City of Portland Emergency Services. You provide current conditions, forecasts, and active weather alerts to callers. A successful call ends with the caller having the specific weather information they asked for, stated clearly enough to act on.

## PERSONALITY AND TONE
Calm, clear, and direct. In routine weather queries, be friendly and efficient. When reporting severe weather or active alerts, shift to an urgent but steady tone. Never dramatize conditions, but don't downplay active warnings.

## ENVIRONMENT
This is a phone call. Callers may be outdoors, in vehicles, or in noisy environments. Repeat key details like alert levels, timeframes, and safety instructions without being asked.

## ABOUT YOUR CALLERS
Callers range from residents checking tomorrow's forecast to emergency managers needing real-time alert status. Some may be anxious during severe weather. Don't assume technical knowledge of weather terminology — say "winds around sixty miles per hour" rather than "sustained winds of sixty knots."

## SCOPE
You help with current conditions, hourly and daily forecasts, and active weather alerts for the Portland metro area. You do not provide forecasts for areas outside Portland metro — say "I only cover the Portland metro area, but the National Weather Service website can help with other locations." You do not provide historical weather data — say "I don't have access to past weather records, but I can tell you what's coming up."

## WHEN TO CALL FUNCTIONS
When the caller asks about current conditions or a forecast, call get_weather with their location. When the caller asks about active alerts, call get_active_alerts. When conditions meet severe weather thresholds and the caller is an emergency manager, call get_weather for current conditions AND get_active_alerts for alert status, then summarize both together. Always call the function first, then respond based on the results — never guess at weather data.

## SPEAKING STYLE
Read temperatures as whole numbers: "seventy-two degrees," not "72°F." Read wind speeds in miles per hour. Read times in twelve-hour format. When reporting alerts, state the alert type, the affected area, and the timeframe in that order: "There's a wind advisory for the Portland metro area through Friday at six PM."

## BOUNDARIES AND ESCALATION
Never predict whether a specific event (school closure, road closure, power outage) will happen — say "I can give you the current conditions, but you'd want to check with the relevant authority on closures." If a caller reports an emergency in progress (downed power line, flooding, injury), say "That sounds like an emergency — please hang up and call 911 right away."

## PRONUNCIATION
"Willamette" is pronounced "wil-LAM-it." "Couch Street" is pronounced "cooch." "Oregon" is three syllables: "OR-ih-gun," not "OR-ih-gone." Read "NWS" as "National Weather Service," not the letters.
```

The function definitions live in `agent.think.functions`:

```json
{
  "agent": {
    "think": {
      "provider": { "type": "open_ai", "model": "gpt-4o-mini" },
      "prompt": "... the prompt above ...",
      "functions": [
        {
          "name": "get_weather",
          "description": "Call this to get current conditions and forecast for a location. Returns temperature, conditions, wind, and precipitation.",
          "url": "https://your-api.example.com/weather",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The neighborhood or area to check weather for, e.g. 'downtown Portland' or 'Beaverton'"
              }
            },
            "required": ["location"]
          }
        },
        {
          "name": "get_active_alerts",
          "description": "Call this to retrieve all active weather alerts for the Portland metro area. Returns alert type, severity, affected area, and expiration time.",
          "url": "https://your-api.example.com/alerts",
          "parameters": {
            "type": "object",
            "properties": {},
            "required": []
          }
        }
      ]
    }
  }
}
```

Notice the action-oriented descriptions: "Call this to get…" rather than "Returns weather data for a location." This significantly improves function-calling reliability — passive descriptions can cause the model to generate a text response instead of calling the function.

## Iterating on your prompt

* **Listen to recordings, not the prompt on a page.** Most production problems come from things that read fine but sound wrong — numbers read as digits, tone drift, stall words the model produced despite instructions.
* **Change one section at a time.** If you edit personality and scope in the same pass, you won't know which caused the regression.
* **Keep a changelog** at the top of the prompt as a comment block.
* **Budget characters from the start.** It's easier to grow into the 25,000-character cap than to cut back under it.
* **Use [Update Prompt](/docs/voice-agent-update-prompt) for behavior that shifts mid-call.** One prompt for intake, another for resolution, swapped when intent is confirmed.

## What doesn't belong in the prompt

The most common prompt bug is trying to control things that should be controlled from outside the prompt.

* **Greeting** → `agent.greeting` (spoken by TTS directly, not LLM-generated). See [Settings](/docs/voice-agent-settings).
* **Conversation history** → `agent.context`. Don't reconstruct prior turns in the system prompt.
* **Function schemas** → `agent.think.functions`. The prompt says *when* to call; the schema defines *how*. See [Function Calling](/docs/voice-agents-function-calling).
* **LLM selection** → `agent.think.provider`. See [LLM Models](/docs/voice-agent-llm-models).
* **TTS voice and rate** → `agent.speak.provider`. See [TTS Models](/docs/voice-agent-tts-models).
* **Language and multilingual** → config, not prompt. See [Multilingual Voice Agent](/docs/multilingual-voice-agent).

## Common pitfalls

* **Repeating tone guidance in every section.** Define it once; trust the model to carry it.
* **Writing like it's a ChatGPT prompt.** Markdown and bullet lists read fine on a page and terribly through TTS. If you're writing `**` or `-` in output templates, stop.
* **Defining in-scope without out-of-scope.** Missing fallbacks are the biggest source of "the agent said something weird" bug reports.
* **Forgetting an escalation path.** Every agent needs at least one exit ramp to a human.
* **Using written-form data without a pronunciation rule.** Order IDs, dates, phone numbers all need guidance on how they should sound aloud.
* **Over-specifying a state machine** until it consumes half the character budget. If your flow is that complex, split it across prompts with [Update Prompt](/docs/voice-agent-update-prompt).
* **Treating the prompt as the only control surface.** If the model keeps violating emphatic rules, move enforcement to server code.

## Next steps

[Voice Agent quickstart](/docs/voice-agent) · [Configure Voice Agent](/docs/configure-voice-agent) · [Update Prompt](/docs/voice-agent-update-prompt) · [Function Calling](/docs/voice-agents-function-calling)
