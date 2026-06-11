## Jordi Agent roadmap

### v0 â€” Working echo bot

**Goal:** prove Telegram bot is alive.

Features:

```text
/start
Echoes normal messages
```

Status: done.

---

### v1 â€” Capture messages to Markdown inbox

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

### v2 â€” `/inbox` command

**Goal:** retrieve recent captures.

Features:

```text
/inbox
```

Shows last 10 captured items.

Status: done.

---

### v3 â€” `/today` command

**Goal:** show todayâ€™s captures only.

Features:

```text
/today
```

Shows all captures from current date.

Status: done.

---

### v4 â€” Local LLM `/ask`

**Goal:** connect Jordi Agent to local Gemma via Ollama.

Features:

```text
/ask Give me one tiny action for today
```

Bot sends the question to:

```text
gemma4:e4b-it-q4_K_M
```

and returns the answer in Telegram.

Status: done or near-done.

---

### v5 â€” Main Telegram button menu

**Goal:** reduce friction; stop relying only on slash commands.

Buttons:

```text
ðŸ§  Ask       ðŸ“¥ Inbox
ðŸ“… Today     âœï¸ Capture
```

Status: done.

---

### v6 â€” Stateful buttons

**Goal:** make buttons conversational.

Flow:

```text
Tap ðŸ§  Ask
â†’ bot asks: â€œWhat do you want to ask?â€
â†’ next message goes to Gemma
```

And:

```text
Tap âœï¸ Capture
â†’ bot asks: â€œWhat should I capture?â€
â†’ next message is saved
```

Status: done.

---

## Now the wealth-management path begins

### v7 â€” Wealth Mode

**Goal:** add a dedicated wealth-management reasoning mode.

New button:

```text
ðŸ’¼ Wealth
```

Flow:

```text
Tap ðŸ’¼ Wealth
â†’ bot asks: â€œWhat wealth-management case should I analyze?â€
â†’ next message goes to Gemma with a special wealth prompt
```

The AI should answer using this structure:

```text
1. Summary
2. Key risks
3. Missing information
4. Questions to ask
5. Possible next tiny action
```

Important rule:

```text
No buy/sell/hold recommendations.
Analysis only.
Human decides.
```

---

### v8 â€” Wealth logs

**Goal:** save every wealth analysis for traceability.

New file:

```text
Wealth_Logs.md
```

Each analysis saves:

```markdown
## 2026-05-15 11:10

### User input
Client is 62, sold business, has â‚¬2M cash...

### Model
gemma4:e4b-it-q4_K_M

### AI analysis
Summary...
Risks...
Missing information...
Questions...
Next action...
```

This matters because wealth management needs an audit trail.

---

### v9 â€” Portfolio text parser

**Goal:** let Jordi Agent understand simple portfolio descriptions.

Input:

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
Allocation summary
Main concentration risks
Liquidity risks
Currency risks
Questions before advising
```

No optimization yet. Just structured understanding.

---

### v10 â€” Suitability checklist generator

**Goal:** create a MiFID-style pre-advice checklist.

Input:

```text
Client is 58, entrepreneur, wants retirement income, moderate risk.
```

Output:

```text
Investment objective
Time horizon
Risk tolerance
Capacity for loss
Liquidity needs
Tax residence
Knowledge and experience
ESG preferences
Existing exposure
Documents needed
```

This becomes a very strong professional feature.

---

### v11 â€” Investment memo generator

**Goal:** draft one-page investment memos.

Input:

```text
Product: European short-duration bond fund
Client: conservative, 3-year horizon, wants income
```

Output:

```text
Investment memo:
- Product summary
- Potential role in portfolio
- Fit / not fit factors
- Main risks
- Fees/liquidity questions
- Suitability concerns
- Human decision required
```

This is high-value because advisors constantly need clear written reasoning.

---

### v12 â€” RAG over your own wealth documents

**Goal:** allow Jordi Agent to answer using your own PDFs, notes, policies, and frameworks.

Local knowledge folder:

```text
/Wealth_Knowledge/
  investment_policy.md
  mifid_checklist.md
  client_meeting_template.md
  product_due_diligence_template.md
```

Bot can answer:

```text
Using my wealth framework, what questions should I ask this client?
```

Instead of relying only on the modelâ€™s general knowledge, it retrieves your own documents first.

This is where Jordi Agent becomes yours.

---

### v13 â€” CSV / Excel portfolio import

**Goal:** analyze real portfolio files.

Input files:

```text
portfolio.csv
portfolio.xlsx
```

Columns might be:

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
```

Output:

```text
Asset allocation
Currency exposure
Top holdings
Concentration risk
Liquidity buckets
Missing fields
Questions for advisor
```

This is the beginning of real wealth-tech utility.

---

### v14 â€” PDF factsheet summarizer

**Goal:** summarize fund factsheets, KIIDs, manager reports, or product PDFs.

Flow:

```text
Upload / point to PDF
â†’ extract text
â†’ summarize
â†’ identify risks
â†’ draft advisor questions
```

Output:

```text
1. Product summary
2. Strategy
3. Fees
4. Liquidity
5. Risk indicators
6. Hidden concerns
7. Questions before recommendation
```

This is very useful because factsheets are dense and repetitive.

---

### v15 â€” Advisor workflow: client prep â†’ memo â†’ follow-up

**Goal:** combine everything into a real professional workflow.

Full flow:

```text
1. Enter client case
2. Generate meeting prep
3. Generate suitability checklist
4. Analyze portfolio
5. Analyze product/factsheet
6. Draft investment memo
7. Draft follow-up email
8. Save complete audit trail
```

Example:

```text
Tap ðŸ’¼ Wealth
â†’ Choose â€œClient prepâ€
â†’ Paste client notes
â†’ Bot creates questions
â†’ Paste portfolio
â†’ Bot identifies risks
â†’ Paste product factsheet
â†’ Bot drafts memo
â†’ Bot drafts follow-up email
â†’ Everything saved to Wealth_Logs.md
```

v15 is the first version that feels like an actual **AI wealth-management assistant**, not just a chatbot.

The shape of v15:

```text
Jordi Agent Wealth Copilot

Inputs:
- Client profile
- Portfolio
- Product documents
- Advisor notes

Processes:
- Suitability check
- Risk review
- Document summary
- Memo generation
- Follow-up drafting

Outputs:
- Meeting prep
- Portfolio risk notes
- Investment memo
- Follow-up email
- Audit trail
```

The principle:

```text
AI prepares.
Human judges.
Human decides.
AI records.
```

That is the correct posture for wealth management. Not magic. Not gambling. Not hallucinated authority. A disciplined copilot.

