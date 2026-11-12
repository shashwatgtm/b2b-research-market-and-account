# Benchmark score: the method

This file sets out one fixed calculation: the benchmark score of every company from a criteria table and an evidence table. Follow the rules exactly. When code execution is available, write your own calculation from these rules and run it; otherwise work it out by hand and say "counted by hand per the method". Either way the printed lines must match the shapes below character for character.

Nothing here is a benchmark of its own. The criteria and their points are the user's; the method only adds them up the same way on every run, so anyone who reruns it gets the same table.

## Inputs

| Input | Required | Meaning |
|---|---|---|
| criteria | yes | A CSV table with the columns criterion_id, question, points. Fixed before any company is scored. |
| evidence | yes | A CSV table with the columns company, criterion_id, answer, source, tier, and optionally cut. One row per company and criterion. |
| publishable only | no | When on, a yes counts only when its tier is publishable. Off unless the user asks. |
| minimum per cut | no | A whole number: the user's minimum number of companies per reported cut. 0 (the default) means no cut check. |
| JSON | no | Print the JSON form instead of the text form. |

Evidence columns:
- answer: yes, no or not found.
- source: the public link that shows the answer (needed for a yes).
- tier: publishable, directional or anecdotal (may be empty).
- cut: optional group the study will report (a region, a vertical, a size band).

### Reading the tables

- Both files are read as UTF-8 CSV with the first line as the header. Fields may be quoted with double quotes, so a quoted cell can hold a comma. Lines that are completely empty are skipped and are not counted as rows. A file that starts with a byte order mark keeps it as part of the first header name, so that column counts as missing.
- Header names must match exactly: lower case, no spaces around them. The criteria table needs criterion_id, question and points; the evidence table needs company, criterion_id, answer, source and tier (cut is optional; without it no row has a cut).
- A row with fewer cells than the header has the missing cells treated as empty.
- "Stripped" below means spaces, tabs and line breaks removed from both ends.
- Rows are numbered for messages from 2: the first data row of the evidence table is row 2, the next row 3, and so on (empty lines skipped are not counted).

## Refusals

Checked in this order; on the first one, print one line and nothing else, and the result code is 2.

| Case | Printed line |
|---|---|
| The criteria file cannot be opened | `Could not read: <the system's error text>`, for a missing file `Could not read: [Errno 2] No such file or directory: '<path>'` |
| The criteria header lacks columns | `Could not read: missing columns <names>` (the missing names in the order criterion_id, question, points, joined by ", ") |
| The evidence file cannot be opened | `Could not read: <the system's error text>` |
| The evidence header lacks columns | `Could not read: missing columns <names>` (in the order company, criterion_id, answer, source, tier, joined by ", ") |

Example: a criteria file with only `criterion_id,question` prints `Could not read: missing columns points`.

## Rules, in this order

Keep one list of problems, in the order they are found.

### 1. Empty tables

1. No criteria rows: add the problem `no criteria: fix the criteria before any company is scored`.
2. No evidence rows: add the problem `no evidence rows: nothing was scored`.

### 2. The points of each criterion

Go through the criteria rows in order. The id is the criterion_id cell, stripped (an empty id is a valid id, the empty text).

1. The id was already seen in an earlier row: add `criterion <id> appears twice in the criteria; the first row is kept, give each criterion its own id` and skip this row. The first row's points stay.
2. Read the points cell as a number the way Python's float() reads text: spaces at both ends are allowed; an optional + or - sign; digits with an optional decimal point (".5" and "2." are numbers); an optional exponent ("1e2" is 100); single underscores between digits are allowed ("1_000" is 1000); and the words inf, infinity and nan in any case, with an optional sign. Anything else, an empty cell included, is not a number.
3. Not a number: add `criterion <id>: points '<cell>' is not a number`, and the criterion counts as 0. The cell is printed exactly as written, spaces kept; an empty cell prints as ''.
4. A number that is not finite (inf, infinity or nan with any sign): add `criterion <id>: points '<cell>' is not a finite number; it counts as 0`, and the criterion counts as 0.
5. Negative points and 0 are accepted as written.

After all rows: add up the absolute values of all the points. If that sum is not finite (it overflows past the largest double, about 1.8e308), add `the points are too large to add up; use smaller points (every criterion counts as 0 until then)` and set every criterion's points to 0.

The criteria keep the order of their first appearance.

### 3. The evidence rows

Go through the evidence rows in order. For each row take: company (stripped), criterion id (stripped), answer (stripped, lower case), tier (stripped, lower case), source (stripped), cut (stripped; empty when the column is missing or the cell is empty).

