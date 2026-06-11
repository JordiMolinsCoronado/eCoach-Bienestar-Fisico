
# Jordi Agent roadmap

## Core principle

Jordi Agent is not a general chatbot.

It is a local-first, task-constrained assistant that works through Telegram and helps with narrow, auditable workflows.

Default posture:

```text
Local first.
Markdown prompts.
Markdown logs.
No hidden magic.
No uncontrolled recommendations.
Human decides.
AI prepares.
AI records.
````

For the first professional use case, Jordi Agent becomes a finance / wealth-management copilot for Spanish clients.

Important rule:

```text
The assistant does not recommend investments.
It gives options, questions, comparisons, risks, and decision criteria.
The client or human advisor decides.
```

---

# Phase 0 â€” Existing foundation

## v0 â€” Working echo bot

**Goal:** prove Telegram bot is alive.

Features:

```text
/start
Echoes normal messages
```

Status: done.

---

## v1 â€” Capture messages to Markdown inbox

**Goal:** turn Telegram into a frictionless capture tool.

Features:

```text
Any normal message â†’ saved to SecondBrain_inbox.md
```

Example:

```text
Follow up with Luis about incubator
```

Saved as:

```markdown
- [2026-05-15 10:42] Follow up with Luis about incubator
```

Status: done.

---

## v2 â€” `/inbox` command

**Goal:** retrieve recent captures.

Features:

```text
/inbox
```

Shows last 10 captured items.

Status: done.

---

## v3 â€” `/today` command

**Goal:** show todayâ€™s captures only.

Features:

```text
/today
```

Shows all captures from current date.

Status: done.

---

## v4 â€” Local LLM `/ask`

**Goal:** connect Jordi Agent to a local LLM via Ollama.

Features:

```text
/ask Give me one tiny action for today
```

Bot sends the question to the local Ollama model and returns the answer in Telegram.

Default local model:

```text
gemma4:e4b-it-q4_K_M
```

Status: done or near-done.

---

## v5 â€” Main Telegram button menu

**Goal:** reduce friction; stop relying only on slash commands.

Buttons:

```text
ðŸ§  Ask       ðŸ“¥ Inbox
ðŸ“… Today     âœï¸ Capture
```

Status: done.

---

## v6 â€” Stateful buttons

**Goal:** make buttons conversational.

Flow:

```text
Tap ðŸ§  Ask
â†’ bot asks: â€œWhat do you want to ask?â€
â†’ next message goes to local LLM
```

And:

```text
Tap âœï¸ Capture
â†’ bot asks: â€œWhat should I capture?â€
â†’ next message is saved
```

Status: done.

---

# Phase 1 â€” Prompt-controlled local assistant

## v7 â€” External Markdown prompt files

**Goal:** stop hardcoding the LLM instructions inside the Python file.

Create a local folder:

```text
/prompts/
```

Initial prompt files:

```text
base_rules.md
wealth_policy.md
client_profile_questions.md
```

Purpose:

```text
The Python code loads prompt files from disk.
The local LLM receives these files as its system prompt.
Changing assistant behavior does not require editing Python code.
```

Status: next step.

---

## v8 â€” Prompt loader in Python

**Goal:** add reusable Python functions for loading prompt files and calling the local LLM.

New helper functions:

```text
load_prompt()
local_llm()
```

Result:

```text
ask_message() and future Wealth functions can reuse the same LLM logic.
```

Status: not started.

---

## v9 â€” Wealth button

**Goal:** add a dedicated Wealth mode to Telegram.

New button:

```text
ðŸ’¼ Wealth
```

Updated keyboard:

```text
ðŸ§  Ask       ðŸ’¼ Wealth
ðŸ“¥ Inbox     ðŸ“… Today
âœï¸ Capture
```

Flow:

```text
Tap ðŸ’¼ Wealth
â†’ bot asks: â€œTell me the finance/portfolio case.â€
â†’ next message goes to local LLM using wealth prompts
```

Status: not started.

---

## v10 â€” Wealth conversation state

**Goal:** make Wealth mode stateful, like Ask and Capture.

Flow:

```text
Tap ðŸ’¼ Wealth
â†’ bot waits for next message
â†’ next message is analyzed as a wealth-management case
â†’ bot replies with structured analysis
â†’ conversation ends
```

Output structure:

```text
1. What the client seems to need
2. Missing information
3. Questions to ask
4. Possible options to compare
5. Risks / warnings
6. Next tiny action
7. No recommendation disclaimer
```

Status: not started.

---

## v11 â€” Wealth logs

**Goal:** save every wealth analysis for traceability.

New file:

```text
Wealth_Logs.md
```

Each analysis saves:

```markdown
## 2026-05-18 11:10

