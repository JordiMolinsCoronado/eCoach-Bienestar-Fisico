# manage_fund_portfolio.md

Purpose: help the user understand and improve a fund portfolio.

Core flow:

1. Ask for documents.
2. Analyze current portfolio.
3. Explain:
   - cartera autogestionada;
   - cartera guiada;
   - gestiÃ³n delegada.
4. Let the client choose a path.
5. Let the client choose provider/candidate.
6. Create Mi Plan.
7. Handle changed mind.
8. Mark downstream stale when upstream changes.
9. Handle side threads.
10. Create followups.

Core story:

```text
Cartera bancaria = dependencia opaca.
GestiÃ³n delegada = dependencia mÃ¡s limpia.
Cartera guiada = soberanÃ­a acompaÃ±ada.
```

Dirty/stale chain:

```text
QuiÃ©n soy
â†’ QuÃ© quiero
â†’ DiagnÃ³stico
â†’ Mi Plan
â†’ Onboarding
â†’ Seguimientos
```

