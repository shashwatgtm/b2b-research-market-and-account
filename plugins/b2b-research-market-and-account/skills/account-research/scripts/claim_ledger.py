#!/usr/bin/env python3
"""Claim ledger (1.0.5): lists every line of the text you are about to deliver that states a fact about the
user, a named company, a person or a buyer seat, or carries a figure or an absence claim, and checks the
ledger of sources you wrote for those lines. Python 3 standard library only; reads files, writes nothing,
sends nothing.

Use (python3, or python on Windows):
  claim_ledger.py list  ANSWER [SAVED ...]
  claim_ledger.py check ANSWER [SAVED ...] --ledger LEDGER [--opened OPENED] [--page PAGE ...] [--prompt PROMPT]
                        [--script-out FILE ...] [--final]

ANSWER is the chat answer exactly as it will be delivered; SAVED are the files saved for the user.
LEDGER has one line per entry:   <id>[,<id>...] | <source> | <detail>
  source user     the user's own message (--prompt file); figures must be in it and the line must keep
                  mostly the words of one of the user's sentences
  source page     detail: the URL opened in this session (it must be in --opened and have a --page file), then
                  optional quotes, each its own | part, copied word for word from that saved page text:
                    <id> | page | <url> | "<words from the page>" | "<more words>"
                  every figure and every quoted phrase of the line must be in the saved page text; a line that says who
                  said, reported, ran, surveyed or owns something (ATTRIBUTION) needs a quote of at most 240 characters
                  that holds its figure (or its quoted words) together with each attribution word the line uses (the
                  role, survey, study, customer, both, all, only); a quote that says the source is not named or not
                  stated never supports an attribution
  source script   detail: optional "printed line" quotes; every figure must appear in a --script-out file, and a line
                  that says what a script or scan found keeps the script's own words (half of its words in one
                  printed line); copy the printed line
  source notes    detail: a file in this skill's references folder; the line must be hedged or say
                  "notes"
  source general  a hedged general statement ("often", "may", "worth checking"), naming no company
  source absence  detail: <word> | <url> <url> ...; each URL must be in --opened with that word under
                  "checked:", and the line must name the pages it checked
  source self     a line that says only what this answer did ("I left out ...", "I opened ..."); it starts with I and
                  says nothing about the user's team, a role or a group of people
  source search   always refused: label the line "from a search result, page not opened" or leave it out
OPENED has one line per page opened in this session:  <url> [| checked: <word>, <word>]
PAGE is the text of one opened page, saved as the tool returned it (WebFetch result, or the downloaded page's text):
  its URL on the first line, the text after it. Give one --page per opened page.
A clause about a group of people (buyers, sellers, visitors, readers, customers, teams, a role) that is not hedged is listed
on its own (GROUP), also inside a table row: give it its own source (page with a quote, user, notes) or hedge it.
check with an empty ledger prints every id and a LEDGER SKELETON to fill in (the lighter procedure).
1.0.5: every check prints SLOTS (the [User to add: ...] slots per file). A file with three or more paragraphs that are only
slots (THIN DRAFT), or a line that holds the asset back until the user replies (HELD BACK), fails: draft those parts from the
user's words and the opened pages as [Draft for you to confirm: ...] and keep a slot only for what no source gives (a name, a
contact, a price, a date, an approval). A figure inside a draft must be in the user's message, a saved page or a script's
output (DRAFT FIGURE). A quote must be the page's own words, not the web tool's comment about the page (TOOL COMMENT: "The
page does not say ...", "No customer count is given"). The premise of a question ("You own the site copy: is there ...?") is
listed as its own line. An absence line about the user's own text (a paste saved as a page file) quotes the closest line it
found in that text (CLOSEST MATCH).
--final: use it on the last check, as your very last tool call. It prints the verdict on the first line and, when the check
passes, the answer file between "=== BEGIN CHECKED REPLY <digest> ===" and "=== END CHECKED REPLY <digest> ===". That
text, exactly, is your whole chat reply: nothing before it, nothing after it, no word changed. In Claude Code the plugin's
Stop hook (hooks/delivery_check.py) compares the reply with it and sends Claude back when they differ.
Every check prints a digest of each file (line ends and trailing spaces ignored).
Exit code: 0 PASS, 1 FAIL, 2 bad input.
"""
import difflib, hashlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

LABEL_SPAN_START = re.compile(r"\[(?=quote from\b|[^\[\]]{0,60}?(?:\bto (?:add|confirm|supply|set|fill|provide|approve|choose|check)\b|\bdraft\b|\bplaceholder\b))", re.I)
LINE_LABEL = re.compile(r"as pasted, not yet checked|not yet checked|from a search result|page (?:itself )?(?:was )?not opened|"
                        r"\bplaceholder\b|\bhypothetical\b|\bassumption\b|draft for you to confirm|user to add|to confirm\]|for you to confirm", re.I)
SEARCH_LABEL = re.compile(r"from a search result|search result.{0,40}not opened|page (?:itself )?(?:was )?not opened", re.I)
ABSENCE = re.compile(r"\b(?:does ?n[o']t|did ?n[o']t|do ?n[o']t|is ?n[o']t|are ?n[o']t|was ?n[o']t|never) (?:mention|say|list|show|state|name|appear|include|use)s?\b|"
                     r"\bno mention\b|\bnot mentioned\b|\bnot (?:found|listed|shown|stated|named)\b|\bfound no\b|\bnowhere\b|\bno (?:sign|trace|record) of\b|"
                     r"\b(?:is|are) not on\b|\bis ?n't on\b|\babsent from\b|\bmissing from\b|\bha(?:s|ve) no\b|\blacks?\b|"
                     r"\bdid ?n[o']t find\b|\bnothing (?:about|on|in)\b|\bha(?:s|ve) ?n[o']t (?:published|posted|said|shared|listed|named|stated|announced)\b|\bnone of the\b|\b(?:is|are) not in\b|\bnever (?:talks|says|mentions|publishes|lists|shows|names)\b|\bdo(?:es)? ?n[o']t (?:offer|publish|have|provide|give|share)\b|\bhad no\b", re.I)
HEDGE = re.compile(r"\b(?:often|may|might|can|could|tends?|usually|sometimes|likely|perhaps|possibly|probably|worth (?:checking|asking|testing)|"
                   r"in many cases|some)\b", re.I)
SEAT = re.compile(r"\b(?:C[EFIMTO]Os?|CISOs?|CHROs?|CROs?|COOs?|CPOs?|VPs?|head of|directors?|buyers?|procurement|champions?|decision makers?|"
                  r"analysts?|journalists?|editors|reporters|investors?|founders?|marketers?|leaders|teams|committee|board)\b")
YOU_US = re.compile(r"\b(?:us|ours)\b")
YOU = re.compile(r"(?:^|[.:]\s|\*\*\s?)I(?:'ve| have)? (?:built|founded|grew|grow|led|lead|run|ran|own|owned|cut|launched|started|sold|sell|manage|managed|"
                 r"joined|spent|host|hosted|speak|spoke|work|worked|helped|help|created|scaled|doubled|tripled|raised|won|hired|advise|advised|have \d)\b|\[Name\]|\b(?:we|our|we're|we've)\b|\byou(?:'ve|'re)? (?:are|were|have|had|lead|led|run|ran|own|built|spent|joined|work|worked|"
                 r"sell|sold|said|told|wrote|manage|managed|speak|spoke|launched|started|founded)\b|\byour (?:team|company|customers?|clients?|product|"
                 r"role|title|years|manager|ceo|founder|board|employer|launch|feature|event|talk|webinar|firm|business|buyers?|accounts?|pipeline)\b", re.I)
