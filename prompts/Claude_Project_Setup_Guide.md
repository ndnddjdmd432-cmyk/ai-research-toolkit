# The Claude Project Setup Guide
## How to Build a Personal AI Operating System — From Scratch

Most people use Claude like a search engine.
They type a question, get an answer, close the tab, and start over next session with zero memory of what worked before.

This guide shows you how to build something different: a Claude Project that functions like an operating system — with persistent knowledge, structured skills, and a session memory that doesn't reset every time you open a new chat.

This is the exact setup used to run @Drag_AILabs. You can copy it entirely, or customize it for your own niche.

---

## What a Claude Project Actually Is

A standard Claude conversation is stateless. Every session starts from zero.

A Claude Project breaks that. It gives you three things standard Claude doesn't have:

**1. Persistent Knowledge Base**
Files you upload to the Project are always in context. Every conversation in that Project can reference them without you re-uploading anything.

**2. Custom Instructions**
A system-level instruction block that runs before every conversation. This is where your persona, content rules, and formatting standards live permanently.

**3. Skill Injection**
Structured XML blocks inside your custom instructions that give Claude specialized, repeatable behaviors you can trigger with simple commands.

Together, these three layers turn Claude from a general assistant into a specialized operator that knows your niche, your voice, and your goals — every single session.

---

## Layer 1: The Knowledge Base (Your Files)

Think of this as Claude's long-term memory. Every file you upload to the Project becomes part of the context Claude draws from when answering your questions.

### What to Put Here

**Research & Reference Docs (goes in every Project):**
These are facts Claude should always be able to cite. Algorithm research, platform mechanics, benchmark data, industry reports. The more specific and verified, the better.

Example files from this Project:
- X Algorithm Research Audit (16-page forensic breakdown of the 2026 X algorithm)
- X Article Formatting Guide (formatting physics and interaction weights)
- X Articles Optimization Audit (linking strategy and session duration mechanics)
- Algorithm Knowledge Base (Tweepcred, shadow hierarchy, dwell time mechanics)

**Strategy Docs (customize per account):**
These are your operational playbooks. Phase plans, content calendars, engagement rules. These are niche-specific — you'll write your own or adapt the templates in this guide.

**Skill Files:**
The 8 structured skill blocks that give Claude repeatable, specialized behaviors. These stay in your Custom Instructions, not as uploaded files.

### File Formats That Work Best
- `.txt` and `.md` — fastest for Claude to read, best for text-heavy research
- `.docx` — works well for formatted strategy documents
- `.pdf` — readable if text-based; avoid scanned PDFs

### What NOT to Upload
- Files with sensitive personal data (Claude Projects are not end-to-end encrypted)
- Duplicate content (two files covering the same topic confuse context weighting)
- Outdated docs you no longer use (they still take up context space)

---

## Layer 2: Custom Instructions (Your Permanent Rules)

Custom Instructions are the most underused feature in Claude Projects. Most people leave them empty or write two sentences.

This is a mistake. Custom Instructions are where your operating system lives.

### Structure Your Custom Instructions in 4 Blocks

**Block 1: Identity & Persona**
Who Claude is operating as. Your account name, niche, audience, and tone. Be specific — vague personas produce vague output.

Example:
```
You are the content engine for @YourAccount.
Niche: [your topic area]
Audience: [beginner to intermediate / technical / general]
Tone: confident, practical, no hype
Posting timezone: [your timezone]
Primary goal: [what you are building toward]
```

**Block 2: Content Rules (Never Break)**
The non-negotiables. Format requirements, what to always include, what is permanently banned. Write these as hard rules, not suggestions.

Example:
```
CONTENT RULES — NEVER BREAK:
- Every post must include a Nerd Note (1 technical sentence at the bottom)
- External links go in replies only — never in main post body
- Hook line must open with a result or insight, never with a problem or failure
- Use 2-3 hashtags at the very end only
- Suggest posting time in every output
- Never promise future content you haven't already tested
```

**Block 3: Output Format Standards**
Exactly how you want content structured. Thread numbering, image placeholder format, CTA style. The more specific this is, the less correction you need per session.

**Block 4: The 8 Skills (injected as numbered blocks)**
See Layer 3 below.

### How Long Should Custom Instructions Be?
As long as they need to be. Claude Projects support substantial custom instruction length. A well-built set of custom instructions for a content account will typically be 2,000–4,000 words. Do not try to be brief here — specificity is the point.

---

## Layer 3: The 8 Skills (Your Repeatable Behaviors)

Skills are structured XML blocks injected into your Custom Instructions. Each skill has:
- A trigger command (e.g., `/comment`, `/thread`, `/post`)
- A set of behavior rules Claude follows when that trigger fires
- An algorithmic planning sequence Claude executes internally
- Output constraints that enforce your format standards

### How Skills Work in Practice

You type: `/post local LLM benchmark on CPU hardware`

Claude reads the trigger, loads the Standalone Post Engine skill, executes the 6-step planning sequence internally, runs the cognitive scratchpad checklist, and outputs a fully formatted post with image placeholders, Nerd Note, CTA, hashtags, and posting time — without you specifying any of that.

Every time. Consistently.

