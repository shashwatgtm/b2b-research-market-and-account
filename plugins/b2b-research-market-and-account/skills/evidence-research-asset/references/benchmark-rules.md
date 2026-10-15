# Benchmark study rules

A benchmark scores many companies on public signals and publishes what it finds. It earns trust only if anyone who reruns it gets the same scores.

## 1. Size the sample to the cuts you will report
- First ask which cuts the study will report (by region, vertical, company size). Each reported cell needs enough companies to say anything; the user sets the minimum per cell.
- Build the sample so every reported cell meets that minimum. If a cell cannot, either merge it with a neighbour or report it as "base too low to report".
- `python3 scripts/benchmark_score.py ... --min-per-cut N` (use `python` where `python3` is not found, as on Windows) lists every cut below the minimum.

## 2. Fix the scoring method before scoring
- Each criterion is a yes or no question about something visible in public, with points the user sets. Example shape: "Does the company publish a security or trust page on its own site?"
- Write the criteria before the first company is looked at, and do not change them mid study. If they must change, rescore every company.
- No outside proprietary framework is used as the scoring method unless the user owns it and supplies it.

## 3. Score by script, the same way every run
- Evidence goes into a table: company, criterion, answer (yes, no, not found), source link, evidence tier, cut.
- `python3 scripts/benchmark_score.py --criteria criteria.csv --evidence evidence.csv` (use `python` where `python3` is not found, as on Windows) scores it. A yes without a public link scores zero. The output is sorted by score and name, so the same input always gives the same table. It reports points that are not a finite number, a criterion id used twice (the first row is kept, never replaced), and a run with no criteria or no evidence rows; `--json` prints strict JSON, with the tiers always in the order publishable, directional, anecdotal.
- Never estimate a score, never score from memory, and never score a company that was not looked up in this session.
- When every company, or every criterion inside a company, gets the same answer or the same score, say so before reporting: tied scores can mean the criteria do not tell the companies apart. Review the criteria with the user before publishing, and never draw a ranking, a "fix first" item or a strength from tied scores.

## 4. Verify every company by search
- Confirm each company exists under that name, its website is the right one, and it fits the sample's definition (region, vertical, size), with a link. A company that cannot be verified is dropped and listed as dropped.
- When a source the user called core cannot be reached, say so by URL and use only the fallbacks the user names; never drop it or swap in another site without the user's word.
- A confirmation or a "yes" that rests only on a search result (the page itself not opened) carries "from a search result, page not opened" in its source cell, is at most directional, and is never reported as a finding or counted as a second source (the claim ledger, references/claim-ledger.md).

## 5. Evidence tiers
| Tier | Meaning | How it is reported |
|---|---|---|
| Publishable | from a primary public source, reproducible by anyone, base large enough | reported as a finding |
| Directional | credible but partial: a small base, one source, or a cut below the minimum | reported only as "directional", with the reason |
| Anecdotal | a single observation or example | not reported as a finding; may illustrate a finding with its label |
The user may move items between tiers only with a stated reason; the asset prints the tier next to every finding. Synthetic respondent results (AI persona panels or other simulated respondents) are at most directional.

## 6. Publish the data without a gate
- The data table, the criteria and the method are published openly, with no email form or other gate.
- If the user wants a gated long form, warn once that the owner rule for this skill is ungated data; the data appendix stays open whatever is decided, and the decision is noted.

## 7. Lead with the thesis
- The study opens with what it found, in one sentence the data supports, then the method, then the table.
- It says plainly what it is not: not a ranking of quality, not advice, limited to what is public.