### User input
Client is 62, sold business, has â‚¬2M cash...

### Model
gemma4:e4b-it-q4_K_M

### Prompt files
- base_rules.md
- wealth_policy.md
- client_profile_questions.md

### AI analysis
...

---
```

Why this matters:

```text
Wealth management needs an audit trail.
Even if the bot gives no recommendation, logs are useful for debugging, compliance posture, and quality control.
```

Status: not started.

---

# Phase 2 â€” First useful wealth assistant

## v12 â€” Client profiling assistant

**Goal:** answer the first essential question:

```text
What does the client want / need?
```

The assistant generates a structured questionnaire similar in spirit to an EAF/MiFID suitability interview.

Question areas:

```text
1. Identity and basic context
2. Investment objective
3. Time horizon
4. Liquidity needs
5. Income and source of income
6. Assets
7. Debts and obligations
8. Capacity for loss
9. Willingness to take risk
10. Investment knowledge
11. Investment experience
12. Existing portfolio
13. Tax residence
14. ESG / sustainability preferences
15. Family, inheritance, or legal constraints
16. Documents needed
17. Questions still unanswered
```

The assistant must not recommend products.

Status: not started.

---

## v13 â€” Platform/options assistant

**Goal:** answer the operational question:

```text
Where could the money be deposited or invested?
```

The assistant compares categories, not specific recommendations.

Possible categories:

```text
1. Traditional bank
2. Private bank
3. Online broker
4. Fund platform
5. Robo-advisor
6. Indexed fund platform
7. Money market / cash account
8. Treasury bills / short-term government debt route
```

Comparison criteria:

```text
- Deposit/custody cost
- Trading cost
- Fund subscription/redemption cost
- Availability of clean share classes
- Availability of low-cost indexed funds
- Availability of ETFs
- RTO / execution quality
- Spanish tax reporting convenience
- Regulation / investor protection
- Minimum investment
- User experience
- Transfer friction
- Currency handling
- Operational risk
```

Rule:

```text
The assistant can say â€œoptions to compare include...â€
The assistant cannot say â€œuse this platform.â€
```

Status: not started.

---

## v14 â€” Basic portfolio parser

**Goal:** understand simple portfolio descriptions pasted into Telegram.

Input example:

```text
Client portfolio:
Cash 15%
MSCI World ETF 45%
Euro bonds 25%
Gold 5%
Private equity 10%
```

Output:

```text
1. Allocation summary
2. Main concentration risks
3. Liquidity risks
4. Currency risks
5. Cost questions
6. Missing information
7. Questions before deciding anything
```

No optimization yet.

No buy/sell/hold recommendation.

Status: not started.

---

## v15 â€” Suitability checklist generator

**Goal:** generate a pre-advice checklist.

Input example:

```text
Client is 58, entrepreneur, wants retirement income, moderate risk.
```

Output:

```text
1. Investment objective
2. Time horizon
3. Risk tolerance
4. Capacity for loss
5. Liquidity needs
6. Knowledge and experience
7. Existing exposure
8. Tax residence
9. ESG preferences
10. Product restrictions
11. Documents needed
12. Red flags
```

Status: not started.

---

## v16 â€” Investment memo generator

**Goal:** draft one-page investment memos.

Input example:

```text
Product: European short-duration bond fund
Client: conservative, 3-year horizon, wants income
```

Output:

```text
Investment memo:
- Product summary
- Possible role in portfolio
- Fit factors
- Not-fit factors
- Main risks
- Fees / liquidity questions
- Suitability concerns
- Human decision required
```

Rule:

```text
The memo may support human reasoning.
It must not pretend to be a final recommendation.
```

Status: not started.

---

# Phase 3 â€” Knowledge and document grounding

## v17 â€” Local Wealth Knowledge folder

**Goal:** allow Jordi Agent to use your own wealth-management documents.

Create folder:

```text
/Wealth_Knowledge/
```

Initial files:

```text
investment_policy.md
mifid_checklist.md
client_meeting_template.md
platform_due_diligence_template.md
product_due_diligence_template.md
portfolio_review_template.md
```

The assistant can answer:

```text
Using my wealth framework, what questions should I ask this client?
```

Status: not started.

---

## v18 â€” Simple local RAG over Markdown files

**Goal:** retrieve relevant text from your local Markdown knowledge files.

First simple version:

```text
Read all .md files from /Wealth_Knowledge/
Search for relevant keywords
Inject the most relevant sections into the prompt
```

No vector database at first.

Principle:

```text
Start stupid and working.
Only add complexity when needed.
```

Status: not started.

---

## v19 â€” Better local RAG

**Goal:** improve retrieval quality.

Possible tools later:

```text
FAISS
Chroma
LanceDB
SQLite FTS
```

But only after the simple Markdown retrieval works in practice.

Status: not started.

---

# Phase 4 â€” Files and structured portfolio analysis

## v20 â€” CSV portfolio import

**Goal:** analyze portfolio files.

Input:

```text
portfolio.csv
```

Possible columns:

```text
Asset name
ISIN
Asset class
Currency
Market value
Weight
Region
Risk level
Liquidity
Expense ratio
```

Output:

```text
1. Asset allocation
2. Currency exposure
3. Top holdings
4. Concentration risk
5. Liquidity buckets
6. Cost overview
7. Missing fields
8. Questions for advisor/client
```

Status: not started.

---

## v21 â€” Excel portfolio import

**Goal:** support real-world portfolio files.

Input:

```text
portfolio.xlsx
```

Same output as CSV import.

Status: not started.

---

## v22 â€” PDF factsheet summarizer

**Goal:** summarize fund factsheets, KIIDs/KIDs, manager reports, or product PDFs.

Flow:

```text
Upload or point to PDF
â†’ extract text
â†’ summarize
â†’ identify risks
â†’ draft advisor questions
```

Output:

```text
1. Product summary
2. Strategy
3. Asset class
4. Costs
5. Liquidity
6. Risk indicators
7. Benchmark
8. Performance caveats
9. Hidden concerns
10. Questions before any decision
```

Status: not started.

---

## v23 â€” Product due-diligence assistant

**Goal:** structure product review.

Input:

```text
Product name / ISIN / factsheet text / KID text
```

Output:

```text
1. What the product is
2. What exposure it gives
3. What it costs
4. What risks it contains
5. What role it could theoretically play
6. What client types it may not fit
7. Questions for provider/platform
8. Human review required
```

Status: not started.

---

# Phase 5 â€” API LLM escalation

## v24 â€” API LLM connector

**Goal:** allow optional escalation to an external API LLM.

Default remains:

```text
Local LLM first.
```

API is used only when useful:

```text
- Long document summarization
- Complex comparison tables
- Higher quality drafting
- Translation/polishing
- Web-grounded research
```

Possible API model families:

```text
DeepSeek
OpenAI
Anthropic
Google
Mistral
```

Status: not started.

---

## v25 â€” Explicit escalation mode

**Goal:** avoid silently sending private client data to an API.

Before using an API LLM, the bot should mark the event clearly.

Possible flow:

```text
This may require stronger external analysis.
Send anonymized text to API model? yes/no
```

For now, in early versions, manual developer control is enough.

Later, client-facing consent may be needed.

Status: not started.

---

## v26 â€” Anonymization before API escalation

**Goal:** remove or replace identifying data before sending anything to external APIs.

Examples:

```text
Client name â†’ CLIENT_A
Company name â†’ COMPANY_A
Exact address â†’ [ADDRESS_REMOVED]
Bank account â†’ [ACCOUNT_REMOVED]
Phone/email â†’ [CONTACT_REMOVED]
```

Status: not started.

---

## v27 â€” API logs

**Goal:** keep a record of external model use.

Log:

```markdown
## 2026-05-18 12:05

