# White paper review in three lenses

Use when the user asks for a review of a white paper, report or research asset written by them or someone else. The review checks the paper; it does not rewrite it unless asked.

## Lens 1: each statistic against what it measured
For every statistic in the paper:
- Open its source. Record what the source measured: region, sample (who and how many), buyer type (business or consumer, which roles), period, and the exact wording.
- Compare with the claim the paper makes. Typical mismatches: a consumer shopping survey used for B2B vendor research; a US or EU sample used for an APAC claim; a share of a subset written as a share of the whole; an old edition used as current; a vendor's own data presented as independent.
- Verdict per statistic: fits, fits with a wording fix, does not fit (replace or remove), source not found.
- If the user sets a recency or region rule (for example "nothing older than a set date, and relevant to Europe"), apply it and find a replacement data point that fits, with its link, or say none was found.

## Lens 2: the reader's job
- Name the reader and the job they hire the paper for (for example "defend a budget conversation").
- Check whether each section serves that job; mark sections that teach theory the reader did not ask for, and gaps where the reader's decision needs evidence the paper lacks.
- Check that the thesis is stated early and the recommendation follows from the evidence.

## Lens 3: the brand guidelines
- Use the user's guidelines if given (voice, terms, visual rules). If none are given, check only the short voice rules (voice-check-short.md) and say that brand guidelines were not supplied.

## Ordering the fixes: fastest credibility win first
1. Statistics that do not fit what they measured, or have no source (a reader who spots one stops trusting the rest).
2. Numbers that differ between sections or between the paper and its summary.
3. Missing sources and dates on figures that are right.
4. Gaps against the reader's job.
5. Voice and brand fixes.
Within each group, fixes on the first pages and in the executive summary come first.

## Output
- A table: rank, location, issue, lens, the source checked (link, page), the smallest fix.
- If the user asked for a number of fixes ("the 5 most important"), give exactly that many in the ranked order, then list the rest in one line each.
- Never say a statistic is verified unless its source was opened in this session.
