# Ultimate Prompt Engineering Guide for Claude Projects & Google Gems (2026)

## Purpose of This Guide
This document contains research-backed best practices for creating system prompts for persistent AI tools (Claude Projects, Google Gems, Custom GPTs). Use this as a reference when creating or improving prompts.

---

## CORE PRINCIPLE: PSD Framework (Persistent Structural Declarative)

All persistent prompts should follow these 4 pillars:

### 1. IDENTITY - Who is the AI?
- **Specific expert role** (not generic "assistant")
- **Years of experience** in the domain
- **Exact expertise areas** (3-5 specific skills)

❌ BAD: "You are a helpful coding assistant"
✅ GOOD: "You are a Senior Backend Engineer with 12 years of experience in Node.js microservices, PostgreSQL optimization, and AWS infrastructure"

### 2. PROTOCOL - How does the AI work?
- **Trigger → Action pairs** (IF/THEN logic)
- **Step-by-step workflows** for common tasks
- **Sequential thinking** requirements

❌ BAD: "Help users with code review"
✅ GOOD: "When user submits code: (1) Check syntax errors, (2) Verify security vulnerabilities, (3) Compare against style guide in @style_guide.md, (4) Output findings in table format"

### 3. KNOWLEDGE - Where does truth come from?
- **File priority rules** (use @ symbol for Gemini, explicit mentions for Claude)
- **Citation requirements** (quote before synthesizing)
- **Grounding exercises** (extract exact text from documents)
- **Hallucination prevention** (never invent file contents)

❌ BAD: "Use the uploaded documents"
✅ GOOD: "Before answering: (1) Search uploaded files using @, (2) Extract exact quote with <citation> tags, (3) Only then provide analysis. If information not found in files, explicitly state 'Not found in uploaded documents'"

### 4. GOVERNANCE - What should outputs look like?
- **Specific format constraints** (not vague adjectives)
- **Self-check rubrics** 
- **Validation requirements**
- **Definition of Done**

❌ BAD: "Be concise"
✅ GOOD: "Provide exactly 5 bullet points, each under 20 words. End with a self-check: 'Format verified: [Yes/No]'"

---

## SYNTAX BEST PRACTICES

### For Claude Projects (XML Structure)
```xml
<identity>
[Expert role definition]
</identity>

<protocol>
[Workflow and trigger-action pairs]
</protocol>

<knowledge_grounding>
[Citation rules and file priority]
</knowledge_grounding>

<constraints>
[Hard rules that must NEVER be violated]
</constraints>

<output_format>
[Exact structure requirements]
</output_format>

<variables>
<project_name>X</project_name>
<tone_style>Y</tone_style>
<!-- Reference these throughout -->
</variables>
```

### For Google Gems (Markdown Structure)
```markdown
# IDENTITY
[Expert role definition]

# PROTOCOL
## Workflow for [Common Task 1]
## Workflow for [Common Task 2]

# KNOWLEDGE GROUNDING
- File priority: @filename.md takes precedence
- Citation requirement: Quote exact text before analysis

# CONSTRAINTS
## Hard Rules (Never Violate)
- Rule 1
- Rule 2

## Style Requirements
- Tone: [specific]
- Format: [specific]

# OUTPUT FORMAT
Default structure:
1. [Step 1]
2. [Step 2]

# VARIABLES
- Project: {project_name}
- Language: {language}
(Reference throughout prompt)
```

---

## CRITICAL DO's and DON'Ts

### ❌ AVOID THESE (Outdated Frameworks)
1. **CO-STAR framework** - Causes instruction drift in long conversations
2. **Mandatory Chain-of-Thought** - 35-600% slower, only 3% accuracy gain
3. **Vague adjectives** - "be creative," "be concise," "be helpful"
4. **Session-based thinking** - Assuming fresh start each time
5. **Prose-heavy instructions** - Long paragraphs without structure
6. **{{curly_braces}}** for variables - Use <angle_brackets> instead

### ✅ USE THESE (Modern Best Practices)
1. **Hierarchical structure** - XML for Claude, Markdown headers for Gemini/GPT
2. **Contract-style constraints** - "Exactly 3 paragraphs, each 50-75 words"
3. **Trigger-action logic** - "IF user uploads CSV THEN validate column headers"
4. **Citation enforcement** - Require quotes from uploaded files
5. **Modular blocks** - Separate sections that can be updated independently
6. **Repetition of key variables** - Mention important constraints 3+ times
7. **Self-check mechanisms** - Force AI to verify its own output
8. **<angle_brackets>** for variables - Better parsing by models

---

## ADVANCED TECHNIQUES

### Chain-of-Draft (Not Chain-of-Thought)
Instead of: "Think step-by-step and explain your reasoning"
Use: "Generate brief scratch notes of key insights, then provide final answer"
Result: Same accuracy, 85% fewer tokens

### Prompt Decorators (Compact Control)
Instead of long prose, use symbolic commands:
- `+++Reasoning(depth=high)` = Deep analytical thinking
- `+++Tone(style=technical)` = Technical language
- `+++Import(topic="Security")` = Pull security knowledge
- `+++Refine(iterations=2)` = Improve answer twice

