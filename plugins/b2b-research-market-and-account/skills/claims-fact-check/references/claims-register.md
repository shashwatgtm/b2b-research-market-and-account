# The claims register

## What counts as a claim
Every statement a reader could check: a number, money amount, percentage, date or weekday, a name or title, a quote, a superlative ("first", "only", "largest", "#1", "leading"), who built, owns, wrote or won something, a product fact (a feature, a limit, a price, a plan), a comparison, an attribution ("according to"), and any statement about what an AI engine says or recommends. scripts/claims_scan.py seeds the list; read the text as well, because a claim can sit in a sentence with no digit ("the company was acquired").

A prediction, a guess about why a named company or person acted, or a "could this be" question about them is not a fact, and it is never written as a finding. In the text a prediction or a "could this be" question is labelled as the writer's view, or cut; a motive is never given to a named company or person, even as the writer's view, without a source that states it. Each one gets a register row with the verdict "View, not a fact".

Every claim is checked. Not a sample, not "the main ones". If time forces a cut, the answer says exactly which claims were not checked.

## Columns
| Column | What goes in it |
|---|---|
| id | C1, C2, ... (from the scan, plus any added by reading) |
| Claim as written | the exact words from the text |
| Type | number, money, percentage, date, name, title, quote, superlative, product fact, comparison, AI visibility |
| Source named by the user | the source the user said to use, if any |
| Source checked | link (or file and page), and the date it was opened in this session |
| What the source says | a short exact quote, with its label, base and period |
| Verdict | see below |
| Strength | the source's standing for this claim: primary (filing, regulator, publisher's own report), the subject's own statement (the company says), secondary (coverage that names its source), weak (coverage with no named source) |
| Smallest fix | the least change that makes the claim true at the source's strength, or "none" |

## Verdicts
- Verified: a source opened in this session (a fetched page or a connector result) says exactly this, with the same label, base and period.
- As pasted, not yet checked: the only source is text, a quote or a file the user pasted or attached; the claim matches it, but no source was opened in this session. Never called verified; the row names the source to open and the fix keeps the claim at the strength of what was pasted.
- Corrected: the source says something different; the fix uses the source's figure and label.
- Weaker than written: the source supports a softer claim ("about 3 in 10" where the text says "1 in 3"; "the company describes itself as the largest" where the text says it is the largest).
- Unverified: no allowed source found, or only weak sources. The fix removes the claim, softens it to what can be shown, or marks it "[User to add: source]". Softening means writing what a source shows: a guessed range ("4 to 5", "7+", "about 10") put on a count that no source or record confirms is still unverified; remove it or write "[User to add: count and where it is recorded]".
- Contradicted: the source says the opposite.
- Source unavailable: the source the user named could not be opened or does not render the figure. The cell stays blank; nothing is filled from memory or another source without the user's word.
- Not checked: listed only when time or tools forced a cut, with the reason.
- View, not a fact: a prediction, a motive or a speculation; the fix labels it as the writer's view or cuts it, and a motive given to a named company or person stays out unless a source states it.

Never write "all verified", "100% verified", "0% hallucination", "all links working" or "I just checked" without the register rows to show it.

## Fix only what is wrong
- Change the fewest words. Keep the user's sentence, order, voice and formatting.
- Do not rewrite locked content (headlines, quotes the user approved, a design's fixed text) unless it is the wrong part.
- Do not remove or restructure the rest of the document. Return the corrected lines, or the full text with changes marked, as the user prefers.
- Carry every correction into the deliverable: the final text must contain the fixes, not just the register.

## After fixing
- Run the date and weekday check on the corrected text (scripts/claims_scan.py --year <current year>).
- For a returning user, compare with the earlier approved version: flag every number, name, title, date, contact detail and definition that changed, and every earlier fix that is missing.
- If the text has several assets (a post, a deck, a page), the same figure must be written the same way in each; list any asset that still differs.
- No headline or opening line may claim more than the corrected body supports.
- When a checked output gives the same score to every item, list it as a finding to question, not as a result.
- Any count the answer states (claims, rows, fixes) matches the register; when one sentence is split into several rows, say so.
