# Where to search — verified 2026-09-27

Every link below was probed live this date. Placeholders from the previous version are gone.
Search in **English and French both** — the Québec market is bilingual-indexed and French queries surface
postings English queries miss.

## Tier A — check every day (this is the whole habit)

| board | why | notes |
|---|---|---|
| **Indeed Canada** — https://ca.indeed.com | volume king | 10 min/day, alerts per query. Filter scam spam fast. |
| **Job Bank** — https://www.jobbank.gc.ca/jobsearch | government-mandated postings | best for public sector + Québec. Province pages: `/browsejobs/province/ON` and `/province/QC` |
| **LinkedIn** — https://ca.linkedin.com/jobs | recruiters actually work this market | keep profile live; agencies reach out here unsolicited |
| **Glassdoor** | decent Canadian coverage | use it for salary research, not applications |

## Tier B — regional / local, high hit rate

| board | region | why |
|---|---|---|
| **Jobillico** — https://jobillico.com | Québec, strong French coverage | reliable Québec-only board, filterable by sector *and* province |
| **Québec Emploi (gouv)** — https://www.quebecemploi.gouv.qc.ca/plateforme-emploi | Québec, official | provincial public-sector + government-contract listings |
| **Guichet-Emplois** — https://www.guichetemplois.gc.ca | Québec, federal | Service Canada official, different listings from Job Bank |
| **WeTech Alliance** — https://www.wetech-alliance.com/jobs/ | **Windsor-Essex** | regional tech board, dense with IT + manufacturing IT |
| **London Tech Jobs** — https://londontechjobs.ca | **London ON** | regional, hits WSIB / Fanshawe / healthcare IT |
| **ITjobs.ca** — https://www.itjobs.ca | national, Canada | IT-only, higher signal density than Indeed |

## Tier C — remote-first

| board | notes |
|---|---|
| **Remote OK** — https://remoteok.com/remote-jobs-in-canada?location=CA | filterable to Canada. `/remote-technical-jobs` is the relevant subcategory |
| **We Work Remotely** — https://weworkremotely.com | remote-heavy with a real filter; `/categories/remote-customer-support-jobs` |
| **Remote.co** | `/remote-jobs/customer-service` |
| **Himalayas** | remote listings, small-team heavy, decent for early-career |
| **LinkedIn remote tech support** — https://ca.linkedin.com/jobs/remote-tech-support-jobs | direct filtered view |
| **ZipRecruiter Ontario** | https://www.ziprecruiter.com/Jobs/Remote-It-Support-Specialist/--in-Ontario | high volume, heavy noise, US-adjacent — use as a funnel, filter hard |

## Direct-employer routes (skip the aggregators)

**This is the underrated move.** Aggregators have the generic helpdesk candidates; career pages
have the jobs nobody reposted.

- **MSPs (managed service providers)** — Québec has a dense MSP scene, and they hire Tier 1
  continuously. This is the fastest route to a first salary, and remote-friendly by business model.
  Independently-owned MSPs, not the national chains — they post nowhere else.
- **Quebec public sector IT** — structured hiring, slower, very stable. Boards: Québec Emploi +
  `carrieres.gouv.qc.ca`
- **Manufacturing / logistics / food-processing companies in southern Ontario** — these run
  multi-site Intune estates, which is literally the Rowse Honey experience. Wabtec (London) is one
  confirmed example with an active careers page.
- **Niche telecom / NOC** — check target employers' career pages directly. Candidates: March Networks
  (Ottawa), and the regional telcos.

## Agencies already holding his CV
- **Stack IT**
- **LeverageTek**

Nudge every 3–4 weeks. Costs nothing, agencies are slow, and these two already have the file.

## Plug-in search strings — what to actually type

Boards are useless without the query. These are ready to paste, split by board type.
Set an alert on each — Indeed and Job Bank both support saved searches with email alerts, and that
is the only way this stays a 10-minute-a-day habit rather than a 2-hour spiral.

### On aggregators (Indeed, Job Bank, Glassdoor, LinkedIn)
```
"IT support specialist" OR "service desk analyst" OR "helpdesk analyst"
"desktop support" OR "end user computing" OR "EUC analyst"
"IT support" AND (Intune OR "endpoint management" OR MDM)
"soc analyst" OR "security analyst" AND (junior OR tier 1)
```
Filter: **Remote** toggle on, **last 7 days** (or 24h during an active push), Canada.

### On the French boards (Jobillico, Québec Emploi, Guichet-Emplois)
```
technicien(ne) soutien informatique
technicien(ne) informatique
analyste du centre de services
administrateur système
gérant des accès
technicien(ne) soutien aux utilisateurs
analyste sécurité
```

### On the remote boards (Remote OK, We Work Remotely, Remote.co, Himalayas)
```
IT support
technical support
service desk
end user computing
endpoint management
```
Remote OK path: `/remote-jobs-in-canada?location=CA` then the `/remote-technical-jobs` subcategory.

### On Workopolis (missed in the previous version — strong Canadian coverage, good salary filters)
```
intune | endpoint | "service desk" | "IT support"
```
https://www.workopolis.com — 285+ Intune openings/week at time of writing. Salary filter is
reliable there, which makes it the best board for validating the target salary in
`salary-research.md`.

## Locations to plug in

**Southern Ontario (your stated preference — proximity to Battle Creek MI)**
Windsor · Sarnia · London · Kitchener-Waterloo · Cambridge · Guelph · Brantford · Hamilton ·
St. Catharines · Niagara · Toronto (outer GTA) · Windsor-Essex region via WeTech Alliance

**Québec — local and remote**
Drummondville (home base) · Sherbrooke · Granby · Trois-Rivières · Québec City · Montréal ·
Laval · Longueuil · Brossard

**Ottawa / Gatineau** — the endpoint/Intune postings are federally concentrated here, and it's the
highest-paying corridor on the Tier 2 list. Medium-term goal per strategy.md.

**Elsewhere, if the role is right**
Calgary · Edmonton · Halifax · Moncton. Not a stretch — "anywhere in Canada" means anywhere, and
Alberta/Atlantic postings carry the lower cost of living that makes an offer pay.

## TODO
- [ ] Probe MSP career pages in the East-Shore / Drummondville corridor and add named employers
- [ ] Add recruiter contacts as they come
- [ ] Validate the target salary against 10 real postings (see `salary-research.md`)
