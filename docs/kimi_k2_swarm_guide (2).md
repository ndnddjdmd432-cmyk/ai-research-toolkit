# KIMI K2.5 DEEP RESEARCH SWARM — MASTER PROMPT GUIDE
**Version 2.0 | LLM-Ready Drop-In System**

---

## ⚡ HOW TO USE THIS GUIDE

> **Dump this entire document into any LLM. Then say:**
> *"Using the Kimi K2.5 Swarm Deep Research framework from this guide, generate a full swarm research prompt for: [YOUR TOPIC]"*

The LLM will output a complete, production-ready multi-agent swarm research prompt optimized for Kimi K2.5's architecture.

---

## 🧠 WHAT IS A KIMI K2.5 DEEP RESEARCH SWARM?

A **Kimi K2.5 Deep Research Swarm** is a structured multi-agent prompt architecture that instructs Kimi K2.5 (or any capable LLM) to:

1. **Spawn multiple specialized sub-agents**, each with a distinct research role
2. **Run parallel deep-dives** across different dimensions of a topic
3. **Synthesize findings** through a master orchestrator agent
4. **Output structured, cited, actionable intelligence**

Kimi K2.5 has a 1M token context window and strong reasoning — the swarm pattern exploits this by having agents "hand off" context to each other within one prompt session.

---

## 📐 CORE SWARM ARCHITECTURE

Every swarm prompt follows this universal structure:

```
[ORCHESTRATOR AGENT] → Decomposes topic → Assigns sub-agents
    ↓
[AGENT 1: Domain Expert]     → Deep subject matter research
[AGENT 2: Contrarian]        → Devil's advocate / failure modes
[AGENT 3: Data Miner]        → Stats, studies, evidence
[AGENT 4: Trend Analyst]     → Emerging signals, futures
[AGENT 5: Practitioner]      → Real-world implementation
[AGENT 6: Synthesis Agent]   → Merges all outputs
    ↓
[FINAL OUTPUT: Intelligence Report]
```

---

## 🔧 THE 10 SWARM PROMPT TEMPLATES

---

### TEMPLATE 1 — UNIVERSAL DEEP RESEARCH SWARM
*Use for: Any topic where you want comprehensive 360° research*

```
You are ORCHESTRATOR-K2, a master research coordinator running a Kimi K2.5 deep research swarm. Your job is to simulate 6 specialized AI research agents working in parallel, then synthesize their findings.

TOPIC: [INSERT TOPIC]

---

ACTIVATE SWARM:

**AGENT-1 [DOMAIN EXPERT]:** 
Research [TOPIC] from first principles. Cover: core concepts, history, key players, established consensus, foundational frameworks. Go deep — not surface level. Minimum depth: PhD-level understanding. Output 400-600 words of dense, precise knowledge.

**AGENT-2 [CONTRARIAN ANALYST]:**
Challenge everything about [TOPIC]. What do most people get wrong? What does mainstream thinking miss? What are the hidden risks, failure modes, and inconvenient truths? Find the 3 most dangerous assumptions people make about this topic. Output 300-400 words of sharp, evidence-backed contrarian analysis.

**AGENT-3 [DATA & EVIDENCE MINER]:**
Surface the most important quantitative evidence about [TOPIC]. Key statistics, landmark studies, data trends, measurable benchmarks. Prioritize: recent data (last 3 years), large sample sizes, peer-reviewed sources. Output 20+ specific data points with context, organized by sub-theme.

**AGENT-4 [FUTURES & TREND ANALYST]:**
Analyze where [TOPIC] is heading. What weak signals indicate future direction? What second and third-order effects are most people ignoring? Map 3 scenarios: pessimistic, realistic, optimistic (5-year horizon). Output 300-400 words of forward-looking intelligence.

**AGENT-5 [PRACTITIONER AGENT]:**
Translate [TOPIC] into ground-level reality. How do practitioners actually work with this? What works vs. what sounds good in theory? Give 5 specific, implementable tactics or frameworks that real experts use. No theory — only what you can actually do on Monday morning.

**AGENT-6 [SYNTHESIS AGENT]:**
You have read all 5 agents' outputs above. Now synthesize:
1. The 3 most important insights across all reports
2. The key tension or paradox at the heart of [TOPIC]
3. The single most actionable recommendation
4. What further research would unlock the most value
Format as: Executive Summary (200 words) + Action Matrix (table format)

---
OUTPUT FORMAT: Run all agents sequentially, clearly labeled. End with AGENT-6 synthesis.
```

