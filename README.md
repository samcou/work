# Job-hunt targeting rig

The working method behind the CV in this repo — how it was scoped, benchmarked, and matched to
posting types. Built while running an active search, not as a portfolio exercise.

**Target:** IT Support / Endpoint Management / Junior Security roles, Canada.

## What this is

A job search run as a small system rather than a folder of CVs:

| File | What it does |
|---|---|
| [`cv/cv-v7-base.md`](cv/cv-v7-base.md) | Single source of truth for the CV. Every variant is a diff from this, not a separate file. |
| [`cv/Samuel_Couchman_CV_v7.pdf`](cv/) | Rendered 2-page ATS-clean output. |
| [`render_cv.py`](render_cv.py) | Markdown → PDF/DOCX. The reason the CV never drifts from its source. |
| [`strategy.md`](strategy.md) | Title tiers, French equivalents, and the positioning split per posting type. |
| [`boards.md`](boards.md) | Verified job boards, pasteable search queries, and target locations. |
| [`salary-research.md`](salary-research.md) | Live salary benchmarking per title, with a proposed target and walk-away floor. |
| [`variant-map.md`](variant-map.md) | Which CV variant goes to which posting, and what changes. |
| [`tracker.md`](tracker.md) | Application pipeline with stale-flagging and dated next actions. |
| [`cv-audit.md`](cv-audit.md) | The pre-rebuild assessment of four older CVs. |

## The two decisions that did the most work

**1. The CV has one source of truth.** The four previous CVs had diverged into a broken table
here, an inflated "3+ years" claim there. `cv-v7-base.md` plus a renderer means a variant is a
diff, not a fork.

**2. Endpoint management + French is the actual ceiling, not Tier 1 helpdesk.** Benchmarking
surfaced a live CMHC posting — *Bilingual Endpoint Management Specialist* — at **CA$86,816–108,520**,
against a Tier 1 service-desk average of ~CA$58,000. The Intune-at-scale work plus a working
French profile is the lever, and it points at a federal housing corporation rather than a fantasy
employer. Tier 1 sets the floor; Tier 2 is where the pay is.

## Honesty constraint

There is a 22-month employment gap. The temptation is to describe it as continuous part-time work
that wasn't. That framing is used nowhere in this repo, and the reasoning is written up in
[`cv-audit.md`](cv-audit.md): a false duration is the one claim class that collapses under a single
follow-up date question, and it turns a survivable gap into a credibility problem across the whole
CV. The gap entry instead carries what is actually true — dated certifications, named projects, a
concurrent CAF application.

## Rebuilding the CV

```bash
python3 render_cv.py
```

Writes both PDF and DOCX. Edit `cv/cv-v7-base.md` only.

## Tooling notes

Built on a 1 vCPU / 2 GB box, so everything here is deliberately static: no server, no runtime
dependencies beyond `reportlab`/`python-docx`, no build step. A dashboard over these files was
considered and rejected — it would render a pipeline that isn't moving.
