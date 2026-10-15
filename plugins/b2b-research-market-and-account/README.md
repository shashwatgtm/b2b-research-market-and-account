# B2B Research: Market and Account

Four research skills for B2B teams who need numbers and account facts they can defend: product marketers, strategy leads, founders, CMOs, ABM and demand generation teams, SDR managers, content leads, and anyone who reviews drafts written with AI. Every skill keeps sourced facts apart from assumptions, says plainly what it could not check, and never fills a gap with an invented figure, quote or company. This version does not size markets or build TAM, SAM and SOM.

Version 1.0.5.

## Skills

**account-research** builds account lists that fit your ICP, audits and enriches lists in fixed fields, and writes a one account brief in TOPS order (technographics, organisation, person, situation) with a probe question for every finding. It uses your data connector first, then two to three web sources, returns verified and unverified lists, covers every account on your list, and stops when the source you named fails. The person block uses only the person's own public professional statements, each with link and date; personality notes are labelled as inferences from those statements, never facts; nothing on health, religion, politics, family, private life, home or personal contact details; for meeting preparation only.
Example prompt: "Brief me on this account before Thursday's call with their head of IT."

**evidence-research-asset** turns published reports and surveys into post series, briefs, reports and decks; runs benchmark studies with a fixed scoring method and scripted scoring; and drafts white paper outlines and case studies with placeholders where metrics and quotes are missing. Every number is checked against the publisher's own topline and locked across every asset by script. It also reviews a white paper in three lenses.
Example prompt: "Turn this threat report into a five post series and a one page brief for plant IT heads."

**claims-fact-check** builds a claims register for a post, deck, release or email, opens the source for every claim, fixes only what is wrong, and keeps each claim only as strong as its source. It maps claims to screenshots, checks every image for personal data, tests AI visibility claims only on the live engine, and checks every date's weekday.
Example prompt: "Fact check this post before I publish it."

**second-opinion-review** judges another model's or a colleague's critique point by point through three filters (facts, your stated objectives, tone), gives each point a verdict (accept, accept with edit, modify, deny), challenges your own view where the evidence says so, and ends with one final version.
Example prompt: "Another AI assistant reviewed my draft. Which of its points should I take? Give me the final text."

## What changed in 1.0.5

- Drafts, not frames. The claim ledger counts the [User to add: ...] slots in every deliverable and sends back one left mostly as slots, or held back until you reply: the parts you asked for are drafted from your words and the pages opened, marked "draft for you to confirm", and a slot is kept only for what no source gives (a name, a contact, a price, an approval). A figure inside a draft must come from your message, an opened page or a script.
- Page words, not the web tool's words. A quote from a fetched page must be the page's own words, not the web tool's comment about the page.
- A question that opens with a statement about you or a company has that statement checked, and a review point about a line that is not word for word in your text is answered on the closest line, quoted.
- Unchanged: the delivery check (the checked text is the reply, with the Stop hook in Claude Code) and the saved page text design of 1.0.4.
- The shipped plugin folder carries no test files; the tests of the scripts and of the hook are kept and run in the plugin's build files.

## What changed in 1.0.4

- Delivery from the checked text. The claim ledger's last run, `claim_ledger.py check ... --final`, is Claude's last step: it prints the verdict on its first line and, when the check passes, the answer between two lines carrying its digest. Claude's whole reply is exactly that text. In Claude Code, one hook (below) compares the final reply with it and sends Claude back when they differ.
- Saved page text. Claude saves the text of every page it opened in this session (as the web tool returned it) next to the ledger, and the check matches each figure, each quoted phrase and each "who said, reported or ran it" line against that text: a figure credited to the wrong speaker, a survey credited to someone the page does not name, or an absence claim for a word that is on the page now fails the check.
- A clause about a group of people (buyers, sellers, visitors, readers, a role) is its own ledger line, also inside a table row whose other cells come from a page; it is hedged or sourced.
- A lighter procedure: the check run with an empty ledger prints every line id with a skeleton to fill in.
- One hook, in Claude Code only: hooks/delivery_check.py runs when Claude is about to end a turn (a Stop hook). If one of these skills ran its claim ledger in that turn, it checks that the final reply is exactly the text the last `--final` run printed and that no file changed after that run, and otherwise sends Claude back with the reason, at most twice per turn. In any other turn it does nothing. It reads only the hook input and the session transcript on your computer, writes no file, reads no environment variable, uses no network and sends nothing. The Claude apps do not run plugin hooks; there the skills follow the same last step without the hook. Because the hook is a script inside a plugin that sits in a subfolder of its repository, a directory listing may be held for an Anthropic reviewer ("Scripts the validator couldn't follow"); that is a review step, not a block.