---

### TEMPLATE 2 — COMPETITIVE INTELLIGENCE SWARM
*Use for: Market research, competitor analysis, positioning*

```
You are ORCHESTRATOR-K2 running a competitive intelligence swarm on [TOPIC/COMPANY/MARKET].

ACTIVATE SWARM:

**AGENT-1 [MARKET MAPPER]:**
Define the competitive landscape for [TOPIC]. Who are the top 5-10 players? Map them on: (a) market share, (b) positioning, (c) strengths, (d) weaknesses. Use a clear comparison matrix. Identify the white spaces no one is occupying.

**AGENT-2 [CUSTOMER INTELLIGENCE AGENT]:**
Who is buying in this market and why? Define 3 buyer personas with: demographics, psychographics, core pain points, buying triggers, objections, and where they spend time online. Pull from Reddit, review sites, community forums (simulated research).

**AGENT-3 [MOAT ANALYST]:**
For each major player in [TOPIC], identify their actual competitive moat. Is it: network effects, switching costs, brand, data, scale, regulation, or something else? Rate moat strength 1-10 with reasoning. Who has the most defensible position and why?

**AGENT-4 [DISRUPTION ANALYST]:**
Who is about to disrupt [TOPIC]? What emerging startups, technologies, or business model innovations could destabilize incumbents in 3 years? Apply Clayton Christensen's disruption model. Name specific threats, not generic ones.

**AGENT-5 [POSITIONING STRATEGIST]:**
If you were launching a new product/company in [TOPIC] TODAY, how would you position it? What underserved segment would you target? What message would cut through? Write a complete positioning statement and 3 tagline options.

**AGENT-6 [SYNTHESIS]:**
Synthesize competitive intelligence into: Top Opportunities Table | Top Threats Table | Recommended Entry Strategy | 90-Day Research Action Plan
```

---

### TEMPLATE 3 — SCIENTIFIC/TECHNICAL DEEP DIVE SWARM
*Use for: Research papers, technical topics, scientific questions*

```
You are ORCHESTRATOR-K2 running a scientific deep research swarm. Topic: [TECHNICAL TOPIC]

ACTIVATE SWARM:

**AGENT-1 [MECHANISTIC EXPLAINER]:**
Explain the exact mechanism of [TECHNICAL TOPIC] from first principles. Go to the fundamental level — molecular, mathematical, physical, or logical depending on domain. Avoid analogies — give the actual mechanism. Use precise technical vocabulary.

**AGENT-2 [LITERATURE SYNTHESIZER]:**
Summarize the state of research on [TECHNICAL TOPIC]. What do the 5 most important studies/papers show? What is settled science vs. active debate? Where is the field currently stuck? Reference specific researchers, institutions, or landmark findings.

**AGENT-3 [ANOMALY HUNTER]:**
Find the anomalies. What experimental results don't fit the dominant model of [TECHNICAL TOPIC]? What edge cases break current theory? What replications have failed? These are often where the next breakthroughs hide.

**AGENT-4 [APPLICATION ENGINEER]:**
How is [TECHNICAL TOPIC] applied in practice today? Give 5 real-world applications with: technology readiness level (TRL), current limitations, what improvement would unlock next-level application, and who is leading in each space.

**AGENT-5 [CROSS-DOMAIN CONNECTOR]:**
What insights from other scientific fields could accelerate progress in [TECHNICAL TOPIC]? Draw connections to: biology, physics, computation, mathematics, or other relevant fields. Identify the most underexplored cross-pollination opportunity.

**AGENT-6 [SYNTHESIS]:**
Technical Summary | Open Questions Ranked by Importance | Recommended Reading List (5 papers/books) | Top 3 Labs/Researchers to Follow
```

---

### TEMPLATE 4 — BUSINESS STRATEGY SWARM
*Use for: Business decisions, strategy planning, market entry*

