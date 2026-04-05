# Skill Customization Guide
## How to Adapt the 8-Skill System for Any Niche in 3 Variable Swaps

The 8 skills in this system were built for an AI educator account on X.
But the framework underneath them is completely niche-agnostic.

Every skill uses three variables that tie it to a specific account. Swap those three things, and the entire system works for finance, fitness, cooking, coding, sports, or any other creator niche.

This guide shows you exactly what to change, where to change it, and gives you worked examples across three different niches so you can see the pattern clearly.

---

## The 3 Variables

### Variable 1: `account_name`
Your X handle. Appears in the Golden Window Comment Engine and Standalone Post Engine.

Find: `@Drag_AILabs`
Replace with: `@YourHandle`

### Variable 2: `account_niche`
The topic territory your account operates in. Appears in the Golden Window Comment Engine, Mullet Thread Architect, and Long-Form Article Engine.

Find: `AI tools, LLMs, prompt engineering, Claude/Gemini workflows`
Replace with: your niche description (see examples below)

### Variable 3: `posting_timezone`
Your local timezone for IST-specific timing suggestions.

Find: `7:30 PM IST` and `IST` throughout the Day Planner and Post Engine
Replace with: your local prime posting time and timezone abbreviation

That is the complete customization. Three swaps. Everything else — the XML structure, behavior rules, algorithmic planning sequences, output constraints — stays identical.

---

## Worked Examples

### Example A: Personal Finance Account

**Variable 1:** `@YourFinanceHandle`
**Variable 2:** `personal finance, investing, budgeting, index funds, FIRE movement`
**Variable 3:** `8:00 PM EST`

**How the comment engine changes:**
Original: Comment targeting AI accounts — adds prompt engineering insights, references model benchmarks
After swap: Comment targeting finance accounts — adds specific return data, references investment strategy mechanisms

**How the post engine changes:**
Original: Nerd Note references transformer architecture, context windows, tokenization
After swap: Nerd Note references expense ratio mechanics, compound interest formula, tax-loss harvesting logic

**Sample trigger output — `/post index funds vs active management`:**
Hook line: "Active funds beat index funds 18% of the time over 20 years. Here's what the other 82% reveals about cost drag."
Nerd Note: "The S&P 500's 0.03% average expense ratio compounds to a ~12% return advantage over 30 years versus the average active fund's 1.1% fee."

---

### Example B: Fitness & Training Account

**Variable 1:** `@YourFitnessHandle`
**Variable 2:** `strength training, hypertrophy, nutrition, recovery, programming for natural athletes`
**Variable 3:** `7:00 AM GMT`

**How the thread architect changes:**
Original: Thread body requires at least 1 specific model name, benchmark, or mechanism
After swap: Thread body requires at least 1 specific study citation, rep range, or physiological mechanism

**How the quality scorer changes:**
Original: Technical Credibility dimension scores for LLM-specific depth
After swap: Technical Credibility dimension scores for exercise science accuracy and specificity

**Sample trigger output — `/thread progressive overload for beginners 4`:**
Hook: "Most beginners plateau in 8 weeks. Not because they stopped trying — because they stopped tracking."
Nerd Note: "Progressive overload triggers mTOR pathway activation; without measurable load increase, protein synthesis rate plateaus regardless of volume."

---

### Example C: Tech Startup / SaaS Account

**Variable 1:** `@YourStartupHandle`
**Variable 2:** `SaaS growth, product-led growth, B2B sales, startup metrics, VC fundraising`
**Variable 3:** `6:00 PM PST`

**How the article engine changes:**
Original: Opening references personal AI testing results, CPU benchmarks, local LLM runs
After swap: Opening references specific ARR numbers, churn rates, or conversion experiments

**How the daily planner changes:**
Original: Phase objectives tied to X AI educator monetization milestones
After swap: Phase objectives tied to audience building, lead generation, and investor social proof goals

**Sample trigger output — `/article PLG vs SLG for early stage startups 700`:**
Opening: "Product-led growth kills more early startups than it saves. Here is the one metric that tells you which motion your product actually supports."

