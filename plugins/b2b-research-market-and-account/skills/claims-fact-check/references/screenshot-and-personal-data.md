# Screenshot mode, the personal data check, and AI visibility claims

## Screenshot mode
Use when the user gives images (screenshots, photos of slides, exported charts) as the evidence for a post or document, or says "state facts from the images only".
1. List each image with a short description of what is visible (title, page, tool, date shown).
2. For every claim in the final text, name the image that shows it, and quote what the image shows. A claim an image shows is "shown in Image N, as pasted, not yet checked", never verified, unless the source in the image was also opened in this session.
3. List the claims that no image shows.
4. For each unshown claim, name the screenshot that would prove it (for example "the paragraph of the release that states the customer count, with its date visible").
5. State facts from the images only. If the text says something the images do not show, it is unshown, even if the skill believes it to be true.
6. Text must match the images: if the text says "three companies" and the images show two, flag it. Check the order of images against any times or sequence the text describes.
7. Anything the user blurred, cropped or removed from an image is not mentioned in the text, the comments or the image text alternative.

## Personal data check (on every image, every time)
Look for, and list with where each sits in the image:
- names of people who are not the subject of the post, and their photos;
- email addresses, phone numbers, postal addresses;
- usernames, account ids, profile pictures in sidebars;
- file paths and folder names (they can show usernames, client names or internal structure);
- internal links, dashboard URLs, ticket numbers, document ids;
- customer or client names, deal values, prices that are not public;
- tokens, keys, passwords, QR codes;
- browser tabs, notifications and chat previews visible at the edges.
For each, suggest crop or blur. If nothing is found, say "none found" for that image; never skip the check.

## AI visibility claims
Claims such as "another AI assistant recommends us first" or "an AI search engine cites our page" are true only for a specific query, engine, date and setting.
- They are verified only by running the query on the live engine and keeping the screenshot (query text, engine, date and time, signed in or not, region if shown).
- If the skill can run the engine through the tools available, it runs the exact query and reports the result with the screenshot or the full answer text.
- If it cannot, the claim stays unverified, and the answer gives the exact query for the user to run and the screenshot to keep.
- A screenshot the user sends of their own engine test is "as pasted, not yet checked", never verified by the skill: the text may then report it as the user's own dated test ("In a test on [date], [assistant name] listed ..."), with the query and settings shown.
- The claim is written at the strength of the test: "In a test on [date], [engine] listed us first for the query '[query]'", never "AI recommends us".
