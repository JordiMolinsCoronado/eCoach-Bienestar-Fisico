# dirty_stale_policy.md

If the client changes `QuÃ© quiero`, downstream artifacts become stale.

Example:

```text
I first chose delegated, but now I want guided.
```

Then:

```text
Mi Plan = stale
Onboarding = stale
Seguimientos = stale
```

If the client adds material data:

```text
I forgot another 50,000 euros in CaixaBank.
```

Then:

```text
Diagnosis = needs_rebuild
Proposal = stale
Mi Plan = stale
Onboarding = stale
Seguimientos = stale
```

