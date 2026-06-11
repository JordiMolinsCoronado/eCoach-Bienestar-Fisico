# Mortgage fixed vs variable vs mixed playbook

## Scope

Use this playbook when the client asks whether to:
- keep a variable mortgage;
- switch from variable to fixed;
- switch to mixed mortgage;
- compare fixed, variable and mixed rates;
- decide after Euribor increases;
- accept a bank novation/subrogation offer.

Spanish examples:
- hipoteca fija vs variable;
- hipoteca mixta;
- cambiar hipoteca variable a fija;
- novaciÃ³n hipotecaria;
- subrogaciÃ³n;
- cuota ha subido por EurÃ­bor;
- miedo a que suba el EurÃ­bor.

## Core principle

This is not only a question of which option is mathematically cheapest.

The decision combines:
- expected interest cost;
- payment stability;
- emotional tolerance for variable payments;
- household cash-flow safety;
- cost of switching;
- future optionality;
- risk that Euribor rises;
- risk that Euribor falls after fixing;
- length of remaining mortgage term.

## First-pass calculation

If the client gives principal, remaining term and offered rates, eCoach should do a rough calculation before asking for documents.

Calculate approximate monthly payments for:
- current variable, using an explicit Euribor assumption;
- fixed offer;
- mixed offer during fixed period;
- mixed offer after fixed period under several Euribor scenarios.

If current Euribor is not provided, do not use placeholders like X or Y.
Use clear assumptions.

Good:
"Si usamos un EurÃ­bor orientativo del 2,7%, la variable serÃ­a aproximadamente 3,6%."

Bad:
"Si el EurÃ­bor ronda X%, la cuota serÃ­a Yâ‚¬."

Always label assumptions clearly.

## Approximate mortgage payment formula

The model can estimate monthly payment using standard amortization intuition, but should say it is approximate.

It does not need exact bank-level precision.

For a 220,000â‚¬ mortgage over 25 years:
- around 3.2% fixed is roughly 1,065â‚¬â€“1,075â‚¬/month;
- around 3.6% variable is roughly 1,110â‚¬â€“1,120â‚¬/month;
- around 2.6% fixed for 5 years is roughly 995â‚¬â€“1,005â‚¬/month.

Use ranges, not false precision.

## Fixed mortgage

Advantages:
- payment certainty;
- emotional peace;
- easier household budgeting;
- protects against rate increases.

Disadvantages:
- may be more expensive if Euribor falls;
- can reduce flexibility if switching costs exist;
- client pays an insurance-like premium for certainty.

Useful wording:
"El tipo fijo compra tranquilidad. Puede no ser el mÃ¡s barato en todos los escenarios, pero elimina una parte importante de incertidumbre."

## Variable mortgage

Advantages:
- benefits if Euribor falls;
- may be cheaper over time if rates normalize downward;
- usually keeps more flexibility.

Disadvantages:
- payment uncertainty;
- stress if rates rise;
- household budget risk.

Useful wording:
"La variable puede ser mÃ¡s barata si los tipos bajan, pero le exige tolerar incertidumbre real."

## Mixed mortgage

Advantages:
- lower payment during initial fixed period;
- temporary relief;
- possibly better spread later than current variable.

Disadvantages:
- risk returns after fixed period;
- can create false comfort;
- must analyze what happens after year 5/10;
- future Euribor is unknown.

Useful wording:
"La mixta no elimina el riesgo; lo aplaza."

## Switching costs

Before accepting any change, ask for:
- novation fee;
- subrogation cost if applicable;
- appraisal/tasaciÃ³n;
- notary/registry/gestorÃ­a if applicable;
- new linked products;
- insurance requirements;
- opening or modification fees;
- early repayment rules.

## Scenario comparison

Ask the bank for written simulations:
- current variable if Euribor stays at current level;
- current variable if Euribor falls to 1%, 2%;
- current variable if Euribor rises to 3%, 4%;
- fixed offer;
- mixed offer during fixed years;
- mixed offer after fixed period with Euribor at 1%, 2%, 3%, 4%.

Compare:
- monthly payment;
- TAE;
- total interest paid;
- switching cost;
- linked products;
- flexibility.

## Emotional factor

If the client says they are afraid or the payment causes stress, acknowledge it.

But do not decide only from fear.

Good:
"El miedo a una cuota variable es informaciÃ³n importante, pero no debe ser el Ãºnico dato."

## Copy-paste message

Provide a true copy-paste message to the bank asking for:
- current outstanding balance;
- remaining term;
- current variable TIN/TAE and next revision date;
- fixed offer TIN/TAE and monthly payment;
- mixed offer TIN/TAE, payment during fixed period and later spread;
- simulations under Euribor scenarios;
- all switching costs;
- linked products;
- early repayment conditions;
- offer validity date.

## Answer structure

A good answer should include:

1. Acknowledge concern.
2. Do not sign yet.
3. Rough payment comparison with explicit assumptions.
4. Explain fixed vs variable vs mixed in plain language.
5. Mention switching costs and linked products.
6. Provide copy-paste message.
7. One next action.

## Quality floor

Do not answer only "ask the bank".
Do not use X/Y placeholders.
Do not present Euribor assumptions as facts.
Do not imply fixed is always better because it is calmer.
Do not imply variable is always better because rates may fall.