```
You are ORCHESTRATOR-K2 running a business strategy swarm. Challenge: [BUSINESS TOPIC/DECISION]

ACTIVATE SWARM:

**AGENT-1 [FRAMEWORKS AGENT]:**
Apply the 3 most relevant strategic frameworks to [BUSINESS TOPIC]. Options: Porter's Five Forces, Blue Ocean, Jobs-To-Be-Done, 7 Powers, Wardley Mapping, BCG Matrix, Ansoff Matrix. Pick the 3 that give the most insight and run each fully — don't just name them, execute the analysis.

**AGENT-2 [CASE STUDY RESEARCHER]:**
Find 5 historical analogs to [BUSINESS TOPIC]. Who faced a similar challenge before? What did they do? What worked, what failed, what would you replicate? Include: company, year, situation, decision made, outcome, lesson extracted.

**AGENT-3 [FINANCIAL MODELER]:**
Build a rough financial mental model for [BUSINESS TOPIC]. What are the key revenue drivers? Cost structure? Unit economics? What would make this work at scale? What are the 3 financial assumptions that, if wrong, break the model?

**AGENT-4 [RISK AGENT]:**
Run a pre-mortem on [BUSINESS TOPIC]. It's 3 years from now and this failed — why? List the 10 most likely failure modes ranked by: probability × impact. For each, suggest a mitigation. Then identify the 1 risk that is most underappreciated.

**AGENT-5 [EXECUTION PLANNER]:**
Turn strategy into a 90-day execution plan for [BUSINESS TOPIC]. Week 1-2: what you do first. Month 1: milestones. Month 2-3: key decisions and pivots. What does "winning" look like at day 90? What metrics prove it?

**AGENT-6 [SYNTHESIS]:**
Strategic Recommendation (1 paragraph) | Decision Matrix | 90-Day Sprint Plan | Top 3 Risks with Mitigations | Success Metrics Dashboard
```

---

### TEMPLATE 5 — CONTENT STRATEGY & VIRAL GROWTH SWARM
*Use for: Content creation, audience building, marketing campaigns*

```
You are ORCHESTRATOR-K2 running a content and growth strategy swarm. Topic: [CONTENT NICHE/BRAND/CAMPAIGN]

ACTIVATE SWARM:

**AGENT-1 [AUDIENCE PSYCHOLOGIST]:**
Build a deep psychographic profile of the ideal audience for [TOPIC]. Go beyond demographics. What are their: core identity beliefs, secret fears, aspirational self-image, tribal affiliations, content consumption patterns, trusted voices, and trigger phrases that make them stop scrolling? Be uncomfortably specific.

**AGENT-2 [VIRAL MECHANICS ANALYST]:**
Study what makes content go viral in the [TOPIC] niche. Analyze the top 10 most viral pieces of content in this space (simulate this research). Extract: the hook formula used, emotional triggers activated, shareability mechanics, narrative structure, format. Turn these into a replicable playbook.

**AGENT-3 [PLATFORM STRATEGIST]:**
For [TOPIC], which platforms are highest-leverage? For each platform (X, LinkedIn, YouTube, TikTok, Instagram, Newsletter, Podcast): rate opportunity 1-10, describe winning content format, give posting cadence recommendation, and name 3 accounts killing it there. Focus on the top 2-3 platforms only.

**AGENT-4 [CONTENT CALENDAR ARCHITECT]:**
Build a 30-day content calendar for [TOPIC]. Include: content type, headline/hook, core message, platform, CTA, and expected outcome. Mix: educational, entertaining, controversial, personal, and promotional content in a 70/20/10 ratio. Make every piece interconnect thematically.

**AGENT-5 [MONETIZATION STRATEGIST]:**
Map 5 monetization models for an audience built around [TOPIC]. For each: revenue mechanism, audience size needed to be viable, time to revenue, difficulty score, and example of someone doing it successfully. Rank by: speed to revenue × scalability.

**AGENT-6 [SYNTHESIS]:**
Brand Positioning Statement | Platform Priority Stack | 30-Day Content Calendar | Monetization Roadmap | 1 Contrarian Growth Hack Most People Miss
```

