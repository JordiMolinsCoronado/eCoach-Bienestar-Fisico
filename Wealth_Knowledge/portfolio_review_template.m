# Portfolio Review Template

## Purpose

This file helps review an existing portfolio before any human decision.

The assistant may summarize, identify exposures, flag risks, and generate questions.
The assistant must not recommend buying, selling, or holding anything.

---

## 1. Portfolio identity

Collect:

- Client name or anonymized client ID
- Review date
- Portfolio value
- Currency
- Platform or custodian
- Account type
- Tax residence
- Investment objective
- Time horizon
- Liquidity needs
- Risk profile if available

---

## 2. Allocation summary

Summarize current allocation by:

- Asset class
- Region
- Currency
- Sector
- Product type
- Provider
- Liquidity bucket
- Risk level

Possible asset classes:

- Cash
- Deposits
- Money market
- Government bonds
- Corporate bonds
- High-yield bonds
- Equity funds
- ETFs
- Individual stocks
- Real estate
- Private equity
- Commodities
- Gold
- Cryptoassets
- Structured products
- Other alternatives

---

## 3. Concentration risks

Check:

- Single product concentration
- Single provider concentration
- Single bank/platform concentration
- Single country concentration
- Single sector concentration
- Single currency concentration
- Single issuer concentration
- Private/illiquid exposure concentration
- Business-owner concentration if client also has company equity

Ask:

- What percentage is held in the top 1, 3, 5, and 10 positions?
- Is any single position large enough to materially affect the portfolio?
- Does the client understand the concentration?

---

## 4. Liquidity review

Group assets by liquidity:

- Immediate liquidity
- Daily liquidity
- Weekly liquidity
- Monthly liquidity
- Quarterly liquidity
- Locked or illiquid
- Unknown liquidity

Ask:

- What money is needed in the next 12 months?
- What money is needed in 2–5 years?
- Are illiquid assets matched with a long enough time horizon?
- Are there redemption gates or notice periods?

---

## 5. Currency exposure

Check:

- Portfolio base currency
- Asset currency
- Fund share-class currency
- Underlying exposure currency
- Hedged or unhedged exposure
- Currency conversion costs
- Currency mismatch with client expenses

Ask:

- In what currency does the client spend?
- Is the client comfortable with currency fluctuation?
- Is currency exposure intentional or accidental?

---

## 6. Cost overview

Collect:

- Fund TER / OCF
- Management fees
- Advisory fees
- Custody fees
- Trading costs
- Subscription/redemption costs
- Performance fees
- Currency conversion costs
- Hidden spreads
- Retrocessions
- Clean share-class availability

Ask:

- What is the all-in annual cost?
- Are costs transparent?
- Are there lower-cost comparable share classes?
- Are retrocessions present?
- Does the client understand the fees?

---

## 7. Risk review

Identify:

- Market risk
- Credit risk
- Interest-rate risk
- Duration risk
- Inflation risk
- Liquidity risk
- Currency risk
- Concentration risk
- Manager risk
- Counterparty risk
- Product-complexity risk
- Tax/reporting risk
- Behavioural risk
- Sequence-of-returns risk

---

## 8. Suitability-style questions

Do not decide suitability. Ask:

- What objective does this portfolio serve?
- Does the time horizon match the asset mix?
- Does the client need income, growth, preservation, or liquidity?
- What drawdown could the client financially tolerate?
- What drawdown could the client emotionally tolerate?
- Does the client understand the products?
- Is the current portfolio consistent with stated preferences?
- Are there conflicts between liquidity needs and asset liquidity?
- Are there tax or reporting issues to verify?

---

## 9. Missing information

Common missing fields:

- ISINs
- Product names
- Market values
- Weights
- Asset classes
- Currencies
- Costs
- Liquidity terms
- Tax situation
- Unrealized gains/losses
- Platform/custodian details
- Client objectives
- Risk profile
- Time horizon
- ESG preferences
- Product documents

---

## 10. Red flags

Flag:

- Percentages do not add to 100%
- Unknown products
- Unknown costs
- Unknown liquidity
- High concentration
- Complex products without clear client understanding
- Illiquid products with short-term needs
- Currency mismatch
- High fees
- Tax-reporting uncertainty
- Product pushed before client profile is clear
- Risk profile inconsistent with allocation
- No emergency cash despite long-term investments
- Heavy exposure to employer/business/sector already tied to client income

---

## 11. Portfolio review output format

Use this format:

```markdown
# Portfolio Review

## Allocation summary

## Concentration risks

## Liquidity risks

## Currency risks

## Cost questions

## Tax/reporting questions

## Missing information

## Red flags

## Questions before deciding anything

## Suggested next tiny action

## Reminder

This is not an investment recommendation.
This review supports comparison and human review only.