FIG = re.compile(r"\d")
LEAD_NAME = re.compile(r"[A-Z][A-Za-z0-9&.\-]*(?:'s)? (?:has|have|is|was|are|were|sells|sold|says|said|offers|ranks|ranked|provides|makes|runs|owns|requires|publishes|"
                       r"lists|launched|raised|serves|builds|uses|named|won|bought|acquired)\b")
WORD = re.compile(r"[A-Za-z][A-Za-z0-9&'.\-]*")
COMMON = set("""I I'm I've I'll I'd A An The This That These Those It Its It's If When Where What Which Who Why How And But Or Not No Yes Use Used Using
Here There Then Than Also Each Every All Any Some Most More Less One Two Three Four Five Six Seven Eight Nine Ten Do Don't Does Is Are Was Were Be Been
For From To In On At By With Without About After Before Between Into Over Under Up Down Out Only Just Still Even So As Of My Me Mine Your You You're
You've We We're Our Us They Their Them He She His Her Please Note Draft Open Items Item Question Questions Plan Source Sources Status Line Lines Check
Checks Fact Facts Notes Summary Option Options Step Steps Next Done Keep Add Make Send Ask Read See Say Write Copy Paste Run Before After Monday
Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July August September October November December Mon Tue
Wed Thu Fri Sat Sun Jan Feb Mar Apr Jun Jul Aug Sep Sept Oct Nov Dec OK Q Subject Title Headline About Bio Short Medium Long Body Hook Opening Close
Call Why What's Who's Here's That's There's Let's Today Tomorrow Yesterday Near-final Confirmed Missing Needed""".split())
STOP = set("""the a an and or but of to in on at by for with from into over under about after before between this that these those it its is are was
were be been being have has had do does did will would shall should can could may might must not no yes you your yours we our us they their them he she
his her i me my mine who whom which what when where why how than then also just only very more most less least so as if each every all any some such
own same other there here name""".split())
ABBR = re.compile(r"\b(Inc|Ltd|Co|Corp|Pvt|e\.g|i\.e|vs|No|Dr|Mr|Ms|Mrs|St|Jr|Sr|approx|est)\.", re.I)
# 1.0.4 (run 36A): a group of people (R34A-3), who said or reported what (R34A-1), what a script found (SON-1)
GROUPN = re.compile(r"\b(?:buyers?|sellers?|visitors?|readers?|customers?|clients?|users?|people|teams?|marketers?|founders?|shoppers?|merchants?|"
                    r"competitors?|prospects?|audiences?|attendees?|journalists?|editors?|reporters?|analysts?|investors?|C[EFIMTO]Os?|CISOs?|CHROs?|CROs?|"
                    r"lenders?|banks|operators?|SMEs|enterprises|brands|vendors|developers?|engineers?|recruiters?|candidates?|employees?|managers?|"
                    r"executives?|leaders?|decision[- ]makers?|procurement|subscribers?|listeners?|viewers?|panelists?|sponsors?|partners|everyone|nobody|"
                    r"guests?|delegates?|exhibitors?|participants?|speakers|members?|shippers?|retailers?|organi[sz]ers?|hosts|students?|agencies|drivers|carriers|"
                    r"applicants?|borrowers?|consumers?|owners?|traders?|distributors?|firms|companies|heads)\b", re.I)
TITLE = re.compile(r"\b[A-Z][a-z]+(?: (?:of |and |for )?[A-Z][a-z]+)+\b")   # an event or product name in Title Case is not a group claim (run 36A events audit)
IMPERATIVE = re.compile(r"^(?:ask|send|use|add|keep|check|run|write|call|invite|share|pick|choose|book|post|email|follow|draft|plan|tell|show|open|put|get|"
                        r"give|let|make|try|test|read|review|confirm|replace|remove|cut|drop|move|start|schedule|brief|prepare|target|name|avoid|do|don't|"
                        r"never|consider|focus|reach|thank|list|note|offer|lead with|link|quote|reply|mention|record|save|set|tag|update|verify|interview)\b", re.I)
ATTR = re.compile(r"\b(?:said|says|told|tells|added|answered|replied|stated|quoted|noted|explained|confirmed|mentioned|highlighted|observed|commented|admitted|acknowledged|warned|according to|reports?|reported|survey(?:s|ed)?|poll(?:s|ed)?|"
                  r"stud(?:y|ies)|research (?:by|from)|found that|finds that|credited|conducted|cites?|cited|citing|own (?:survey|figures?|data|study|numbers)|"
                  r"customer stor(?:y|ies)|case stud(?:y|ies)|figures? (?:about|from|for|of)|numbers? (?:about|from|for))\b", re.I)
SPEECH = re.compile(r"\b(?:said|says|told|tells|added|answered|replied|stated|quoted|noted|explained|confirmed|mentioned|highlighted|observed|commented|admitted|pointed out|acknowledged|warned|ran|runs|conducted|commissioned|published|released)\b", re.I)
ROLE = re.compile(r"\b(?:chief|officer|chair(?:man|woman|person)?|controller|director|head|president|founder|co-?founder|manager|analyst|spokesperson|"
                  r"executive|treasurer|secretary|minister|governor|cfo|ceo|coo|cto|cmo|cio|ciso|vp|vice|finance|financial|operating|technology|marketing)\b", re.I)
AGENT2 = re.compile(r"\b(?:according to|reported by|published by|conducted by|run by|commissioned by|cited by|credited to)\s+((?:[\w'.-]+[,\s]*){1,4})", re.I)
AGENT = re.compile(r"\b(?:survey|study|poll|report|research|figures?|data|numbers?)\s+(?:by|from)\s+((?:[\w'.-]+\s*){1,5})", re.I)
AGENT_END = re.compile(r"^(?:found|finds|said|says|shows|showed|reported|reports|suggests?|revealed|of|on|in|that|and|which|was|is)$", re.I)
TURN = re.compile(r"(?:^|(?<=[\s*>]))(?<!, )(?=(?:[A-Z][\w.'-]+ ){1,3}[A-Z][\w.'-]+(?:, [A-Z][\w &.'-]{1,40}| \([A-Za-z &.'-]{1,40}\))?\**:)"
                  r"|(?:^|(?<=[.!?]\s)|(?<=\n))(?!(?:Source|Note|Quote|Context|Sample|Conducted|Publication|Key|Survey|Excluded|Status|Date|Fetched)\b)(?=[A-Z][a-z]+(?: \([A-Za-z &.'-]{1,40}\))?\**: )"
                  r"|(?<=,)\s+(?=while\b|whereas\b)|;\s*")   # speaker turns: "Name Name:", "Name, Role:", "Name (Role):", "Name:" after a sentence, and "..., while ..." in a prose summary (events audit round 2 N4)
ATTR_NOUN = re.compile(r"\b(survey|study|studies|poll|customer|client|story|research|C[EFIMTO]O|CISO|CHRO|CRO|founder|analyst)s?\b", re.I)
SCOPE = re.compile(r"\b(both|all|every|each|only|one (?:customer|client|company|account|story|study|survey))\b", re.I)
NEG_ATTR = re.compile(r"not (?:named|stated|disclosed|given|attributed|identified|specified)|\bunnamed\b|\bno source\b|does ?n[o']t (?:say|state|name) who", re.I)
SCRIPTREF = re.compile(r"(?:\b(?:scan|script|checker|count)\b|\w+\.py\b).*\b(?:flagged|found|printed|counted|shows?|showed|reports?|reported|passed|failed|returned|gave|lists?|listed|says?)\b"
                       r"|\b(?:flagged|printed|counted)\b.*\b(?:scan|script|checker|\w+\.py)\b", re.I)
GENERIC = set("script scan checker check checks checked print printed run ran flag flagged count counted show shows showed found find report reported "
              "list listed output line lines version file".split())
