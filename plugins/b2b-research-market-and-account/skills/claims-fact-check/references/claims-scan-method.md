# Claims scan: the method

This file sets out one fixed scan of a text: the list of sentences that carry a checkable claim (to seed a claims register), attributions with no named source, the weekday written next to each date, dates in an earlier year, dashes, and, on request, banned words and patterns. Follow the rules exactly. When code execution is available, write your own scan from these rules and run it; otherwise work it out by hand and say "counted by hand per the method". Either way the printed lines must match the shapes below character for character.

The claim list seeds the register; it is never the whole register. Read the text as well, because a claim can sit in a sentence with no digit and no listed word.

## Inputs

| Input | Required | Meaning |
|---|---|---|
| text | yes | The text to scan (a draft, a critique, a final version). A file is read as UTF-8; line endings \r\n and \r are read as \n. |
| current year | no | A whole number. When given (and not 0), dates in an earlier year are listed for a look. |
| tone | no | When on, also list banned words and patterns. |
| JSON | no | Print the JSON form instead of the text form. |

## Refusal

A file that cannot be opened or is not UTF-8: print one line, `Could not read <path>: <the system's error text>` (for a missing file `Could not read <path>: [Errno 2] No such file or directory: '<path>'`), and nothing else. The result code is 2.

## Patterns used below

All patterns are regular expressions in Python syntax. `\d` and `\s` are in their Unicode sense (so Arabic Indic digits count as digits). "Case insensitive" means upper and lower case letters match each other.

Building blocks:
- WD: `(?P<wd>mon(?:day)?|tue(?:s|sday)?|wed(?:nesday)?|thu(?:r|rs|rsday)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)`
- MON: `(?P<mon>jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)`
- DAY: `(?P<day>\d{1,2})(?:st|nd|rd|th)?`
- YEAR: `(?P<year>\d{4})`

Date patterns (all case insensitive):

| Name | Pattern |
|---|---|
| ANY_DMY | `\b` DAY `\s+(?:of\s+)?` MON `\.?,?\s+` YEAR `\b` |
| ANY_MDY | `\b` MON `\.?\s+` DAY `,?\s+` YEAR `\b` |
| ISO | `\b(?P<year>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})\b` (case does not matter) |
| WD_BEFORE_DMY | WD `\.?,?\s+` DAY `\s+(?:of\s+)?` MON `\.?,?\s+` YEAR |
| WD_BEFORE_MDY | WD `\.?,?\s+` MON `\.?\s+` DAY `,?\s+` YEAR |
| DMY_WD_AFTER | DAY `\s+(?:of\s+)?` MON `\.?,?\s+` YEAR `\s*(?:\(\|,\s*(?:a\|which is a\|is a)?\s*)` WD |
| MDY_WD_AFTER | MON `\.?\s+` DAY `,?\s+` YEAR `\s*(?:\(\|,\s*(?:a\|which is a\|is a)?\s*)` WD |

(In the table, `\|` stands for the alternation bar; each row is one pattern made by joining the pieces with nothing between them.)

The four weekday patterns have no word boundary before or after the weekday, so a weekday can start inside a longer word ("Lemon 5 May 2026" is read as "mon 5 May 2026", and "5 May 2026, Monitoring" as "5 May 2026, Mon"). When the weekday comes last, the pattern takes the first alternative that fits, so "(Thursday" is matched as "(Thur" and "a Tuesday" as "a Tues"; the text printed is exactly what the pattern matched. When the weekday comes first, the match runs on to the date, so "Thursday, 13 August 2026" is matched whole.

Month of a match: if the month text, in lower case, starts with "sept", it is September; otherwise its first three letters give the month (jan 1, feb 2, mar 3, apr 4, may 5, jun 6, jul 7, aug 8, sep 9, oct 10, nov 11, dec 12). The written weekday is the weekday whose name starts with the first three letters of the weekday text.

## Step 1. Sentences

1. Split the text at every line break (\n). Strip white space from both ends of each piece; drop the empty pieces. Each remaining piece is a block. (A bullet or numbered line is its own block, like any other line.)
2. Split each block into sentences at every run of white space that comes right after ".", "!" or "?" and right before an optional opening `"`, `“` (U+201C), `(` or `[` followed by an upper case letter A to Z, a digit 0 to 9, `₹` or `$`. The regular expression is `(?<=[.!?])\s+(?=["“(\[]?[A-Z0-9₹$])`, case sensitive. Strip each sentence; drop empty ones.

So "No. 1 in India." becomes "No." and "1 in India.", "Revenue was Rs. 51.4 crore" becomes "Revenue was Rs." and "51.4 crore", "1. First item" becomes "1." and "First item", and "Sentence one. sentence two" stays one sentence (lower case after the space).

## Step 2. Claim types

For each sentence, collect its types in this order (each at most once):
1. money: the sentence contains `[₹$€£]` or, case insensitive, `\b(?:rs\.?|inr|usd|eur|gbp)\b` (the word Rs, INR, USD, EUR or GBP standing alone).
2. If the sentence contains any digit:
   - percentage: it contains `%` or, case insensitive, `\bper ?cent\b` ("percent", "per cent", "Percent").
   - date: ANY_DMY, ANY_MDY or ISO finds a match in it.
   - number: always added when there is a digit.