### The 8 Skills in This System

| Trigger | Skill Name | What It Solves |
|--------|-----------|---------------|
| `/comment [post]` | Golden Window Comment Engine | Timing-aware comments on large accounts |
| `/day [N]` | Daily Execution Planner | Phase-mapped daily schedule in IST |
| `/thread [topic] [count]` | Mullet Thread Architect | Structured thread drafts with quality scores |
| `/bridge [summary]` | Context Bridge Protocol | Session continuity across conversations |
| `/score [vA] vs [vB]` | Post Quality Scorer | Dimension-by-dimension post evaluation |
| `/refine [format] [audience]` | Content Stress-Test Engine | 8-protocol invisible refinement pass |
| `/post [topic]` | Standalone Post Engine | Single post with Nerd Note and image anchors |
| `/article [topic] [wordcount]` | Long-Form Article Engine | Practitioner-voice deep-dive articles |

### Installing Skills Into Your Project

Copy each skill block exactly as written (including the XML tags) into your Custom Instructions. Paste them in sequence under a header that says `SKILL SYSTEM`. Number them 1–8.

The XML structure is what makes skills fire reliably. Do not paraphrase or simplify the skill blocks — the behavioral rules and output constraints are load-bearing.

---

## Layer 4: How the Three Layers Talk to Each Other

Here is what actually happens when you open a Project conversation and type a trigger:

1. Claude loads your Custom Instructions first — your identity, rules, and all 8 skills are active
2. Claude indexes your uploaded files — algorithm research, strategy docs, and reference material are in context
3. You type a trigger command
4. The relevant skill fires and uses both the Custom Instructions (behavior rules) and the uploaded files (knowledge) to produce output
5. Your output matches your format standards, references verified data, and follows your content rules — without you specifying any of that

The files are the brain. The custom instructions are the spine. The skills are the hands.

---

## Setup Checklist

Use this to verify your Project is correctly configured before your first session:

**Files:**
- [ ] At least 2 research/reference docs uploaded (algorithm mechanics, platform data)
- [ ] Strategy doc uploaded (your phase plan and content rules)
- [ ] No duplicate or outdated files present

**Custom Instructions:**
- [ ] Identity & Persona block written (account name, niche, audience, tone)
- [ ] Content Rules block written (hard rules, not suggestions)
- [ ] Output Format block written (thread numbering, image placeholder format, CTA style)
- [ ] All 8 skill blocks injected in sequence

**First Session Test:**
- [ ] Type `/post [any topic in your niche]` — verify Nerd Note appears, posting time appears, image placeholders appear
- [ ] Type `/comment [paste any post text]` — verify timing header appears, comment is under 240 chars, ends on authority signal
- [ ] Type `/day 1` — verify a phase-mapped schedule outputs with IST times

If any test fails, the issue is almost always in the Custom Instructions — either a skill block was paraphrased, a behavior rule is missing, or the output format wasn't specified precisely enough.

---

## Common Setup Mistakes

**Mistake 1: Uploading files without organizing the Custom Instructions**
The files are passive — Claude doesn't actively reference them unless the Custom Instructions tell it to. Your content rules and skill triggers are what activate the knowledge base.

**Mistake 2: Writing vague persona blocks**
"You are a helpful content assistant" produces generic output. "You are the content engine for @AccountName, writing for an audience of AI builders and LLM users at beginner-to-intermediate technical level, using a confident practitioner voice" produces on-brand output.

**Mistake 3: Simplifying the skill XML**
The XML structure isn't decorative. The `<behavior_rules>`, `<algorithmic_planning>`, and `<output_constraints>` tags tell Claude exactly how to process inputs and what format to enforce. Remove them and the skill degrades to a basic prompt.

**Mistake 4: Treating the Project like a regular chat**
A Project conversation can be long. You don't need to start a new chat for every question. Use the `/bridge` skill to restore context across sessions if a conversation gets too long.

**Mistake 5: Not updating files when your strategy changes**
If your phase plan changes, update the strategy doc in the Project. Stale files produce stale recommendations.

---

## What This System Cannot Do

Be honest with your audience about limitations:

- Claude Projects do not have internet access by default. The knowledge base is only as current as your uploaded files.
- Skills fire reliably but are not infallible. If output drifts from the expected format, re-trigger with the exact command.
- The Project memory is file-based, not conversation-based. Claude does not remember what you posted last Tuesday unless you tell it or upload a log.
- This system multiplies your effort. It does not replace it. If your content strategy is weak, better-formatted weak content is still weak content.

---

## The Setup in 20 Minutes

1. Create a new Claude Project (5 min)
2. Upload your research files — use the 4 universal algorithm docs from this repository (2 min)
3. Write your Custom Instructions using the 4-block structure above (8 min)
4. Paste the 8 skill blocks into Custom Instructions under `SKILL SYSTEM` (3 min)
5. Run the 3-test checklist to verify everything fires correctly (2 min)

You now have a Claude Project that knows your niche, follows your format rules, and executes 8 specialized content behaviors on command — every session, without re-explaining anything.

---

*Part of the @Drag_AILabs Open Source Content OS — released publicly so any creator can replicate, adapt, and improve it.*