GROUP_UNITS = set()


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().replace("\u2019", "'").replace("\u2018", "'").replace("\r\n", "\n")


def label_ranges(text):
    """Character ranges inside [Draft for you to confirm: ...], [User to add: ...] and similar brackets (nested brackets allowed)."""
    out = []
    for m in LABEL_SPAN_START.finditer(text):
        depth, i = 0, m.start()
        while i < len(text):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
                if depth == 0:
                    break
            elif text[i] == "\n":   # an unclosed label ends at the end of its line (auditor item 3)
                break
            i += 1
        out.append((m.start(), i + 1))
    return out


def split_sentences(line):
    protected = ABBR.sub(lambda m: m.group(0)[:-1] + "\u0001", line)
    protected = re.sub(r"^(\s*(?:[-*]\s+)?\d{1,2})\.", lambda m: m.group(1) + "\u0001", protected)   # a list number is not a sentence end
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\[\"'(*_0-9])", protected)
    return [p.replace("\u0001", ".") for p in parts if p.strip()]


def units(text, fname):
    """(file, line number, text, labelled) for every sentence (table rows whole); code fences skipped."""
    ranges = label_ranges(text)
    res, pos, fence = [], 0, False
    lines = text.split("\n")
    for n, line in enumerate(lines, 1):
        start = pos
        pos += len(line) + 1
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence or not line.strip() or re.fullmatch(r"[\s|:\-]+", line) or line.lstrip().startswith("#"):
            continue
        is_row = line.lstrip().startswith("|")
        if is_row and n < len(lines) and re.fullmatch(r"\s*\|?[\s|:\-]+\|?\s*", lines[n]) and "-" in lines[n]:
            continue   # a table header row (the next line is the separator) states no fact (auditor item 2)
        pieces = [line] if is_row or fname.lower().endswith(".csv") else split_sentences(line)
        cursor = 0
        for piece in pieces:
            off = line.find(piece, cursor)
            off = cursor if off < 0 else off
            cursor = off + len(piece)
            a, b = start + off, start + off + len(piece)
            inside = sum(max(0, min(b, y) - max(a, x)) for x, y in ranges)
            outside = re.sub(r"\[(?:[^\[\]]|\[[^\[\]]*\])*\]", " ", piece)
            labelled = bool(LINE_LABEL.search(outside)) or (inside >= 0.5 * max(1, b - a) and len(WORD.findall(outside)) < 3) or bool(re.search(r"\bVERIFY WITH\b", piece))
            labelled = labelled or inside >= 0.9 * max(1, len(piece.strip()))   # 1.0.5: a later sentence of a multi sentence [Draft ...] is inside the draft label too
            if is_row and not LINE_LABEL.search(re.sub(r"\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]", " ", piece)) and not re.search(r"as pasted|search result|not opened|hypothetical|assumption", piece, re.I):
                # a row whose only label is a bracket slot in one cell: the other cells still state facts (auditor item 4)
                rest = [c for c in piece.strip().strip("|").split("|") if not re.fullmatch(r"\s*\[(?:[^\[\]]|\[[^\[\]]*\])*\]\s*", c)]
                if rest and len(rest) < len(piece.strip().strip("|").split("|")):
                    labelled = False
                    piece = "| " + " | ".join(c.strip() for c in rest) + " |"
            bare = strip_labels(piece)
            if res and res[-1][0] == fname and res[-1][1] == n and labelled and len(bare.split()) < 3 and not piece.lstrip("*_ ").startswith("["):
                res[-1] = (res[-1][0], res[-1][1], res[-1][2], True)   # a label standing alone labels the sentence before it
                continue
            res.append((fname, n, piece.strip(), labelled))
            if is_row and not labelled:
                res += group_clauses(fname, n, piece)
    return res


def group_clauses(fname, n, row):
    """A clause about a group of people inside a table cell is its own line (R34A-3, run 34A SOR-2): the row's page source does not cover it."""
    out = []
    for cell in row.strip().strip("|").split("|"):
        cell = re.sub(r"^\s*(?:pass|fail|partial|keep|cut|change|verdict|why|reason)\s*:\s*", "", cell.strip(), flags=re.I)
        cell = re.sub(r"['\"\u2018\u201c][^'\"\u2019\u201d]*\?['\"\u2019\u201d]", " ", cell)   # a quoted probe question (gate audit round 3, 4)
        if not GROUPN.search(TITLE.sub(" ", cell)):
            continue
        for cl in re.split(r";|,\s+(?:and|but|so|while|because|since|which)\s+|\s+(?:because|since|so that|while)\s+|\.\s+", cell):
            cl = cl.strip(" .,*_")
            if len(cl.split()) < 3 or cl.endswith("?") or HEDGE.search(cl) or re.match(r"(?i)if\b", cl) or IMPERATIVE.match(cl) or LINE_LABEL.search(cl):
                continue
            if GROUPN.search(TITLE.sub(" ", cl)) or re.search(r"\bthey\b|\bthem\b|\btheir\b", cl, re.I):
                GROUP_UNITS.add((fname, n, cl))
                out.append((fname, n, cl, False))
    return out