### Reason for escalation
Long PDF summary

### Data sent
Anonymized / full / unknown

### Model used
deepseek-v4-flash

### Output
...

---
```

Status: not started.

---

# Phase 6 â€” Proactive assistant

## v28 â€” Local reminders and proactive messages

**Goal:** let the assistant send useful messages without the client asking.

Safe proactive message types:

```text
- Missing profile information
- Upcoming review date
- Calendar-based reminder
- Document still missing
- Portfolio review scheduled
- Cost comparison reminder
- Risk-profile update reminder
```

Unsafe proactive message types:

```text
- Buy this now
- Sell this now
- Market timing
- Panic messages
- Product pushing
```

Status: not started.

---

## v29 â€” Calendar/event integration

**Goal:** trigger proactive messages from calendar events.

Example:

```text
Calendar event: Review client portfolio
â†’ Bot sends: â€œToday you planned to review your portfolio. Do you want to start with your objectives, current allocation, or missing documents?â€
```

Status: not started.

---

## v30 â€” Periodic review logic

**Goal:** generate review prompts every month/quarter/year.

Possible checks:

```text
- Has risk profile changed?
- Has liquidity need changed?
- Has time horizon changed?
- Has family situation changed?
- Has tax residence changed?
- Has portfolio drifted materially?
- Are costs still acceptable?
```

Status: not started.

---

# Phase 7 â€” Advisor workflow

## v31 â€” Client prep workflow

**Goal:** prepare for a client meeting.

Flow:

```text
1. Enter client notes
2. Generate missing questions
3. Generate meeting agenda
4. Generate documents-needed list
5. Save to log
```

Status: not started.

---

## v32 â€” Portfolio review workflow

**Goal:** review an existing portfolio.

Flow:

```text
1. Paste or upload portfolio
2. Parse allocation
3. Identify risk areas
4. Identify missing data
5. Generate questions
6. Save to log
```

Status: not started.

---

## v33 â€” Product review workflow

**Goal:** review a product/fund/factsheet.

Flow:

```text
1. Paste product description or upload factsheet
2. Summarize product
3. Identify costs, risks, liquidity
4. Draft product due-diligence questions
5. Save to log
```

Status: not started.

---

## v34 â€” Follow-up email/message drafter

**Goal:** draft client follow-ups.

Output:

```text
- Summary of discussion
- Missing information
- Options to compare
- Documents requested
- Next step
```

Rule:

```text
Do not include investment recommendation unless explicitly written and approved by a human advisor.
```

Status: not started.

---

## v35 â€” Complete wealth copilot workflow

**Goal:** combine everything into a real professional workflow.

Full flow:

```text
1. Enter client case
2. Generate client profile questions
3. Generate meeting prep
4. Analyze current portfolio
5. Analyze product/factsheet
6. Compare platform/options
7. Draft investment memo
8. Draft follow-up message
9. Save complete audit trail
```

Product shape:

```text
Jordi Agent Wealth Copilot