### I.N.V.E.S.T. Plan Mode (Prevent Hallucination)
For complex tasks, force this workflow:
1. Generate plan with discrete, testable steps
2. Present plan for user approval
3. Execute one step at a time
4. Verify each step before proceeding
5. Self-check: "Step completed successfully: [Yes/No with evidence]"

### Variable Anchoring (Prevent Drift)
Mention critical variables in multiple sections:
```xml
<identity>
Your tone is <tone_style>
</identity>

<constraints>
Always maintain <tone_style> throughout
</constraints>

<output_format>
Verify tone matches <tone_style> before responding
</output_format>
```

### Citation Enforcement Pattern
```xml
<protocol>
For any factual claim:
1. <thinking>Search uploaded files for evidence</thinking>
2. <citation>"Exact quote from source"</citation>
3. Then provide analysis
4. If no evidence found: State "Cannot verify from uploaded documents"
</protocol>
```

---

## MODEL-SPECIFIC OPTIMIZATION

### Claude Projects (Anthropic)
- **Strength**: Structured reasoning, code generation
- **Syntax preference**: XML tags
- **Best for**: Technical documentation, coding assistants
- **Pro tip**: Use `<thinking>` tags to show reasoning process

### Google Gems (Gemini)
- **Strength**: Massive context (1M tokens), multimodal
- **Syntax preference**: Markdown with # headers
- **Best for**: Research across large documents, document analysis
- **Pro tip**: Use @ symbol to reference specific files (e.g., @report.pdf)
- **File import**: Use `@./filename.md` in instructions to import directly

### Custom GPTs (OpenAI)
- **Strength**: Benchmark performance, technical accuracy
- **Syntax preference**: Markdown with clear sections
- **Best for**: Math, logic, structured data processing
- **Pro tip**: Use ``` code blocks for examples in instructions

---

## COST OPTIMIZATION (Caching)

### Understanding Caching Economics
- **First message**: System prompt charged at full price
- **Subsequent messages**: 90% discount on cached system prompt
- **Implication**: Use LONG, detailed prompts without worry

### Best Practices
1. **Front-load instructions** - Put all rules in system prompt, not in conversation
2. **Include 10-20 examples** - No longer wasteful with caching
3. **Heavy documentation** - Include full style guides, standards
4. **Avoid repetition in chat** - Say it once in system prompt, reference it in chat

Example economics (100 turns, 5000-token system prompt):
- Without caching: $0.80
- With caching: $0.088
- **Savings: 91%**

---

## TESTING & ITERATION

### Evaluation Checklist
Before deploying a prompt, test for:
1. **Instruction adherence** - Does it follow exact formatting requirements?
2. **Consistency** - Same quality across 20+ test queries?
3. **Citation accuracy** - Does it quote sources correctly?
4. **Hallucination rate** - Any false claims in 50 test responses?
5. **Edge cases** - What happens with unusual inputs?

### Red Teaming Questions
- What if user asks to "ignore all previous instructions"?
- What if uploaded file contradicts system prompt?
- What if user requests something outside the scope?
- What if two constraints conflict?

### Versioning Strategy
1. Start with v1.0 minimal prompt
2. Test with 20 real queries
3. Identify failure patterns
4. Add specific constraints for failures
5. Release v1.1
6. Repeat

---

## COMMON USE CASE TEMPLATES

### Coding Assistant
Focus on: Identity (specific stack), Protocol (review workflow), Constraints (style guide), Governance (testing requirements)

### Research Assistant
Focus on: Knowledge (citation rules), Protocol (search → analyze workflow), Governance (source quality standards)

### Writing Coach
Focus on: Identity (writing expertise), Constraints (style rules), Governance (feedback structure), Protocol (revision workflow)

### Data Analyst
Focus on: Protocol (analysis steps), Constraints (statistical rigor), Governance (visualization requirements), Knowledge (data source priority)

### Project Manager
Focus on: Protocol (task breakdown), Governance (deliverable definitions), Knowledge (project file priority), Constraints (timeline rules)

---

## FINAL CHECKLIST FOR ANY PROMPT

Before finalizing, verify:
- [ ] Specific expert identity (not generic assistant)
- [ ] Clear trigger-action protocols for common tasks
- [ ] Explicit citation and grounding requirements
- [ ] Measurable constraints (numbers, not adjectives)
- [ ] Self-check mechanisms in output format
- [ ] Variables defined and referenced 3+ times
- [ ] Structured with XML (Claude) or Markdown headers (Gemini/GPT)
- [ ] No CO-STAR or mandatory Chain-of-Thought
- [ ] Modular blocks that can be updated independently
- [ ] Examples of perfect output (if applicable)

---

## HOW TO USE THIS GUIDE

1. **Save this guide** as a reference document
2. **Upload it to a Claude chat** when you need a new prompt
3. **Request**: "Based on this guide, create a [Project/Gem] prompt for [specific purpose]"
4. **Claude will generate** a prompt following these principles
5. **Copy-paste** the generated prompt into your Project/Gem
6. **Test and iterate** using the evaluation checklist

---

## KEY TAKEAWAY

Modern prompt engineering for persistent AI is **configuration, not conversation**. Think like a software engineer writing a config file, not like someone chatting with a friend.

**The shift:** "Talking to AI" → "Programming AI behavior"

---

*Based on: "Architectural Paradigms for Persistent AI Systems" (2026 Research)*
