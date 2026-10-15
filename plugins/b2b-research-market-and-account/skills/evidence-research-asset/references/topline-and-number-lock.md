# Topline check and number lock

## 1. Before building: purpose, scope, boundary
Write these down first, from the user's words:
- Purpose: what the asset must do for its reader (for example "help plant IT heads decide what to check first").
- Channel and format: where it will be published (a newsletter tool, LinkedIn, a web page, a PDF, slides) and in what file format the user needs it.
- Reader: role and what they already know.
- Scope: the questions the asset answers, and what it leaves out.
- Source boundary: "only the attached documents", "the attached report plus web search", or "web search". Respect it exactly; anything outside it is marked "not in the agreed sources".
- Source log: when the user names the sources, write one line per source: what the asset uses from it, what it skips, and why. Show it in the scope block.
- Region of sources: when the asset or study has a region, look first for publications, trade press and data published in or about that region; do not default to a US or global list. Record the region of each source.
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
- Benchmarks beside the subject's own findings: when an asset sets published benchmarks beside a company's own figures or findings, put each benchmark next to the finding it is compared with, check that both use the same definition, period and segment (like for like), and say in one line what the comparison means for the reader. A benchmark that no finding uses is cut. Never deliver a benchmark section that the analysis does not refer to.

## 2a. The user's own survey or study data, when an asset is built from it
When the user has the raw response file of a survey or study they ran and wants an asset from it, read every row of it. The tool's or vendor's summary report is coverage: check it against the raw rows and never use it in place of them. Re-derive every segment result from the rows, with the base of each segment next to it; a segment that comes first only because it has more respondents is reported with its base, not as the winner. Here the raw rows are the source: each result derived from them goes on the lock sheet with its base and how it was counted (the file and the rows), and the summary report's figures do not; for a published report, the section 2 rules and the rule against printing a number the publisher did not print still stand. A finding holds only for the segments, regions and base the study covered. Results from AI persona panels or other simulated respondents are labelled as such and are at most directional; their quotes are never presented as quotes from real buyers. (Designing a questionnaire or a study is not a job of this skill.)

## 2b. Findings without numbers
Every conclusion that is not a number (a theme, a pattern, a reading of how a company positions itself or what its customers value) shows the passages it rests on: a short exact quote, where it was found and the date. A conclusion with no quoted evidence is cut, or labelled as the writer's view. Use the material already collected before looking for more.

## 3. The number lock sheet
One sheet per project, before any asset is written. Columns: id, label, value (exactly as every asset must write it), source (link and page), base, period, tier. A rounded form ("265 million") is allowed only as its own row, so every asset knows which form is approved.

Every asset (post, deck, page, PDF, newsletter, comment) uses only lock sheet numbers. When a number changes, it changes on the sheet first, then in every asset, and the check is run again.

## 4. The check
Run `python3 scripts/number_lock.py --lock lock.csv asset1.md asset2.md ...` (use `python` where `python3` is not found, as on Windows) on the text of every asset. It lists numbers that are not on the sheet, numbers that are near a locked value (a rounded or retyped form), and weekdays that do not match their dates. A minus sign directly before a number makes it negative ("-14.22%" is not the lock row "14.22%"; a hyphen between two numbers, "10-12", is a range), and a four digit count ("2024 accounts") is checked like any number, not skipped as a year. Fix each and run it again. If the script cannot run, compare by hand and say the check was manual.

## 5. Staged release
When timing matters (a holiday, a news cycle), release the evidence layer first (the data, its sources and method, ungated) and the polished asset later. The numbers stay locked across both.

## 6. Disclaimers and credits
- The asset names the publisher of every source it cites, inline, with the page.
- Research that is not advice says so ("Research only. Not investment advice." where money decisions are in play).
- The asset never implies the user produced research they only cite; it never puts words in a partner's or customer's mouth.
- When an asset builds on another publisher's research, ask the user's stance on it (agree, agree with a qualification, disagree). Keep the source's findings at their own strength and mark the user's added view as the user's view, never as a finding of the source.
- An author line names the real author; no "first to quantify" or similar badge without a source showing it.