Inputs:
- Client profile
- Portfolio
- Product documents
- Advisor notes
- Calendar events

Processes:
- Suitability preparation
- Risk review
- Platform comparison
- Product due diligence
- Memo generation
- Follow-up drafting
- Audit trail

Outputs:
- Meeting prep
- Client questionnaire
- Portfolio risk notes
- Product memo
- Platform comparison
- Follow-up message
- Logs
```

Principle:

```text
AI prepares.
Human judges.
Human decides.
AI records.
```

Status: not started.

````

Now we begin with the **first uncompleted step**:

# v7 â€” External Markdown prompt files

You do **not** change the Python yet.

First we create the prompt folder and files. We only move to Python after the files exist.

## What you need to do now

In the same folder where your `Jordi_Agent.py` file lives, create this folder:

```text
prompts
````

Inside it, create these three files:

```text
base_rules.md
wealth_policy.md
client_profile_questions.md
```

## File 1: `prompts/base_rules.md`

Paste this:

```markdown
# Base rules for Jordi Agent

You are Jordi Agent, a local-first assistant connected to Telegram.

You are not a general chatbot.
You are a narrow, practical assistant that helps with specific workflows.

General behavior:
- Be concise.
- Be clear.
- Be structured.
- Ask for missing information.
- Do not pretend certainty.
- Do not hallucinate facts.
- If you do not know something, say so.
- Use the same language as the user when possible: Spanish, Catalan, or English.

Privacy posture:
- Prefer local reasoning.
- Do not ask for unnecessary personal data.
- Do not expose sensitive information.
- When information is missing, ask questions instead of guessing.

Output style:
- Use numbered sections.
- Use short paragraphs.
- Prefer practical next steps.
- End with one small concrete next action when useful.
```

## File 2: `prompts/wealth_policy.md`

Paste this:

