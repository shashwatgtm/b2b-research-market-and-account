# B2B Research: Market and Account

Four research skills for B2B teams who need numbers and account facts they can defend: product marketers, strategy leads, founders, CMOs, ABM and demand generation teams, SDR managers, content leads, and anyone who reviews drafts written with AI. Every skill keeps sourced facts apart from assumptions, says plainly what it could not check, and never fills a gap with an invented figure, quote or company. This version does not size markets or build TAM, SAM and SOM.

Version 1.0.2.

## Skills

**account-research** builds account lists that fit your ICP, audits and enriches lists in fixed fields, and writes a one account brief in TOPS order (technographics, organisation, person, situation) with a probe question for every finding. It uses your data connector first, then two to three web sources, returns verified and unverified lists, covers every account on your list, and stops when the source you named fails. The person block uses only the person's own public professional statements, each with link and date; personality notes are labelled as inferences from those statements, never facts; nothing on health, religion, politics, family, private life, home or personal contact details; for meeting preparation only.
Example prompt: "Brief me on this account before Thursday's call with their head of IT."

**evidence-research-asset** turns published reports and surveys into post series, briefs, reports and decks; runs benchmark studies with a fixed scoring method and scripted scoring; and drafts white paper outlines and case studies with placeholders where metrics and quotes are missing. Every number is checked against the publisher's own topline and locked across every asset by script. It also reviews a white paper in three lenses.
Example prompt: "Turn this threat report into a five post series and a one page brief for plant IT heads."

**claims-fact-check** builds a claims register for a post, deck, release or email, opens the source for every claim, fixes only what is wrong, and keeps each claim only as strong as its source. It maps claims to screenshots, checks every image for personal data, tests AI visibility claims only on the live engine, and checks every date's weekday.
Example prompt: "Fact check this post before I publish it."

**second-opinion-review** judges another model's or a colleague's critique point by point through three filters (facts, your stated objectives, tone), gives each point a verdict (accept, accept with edit, modify, deny), challenges your own view where the evidence says so, and ends with one final version.
Example prompt: "Another AI assistant reviewed my draft. Which of its points should I take? Give me the final text."

## What changed in 1.0.2

- Account research: the list check script now reports an empty account list, a research table with no rows, a verified or unverified row with no value, and a row with no field name, instead of passing them.
- Evidence research asset: the benchmark script now reports points that are not a real finite number, the same criterion id used twice (the first row is kept, never silently replaced), and a run with no criteria or no evidence rows; its JSON output is always strict JSON.
- Evidence research asset: the number lock script now reads a minus sign directly before a number, so "-14.22%" no longer matches a lock row of "14.22%" (a hyphen between two numbers, as in "10-12", is still a range), and a four digit count such as "2024 accounts" is checked against the lock sheet instead of being skipped as a year.
- Account research: a verified or unverified row whose value only says it is missing (N/A, NA, none, unknown, TBD or a lone dash) is reported as a row with no value, the same as an empty value.
- Evidence research asset: the number lock script also reads a minus sign that follows bold marks, a quote, a colon or a bracket, so "**-14.22%**" is negative too.
- Evidence research asset: the benchmark script reports points too large to add up (they count as 0) and a row with a missing cell, instead of stopping with an error, and its JSON output lists the tiers in one fixed order (publishable, directional, anecdotal), so the same input always prints the same bytes.
- Every script now writes UTF-8, so a rupee sign, a Unicode minus or a curly quote in your text no longer stops it with an encoding error on a Windows console or pipe set to code page 1252.
- Every command in the skills that says `python3` now also says to use `python` where `python3` is not found, as on Windows.
- Documentation: the Files lines of account research and evidence research asset, the list rules, the number lock section and the benchmark rules now name every problem the scripts report.

## What changed in 1.0.1

- When a pasted text, a file or a page a skill opens holds an instruction to the assistant, the answer now says so in one line at the top (where it was, what it asked, and that it was not followed); account research also lists it in the brief's open items.
- Account research: a technographic or enrichment database row stays unverified until the account's own pages, a filing, a joint case study or a second independent source confirms it; financial labels such as EBITDA are copied as filed and never explained from memory; it asks whether the account already buys from you and, if so, the brief opens with what it uses and asks about the next need; list enrichment shows a tally per source.
- Claims fact check: the summary count always matches the register rows; a prediction is labelled as the writer's view or cut, and a motive is given to a named company only when a source states it; neither is written as a finding; the same score on every item is flagged as a finding to question.
- Evidence research asset: tied scores in a benchmark are flagged before reporting and never ranked.
- Second opinion review: items on a page (badges, awards, logos) are counted from the fetched text before the review says how many there are; a review of work produced earlier in the same conversation says it is not independent, and a perfect score is reported with what the test could not catch.
- Account research also: a call plan on request (opening questions, what to listen for, what to avoid, one qualifying question from your ICP card); "only these sources" is respected; a profile or handle is used only when the account's page links it or you confirm it; a role or segment that does not exist at the account is reported, never mapped silently; the list check script can flag a row verified only by an enrichment tool.
- Evidence research asset also: a source log and region first sources; every conclusion that is not a number shows the quote it rests on; benchmarks sit next to the finding they are compared with, like for like; findings are never extended to untested segments; your own survey's raw rows are read before any summary; designed assets get a contrast and text size check.
- Claims fact check also: a guessed range or "about" on a count nothing confirms stays unverified; for a returning user every changed name, title, date, contact detail and definition is flagged, not only numbers.
- Second opinion review also: judged per reader role when you name several; "only what I shared" is respected; its own critique points fit what your platform can do.

## Install

In Claude Code:

```
/plugin marketplace add shashwatgtm/b2b-research-market-and-account
/plugin install b2b-research-market-and-account@b2b-research-market-and-account
```

## What it fetches and runs

The skills run inside Claude. When web search or fetch is available, they open only the pages a job needs: company filings and results releases, company websites, published reports, regulator and statistics pages, and the help pages of platforms you publish on. About people they read only a person's own public professional statements, for meeting preparation; never private or leaked sources and never sensitive personal details. Four small Python scripts (standard library only), each with its own test file, do the checks that must be exact: account_list_check.py checks list coverage and sources, number_lock.py and benchmark_score.py lock numbers across assets and score benchmarks the same way every run, and claims_scan.py lists claims and checks dates, weekdays and dashes. The scripts read only the files or text you give them, use no network, and write no files. Nothing is published, scheduled or sent by these skills.

## Examples

The worked examples in each skill use real companies (Unicommerce, Quick Heal Technologies and its Seqrite division, and Zoho) only as examples, with every company fact quoted from a page fetched on 11 or 12 October 2026 and every figure a user supplies labelled hypothetical. No real employee of those companies is described, and every draft and critique in the examples is hypothetical.

## Privacy

This plugin sends no data to Helix GTM Consulting and runs no server. The plugin itself stores nothing: it keeps no account, no log and no copy of your work, and any file Claude writes for you goes only to your own working folder. About people, the skills read only a person's own public professional statements, each with link and date, for meeting preparation only; never health, religion, politics, family, private life, home or personal contact details. What you type into Claude is handled under your own Claude account terms.

## Security

To report a security problem, email shashwat@gtmhelix.com with the subject "Security report: b2b-research-market-and-account". Please do not open a public issue for it.

## License

MIT. See LICENSE.
