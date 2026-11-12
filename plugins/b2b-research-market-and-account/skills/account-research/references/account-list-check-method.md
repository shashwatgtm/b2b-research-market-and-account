# Account list check: the method

This file sets out one fixed check of account research: coverage of the user's list, possible duplicates, status, value and source on every row, the verification rule, banned sources, and the verified and unverified lists. Follow the rules exactly. When code execution is available, write your own check from these rules and run it; otherwise work it out by hand and say "counted by hand per the method". Either way the printed lines must match the shapes below character for character.

## Inputs

| Input | Required | Meaning |
|---|---|---|
| list | yes | The user's account list: a text with one account per line, or a CSV with an "account" column. |
| research | yes | The research table, a CSV with the columns account, field, value, source, status, verified_by, checked_on (more columns are allowed and ignored). |
| ban | no | Domains the user banned, comma separated (for example "screener.in"). Default none. |
| minimum web sources | no | A whole number, default 2: web sources from different domains needed to call a row verified without a connector. |
| enrichment | no | Names of enrichment or technographic tools, comma separated (for example "ToolA,ToolB"). A row verified by one of them must also carry a web source that is not on the tool's own site. Default none. |
| JSON | no | Print the JSON form instead of the text form. |

Research table cells:
- status: verified, unverified or not found.
- source: one or more public links separated by " | " or ";", or the user's file and row ("file: crm-export.csv row 12").
- verified_by: the connector that verified the row (the user's CRM for the user's own records, or an enrichment tool whose row a second source in the source column confirms), or empty when verified on the web.

Both inputs are read as UTF-8; line endings \r\n and \r are read as \n. "Stripped" below means white space removed from both ends.

## Refusals

On the first one, print one line and nothing else; the result code is 2.

| Case | Printed line |
|---|---|
| The list or the research file cannot be opened or is not UTF-8 (the list is read first) | `Could not read a file: <the system's error text>. Stop and ask the user for a readable copy; do not fill rows from memory.` For a missing file the error text is `[Errno 2] No such file or directory: '<path>'`. |
| The research header lacks columns | `Could not read the research table: missing columns <names>` (missing names in the order account, field, value, source, status, verified_by, checked_on, joined by ", "; header names must match exactly, lower case) |

## Reading the list

1. Take the non blank lines of the list (a line is blank when it holds only white space).
2. Read the first non blank line as one CSV line. If one of its cells, stripped and in lower case, is "account", the list is a CSV: read the whole text as a CSV table with that header (quoted cells allowed, completely empty lines skipped); the account column is the first header whose stripped, lower case name is "account"; the accounts are that column's cells, stripped, keeping only the non empty ones.
3. Otherwise every non blank line, stripped, is one account (commas included). Note that a plain list whose first line is the word "Account" is read as a CSV with that header.

The accounts keep their list order and duplicates.

## Reading the research table

A CSV table with the first line as the header; quoted cells may hold commas; completely empty lines are skipped. A row with fewer cells than the header has the missing cells empty. Rows are numbered from 2: the first data row is row 2 (skipped empty lines are not counted).

## The name key

Two names are the same account when their keys are equal. The key of a name:
1. Lower case it.
2. Replace every run of characters that are not a to z, 0 to 9 or a space with one space (accented and other non ASCII letters are replaced too).
3. Split into words at white space.
4. While the last word is one of: limited, ltd, pvt, private, inc, incorporated, llc, llp, corp, corporation, plc, co, company, gmbh, sa, ag, bv, technologies, technology, solutions, systems, software, esolutions, group, holdings, the; remove it.
5. While the first word is "the", remove it.
6. Join the remaining words with single spaces. The key can be empty (for "Ltd" or "The Group").

So "Freshworks Inc.", "Freshworks" and "The Freshworks Group" all have the key "freshworks", and "Postman, Inc" has the key "postman".

## Domains in a source

Split the source cell at every "|" or ";" (with any white space around it). Strip each part.
- Web sources (links): a part that starts with `http://` or `https://` (exactly these lower case letters). Its host: the text after "//" up to the first "/", "?" or "#"; anything up to and including the last "@" removed; a ":port" removed; lower cased; then a leading "www." removed once. An empty host counts as the empty domain.
- Bare site names (used for the banned check only): a part that does not start with http:// or https:// and matches, ignoring case, `^(?:www\.)?([a-z0-9-]+(?:\.[a-z0-9-]+)+)(?:/\S*)?$`: an optional "www.", then a host of letters, digits and hyphens with at least one point, then optionally "/" and a path with no spaces. Its host is the captured part in lower case. "screener.in/company/x" gives "screener.in"; "file: crm-export.csv row 12" gives nothing.

"All hosts" of a row = the link hosts in order, then the bare site names in order.