```markdown
# Wealth-management policy

You assist with finance, investment, and portfolio-management preparation for Spanish clients.

You are not a regulated financial advisor.
You do not give personalized investment recommendations.

Hard rules:
- Do not say "I recommend".
- Do not say "you should buy".
- Do not say "you should sell".
- Do not say "you should hold".
- Do not say a product is suitable for the client.
- Do not make final investment decisions.
- Do not optimize the portfolio as if the decision were yours.
- Do not rank one product/platform as the final best choice.
- Do not create urgency around market timing.

Allowed:
- Give options to compare.
- Explain trade-offs.
- Identify missing information.
- Identify risks.
- Generate questions for the client.
- Generate questions for a human advisor.
- Compare categories of platforms or products.
- Draft non-final memos.
- Help the client prepare for a decision.

Default answer structure:
1. What the client seems to need
2. What information is missing
3. Questions to ask the client
4. Possible options to compare
5. Main risks or warnings
6. Suggested next tiny action
7. Reminder: this is not a recommendation

Important wording:
- Say "options to compare", not "best option".
- Say "possible fit factors", not "suitable".
- Say "a human advisor should verify", not "this is correct".
- Say "the client decides", not "the assistant decides".
```

## File 3: `prompts/client_profile_questions.md`

Paste this:

```markdown
# Client profile questions

Your task is to generate client profiling questions for finance and portfolio-management preparation.

The questions should be similar in spirit to a MiFID/EAF suitability conversation, but you must not claim to perform a formal legal suitability assessment.

You should help clarify:

1. Basic context
- Age
- Country of residence
- Tax residence
- Family situation
- Dependants
- Employment or business situation

2. Investment objective
- Why is the client investing?
- Capital preservation?
- Retirement?
- Income?
- Growth?
- Future purchase?
- Inheritance planning?
- Education for children?
- Other goal?

3. Time horizon
- When will the money be needed?
- Is the horizon short, medium, or long term?
- Are there different buckets with different horizons?

4. Liquidity needs
- How much cash should remain available?
- What expenses are expected in the next 12, 24, and 60 months?
- Emergency fund needs?
- Possible real-estate purchase?
- Business needs?

5. Financial situation
- Income
- Stability of income
- Assets
- Debts
- Mortgages
- Other obligations
- Pension expectations
- Insurance coverage

6. Capacity for loss
- How much loss could the client financially tolerate?
- What drawdown would create real-life problems?
- Would a temporary 10%, 20%, or 30% fall be tolerable?
- What money must not be exposed to market risk?

7. Willingness to take risk
- How does the client emotionally react to losses?
- Has the client lived through market declines before?
- Would the client sell after a large fall?
- Does the client prefer stability or higher expected return?

8. Knowledge and experience
- Has the client invested before?
- In funds?
- ETFs?
- Stocks?
- Bonds?
- Private equity?
- Crypto?
- Structured products?
- Does the client understand volatility, liquidity, currency risk, and fees?

9. Existing portfolio
- Current assets
- Current weights
- Current platforms
- Current costs
- Current tax situation
- Unrealized gains/losses
- Concentration risks
- Currency exposure

10. Preferences and constraints
- ESG/sustainability preferences
- Preference for simple products
- Preference for indexed funds
- Preference for discretionary management or self-directed investing
- Need for Spanish tax reporting simplicity
- Need for low costs
- Ethical or sector restrictions

11. Documents needed
- Current portfolio statement
- Fund/ETF names and ISINs
- Cost breakdown
- Tax residence information
- Investment history
- Pension information
- Expected cash-flow needs
- Existing advisory agreements

When answering:
- Generate clear questions.
- Group them by topic.
- Highlight the most urgent missing information.
- Do not recommend investments.
- End with one small next action.
```

## How to test v7

After creating the files, do this in your terminal from the project folder:

```bash
dir prompts
```

On Windows, you should see:

```text
base_rules.md
wealth_policy.md
client_profile_questions.md
```

Or in PowerShell:

```powershell
Get-ChildItem prompts
```

Expected result:

```text
base_rules.md
wealth_policy.md
client_profile_questions.md
```

That is all for this step.

No Python changes yet. No Telegram test yet. This rep is only: **the prompt files exist.**

Tiny action now: create the `prompts` folder and the three files. Then tell me what you see when you run `dir prompts`.