1. The company gets an entry the first time it is seen, even when every one of its rows has a problem. Each entry starts with score 0, no criteria seen, and the tier counts publishable 0, directional 0, anecdotal 0. Company names are compared exactly as stripped, so "Zoho" and "zoho" are two companies.
2. If the cut is not empty, the company is added to that cut's set of companies (a company counts once per cut). This happens before any other check of the row, so rows with problems still count towards cuts.
3. The criterion id is not in the criteria: add `row <n> <company>: criterion <id> is not in the criteria` and go to the next row.
4. This company already has a row for this criterion: add `row <n> <company>: criterion <id> answered twice` and go to the next row. The first row stays.
5. Mark the criterion as seen for this company. (From here on the criterion is never "missing" for this company, even if the answer below is refused.)
6. The answer is not yes, no or not found: add `row <n> <company> / <id>: answer '<answer>'; use yes, no or not found` (the answer as lower cased and stripped) and go to the next row. No tier is counted.
7. Tier: if the tier is not empty and is not publishable, directional or anecdotal, add `row <n> <company> / <id>: tier '<tier>'; use publishable, directional or anecdotal`. Otherwise, if the tier is not empty, add 1 to that tier's count. The row goes on in both cases. Tiers are counted for every valid answer: yes, no and not found.
8. If the answer is yes:
   - The source does not start with `http://` or `https://` (exactly these lower case letters): add `row <n> <company> / <id>: yes without a public link scores 0` and go to the next row.
   - Publishable only is on and the tier is not publishable: the yes scores nothing, with no problem.
   - Otherwise add the criterion's points to the company's score.
9. No and not found score nothing.

### 4. The table

For each company in the order it was first seen:
- missing = the criteria ids this company has no seen row for, sorted by plain character order (so "Q10" comes before "Q2", and upper case before lower case).
- If missing is not empty, add `<company>: not fully scored, no row for <ids joined by ", ">`. These problems come in the order companies were first seen, not in table order.
- max = the sum of the points of all criteria (after the rules above), added with compensated summation (the Neumaier method, which is what Python 3.12 and later use for sum() over floats), so the rounding error of each addition is carried and put back at the end: 0.1, 0.2 and 0.3 give a max of 0.6, while a score built from the same three points one addition at a time is 0.6000000000000001. With no criteria at all, max is the whole number 0.

Then sort the table: highest score first; equal scores by company name compared in lower case (plain character order); names equal in lower case keep the order they were first seen.

### 5. Low cuts

Only when the minimum per cut is not 0. For each cut in plain character order of its name: if the number of companies in the cut is below the minimum, add a low cut line `<cut>: <count> companies, below the minimum of <minimum>; base too low to report this cut` ("companies" stays plural even for 1). A negative minimum never flags anything.

## Number writing

Scores are added as double precision floating point numbers, one plain addition at a time, in row order, starting from 0. Max is added in criteria order with compensated summation, as section 4 says.

In the text form, a number is written as Python's `%g` writes it: 6 significant digits, rounded half to even on the exact binary value; trailing zeros and a trailing point dropped; written with an exponent (`e+06`, `e-05`, always a sign and at least two exponent digits) when the exponent is below -4 or at least 6. Examples: 3 is `3`, 4.5 is `4.5`, 0.1 + 0.2 is `0.3`, 1234567 is `1.23457e+06`, 0.00001 is `1e-05`, -2 is `-2`, 0 is `0`.

In the JSON form, a score or a max that is a float is written as Python writes a float: the shortest digits that read back to the same value, always with a point or an exponent, so 3 is `3.0`, 4.5 is `4.5`, 0.1 + 0.2 is `0.30000000000000004`, 1e16 is `1e+16`. The max of a run with no criteria is the whole number `0`.

## Printed output (text)

Line by line:

| Line | Exact shape | When |
|---|---|---|
| First | `Scores (same input, same order, every run):` | Always. |
| One per company, in table order | `  <company>: <score> of <max>  [publishable <n>, directional <n>, anecdotal <n>]` followed by `  NOT FULLY SCORED` when the company has missing criteria | Always. Two spaces before the company; two spaces before the bracket; two spaces before NOT FULLY SCORED. |
| One per low cut | `Cut: <low cut line>` | In cut name order. |
| Problems | `Problems: <count>` then one line per problem, `  <problem>`, in the order found | When there is at least one problem. |
| No problems | `Problems: none` | When there are none. |

The result code is 0 when there are no problems and no low cuts, and 1 otherwise. A low cut alone makes the result 1 even when the last line says "Problems: none".

## Printed output (JSON, for API or programmatic use)

