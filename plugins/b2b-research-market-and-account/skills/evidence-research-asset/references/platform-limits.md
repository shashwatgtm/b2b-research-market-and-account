# Checking each platform's paste and render limits before writing

Limits change, and an assumption here breaks the asset at the last step. This file holds no limit values on purpose.

## Before writing for a platform
1. Name every platform the asset will go to (for example a newsletter tool, LinkedIn, a company blog, a slide tool, a PDF, a knowledge base page).
2. For each, open the platform's own help or documentation page in this session and record, with the link and date:
   - whether pasted Markdown renders, or is shown as raw symbols, or is stripped;
   - which formatting survives a paste (headings, bold, tables, line breaks, links);
   - character or word limits for the field the text goes into (post body, title, description, image text alternative, comment);
   - image sizes, file types and file size limits, and whether images in comments carry text alternatives;
   - whether tables are supported, and what to use instead if not (an image of the table with full text alternative, or prose).
3. If the help page cannot be opened, say so, run a web search for the limit's wording, show any result labelled "from a search result; the page itself was not opened", and ask the user to confirm what the platform accepts, or ask them to paste a test and report what they see. Never assume a limit or that Markdown renders.

## While writing
- Count characters and words with code (for example Python's len() on the exact text) where code execution is available, never by estimate, where a limit applies. Without code execution, count by hand and say the count was manual.
- Give each platform its own version in its native shape; do not paste one platform's format into another.
- Keep links where the platform's norms and the user's rules put them (for example, the user's rule may keep links out of a post body).

## After writing
- Record per asset: platform, limit checked (with link), the count, within or over.
- If the user pastes and reports a rendering problem, fix that asset only.