3. superlative: case insensitive, `(#\s?1\b|\bnumber one\b|\bfirst\b|\bonly\b|\blargest\b|\bbiggest\b|\bleading\b|\bbest\b|\btop\b|\bfastest\b|\bmost\b|\blowest\b|\bhighest\b|\bunique\b|\bno\.? 1\b)`. Note "first", "only", "top", "most" and "leading" count wherever they stand ("Leading space" counts).
4. attribution: case insensitive, `\b(according to|as per|per the|reports?|reported|says|said|states|stated|survey|study|studies|research|data shows?|found that|estimates?)\b`. "United States" counts; "reporters" and "researchers" do not.
5. quote: `["“][^"”]{3,}["”]`: a straight or left curly double quote, at least 3 characters that are neither a straight double quote nor U+201D, then a straight double quote or U+201D. Curly single quotes do not count.

A sentence with at least one type is a claim. Claims are numbered C1, C2, ... in text order.

## Step 3. Attribution with no named source

A claim whose sentence matches, case insensitive, `\b(research shows|studies show|studies have shown|experts say|data shows|reports suggest|it is said|many believe|according to research|according to studies|according to experts)\b` is also listed here with its id. Only claims are checked: "Many believe it." with no digit and no listed word is not a claim, so it is not listed.

## Step 4. Weekday problems

Run WD_BEFORE_DMY, then WD_BEFORE_MDY, then DMY_WD_AFTER, then MDY_WD_AFTER over the whole text, each left to right without overlaps. Skip a match whose exact start and end were already taken by an earlier match (of any of the four). For each other match:
- If day, month and year do not form a real calendar date: `{"text": <matched text>, "problem": "not a real date"}`.
- Else if the written weekday differs from the real weekday: problem `that date is a <Real>, not a <Written>` (both capitalised, full names).

## Step 5. Year checks

Only when a current year is given and is not 0. List every match of ANY_DMY (left to right), then every match of ANY_MDY, then every match of ISO (here the middle number is the month and the last the day). No de-duplication. For each:
- Not a real calendar date: problem `not a real date`.
- Year below the current year: problem `year <year> is before <current year>: fine if this is history, wrong if this document is meant to be current`.
- Otherwise nothing.

## Step 6. Dashes

Split the text into lines the way Python's splitlines() does (at \n and also at the rare separators U+000B, U+000C, U+001C, U+001D, U+001E, U+0085, U+2028, U+2029), numbered from 1. In each line find, left to right without overlaps, `[\u2012\u2013\u2014\u2015]|\s--?\s`: a figure dash (U+2012), an en dash (U+2013), an em dash (U+2014), a horizontal bar (U+2015), or one or two plain hyphens with a white space character on both sides (the white space is part of the match). For each, the context is the line from 20 characters before the start of the match (or the line start) to 20 characters after its end (or the line end), not stripped.

So a bullet "- item" at the very start of a line is not a dash, but an indented bullet "  - item" is, and "word--joined" is not.

## Step 7. Banned words and patterns (tone on)

1. Make a lower case copy of the text with U+2019 and U+2018 replaced by a straight apostrophe.
2. For each word in this list, in this order, find every place in the copy where it stands with no letter a to z directly before or after it (digits, underscores, hyphens and spaces do not block it): game-changer, game changer, game-changing, game changing, leverage, dive in, dive deep, delve, tapestry, elevate, elevated, unlock, seamless, seamlessly, landed hard, resonated, struck a chord, genuine unlock, genuinely, honestly, straightforward, revolutionize, revolutionise, revolutionary, supercharge, harness, empower, in today's world, ever-evolving, next level, it's important to note, testament to, the rise of, keep coming back to, sat with me, rubric, move the needle, here's the thing, groundbreaking, transformative, comprehensive, robust, dynamic, holistic, synergy, paradigm shift, thought leader, next-level, humbled to share. Each find is an entry with its line number (1 plus the number of \n before it) and the word. So "leveraged", "unlocked" and "Gamechanger" are not found, but "3x_leverage" is, and "genuine unlock" also gives "unlock".
3. Three patterns, run on the original text (not the copy), each find an entry with its line number and label:

| Pattern | Label |
|---|---|
| case insensitive `\b(?:it\|this\|that)(?:'s\| is\| was) not [^.!?]{1,60}[.!?]\s+(?:it\|this\|that)(?:'s\| is\| was) ` (straight apostrophe only; the text in between may cross a line break; a trailing space ends the pattern) | `"It is not X. It is Y" contrast pattern` |
| `!` | `exclamation mark` |
| case insensitive `\bstart(?:ing)? (?:on\|from) monday\b` | `"start on Monday" line` |

4. Sort all entries by line number, then by the word or label in plain character order (a label starting with a double quote comes before letters); entries that are equal keep their order.

Without tone, there are no entries and no banned section.

## Printed output (text)

Line by line:

