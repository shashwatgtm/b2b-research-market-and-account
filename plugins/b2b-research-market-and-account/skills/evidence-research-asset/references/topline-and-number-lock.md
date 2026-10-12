# Topline check and number lock

## 1. Before building: purpose, scope, boundary
Write these down first, from the user's words:
- Purpose: what the asset must do for its reader (for example "help plant IT heads decide what to check first").
- Channel and format: where it will be published (a newsletter tool, LinkedIn, a web page, a PDF, slides) and in what file format the user needs it.
- Reader: role and what they already know.
- Scope: the questions the asset answers, and what it leaves out.
- Source boundary: "only the attached documents", "the attached report plus web search", or "web search". Respect it exactly; anything outside it is marked "not in the agreed sources".
- Recency window: the period the user wants (for example "the last two quarters only").
- Treatment rules for edge cases, agreed before building: how to treat an unnamed client ("Unnamed client", never penalised, with no reason added unless the user gave one), a management disclosed figure with no reconciliation ("management disclosed, not reconciled"), a figure that appears in two editions.

## 2. The topline check
For every statistic the asset will use, open the publisher's own document (the report, the filing, the release, the survey's topline tables) and record:

| Field | What to record |
|---|---|
| Figure as published | exactly as written, with its unit ("265.52 million detections", "14.22%") |
| Label | what the publisher calls it (detections, not "attacks", if the publisher says detections) |
| Base | what the figure is out of (all detections, a sector subset, respondents, a region) |
| Period | the dates it covers |
| Sample | who or what was counted and how many (endpoints monitored, respondents, companies) |
| Region and buyer type | where, and whether business or consumer |
| Location | page or section in the publisher's document |

Rules:
- Secondary coverage (news articles, posts, summaries) never replaces the topline. When coverage and topline differ, the topline wins and the difference is noted.
- Do the arithmetic. If two published figures do not reconcile against the base the asset implies, say so: for example a sector count divided by the national total gives a different percentage from the one printed, which means the printed percentage uses another base. Never print a percentage against a base the publisher did not use.
- Never add or combine rows into a new headline the publisher did not print (summing two survey answers into one "net" figure is a new number; it needs the publisher's own net or it does not run).
- Keep the publisher's word: if they say "detections", the asset does not say "attacks".
- When the only copy of the publisher's document is one the user pasted or attached, record each figure as "as pasted, not yet checked" until the document is opened at its source in this session; never as verified.
- When the asset's story needs a figure the source does not have, change the story, not the figure.

## 3. The number lock sheet
One sheet per project, before any asset is written. Columns: id, label, value (exactly as every asset must write it), source (link and page), base, period, tier. A rounded form ("265 million") is allowed only as its own row, so every asset knows which form is approved.

Every asset (post, deck, page, PDF, newsletter, comment) uses only lock sheet numbers. When a number changes, it changes on the sheet first, then in every asset, and the check is run again.

## 4. The check
Run `python3 scripts/number_lock.py --lock lock.csv asset1.md asset2.md ...` on the text of every asset. It lists numbers that are not on the sheet, numbers that are near a locked value (a rounded or retyped form), and weekdays that do not match their dates. Fix each and run it again. If the script cannot run, compare by hand and say the check was manual.

## 5. Staged release
When timing matters (a holiday, a news cycle), release the evidence layer first (the data, its sources and method, ungated) and the polished asset later. The numbers stay locked across both.

## 6. Disclaimers and credits
- The asset names the publisher of every source it cites, inline, with the page.
- Research that is not advice says so ("Research only. Not investment advice." where money decisions are in play).
- The asset never implies the user produced research they only cite; it never puts words in a partner's or customer's mouth.
- An author line names the real author; no "first to quantify" or similar badge without a source showing it.
