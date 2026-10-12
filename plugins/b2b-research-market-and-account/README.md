# B2B Research: Market and Account

Four research skills for B2B teams who need numbers and account facts they can defend: product marketers, strategy leads, founders, CMOs, ABM and demand generation teams, SDR managers, content leads, and anyone who reviews drafts written with AI. Every skill keeps sourced facts apart from assumptions, says plainly what it could not check, and never fills a gap with an invented figure, quote or company. This version does not size markets or build TAM, SAM and SOM.

## Skills

**account-research** builds account lists that fit your ICP, audits and enriches lists in fixed fields, and writes a one account brief in TOPS order (technographics, organisation, person, situation) with a probe question for every finding. It uses your data connector first, then two to three web sources, returns verified and unverified lists, covers every account on your list, and stops when the source you named fails. The person block uses only the person's own public professional statements, each with link and date; personality notes are labelled as inferences from those statements, never facts; nothing on health, religion, politics, family, private life, home or personal contact details; for meeting preparation only.
Example prompt: "Brief me on this account before Thursday's call with their head of IT."

**evidence-research-asset** turns published reports and surveys into post series, briefs, reports and decks; runs benchmark studies with a fixed scoring method and scripted scoring; and drafts white paper outlines and case studies with placeholders where metrics and quotes are missing. Every number is checked against the publisher's own topline and locked across every asset by script. It also reviews a white paper in three lenses.
Example prompt: "Turn this threat report into a five post series and a one page brief for plant IT heads."

**claims-fact-check** builds a claims register for a post, deck, release or email, opens the source for every claim, fixes only what is wrong, and keeps each claim only as strong as its source. It maps claims to screenshots, checks every image for personal data, tests AI visibility claims only on the live engine, and checks every date's weekday.
Example prompt: "Fact check this post before I publish it."

**second-opinion-review** judges another model's or a colleague's critique point by point through three filters (facts, your stated objectives, tone), gives each point a verdict (accept, accept with edit, modify, deny), challenges your own view where the evidence says so, and ends with one final version.
Example prompt: "Another AI assistant reviewed my draft. Which of its points should I take? Give me the final text."

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