| Line | Exact shape | When |
|---|---|---|
| | `Claims to check: <count>` | Always. |
| one per claim | `  <id> [<types joined by ", ">] <sentence>` | |
| | `Attribution with no named source:` then one line per item, `  <id> <sentence>` | Only when there is at least one. |
| | `Date problems:` then one line per problem, `  '<text>': <problem>` | When there is at least one. |
| | `Date problems: none found (weekdays written next to dates match the calendar)` | When there are none. |
| | `Year checks:` then one line per item, `  '<text>': <problem>` | Only when there is at least one. |
| | `Dashes: <count>` then one line per dash, `  line <n>: ...<context>...` | When there is at least one. |
| | `Dashes: none` | When there are none. |
| | `Banned words and patterns: <count>` then one line per entry, `  line <n>: <word or label>` | Only when there is at least one (tone on). |

The result code is 1 when there is at least one weekday problem, dash or banned entry, and 0 otherwise. Claims, unnamed sources and year checks never change the result code.

## Printed output (JSON, for API or programmatic use)

One object, indented by 2 spaces per level, every key and every list item on its own line, a space after each colon, an empty list written `[]`. Characters outside plain ASCII are written as they are (no `\u` escapes); a double quote inside a text is written `\"`, a backslash `\\`. Keys, in order:
- "claims": objects with "id", "types" (a list), "sentence".
- "unnamed_sources": objects with "id", "sentence".
- "date_problems": objects with "text", "problem".
- "year_checks": objects with "text", "problem" (an empty list when no current year is given).
- "dashes": objects with "line", "context".
- "banned": objects with "line", "word".

The result code is as for the text form.

## Worked example

Text (one line): "Unicommerce grew revenue 20.2% to ₹51.3 crore in Q1 FY27 and now serves 10,000 clients. It is India's largest e-commerce SaaS platform. Results came out on Wednesday, 13 August 2026." Current year 2026.

Working: three sentences. The first has ₹ (money), a digit and % (percentage, number). The second has "largest" (superlative). The third has a digit and "13 August 2026" (date, number). WD_BEFORE_DMY matches "Wednesday, 13 August 2026"; 13 August 2026 is a Thursday. No date is before 2026. No dash.

Printed text:

```
Claims to check: 3
  C1 [money, percentage, number] Unicommerce grew revenue 20.2% to ₹51.3 crore in Q1 FY27 and now serves 10,000 clients.
  C2 [superlative] It is India's largest e-commerce SaaS platform.
  C3 [date, number] Results came out on Wednesday, 13 August 2026.
Date problems:
  'Wednesday, 13 August 2026': that date is a Thursday, not a Wednesday
Dashes: none
```

Result code 1. The JSON form ends:

```
  "date_problems": [
    {
      "text": "Wednesday, 13 August 2026",
      "problem": "that date is a Thursday, not a Wednesday"
    }
  ],
  "year_checks": [],
  "dashes": [],
  "banned": []
}
```

### Further checked cases

| Text | Printed result |
|---|---|
| "Zoho, headquartered in Chennai, serves 100 million users across 55+ applications" U+2014 "and it got there without outside funding. For an IT head choosing a suite, that matters: a vendor answering to customers, not investors." with tone | `C1 [number]` for the first sentence; `Dashes: 1` and `  line 1: ...ss 55+ applications ` U+2014 ` and it got there wi...`; no banned section. |
| "Research shows buyers prefer suites. Studies show 80% of SMBs agree." | `C1 [attribution]`, `C2 [percentage, number, attribution]`, both under "Attribution with no named source:". |
| "The launch was on 13 August 2025 and the review on August 14, 2024. Our filing is dated 2026-03-31." with year 2026 | Year checks in the order `'13 August 2025': year 2025 is before 2026: ...` then `'August 14, 2024': year 2024 is before 2026: ...`. |
| "On 5 May 2026, Monitoring starts." | `'5 May 2026, Mon': that date is a Tuesday, not a Monday` |
| "13 August 2026, which is a Wednesday." | `'13 August 2026, which is a Wednesday': that date is a Thursday, not a Wednesday` |
| "Sept 9, 2026, a Tuesday." | `'Sept 9, 2026, a Tues': that date is a Wednesday, not a Tuesday` |
| "Friday 31 February 2026." with year 2026 | Date problems `'Friday 31 February 2026': not a real date`; year checks `'31 February 2026': not a real date`. |
| "It is not a tool. It is a platform. That's not luck. That's process!" with tone | `line 1: "It is not X. It is Y" contrast pattern` twice, then `line 1: exclamation mark`. |
| "We are the #1 vendor. No. 1 in India." | `C1 [number, superlative] We are the #1 vendor.` and `C2 [number] 1 in India.` ("No." alone has no type). |
| Lines "- bullet item" and "  - indented bullet" | Only line 2 is a dash: `  line 2: ...  - indented bullet...` |

## Results in short

| Result | Meaning |
|---|---|
| a "Could not read" line | The file is missing or unreadable; ask for a readable copy. |
| result code 0 | No weekday problem, dash or banned entry. Claims are still to be checked. |
| result code 1 | Fix every weekday problem, dash and banned entry, then scan again. |
