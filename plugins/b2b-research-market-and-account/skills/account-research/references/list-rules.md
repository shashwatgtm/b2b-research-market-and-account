# List building, list audit and enrichment

## The ICP card (ask, do not invent)
Before building or auditing a list, the skill needs the user's ideal customer profile. If the user has none, it helps them write one with this card. Every field is the user's answer; the skill does not fill them with guesses.

- Firmographics: industries (up to three), company size band (the user's measure: employees, revenue, orders, endpoints), revenue band if used, geography, technologies the account runs that matter to the offer.
- Buying group: the champion's title and what they are trying to get done; the economic buyer's title and concerns; the users' titles and needs. Titles only, no named people.
- Qualifying criteria: must haves (three), nice to haves (three), disqualifiers (three, for example B2C only, government or public sector, as the user decides).
- One line on what the user sells, in their own words (15 words or fewer).
- Example accounts: only accounts with a source per account that shows each one fits (its own page, filing or release, linked). An example account without a source is not listed.

## Building a list
1. Confirm the ICP card, the region and the vertical. Restrict the search to them.
2. Ask for named sources first (a connector, a directory the user trusts, a list of event attendees the user owns) and banned sources.
3. Tiers, if the user wants volume: a primary tier that meets every must have; a secondary tier "if and only if" the primary falls short of the user's target; a fallback only on the user's word. Each account carries its tier and the reason.
4. Each account row: name, website, the evidence that it fits (link and quote), region, status.
5. Complete or drop: if the list is defined by a period (for example companies funded in a year), either cover the whole period or say which part is covered.
6. One working file: keep adding to the same list; never restart a search from zero when a list already exists in the conversation.

## Auditing a list
For each account, check and report (never remove silently):
- Duplicate or alias (the same company under two names or legal suffixes). The script flags possible duplicates for a human to confirm.
- Fit against the must haves and disqualifiers, with the evidence.
- Still trading under that name (merged, acquired or renamed, from the account's own pages or filings).
- Region and vertical inside the user's restriction.
- Rows from banned sources.
Report: kept, removed (with reason), unsure (with what would settle it).

## Enrichment
- Fixed field blocks per account, agreed before starting. Typical blocks: firmographics, technographics, organisation, situation, and the people block only for the designations the user named. Do not enrich roles the user did not ask for.
- Same designations across every company; include partial information where that is all there is, marked partial.
- When the account's own pages or the evidence show that the role, team or segment the user asked about does not exist there, or sits under another title, say so in one line and name what was found, with its source. Never map it silently to the user's term.
- Work in batches of 3 to 5 accounts for long lists, with a running count ("12 of 40 covered"). Never stop at a subset and call it done.
- Every field has a value or "not found", a source, a status and a checked date.
- Raw data when the user asks for raw data: the fields, no commentary.
- Periods: when a field is periodic (results, headcount), state the period; use the latest published period, and a newer one only "if it has been published".

## Coverage rule
Every account on the user's list gets rows, including "not found" rows. Before saying the work is done, run scripts/account_list_check.py and show the coverage line; it also reports an empty list, a table with no rows, a verified or unverified row with no value (a value of N/A, NA, none, unknown, TBD or a lone dash counts as no value), and a row with no field name. If time or tools run out, say exactly which accounts are not covered yet. For enrichment across many accounts, show the source tally (source-and-verification.md) with the two lists.