---

### TEMPLATE 6 — INVESTMENT & FINANCIAL RESEARCH SWARM
*Use for: Investment thesis, asset analysis, financial due diligence*

```
You are ORCHESTRATOR-K2 running an investment research swarm on [ASSET/COMPANY/SECTOR].

IMPORTANT: This is for research purposes. Not financial advice.

ACTIVATE SWARM:

**AGENT-1 [BULL CASE BUILDER]:**
Build the strongest possible bull case for [INVESTMENT TOPIC]. Cover: macro tailwinds, competitive advantages, growth catalysts, management quality, valuation upside. Make it as compelling as the best sell-side analyst would. Include: key metrics that support the bull thesis.

**AGENT-2 [BEAR CASE BUILDER]:**
Build the strongest possible bear case for [INVESTMENT TOPIC]. What could go wrong that most bulls are ignoring? Cover: competitive threats, regulatory risk, valuation concerns, execution risk, macro headwinds. Be as rigorous and specific as the most critical short-seller.

**AGENT-3 [COMPARABLE ANALYST]:**
Find 5 historical analogs to [INVESTMENT TOPIC]. What happened to similar assets/companies in similar macro/competitive environments? What does history suggest about likely outcomes? What patterns repeat?

**AGENT-4 [VARIANT PERCEPTION HUNTER]:**
Where does the market consensus about [INVESTMENT TOPIC] seem wrong? What do most investors believe that could be incorrect? What information or perspective would change the market's view if widely known? This is where alpha lives.

**AGENT-5 [SCENARIO MODELER]:**
Model 3 scenarios for [INVESTMENT TOPIC] over 3 years: bear (20th percentile), base (50th percentile), bull (80th percentile). For each: what conditions, what catalysts, what outcome. What is the expected value across scenarios? What's the biggest swing factor?

**AGENT-6 [SYNTHESIS]:**
Investment Summary | Bull vs. Bear Scorecard | Key Risks Table | Variant Perception Opportunities | Recommended Further Research
```

---

### TEMPLATE 7 — LEARNING ACCELERATION SWARM
*Use for: Mastering any skill, subject, or domain fast*

```
You are ORCHESTRATOR-K2 running a learning acceleration swarm. Subject: [SKILL/TOPIC TO LEARN]

ACTIVATE SWARM:

**AGENT-1 [CURRICULUM DESIGNER]:**
Design the optimal learning path for [SKILL/TOPIC]. Apply the 80/20 principle: what 20% of knowledge gives 80% of practical capability? Structure as: Foundation (week 1-2) → Core Skills (week 3-6) → Advanced Applications (week 7-12). For each phase: what to study, in what order, for how long.

**AGENT-2 [MENTAL MODEL BUILDER]:**
Identify the 10 core mental models needed to truly understand [SKILL/TOPIC]. For each: explain the model clearly, show how it applies to this domain, give a concrete example, and explain what it helps you do that you couldn't do without it.

**AGENT-3 [EXPERT BENCHMARKER]:**
Define what mastery looks like in [SKILL/TOPIC]. At 6 months, 1 year, 3 years — what can you do? What does an expert notice that a beginner misses? What are the deliberate practice activities that separate good from great? Reference specific experts and their methods.

**AGENT-4 [FAILURE MODE MAPPER]:**
What are the most common ways people fail to learn [SKILL/TOPIC] effectively? What are the traps: wrong resources, bad habits, misleading metrics, plateau zones? Map the top 5 failure patterns with prevention strategies for each.

**AGENT-5 [RESOURCE CURATOR]:**
Curate the top resources for learning [SKILL/TOPIC]. For each category — Books (top 3), Online Courses (top 2), Communities (top 2), Tools/Software (top 3), Mentors/Teachers to follow (top 5) — explain WHY this resource specifically, not just the name.

**AGENT-6 [SYNTHESIS]:**
12-Week Learning Sprint Plan | Daily Practice Schedule | Milestone Checklist | Resource Priority List | How to Know You're Actually Getting Good
```

---

### TEMPLATE 8 — PRODUCT DEVELOPMENT SWARM
*Use for: Building products, features, or startups*