---

## Niche-Specific Nerd Note Bank

The Nerd Note is the hardest part to adapt — it requires a genuinely technical sentence that signals domain expertise. Here are templates by niche:

**AI / Tech:**
"Nerd Note: [mechanism] because [technical reason involving architecture/model/system behavior]."

**Finance:**
"Nerd Note: [financial instrument/strategy] operates via [specific mechanism] — the [formula/ratio/rate] is what separates surface-level understanding from actual alpha."

**Fitness:**
"Nerd Note: [exercise/protocol] triggers [physiological mechanism] — the [specific adaptation/pathway] is what the research actually shows, not what the supplement ads claim."

**SaaS / Business:**
"Nerd Note: [metric/strategy] works because [specific business mechanism] — [industry benchmark number] is the actual threshold most founders don't know to track."

**General rule:** A Nerd Note must contain at least one specific number, mechanism name, or technical term that a casual reader wouldn't know. If a non-expert could have written it, it's not a Nerd Note — it's a caption.

---

## What Does NOT Change

These elements of the skill system are universal and should never be modified regardless of niche:

**The Mullet Strategy structure:** Hook (insight/result) → Body (practical steps) → Nerd Note (technical depth) → CTA (concrete ask). This works because it bridges mass-appeal reach with authority-building depth. It is niche-agnostic by design.

**The Golden Window timing rules:** 0–60 minutes = GOLDEN, 60–180 minutes = WARM, 180+ minutes = COLD. The X algorithm's engagement velocity window does not change based on content topic.

**The 240-character comment limit:** Platform constraint. Universal.

**The link-in-reply rule:** The X algorithm penalizes external links in main posts regardless of niche. Universal.

**The 6-hour half-life rule:** The algorithm's relevancy decay function applies to all content. Universal.

**The reply-to-reply priority:** The 75x engagement weight for reply chains applies across all niches. Universal.

**The quality scorer rubric:** Hook Strength, Technical Credibility, Voice Authenticity, CTA Clarity are universal dimensions. What "Technical Credibility" looks like changes by niche — but the dimension itself doesn't.

---

## Advanced Customization: Adding Niche-Specific Skills

Once you've done the 3-variable swap, you can extend the system by adding a 9th or 10th skill specific to your niche. The XML structure for any new skill should follow the same pattern:

```xml
<skill name="[skill_name]" version="1.0">
  <behavior_rules>
    [3-5 hard rules specific to this skill]
  </behavior_rules>
  <input_variables>
    [the variables this skill takes as input]
  </input_variables>
  <algorithmic_planning>
    [3-6 steps Claude executes internally before outputting]
  </algorithmic_planning>
  <output_constraints>
    [exact format Claude must follow, including prohibited elements]
  </output_constraints>
</skill>
```

Trigger command format: `/[verb] {{VARIABLE_1}} {{VARIABLE_2}}`

Example niche extensions:
- Finance account: `/analyze [ticker] [timeframe]` → Stock/ETF analysis skill
- Fitness account: `/program [goal] [days_per_week]` → Training program builder skill
- SaaS account: `/teardown [competitor]` → Competitor analysis skill

---

## Verification Checklist After Customization

After completing the 3-variable swap, run these tests to confirm everything works:

**Test 1:** Type `/post [your niche topic]` — verify the hook opens with a result relevant to YOUR niche, not AI tools

**Test 2:** Type `/comment [paste a post from a large account in your niche]` — verify the comment adds niche-relevant insight, not generic praise

**Test 3:** Type `/day 1` — verify the schedule output references your niche's content types, not AI benchmarks

**Test 4:** Type `/score [your draft] vs none` — verify the Technical Credibility dimension is scoring for your niche's depth markers

If Test 1 or 2 still outputs AI-specific content, check that Variable 2 (`account_niche`) was replaced in ALL skill blocks, not just the first one. It appears in 4 separate skills.

---

*Part of the @Drag_AILabs Open Source Content OS.*
