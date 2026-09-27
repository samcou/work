# CV variant map

Last updated: 2026-09-27
**Filled from CV v7.** The previous version was a stub written before the CVs arrived.

## The base

`cv/cv-v7-base.md` is the single source of truth. Renderer: `render_cv.py` → `.pdf` + `.docx`.
Every variant below is a *diff from base*, not a separate document. Never maintain a variant by hand
as an independent file — that's how the four old CVs diverged and ended up with broken tables.

## Variant table

| Posting type | Variant name | Lead with | Change from base |
|---|---|---|---|
| Remote IT support / service desk | `remote-support` | Intune + PowerShell automation, trilingual SLA support | Headline → "IT Support Specialist"; add remote-first line; drop project section to 1 line |
| MDM / Intune administrator | `endpoint` | Intune at scale, PowerShell provisioning automation, in-house MDM | Headline → "Endpoint Management Specialist"; **projects section stays in full** — the automation work IS the differentiator here |
| SOC / junior security | `security` | Cisco certs (Aug/Sep 2025) + PHANTOM pipeline | **Projects section becomes the centre of the CV.** Education and EC-Council move up. Recency gap closes because the certs and project are the most recent things on the page |
| Québec public sector | `qc-public` | Trilingual, no sponsorship required, formal cert listing | French-forward summary; certifications in a formal table with dates; **formal register, no "Notable Projects" hype** — this audience reads it as amateurish. Include CAF application as "pursuing" |
| French client-facing / Québec commercial | `fr` | French-language support capability | Summary in French; trilingual line foregrounded; keep English cert names untranslated (they're globally recognised) |
| MSP / NOC | `msp` | Breadth + autonomy at small-team scale | Lead with cross-platform (Win/macOS/Linux) and the multi-site FMCG + multinational logistics combo; frame broad scope as a feature |
| Southern Ontario manufacturing / logistics | `ont-manufacturing` | Multi-site Intune estate + hardware diagnostics | **The strongest existing fit.** The Rowse Honey/Valeo FMCG multi-site story sells directly to a Southwestern Ontario manufacturer with the same estate shape. Add the hardware diagnostics depth (HDD→SSD, imaging) — that posting class values it |

## Rules that apply to every variant

1. **Never inflate.** The declined Outlier framing stays declined (`USER.md` §3, `2026-09-27-cv-audit.md`).
2. **Every variant keeps the "no sponsorship required" line** — three citizenships is a genuine
   differentiator and costs one line.
3. **The gap entry is the same in all of them.** Vary the *lead*, never the facts.
4. **Check the variant before sending.** A mismatched version is worse than a generic one — the
   security CV sent to a helpdesk posting reads as "didn't read the posting."

## Known gaps in this map
- [ ] No variant has been tested against a real posting yet. The first application is the test case.
- [ ] `fr` has never been rendered — the French summary text doesn't exist yet.
- [ ] Whether `security` should *drop* the IT support experience or recast it as an asset is untested.
      Recasting as "endpoint hardening + compliance" is plausible but unproven.
- [ ] No cover-letter templates per variant yet. The `job-application` skill writes them per posting.
