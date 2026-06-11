# initial_discovery.md

Purpose: handle the initial conversation until a concrete task is discovered.

For the Saturday pilot, the concrete task is:

```text
improve_fund_portfolio
```

Expected input:

```text
Tengo fondos en mi banco y no los entiendo.
```

Handoff:

```json
{
  "detected_task": "improve_fund_portfolio",
  "handoff_skill": "manage_fund_portfolio"
}
```