## Rules, in this order

Keep one list of problems, in the order found.

### 1. The list

1. Go through the accounts in list order with their keys. The first account with a key is that key's name. Each later account with a key already seen gives the problem `possible duplicate on the list: '<first name>' and '<this name>' (check by hand)`.
2. No accounts at all: `the account list is empty: add the accounts to research before calling the list done`.
3. No research rows at all: `the research table has no rows: every account needs at least one row, a not found row included`.

### 2. Each research row, in order

Take: account (stripped), its key, status (stripped, lower case), source (stripped), value (stripped), field (stripped; written "(no field)" in messages when empty), verified_by (stripped). Every row is "covered" under its key, whatever its problems. A row whose key is not a key from the list is an extra row: its stripped account name is kept as an extra name.

Then, in this order (several can apply to one row):
1. The field is empty: `row <n> <account>: has no field name; name the field the value answers`.
2. The status is not verified, unverified or not found: `row <n> <account> / <field>: status '<status>'; use verified, unverified or not found` (the status as stripped and lower cased, so an empty one prints '').
3. Status not found and the value is not empty: `row <n> <account> / <field>: marked not found but has a value`.
4. Status verified or unverified and the value is empty: `row <n> <account> / <field>: <status> row has no value; give the value or mark it not found`. Otherwise, status verified or unverified and the value in lower case is one of n/a, na, none, unknown, tbd, a lone hyphen, a lone U+2013 or a lone U+2014: `row <n> <account> / <field>: <status> row has no value ('<value>' counts as empty); give the value or mark it not found` (the value as stripped, original case).
5. Status verified or unverified and the source is empty: `row <n> <account> / <field>: has no source`.
6. Banned: for each host in all hosts of the row, in order, and for each banned domain in the order given, if the host equals the banned domain or ends with "." followed by it: `row <n> <account> / <field>: uses banned source <host>`. The banned domains are the ban input split at commas, each stripped, lower cased, leading points removed, empty ones dropped. One row can give the same line twice (two parts on the same banned site).
7. Status verified:
   - verified_by is empty and the number of different link hosts is below the minimum web sources: `row <n> <account> / <field>: verified needs a connector or <minimum> web sources from different domains (has <number of different link hosts>)`. Bare site names do not count.
   - verified_by, in lower case, equals one of the enrichment names (the enrichment input split at commas, each stripped and lower cased, empty ones dropped), and no link host is independent: `row <n> <account> / <field>: verified by an enrichment tool (<verified_by>) needs a second source in the source column (the account's own page, a filing, a joint case study or another independent source; a page on the tool's own site does not count)`. The tool key is verified_by in lower case with everything but a to z and 0 to 9 removed; a link host is independent when the tool key is empty or the tool key does not appear inside the host with everything but a to z and 0 to 9 removed (so for "ZoomInfo", "zoominfo.com" is not independent and "whatfix.com" is).

### 3. After the rows

1. Each account on the list (in list order, duplicates included) whose key has no row: `not covered: <account> has no rows`.
2. Each distinct extra name, in plain character order: `row for an account not on the list: <name>`. Different spellings of one key give separate lines.

### 4. The two lists

Go through the covered keys in the order of their first row. The name shown for a key is the list name for that key; for an extra key it is the account cell of its first row exactly as written in the file (not stripped). For each row of that key, in row order, add the entry `<field> (<status>)` to the verified list when the status is verified and to the unverified list otherwise (unverified, not found and every invalid status). Here field is the stripped field (empty stays empty, so the entry starts with a space) and status is the stripped, lower cased status, or "no status" when empty.

### 5. The counts

- names on the list: the number of accounts, duplicates included.
- unique accounts: the number of distinct keys on the list.
- covered: the number of distinct list keys that have at least one row.

## Printed output (text)

Line by line:

| Line | Exact shape |
|---|---|
| 1 | `Coverage: <covered> of <unique accounts> unique accounts have rows (<names on the list> names on the list)` |
| | `Verified list:` |
| per account in the verified list, names in plain character order | `  <name>: <entries joined by "; ">`, or `  (none)` when the list is empty |
| | `Unverified list:` |
| per account in the unverified list, names in plain character order | `  <name>: <entries joined by "; ">`, or `  (none)` |
| problems | `Problems: <count>` then one line per problem, `  <problem>`, in the order found; or `Problems: none` |

The words stay as shown for any count ("1 names", "1 unique accounts"). The result code is 1 when there is at least one problem and 0 otherwise.

## Printed output (JSON, for API or programmatic use)

