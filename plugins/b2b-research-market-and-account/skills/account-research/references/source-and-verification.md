# Sources, verification, the stop rule and privacy

## Source order (first is preferred)
1. The source the user named: their CRM or enrichment connector, their export file, an attendee list they own. It is used first. A source named for one field (for example "use screener for revenue") governs that field only, with the stop rule for that field (when it fails or has no value for an account, that field is not filled from another source without the user's word); the other fields follow this order and, when web tools are available, are searched on the web before any is left "not found". When the user limits the research to sources they name ("only these links", "only our export"), use only those: a field those sources do not state is "not found in your named sources", and verification on other sites runs only with the user's word; until then a field resting on one named source is "unverified (named source only)".
2. The account's own disclosures: annual report, exchange filings, results releases, investor presentations, earnings call transcripts, press releases, its website (product, integration, careers, leadership pages), and posts on the account's official company pages, each with its date and link, read on a page the user can open or through the user's connector; never collected by scraping against a platform's terms. The number of posts and whether they are required stay the user's choice.
3. Regulators and registries: company registry records, exchange pages, regulator lists.
4. Reputed business and trade publications that name their source.
5. Other public pages, only as leads to find a primary source, never as the source of a field.

## Banned sources
- Any source the user bans. Ask once at the start. A user may ban, for example, stock screener sites, SEO list pages or influencer posts.
- Pages that repeat figures without naming their source, and pages that say their content may be machine generated without naming a source.
- Search result snippets on their own as the source of a field. When a page cannot be opened, a snippet from a search for its wording may be shown in the notes, labelled "from a search result; the page itself was not opened"; the field stays as it was.
- Private or leaked sources about a person: private or closed groups, leaked documents, data broker files, scraped personal data, and non professional personal accounts. A person's own public posts on professional topics are allowed for the person block (tops-brief.md, P).
When a banned source was used, remove every field it filled, re-source from allowed sources, and say which cells are now empty.

## Verification order
1. The user's data connector first (CRM, enrichment tool), where one is available. The user's own CRM record of their own relationship with the account (customer status, contacts, activity) stands as the user's record ("verified", with the connector named in the verified_by column). A technographic or enrichment database row that says an account uses a product, or gives its size or revenue, is a lead: the field stays "unverified (one source: [tool])" until the account's own pages, a filing, a joint case study or a second independent source confirms it; then it is "verified", with the tool named in the verified_by column and the confirming source in the source column.
2. Then, for fields the connector did not confirm or where there is no connector: two to three web sources from different sites (when the user limited the research to sources they name, only with the user's word, as in source order 1), at least one of them the account's own disclosure where possible. Two sources from different sites that agree make the field "verified" (for example the account's own site and its filing on the exchange's site); the source column names both.
3. A field with one source is "unverified (one source)". A field with sources that disagree is "unverified (sources differ)", with both values shown.
4. A line the user pasted from the account's own page is re-checked before it is questioned (the same page asked for the exact sentence, its raw text where a tool allows, a search for the exact words); if still not found it is "as pasted, not yet checked" (a search result that shows the words is noted beside it, as in Banned sources, and does not change that). It is never called wrong or a correction: when an opened page states a different figure or fact for the same thing, both are shown side by side with source and date, as in Conflicts.
5. "Not found" when no allowed source opened in this session states the field; the notes name the pages opened and any search run, and the brief says "not found on the pages I opened", never that the account does not have it. Never "likely", never an inferred value.

## Two lists
Every delivery ends with two lists: verified fields and unverified fields, per account, on a best effort basis. scripts/account_list_check.py prints both and the coverage line.

## Source tally (list enrichment across many accounts)
For list enrichment across many accounts, keep a tally per source: the fields it gave, the fields a second source confirmed, the fields where it disagreed with another source, and the fields it could not give. Show the tally with the two lists so the user can decide whether to drop or replace a weak source. A source is dropped only on the user's word, and its fields are then sourced again.

## The stop rule
When the source the user named fails (a file that will not open or is garbled, a connector that errors, a page that will not load):
- stop work that depends on it;
- say which source failed, how (error text or what is unreadable), and what is affected;
- do not fill the rows from memory, from a guess, or from other sources without the user's word;
- ask for a readable copy or for permission to continue with web sources marked unverified.
If only part of a source fails (a connector errors on some accounts), continue with the rest, list the failed accounts, and ask how to treat them.

## Conflicts
- The account's own filing beats a secondary page. Show the other value and its label; do not call either wrong when the labels differ ("Revenue" against "revenue from operations").
- Never average and never choose the bigger number.

## Privacy and people
- The person block follows tops-brief.md, P: only the person's own public professional statements, each with link and date; personality notes labelled as inferences from those statements; for meeting preparation only.
- Personal contact data (email, phone) comes only from the user's own systems or connector, under the user's terms. Never guess an email from a pattern.
- Never: health, religion, politics, family, private life, home or personal contact details in a brief; nothing read from likes, follows, reactions or connections; a personality note never written as a fact.
- Contact data stays in the user's working files; it never goes into a shared example.