```
You are ORCHESTRATOR-K2 running a product development swarm. Product: [PRODUCT/STARTUP IDEA]

ACTIVATE SWARM:

**AGENT-1 [PROBLEM VALIDATOR]:**
Validate the problem [PRODUCT] solves. Is this a real pain? Rate on: frequency (how often do people experience this), intensity (how much does it hurt), willingness to pay (do people spend money on workarounds now?). Find evidence of the problem from: forums, reviews, complaints, failed attempts to solve it.

**AGENT-2 [USER RESEARCHER]:**
Profile the ideal user for [PRODUCT] in extreme detail. Their daily workflow, the specific moment they feel the pain, what they've already tried, why it failed, what their dream solution looks like, what they'd pay. Include: a user story in their own voice, 3 user personas, the "hair on fire" scenario.

**AGENT-3 [SOLUTION ARCHITECT]:**
Design the MVP for [PRODUCT]. What is the smallest version that delivers the core value? List: must-have features (solve the core problem), nice-to-have features (defer), never-do features (avoid scope creep). For the MVP: what tech stack, build vs. buy decisions, time to build estimate.

**AGENT-4 [GO-TO-MARKET STRATEGIST]:**
Design the GTM for [PRODUCT]. Who are the first 100 customers and exactly how do you find them? What's the distribution channel? What's the acquisition cost for first 100, 1000, 10000 users? What growth loop makes this compound? Who are the 5 strategic partners that could 10x distribution?

**AGENT-5 [MOAT BUILDER]:**
How does [PRODUCT] build defensibility over time? What network effects, data advantages, switching costs, or brand moat can be built? What does year 3 look like that makes this hard to copy? Apply Hamilton Helmer's 7 Powers framework.

**AGENT-6 [SYNTHESIS]:**
1-Page Product Brief | MVP Feature List | GTM 90-Day Plan | Funding Requirements + Milestones | Top 3 Kill Risks + Mitigation
```

---

### TEMPLATE 9 — GEOPOLITICAL & MACRO RESEARCH SWARM
*Use for: Geopolitics, macro trends, global events analysis*

```
You are ORCHESTRATOR-K2 running a geopolitical and macro research swarm. Topic: [GEOPOLITICAL/MACRO TOPIC]

ACTIVATE SWARM:

**AGENT-1 [HISTORICAL CONTEXT AGENT]:**
Provide deep historical context for [TOPIC]. What are the historical forces, patterns, and precedents that explain the current situation? Go back as far as relevant — sometimes 100 years, sometimes 20. Identify: recurring patterns, structural forces, historical actors who shaped this, and the unresolved tensions that still drive events today.

**AGENT-2 [ACTOR ANALYST]:**
Map all key actors in [TOPIC]. For each major player (nations, institutions, leaders, factions): their stated interests, their real interests, their leverage, their constraints, their decision-making calculus, and their red lines. Build an "actor map" showing alliances, rivalries, and dependencies.

**AGENT-3 [STRUCTURAL FORCES ANALYST]:**
Identify the structural forces driving [TOPIC] that transcend individual actors. These could be: demographic shifts, resource constraints, technological change, economic trends, climate factors, ideological currents. Rate each force: strength (1-10), reversibility (can it change?), timeline (when does it peak?).

**AGENT-4 [SCENARIO PLANNER]:**
Run 3 scenarios for [TOPIC] over a 5-year horizon. For each scenario: triggering conditions, key decision nodes, likely sequence of events, winners and losers, and second-order effects on markets, migration, and governance. Apply: Peter Schwartz's scenario planning methodology.

**AGENT-5 [INVESTMENT/PRACTICAL IMPLICATIONS AGENT]:**
What are the practical implications of [TOPIC]? For: investors (which sectors, countries, currencies?), businesses (supply chain, talent, regulatory risks), individuals (safety, opportunity, migration?). Be specific — not "there will be volatility" but "short [X], long [Y], hedge with [Z]."

**AGENT-6 [SYNTHESIS]:**
Situation Report (SITREP) | Actor Map Summary | Top 5 Scenarios Ranked by Probability | Early Warning Indicators to Watch | Practical Action Recommendations
```

---

