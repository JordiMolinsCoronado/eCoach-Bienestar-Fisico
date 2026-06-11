# eCoach Relaciones v3 hybrid

This package keeps the existing working engine:

- Telegram bot;
- DeepSeek/Gemini LLM flow;
- document upload;
- existing memory files;
- followups;
- public enrichment;
- existing ClientData.

And adds the new architecture:

- project-based workflow board;
- Saturday pilot project;
- path choice state;
- provider choice state;
- dirty/stale/needs_rebuild flags;
- deterministic handling for key upstream revisions;
- `/workflow_board` command;
- `eCoach_Quien_Soy/` documentation layer;
- supported-sovereignty product story.

## Main file

```text
eCoach_Relaciones.py
```

## Run

Use the same `.env` you already had before.

```powershell
cd "C:\SecondBrain\OneDrive - Jordi Molins Coronado\RAM_Jordi\Prevengen\eCoaches\eCoach_Relaciones"
python eCoach_Relaciones.py
```

## New Telegram commands

```text
/workflow_board
/project_board
```

They show the internal project state.

## New state files

For each Telegram client:

```text
ClientData/telegram_<id>/projects/project_saturday_demo_funds_supported_sovereignty/
  project.json
  workflow_board.json
```

## What changed

### 1. Documents now update project state

When a PDF/XLSX/CSV/TXT/MD is uploaded:

- `documents = complete`
- `diagnosis = needs_rebuild`
- `dirty_flags += diagnosis`
- `needs_rebuild_flags += diagnosis`

### 2. Analyzing documents updates project state

When document analysis starts:

- `diagnosis = active`

### 3. Path buttons update project state

Buttons now update:

- `path_choice.selected`
- `que_quiero`
- `provider_choice`

### 4. Provider buttons update project state

Buttons now update:

- `provider_choice.selected`
- `mi_plan`
- `onboarding`
- `seguimientos`

### 5. Free text can update state before LLM

These inputs are intercepted deterministically:

```text
Espera. Esto vuelve a ser delegar. Creo que quiero cartera guiada con vuestra ayuda.
```

Marks:

- path = guided;
- Mi Plan stale;
- onboarding stale;
- seguimientos stale.

```text
Se me olvidÃ³ que tengo otros 50.000 euros en CaixaBank.
```

Marks:

- diagnosis needs_rebuild;
- proposal stale;
- Mi Plan stale;
- onboarding stale;
- seguimientos stale.

```text
Me da miedo abrir una cuenta en MyInvestor.
```

Opens a side thread without invalidating the main plan.

## Product story

```text
Banco = dependencia opaca.
Delegada = dependencia mÃ¡s limpia.
Guiada = soberanÃ­a acompaÃ±ada.
```

## Important

This is not a full rewrite. It is a safer hybrid refactor:

```text
old working engine + new architecture layer
```

