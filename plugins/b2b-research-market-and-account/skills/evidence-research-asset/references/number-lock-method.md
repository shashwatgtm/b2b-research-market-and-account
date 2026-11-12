# Number lock check: the method

This file sets out one fixed check: every number in every asset against the number lock sheet, plus the weekday written next to each date. Follow the rules exactly. When code execution is available, write your own check from these rules and run it; otherwise work it out by hand and say "counted by hand per the method". Either way the printed lines must match the shapes below character for character.

The check matches values and units, never bases: whether a matched number describes the right thing stays with the topline check (references/topline-and-number-lock.md).

## Inputs

| Input | Required | Meaning |
|---|---|---|
| lock | yes | The number lock sheet: a CSV table with the columns id, label, value, source. The value is written as every asset must write it, for example "265.52 million", "14.22%", "Rs 51.4 crore", "8 million", "2,024 accounts". |
| assets | yes | One or more asset texts (the post, the deck text, the page, the PDF text), each with its name. The name printed is the name exactly as given (for a file, the path as the user gave it). |
| allow small | no | A whole number, default 0. Plain whole numbers from 0 up to this number are skipped (for structure such as "Part 2 of 5"). |
| JSON | no | Print the JSON form instead of the text form. |

Files are read as UTF-8. Line endings \r\n and \r are read as \n. In the lock sheet, the first line is the header, fields may be quoted with double quotes (so "2,024 accounts" must be quoted), and empty lines are skipped. Header names must match exactly (lower case).

## Refusals

Checked in this order: the lock sheet first, then each asset in the order given. On the first one, print one line and nothing else; the result code is 2.

| Case | Printed line |
|---|---|
| A file cannot be opened | `Could not read: <the system's error text>`, for a missing file `Could not read: [Errno 2] No such file or directory: '<path>'` |
| The lock header lacks columns | `Could not read: lock sheet is missing columns <names>` (missing names in the order id, label, value, source, joined by ", ") |
| A lock row's value holds no number | `Could not read: lock row <id> has no number in value '<value>'` (id and value exactly as in the cells, spaces kept) |

## The number pattern

A number in a text, and the number in a lock value, is found with this regular expression (Python syntax, case insensitive, `\w` and `\s` in their Unicode sense):

`(?<![\w.])(?P<cur>[₹$€£]|rs\.?\s?|inr\s?|usd\s?)?(?P<num>\d(?:[\d,]*\d)?(?:\.\d+)?)(?:\s?(?P<unit>%|percent|per cent|million|billion|crore|lakhs?|thousand|mn|bn|cr|k|m|b|x)(?![a-z]))?`

In plain words, matches are found left to right, never overlapping:
- An optional currency: a rupee, dollar, euro or pound sign directly before the digits (no space allowed after a sign), or "Rs" (optionally "Rs.") or "INR" or "USD", each optionally followed by one white space character. Any case.
- The match must not start right after a letter, a digit, an underscore or a point. So "v2.0", "x5", "Q3" and ".5" hold no number, and in "1.5.3" only "1.5" is a number. When a currency word would be glued to a word before it, the currency is not taken but the digits can still match on their own: in "US$8 million" the number is "8 million" with no currency.
- The digits: a digit, then optionally digits and commas ending in a digit, then optionally a point and digits. "1,000,000" and "1,2,3" are single numbers; in "5," the number is "5".
- An optional unit after at most one white space character: %, percent, per cent (one space), million, billion, crore, lakh, lakhs, thousand, mn, bn, cr, k, m, b, x, not followed by a letter. So "8M" and "8 m" are 8 million, "3 x" is 3x, but in "5 bananas", "5 more" and "5 billionaires" there is no unit.

