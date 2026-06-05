---
name: neuromarketing
description: Create and optimize conversion-focused copy using evidence-based neuromarketing and behavioral psychology principles. Use when writing or rewriting ads, landing pages, emails, sales pages, product pages, scripts, headlines, CTAs, or campaign messaging that must increase attention, trust, and action without manipulative claims. Also use for message strategy, objection handling, A/B variants, and structured copy audits with clear rationale.
---

# Neuromarketing Copywriting

## Overview
Use this skill to produce high-conversion, ethical copy that maps each major claim to a persuasion principle.
Default to the user's language. If language is not specified, ask once or mirror the conversation language.

## Execution Standard
Follow this order every time:
1. Capture brief inputs.
2. Build persuasion strategy.
3. Draft with channel blueprint.
4. Audit and refine.
5. Deliver variants and test plan.

Do not skip steps unless the user explicitly asks for a fast draft.

## 1) Capture Brief Inputs
Collect decision-critical inputs before drafting:
- Audience: ICP, awareness level, pains, desired outcomes.
- Offer: product or service, mechanism, differentiation, price context.
- Goal: conversion type, primary CTA, funnel stage.
- Channel: landing page, email, ad, social post, script, or other.
- Constraints: tone, legal limits, brand voice, banned claims.
- Proof: testimonials, data, case results, guarantees, authority cues.
- Practical limits: word or character limit, language, deadline.

If critical inputs are missing, ask focused questions first.
If the user wants speed, state assumptions explicitly and continue.

## 2) Build Persuasion Strategy
Before writing, create a short strategy block with:
- Core tension: current pain vs desired state.
- One-sentence value proposition.
- Objection map: top 3-5 objections and proof to neutralize each.
- Decision triggers: choose 3-6 principles from [principles.md](references/principles.md).
- Risk controls: compliance boundaries from [ethics-and-compliance.md](references/ethics-and-compliance.md).

## 3) Draft With Blueprint
Select the relevant format in [channel-blueprints.md](references/channel-blueprints.md) and map each section to one decision objective.
Always enforce:
- Prefer concrete language over vague claims.
- Keep sentences short and cognitively easy.
- Put evidence before intensity.
- Use one primary CTA per asset.

## 4) Audit and Refine
Evaluate the draft with [quality-rubric.md](references/quality-rubric.md).
If available, run:

```bash
python3 scripts/neuro_audit.py --file <draft.txt>
```

Revise until all are true:
- Total rubric score is at least 85 out of 100.
- No red-flag claims from [ethics-and-compliance.md](references/ethics-and-compliance.md).
- Every major claim has proof or a bounded qualifier.
- CTA is explicit, low-friction, and context-appropriate.

## 5) Deliver Output Package
Return output in this structure:
1. Final copy.
2. 2-5 variants (angle, headline, and CTA changes).
3. Rationale map: phrase -> principle -> intended effect.
4. A/B test plan:
   - Hypothesis per variant.
   - Primary metric (CTR, CVR, reply rate, or other channel metric).
   - Secondary guardrail metric.
   - Stop or continue rule.
5. Known assumptions and required follow-up data.

## Non-Negotiable Rules
- Do not invent data, testimonials, or credentials.
- Do not use fake scarcity, fake urgency, or deceptive framing.
- Do not make medical, legal, or financial outcome guarantees.
- Do not overclaim "neuroscience" without real evidence.
- Prefer precision, honesty, and customer benefit over pressure tactics.

## Resources
Read only what is needed:
- [references/principles.md](references/principles.md): persuasion principles and usage guardrails.
- [references/channel-blueprints.md](references/channel-blueprints.md): templates per channel.
- [references/quality-rubric.md](references/quality-rubric.md): scoring rubric and revision protocol.
- [references/ethics-and-compliance.md](references/ethics-and-compliance.md): red lines and safe alternatives.
- [scripts/neuro_audit.py](scripts/neuro_audit.py): heuristic draft audit helper.