## What changed in 1.0.3

- Every skill now ends with a claim ledger before it answers: a new script, claim_ledger.py (standard library only), lists every line of the answer and of every saved file that states a fact about you, a named company, a person or a buyer, every figure and every "not on the site" claim. Claude gives each line its source (your own words, a page opened in this session, a script's printed output, the plugin's sector notes) or turns it into a label, a [User to add: ...] slot, a hedged line, or nothing, runs the check again until it passes, sends you exactly the checked text, and ends the answer with one line saying the claim ledger passed.
- Saved files keep every label the chat answer has ("[Draft for you to confirm: ...]", "as pasted, not yet checked", "from a search result, page not opened"); the check reports a saved file that drops one.
- A fact seen only in a search result is labelled "from a search result, page not opened" everywhere it appears, or left out, and is never counted as a second source.
- A claim that a site does not say something names only the pages checked for that word.
- No background fact about another company or body (what it sells, where it is based, a policy, a ticker, a listing, a customer, a headline) without a page opened in this session or the search label.
- Lines about you, your team, your product or your event keep your own words; anything that joins two of your facts or says more than you said is marked as a draft for you to confirm.
- Working files: the ledger keeps its notes in a claim-ledger folder in your working folder (the answer as checked, your message, the list of pages opened, the ledger). Nothing in it is sent anywhere; delete it whenever you like.

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

The skills run inside Claude. When web search or fetch is available, they open only the pages a job needs: company filings and results releases, company websites, published reports, regulator and statistics pages, and the help pages of platforms you publish on. About people they read only a person's own public professional statements, for meeting preparation; never private or leaked sources and never sensitive personal details. Four small Python scripts (standard library only), each, do the checks that must be exact: account_list_check.py checks list coverage and sources, number_lock.py and benchmark_score.py lock numbers across assets and score benchmarks the same way every run, and claims_scan.py lists claims and checks dates, weekdays and dashes. The scripts read only the files or text you give them, use no network, and write no files. A fifth script, claim_ledger.py (in each skill, with its own tests), checks the answer before you get it and, with --final, prints the checked reply; Claude itself writes the working notes it needs (the answer as checked, your message, the pages opened and their text, the ledger) into a claim-ledger folder in your working folder. One hook, hooks/delivery_check.py, runs in Claude Code only (the Claude apps do not run plugin hooks): when a turn ended after the claim ledger ran, it reads the hook input and the session transcript on your computer, compares the final reply with the checked text, writes no file, reads no environment variable and uses no network. Because it is a script inside a plugin that sits in a subfolder of its repository, a directory listing may be held for a reviewer. Nothing is published, scheduled or sent by these skills.

## Examples

The worked examples in each skill use real companies (Unicommerce, Quick Heal Technologies and its Seqrite division, and Zoho) only as examples, with every company fact quoted from a page fetched on 11 or 12 October 2026 and every figure a user supplies labelled hypothetical. No real employee of those companies is described, and every draft and critique in the examples is hypothetical.

## Privacy

This plugin sends no data to Helix GTM Consulting and runs no server. The plugin itself stores nothing: it keeps no account, no log and no copy of your work, and any file Claude writes for you goes only to your own working folder. About people, the skills read only a person's own public professional statements, each with link and date, for meeting preparation only; never health, religion, politics, family, private life, home or personal contact details. What you type into Claude is handled under your own Claude account terms. The claim ledger script, claim_ledger.py, reads the answer and the files Claude saved for you, uses no network and writes no files; Claude keeps its working notes (the answer as checked, your message, the pages opened, the ledger) in a claim-ledger folder in your working folder (1.0.4: with a pages folder holding the text of each page opened in the session, as the web tool returned it). The Stop hook (Claude Code only) reads the session transcript on your computer and writes nothing.

## Security

To report a security problem, email shashwat@gtmhelix.com with the subject "Security report: b2b-research-market-and-account". Please do not open a public issue for it.

## License

MIT. See LICENSE.