Each match gives:
- value: the digits with commas removed, read as a decimal number (double precision).
- sign: the value is negative when the character just before the match (before the currency, if there is one) is the Unicode minus sign U+2212, or is a plain hyphen U+002D that is either the very first character of the text or follows a character that is not a letter, not a digit, not % and not a point. So "-14.22%" at the start of a text, "**-14.22%**", ":-14.22%", "(-14.22%)" and " -5" are negative, while "10-12", "12%-14%", "a-5" and "1-5" are ranges or words, not signs. "-0" gives minus zero, which equals zero everywhere below.
- unit: the unit in lower case, mapped: % percent "per cent" to `%`; million mn m to `million`; billion bn b to `billion`; crore cr to `crore`; lakh lakhs to `lakh`; thousand k to `thousand`; x to `x`; no unit to empty.
- currency: the currency text with spaces removed at both ends, in lower case, a final point removed, then mapped: ₹ and rs to `inr`; $ to `usd`; € to `eur`; £ to `gbp`; inr stays `inr`, usd stays `usd`; no currency is empty.
- written form: the matched text with white space removed at both ends; when the value is below zero, the character before the match (the minus) is put in front. (Minus zero is not below zero, so "-0%" is written "0%".)

## Reading the lock sheet

For each lock row in order: take the first number in the value cell (by the pattern above, with the sign rule applied inside the value text). If there is none, refuse (see above). Keep: id (stripped), label (stripped), value (stripped), the number's value, unit and currency, and the lock word: the first run of letters after the number match, after optional white space (lower case), or empty. For "2,024 accounts" the lock word is "accounts"; for "8 million" it is empty because "million" is the unit; for "Rs 51.4 crore" it is empty.

## Dates

Spans that are dates (found with these patterns, case insensitive, all four used):

| Name | Pattern |
|---|---|
| day month year | `\b(?P<day>\d{1,2})(?:st\|nd\|rd\|th)?\s+MON\.?,?\s+(?P<year>\d{4})\b` |
| month day year | `\bMON\.?\s+(?P<day>\d{1,2})(?:st\|nd\|rd\|th)?,?\s+(?P<year>\d{4})\b` |
| ISO | `\b\d{4}-\d{2}-\d{2}\b` |
| month year | `\bMON\.?\s+(?P<year>\d{4})\b` |

where MON is `(?P<mon>jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)`. (In the table, `\|` stands for the alternation bar.)

## Rules for each asset, in this order

Go through the numbers in the asset text left to right. For each number (value v, unit u, currency c, written form w):