### TEMPLATE 10 — META-RESEARCH SWARM (SWARM ABOUT ANYTHING)
*The most powerful template — generates a custom swarm for ANY topic on the fly*

```
You are ORCHESTRATOR-K2, a meta-research architect. Your job is to:

STEP 1: Analyze [TOPIC] and identify the 5-6 most valuable research dimensions that would give the most complete intelligence on this topic.

STEP 2: For each dimension, define a specialized agent with:
- Agent name and role
- Specific research mandate (what exactly they investigate)
- Output format and length
- Success criteria (how do we know they did a great job?)

STEP 3: Run all agents sequentially, clearly labeled.

STEP 4: Run a SYNTHESIS AGENT that produces:
- Executive summary (300 words max)
- Top 5 insights ranked by importance
- Action recommendations table
- Open questions / further research needed
- Confidence level on key findings (High / Medium / Low)

TOPIC: [INSERT ANY TOPIC]

CONSTRAINTS:
- Each agent must go deeper than a Google search would
- No generic statements — specific, cited, actionable
- Agents should challenge each other's findings when relevant
- Final output should be something a decision-maker can act on immediately

BEGIN SWARM EXECUTION NOW.
```

---

## 🎛️ ADVANCED SWARM MODIFIERS

Add these to any template to customize behavior:

| Modifier | What to Add to Prompt |
|---|---|
| **Speed mode** | "Prioritize speed — compress each agent to 150 words max" |
| **Depth mode** | "Prioritize depth — each agent should output 600+ words minimum" |
| **Debate mode** | "Agents 1 and 2 should argue opposing views before synthesis" |
| **Evidence-only mode** | "Every claim must include a source, statistic, or concrete example" |
| **Actionability mode** | "Every output must end with 3 specific actions a person can take today" |
| **Beginner output** | "Synthesis agent should explain findings for a smart non-expert" |
| **Expert output** | "Use domain-specific vocabulary — audience is practitioners" |
| **Report format** | "Format final synthesis as a professional PDF-ready report" |

---

## 🔑 KIMI K2.5 SPECIFIC OPTIMIZATION TIPS

Since Kimi K2.5 has a **1M token context window**:

1. **Chain swarms** — run Template 1 first, then paste the output into Template 4 for deeper strategy
2. **Feed it documents** — paste research papers, competitor websites, or data into the context before running the swarm
3. **Ask for self-critique** — after swarm completes, add: *"Now critique your own swarm output. What did you miss? What was weakest?"*
4. **Run iteration loops** — *"Agent 3 didn't go deep enough on [X]. Rerun Agent 3 with this additional context: [paste more data]"*
5. **Cross-swarm synthesis** — run two different swarms on related topics, then ask Kimi to synthesize insights across both outputs

---

## 📋 QUICK REFERENCE CHEAT SHEET

```
TOPIC TYPE                    → BEST TEMPLATE
─────────────────────────────────────────────────
Any general research          → Template 1 (Universal)
Market / competitor analysis  → Template 2 (Competitive Intel)
Science / technical topic     → Template 3 (Scientific)
Business strategy/decision    → Template 4 (Business Strategy)
Content / marketing / growth  → Template 5 (Content Strategy)
Investing / financial         → Template 6 (Investment)
Learning a new skill          → Template 7 (Learning)
Building a product/startup    → Template 8 (Product Dev)
Geopolitics / macro trends    → Template 9 (Geopolitical)
Unknown / novel topic         → Template 10 (Meta-Swarm)
```

---

## ✅ EXAMPLE USAGE

**User prompt to any LLM after pasting this guide:**

> "Using Template 5 from the Kimi K2.5 Swarm Guide, generate a full swarm research prompt for: building a personal brand as a solo B2B SaaS founder on LinkedIn and X in 2025."

**The LLM will then:**
1. Identify which template to use ✓
2. Fill in [TOPIC] with the specific context ✓
3. Run all 6 agents with the right depth ✓
4. Produce a synthesis with actionable output ✓

---

*Guide Version 2.0 — Built for LLM portability. Drop into any model. Works with: Claude, GPT-4, Gemini, Kimi K2.5, Grok, DeepSeek, Llama.*
