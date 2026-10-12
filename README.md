# B2B Research: Market and Account

Research skills for B2B teams, built by Shashwat Ghosh, Helix GTM Consulting. This version does not size markets or build TAM, SAM and SOM.

- **account-research**: target account lists, list audits and enrichment in fixed fields, and a one account brief in TOPS order (technographics, organisation, person, situation) with a probe question for every finding, verified and unverified lists, and every account on the list covered.
- **evidence-research-asset**: post series, briefs, reports, benchmarks, white paper outlines and case studies where every number is checked against the publisher's own topline and locked across every asset, plus a three lens white paper review.
- **claims-fact-check**: a claims register for every claim in a post, deck or release, fixes only what is wrong, screenshot mode, a personal data check on every image, and a date and weekday check.
- **second-opinion-review**: another model's or a colleague's critique judged point by point through three filters (facts, your objectives, tone), four verdicts, and one final version.

Version 1.0.0. More plugins by Helix GTM Consulting: https://tools.gtmhelix.com/plugins/

## Install

```bash
# Add this repository as a marketplace
claude plugin marketplace add shashwatgtm/b2b-research-market-and-account

# Install the plugin
claude plugin install b2b-research-market-and-account@b2b-research-market-and-account
```

## Quick start

"Brief me on this account before Thursday's call with their head of IT."

"Turn this threat report into a five post series for plant IT heads."

"Fact check this post before I publish it."

"Another AI assistant reviewed my draft. Which of its points should I take?"

## Examples

The worked examples inside the skills use real companies (Unicommerce, Quick Heal Technologies and its Seqrite division, and Zoho) only as examples, with every company fact quoted from a page fetched on 11 or 12 October 2026 and every figure a user supplies labelled hypothetical. No real employee of those companies is described.

## Privacy

This plugin sends no data to Helix GTM Consulting and runs no server. The plugin itself stores nothing: it keeps no account, no log and no copy of your work, and any file Claude writes for you goes only to your own working folder. The skills run inside Claude. When web tools are available, they open public pages such as company filings, company websites, published reports and platform help pages; they read about a person only through that person's own public professional statements, each with link and date, label any personality note as an inference, never collect health, religion, politics, family, private life, home or personal contact details, and use the result for meeting preparation only. The small Python scripts in the skills run on files or text you give them, use no network, and write no files. What you type into Claude is handled under your own Claude account terms.

## Security

To report a security problem, email shashwat@gtmhelix.com with the subject "Security report: b2b-research-market-and-account". Please do not open a public issue for it.

## License

MIT. See [LICENSE](LICENSE).