One object, indented by 2 spaces per level, every key and every list item on its own line, a space after each colon, an empty list written `[]`. Characters outside plain ASCII are written as `\u` escapes (for example `Caf\u00e9`). Key order:

- "table": a list with one object per company in table order, each with the keys "company", "score", "max", "missing" (the list of missing ids), "tiers" (an object with "publishable", "directional", "anecdotal", always in that order).
- "problems": the list of problem texts.
- "low_cuts": the list of low cut lines, without "Cut: ".

No NaN or Infinity can appear, because such points count as 0. The result code is as for the text form.

## Worked example

Criteria:

```
criterion_id,question,points
Q1,Publishes a security or trust page on its own site,2
Q2,Publishes pricing on its own site,1
Q3,Has a public status page,1.5
```

Evidence:

```
company,criterion_id,answer,source,tier,cut
Freshworks,Q1,yes,https://www.freshworks.com/security/,publishable,India
Freshworks,Q2,yes,https://www.freshworks.com/pricing/,publishable,India
Freshworks,Q3,no,,directional,India
Zoho,Q1,yes,https://www.zoho.com/security.html,publishable,India
Zoho,Q2,yes,https://www.zoho.com/crm/pricing.html,directional,India
Zoho,Q3,yes,https://status.zoho.com/,anecdotal,India
Postman,Q1,yes,,publishable,US
Postman,Q2,not found,,directional,US
Postman,Q3,yes,https://status.postman.com/,publishable,US
```

Working: max = 2 + 1 + 1.5 = 4.5. Zoho scores 2 + 1 + 1.5 = 4.5. Freshworks scores 2 + 1 = 3 (Q3 is no). Postman's Q1 yes has no link (row 8: the header is row 1, so Postman's Q1 row is row 8), so it scores 0 and is a problem; Q3 earns 1.5. Postman's Q1 tier still counts, so Postman has publishable 2.

Printed text, with a minimum per cut of 2:

```
Scores (same input, same order, every run):
  Zoho: 4.5 of 4.5  [publishable 1, directional 1, anecdotal 1]
  Freshworks: 3 of 4.5  [publishable 2, directional 1, anecdotal 0]
  Postman: 1.5 of 4.5  [publishable 2, directional 1, anecdotal 0]
Cut: US: 1 companies, below the minimum of 2; base too low to report this cut
Problems: 1
  row 8 Postman / Q1: yes without a public link scores 0
```

Result code 1. With publishable only on, Zoho's Q2 (directional) and Q3 (anecdotal) yes rows score nothing, so Zoho scores 2 and the order becomes Freshworks 3, Zoho 2, Postman 1.5.

The same run (no minimum per cut) in JSON starts:

```
{
  "table": [
    {
      "company": "Zoho",
      "score": 4.5,
      "max": 4.5,
      "missing": [],
      "tiers": {
        "publishable": 1,
        "directional": 1,
        "anecdotal": 1
      }
    },
    {
      "company": "Freshworks",
      "score": 3.0,
```

and ends:

```
  "problems": [
    "row 8 Postman / Q1: yes without a public link scores 0"
  ],
  "low_cuts": []
}
```

### Further checked cases

| Input | Printed result |
|---|---|
| Points Q1 `two`, Q2 empty, Q3 `nan` | Problems `criterion Q1: points 'two' is not a number`, `criterion Q2: points '' is not a number`, `criterion Q3: points 'nan' is not a finite number; it counts as 0`; every score `0 of 0`. |
| Points Q1 `1e308`, Q2 `1e308`, Q3 `1` | `the points are too large to add up; use smaller points (every criterion counts as 0 until then)`; every company `0 of 0`. |
| Points Q1 `1234567`, Q2 `0.00001`, Q3 `3` | `Zoho: 1.23457e+06 of 1.23457e+06` |
| Points ` 2 `, `1_000`, `+3` | read as 2, 1000 and 3: `Zoho: 1005 of 1005` |
| Companies Zeta, zeta, Alpha, alpha all scoring 0 | Table order Alpha, alpha, Zeta, zeta; the "not fully scored" problems in first seen order Zeta, zeta, Alpha, alpha. |
| Evidence row `Zoho,Q2` with the other cells missing | `row 3 Zoho / Q2: answer ''; use yes, no or not found` (row 3 if it is the second data row) |

## Results in short

| Result | Meaning |
|---|---|
| a "Could not read: " line | A file was missing, unreadable or lacked columns; pass the line on and ask the user for the file. |
| `Problems: none` and no Cut lines | Every company is fully scored with no problem. |
| Problems or Cut lines | Fix every problem (or report each low cut as "base too low to report") and score again. Never report a score from a run with problems as final. |
