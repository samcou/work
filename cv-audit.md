---
title: "CV audit — 4 files read, ordered, and assessed"
tags: [job-hunt, cv, audit, applications]
status: active
updated: 2026-09-27
---

# CV audit — 2026-09-27

Files read in `job-hunt/cv/`. Ordered by internal evidence, since PDF creation dates are
stripped (two are Google Docs exports with no Info dates; v6 has no embedded date at all).

## Ordering — how it was established

| Order | File | Evidence for that position |
|---|---|---|
| 1 (oldest) | `CV_8.docx` | UK address (Wallingford OX10), phone `+44`, no Canadian work auth line, "Learning SQL/Rust", Udemy course list (Ermin Kreponic, 2016–17), named reference with partial email, flat bullet style. Pre-dates all 2025 certifications. |
| 2 | `Samuel_Couchman_ITAnalystResume.pdf` | First to claim Ottawa + "Canadian Citizen — eligible to work in Canada, UK & EU". Security-forward framing. Has "3+ years hands-on" Windows claim. |
| 3 | `Samuel_Couchman_Resume_v5.pdf` | Same Ottawa address, support-forward framing, certifications separated out properly. |
| 4 (newest) | `Samuel_Couchman_Resume_v6.pdf` | **Drummondville, QC** — only file with the correct current location. Merged certs+skills, 2 pages. |

## RESOLVED 2026-09-27 — corrections to the audit above

1. **Intune was at Rowse Honey, not Simon Hegele.** `USER.md` §3 was wrong; corrected there.
   v5/v6 are right, CV_8 simply omitted it. **The blocking concern is cleared** — the newer
   CVs are accurate on this point and the lead is real.
2. **Work eligibility: three passports, three citizenships — Canada, UK, Germany.** German
   citizenship = EU work rights directly. The "cut the EU line" flag above is **void**; the
   line is accurate and is a genuine differentiator.
3. **The 22-month gap was not unemployment in the way it reads.** It was structured
   self-study (leading to the Cisco certifications actually obtained in Aug/Sep 2025),
   Outlier AI-training work, family support, and the CAF application.
4. **No French-Canadian CV exists.** It is to be built, not located.

### The one thing I declined

Sam proposed writing Outlier as 22 months of steady part-time work — and volunteered
"it's definitely not been that for 22 months but we don't have to say that necessarily."

**Declined, and it stays declined.** A false duration is the only claim class that reliably
falls apart under a single follow-up date question, and it converts a survivable gap into
a credibility problem across the whole CV. The gap is not the problem. A caught
inconsistency is.

**What goes there instead** — fully true, closes the gap, costs nothing:

> **Independent — Self-Directed Study & AI Training** · Nov 2024 – Present
> - Contract AI-training work with a distributed employer (remote).
> - Self-directed study toward Cisco cybersecurity certifications, obtained Aug–Sep 2025.
> - Independent project development in security research and applied AI (PHANTOM, GENESIS).
> - Pursuing Canadian Armed Forces Cyber Operator application.

This is stronger than a padded Outlier entry, because it is *true and specific*: real
certifications with real dates, real named projects, a real concurrent track. A recruiter
reading it learns four things instead of one.

**Also rejected:** splitting the period into several overlapping part-time entries to pad
the appearance of continuous employment. Same defect, repeated.

Related: [[USER]] §3

---

**Corroborating timeline from cert dates:** EC-Council 2021 → 01 Founders 2022–2024 →
SF consulting Oct–Nov 2024 → Cisco Ethical Hacker Aug 2025 → Cisco Junior Cybersecurity
Sep 2025 → Google AI Essentials Feb 2026. So v5/v6 were built Feb 2026 or later; CV_8
predates Aug 2025.

## The three things that actually matter

### 1. There is an employment hole and the CV hides it

Employment ends **Nov 2024** (SF consulting). Today is Sept 2026. That is a **~22-month
gap** with nothing on the page. The volunteer role is marked "Oct 2018 – Present", so the
reader technically sees something — but "present" on unpaid charity IT is not employment,
and padding it that way invites the question rather than pre-empting it.

**Missing entirely: Outlier.** That is real paid AI-training work and it appears on no CV.
It is the answer to "what have you been doing" and its absence is the single largest
weakness in the document.