1. Inside a date: if the start of the match (the currency, if any) lies inside any date span (at or after the span's start and before its end), skip it.
2. A year: if u is empty, v is a whole number from 1900 to 2099, and the digits have no comma, the number is a year and is skipped, unless it is a count. It is a count when some lock row with an empty unit has the value v, or when the first run of letters after the match (after optional white space) equals, in lower case, the non empty lock word of some lock row with an empty unit. So "2024 accounts" is checked against a lock row "2,024 accounts", "2023" next to no such row is skipped, and "1999.0" is a year too.
3. Small: if u and c are both empty, v is a whole number, and 0 <= v <= allow small, skip it. With the default 0, a plain "0" (and "0.0") is always skipped. A negative allow small skips nothing.
4. Exact: the lock rows whose value equals v and whose unit equals u, in sheet order.
   - If c is not empty and some of those rows have a non empty currency different from c, take the first such row: a near match, shown as that row's value followed by " (the currency differs)". Go to the next number.
   - Otherwise, if there is any exact row, take the first: a match `(w, id)`. Go to the next number. (A lock row without a currency matches any currency in the text: lock "2.5 billion" matches "$2.5 billion".)
5. Close: the lock rows with the same unit u and a non zero value L such that |v - L| / |L| <= 0.01, computed in double precision floating point, in sheet order. If any, take the first: a near match, shown as that row's value. Floating point counts: against 0.5%, the text 0.505% gives 0.010000000000000009 and is not close.
6. Otherwise the number is not on the lock sheet.

Then the weekday check on the same asset text, with these three patterns (case insensitive), all matches of the first, then all of the second, then all of the third, with no de-duplication:

| Form | Pattern |
|---|---|
| 1 | `WD\.?,?\s+DAY\s+MON\.?,?\s+(?P<year>\d{4})` |
| 2 | `WD\.?,?\s+MON\.?\s+DAY,?\s+(?P<year>\d{4})` |
| 3 | `DAY\s+MON\.?,?\s+(?P<year>\d{4})\s*(?:\(\|,\s*(?:a\s+)?)WD` |

where WD is `(?P<wd>mon(?:day)?|tue(?:s|sday)?|wed(?:nesday)?|thu(?:r|rs|rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)`, DAY is `(?P<day>\d{1,2})(?:st|nd|rd|th)?` and MON is as above.

There is no word boundary before or after the weekday, so a weekday can start inside a longer word ("Lemon 5 May 2026" is read as "mon 5 May 2026"), and in form 3 the weekday match takes the first alternative that fits, so "a Tuesday" is matched as "a Tues" and "(Thursday" as "(Thur". The matched text printed is exactly what the pattern matched.

For each match: the month is the position of its first three letters in jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec. If day, month and year do not form a real calendar date, the problem is `'<matched text>': not a real date`. Otherwise the written weekday is the weekday whose name starts with the first three letters of the weekday text; if it differs from the real weekday of the date, the problem is `'<matched text>': that date is a <real weekday, capitalised>`.

## Printed output (text)

For each asset, in the order given:

| Line | Exact shape |
|---|---|
| 1 | `Asset: <name>` |
| 2 | `  matched: <w> (<id>), <w> (<id>), ...` in text order, or `  matched: none` |
| one per near match, in text order | `  near <id>: '<w>' is close to '<shown value>'; write it as on the sheet or lock the rounded form` |
| one per number not on the sheet, in text order | `  not on the lock sheet: '<w>'` |
| one per weekday problem, in the order above | `  weekday: <problem>` |

Then:

| Line | Exact shape |
|---|---|
| | `Lock rows used:` |
| one per lock row, in sheet order | `  <id> <label> = <value>: <names of the assets that have a match with this id, in asset order, joined by ", ">`, or `: not used` |
| last | `Result: problems found` when any asset has a near match, a number not on the sheet or a weekday problem; otherwise `Result: every number is on the lock sheet and every weekday is right` |

An asset name appears once in a lock row's list however many matches it has. Two lock rows with the same id both list every asset that matched that id.

The result code is 1 when problems were found and 0 otherwise.

## Printed output (JSON, for API or programmatic use)

A list with one object per asset, in order, indented by 2 spaces per level, every key and every list item on its own line, a space after each colon, an empty list written `[]`. Characters outside plain ASCII are written as they are (no `\u` escapes). Each object has the keys, in this order: "asset" (the name), "matched" (a list of two item lists `[w, id]`), "near" (a list of three item lists `[w, id, shown value]`), "unlocked" (a list of written forms), "weekday_problems" (a list of problem texts). The "Lock rows used" block and the Result line are not printed in JSON. The result code is as for the text form.

## Worked example

Lock sheet:

```
id,label,value,source
L1,detections in India,265.52 million,report p. 12
L2,endpoints monitored,8 million,report p. 4
L3,engineering and manufacturing detections,3.79 million,report p. 39
L4,engineering and manufacturing share,14.22%,report p. 39
L5,top state detections (Maharashtra),36.13 million,report p. 36
```

Asset post1.md: "Between October 2024 and September 2025, the publisher's telemetry recorded 265.52 million detections across over 8 million endpoints in India. Engineering and manufacturing came third in its industry list, with 3.79 million detections."

Asset brief.md: "# Brief", an empty line, then "14.22% of all detections hit manufacturing. That is 265 million attacks, and 91% of plants were exposed." and on the next line "The report launched on Wednesday, 9 December 2025."

Working: in post1.md, 2024 and 2025 are years with no lock row of that value, so they are skipped; 265.52 million, 8 million and 3.79 million match L1, L2 and L3. In brief.md, 14.22% matches L4; 265 million is within 1 percent of 265.52 million (0.52 / 265.52 = 0.00196), so it is a near match to L1; 91% matches nothing; 9, December and 2025 sit inside a date span; 9 December 2025 is a Tuesday.

Printed text:

```
Asset: post1.md
  matched: 265.52 million (L1), 8 million (L2), 3.79 million (L3)
Asset: brief.md
  matched: 14.22% (L4)
  near L1: '265 million' is close to '265.52 million'; write it as on the sheet or lock the rounded form
  not on the lock sheet: '91%'
  weekday: 'Wednesday, 9 December 2025': that date is a Tuesday
Lock rows used:
  L1 detections in India = 265.52 million: post1.md
  L2 endpoints monitored = 8 million: post1.md
  L3 engineering and manufacturing detections = 3.79 million: post1.md
  L4 engineering and manufacturing share = 14.22%: brief.md
  L5 top state detections (Maharashtra) = 36.13 million: not used
Result: problems found
```

Result code 1. The JSON form of brief.md is:

```
  {
    "asset": "brief.md",
    "matched": [
      [
        "14.22%",
        "L4"
      ]
    ],
    "near": [
      [
        "265 million",
        "L1",
        "265.52 million"
      ]
    ],
    "unlocked": [
      "91%"
    ],
    "weekday_problems": [
      "'Wednesday, 9 December 2025': that date is a Tuesday"
    ]
  }
```

### Further checked cases (same lock sheet unless named)

| Asset text | Printed lines for the asset |
|---|---|
| `Share fell to -14.22% this year; a **-14.22%** swing, (-14.22%) and :-14.22% too.` | `matched: none` and four times `not on the lock sheet: '-14.22%'` |
| `Ranges: 10-12 plants, 12%-14% share, and 14.22%-15% in Q3.` | `matched: 14.22% (L4)`; not on the sheet '10', '12', '12%', '14%', '15%' |
| `Part 2 of 5: 3 charts, 0 errors, 12 slides and 265.52 million detections.` with allow small 5 | `matched: 265.52 million (L1)`; not on the sheet '12' only |
| The same with allow small 0 | not on the sheet '2', '5', '3', '12' ("0" is skipped) |
| `Close forms: 265.5 million, 265.52 mn, 266 million, 263 million, 14.2%, 14.22 percent, 14.22 per cent, 8M, 8 m.` | `matched: 265.52 mn (L1), 14.22 percent (L4), 14.22 per cent (L4), 8M (L2), 8 m (L2)`; near L1 for '265.5 million', '266 million', '263 million'; near L4 for '14.2%' |
| Lock `C1,accounts in the study,"2,024 accounts",...` and `C2,median deal size,Rs 51.4 crore,...`; text `We studied 2024 accounts in 2024 and 2,024 accounts in total. Median deal: Rs 51.4 crore, or $51.4 crore by mistake, or ₹51.4 crore, or INR 51.4 crore, or Rs. 51.4 cr, or 51.4 crore.` | `matched: 2024 (C1), 2024 (C1), 2,024 (C1), Rs 51.4 crore (C2), ₹51.4 crore (C2), INR 51.4 crore (C2), Rs. 51.4 cr (C2), 51.4 crore (C2)` and `near C2: '$51.4 crore' is close to 'Rs 51.4 crore (the currency differs)'; ...` |
| `Lemon 5 May 2026 is odd; Sunday 5 May 2026 is wrong; Tuesday, 5 May 2026 is right.` | `weekday: 'mon 5 May 2026': that date is a Tuesday` and `weekday: 'Sunday 5 May 2026': that date is a Tuesday` |
| `13 August 2026 (Friday) is wrong; 31 February 2026, a Tuesday is not real.` | `weekday: '13 August 2026 (Friday': that date is a Thursday` and `weekday: '31 February 2026, a Tues': not a real date` |
| Lock `N1,loss,-5,p`; text `-5 and 5 and ` U+2212 `5 and a-5 and 1-5.` | matched '-5' and the U+2212 form (both N1); not on the sheet '5', '5', '1', '5' |

## Results in short

| Result | Meaning |
|---|---|
| a "Could not read: " line | A file is missing or unreadable, or the lock sheet is malformed; pass the line on and ask for the file. |
| `Result: every number is on the lock sheet and every weekday is right` | Every number in every asset matches a lock row. |
| `Result: problems found` | Fix every near match, unlocked number and weekday, then check again. |