def strip_labels(s):
    s = re.sub(r"\[(?:draft for you to confirm|user to add|principal to confirm)[^:\]]*:?", " ", s, flags=re.I)
    s = LINE_LABEL.sub(" ", s)
    s = re.sub(r"[*_`#>|\[\]()\"]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def uid(s):
    return hashlib.sha1(strip_labels(s).encode("utf-8")).hexdigest()[:6]


def flags(text, mid_caps):
    text = re.sub(r"`[^`]*`|https?://\S+|\]\([^)]*\)|(?:/[\w.\-]+){2,}", " ", text)   # code spans, links and paths are not claims
    f = []
    if FIG.search(re.sub(r"\b[A-Za-z]+\d+[A-Za-z]+\b|python3|^[\s*_-]*\d{1,2}[.)]\s", " ", text)):   # B2B, D2C and python3 are not figures (auditor item 10)
        f.append("FIG")
    words = WORD.findall(re.sub(r"\[Name\]", "", text))
    names = [w for i, w in enumerate(words) if (w[0].isupper() and w.strip("'.") not in COMMON and (i > 0 or w in mid_caps))]
    if not names and LEAD_NAME.match(text.strip("*_ #>|-")) and words and words[0] not in COMMON:
        names = words[:1]   # a sentence that opens with a name and a verb: "Gartner has a policy ...", "SHRM is US-based"
    if names:
        f.append("NAME")
    if YOU.search(text) or YOU_US.search(text):
        f.append("YOU")
    if SEAT.search(text):
        f.append("SEAT")
    if ABSENCE.search(re.sub(r"(?i)\byou (?:did|do) ?n[o']t \w+|\bha(?:s|ve) no (?:source|link|date)\b", " ", text)) and "python" not in text.lower() and not re.match(r"[\s*_-]*(?:do not|don't|never)\b", text, re.I):
        f.append("ABS")   # an instruction ("Do not say ...") or a python note is not an absence claim (auditor item 8)
    if ATTR.search(text):
        f.append("ATTR")
    if SCRIPTREF.search(text):
        f.append("SCRIPT")
    return f


def is_group(text):
    """An unhedged sentence about how a group of people behaves (buyers, visitors, sellers, a role): its own source or a hedge (R34A-3)."""
    t = re.sub(r"^[\s*_>-]*(?:pass|fail|partial|keep|cut|change|verdict|why|reason)\s*:\s*", "", text.strip(), flags=re.I)
    t = re.sub(r"^[\s*_>-]*(?:\d{1,2}[.)]\s*)?", "", t)
    t = re.sub(r"\[[^\[\]]*\]", " ", t).strip()   # a [User to add: ...] slot is not a claim about users
    t = re.sub(r"(?:^|(?<=[\s(|]))['\"\u2018\u201c][^'\"\u2019\u201d]*\?['\"\u2019\u201d]", " ", t).strip()   # a quoted question (a probe) claims nothing (gate audit round 3, 4)
    clauses = [c.strip() for c in re.split(r";|,\s+(?:and|but|so|while|whereas|which|since|because)\s+|\s+(?:but|whereas|while|because|since)\s+", t) if c.strip()]
    if len(clauses) > 1:   # one hedged clause does not cover an unhedged one (research audit S6)
        return any(is_group(c) for c in clauses)
    return bool(t) and bool(GROUPN.search(t[:1] + TITLE.sub(" ", t[1:]))) and not HEDGE.search(t) and not IMPERATIVE.match(t) and not t.endswith("?")


def claim_units(files):
    allu = []
    for p in files:
        allu += units(read(p), os.path.basename(p))
    mid = set()
    for _, _, t, _ in allu:
        ws = WORD.findall(t)
        mid |= {w for w in ws[1:] if w[0].isupper() and w not in COMMON}
    claims = []
    for f, n, t, lab in allu:
        bare = t.strip("*_ ")
        if not lab and bare.endswith("?") and premise(bare):   # 1.0.5: a question's premise states a fact (EVL-1)
            t = bare = premise(bare)
        if lab or bare.endswith("?") or re.match(r"(?i)if\b", bare):
            continue
        fl = flags(t, mid)
        is_row = t.lstrip().startswith("|")
        if ((f, n, t) in GROUP_UNITS or (not is_row and is_group(t))) and "GROUP" not in fl:
            fl.append("GROUP")
        if fl:
            claims.append((uid(t), f, n, t, fl))
    return allu, claims


def lost_labels(allu, chat_name):
    chat = [(strip_labels(t), t) for f, n, t, lab in allu if f == chat_name and lab]
    errs = []
    for f, n, t, lab in allu:
        if f == chat_name or lab:
            continue
        key = strip_labels(t)
        if len(key) < 12:
            continue
        for ck, ct in chat:
            if len(ck) < 12:
                continue
            if ck == key or (len(ck) >= 25 and ck in key) or (len(key) >= 25 and key in ck) or difflib.SequenceMatcher(None, ck, key).ratio() >= 0.9:
                errs.append(f"LABEL LOST {f}:{n}: the chat answer marks this line ({ct[:90]}) but the saved file prints it with no label: {t[:120]}")
                break
    return errs


def unchecked_saved(files):
    """A file the answer names (.md, .txt, .csv) that exists next to the answer or one folder up, and is not in the check, is reported."""
    given = {os.path.realpath(p) for p in files}
    base = os.path.dirname(os.path.abspath(files[0]))
    errs, seen = [], set()
    for name in re.findall(r"[\w./\\~-]+\.(?:md|txt|csv)\b", read(files[0])):
        for root in (base, os.path.dirname(base), os.getcwd()):
            cand = os.path.realpath(os.path.join(root, os.path.expanduser(name)))
            if os.path.isfile(cand) and cand not in given and "claim-ledger" not in cand.split(os.sep) and cand not in seen:
                seen.add(cand)
                errs.append(f"SAVED FILE NOT CHECKED {name}: the answer names this saved file; add it to the check so its labels and lines are checked")
                break
    # a file saved in the working folder (the folder that holds claim-ledger/) in the 3 hours before the answer was written is a deliverable too
    if os.path.basename(base) == "claim-ledger":
        work, t0 = os.path.dirname(base), os.path.getmtime(files[0])
        for name in sorted(os.listdir(work)):
            cand = os.path.realpath(os.path.join(work, name))
            if (name.lower().endswith((".md", ".txt", ".csv")) and os.path.isfile(cand) and cand not in given and cand not in seen
                    and os.path.getmtime(cand) >= t0 - 3 * 3600):
                seen.add(cand)
                errs.append(f"SAVED FILE NOT CHECKED {name}: it was saved in the working folder in this session; add it to the check (a file only for a script goes in claim-ledger/)")
    return errs


def norm_url(u):
    u = u.strip().strip("<>").split("#")[0].lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")


def stem(w):
    w = w.lower().strip("'.-")
    for suf, rep in (("ies", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: len(w) - len(suf)] + rep
    return w


def content(s):
    s = re.sub(r"^[\s*_-]*[A-Za-z][\w ]{0,30}:\s", " ", s)   # an asset label such as "Short bio:" is not the user's claim
    return {stem(w) for w in WORD.findall(strip_labels(s)) if len(w) >= 3 and w.lower() not in STOP}


def numbers(s):
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", s)}


def nums(s):
    """Figures for the page checks: commas and leading zeros dropped ("07" is "7")."""
    out = set()
    for n in re.findall(r"\d[\d,]*(?:\.\d+)?", s):
        n = n.replace(",", "").rstrip(".")
        out.add(n.lstrip("0") or "0" if "." not in n else n.lstrip("0") or "0")
    return out


def flat(s):
    """Page text and quotes compared without case, markdown marks, curly quotes or line breaks."""
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2013", "-").replace("\u2014", "-")
    s = re.sub(r"[*_`\\]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def quoted(s):
    """Quoted phrases of three or more words in a line (straight or curly double quotes)."""
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return [q for q in re.findall(r'"([^"]+)"', s) if len(q.split()) >= 3]


SLOT = re.compile(r"\[(?:User|Local PR team|Principal) to add\b|\[Quote from\b", re.I)
SOURCELESS = re.compile(r"\b(?:names?|contacts?|e-?mails?|phones?|city|dateline|dates?|times?|time zone|prices?|pricing|costs?|budgets?|approv\w*|limits?|links?|urls?|"
                        r"embargo|signature|logos?|handles?|titles?|owners?|address|currency|headcount|list of|media list|sender|consent)\b", re.I)
ASSET = r"(?:full |whole |complete )?(?:spec|specification|emails?|email series|series|draft|release|press release|plan|asset|nurture|copy|brief|kit|post|outline|sequence|journey|deliverable)s?"
HELD = re.compile(r"\b(?:I(?:'ve| have)? held|I(?:'m| am) holding|I(?:'ll| will) hold|holding back|held back)\s+(?:back\s+)?(?:the |your |this |these )?" + ASSET + r"\b|"
                  r"\bI(?:'ll| will) (?:write|draft|build|send|give you|share) (?:the |your |these |this )?" + ASSET + r"\b[^.\n]{0,80}\b(?:once|after|when|as soon as) you (?:reply|answer|confirm|say yes)", re.I)
SECTION_OK = re.compile(r"open items?|questions?|next steps?|to add|missing|approvals?|before you|checklist|still needed|to fill|placeholders?|what I need|distribution", re.I)
TOOL_COMMENT = re.compile(r"^(?:the (?:page|site|website|homepage|article|content|text|footer|header|post|release|document|provided|fetched)\b|this (?:page|site|article|content)\b|"
                          r"based on\b|here (?:is|are)\b|i (?:could|can|did|found|cannot)\b|no (?:\w+ ){0,3}(?:is|are|was|were) (?:given|stated|listed|shown|named|provided|mentioned)\b|"
                          r"not (?:stated|given|listed|shown|mentioned)\b|there (?:is|are) no\b|it does ?n[o']t\b|unfortunately\b|note:|where the page\b|all statements below)", re.I)
TOOL_PHRASE = re.compile(r"\bthe (?:page|site|article|homepage|footer|content)(?: itself)? (?:does ?n[o']t|gives|lists|shows|says|names|mentions|states|labels|references|reads)\b|\bnot stated on the page\b|\bthe page gives no\b", re.I)


def slot_paragraphs(text):
    """Paragraphs (outside open items, questions and tables) that are only [User to add: ...] slots: THIN DRAFT (run 36A R36A-1)."""
    out, head = [], ""
    for para in re.split(r"\n\s*\n", text):
        for line in para.split("\n"):
            ls = line.strip()
            if ls.startswith("#") or re.fullmatch(r"\**[^*\[\]]{2,60}\**:?", ls):
                head = ls
        body = [l for l in para.split("\n") if l.strip() and not l.strip().startswith(("#", "|", "-", "*  ", ">")) and not re.match(r"\s*\d{1,2}[.)]\s", l)]
        if not body or SECTION_OK.search(head):
            continue
        b = " ".join(body)
        slots = [m for m in re.finditer(r"\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]", b) if SLOT.match(m.group(0))]
        if not slots:
            continue
        rest = re.sub(r"\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]", " ", b)
        rest = re.sub(r"^\s*\**[\w ]{1,30}:\**", " ", rest)   # a field label such as "Media contact:" is not drafted text
        if len(WORD.findall(rest)) >= 4:
            continue
        if all(SOURCELESS.search(" ".join(m.group(0).split()[:8])) and not re.search(r"(?i)quote|sentence|paragraph|why|what|how", m.group(0)) for m in slots):
            continue   # a name, contact, price or approval no source gives stays a slot
        out.append(b.strip()[:120])
    return out


def tool_comment(q, page_raw):
    """True when the quote sits in the web tool's own comment about the page, outside the page words the tool quoted (R36A-2)."""
    t = page_raw.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'")
    t = re.sub(r"[*_`\\]", "", t)
    t = re.sub(r"[ \t]+", " ", t).lower()
    fq = flat(q)
    i = t.find(fq)
    if i < 0:
        return False
    if t[t.rfind("\n", 0, i) + 1:i].count('"') % 2 == 1:   # inside a quoted span of the tool's answer, on that line: the page's own words
        return False
    start = max(t.rfind(". ", 0, i) + 2, t.rfind("\n", 0, i) + 1, t.rfind("? ", 0, i) + 2, t.rfind("! ", 0, i) + 2, 0)
    sent = t[start:i + len(fq) + 200].lstrip(" -*>")
    sent = re.sub(r"^[\w ]{1,40}:\s*", lambda m: m.group(0) if m.group(0).strip().lower() in ("note:",) else "", sent)   # a heading such as "Users protected:" before the sentence
    return bool(TOOL_COMMENT.match(sent) or TOOL_PHRASE.search(t[start:i + len(fq)]))


def premise(q):
    """The declarative premise of a question ("You own the site copy: is there ...?", "Since you run X, ...?"), or None (EVL-1)."""
    b = re.sub(r"^[\s*_>-]*(?:\d{1,2}[.)]\s*)?", "", q)
    m = re.match(r"(?i)(?:since|as|given that|because|now that)\s+([^,?]{8,}),", b)
    cand = m.group(1).strip() if m else None
    if not cand:
        m = re.match(r"([^?:;]{12,}?)[:;]\s+\S", b)
        if m and not m.group(1).rstrip().endswith("?") and len(m.group(1).split()) >= 3 and not re.match(r"(?i)(?:question|q\d|ask|probe|cross question|why|what|how|which|who|when|where|is|are|do|does|can|could|would|will|should|from|in|on|for|about|re|per|based on|one|two|three|first|second|third|next|before|after)\b", m.group(1).strip(" *_")):
            cand = m.group(1).strip()
    if not cand or cand.lstrip(" *_").startswith("[") or LINE_LABEL.search(cand) or "**" in cand or re.search(r"(?i)\b(?:which|what|how|who|whether|do you|does it|is there|are there|can you|could you|would you|will you)\b", cand):
        return None
    return cand


def entry_quotes(parts):
    """The quotes of a ledger entry: each | part that starts with a double quote; the outer quote marks are dropped."""
    out = []
    for x in parts:
        x = x.strip()
        if len(x) >= 2 and x[0] in "\"\u201c":
            x = x[1:]
            if x and x[-1] in "\"\u201d":
                x = x[:-1]
            out.append(x.strip())
    return out


def raw_text(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8-sig", errors="replace").replace("\r\n", "\n")


def digest(text):
    t = "\n".join(l.rstrip() for l in text.replace("\r\n", "\n").strip().splitlines())
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def word_stem(w):
    """price, prices, pricing -> pric; notes -> note (a stem keeps at least 4 letters; events audit round 2 N3)."""
    for suf in ("ies", "ing", "es", "ed", "s", "e", "y"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: len(w) - len(suf)]
    return w


def split_turns(q):
    """Split a quote at speaker turns; a cut inside a "Name, Role Words:" label (after its comma) is not a turn (gate audit round 3, 1)."""
    cuts = [0]
    for m in TURN.finditer(q):
        k = m.start()
        if k == 0:
            continue
        head = q[:k]
        c = head.rfind(",")
        if c >= 0 and re.fullmatch(r",(?: [A-Z][\w&.'-]*)+ ?", head[c:].rstrip() + " ") and "\n" not in head[c:]:
            continue
        cuts.append(k)
    cuts.append(len(q))
    return [q[a:b] for a, b in zip(cuts, cuts[1:])]


def speaker_terms(t):
    """The words naming who spoke, just before said, says, told and the like ("the CFO said" gives CFO)."""
    terms = set()
    for m in SPEECH.finditer(t):
        before = re.split(r"[:;,(|]", t[:m.start()])[-1]
        ws = WORD.findall(before)[-4:]
        terms |= {w.strip("'.").replace("'s", "") for w in ws if w[0].isupper() and w.strip("'.") not in COMMON}
        terms |= {x.group(0) for x in SEAT.finditer(before)}
        terms |= {x.group(0) for x in ROLE.finditer(" ".join(before.split()[-4:]))}   # lowercase roles: "the finance chief said" (research audit S5)
        if re.search(r",\s*$", t[:m.start()]):   # "..., said Dev Patel": the speaker comes after the verb (gate audit round 3, 6)
            after = re.split(r"[.;:(|]", t[m.end():])[0]
            terms |= {w.strip("'.").replace("'s", "") for w in WORD.findall(after)[:4] if w[0].isupper() and w.strip("'.") not in COMMON}
            terms |= {x.group(0) for x in SEAT.finditer(after)}
    return {x for x in terms if x}


def attribution_errors(where, t, quotes, page):
    """R34A-1: who said, reported, ran or owns what must be in the saved page text, in one quote with the figure or quoted words."""
    errs = []
    if not quotes:
        return [f"ATTRIBUTION {where}: the line says who said, reported, ran or owns something; add the page's own words as a quote: <id> | page | <url> | \"<words from the page>\""]
    fq = [flat(q) for q in quotes]
    for q, f in zip(quotes, fq):
        if NEG_ATTR.search(q):
            errs.append(f"ATTRIBUTION {where}: the quote \"{q[:80]}\" says the source is not given, so it cannot support who said or ran it; say the page does not name the source, or leave the attribution out")
    keys = [("fig", k) for k in nums(re.sub(r"\b(?:19|20)\d\d\b", " ", t))] + [("q", flat(x)) for x in quoted(t)]
    need = {flat(x.group(0)) for x in ATTR_NOUN.finditer(t)} | {flat(x.group(0)) for x in SCOPE.finditer(t)} | {flat(x) for x in speaker_terms(t)}
    for m in AGENT2.finditer(t):   # "according to Forrester", "reported by Bain": that source is in the quote with the figure (research audit round 2 N3)
        words = []
        for w in m.group(1).split():
            w = w.strip(",.;:)(\"")
            if not w or AGENT_END.match(w) or not w[0].isupper():
                break
            words.append(w)
        need |= {flat(w.replace("'s", "")) for w in words if w.lower() not in STOP and len(w) > 1}
    for m in AGENT.finditer(t):   # "a survey by the show's organiser": who ran it must be on the page with the figure (events audit G2)
        words = []
        for w in m.group(1).split():
            w = w.strip(",.;:)(")
            if not w or AGENT_END.match(w):
                break
            words.append(w)
        need |= {flat(w.replace("'s", "")) for w in words if w.lower() not in STOP and len(w) > 2}
    def has(f, term):
        return re.search(r"(?<![a-z0-9])" + re.escape(term.rstrip("s")) + r"[a-z]{0,3}(?![a-z0-9])", f) is not None

    def holds_key(f):
        return not keys or any((k in nums(f)) if kind == "fig" else (k in f) for kind, k in keys)
    segs = []   # one speaker turn per segment: a quote holding two turns credits nothing across them (events audit G1)
    for q in quotes:
        parts = [x for x in split_turns(q) if x.strip()]
        segs += [flat(x) for x in parts] if len(parts) > 1 else [flat(q)]
    ok = [f for f in segs if holds_key(f) and all(has(f, n) for n in need) and not NEG_ATTR.search(f)]
    if not ok:
        what = ("its figure or quoted words" if keys else "") + (" and " if keys and need else "") + (", ".join(sorted(need)) if need else "")
        errs.append(f"ATTRIBUTION {where}: no quote from the saved page holds {what or 'the attribution'} together; quote the words that say it, "
                    "or change the line to say only what the page says (for example \"the page does not name who ran the survey\")")
    return errs


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace", newline="\n")
    except (AttributeError, ValueError):
        pass
    if len(argv) < 2 or argv[0] not in ("list", "check"):
        print(__doc__)
        return 2
    mode, rest = argv[0], [a for a in argv[1:] if a != "--final"]
    final = "--final" in argv[1:]
    if final and mode != "check":
        print("bad input: --final goes with check")
        return 2
    opts = {"--ledger": [], "--opened": [], "--prompt": [], "--script-out": [], "--page": []}
    files, cur = [], None
    for a in rest:
        if a in opts:
            cur = a
        elif a.startswith("--"):
            print(f"bad input: unknown option {a}")
            return 2
        elif cur:
            opts[cur].append(a)
            if cur not in ("--script-out", "--page"):
                cur = None
        else:
            files.append(a)
    if cur and not opts[cur]:
        print(f"bad input: {cur} needs a file")
        return 2
    if not files:
        print("bad input: give the chat answer file first, then each saved file")
        return 2
    for p in files + sum(opts.values(), []):
        if not os.path.isfile(p):
            print(f"bad input: no such file {p}")
            return 2
    if not read(files[0]).strip():
        print("bad input: the answer file is empty; write the answer you will deliver first")
        return 2
    GROUP_UNITS.clear()
    allu, claims = claim_units(files)
    errs = lost_labels(allu, os.path.basename(files[0]))
    errs += unchecked_saved(files)
    report = [f"CLAIM LEDGER {mode}: {len(files)} file(s), {len(allu)} lines read, {len(claims)} need a source"]
    slot_line = []
    for p in files:   # 1.0.5: slots counted per file; a draft left mostly as slots, or held back, fails (R36A-1)
        body = read(p)
        slot_line.append(f"{os.path.basename(p)} {len(SLOT.findall(body))}")
        thin = slot_paragraphs(body)
        if len(thin) >= 3:
            errs.append(f"THIN DRAFT {os.path.basename(p)}: {len(thin)} paragraphs are only [User to add: ...] slots (first: {thin[0][:90]}); draft each from the user's words and "
                        "the opened pages as [Draft for you to confirm: ...] (no new figure, name, customer or result), and keep a slot only for what no source gives "
                        "(a name, a contact, a price, a date, an approval)")
        for ln in body.splitlines():
            if HELD.search(ln):
                errs.append(f"HELD BACK {os.path.basename(p)}: \"{ln.strip()[:100]}\": deliver the asset now, under your questions, as a marked draft that the answers can change")
                break
    report.append("SLOTS: " + ", ".join(slot_line))
    for c in claims:
        report.append(f"{c[0]}  [{','.join(c[4])}]  {c[1]}:{c[2]}  {c[3][:160]}")
    if mode == "list":
        print("\n".join(report))
        for e in errs:
            print(e)
        print("Next: write the ledger (one line per id: <id> | user|page|script|notes|general|absence|self | detail), or turn a line into a"
              " label or a [User to add: ...] slot, then run check (check with an empty ledger prints a skeleton to fill in).")
        return 1 if errs else 0
    if not opts["--ledger"]:
        print("bad input: check needs --ledger (an empty file prints a skeleton)")
        return 2
    opened = {}
    for p in opts["--opened"]:
        for line in read(p).splitlines():
            if line.strip() and not line.startswith("#"):
                url, _, chk = line.partition("|")
                words = [w.strip().lower() for w in re.sub(r"(?i)^\s*checked:\s*", "", chk).split(",") if w.strip()]
                opened.setdefault(norm_url(url), set()).update(words)
    pages = {}
    for p in opts["--page"]:
        head, _, body = read(p).partition("\n")
        u = re.findall(r"https?://\S+|\S+\.\S+", head)
        if not u or not body.strip():
            errs.append(f"PAGE TEXT {os.path.basename(p)}: put the page's URL on the first line and the text the tool returned after it")
            continue
        pages[norm_url(u[0])] = pages.get(norm_url(u[0]), "") + "\n" + body
    flat_pages = {k: flat(v) for k, v in pages.items()}
    for u in sorted(opened):
        if u not in pages:
            errs.append(f"PAGE TEXT MISSING {u}: save the text this page returned (its URL on the first line) and pass it with --page; every opened page needs its saved text")
    prompt = "\n".join(read(p) for p in opts["--prompt"])
    psents = [content(s) for s in re.split(r"(?<=[.!?])\s+|\n+", prompt) if s.strip()]
    script_out = "\n".join(read(p) for p in opts["--script-out"])
    known = nums(prompt + " " + script_out + " " + " ".join(pages.values()))
    for p in files:   # 1.0.5: a figure inside a drafted line comes from the user, a saved page or a script (DRAFT FIGURE)
        for m in re.finditer(r"\[(?:draft|suggested)[^\[\]:]{0,60}:(?:[^\[\]]|\[[^\[\]]*\])*\]", read(p), re.I):
            miss = nums(re.sub(r"\b[A-Za-z]+\d+[A-Za-z]*\b|^\[\w[^:]*:|\b(?:[Qq]uestion|[Ss]tep|[Ii]tem|[Pp]oint|[Oo]ption|[Rr]ow|[Pp]art|[Ss]ection|[Ee]mail|[Qq]uote|[Pp]hase|[Ww]ave|[Tt]ouch|[Ss]tage|[Nn]o\.|#)\s*\d{1,2}\b", " ", m.group(0))) - known
            if miss:
                errs.append(f"DRAFT FIGURE {os.path.basename(p)}: {', '.join(sorted(miss))} in \"{m.group(0)[:90]}\" is in no user message, saved page or script output; a draft uses only figures a source gives")
    entries = {}
    for n, line in enumerate(read(opts["--ledger"][0]).splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = [x.strip() for x in line.split("|")]
        if len(parts) < 2:
            errs.append(f"LEDGER line {n}: needs <id> | <source> | <detail>")
            continue
        for i in re.split(r"[,\s]+", parts[0]):
            if i:
                if i in entries:
                    errs.append(f"DUPLICATE {i}: ledger lines {entries[i][2]} and {n} both give a source; keep one")
                entries[i] = (parts[1].lower(), parts[2:], n)
    by_id = {c[0]: c for c in claims}
    if not entries and claims:
        errs.append(f"LEDGER EMPTY: {len(claims)} line(s) need a source; fill in the skeleton below")
        report.append("LEDGER SKELETON (copy into the ledger file, give each line its source and detail, delete nothing you keep in the text):")
        for i, (_, f, n, t, fl) in by_id.items():
            hint = ("absence | <word> | <url>" if "ABS" in fl else "page | <url> | \"<words from the saved page>\"" if "ATTR" in fl
                    else "general (hedge the line) or page | <url> | \"<quote>\"" if "GROUP" in fl else "user|page|script|notes|general|self | <detail>")
            report.append(f"# [{','.join(fl)}] {f}:{n} {t[:100]}")
            report.append(f"{i} | {hint}")
    for i in entries:
        if i not in by_id:
            errs.append(f"STALE {i}: no line of the text has this id now (the text changed after the list, or the id is wrong); run list again")
    for i, (_, f, n, t, fl) in by_id.items():
        if i not in entries:
            if entries:
                errs.append(f"NO SOURCE {i} {f}:{n}: {t[:120]}")
            continue
        src, detail, ln = entries[i]
        where = f"{i} {f}:{n}"
        if "ABS" in fl and src != "absence":
            errs.append(f"ABSENCE {where}: an absence claim needs an absence entry naming the word and the pages checked for it")
            continue
        if src == "user":
            if not prompt:
                errs.append(f"BAD INPUT {where}: source user needs --prompt with the user's message")
                continue
            miss = numbers(t) - numbers(prompt)
            if miss:
                errs.append(f"USER FIGURE {where}: {', '.join(sorted(miss))} is not in the user's message")
            if re.search(r"\bnot\b|n't\b|\bnever\b|\bno\b", t, re.I) and not re.search(r"\bnot\b|n't\b|\bnever\b|\bno\b", prompt, re.I):
                errs.append(f"USER NEGATION {where}: the line says not or never and the user's message never does; use the user's words")
            cw = content(t)
            best = max((len(cw & ps) / max(1, len(cw)) for ps in psents), default=0)
            if cw and best < 0.75:
                errs.append(f"USER WORDS {where}: only {best:.0%} of this line's words (75% needed) are in any one sentence the user wrote; use the user's own words, or mark it [Draft for you to confirm: ...]")
        elif src == "page":
            urls = re.findall(r"\S+", detail[0]) if detail else []
            quotes = entry_quotes(detail[1:])
            if not urls:
                errs.append(f"PAGE {where}: name the opened page")
            text = ""
            for u in urls:
                if norm_url(u) not in opened:
                    errs.append(f"NOT OPENED {where}: {u} is not in the list of pages opened in this session; label the line or leave it out")
                elif norm_url(u) not in pages:
                    errs.append(f"PAGE TEXT {where}: {u} has no saved page text; pass the text it returned with --page")
                else:
                    text += " " + flat_pages[norm_url(u)]
            if not text:
                continue
            raw_pages = " \n".join(pages[norm_url(u)] for u in urls if norm_url(u) in pages)
            for q in quotes:
                if len(flat(q)) > 240:
                    errs.append(f"QUOTE {where}: the quote \"{q[:60]}...\" is longer than 240 characters; quote only the words that say it")
                elif flat(q) not in text:
                    errs.append(f"QUOTE {where}: \"{q[:100]}\" is not word for word in the saved page text")
                elif tool_comment(q, raw_pages):
                    errs.append(f"TOOL COMMENT {where}: \"{q[:100]}\" is the web tool's comment about the page, not the page's own words; quote the words the page shows (in the tool's quotation marks), or say \"the fetch result says ...\" without quote marks")
            for q in quoted(t):
                if flat(q) in text and tool_comment(q, raw_pages):
                    errs.append(f"TOOL COMMENT {where}: the line puts \"{q[:80]}\" in quote marks, but it is the web tool's comment, not the page's words; quote the page, or write it as what the fetch result says")
            figs = re.sub(r"https?://\S+|\]\([^)]*\)|\b[\w-]+\.(?:com|in|io|ai|org|co|net)\S*", " ", t)   # digits in a link are not figures (research audit S4)
            figs = re.sub(r"(?i)\b(?:fetched|checked|opened|accessed|retrieved|read|as of)\b(?: on)?\s+\d{1,2}\s+[A-Za-z]{3,9}\.?\s+\d{4}", " ", figs)   # a fetch date (S2)
            figs = re.sub(r"^\s*\|\s*[A-Za-z0-9]{1,4}\s*\|", "|", figs)   # a row number or id in the first cell (S3)
            figs = re.sub(r"^[\s*>-]*(?:\d{1,2}[.)]|(?i:step|item|point|row|part|option)\s+\d{1,2}[.:)])\s+|\[\d{1,2}\]", " ", figs)   # list and citation markers (gate audit round 3, 3)
            miss = nums(re.sub(r"\b[A-Za-z]+\d+[A-Za-z]*\b", " ", figs)) - nums(text) - nums(" ".join(q for q in quoted(t) if flat(q) in flat(prompt)))   # the user's own words quoted back in a correction row (S1; round 2 N2: only inside such a quote)
            if miss:
                errs.append(f"NOT ON PAGE {where}: {', '.join(sorted(miss))} is not in the saved page text; copy the page's figure, or say where it comes from")
            for q in quoted(t):
                if flat(q) not in text and flat(q) not in flat(prompt):
                    errs.append(f"NOT ON PAGE {where}: the quoted words \"{q[:80]}\" are not in the saved page text; quote the page word for word")
            pflat = text + " " + flat(prompt)   # events audit G2: a name in a page line is on that page (or in the user's message)
            gone = set()   # round 2 N1: the first word of a sentence or a cell, a role, a status word and a question word are not names
            for m in re.finditer(r"[A-Za-z][A-Za-z0-9&'.\-]*", re.sub(r"[\w'.-]+\**:", " ", figs)):
                w = m.group(0).replace("'s", "").strip("'.")
                before = figs[:m.start()].rstrip(" *_\"'(")
                opens_claim = re.match(r"(?:'s)?\s+(?:has|have|is|was|are|were|sells|sold|says|said|offers|serves|served|ranks|provides|makes|runs|ran|owns|reported|reports|"
                                       r"found|finds|claims|lists|launched|raised|uses|named|won|bought|acquired|grew|employs|notes|noted)\b", figs[m.end():])
                if (not w or not w[0].isupper() or len(w) < 2 or w in COMMON or (not opens_claim and (not before or before[-1] in "|.?!:;(\"")) or SEAT.fullmatch(w) or ROLE.fullmatch(w)
                        or w.lower() in ("verified", "unverified", "corrected", "contradicted", "primary", "secondary", "none", "pass", "fail", "partial", "deny", "accept", "modify")):
                    continue
                if not re.search(r"(?<![a-z0-9])" + re.escape(flat(w)) + r"(?![a-z0-9])", pflat):
                    gone.add(w)
            gone = sorted(gone)
            if gone:
                errs.append(f"NOT ON PAGE {where}: {', '.join(gone)} is not in the saved page text or the user's message; a line about a company or a person names only what the page shows")
            if "ATTR" in fl:
                errs += attribution_errors(where, t, [q for q in quotes if flat(q) in text], text)
            if "GROUP" in fl and "FIG" not in fl and "NAME" not in fl:
                cw = content(t)
                if not any(len(cw & content(q)) >= 0.5 * max(1, len(cw)) for q in quotes if flat(q) in text):
                    errs.append(f"GROUP {where}: a line about how a group of people behaves needs a quote from the page that says it (half its words); or hedge it (may, often, worth checking)")
        elif src == "script":
            miss = numbers(t) - numbers(script_out)
            if not script_out:
                errs.append(f"BAD INPUT {where}: source script needs --script-out with the script's printed output")
            elif miss:
                errs.append(f"SCRIPT FIGURE {where}: {', '.join(sorted(miss))} is not in the script output; copy the script's figure and its meaning exactly")
            elif script_out:
                fo = flat(script_out)
                qs = [q for q in quoted(t) + [x for x in re.findall(r'"([^"]+)"', t) if len(x.split()) < 3]]
                for q in entry_quotes(detail):
                    if flat(q) not in fo:
                        errs.append(f"SCRIPT {where}: \"{q[:80]}\" is not a printed line of the script output")
                if not any(flat(q) in fo for q in qs):
                    words = lambda x: {stem(w) for w in WORD.findall(strip_labels(x)) if len(w) >= 3 and w.lower() not in STOP}
                    cw = {w for w in words(t) if w not in GENERIC and not w.endswith(".py")}
                    best = max((len(cw & words(l)) / max(1, len(cw)) for l in script_out.splitlines() if l.strip()), default=0)
                    if cw and best < 0.5:
                        errs.append(f"SCRIPT WORDS {where}: only {best:.0%} of this line's words are in one printed line of the script; copy the printed line in quotes (\"Claims to check: 0\") and say only what it means")
        elif src == "notes":
            ref = (detail[0] if detail else "").strip()
            if not ref or not os.path.isfile(os.path.join(HERE, "..", "references", os.path.basename(ref))):
                errs.append(f"NOTES {where}: name a file in this skill's references folder")
            elif not (HEDGE.search(t) or re.search(r"\bnotes?\b", t, re.I)):
                errs.append(f"NOTES {where}: a general line from the sector notes is hedged (often, may, worth checking) or names the notes")
        elif src == "general":
            if "NAME" in fl or "YOU" in fl:
                errs.append(f"GENERAL {where}: names a company, a person or the user, so it is not general; give its source, label it, or leave it out")
            elif not HEDGE.search(t) or is_group(t):
                errs.append(f"GENERAL {where}: a general claim about how people or companies behave needs hedged wording (often, may, worth checking) in every clause")
        elif src == "absence":
            if "ABS" not in fl:
                errs.append(f"ABSENCE {where}: the line states no absence")
                continue
            word = detail[0].strip().lower() if detail else ""
            urls = re.findall(r"\S+", " ".join(detail[1:]))
            if not word or not urls:
                errs.append(f"ABSENCE {where}: give the word and the pages: <id> | absence | <word> | <url> <url>")
                continue
            if word.lower() not in t.lower():
                errs.append(f"ABSENCE {where}: the word '{word}' is not in the line; the entry must name the word the line says is missing")
            for u in urls:
                if norm_url(u) not in opened:
                    errs.append(f"NOT OPENED {where}: {u} is not in the list of opened pages")
                elif word not in opened[norm_url(u)]:
                    errs.append(f"NOT CHECKED {where}: {u} was opened but not checked for '{word}'; name only the pages checked for it")
                elif norm_url(u) not in pages:
                    errs.append(f"PAGE TEXT {where}: {u} has no saved page text; pass the text it returned with --page")
                elif re.search(r"(?<![a-z0-9])" + re.escape(word_stem(flat(word))) + r"[a-z]{0,4}(?![a-z0-9])", flat_pages[norm_url(u)]):
                    errs.append(f"ABSENCE {where}: '{word}' is ON THE PAGE in the saved text of {u}; the line is wrong, so change or remove it")
            if re.search(r"\banywhere\b|\bnowhere\b|whole site|entire site|across the site|the site does", t, re.I):
                errs.append(f"ABSENCE {where}: the line speaks for the whole site; name only the pages checked for '{word}'")
            for u in urls:   # 1.0.5: the user's own text saved as a page: name the closest line found (SOR-1)
                if not re.match(r"(?i)https?://", u) and re.search(r"\.(?:txt|md)$", u, re.I) and norm_url(u) in pages:
                    ut = flat(pages[norm_url(u)])
                    if not any(flat(q) in ut and len(q.split()) >= 3 for q in quoted(t)) and not re.search(r"(?i)nothing in (?:it|your [\w ]{1,20}) comes (?:near|close)|no line (?:in|of) (?:it|your [\w ]{1,20}) comes (?:near|close)", t):
                        errs.append(f"CLOSEST MATCH {where}: the line says '{word}' is not in the user's own text ({u}); quote the closest line you found in it "
                                    "(\"the closest line is \\\"...\\\"\") and judge that line, or say plainly that nothing in it comes near")
            if not re.search(r"pages? (?:I|we) (?:opened|checked|read)|https?://|\b[a-z0-9-]+\.(?:com|in|io|ai|org|co|net)\b|\byour (?:draft|paste|text|post|note|notes|message|copy|brief|list|file|deck)\b|\byou pasted\b", t, re.I):
                errs.append(f"ABSENCE {where}: the line must name the pages it checked (for example 'on the pages I opened: home, about')")
        elif src == "self":
            if (not re.match(r"[*_\s-]*(?:I|I've|I'd|I'll|I'm)\b", t) or "YOU" in fl or "SEAT" in fl or "GROUP" in fl or re.search(r"\byour\b", t, re.I)
                    or "FIG" in fl and not re.search(r"\b(?:left out|kept out|removed|dropped|did not use|didn't use|counted|ran|checked)\b", t)):
                errs.append(f"SELF {where}: source self is only for a line that says what this answer did (it starts with I), not a fact about the user, their team, a role or a group")
        elif src == "search":
            errs.append(f"SEARCH ONLY {where}: label it \"from a search result, page not opened\" in every place it appears, or leave it out")
        else:
            errs.append(f"LEDGER line {ln}: unknown source '{src}' (user, page, script, notes, general, absence, self)")
    report += errs
    texts = [(p, raw_text(p)) for p in files]
    for p, t in texts:
        report.append(f"digest {p}: {digest(t)}")
    short = ", ".join(f"{os.path.basename(p)}={digest(t)}" for p, t in texts)
    if errs:
        report.append(f"LEDGER FAIL: {len(errs)} problem(s). Fix the text or the ledger, then run check again; deliver only text that passed.")
    else:
        report.append(f"LEDGER PASS: {len(claims)} line(s) traced, labels kept in every saved file.")
    report.append(f"claim_ledger: {len(errs)} problem{'' if len(errs) == 1 else 's'}; digests {short}")
    if final:
        name, text = texts[0]
        d = digest(text)
        if errs:
            report.insert(0, f"claim_ledger --final: NOT DELIVERABLE, {len(errs)} to fix")
            report.append("NOT DELIVERABLE: fix every problem above, then run check --final again as your last tool call.")
        else:
            report.insert(0, f"claim_ledger --final: PASS, reply digest {d}")
            body = "\n".join(l.rstrip() for l in text.strip().splitlines())
            saved = "; ".join(f"{os.path.basename(p)} ({digest(t)})" for p, t in texts[1:]) or "none"
            report.append(f"DELIVER: send as your whole chat reply exactly the text between the two marker lines below (the checked {os.path.basename(name)}), "
                          f"with nothing before or after it and no word changed. Saved files checked: {saved}. To change anything, edit the file and run check --final again.")
            report += [f"=== BEGIN CHECKED REPLY {d} ===", body, f"=== END CHECKED REPLY {d} ==="]
    elif not errs:
        report.append("Next: run the same command with --final as your very last tool call, and send exactly the text it prints between its BEGIN and END lines.")
    print("\n".join(report))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