**Also unaccounted:** roughly Dec 2024 → Jul 2025 (between SF and the Cisco certs). He
should decide whether 01 Founders ran to late 2024 and what filled that window.

### 2. v6 — the newest file — is the most broken

- **Certifications and Languages are mangled into one broken table.** The markdown table
  did not survive PDF export: `CERTIFICATIONS & TRAINING LANGUAGES` has a two-column grid
  with languages dumped into the right-hand column.
- **TECHNICAL SKILLS is a single run-on paragraph.** All seven categories concatenated with
  no line breaks. Visually bad and **worse for ATS parsing**, which is how most Canadian
  postings are pre-filtered.
- Page 1 of 2, ending mid-Education.

**Recommendation: do not send v6 as-is.** v5 has the same run-on skills paragraph but a
cleaner certifications section. v5 is the better base to build from.

### 3. Intune appears to have moved employers between CV_8 and v5

- **CV_8 (Simon Hegele)**: inventory, ticketing, AD, cross-platform support, German→English
  docs, onboarding, **network ports**. **No Intune, no MDM, no PowerShell.**
- **CV_8 (Rowse Honey)**: AD, M365, IFS, JIRA, Sophos, hardware. **No Intune either.**
- **v5/v6**: Intune + PowerShell automation + in-house MDM are attributed to **Rowse
  Honey**; MDM (unnamed) to Simon Hegele.
- **USER.md §3**: the MDM/Intune migration is attributed to **Simon Hegele**.

So either he did Intune at both, or the migration was relocated in the newer CVs. This
needs a straight answer before anything is sent — an interviewer who probes "where did
you do the Intune work" and gets a different answer than the CV implies is a much worse
outcome than a shorter CV.

## Other flags

**Claims to verify before sending:**
- **"eligible to work in the European Union (EU)"** — Canadian citizenship does not confer
  EU work rights. Depends on descent through family. If unconfirmed, this is the kind of
  claim that unravels in a screening call. Recommend cutting or confirming.
- **"Windows 10/11 (3+ years hands-on)"** (ITAnalyst CV) — employment totals ~2 years.
  Contradicts the rest of the document and USER.md. Inflated.
- **"Advanced Cyber Security — EC-Council (2021)"** listed as a *certification*. CV_8
  describes it as a course (Apr–Jul 2021) plus "studying towards Certified Ethical Hacker
  (in progress)" — never completed. Listing the in-progress path as a cert is overstatement.
- **PowerShell/Intune automation** — not in CV_8 at all, so unverified by an earlier
  document. Probably true (he built tooling), but it is the first thing an interviewer will
  drill.
- **SF consulting bullets are empty** — "supported architecture decisions and operational IT
  planning" says nothing. Confidentiality is legitimate; add "details on request".

**Farsi** appears in CV_8 but is dropped from v5/v6. Probably the right call for a Canadian
application. Confirm it was a choice.

**CV_8 should be retired outright** — it is not salvageable as a document and its
references section leaks a partial email. Keep it for content archaeology only.

**Missing from all four CVs and worth considering:**
- Outlier (paid, current)
- Synapse, ARIA, McKenna, fiver-bot — only PHANTOM and GENESIS appear
- AON (too early to claim, but worth a line once it exists)
- No French-Canadian-market variant here. USER.md says one exists — not in this upload.

## Verdict

**v5 is the base to build from.** v6 has the correct location but broken formatting.
ITAnalyst is the security angle and needs the "3+ years" and SIEM-adjacent claims tightened.
CV_8 is history.

Best assets, ranked:
1. **Intune/MDM + PowerShell automation** — genuinely scarce for his level, and the single
   best lever into Tier 2 pay.
2. **Trilingual support with documented professional translation** — rare and concrete.
3. **CISCO certs + PHANTOM/GENESIS** — the security pivot, and the only route to a better
   ceiling than helpdesk.
4. Cross-platform support (Win/macOS/Linux) + multi-site FMCG + multinational logistics.

Weakest point, in order: **the 22-month gap**, then the **v6 formatting**, then the
**unverified Intune attribution**.

## Open questions for Sam
1. Did you do the Intune work at Rowse Honey, Simon Hegele, or both? (blocking)
2. EU work eligibility — is that descent-based and confirmed?
3. What filled Dec 2024 → Jul 2025?
4. Outlier — worth adding, and described how?
5. Where's the French-Canadian version?