One object, indented by 2 spaces per level, every key and every list item on its own line, a space after each colon, an empty list written `[]` and an empty object `{}`. Characters outside plain ASCII are written as `\u` escapes (for example `Caf\u00e9`). Keys, in order: "accounts_on_list", "unique_accounts", "covered", "missing" (the list accounts with no rows, in list order), "problems", "lists" (an object with "verified" then "unverified", each an object from name to its list of entries; in JSON the names keep the order of the covered keys, not sorted). The result code is as for the text form.

## Worked example

List: Zoho, Quick Heal Technologies, Unicommerce, Zoho Corporation (one per line). Ban: screener.in. Research table (sources shortened here; in the run they were full links on businesswire.com, unicommerce.com and business-standard.com):

| row | account | field | value | source | status |
|---|---|---|---|---|---|
| 2 | Zoho | HQ | Austin, Texas; Chennai, India | one businesswire.com link | unverified |
| 3 | Zoho | Customers | 700,000+ | the same link | unverified |
| 4, 5 | Zoho | Latest revenue, ERP in use | | | not found |
| 6 to 9 | Quick Heal Technologies | HQ, Customers, Latest revenue, ERP in use | | | not found |
| 10 | Unicommerce | HQ | | | not found |
| 11 | Unicommerce | Customers | 8,000+ | https://unicommerce.com/ \| a business-standard.com link | verified |
| 12 | Unicommerce | Latest revenue | Rs 51.4 Cr | a unicommerce.com link | unverified |
| 13 | Unicommerce | ERP in use | | | not found |

Working: "Zoho" and "Zoho Corporation" share the key "zoho", so there are 3 unique accounts and a possible duplicate; all 3 keys have rows; row 11 is verified with two different link hosts; no host is on screener.in.

Printed text:

```
Coverage: 3 of 3 unique accounts have rows (4 names on the list)
Verified list:
  Unicommerce: Customers (verified)
Unverified list:
  Quick Heal Technologies: HQ (not found); Customers (not found); Latest revenue (not found); ERP in use (not found)
  Unicommerce: HQ (not found); Latest revenue (unverified); ERP in use (not found)
  Zoho: HQ (unverified); Customers (unverified); Latest revenue (not found); ERP in use (not found)
Problems: 1
  possible duplicate on the list: 'Zoho' and 'Zoho Corporation' (check by hand)
```

Result code 1.

### Further checked cases

| Input | Printed problem lines |
|---|---|
| Row `Razorpay,HQ,N/A,https://razorpay.com/about/,unverified,,...` as row 2 | `row 2 Razorpay / HQ: unverified row has no value ('N/A' counts as empty); give the value or mark it not found` |
| Row 9 `CleverTap,HQ,,https://clevertap.com/about-us/,verified,,...` | `row 9 CleverTap / HQ: verified row has no value; give the value or mark it not found` and `row 9 CleverTap / HQ: verified needs a connector or 2 web sources from different domains (has 1)` |
| Row 12 with an empty field | `row 12 CleverTap: has no field name; name the field the value answers` |
| Row 15 with an empty status | `row 15 CleverTap / CRM: status ''; use verified, unverified or not found`; the unverified list shows `CRM (no status)` |
| Enrichment "ZoomInfo, BuiltWith"; row 3 `Whatfix,Tech stack 2,Snowflake,https://www.zoominfo.com/c/whatfix/123,verified,ZoomInfo,...` | `row 3 Whatfix / Tech stack 2: verified by an enrichment tool (ZoomInfo) needs a second source in the source column (the account's own page, a filing, a joint case study or another independent source; a page on the tool's own site does not count)` |
| Ban "screener.in"; row 15 source `screener.in/company/UNIECOM/ ; www.Screener.in/x` | `row 15 Unicommerce / Revenue FY24: uses banned source screener.in`, twice |
| Ban "exotel.in"; source `https://exotel.com:443/a \| https://user@www.exotel.in/b` | `uses banned source exotel.in` |
| Source `HTTPS://exotel.com/ \| exotel.com`, verified, no connector | `verified needs a connector or 2 web sources from different domains (has 0)` (upper case HTTPS is not a link) |
| List `Hasura`, `Exotel`; rows for Hasura, Kissflow, Sprinklr and ` Kissflow Inc ` | `not covered: Exotel has no rows`, then `row for an account not on the list: Kissflow`, `... Kissflow Inc`, `... Sprinklr`; the unverified list shows `Kissflow: HQ (unverified); CEO (unverified)` |
| Empty list and a table with only the header | `the account list is empty: ...` and `the research table has no rows: ...`; coverage `0 of 0 unique accounts have rows (0 names on the list)`, both lists `(none)` |

## Results in short

| Result | Meaning |
|---|---|
| a "Could not read" line | A file is missing, unreadable or lacks columns; ask the user for a readable copy and do not fill rows from memory. |
| `Problems: none` | Every account is covered and every row passes. |
| problems listed | Fix every one and check again; list any account not yet covered. |
