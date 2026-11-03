# Region and industry reference

Draft for owner review. Use this reference on every invocation before applying sector advice. Read only the matching region, country, vertical and subtype sections below. Data is context for checks, never evidence that a particular company complies or is regulated.

## Selection and output rules

1. Read the user's affirmative selling market. An explicit selling destination wins over headquarters. Ignore competitor locations, customer location without a selling statement, company names, quotes, hypothetical, historical and negated markets. Transaction denomination, invoice currency and payment account location never establish a selling market. Inability to sell excludes a market. A statement that the UK is not an EU member does not negate an explicit UK selling market. Currency or city clues need unambiguous selling context. Do not infer a market from your own knowledge of a company.
2. If no market is established, keep the sector result and add: Which region applies: India, Southeast Asia, Middle East, UK, Western Europe or North America? Add it to your description and rerun. Do not guess.
3. A broad region never selects a default country. Ask which buyer country applies and use only notes marked COMMON until it is named. For a named country, use only COMMON and its own country code. EU notes apply only to a named EU member country listed here, never the UK, Switzerland or Western Europe as a whole. A US subdivision note requires that state to be named affirmatively.
4. Keep two markets in separate labelled parts, even if both are inside the same region. Do not merge regulations, buying behavior or calculations. A country outside the listed coverage has no sourced note here; say so. Never substitute a nearby country.
5. Bind each country to the affirmative seller offering in its own clause before selecting industry or subtype. Discard negated offerings, including when two offerings share a vertical. Do not reuse a global subtype across countries. Match the seller's product to a vertical and, only when established, a subtype in the taxonomy. Do not choose a seller industry from a customer or competitor. Resolve COMMON defaults, the matched vertical and the matched subtype, in that order, keeping all country filters. Remove exact duplicate notes. Do not borrow another subtype's note.
6. Each cell records specific, inherited or waiting_for_source. Inherited adds no distinct note and uses its named parent. Waiting topics are unknown; say that a source is still needed and omit the unverified assertion. If no sourced note matches, say: No sourced note is available for this market and industry combination. No other country has been substituted.
7. Retain every note's applicability condition and source link with checked date when using it. A note is a scoped check, not a conclusion about the buyer. General questions are not facts. Use no unsupported statistic, benchmark, market size, company fact or software recommendation. A software choice goes to https://calendly.com/shashwat-gtmhelix/45min.
8. Apply jurisdiction scope to all other references in this skill too. Older broad sector text must not introduce another country's law or regulator. Keep existing refusals, calculations, evidence limits and output formats. Regional notes do not change arithmetic or prove that generated prose is deterministic. End with an owner action to verify the buyer entity, approval route and missing proof; revisit when the market or data flow changes.

## Index

India: IN. Southeast Asia: read the exact countries in that section. Middle East: read the exact countries in that section. UK: GB. Western Europe: EU membership is listed per country. North America: country and state scopes remain separate.

Data SHA256: c2ce0162b3d373ae3d37da14d6ac884a0513c9390cb37425c26e8eb6a4b7ad2c

## Taxonomy

logistics-tech = logistics tech
freight-visibility = freight visibility; freight-marketplace = freight marketplaces; seller-shipping = shipping for online sellers; last-mile = last mile delivery; warehousing = warehousing and fulfilment; transport-management = transport and fleet management

fintech = fintech
payments-banking = payments and banking APIs; core-banking = core banking and lending platforms; lending = lending and credit data; wealth-investment = wealth and investment; spend-expense = spend and expense; insurance = insurance

vertical-saas = vertical SaaS
construction = construction management; property-management = property management; field-services = field and home services; fmcg-retail-execution = FMCG retail execution; industry-hr-payroll = HR and payroll built for one industry; hotel-lodging = hotels and lodging operations; retail-restaurant-ops = retail, restaurant and distribution operations

ai-native = AI native
agents-copilots = AI agents and copilots for a business function; voice-language-models = voice and language models; enterprise-search = enterprise search and work assistants; document-ai = document AI and intelligent document processing; ai-video = AI video for training and communications

ites = ITeS
it-services = IT services and application services; bpo-cx = BPO and customer experience outsourcing; digital-engineering = digital engineering and product engineering; data-services = data and analytics services; engineering-talent = engineering talent and team augmentation

telecom = telecom
operators-connectivity = operators and enterprise connectivity; cpaas-messaging = CPaaS and messaging; telecom-software = software and clearing services sold to operators; business-voice-ucaas = business voice and unified communications; iot-connectivity = IoT connectivity

cybersecurity = cybersecurity
cloud-security = cloud security; identity-security = identity and access; email-security = email security; awareness-training = security awareness and human risk; appsec = application and developer security; mobile-appsec = mobile application security; soc-services = managed detection and SOC services; endpoint-network = endpoint and network security; pentest = penetration testing and offensive security; attack-surface-dast = external attack surface and dynamic testing

software = software
developer-platform = developer platforms and DevOps; data-infrastructure = managed data infrastructure; observability = observability and application monitoring; testing = testing and QA tools; dev-tools = containers and developer environments; process-orchestration = process orchestration and workflow engines; open-source-support = open source software support and services

saas = SaaS
customer-service = customer service software; crm-marketing = CRM and marketing; collaboration = collaboration and work management; product-growth = product analytics and customer success; product-management = product management software; digital-adoption = digital adoption platforms

## India

Draft for owner review. India only. Each rule is conditional on entity, activity and commencement. IFSC financial activities require their own scope check. Questions are discovery prompts, not claims about all Indian buyers. No payment term, language preference or purchasing habit is assumed.
Countries: IN = India
Clues, only in selling context: {"aliases":["India"],"countries":[{"code":"IN","name":"India","aliases":["India","Bharat"],"cities":["Bengaluru","Bangalore","Mumbai","New Delhi","Chennai","Hyderabad","Pune"],"currencies":["INR","Indian rupee"],"regulators":["Reserve Bank of India","RBI","Securities and Exchange Board of India","SEBI","Insurance Regulatory and Development Authority of India","IRDAI","Telecom Regulatory Authority of India","TRAI"]}]}

### Defaults

decision_approvers | scope IN | question: Who owns the budget, security review, data permissions and final purchase approval for this Indian buyer?

procurement_payment | scope IN | question: What purchase order, invoice acceptance, currency and payment terms has this buyer actually agreed?

data_privacy | scope IN | legal: India: the Digital Personal Data Protection Rules, 2025 have staged commencement. Have the privacy owner map each proposed obligation to its effective date before promising compliance.
Applies only: For processing in scope of the Digital Personal Data Protection Act, 2023. Do not treat later commencing rules as already effective.
Source I:IN-DPDP: Digital Personal Data Protection Rules, 2025 <https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf>. Checked 2026-11-03. Gazette dated 13 November; ministry listing published 14 November 2025. Most operational rules have later commencement. Do not describe the full regime as already operative.

buyer_language | scope IN | question: Which languages must the Indian buying team and end users understand in the proposal, notices and support?

proof | scope IN | question: Which workflow, sample data and acceptance evidence will the buyer approve before a wider rollout?

objections | scope IN | question: Which unresolved data access, integration, support or contract issue could prevent this purchase?

sales_motion | scope IN | question: Who will own a limited evaluation, its acceptance decision and the next purchase step?

### logistics-tech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

sector_regulator | scope IN | legal: India: Rule 138 of the Central Goods and Services Tax Rules, 2017 links qualifying goods movements to an e way bill workflow. Establish whether the consignor, consignee or transporter owns the record.
Applies only: Only for goods movements within the rule, subject to exemptions and current central and state requirements. Selling logistics software does not itself make the vendor the transporter.
Source I:IN-EWB: E Way Bill System FAQs <https://docs.ewaybillgst.gov.in/html/faq.html>. Checked 2026-11-03. No reliable publication date. Some portal instructions are visibly old. Used only for workflow ownership; no thresholds, validity distance or current API rules asserted.

proof | scope IN | question: Can the operator demonstrate the handoff from shipment documents to the transport record, including corrections and responsibility for exceptions?

### fintech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

decision_approvers | scope IN | legal: For a commercial bank in scope, the 2025 outsourcing directions retain responsibility with its board and senior management and require an approved outsourcing policy.
Applies only: For the banks and outsourcing arrangements covered by the Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025.
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

sector_regulator | scope IN | legal: India: identify the financial activity and the buyer's regulated entity category before selecting an RBI outsourcing instrument.
Applies only: This source covers specified commercial banks. It excludes small finance banks, local area banks, payments banks and regional rural banks; do not apply it to those entities or NBFCs.
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

proof | scope IN | question: Ask the bank to confirm whether the proposed IT service is material outsourcing and which risk review and approval evidence it requires.
Applies only: For the proposed bank service only.

### vertical-saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

proof | scope IN | operating: India: for a retail or industry billing workflow supporting input tax credit, preserve the invoice, receipt and matching evidence required by CGST section 16 and rule 36.
Applies only: Registered recipient and eligible supplies only; no promise of credit eligibility.
Source I:IN-GST-CREDIT: CGST Act section 16 and eligibility for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-act/1000285/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No rate threshold credit eligibility for a specific expense or payment deadline asserted.
Source I:IN-GST-DOCS: CGST Rules rule 36 documentary requirements for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-rules/1000123/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No tax advice for an individual claim.

### ai-native | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

proof | scope IN | operating: India's AI Governance Guidelines recommend accountable and understandable systems. Use an evaluation showing failure handling, human responsibility and risks in the intended Indian use case.
Applies only: Government guidance for AI development or deployment in India. These recommendations do not establish mandatory certification.
Source I:IN-AI: India AI Governance Guidelines <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2228315&lang=2&reg=48>. Checked 2026-11-03. Policy guidance is not a blanket certification or new licence. Binding sector laws remain separate.

### ites | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

sector_regulator | scope IN | legal: India: DoT's Revised Guidelines for Other Service Providers address the defined OSP activity. Check whether the service is voice based BPO before applying that framework.
Applies only: Only a service within the OSP definition; not every IT outsourcing engagement.
Source I:IN-OSP: Revised Guidelines for Other Service Providers <https://www.dot.gov.in/static/uploads/2025/08/4e6e21029dc45f42b4e1e57e6300fa72.pdf>. Checked 2026-11-03. Do not treat every IT service or software vendor as an OSP. Verify later changes for the actual service.

### telecom | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

sector_regulator | scope IN | legal: India: DoT opened the authorisation and licence migration route under the Telecommunications Act, 2023 in June 2026. Confirm the service category and current authorisation with the operator.
Applies only: For providing a telecommunications service or migrating an existing licence; do not assume operator authorisation applies to a software supplier.
Source I:IN-DOT: Telecommunication service authorisations and licence migration <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2277786&lang=1&reg=3>. Checked 2026-11-03. Announcement supports the authorisation route only. Service specific eligibility must be checked in current rules.

### cybersecurity | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

sector_regulator | scope IN | legal: India: CERT In's directions under section 70B of the Information Technology Act, 2000 include incident reporting and contact requirements. Agree who classifies and reports applicable incidents.
Applies only: For entities and incidents within the directions and accompanying FAQs. An alert alone is not evidence of a reportable breach.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

proof | scope IN | operating: Ask for a demonstration of relevant event logs, reliable timestamps and the escalation path that supports the customer's CERT In duties.
Applies only: Only where the customer and service fall within the directions; this is suggested evidence, not a compliance certificate.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

### software | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

proof | scope IN | operating: India: CERT In guidance asks application owners to assess secure development as well as final audits. Show design controls, source review and security testing evidence.
Applies only: Developing or outsourcing applications, especially government projects; guidance rather than product certification.
Source I:IN-APP-SECURE: Guidelines for Secure Application Design Development Implementation and Operations <https://www.cert-in.org.in/PDF/Application_Security_Guidelines.pdf>. Checked 2026-11-03. Primary PDF and dated regulator index read. Guidance especially relevant to government development and outsourcing; not a universal product licence. No vendor recommendation.

### saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.

decision_approvers | scope IN | operating: India: the procuring government department specifies audit rights, contract period and service terms; STQC audit supports empanelment rather than replacing purchase approval.
Applies only: MeitY cloud empanelment guide steps 4 to 6.
Source I:IN-CLOUD-EMPANEL: Stepwise Guide on Empanelment of Cloud Service Offerings <https://www.meity.gov.in/writereaddata/files/Stepwise%20guide%20on%20empanelment%20process.pdf>. Checked 2026-11-03. Primary advisory guide steps 4 to 6 read. No reliable full issue date. Government cloud procurement scope, not every SaaS vendor. Current empanelment status must be verified.

procurement_payment | scope IN | operating: India: government cloud procurement should verify the empanelled offering, deployment model and data centre against the MeitY letter; provider name alone is insufficient.
Applies only: Government procurement using the cloud empanelment programme, not all commercial SaaS.
Source I:IN-CLOUD-EMPANEL: Stepwise Guide on Empanelment of Cloud Service Offerings <https://www.meity.gov.in/writereaddata/files/Stepwise%20guide%20on%20empanelment%20process.pdf>. Checked 2026-11-03. Primary advisory guide steps 4 to 6 read. No reliable full issue date. Government cloud procurement scope, not every SaaS vendor. Current empanelment status must be verified.

### freight-visibility | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: connect shipment visibility to the responsible consignor, consignee or transporter record in the e way bill workflow.
Applies only: Qualifying goods movement; no current threshold or API assertion.
Source I:IN-EWB: E Way Bill System FAQs <https://docs.ewaybillgst.gov.in/html/faq.html>. Checked 2026-11-03. No reliable publication date. Some portal instructions are visibly old. Used only for workflow ownership; no thresholds, validity distance or current API rules asserted.

### freight-marketplace | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### seller-shipping | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: show the seller shipping handoff from invoice or delivery document to the responsible e way bill party.
Applies only: Qualifying movement under rule 138; document and responsibility check only.
Source I:IN-EWB: E Way Bill System FAQs <https://docs.ewaybillgst.gov.in/html/faq.html>. Checked 2026-11-03. No reliable publication date. Some portal instructions are visibly old. Used only for workflow ownership; no thresholds, validity distance or current API rules asserted.

### last-mile | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### warehousing | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### transport-management | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### payments-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | operating: Ask the authorised system provider to own the storage compliance decision and nominate its delegated technical and contract reviewers. A vendor demonstration does not transfer that responsibility.
Applies only: Payment system provider accountable under RBI's storage direction
Source I:IN-PAY-DATA: Frequently asked questions on Storage of Payment System Data <https://systemhealth.rbi.org.in/Scripts/FAQDisplay.aspx_Id%3D130%281%29.html>. Checked 2026-11-03. Official RBI archived page. Check subsequent directions and the stated cross border exceptions. Never translate this payment data rule into a rule for all SaaS data.

sector_regulator | scope IN | legal: India: the Payment and Settlement Systems Act, 2007 places payment system authorisation with RBI, subject to statutory exceptions. Separate the system operator from its software supplier.
Applies only: For operating a payment system in the Act's scope. IFSC activities require the separate statutory boundary check.
Source I:IN-PSS: Payment and Settlement Systems Act, 2007 <https://financialservices.gov.in/sites/default/files/Act-Policies/2026-01/Payment-and-Settlement-Systems-Act_2007.pdf>. Checked 2026-11-03. Check statutory exceptions and IFSC scope. Does not establish that selling payment software is operating a payment system.

data_privacy | scope IN | legal: The authorised payment system provider owns compliance with RBI's payment data storage direction, including providers it engages. Map the domestic and cross border data separately before approving hosting or processing.
Applies only: Payment ecosystem data within RBI's storage direction; apply its stated exceptions and check later directions
Source I:IN-PAY-DATA: Frequently asked questions on Storage of Payment System Data <https://systemhealth.rbi.org.in/Scripts/FAQDisplay.aspx_Id%3D130%281%29.html>. Checked 2026-11-03. Official RBI archived page. Check subsequent directions and the stated cross border exceptions. Never translate this payment data rule into a rule for all SaaS data.

proof | scope IN | operating: Prepare the payment data flow, storage and backup evidence and the relevant system audit scope. Verify cross border handling separately rather than treating every record as a domestic payment.
Applies only: Payment system data review covered by RBI's FAQ
Source I:IN-PAY-DATA: Frequently asked questions on Storage of Payment System Data <https://systemhealth.rbi.org.in/Scripts/FAQDisplay.aspx_Id%3D130%281%29.html>. Checked 2026-11-03. Official RBI archived page. Check subsequent directions and the stated cross border exceptions. Never translate this payment data rule into a rule for all SaaS data.

### core-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | legal: For a covered commercial bank, its board and senior management retain outsourcing accountability. Identify the contract approver under the bank's approved outsourcing policy; policy approval is not the same as signing every purchase.
Applies only: Commercial bank in the scope of the 2025 outsourcing directions; excluded bank categories require separate directions
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

sector_regulator | scope IN | legal: Confirm the bank's RBI licence and legal category under the Banking Regulation Act 1949 before choosing the core banking approval path. Section 22 governs banking company licensing, subject to its exceptions.
Applies only: Core banking supplied to a banking company within this Act; other bank categories need their own scope check
Source I:IN-BANK-LAW: Banking Regulation Act 1949 <https://www.indiacode.nic.in/bitstream/123456789/1885/1/A1949-10.pdf>. Checked 2026-11-03. Foundational licence rule only, subject to the Act's exceptions. Does not establish the licence category or technology approval for a specific bank.

procurement_payment | scope IN | legal: Map the core platform contract to the bank's outsourcing policy and risk assessment. Ask the bank to identify any nondelegable activity and the controls it must retain.
Applies only: Covered commercial bank outsourcing arrangement
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

data_privacy | scope IN | legal: Treat customer data access, confidentiality and the bank's continued oversight as core banking design requirements. Show the bank which provider and subcontractor roles can access its records.
Applies only: Core banking arrangement assessed as outsourcing within the applicable commercial bank directions
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

proof | scope IN | operating: Use the outsourcing review to agree evidence for continuity, recovery, audit access and an exit from the service. Demonstrate those controls with the bank's own acceptance criteria before migration approval.
Applies only: Covered commercial bank outsourcing review
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

### lending | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | legal: For a covered commercial bank using a lending service provider, route vendor review through the bank's outsourcing policy and delegated authority. The bank remains accountable for the outsourced service.
Applies only: Commercial bank lending arrangement within the 2025 outsourcing directions; not an NBFC or other excluded bank category
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

sector_regulator | scope IN | legal: India: the Finance Ministry confirms RBI digital lending rules apply to regulated lenders, their lending service providers and digital lending apps. Identify the actual role.
Applies only: Framework confirmation as of July 2026; detailed current entity directions still need checking.
Source I:IN-DIGITAL-LENDING-2026: Government and RBI strengthen digital lending safeguards <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2287195&lang=2&reg=48>. Checked 2026-11-03. Primary parliamentary reply read. Used for framework and role confirmation only. Current entity specific Credit Facilities Directions and detailed permission and data clauses remain pending.

data_privacy | scope IN | operating: India: the digital lending framework includes data privacy and grievance controls. Require the regulated lender to map the proposed data flow to its current entity rules.
Applies only: Digital lending arrangement in RBI scope; no unsupported consent or hosting rule asserted.
Source I:IN-DIGITAL-LENDING-2026: Government and RBI strengthen digital lending safeguards <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2287195&lang=2&reg=48>. Checked 2026-11-03. Primary parliamentary reply read. Used for framework and role confirmation only. Current entity specific Credit Facilities Directions and detailed permission and data clauses remain pending.

proof | scope IN | operating: Agree evidence of service boundaries, customer data controls, audit access and continuity with the bank. The current entity specific Credit Facilities Directions still need checking before adding digital lending rules.
Applies only: Commercial bank outsourcing evidence only
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

### wealth-investment | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | legal: Have the adviser's compliance owner review the workflow and confirm the delegated contract approver. Its outsourcing governance remains with the intermediary's board or senior management.
Applies only: Outsourcing or compliance workflow for an investment adviser in scope
Source I:IN-IA-2026: Master Circular for Investment Advisers <https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770375291405.pdf>. Checked 2026-11-03. Applies to investment advisers. Do not extend these detailed obligations to all brokers funds or portfolio managers.

sector_regulator | scope IN | legal: India: SEBI lists distinct regulations for investment advisers, research analysts, brokers, funds and portfolio managers. Identify the actual service before choosing the applicable instrument.
Applies only: For securities activity within SEBI scope. A software vendor is not automatically a licensed financial intermediary.
Source I:IN-SEBI: Updated list of SEBI regulations <https://sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=2&smid=0&ssid=3>. Checked 2026-11-03. Live index has no single publication date. Identifies instruments only; does not validate licensing requirements or every underlying rule.

sector_regulator | scope IN | legal: For a SEBI investment adviser, use the Investment Advisers Regulations 2013 with the February 2026 Master Circular. Confirm the adviser registration and whether the product supports advice, execution or both.
Applies only: SEBI investment adviser activity; this is not the complete broker or portfolio manager regime
Source I:IN-IA-2026: Master Circular for Investment Advisers <https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770375291405.pdf>. Checked 2026-11-03. Applies to investment advisers. Do not extend these detailed obligations to all brokers funds or portfolio managers.

data_privacy | scope IN | legal: Preserve client confidentiality and legally verifiable records of advisory interactions. For telephone implementation consent, retain the time stamped audit trail required by the circular.
Applies only: Investment adviser interactions and implementation services covered by the circular
Source I:IN-IA-2026: Master Circular for Investment Advisers <https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770375291405.pdf>. Checked 2026-11-03. Applies to investment advisers. Do not extend these detailed obligations to all brokers funds or portfolio managers.

proof | scope IN | operating: Demonstrate risk profiling, suitability, client consent records and an export usable for the adviser's compliance audit. This evidence follows the adviser's documented obligations, not a promised investment result.
Applies only: Investment adviser workflow within the circular
Source I:IN-IA-2026: Master Circular for Investment Advisers <https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770375291405.pdf>. Checked 2026-11-03. Applies to investment advisers. Do not extend these detailed obligations to all brokers funds or portfolio managers.

### spend-expense | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | question: Which person has delegated authority for the expense, and which person validates the tax claim? Record both from this Indian buyer's policy rather than assuming a universal job title.
Applies only: Expense approval and tax evidence workflow

sector_regulator | scope IN | legal: Separate expense records and tax support from operating a payment system. Confirm the actual movement of funds before selecting RBI authorisation checks, and identify the GST registered recipient making any credit claim.
Applies only: Expense workflow with GST claims or payment activity; each regime applies only within its scope
Source I:IN-PSS: Payment and Settlement Systems Act, 2007 <https://financialservices.gov.in/sites/default/files/Act-Policies/2026-01/Payment-and-Settlement-Systems-Act_2007.pdf>. Checked 2026-11-03. Check statutory exceptions and IFSC scope. Does not establish that selling payment software is operating a payment system.
Source I:IN-GST-CREDIT: CGST Act section 16 and eligibility for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-act/1000285/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No rate threshold credit eligibility for a specific expense or payment deadline asserted.

procurement_payment | scope IN | legal: For input tax credit support, the workflow must preserve the relevant tax documents and the supplier statement matching required by rule 36. An expense approval by itself is not the required tax evidence.
Applies only: GST registered recipient seeking input tax credit
Source I:IN-GST-DOCS: CGST Rules rule 36 documentary requirements for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-rules/1000123/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No tax advice for an individual claim.

proof | scope IN | operating: Show a receipt or invoice moving through review, supplier detail checks and a traceable credit evidence record. Have the buyer's tax reviewer confirm the workflow; do not promise that every employee expense is creditable.
Applies only: Evaluation of GST evidence handling, not a conclusion on a particular tax claim
Source I:IN-GST-CREDIT: CGST Act section 16 and eligibility for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-act/1000285/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No rate threshold credit eligibility for a specific expense or payment deadline asserted.
Source I:IN-GST-DOCS: CGST Rules rule 36 documentary requirements for input tax credit <https://taxinformation.cbic.gov.in/content-page/explore-rules/1000123/1000001>. Checked 2026-11-03. Current primary publisher indexed text read; live page returned 502. No tax advice for an individual claim.

### insurance | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | legal: The insurer's outsourcing committee implements its board approved policy and includes risk, finance and operations leadership. Confirm the delegated approver for this arrangement under that policy.
Applies only: Insurer outsourcing within regulations 45 to 48; reinsurance exclusion applies
Source I:IN-INS-OPS: Protection of Policyholders Interests Operations and Allied Matters of Insurers Regulations 2024 <https://egazette.gov.in/WriteReadData/2024/253330.pdf>. Checked 2026-11-03. Outsourcing schedule excludes insurers engaged in reinsurance. Actual delegated contract approval comes from the insurer's policy; committee membership is not a statement that every member signs every contract.

sector_regulator | scope IN | legal: India: the Insurance Regulatory and Development Authority Act, 1999 assigns insurance supervision to IRDAI. Identify the insurer or intermediary role before mapping obligations.
Applies only: For insurance activities in scope; check the IFSC exclusion and the current product specific instrument.
Source I:IN-IRDAI: Insurance Regulatory and Development Authority Act, 1999 <https://www.indiacode.nic.in/bitstream/123456789/1893/1/A1999_41.pdf>. Checked 2026-11-03. Used only for regulator boundary. Product specific current regulations require separate checks.

procurement_payment | scope IN | legal: Have the insurer check that the proposed service is permitted to be outsourced and that the contract preserves IRDAI access and the insurer's oversight.
Applies only: Covered insurer outsourcing; any prohibited activity remains prohibited
Source I:IN-INS-OPS: Protection of Policyholders Interests Operations and Allied Matters of Insurers Regulations 2024 <https://egazette.gov.in/WriteReadData/2024/253330.pdf>. Checked 2026-11-03. Outsourcing schedule excludes insurers engaged in reinsurance. Actual delegated contract approval comes from the insurer's policy; committee membership is not a statement that every member signs every contract.

data_privacy | scope IN | legal: Protect policyholder information through the contract and after termination. The insurer must secure the return of customer data and prevent its further use after the arrangement ends.
Applies only: Insurer outsourcing covered by regulation 51
Source I:IN-INS-OPS: Protection of Policyholders Interests Operations and Allied Matters of Insurers Regulations 2024 <https://egazette.gov.in/WriteReadData/2024/253330.pdf>. Checked 2026-11-03. Outsourcing schedule excludes insurers engaged in reinsurance. Actual delegated contract approval comes from the insurer's policy; committee membership is not a statement that every member signs every contract.

proof | scope IN | operating: Prepare evidence of service provider controls, data return and regulator access to relevant records, systems and audit findings. These are procurement tests derived from the insurer's outsourcing duties.
Applies only: Covered insurer outsourcing under regulations 50 to 53
Source I:IN-INS-OPS: Protection of Policyholders Interests Operations and Allied Matters of Insurers Regulations 2024 <https://egazette.gov.in/WriteReadData/2024/253330.pdf>. Checked 2026-11-03. Outsourcing schedule excludes insurers engaged in reinsurance. Actual delegated contract approval comes from the insurer's policy; committee membership is not a statement that every member signs every contract.

### customer-service | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### crm-marketing | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### collaboration | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-growth | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### construction | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### property-management | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### field-services | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### fmcg-retail-execution | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### industry-hr-payroll | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### hotel-lodging | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### retail-restaurant-ops | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### agents-copilots | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### voice-language-models | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### enterprise-search | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### it-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### bpo-cx | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-engineering | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### operators-connectivity | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: show the operator entity, authorised service category and current DoT permission or migration position before proposing connectivity delivery.
Applies only: Operating telecom service, not merely supplying software to an operator.
Source I:IN-DOT: Telecommunication service authorisations and licence migration <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2277786&lang=1&reg=3>. Checked 2026-11-03. Announcement supports the authorisation route only. Service specific eligibility must be checked in current rules.

### cpaas-messaging | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope IN | legal: India: TRAI's Telecom Commercial Communications Customer Preference Regulations, 2018 address registered senders and customer preference and consent. Map the intended commercial messaging route before launch.
Applies only: For commercial communications within the telecom framework; verify the current consolidated rules and amendments.
Source I:IN-TRAI: TRAI strengthens consumer protection with amendments to TCCCPR, 2018 <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2102413&lang=2&reg=48>. Checked 2026-11-03. Announcement rather than consolidated regulations. No detailed number series or timing requirement asserted.

### telecom-software | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### business-voice-ucaas | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### developer-platform | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-infrastructure | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### observability | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### testing | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### dev-tools | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### cloud-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: verify the government cloud offering and data centre in the MeitY empanelment letter, then test the agreed security responsibilities.
Applies only: Government cloud procurement only.
Source I:IN-CLOUD-EMPANEL: Stepwise Guide on Empanelment of Cloud Service Offerings <https://www.meity.gov.in/writereaddata/files/Stepwise%20guide%20on%20empanelment%20process.pdf>. Checked 2026-11-03. Primary advisory guide steps 4 to 6 read. No reliable full issue date. Government cloud procurement scope, not every SaaS vendor. Current empanelment status must be verified.

### identity-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: CERT In application guidance supports testing authentication, authorisation and session termination together.
Applies only: Application security guidance.
Source I:IN-APP-SECURE: Guidelines for Secure Application Design Development Implementation and Operations <https://www.cert-in.org.in/PDF/Application_Security_Guidelines.pdf>. Checked 2026-11-03. Primary PDF and dated regulator index read. Guidance especially relevant to government development and outsourcing; not a universal product licence. No vendor recommendation.

### email-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: test how an email security alert reaches the designated incident contact and the applicable CERT In reporting workflow.
Applies only: Suggested evaluation for entities within the directions.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

### awareness-training | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: audit social engineering exercises should assess agreed staff groups without identifying or penalising individuals. External targets require specific written consent.
Applies only: CERT In audit guidance section 15.
Source I:IN-AUDIT-POLICY: Comprehensive Cyber Security Audit Policy Guidelines <https://www.cert-in.org.in/Downloader?fileName=CIGU-2025-0002.pdf&pageid=6&type=2>. Checked 2026-11-03. Primary version 1.0 read, especially sections 8 13 and 15. Audit engagement guidance is not a universal security software licence or an endorsement of a provider.

### appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: combine secure development evidence with source review and black box testing under CERT In application guidance.
Applies only: Application development and outsourcing guidance.
Source I:IN-APP-SECURE: Guidelines for Secure Application Design Development Implementation and Operations <https://www.cert-in.org.in/PDF/Application_Security_Guidelines.pdf>. Checked 2026-11-03. Primary PDF and dated regulator index read. Guidance especially relevant to government development and outsourcing; not a universal product licence. No vendor recommendation.

### mobile-appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: CERT In audit guidance identifies mobile testing standards; define the tested application version and environment in the report.
Applies only: Mobile application audit.
Source I:IN-AUDIT-POLICY: Comprehensive Cyber Security Audit Policy Guidelines <https://www.cert-in.org.in/Downloader?fileName=CIGU-2025-0002.pdf&pageid=6&type=2>. Checked 2026-11-03. Primary version 1.0 read, especially sections 8 13 and 15. Audit engagement guidance is not a universal security software licence or an endorsement of a provider.

### soc-services | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | operating: India: confirm the designated CERT In contact and demonstrate the monitoring to reporting escalation. Outsourcing monitoring does not identify the buyer signatory.
Applies only: In-scope incident reporting and contact duties.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

### endpoint-network | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: demonstrate endpoint and network event logging with reliable timestamps against applicable CERT In logging requirements.
Applies only: ICT systems within the directions; suggested evidence.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

### document-ai | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### ai-video | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### engineering-talent | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-management | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-adoption | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### pentest | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope IN | operating: India: obtain the auditee approval for the audit team and agreed test scope before work; maintain confidential evidence handling.
Applies only: CERT In audit engagement guidance.
Source I:IN-AUDIT-POLICY: Comprehensive Cyber Security Audit Policy Guidelines <https://www.cert-in.org.in/Downloader?fileName=CIGU-2025-0002.pdf&pageid=6&type=2>. Checked 2026-11-03. Primary version 1.0 read, especially sections 8 13 and 15. Audit engagement guidance is not a universal security software licence or an endorsement of a provider.

### attack-surface-dast | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope IN | operating: India: an automated scan alone is insufficient audit evidence under CERT In guidance; include manual coverage and documented limitations.
Applies only: Audit assurance, not every standalone scan.
Source I:IN-AUDIT-POLICY: Comprehensive Cyber Security Audit Policy Guidelines <https://www.cert-in.org.in/Downloader?fileName=CIGU-2025-0002.pdf&pageid=6&type=2>. Checked 2026-11-03. Primary version 1.0 read, especially sections 8 13 and 15. Audit engagement guidance is not a universal security software licence or an endorsement of a provider.

### process-orchestration | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### open-source-support | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### iot-connectivity | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

## Southeast Asia

Draft for owner review. Every listed country has at least one sourced topic, but legal and industry coverage is incomplete. Privacy notes currently cover Singapore, Indonesia, Malaysia, Thailand, Viet Nam, the Philippines and Brunei. Cambodia, Laos, Myanmar and Timor Leste have only limited financial sector source notes. A broad regional request needs a country before country law can be selected. Questions do not assert local buying habits.
Countries: SG = Singapore; ID = Indonesia; MY = Malaysia; TH = Thailand; VN = Viet Nam; PH = Philippines; BN = Brunei; KH = Cambodia; LA = Laos; MM = Myanmar; TL = Timor Leste
Clues, only in selling context: {"aliases":["Southeast Asia","South East Asia"],"countries":[{"code":"SG","name":"Singapore","aliases":[],"cities":[],"currencies":["SGD","Singapore dollar"],"regulators":["Monetary Authority of Singapore"]},{"code":"ID","name":"Indonesia","aliases":[],"cities":["Jakarta","Surabaya"],"currencies":["IDR","Indonesian rupiah"],"regulators":["Bank Indonesia","Otoritas Jasa Keuangan"]},{"code":"MY","name":"Malaysia","aliases":[],"cities":["Kuala Lumpur"],"currencies":["MYR","Malaysian ringgit"],"regulators":["Bank Negara Malaysia"]},{"code":"TH","name":"Thailand","aliases":[],"cities":["Bangkok"],"currencies":["THB","Thai baht"],"regulators":["Bank of Thailand"]},{"code":"VN","name":"Viet Nam","aliases":["Vietnam"],"cities":["Hanoi","Ho Chi Minh City"],"currencies":["VND","Vietnamese dong"],"regulators":[]},{"code":"PH","name":"Philippines","aliases":["the Philippines"],"cities":["Manila","Cebu"],"currencies":["PHP","Philippine peso"],"regulators":["Bangko Sentral ng Pilipinas"]},{"code":"BN","name":"Brunei","aliases":["Brunei Darussalam"],"cities":["Bandar Seri Begawan"],"currencies":["BND"],"regulators":[]},{"code":"KH","name":"Cambodia","aliases":[],"cities":["Phnom Penh"],"currencies":["KHR"],"regulators":[]},{"code":"LA","name":"Laos","aliases":["Lao PDR"],"cities":["Vientiane"],"currencies":["LAK"],"regulators":[]},{"code":"MM","name":"Myanmar","aliases":[],"cities":["Yangon","Naypyidaw"],"currencies":["MMK"],"regulators":[]},{"code":"TL","name":"Timor Leste","aliases":["Timor-Leste","East Timor"],"cities":["Dili"],"currencies":[],"regulators":[]}]}

### Defaults

decision_approvers | scope COMMON | question: Which named country and contracting entity are in scope, and who approves budget, risk and the purchase?

procurement_payment | scope COMMON | question: What currency, purchase order, invoice acceptance and payment terms has this buyer confirmed?

data_privacy | scope SG | legal: Singapore: the Personal Data Protection Act requires appropriate protection and retention controls and comparable protection for overseas transfers. Map where personal data goes and who controls it.
Applies only: For organisations and processing in the Act's scope, subject to applicable exclusions and transfer regulations.
Source I:SG-PDPA: Data protection obligations under the Personal Data Protection Act <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Resource-for-Organisation/Data-Protection-Obligations-under-the-PDPA.ashx?la=en>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Document states May 2021. Used only for these stable obligations, not its uncommenced data portability item. Check exceptions and current regulations.

data_privacy | scope ID | legal: Indonesia: check the proposed processing against Law No. 27 of 2022 on Personal Data Protection before agreeing data access and transfer terms.
Applies only: For processing within the Indonesian law's scope. Detailed implementing requirements must be checked for the actual data flow.
Source I:ID-PDP: Law No. 27 of 2022 on Personal Data Protection <https://jdih.komdigi.go.id/produk_hukum/view/id/832/t/crc32/>. Checked 2026-11-03. Primary indexed law entry read; live open timed out. Detailed transfer mechanisms and implementing rules not asserted.

data_privacy | scope MY | legal: Malaysia: the Personal Data Protection Act 2010 applies to personal data in commercial transactions within its scope; federal and state governments are excluded.
Applies only: Check establishment, processing location and statutory exclusions. Read the Act with its amendments.
Source I:MY-PDPA: Application and non application of the Personal Data Protection Act <https://www.pdp.gov.my/en/akta/application-and-non-application-of-the-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used only for scope. Read Act 709 as amended and current commencement instruments before specific obligations.

data_privacy | scope PH | legal: Philippines: Republic Act 10173, the Data Privacy Act of 2012, sets lawful processing and security requirements. Identify the personal information controller and processor roles.
Applies only: For processing in the Act's scope, with separate treatment for sensitive personal information and statutory exceptions.
Source I:PH-DPA: Republic Act 10173: Data Privacy Act of 2012 <https://privacy.gov.ph/data-privacy-act/>. Checked 2026-11-03. Statutory exclusions, sensitive information rules and current implementing instruments require scope review.

data_privacy | scope TH | legal: Thailand: use the Personal Data Protection Act B.E. 2562 (2019) for the local privacy scope review. Confirm the controller, processor and proposed data use.
Applies only: For Thai processing in scope; this note does not determine the lawful basis or transfer mechanism.
Source I:TH-PDPA: Personal Data Protection Act B.E. 2562 (2019) <https://mdes.go.th/law/128>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Index identifies law; no specific consent, transfer or reporting deadline asserted.

data_privacy | scope VN | legal: Viet Nam: the Law on Personal Data Protection took effect on 1 January 2026. Review the current law and implementing rules before finalising data handling terms.
Applies only: For processing in scope of the Vietnamese regime. An older decree alone is not a complete current review.
Source I:VN-PDP: Presidential Office announces new laws <https://en.baochinhphu.vn/presidential-office-announces-18-new-laws-111250711204559004.htm>. Checked 2026-11-03. Announcement used for commencement only. No penalties or detailed transfer rules reproduced.

data_privacy | scope BN | legal: Brunei's Personal Data Protection Order 2025 has commenced its organisation obligations. Confirm the entity's role and section 3 exceptions, then identify the person responsible for compliance and the data processing safeguards.
Applies only: Organisation and processing within the Order's scope; public agencies and processors have different treatment
Source I:BN-PDP: Personal Data Protection Order 2025 <https://pdp.aiti.gov.bn/media/tndpduml/s-1_2025-e.pdf>. Checked 2026-11-03. Read with commencement notification S 11 of 2025. Private organisation obligations must not be transferred wholesale to public agencies or data processors.
Source I:BN-PDP-COMMENCEMENT: Personal Data Protection Order 2025 notification S 11 <https://www.agc.gov.bn/wp-content/uploads/2026/07/S-11-2025-PERSONAL-DATA-PROTECTION-ORDER-2025-NOTIFICATION-OF-COMMENCEMENT-1.pdf>. Checked 2026-11-03. Notification dated 8 January 2025; URL upload date is not enactment date. Other parts commenced under S 10.

buyer_language | scope COMMON | question: Which languages do the buying team, users and required notices need?

proof | scope COMMON | question: What sample workflow and acceptance evidence will the buyer approve?

objections | scope COMMON | question: Which data access, integration, support or contract issue could block the purchase?

sales_motion | scope COMMON | question: Who owns the evaluation, acceptance decision and next purchase step?

### logistics-tech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope SG | legal: Singapore: import permits use the Singapore Customs TradeNet process. Confirm whether the importer submits the declaration or appoints a declaring agent.
Applies only: For goods imported into Singapore within the applicable permit requirements. A logistics software vendor is not automatically the declaring agent.
Source I:SG-CUSTOMS: Obtain a Customs Import Permit <https://www.customs.gov.sg/doing-business/import-operations/import-procedures/obtain-a-customs-import-permit/>. Checked 2026-11-03. Page update date. Exceptions and controlled goods requirements remain activity specific.

### fintech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

decision_approvers | scope SG | question: Ask the institution which outsourcing governance and risk approval process applies, and which evidence the supplier must provide.
Applies only: For the proposed Singapore financial institution engagement.

sector_regulator | scope SG | legal: Singapore: MAS distinguishes bank outsourcing notices and guidance from guidance for other financial institutions. Classify the buyer before choosing the review.
Applies only: For a financial institution and outsourcing arrangement within the relevant MAS instrument; a consultation is not a final rule.
Source I:SG-OUTSOURCE: Third party risk management <https://www.mas.gov.sg/regulation/third-party-risk-management>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Index last updated 6 March 2026. Distinguish a notice from guidelines and from a consultation; no universal vendor licence inferred.

sector_regulator | scope ID | legal: Indonesia: OJK supervises banking, insurance, financing and capital market activities within its remit. Select the activity before requesting its compliance evidence.
Applies only: For an OJK supervised entity or activity. Payment system matters require the separately scoped payment note.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Bank Negara Malaysia supervises banking and insurance and takaful institutions under its remit. Confirm the buyer's category.
Applies only: For institutions within BNM supervision; do not extend this to all lenders or securities activities.
Source I:MY-BNM: Supervision <https://www.bnm.gov.my/supervision>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not cover every nonbank lender or every capital market service.

sector_regulator | scope PH | legal: Philippines: BSP supervises banks and other institutions within its remit and oversees payment systems. Confirm whether the actual buyer is BSP supervised.
Applies only: Only for BSP supervised entities and activities.
Source I:PH-BSP: Governance of the Bank <https://www.bsp.gov.ph/Pages/AboutTheBank/WhoWeAre/OrganizationAndGovernance/GovernanceOfTheBank.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not all lenders or insurers are BSP regulated.

sector_regulator | scope TH | legal: Thailand: the Bank of Thailand supervises financial institutions and has payment system responsibilities. Confirm the institution and product before selecting requirements.
Applies only: Only for the Bank of Thailand's actual supervisory scope.
Source I:TH-BOT: Our Roles <https://www.bot.or.th/en/our-roles.html>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish oversight of every finance or insurance business.

sector_regulator | scope BN | legal: For Brunei financial services, identify the BDCB category covering the buyer and activity. Banking, finance providers, payments, insurance and capital markets use separate regulatory requirements.
Applies only: Activity within Brunei Darussalam Central Bank's regulatory remit
Source I:BN-BDCB: Regulatory sectors and instruments <https://www.bdcb.gov.bn/regulatory>. Checked 2026-11-03. Undated official current index. It establishes categories, not a licence conclusion for a particular product.

sector_regulator | scope KH | legal: For a Cambodia banking or financial institution supervised by the National Bank of Cambodia, confirm its regulated category. The NBC supervision framework distinguishes banks, microfinance, financial leasing and payment service institutions.
Applies only: Institution within NBC supervision; this does not establish the insurance or securities regulator
Source I:KH-NBC: Banking supervision overview <https://www.nbc.gov.kh/english/supervision/overview.php>. Checked 2026-11-03. Official publisher search extract read; live page returned 403. No current detailed banking or payment licence condition asserted.

sector_regulator | scope LA | legal: For Laos, check the applicable banking or payment framework listed by the Bank of the Lao PDR. The index lists the amended Commercial Bank Law 39/NA of 2023 and amended Payment System Law 45/NA of 2023. Confirm the activity and current implementing requirements.
Applies only: Banking or payment activity governed by the relevant Lao law; no licence condition is inferred from the index
Source I:LA-BOL: Bank of the Lao PDR laws index <https://bol.gov.la/en/law>. Checked 2026-11-03. Official publisher index read; live page returned 502. Only legal names and dates used. Licence conditions and current subordinate instructions remain unverified.

sector_regulator | scope TL | legal: In Timor Leste, BCTL's licensing remit under Law No. 5/2011 covers regulated financial institutions. Its published framework separates banks, insurance, money transfer and currency exchange. Confirm the relevant activity before choosing the licence and evidence checklist.
Applies only: Institution or activity within BCTL's licensing remit
Source I:TL-BCTL: Licence application framework <https://bancocentral.tl/stats/lic_app/>. Checked 2026-11-03. Undated current official page. No provider count or company fact copied. Specific licence and current instruction details require review.

sector_regulator | scope MM | legal: Myanmar's Financial Institutions Law 2016 gives the Central Bank licensing, registration and supervisory powers for covered banks and nonbank financial institutions. Confirm the buyer's legal category and current directives before defining approval evidence.
Applies only: Institution covered by this law; separate insurance, microfinance and securities regimes require their own checks
Source I:MM-BANK: Financial Institutions Law 2016 <https://www.mfiu.gov.mm/sites/default/files/document/files/The%20Financial%20Institutions%20Law%202016.pdf>. Checked 2026-11-03. Official government hosted English law. Detailed current directives and separate microfinance insurance or securities frameworks not verified.

### vertical-saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

proof | scope SG | legal: Singapore: HR and payroll workflows must support Employment Act employee and salary records, including the applicable retention periods.
Applies only: Employers and employees covered by the Employment Act.
Source I:SG-EMPLOYMENT-RECORDS: Employment records <https://www.mom.gov.sg/employment-practices/employment-records>. Checked 2026-11-03. Current primary page read and checked against section 95 and S148/2016. No page publication date. Applies only to employees covered by the Act; no payroll vendor licensing claim.

### ai-native | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

proof | scope SG | operating: Singapore's Model AI Governance Framework for Agentic AI recommends human accountability and controls on agent actions. Show approval boundaries and failure handling in the evaluation.
Applies only: Guidance for agentic AI deployment, not a certification or general software licence.
Source I:SG-AI: Updated Model AI Governance Framework for Agentic AI <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai>. Checked 2026-11-03. Primary indexed extract read; live open returned a script challenge. Guidance, not a mandatory certification.

### ites | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

data_privacy | scope SG | legal: Singapore: outsourced personal data processing needs documented responsibilities between the organisation and data intermediary; staff handoffs should follow the agreed processing instructions.
Applies only: PDPA processing on behalf of private organisations; government outsourcing has separate requirements.
Source I:SG-DATA-INTERMEDIARIES: Guide to Managing Data Intermediaries <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Managing-Data-Intermediaries--2020.pdf?la=en>. Checked 2026-11-03. Primary PDF read. Filename year is not a verified full publication date. Distinguish PDPA duties from recommended operating practices; public agencies use a separate framework.

proof | scope SG | operating: Singapore: use the PDPC lifecycle guide to demonstrate vendor onboarding, incident escalation and an agreed data exit plan.
Applies only: Suggested diligence evidence, proportionate to outsourced processing risk.
Source I:SG-DATA-INTERMEDIARIES: Guide to Managing Data Intermediaries <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Managing-Data-Intermediaries--2020.pdf?la=en>. Checked 2026-11-03. Primary PDF read. Filename year is not a verified full publication date. Distinguish PDPA duties from recommended operating practices; public agencies use a separate framework.

### telecom | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope SG | legal: Singapore: IMDA's Services Based Operations licence covers defined telecommunications service operations. Confirm whether the seller operates a service or supplies software to an operator.
Applies only: Only for the activity within the relevant Singapore licensing category.
Source I:SG-TELECOM: Services Based Operations licence <https://www.imda.gov.sg/regulations-and-licensing-listing/services-based-operations--sbo--licence>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Primary indexed page extract read; live open returned a script challenge. No specific licence conditions asserted.

### cybersecurity | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

decision_approvers | scope BN | legal: Brunei: CII owners assign cybersecurity responsibilities and maintain board and senior management oversight.
Applies only: CII code section 3.1.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

sector_regulator | scope SG | legal: Singapore: the Cybersecurity Act licensing framework covers penetration testing and managed security operations centre monitoring services. Check the exact service scope.
Applies only: For licensable services under the Act. Do not classify every cybersecurity product as a licensed service.
Source I:SG-CYBER: Cybersecurity Act <https://www.csa.gov.sg/legislation/cybersecurity-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Live page used for service scope only. Other cybersecurity obligations and amended designation regimes require separate applicability review.

sector_regulator | scope MY | legal: Malaysia: NACSA licensing under the Cyber Security Act 2024 and its provider regulations covers managed SOC monitoring and penetration testing. Establish the actual service and statutory exclusions.
Applies only: Only the defined licensable services and territorial scope.
Source I:MY-CYBER-LICENCE: Cyber Security Service Provider Licensing FAQ <https://www.nacsa.gov.my/doc/FAQ%20LICENSING%20SERVICE%20PROVIDER.pdf>. Checked 2026-11-03. Live primary PDF. No reliable full publication date. Do not extend the two licensed service categories to every security software product; check statutory exclusions.

sector_regulator | scope BN | legal: Brunei: Cybersecurity Act Chapter 272 regulates critical information infrastructure owners. Confirm CII designation before applying the code.
Applies only: CII scope only.
Source I:BN-CYBER-ACT: Cybersecurity Act Chapter 272 <https://csb.gov.bn/cybersecurity-act-chapter-272>. Checked 2026-11-03. Live primary page states 2023 Order became Act in 2024. No full page publication date. Do not extend CII owner requirements to all private software buyers.

data_privacy | scope BN | legal: Brunei: CII outsourcing contracts address access, protection, incident reporting and audit rights; the owner retains accountability.
Applies only: CII code section 3.7.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

proof | scope SG | operating: Singapore: check the supplier licence category, service scope and current certification position. The CTM grace period ends on 31 December 2026; the final CSA response does not require DPTM certification.
Applies only: Licensed cybersecurity services only; verify the current certificate and applicable transition.
Source I:SG-CYBER-LICENCE: Apply for Licence <https://www.csro.gov.sg/how-to/apply-for-licence/>. Checked 2026-11-03. Live primary page. Licence application and provider responsibility are distinct from the customer purchase approval. CTM grace runs to 31 December 2026.
Source I:SG-CYBER-CONDITIONS: Closing note and updated cybersecurity licence conditions <https://www.csa.gov.sg/legislation/consultations/closing-note-to-the-consultation-on-the-licensing-framework-for-cybersecurity-service-providers/>. Checked 2026-11-03. Final closing note with operative condition text, not a consultation proposal. Standalone conditions PDF returned 404, so scope is cross checked against current CSRO FAQ. DPTM is not a mandatory certification in the final response.

### software | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

proof | scope SG | operating: Singapore: PDPC guidance recommends testing with synthetic or anonymised data and checking exception paths for personal data leaks before release.
Applies only: ICT systems handling personal data; guidance is not a product certificate.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Indonesia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Malaysia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Thailand: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Viet Nam: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Philippines: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Brunei: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Cambodia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Laos: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Myanmar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Timor Leste: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

data_privacy | scope SG | operating: Singapore: a hosted data intermediary agreement should define processing obligations, overseas protection and the end of service data arrangements.
Applies only: Personal data processing under the PDPA; verify transfer arrangements separately.
Source I:SG-DATA-INTERMEDIARIES: Guide to Managing Data Intermediaries <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Managing-Data-Intermediaries--2020.pdf?la=en>. Checked 2026-11-03. Primary PDF read. Filename year is not a verified full publication date. Distinguish PDPA duties from recommended operating practices; public agencies use a separate framework.

proof | scope SG | operating: Singapore: demonstrate secure migration and exit checks against the agreed data handling contract.
Applies only: Suggested SaaS evaluation evidence from PDPC intermediary guidance.
Source I:SG-DATA-INTERMEDIARIES: Guide to Managing Data Intermediaries <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Managing-Data-Intermediaries--2020.pdf?la=en>. Checked 2026-11-03. Primary PDF read. Filename year is not a verified full publication date. Distinguish PDPA duties from recommended operating practices; public agencies use a separate framework.

### freight-visibility | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SG | operating: Singapore: distinguish a Customs permit status from a carrier arrival estimate and show which declaring party supplied the permit evidence.
Applies only: Suggested import workflow evidence; not a guarantee of customs clearance.
Source I:SG-CUSTOMS: Obtain a Customs Import Permit <https://www.customs.gov.sg/doing-business/import-operations/import-procedures/obtain-a-customs-import-permit/>. Checked 2026-11-03. Page update date. Exceptions and controlled goods requirements remain activity specific.

### freight-marketplace | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### seller-shipping | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SG | operating: Singapore: the importer obtains the Customs permit itself or through its declaring agent; preserve that handoff in seller shipping.
Applies only: Import permit workflow, including applicable goods restrictions and exceptions.
Source I:SG-CUSTOMS: Obtain a Customs Import Permit <https://www.customs.gov.sg/doing-business/import-operations/import-procedures/obtain-a-customs-import-permit/>. Checked 2026-11-03. Page update date. Exceptions and controlled goods requirements remain activity specific.

### last-mile | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### warehousing | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### transport-management | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### payments-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the payment institution's board and senior management oversee outsourcing under applicable MAS nonbank guidelines; confirm the delegated purchase approver.
Applies only: Only an institution and outsourcing arrangement within these supervisory guidelines.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

decision_approvers | scope MY | legal: Malaysia: an electronic money issuer's board charter identifies reserved decisions; the board approves a proposed first white label arrangement before seeking BNM approval.
Applies only: An e-money issuer and white labelling arrangement within the policy; not a universal software purchase route.
Source I:MY-E-MONEY: Electronic Money policy document <https://www.bnm.gov.my/documents/20124/943361/27012025_Revised_E-Money_PD_v2.pdf>. Checked 2026-11-03. Primary PDF read. E-money issuer category only, not every payment service or expense software vendor.

sector_regulator | scope SG | legal: Singapore: the Payment Services Act 2019 regulates defined payment services and exemptions. Map the actual money flow and service before choosing the MAS licence category.
Applies only: For a payment service within the Act, not every supplier of payment software.
Source I:SG-PAYMENTS: Payments regulation <https://www.mas.gov.sg/regulation/payments>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish that all payment software suppliers provide a regulated service.

sector_regulator | scope ID | legal: Indonesia: Bank Indonesia's PBI 10 of 2025 and PADG 32 of 2025 govern the payment system industry from 31 March 2026. Map the provider and supporting party roles.
Applies only: For the payment activity and entities in scope; no licence or exemption is inferred.
Source I:ID-PAYMENTS: Bank Indonesia strengthens structure of payment system industry <https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_281626.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Announcement used to identify the current framework and third party risk focus. No financial projection or statistic used.

sector_regulator | scope BN | legal: Brunei payment services fall within BDCB's payment oversight framework, including the Payment and Settlement Systems (Oversight) Act, Cap 251. Confirm the service category, such as account issuance, electronic money or merchant acquiring, before preparing the approval evidence.
Applies only: Payment service or system within BDCB's regulatory perimeter
Source I:BN-PAYMENTS: Payment Services and Payment and Settlement Systems Oversight Act Cap 251 <https://www.bdcb.gov.bn/regulatory/payment-services>. Checked 2026-11-03. Undated current regulator overview. Detailed service authorisation requirements require separate review.

sector_regulator | scope MY | operating: Malaysia: identify whether the product issues electronic money, acquires merchants or operates a payment system; BNM uses distinct categories and requirements.
Applies only: Activity and institution classification only; complete approval and exemption review remains pending.
Source I:MY-E-MONEY: Electronic Money policy document <https://www.bnm.gov.my/documents/20124/943361/27012025_Revised_E-Money_PD_v2.pdf>. Checked 2026-11-03. Primary PDF read. E-money issuer category only, not every payment service or expense software vendor.
Source I:MY-RMIT-2026: Risk Management in Technology BNM/RH/PD 028-98 <https://www.bnm.gov.my/documents/20124/938039/pd-rmit-sep26.pdf>. Checked 2026-11-03. Current primary PDF. Effective and transitional provisions vary; Part C excludes designated payment system operators, eligible e-money issuers, nonbank merchant acquirers and intermediary remittance institutions. No blanket bank cloud approval claim.

data_privacy | scope SG | operating: Singapore: for in-scope payment institution outsourcing, demonstrate confidentiality, audit access and an exit plan.
Applies only: MAS nonbank outsourcing guidelines; a supervisory expectation, not a universal vendor licence.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

data_privacy | scope MY | legal: Malaysia: e-money customer information disclosures must use the applicable BNM basis and controls; when relying on consent, retain the explicit consent and withdrawal trail.
Applies only: A financial service provider and customer information disclosure within the policy.
Source I:MY-CUSTOMER-DATA: Management of Customer Information and Permitted Disclosures <https://www.bnm.gov.my/documents/20124/938039/MCIPD_PD_2025.pdf>. Checked 2026-11-03. Primary PDF checked 3 November 2026. Paragraphs 2.1, 2.2 and 5.2 distinguish FSPs from financial institutions. Insurer and takaful lifecycle policies use Part B paragraph 10.6; do not extend Part C consent conditions to them.

proof | scope SG | operating: Singapore: map each payment service and licence exemption boundary, then give the regulated institution the outsourcing diligence and control evidence for that service.
Applies only: Payment Services Act activity and, separately, an institution within the nonbank outsourcing guidelines.
Source I:SG-PAYMENTS: Payments regulation <https://www.mas.gov.sg/regulation/payments>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish that all payment software suppliers provide a regulated service.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

proof | scope MY | operating: Malaysia: map the issuer category, reserved decisions and white label responsibilities, then demonstrate technology oversight and the applicable RMiT controls.
Applies only: E-money case only. RMiT Part C has institution exclusions; do not impose bank cloud consultation on an excluded issuer.
Source I:MY-E-MONEY: Electronic Money policy document <https://www.bnm.gov.my/documents/20124/943361/27012025_Revised_E-Money_PD_v2.pdf>. Checked 2026-11-03. Primary PDF read. E-money issuer category only, not every payment service or expense software vendor.
Source I:MY-RMIT-2026: Risk Management in Technology BNM/RH/PD 028-98 <https://www.bnm.gov.my/documents/20124/938039/pd-rmit-sep26.pdf>. Checked 2026-11-03. Current primary PDF. Effective and transitional provisions vary; Part C excludes designated payment system operators, eligible e-money issuers, nonbank merchant acquirers and intermediary remittance institutions. No blanket bank cloud approval claim.

### core-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | legal: Singapore: MAS Notice 658 requires an appropriate approving authority for outsourcing, proportionate to its scale and complexity. Obtain the bank's actual delegated authority.
Applies only: A bank's outsourced relevant service within Notice 658.
Source I:SG-BANK-OUTSOURCE: MAS Notice 658 Management of Outsourced Relevant Services for Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/notices/bd/notice-658/mas-notice-658---4.pdf?hash=F4A9B72C07037B0DB0E32C6FEF3B8CD5&sc_lang=en>. Checked 2026-11-03. Effective 11 December 2024. Applies to banks; merchant banks have Notice 1121. Not every software purchase is an outsourced relevant service.

decision_approvers | scope MY | legal: Malaysia: the bank's board approves its outsourcing framework; obtain approval evidence from the authority designated in that framework.
Applies only: A listed BNM regulated institution and in-scope outsourcing; apply policy exceptions.
Source I:MY-OUTSOURCE: Outsourcing policy document BNM/RH/PD 028-93 <https://www.bnm.gov.my/documents/20124/938039/PD_Outsourcing_20191023.pdf/115dc006-4220-44ff-e443-7dc6e9a9a2f5?t=1592250636323>. Checked 2026-11-03. Primary PDF read; current BNM bank and insurance index still lists this version. Apply only to listed institutions and consider current RMiT interaction, affiliate exceptions and local branch scope.

decision_approvers | scope ID | operating: Indonesia: the current bank IT framework assigns roles to directors, commissioners and the IT steering committee. Check its annexes and the bank's delegation for the precise approval.
Applies only: Commercial bank IT review; the source abstract does not establish a specific purchase signatory.
Source I:ID-BANK-IT-2026: PADK 1 Tahun 2026 Penyelenggaraan Teknologi Informasi oleh Bank Umum <https://ojk.go.id/id/regulasi/Pages/PADK-1-Tahun-2026-Penyelenggaraan-Teknologi-Informasi-oleh-Bank-Umum.aspx>. Checked 2026-11-03. Primary indexed abstract read; live page timed out. Effective 1 March 2026, supersedes SEOJK 21/2017. Detailed Annex I to IV obligations are still waiting for source review. No specific permission or hosting conclusion inferred.

sector_regulator | scope SG | legal: Singapore: Banking Act section 7 provides the MAS bank licence application route and allows activity conditions. Establish the bank category before mapping the core banking deployment.
Applies only: Banking business in scope; merchant bank provisions and exceptions require separate review.
Source I:SG-BANK-LICENCE: Banking Act 1970 section 7 <https://sso.agc.gov.sg/Act/BA1970?ProvIds=pr7->. Checked 2026-11-03. Primary indexed current version at 7 October 2026 read. Subject to section 55S and the Act's scope. Does not license a software supplier.

sector_regulator | scope MY | operating: Malaysia: confirm the bank's BNM licence and whether the Financial Services Act, Islamic Financial Services Act or development institution regime applies before selecting the deployment conditions.
Applies only: Only the listed institution categories; precise licence application requirements remain pending.
Source I:MY-OUTSOURCE: Outsourcing policy document BNM/RH/PD 028-93 <https://www.bnm.gov.my/documents/20124/938039/PD_Outsourcing_20191023.pdf/115dc006-4220-44ff-e443-7dc6e9a9a2f5?t=1592250636323>. Checked 2026-11-03. Primary PDF read; current BNM bank and insurance index still lists this version. Apply only to listed institutions and consider current RMiT interaction, affiliate exceptions and local branch scope.

sector_regulator | scope ID | legal: Indonesia: PADK 1/2026 is OJK's current commercial bank IT framework, effective March 2026; its annexes cover overseas electronic system and transaction processing permissions.
Applies only: Commercial banks under POJK 11/2022; this note identifies the framework, not a permission outcome.
Source I:ID-BANK-IT-2026: PADK 1 Tahun 2026 Penyelenggaraan Teknologi Informasi oleh Bank Umum <https://ojk.go.id/id/regulasi/Pages/PADK-1-Tahun-2026-Penyelenggaraan-Teknologi-Informasi-oleh-Bank-Umum.aspx>. Checked 2026-11-03. Primary indexed abstract read; live page timed out. Effective 1 March 2026, supersedes SEOJK 21/2017. Detailed Annex I to IV obligations are still waiting for source review. No specific permission or hosting conclusion inferred.

procurement_payment | scope MY | legal: Malaysia: RMiT requires first adoption of public cloud for critical systems to be discussed with BNM; later adoption uses conditional notification. Check institution exemptions and the current Appendix 7 evidence.
Applies only: A bank within RMiT Part C, paragraphs 17.1 to 17.4; not all cloud use.
Source I:MY-RMIT-2026: Risk Management in Technology BNM/RH/PD 028-98 <https://www.bnm.gov.my/documents/20124/938039/pd-rmit-sep26.pdf>. Checked 2026-11-03. Current primary PDF. Effective and transitional provisions vary; Part C excludes designated payment system operators, eligible e-money issuers, nonbank merchant acquirers and intermediary remittance institutions. No blanket bank cloud approval claim.

data_privacy | scope SG | legal: Singapore: Notice 658 controls customer information access and confidentiality, including contractual treatment when the service ends.
Applies only: A bank outsourcing customer information within Notice 658.
Source I:SG-BANK-OUTSOURCE: MAS Notice 658 Management of Outsourced Relevant Services for Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/notices/bd/notice-658/mas-notice-658---4.pdf?hash=F4A9B72C07037B0DB0E32C6FEF3B8CD5&sc_lang=en>. Checked 2026-11-03. Effective 11 December 2024. Applies to banks; merchant banks have Notice 1121. Not every software purchase is an outsourced relevant service.

data_privacy | scope MY | legal: Malaysia: where the bank relies on customer consent for disclosure, preserve explicit consent and withdrawal evidence. Statutory permitted disclosures require a separate basis check.
Applies only: Customer information within the BNM policy and consent based disclosure scope.
Source I:MY-CUSTOMER-DATA: Management of Customer Information and Permitted Disclosures <https://www.bnm.gov.my/documents/20124/938039/MCIPD_PD_2025.pdf>. Checked 2026-11-03. Primary PDF checked 3 November 2026. Paragraphs 2.1, 2.2 and 5.2 distinguish FSPs from financial institutions. Insurer and takaful lifecycle policies use Part B paragraph 10.6; do not extend Part C consent conditions to them.

data_privacy | scope ID | legal: Indonesia: PADK 1/2026 expressly covers data management and personal data protection for commercial bank IT. Validate the annex requirements alongside the applicable PDP law duties.
Applies only: Commercial bank processing in scope; no unverified localisation or transfer permission is asserted.
Source I:ID-BANK-IT-2026: PADK 1 Tahun 2026 Penyelenggaraan Teknologi Informasi oleh Bank Umum <https://ojk.go.id/id/regulasi/Pages/PADK-1-Tahun-2026-Penyelenggaraan-Teknologi-Informasi-oleh-Bank-Umum.aspx>. Checked 2026-11-03. Primary indexed abstract read; live page timed out. Effective 1 March 2026, supersedes SEOJK 21/2017. Detailed Annex I to IV obligations are still waiting for source review. No specific permission or hosting conclusion inferred.
Source I:ID-PDP: Law No. 27 of 2022 on Personal Data Protection <https://jdih.komdigi.go.id/produk_hukum/view/id/832/t/crc32/>. Checked 2026-11-03. Primary indexed law entry read; live open timed out. Detailed transfer mechanisms and implementing rules not asserted.

proof | scope SG | operating: Singapore: present documented provider diligence and a demonstration of access limits and end of contract information handling against the bank's Notice 658 assessment.
Applies only: A proposed bank outsourcing; procurement evidence derived from the notice.
Source I:SG-BANK-OUTSOURCE: MAS Notice 658 Management of Outsourced Relevant Services for Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/notices/bd/notice-658/mas-notice-658---4.pdf?hash=F4A9B72C07037B0DB0E32C6FEF3B8CD5&sc_lang=en>. Checked 2026-11-03. Effective 11 December 2024. Applies to banks; merchant banks have Notice 1121. Not every software purchase is an outsourced relevant service.

proof | scope MY | operating: Malaysia: give the bank provider diligence, processing and backup locations, and internal approval evidence for its outsourcing review.
Applies only: Evidence derived from BNM outsourcing policy, with materiality and applicable exceptions assessed.
Source I:MY-OUTSOURCE: Outsourcing policy document BNM/RH/PD 028-93 <https://www.bnm.gov.my/documents/20124/938039/PD_Outsourcing_20191023.pdf/115dc006-4220-44ff-e443-7dc6e9a9a2f5?t=1592250636323>. Checked 2026-11-03. Primary PDF read; current BNM bank and insurance index still lists this version. Apply only to listed institutions and consider current RMiT interaction, affiliate exceptions and local branch scope.

proof | scope ID | operating: Indonesia: request an evidence map against PADK 1/2026 covering provider controls, internal audit, data protection and applicable overseas processing permission forms.
Applies only: A review checklist derived from the published abstract; detailed annex evidence remains pending.
Source I:ID-BANK-IT-2026: PADK 1 Tahun 2026 Penyelenggaraan Teknologi Informasi oleh Bank Umum <https://ojk.go.id/id/regulasi/Pages/PADK-1-Tahun-2026-Penyelenggaraan-Teknologi-Informasi-oleh-Bank-Umum.aspx>. Checked 2026-11-03. Primary indexed abstract read; live page timed out. Effective 1 March 2026, supersedes SEOJK 21/2017. Detailed Annex I to IV obligations are still waiting for source review. No specific permission or hosting conclusion inferred.

### lending | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | question: Singapore: identify the licensed moneylender's authorised signatory and borrower data reviewer from its licence and delegation policy.
Applies only: The current source does not establish a universal purchase approver.

sector_regulator | scope SG | legal: Singapore: licensed moneylenders fall under the Ministry of Law Registry of Moneylenders. Its rules include physical identity verification and do not allow a fully online loan transaction.
Applies only: Only licensed moneylenders under that regime; do not apply this condition to bank lending.
Source I:SG-LENDING: List of licensed moneylenders in Singapore <https://rom.mlaw.gov.sg/information-for-borrowers/list-of-licensed-moneylenders-in-singapore/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. This rule is for licensed moneylenders, not every bank or financial institution. No entity names copied.

sector_regulator | scope ID | legal: Indonesia: POJK 40 of 2024 addresses technology based joint funding services. Establish whether the platform is an intermediary in that regime before mapping OJK requirements.
Applies only: For LPBBTI activity only, not all lending or credit data software.
Source I:ID-LENDING: POJK 40 Tahun 2024 Layanan Pendanaan Bersama Berbasis Teknologi Informasi <https://ojk.go.id/id/regulasi/Pages/POJK-40-Tahun-2024-Layanan-Pendanaan-Bersama-Berbasis-Teknologi-Informasi.aspx>. Checked 2026-11-03. Entry gives effective date. Primary indexed abstract read; live open timed out. Do not extend P2P rules to every lender.

sector_regulator | scope PH | legal: Philippines: lending companies under the Lending Company Regulation Act, RA 9474, need the SEC authority for that business. Distinguish this entity from a BSP supervised bank.
Applies only: Only companies within RA 9474; software supply alone does not establish that activity.
Source I:PH-LENDING: Frequently asked questions on lending companies <https://www.sec.gov.ph/wp-content/uploads/2019/11/2019FAQ_LendingCompanies.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Undated FAQ. Used only for basic entity boundary; no capital requirement or current platform procedure asserted.

data_privacy | scope SG | legal: Singapore: a licensed moneylender's borrower identity records require applicable PDPA protection and retention controls.
Applies only: Personal data processing within the PDPA; separate the moneylender regime from bank lending.
Source I:SG-PDPA: Data protection obligations under the Personal Data Protection Act <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Resource-for-Organisation/Data-Protection-Obligations-under-the-PDPA.ashx?la=en>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Document states May 2021. Used only for these stable obligations, not its uncommenced data portability item. Check exceptions and current regulations.

proof | scope SG | operating: Singapore: for a licensed moneylender, demonstrate the physical identity verification handoff; a wholly online loan journey would not meet the Registry's stated requirement.
Applies only: Only Ministry of Law licensed moneylenders, not a blanket rule for all lenders.
Source I:SG-LENDING: List of licensed moneylenders in Singapore <https://rom.mlaw.gov.sg/information-for-borrowers/list-of-licensed-moneylenders-in-singapore/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. This rule is for licensed moneylenders, not every bank or financial institution. No entity names copied.

### wealth-investment | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the financial adviser's board and senior management oversee outsourcing under applicable MAS nonbank guidelines; confirm the delegated purchase approver.
Applies only: Only an institution and outsourcing arrangement within these supervisory guidelines.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

sector_regulator | scope SG | legal: Singapore: regulated financial advice under the Financial Advisers Act 2001 requires the relevant MAS licence unless exempt. Separate advice from general information or software supply.
Applies only: For the actual regulated activity and applicable exemptions.
Source I:SG-ADVISERS: Financial adviser's licence <https://www.mas.gov.sg/regulation/capital-markets/apply-for-licensing-or-registration-of-capital-market-entities/financial-advisers>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Investment advice is distinct from general financial software.

sector_regulator | scope ID | legal: Indonesia: OJK supervises capital market activities in its remit. Identify the investment service and regulated entity.
Applies only: For capital market activities in Indonesia within OJK's authority.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Securities Commission Malaysia regulates capital market services under the Capital Markets and Services Act 2007. Map the actual regulated activity.
Applies only: For capital market entities and services within that Act.
Source I:MY-SC: About the Securities Commission Malaysia <https://www.sc.com.my/about/about/about-the-sc>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Entity and activity licensing must be checked separately.

sector_regulator | scope TH | legal: Thailand: the Securities and Exchange Commission supervises the Thai capital market. Establish the investment activity and regulated entity before selecting obligations.
Applies only: For capital market activities within the Thai SEC's remit.
Source I:TH-SEC: Enforcement <https://www.sec.or.th/EN/pages/lawandregulations/enforcement.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not every wealth related software activity needs the same authorisation.

sector_regulator | scope BN | legal: Brunei capital market activity is governed by BDCB's Securities Markets Order 2013 and Securities Markets Regulations 2014 framework. Confirm the dealing, management, advice or custody permission for the actual activity.
Applies only: Capital market intermediary or other activity within the named framework
Source I:BN-WEALTH: Capital market regulatory framework <https://www.bdcb.gov.bn/regulatory/capital-market>. Checked 2026-11-03. Undated current regulator overview; confirm current licence permissions and supplementary requirements.

data_privacy | scope SG | operating: Singapore: for in-scope financial adviser outsourcing, demonstrate confidentiality, audit access and an exit plan.
Applies only: MAS nonbank outsourcing guidelines; a supervisory expectation, not a universal vendor licence.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

proof | scope SG | operating: Singapore: show how the advice workflow preserves client information, needs analysis, product knowledge assessment and recommendation records under FAA-N16.
Applies only: Financial advisers and representatives in the notice's scope; demonstrate with synthetic client records.
Source I:SG-ADVICE-RECORDS: Notice FAA-N16 Recommendations on Investment Products <https://www.mas.gov.sg/regulation/notices/notice-faa-n16>. Checked 2026-11-03. Last revised date. Applies to stated advisers representatives and exempt service companies. No assumption that fund management or execution alone is financial advice.

### spend-expense | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | question: Singapore: who approves the expense, verifies the GST evidence and authorises the software purchase under the buyer's own delegation policy?
Applies only: Ask the buyer; the IRAS evidence rule does not name its internal purchase signatory.

sector_regulator | scope SG | operating: Singapore: separate expense records and IRAS tax evidence from a payment service requiring MAS authorisation. Map any money movement before deciding the latter.
Applies only: Expense software versus a regulated payment service; no licensing conclusion without the service facts.
Source I:SG-EXPENSE-GST: Expenses Incurred by Employee on Behalf of the Company <https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/claiming-gst-(input-tax)/common-scenarios---do-i-claim-gst/expenses-incurred-by-employee-on-behalf-of-the-company>. Checked 2026-11-03. Page update date. Other input tax conditions apply. Does not establish eligibility for any particular claim or prescribe the buyer's purchase approver.
Source I:SG-PAYMENTS: Payments regulation <https://www.mas.gov.sg/regulation/payments>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish that all payment software suppliers provide a regulated service.

data_privacy | scope SG | legal: Singapore: employee receipts containing personal data need PDPA protection and retention controls; overseas handling requires the applicable transfer safeguards.
Applies only: An organisation and personal data processing within the PDPA, subject to its exceptions.
Source I:SG-PDPA: Data protection obligations under the Personal Data Protection Act <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Resource-for-Organisation/Data-Protection-Obligations-under-the-PDPA.ashx?la=en>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Document states May 2021. Used only for these stable obligations, not its uncommenced data portability item. Check exceptions and current regulations.

proof | scope SG | operating: Singapore: show the invoice, employee agency evidence, reimbursement and business accounting trail. Separate private expenses; IRAS input tax eligibility has further conditions.
Applies only: A GST registered employer considering input tax for employee expenses.
Source I:SG-EXPENSE-GST: Expenses Incurred by Employee on Behalf of the Company <https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/claiming-gst-(input-tax)/common-scenarios---do-i-claim-gst/expenses-incurred-by-employee-on-behalf-of-the-company>. Checked 2026-11-03. Page update date. Other input tax conditions apply. Does not establish eligibility for any particular claim or prescribe the buyer's purchase approver.

### insurance | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the insurer's board and senior management oversee outsourcing under applicable MAS nonbank guidelines; confirm the delegated purchase approver.
Applies only: Only an institution and outsourcing arrangement within these supervisory guidelines.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

decision_approvers | scope MY | legal: Malaysia: the insurer or takaful operator's board approves its outsourcing framework; obtain approval evidence from the authority designated in that framework.
Applies only: A listed BNM regulated institution and in-scope outsourcing; apply policy exceptions.
Source I:MY-OUTSOURCE: Outsourcing policy document BNM/RH/PD 028-93 <https://www.bnm.gov.my/documents/20124/938039/PD_Outsourcing_20191023.pdf/115dc006-4220-44ff-e443-7dc6e9a9a2f5?t=1592250636323>. Checked 2026-11-03. Primary PDF read; current BNM bank and insurance index still lists this version. Apply only to listed institutions and consider current RMiT interaction, affiliate exceptions and local branch scope.

sector_regulator | scope SG | legal: Singapore: MAS is the responsible agency for the Insurance Act 1966. Identify whether the buyer is an insurer, insurance intermediary or another service provider.
Applies only: For insurance business and entities within the Act; no licence conclusion for a software vendor.
Source I:SG-INSURANCE: Sectoral legislation with ownership and control provisions <https://www.osir.gov.sg/resources/other-legislation/sectoral-legislation/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used to identify regulator and legal instrument, not detailed ownership approval conditions.

sector_regulator | scope ID | legal: Indonesia: OJK's remit includes insurance. Have the insurer or intermediary identify the current instrument for its activity.
Applies only: For insurance entities under OJK supervision.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Bank Negara Malaysia's insurance and takaful supervision covers the institutions within its remit. Confirm the insurance or takaful entity before the compliance review.
Applies only: For the applicable BNM supervised institution.
Source I:MY-BNM: Supervision <https://www.bnm.gov.my/supervision>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not cover every nonbank lender or every capital market service.

sector_regulator | scope PH | legal: Philippines: the Insurance Commission supervises insurance under the Insurance Code. Start the review with the insurer or intermediary's actual role.
Applies only: For insurance activity within the Commission's remit.
Source I:PH-INSURANCE: Mandate, objectives and functions <https://site.insurance.gov.ph/about/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not a licence determination for a software provider.

sector_regulator | scope BN | legal: In Brunei, BDCB supervises insurance and takaful. Distinguish the Insurance Order 2006 and Takaful Order 2008, and confirm whether the buyer is an insurer, operator or intermediary.
Applies only: Insurance or takaful activity within BDCB supervision; check any international regime separately
Source I:BN-INSURANCE: Takaful and insurance regulatory framework <https://www.bdcb.gov.bn/index.php/regulatory/takaful-insurance>. Checked 2026-11-03. Undated current regulator overview. International insurance and intermediary regimes may differ; no detailed licence requirement inferred.

sector_regulator | scope SG | legal: Singapore: MAS distinguishes licensed insurers, authorised reinsurers and registered or exempt brokers. Confirm the entity and permission under the Insurance Act before choosing the sales route.
Applies only: Actual insurance or intermediary activity; software supply alone does not determine licensing.
Source I:SG-INSURANCE-TYPES: Types of Insurance Entities <https://www.mas.gov.sg/regulation/Insurance/Types-of-Insurers-in-Singapore>. Checked 2026-11-03. Live primary page read. No page publication date supplied. Entity and activity must be established before choosing a route.

data_privacy | scope SG | operating: Singapore: for in-scope insurer outsourcing, demonstrate confidentiality, audit access and an exit plan.
Applies only: MAS nonbank outsourcing guidelines; a supervisory expectation, not a universal vendor licence.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

data_privacy | scope MY | legal: Malaysia: licensed insurers and takaful operators must maintain written policies and procedures covering the customer information lifecycle.
Applies only: BNM Management of Customer Information and Permitted Disclosures, issued 31 October 2025: Part B, paragraphs 2.1, 5.2 and 10.6. Part C applies only to its separately defined financial institutions; do not infer insurer consent requirements from it.
Source I:MY-CUSTOMER-DATA: Management of Customer Information and Permitted Disclosures <https://www.bnm.gov.my/documents/20124/938039/MCIPD_PD_2025.pdf>. Checked 2026-11-03. Primary PDF checked 3 November 2026. Paragraphs 2.1, 2.2 and 5.2 distinguish FSPs from financial institutions. Insurer and takaful lifecycle policies use Part B paragraph 10.6; do not extend Part C consent conditions to them.

proof | scope SG | operating: Singapore: show the insurer or broker's applicable permission and the data access and exit evidence requested in its outsourcing review.
Applies only: Only the relevant insurance entity and in-scope outsourcing arrangement.
Source I:SG-INSURANCE-TYPES: Types of Insurance Entities <https://www.mas.gov.sg/regulation/Insurance/Types-of-Insurers-in-Singapore>. Checked 2026-11-03. Live primary page read. No page publication date supplied. Entity and activity must be established before choosing a route.
Source I:SG-NONBANK-OUTSOURCE: Guidelines on Outsourcing Financial Institutions other than Banks <https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-outsourcing/guidelines-on-outsourcing--financial-institutions-other-than-banks-updated.pdf>. Checked 2026-11-03. Supervisory guidelines, not a new vendor licence. Apply to the financial institutions in scope, not every Singapore moneylender or corporate expense buyer.

proof | scope MY | operating: Malaysia: give the insurer or takaful operator provider diligence, processing and backup locations, and internal approval evidence for its outsourcing review.
Applies only: Evidence derived from BNM outsourcing policy, with materiality and applicable exceptions assessed.
Source I:MY-OUTSOURCE: Outsourcing policy document BNM/RH/PD 028-93 <https://www.bnm.gov.my/documents/20124/938039/PD_Outsourcing_20191023.pdf/115dc006-4220-44ff-e443-7dc6e9a9a2f5?t=1592250636323>. Checked 2026-11-03. Primary PDF read; current BNM bank and insurance index still lists this version. Apply only to listed institutions and consider current RMiT interaction, affiliate exceptions and local branch scope.

### customer-service | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### crm-marketing | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### collaboration | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-growth | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### construction | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### property-management | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### field-services | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### fmcg-retail-execution | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### industry-hr-payroll | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### hotel-lodging | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### retail-restaurant-ops | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### agents-copilots | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### voice-language-models | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### enterprise-search | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### it-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### bpo-cx | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-engineering | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### operators-connectivity | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SG | operating: Singapore: establish the operating entity and IMDA service licence category; a software supplier is not automatically the licensed service operator.
Applies only: Services Based Operations scope; facilities based operations need their separate route.
Source I:SG-TELECOM: Services Based Operations licence <https://www.imda.gov.sg/regulations-and-licensing-listing/services-based-operations--sbo--licence>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Primary indexed page extract read; live open returned a script challenge. No specific licence conditions asserted.

### cpaas-messaging | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the organisation designates its registry administrator and identifies its participating aggregator; verify the sender belongs to that organisation.
Applies only: SSIR account and sender administration, not buyer purchase delegation.
Source I:SG-SMS-REGISTRY: Overview of SMS Sender ID Registry <https://www.sgnic.sg/smsregistry/overview>. Checked 2026-11-03. Current primary registry operator page read; no full publication date. Scope is SMS Sender IDs used for Singapore mobile users. No price, software recommendation or claim that registration substitutes for messaging consent.

sector_regulator | scope SG | legal: Singapore: organisations using SMS Sender IDs for Singapore mobile users must register them with SSIR.
Applies only: Sender ID registry scope; messaging consent obligations remain separate.
Source I:SG-SMS-REGISTRY: Overview of SMS Sender ID Registry <https://www.sgnic.sg/smsregistry/overview>. Checked 2026-11-03. Current primary registry operator page read; no full publication date. Scope is SMS Sender IDs used for Singapore mobile users. No price, software recommendation or claim that registration substitutes for messaging consent.

### telecom-software | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### business-voice-ucaas | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### developer-platform | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-infrastructure | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### observability | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### testing | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### dev-tools | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### cloud-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope BN | legal: Brunei: planned CII cloud implementation requires owner risk acceptance and Commissioner review.
Applies only: CII code section 3.6, including required rectification.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends documenting cloud security responsibilities and incident escalation.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### identity-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope BN | legal: Brunei: CII vendor access must be documented, preapproved, supervised and on site.
Applies only: CII code section 5.1.3; verify any applicable exception separately.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

proof | scope SG | operating: Singapore: PDPC guidance recommends role based access and reviews when staff change roles.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### email-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends phishing exercises and clear incident reporting processes.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### awareness-training | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends recurring training and checks of staff awareness.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends testing exception paths for personal data exposure.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### mobile-appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends protecting personal data on devices and testing data flows.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### soc-services | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the provider names its Key Executive Officer and key officers in the licence application. Ask the customer separately who may authorise the service and purchase.
Applies only: Provider accountability is sourced; buyer purchase delegation is not inferred.
Source I:SG-CYBER-LICENCE: Apply for Licence <https://www.csro.gov.sg/how-to/apply-for-licence/>. Checked 2026-11-03. Live primary page. Licence application and provider responsibility are distinct from the customer purchase approval. CTM grace runs to 31 December 2026.

decision_approvers | scope MY | operating: Malaysia: a company licence application appoints a responsible person and supplies company and qualification evidence. The buyer must identify its own approval delegation.
Applies only: Provider application responsibility only; not a prescribed customer signatory.
Source I:MY-CYBER-APPLICATION: Cyber Security Service Provider licence application guideline <https://www.nacsa.gov.my/application-licensing.php>. Checked 2026-11-03. Live primary page. Provider application responsible person is not the buyer contract approver; no universal buyer title asserted.

sector_regulator | scope SG | legal: Singapore: managed SOC monitoring is a licensable service under the Cybersecurity Act. Apply through CSRO; a provider offering both licensable services needs each category.
Applies only: Actual licensable service, subject to the related company exception.
Source I:SG-CYBER-LICENCE: Apply for Licence <https://www.csro.gov.sg/how-to/apply-for-licence/>. Checked 2026-11-03. Live primary page. Licence application and provider responsibility are distinct from the customer purchase approval. CTM grace runs to 31 December 2026.

sector_regulator | scope MY | legal: Malaysia: managed SOC monitoring falls within NACSA provider licensing. Check the service definition and exemptions before relying on a licence conclusion.
Applies only: Act 854 and P.U. A 221/2024, including territorial and entity exclusions.
Source I:MY-CYBER-LICENCE: Cyber Security Service Provider Licensing FAQ <https://www.nacsa.gov.my/doc/FAQ%20LICENSING%20SERVICE%20PROVIDER.pdf>. Checked 2026-11-03. Live primary PDF. No reliable full publication date. Do not extend the two licensed service categories to every security software product; check statutory exclusions.

data_privacy | scope SG | legal: Singapore: information obtained through managed SOC monitoring is limited to providing that service; other uses require appropriate written customer consent or a lawful exception.
Applies only: Licensed service provider and customer information within condition 3.1(e).
Source I:SG-CYBER-CONDITIONS: Closing note and updated cybersecurity licence conditions <https://www.csa.gov.sg/legislation/consultations/closing-note-to-the-consultation-on-the-licensing-framework-for-cybersecurity-service-providers/>. Checked 2026-11-03. Final closing note with operative condition text, not a consultation proposal. Standalone conditions PDF returned 404, so scope is cross checked against current CSRO FAQ. DPTM is not a mandatory certification in the final response.

data_privacy | scope MY | legal: Malaysia: map any personal data in managed SOC monitoring logs or reports to the applicable PDPA processing, security and disclosure duties.
Applies only: Personal data and commercial processing within Malaysia PDPA scope; sector duties require separate assessment.
Source I:MY-PDPA: Application and non application of the Personal Data Protection Act <https://www.pdp.gov.my/en/akta/application-and-non-application-of-the-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used only for scope. Read Act 709 as amended and current commencement instruments before specific obligations.

proof | scope SG | operating: Singapore: show the managed SOC monitoring licence, traceable service records and certification scope covering the delivery environment.
Applies only: Evidence derived from current CSRO guidance; it does not guarantee technical outcomes.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope MY | operating: Malaysia: provide the NACSA managed SOC monitoring licence and matching qualification and experience evidence; agree the customer evidence access and acceptance process.
Applies only: Licence and provider evidence only, not a universal product certification.
Source I:MY-CYBER-LICENCE: Cyber Security Service Provider Licensing FAQ <https://www.nacsa.gov.my/doc/FAQ%20LICENSING%20SERVICE%20PROVIDER.pdf>. Checked 2026-11-03. Live primary PDF. No reliable full publication date. Do not extend the two licensed service categories to every security software product; check statutory exclusions.
Source I:MY-CYBER-APPLICATION: Cyber Security Service Provider licence application guideline <https://www.nacsa.gov.my/application-licensing.php>. Checked 2026-11-03. Live primary page. Provider application responsible person is not the buyer contract approver; no universal buyer title asserted.

### endpoint-network | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends current endpoint defences and documented malware response.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### document-ai | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### ai-video | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### engineering-talent | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-management | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-adoption | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### pentest | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SG | operating: Singapore: the provider names its Key Executive Officer and key officers in the licence application. Ask the customer separately who may authorise the service and purchase.
Applies only: Provider accountability is sourced; buyer purchase delegation is not inferred.
Source I:SG-CYBER-LICENCE: Apply for Licence <https://www.csro.gov.sg/how-to/apply-for-licence/>. Checked 2026-11-03. Live primary page. Licence application and provider responsibility are distinct from the customer purchase approval. CTM grace runs to 31 December 2026.

decision_approvers | scope MY | operating: Malaysia: a company licence application appoints a responsible person and supplies company and qualification evidence. The buyer must identify its own approval delegation.
Applies only: Provider application responsibility only; not a prescribed customer signatory.
Source I:MY-CYBER-APPLICATION: Cyber Security Service Provider licence application guideline <https://www.nacsa.gov.my/application-licensing.php>. Checked 2026-11-03. Live primary page. Provider application responsible person is not the buyer contract approver; no universal buyer title asserted.

decision_approvers | scope BN | legal: Brunei: the CII owner supervises external testing to keep it within scope and avoid disruption.
Applies only: CII code section 5.15.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

sector_regulator | scope SG | legal: Singapore: penetration testing is a licensable service under the Cybersecurity Act. Apply through CSRO; a provider offering both licensable services needs each category.
Applies only: Actual licensable service, subject to the related company exception.
Source I:SG-CYBER-LICENCE: Apply for Licence <https://www.csro.gov.sg/how-to/apply-for-licence/>. Checked 2026-11-03. Live primary page. Licence application and provider responsibility are distinct from the customer purchase approval. CTM grace runs to 31 December 2026.

sector_regulator | scope MY | legal: Malaysia: penetration testing falls within NACSA provider licensing. Check the service definition and exemptions before relying on a licence conclusion.
Applies only: Act 854 and P.U. A 221/2024, including territorial and entity exclusions.
Source I:MY-CYBER-LICENCE: Cyber Security Service Provider Licensing FAQ <https://www.nacsa.gov.my/doc/FAQ%20LICENSING%20SERVICE%20PROVIDER.pdf>. Checked 2026-11-03. Live primary PDF. No reliable full publication date. Do not extend the two licensed service categories to every security software product; check statutory exclusions.

data_privacy | scope SG | legal: Singapore: information obtained through penetration testing is limited to providing that service; other uses require appropriate written customer consent or a lawful exception.
Applies only: Licensed service provider and customer information within condition 3.1(e).
Source I:SG-CYBER-CONDITIONS: Closing note and updated cybersecurity licence conditions <https://www.csa.gov.sg/legislation/consultations/closing-note-to-the-consultation-on-the-licensing-framework-for-cybersecurity-service-providers/>. Checked 2026-11-03. Final closing note with operative condition text, not a consultation proposal. Standalone conditions PDF returned 404, so scope is cross checked against current CSRO FAQ. DPTM is not a mandatory certification in the final response.

data_privacy | scope MY | legal: Malaysia: map any personal data in penetration testing logs or reports to the applicable PDPA processing, security and disclosure duties.
Applies only: Personal data and commercial processing within Malaysia PDPA scope; sector duties require separate assessment.
Source I:MY-PDPA: Application and non application of the Personal Data Protection Act <https://www.pdp.gov.my/en/akta/application-and-non-application-of-the-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used only for scope. Read Act 709 as amended and current commencement instruments before specific obligations.

proof | scope SG | operating: Singapore: show the penetration testing licence, traceable service records and certification scope covering the delivery environment.
Applies only: Evidence derived from current CSRO guidance; it does not guarantee technical outcomes.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope MY | operating: Malaysia: provide the NACSA penetration testing licence and matching qualification and experience evidence; agree the customer evidence access and acceptance process.
Applies only: Licence and provider evidence only, not a universal product certification.
Source I:MY-CYBER-LICENCE: Cyber Security Service Provider Licensing FAQ <https://www.nacsa.gov.my/doc/FAQ%20LICENSING%20SERVICE%20PROVIDER.pdf>. Checked 2026-11-03. Live primary PDF. No reliable full publication date. Do not extend the two licensed service categories to every security software product; check statutory exclusions.
Source I:MY-CYBER-APPLICATION: Cyber Security Service Provider licence application guideline <https://www.nacsa.gov.my/application-licensing.php>. Checked 2026-11-03. Live primary page. Provider application responsible person is not the buyer contract approver; no universal buyer title asserted.

proof | scope BN | legal: Brunei: CII testers need recognized certification and providers need recognized accreditation, such as CREST or equivalent.
Applies only: CII code section 5.15; not a recommendation of a software vendor.
Source I:BN-CII-CODE: Cybersecurity Code of Practice for Critical Information Infrastructure 2023 <https://www.csb.gov.bn/sites/default/files/downloads/CodeOfPractice/Code_of_Practice_for_Critical_Information_Infrastrcture_(CII)_-_Public_Release.pdf>. Checked 2026-11-03. Public primary PDF sections 3.1 3.6 3.7 5.1 and 5.15 read. Initial release date printed 11/03/2024; full ISO date left blank rather than assuming day order. CII scope only; check designation and compliance date.

### attack-surface-dast | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SG | legal: Singapore: software-only supply falls outside CSRO service licensing; reassess bundled services.
Applies only: Software-only supply.
Source I:SG-CYBER-FAQ: Cybersecurity service provider licensing FAQ <https://www.csro.gov.sg/resources/faq/>. Checked 2026-11-03. Live primary page. Applies to the defined licensed services; software suppliers are not licensed solely because their tools support providers.

proof | scope SG | operating: Singapore: PDPC guidance recommends periodic web vulnerability assessment after deployment.
Applies only: Personal data systems; guidance.
Source I:SG-ICT-PRACTICES: Guide to Data Protection Practices for ICT Systems <https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/tech-omnibus/guide-to-data-protection-practices-for-ict-systems.pdf>. Checked 2026-11-03. Primary PDF read. Regulator guidance index lists July 2026 but this retrieved PDF has no verified full revision date. Recommendations are not a universal software certification requirement.

### process-orchestration | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### open-source-support | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### iot-connectivity | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

## Middle East

Draft for owner review. Country scoped notes cover the UAE, Saudi Arabia, Qatar, Bahrain, Oman and Kuwait, with activity specific gaps still marked. No Gulf wide regulatory or buying habit claim is made. UAE federal, DIFC and ADGM scopes, and Qatar QCB and QFC scopes, must be distinguished. A city alone does not select a special financial regime. Other Middle East jurisdictions are not covered and must never inherit a neighbouring country's law.
Countries: AE = United Arab Emirates; SA = Saudi Arabia; QA = Qatar; BH = Bahrain; OM = Oman; KW = Kuwait
Clues, only in selling context: {"aliases":["Middle East","Gulf","GCC"],"countries":[{"code":"AE","name":"United Arab Emirates","aliases":["UAE"],"cities":["Dubai","Abu Dhabi","Sharjah"],"currencies":["AED","UAE dirham"],"regulators":["Central Bank of the United Arab Emirates","CBUAE","Dubai Financial Services Authority","DFSA","Financial Services Regulatory Authority","FSRA","Telecommunications and Digital Government Regulatory Authority","TDRA"]},{"code":"SA","name":"Saudi Arabia","aliases":["Kingdom of Saudi Arabia","KSA"],"cities":["Riyadh","Jeddah","Dammam"],"currencies":["SAR","Saudi riyal"],"regulators":["Saudi Central Bank","SAMA","Saudi Data and AI Authority","SDAIA","Zakat Tax and Customs Authority","ZATCA"]},{"code":"QA","name":"Qatar","aliases":[],"cities":["Doha"],"currencies":["QAR","Qatari riyal"],"regulators":[]},{"code":"BH","name":"Bahrain","aliases":[],"cities":["Manama"],"currencies":["BHD","Bahraini dinar"],"regulators":[]},{"code":"OM","name":"Oman","aliases":[],"cities":["Muscat"],"currencies":["OMR","Omani rial"],"regulators":[]},{"code":"KW","name":"Kuwait","aliases":[],"cities":["Kuwait City"],"currencies":["KWD","Kuwaiti dinar"],"regulators":[]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country, legal entity and activity are in scope, and who approves budget, risk and the purchase?

procurement_payment | scope AE | legal: UAE: electronic invoicing is being implemented in phases. Have the finance owner establish the entity's applicable implementation and preparation dates from the current FTA notice.
Applies only: For persons and transactions subject to the electronic invoicing regime. Do not assume every business already has the same deadline.
Source I:AE-INVOICE: FTA calls on persons subject to electronic invoicing to comply with deadlines <https://tax.gov.ae/en/media.centre/News/federal.tax.authority.calls.on.persons.subject.to.einvoicing.to.comply.wit.the.prescribed.legal.deadlines.and.avoid.administrative.penalties.aspx>. Checked 2026-11-03. Latest accessed notice differs from the older provider designation deadline. No thresholds or universal immediate obligation asserted.

procurement_payment | scope SA | legal: Saudi Arabia: ZATCA distinguishes invoice generation requirements from integration requirements introduced in notified waves. Ask finance which phase and notice apply.
Applies only: For taxpayers and invoices within the electronic invoicing rules; nonresident and other exclusions require checking.
Source I:SA-INVOICE: Electronic invoice rollout phases <https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. No universal integration deadline, tax rate or revenue threshold asserted.

data_privacy | scope AE | legal: UAE: Federal Decree Law 45 of 2021 on personal data has exclusions, including certain sector data and free zones with their own privacy laws. Identify the entity, data and legal regime before choosing controls.
Applies only: Apply only after checking Article 2 exclusions and the relevant implementation instruments. Do not infer DIFC or ADGM from a city name.
Source I:AE-PDPL: Federal Decree Law 45 of 2021 concerning the Protection of Personal Data <https://www.uaelegislation.gov.ae/en/legislations/1972/download>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Current executive instruments and implementation timing must be checked. No universal federal privacy or residency claim.

data_privacy | scope SA | legal: Saudi Arabia: the Personal Data Protection Law and the Regulation on Personal Data Transfer outside the Kingdom require an applicable transfer basis and protection review. Map overseas processing before agreeing the contract.
Applies only: For personal data transfers within the Saudi regime. This is not a blanket requirement to keep every type of data in Saudi Arabia.
Source I:SA-TRANSFER: Regulation on Personal Data Transfer outside the Kingdom <https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1g1Pz9L30o_ArAppiVOTr7JuuH1WQWJKhm5mXlq8fEeAS4GOkX5DtHg4A45XaIQ!!/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Read with Personal Data Protection Law and implementing regulations; no blanket local hosting requirement inferred.

data_privacy | scope QA | legal: For Qatar, identify whether Law No. 13 of 2016 on Protecting Personal Data Privacy governs the planned electronic processing. Record the controller, processor and purpose before selecting the contract and access checks.
Applies only: Processing within this law's scope; confirm the entity's legal regime before applying it
Source I:QA-PDP: Law No. 13 of 2016 on Protecting Personal Data Privacy <https://ncsa.gov.qa/shared/document_library/94787172324409/33000/8821/1.0~735ebb9c-e29e-4acb-a7ed-96449884a20b?filename=Law+No.+%2813%29+of+2016+on+Protecting+Personal+Data+Privacy.pdf&mimetype=application%2Fpdf>. Checked 2026-11-03. Regulator hosted English translation expressly says it is not the official Gazette text. Confirm Arabic law and the entity's regime, including whether separate QFC rules apply.

data_privacy | scope BH | legal: Bahrain has Law No. 30 of 2018 with Respect to Personal Data Protection Law. Identify the controller and processor and have the privacy reviewer confirm the current processing and transfer conditions for the proposed workflow.
Applies only: Personal data processing governed by Bahrain's law; current implementing decisions must be checked
Source I:BH-PDP: Law No. 30 of 2018 with Respect to Personal Data Protection Law <https://www.bahrain.bh/wps/wcm/connect/ab8b334e-8c6f-4ff9-90b6-94135da559ca/Law%2BNo.%2B%2830%29%2Bof%2B2018%2BDPL.pdf?CVID=oFapPNI&MOD=AJPERES>. Checked 2026-11-03. Government hosted EDB translation reflects provisions through January 2019 and is unofficial. Arabic prevails. Current implementing decisions and amendments need checking for a specific workflow.

data_privacy | scope OM | legal: In Oman, use the Personal Data Protection Law with the amendments in Royal Decree 68/2026. The amendments affect scope, exemptions and automated processing. Ask the privacy reviewer to confirm which provisions govern the data flow before using an older permit or consent checklist.
Applies only: Oman personal data processing within the amended law's scope
Source I:OM-PDP: Royal Decree 68/2026 amending the Personal Data Protection Law <https://www.mtcit.gov.om/library-3/legislations-policies-8/laws-75/royal-decree-68-2026-amending-some-provisions-of-the-personal-data-protection-law-1481>. Checked 2026-11-03. Official ministry summary and linked Arabic decree checked. No specific permit or consent requirement inferred from the summary.

data_privacy | scope KW | legal: For Kuwait, check the applicable scope of CITRA's Data Privacy Protection Regulation issued by Decision 26 of 2024. That decision replaced the regulation under Decision 42 of 2021, so an old 2021 checklist is not a sufficient basis for the review.
Applies only: Only where the current CITRA regulation covers the entity and service; scope requires confirmation
Source I:KW-PDP: Decision 26 of 2024 issuing the Data Privacy Protection Regulation <https://www.citra.gov.kw/sites/ar/Pages/DecisionsDetails.aspx?id=6>. Checked 2026-11-03. Arabic official decision read. Attached regulation's activity and entity scope still needs checking. Do not infer an economy wide obligation from the old 2021 English PDF.

buyer_language | scope COMMON | question: Which languages must the buying team, users, contract and notices support?

proof | scope COMMON | question: What sample workflow and acceptance evidence will the buyer approve?

objections | scope COMMON | question: Which hosting, access, integration, support or contract issue could block this purchase?

sales_motion | scope COMMON | question: Who owns the evaluation, acceptance decision and next purchase step?

### logistics-tech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: United Arab Emirates: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

decision_approvers | scope SA | operating: Saudi Arabia: the importer or exporter authorises its customs broker and defines the delegation scope and duration in Fasah.
Applies only: Customs delegation only; the software supplier is not automatically the broker.
Source I:SA-CUSTOMS-AUTH: Customs Broker Authorization <https://www.zatca.gov.sa/en/eServices/Pages/eServices-235.aspx>. Checked 2026-11-03. Live primary service page. Published date is service release date. Customs workflow does not mean a freight software supplier itself needs a customs broker licence.

proof | scope SA | operating: Saudi Arabia: demonstrate how the shipment workflow preserves the broker licence reference and the importer or exporter authorisation.
Applies only: Suggested evidence derived from the ZATCA delegation workflow.
Source I:SA-CUSTOMS-AUTH: Customs Broker Authorization <https://www.zatca.gov.sa/en/eServices/Pages/eServices-235.aspx>. Checked 2026-11-03. Live primary service page. Published date is service release date. Customs workflow does not mean a freight software supplier itself needs a customs broker licence.

### fintech | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope AE | legal: UAE: Federal Decree Law 6 of 2025 covers CBUAE licensed financial activities. Confirm the entity and whether a financial free zone regime applies before selecting obligations.
Applies only: For financial institutions and activities within the federal law; do not assume every UAE buyer is in its scope.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope AE | legal: If the activity is conducted in or from DIFC, check the Dubai Financial Services Authority regime with the contracting entity.
Applies only: DIFC financial activity only. Dubai city alone does not establish this scope.
Source I:AE-DFSA: About the DFSA <https://www.dfsa.ae/about-dfsa/who-we-are/the-dfsa>. Checked 2026-11-03. No reliable full publication date on the retrieved page. DIFC only. Dubai city does not establish DIFC jurisdiction.

sector_regulator | scope AE | legal: If the financial activity is in ADGM, check the Financial Services Regulatory Authority regime with the contracting entity.
Applies only: ADGM financial activity only. Abu Dhabi city alone does not establish this scope.
Source I:AE-FSRA: Financial Services Regulatory Authority <https://www.adgm.com/financial-services-regulatory-authority>. Checked 2026-11-03. No reliable full publication date on the retrieved page. ADGM only. Abu Dhabi city does not establish ADGM jurisdiction.

sector_regulator | scope SA | legal: Saudi Arabia: the Saudi Central Bank Law gives SAMA supervisory powers over financial institutions within relevant sector laws. Identify the activity and actual regulated entity.
Applies only: For financial institutions in SAMA's remit. Insurance and securities activities have separate subtype checks.
Source I:SA-SAMA: Saudi Central Bank Law <https://sama.gov.sa/en-US/About/Pages/bank-law.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Relevant sector laws determine the entity scope. Insurance remit is separately mapped to the Insurance Authority.

sector_regulator | scope QA | legal: For a Qatar institution supervised by Qatar Central Bank, confirm its regulated activity and licence category under Law No. 13 of 2012. QCB's supervision remit includes banks, insurance and relevant financial technology institutions.
Applies only: Institution subject to QCB supervision; do not infer this regime solely from a Doha address
Source I:QA-QCB: Supervision Sector <https://www.qcb.gov.qa/en/Supervision/pages/supervision-sector.aspx>. Checked 2026-11-03. Primary publisher search extract read; direct page fetch timed out. QFC authorisation is separately sourced. No detailed outsourcing or licence conditions asserted.

sector_regulator | scope QA | legal: For financial services conducted in or from the Qatar Financial Centre, check QFCRA authorisation under the framework established by Law No. 7 of 2005. Confirm the entity and authorised activity before choosing its regulatory checklist.
Applies only: Only financial services in or from the Qatar Financial Centre
Source I:QA-QFCRA: About Us <https://www.qfcra.com/about-us/>. Checked 2026-11-03. Official publisher search extract read; live fetch returned a server error. Does not establish which regime a named company uses.

sector_regulator | scope BH | legal: Bahrain's Central Bank and Financial Institutions Law places regulated financial services under CBB licensing and supervision. Confirm the buyer's licence category and applicable current Rulebook volume before defining approval evidence.
Applies only: Financial services regulated by the Central Bank of Bahrain
Source I:BH-CBB: Central Bank of Bahrain and Financial Institutions Law <https://www.cbb.gov.bh/wp-content/uploads/2018/12/THE_CENTRAL_BANK_OF_BAHRAIN_AND_FINANCIAL_INSTITUTIONS_LAW_ENGLISH.pdf>. Checked 2026-11-03. Official English text provides foundational remit. The legislation index lists amendments. Use the current activity specific CBB Rulebook for detailed obligations.

sector_regulator | scope OM | legal: For an Oman institution supervised by the Central Bank of Oman, use the Banking Law issued by Royal Decree 2/2025 and applicable current instructions. Confirm whether the buyer is a bank, finance or leasing company, exchange business or payment provider.
Applies only: Institution within Central Bank of Oman supervision
Source I:OM-BANK: Circular BM 1211 on Banking Law under Royal Decree 2/2025 <https://cbo.gov.om/sites/assets/Documents/Global/Circulars/2025/2025-01-20%20BM%201211%20-%20Issue%20of%20Banking%20Law%20%28Royal%20Decree%20No.%202-2025%29.pdf>. Checked 2026-11-03. Circular confirms new law and continuing compatible instructions. It does not itself establish detailed authorisation requirements for every fintech activity.

### vertical-saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

procurement_payment | scope SA | legal: Saudi Arabia: retail billing workflows must distinguish invoice generation from ZATCA integration waves; confirm the taxpayer notice before promising readiness.
Applies only: Taxpayers and invoices in scope, subject to applicable phase and exclusions.
Source I:SA-INVOICE: Electronic invoice rollout phases <https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. No universal integration deadline, tax rate or revenue threshold asserted.

proof | scope AE | operating: UAE: map the industry billing workflow to the FTA electronic invoicing timetable for the actual entity and transaction.
Applies only: Phased regime; this does not establish a universal immediate deadline.
Source I:AE-INVOICE: FTA calls on persons subject to electronic invoicing to comply with deadlines <https://tax.gov.ae/en/media.centre/News/federal.tax.authority.calls.on.persons.subject.to.einvoicing.to.comply.wit.the.prescribed.legal.deadlines.and.avoid.administrative.penalties.aspx>. Checked 2026-11-03. Latest accessed notice differs from the older provider designation deadline. No thresholds or universal immediate obligation asserted.

### ai-native | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: United Arab Emirates: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

decision_approvers | scope SA | operating: Saudi Arabia: SDAIA ethics guidance calls for the system owner and relevant stakeholders to accept the model after validation before production use.
Applies only: AI Ethics Principles guidance; actual contractual authority remains buyer specific.
Source I:SA-AI-ETHICS: AI Ethics Principles <https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf>. Checked 2026-11-03. Primary PDF read and current SDAIA regulatory index checked. No reliable full publication date. Presented as framework guidance, not a new statutory licence or guarantee of compliance.

proof | scope SA | operating: Saudi Arabia: demonstrate traceable decisions, privacy assessment and monitoring against the intended use case and the SDAIA principles.
Applies only: Evidence suggested from the framework, not a statutory approval certificate.
Source I:SA-AI-ETHICS: AI Ethics Principles <https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf>. Checked 2026-11-03. Primary PDF read and current SDAIA regulatory index checked. No reliable full publication date. Presented as framework guidance, not a new statutory licence or guarantee of compliance.

### ites | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Saudi Arabia: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

data_privacy | scope AE | legal: UAE: Article 8 of the federal personal data law describes processor work under controller instructions and a defined processing contract.
Applies only: First confirm Article 2 exclusions, entity regime and applicable executive instruments.
Source I:AE-PDPL: Federal Decree Law 45 of 2021 concerning the Protection of Personal Data <https://www.uaelegislation.gov.ae/en/legislations/1972/download>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Current executive instruments and implementation timing must be checked. No universal federal privacy or residency claim.

### telecom | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope AE | legal: UAE: TDRA issues licences for public telecommunications networks and services under the Telecommunications Law. Distinguish operating the service from supplying an operator.
Applies only: For activities requiring TDRA authorisation, not every telecom software supplier.
Source I:AE-TELECOM: Issue licences to provide telecommunication services <https://tdra.gov.ae/en/Services/issue-licences-to-provide-telecommunication-services>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not a requirement for every software vendor supplying an operator.

sector_regulator | scope SA | legal: Saudi Arabia's Telecommunications and Information Technology Bylaw gives CST service classification and authorisation responsibilities. Confirm the required licence, registration or permit for the actual service and which entity holds it.
Applies only: Telecommunications or information technology activity within CST's regulatory scope
Source I:SA-TELECOM: Telecommunications and Information Technology Bylaw <https://www.cst.gov.sa/en/regulations-and-licenses/acts-and-bylaws/bylaws/telecommunications-and-information-technology-bylaw>. Checked 2026-11-03. Undated current regulator text accessed on review date. Exact service classification and subordinate rules require separate checking.

### cybersecurity | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: United Arab Emirates: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope SA | legal: Saudi Arabia: NCA publishes Essential Cybersecurity Controls ECC 2 2024. Ask the buyer which entity and system scope applies before mapping the proposed controls.
Applies only: For an entity and system within the controls' scope. This note does not claim every private buyer is subject to every NCA control.
Source I:SA-ECC: Essential Cybersecurity Controls ECC 2 2024 <https://nca.gov.sa/en/regulatory-documents/controls-list/ecc/>. Checked 2026-11-03. Date is official page publication. No blanket all private business mandate or detailed control asserted; scope must be established.

sector_regulator | scope SA | legal: Saudi Arabia: NCA has a dedicated managed SOC licensing framework. Check it separately from general cybersecurity provider registration and any proposed wider licensing framework.
Applies only: Managed SOC services in the framework; no claim that a consultation draft is current law.
Source I:SA-MSOC-FRAMEWORK: Regulatory Framework for Licensing Managed Security Operations Center Services RFMSOC 1 2024 <https://cdn.nca.gov.sa/api/public/cms/files/8417b9fe-8066-47f5-8282-bb1d6ddbfbf5_rfmsoc-EN.pdf>. Checked 2026-11-03. Primary indexed provisions 6.23 and 7 read; alternate official PDF confirms identity but has incomplete text extraction. No unsupported data residency or tier customer scope claim. Arabic is authoritative. Not the March 2026 general services consultation draft.

sector_regulator | scope OM | legal: Oman: security assessment and managed security accreditation transferred from MTCIT to the Cyber Defence Centre. Check current CDC procedures.
Applies only: Services within the transferred accreditation programme.
Source I:OM-CYBER-TRANSFER: Accreditation Program and current authority transfer notices <https://www.mtcit.gov.om/media-4/projects-initiatives-12/program-89/accreditation-program-381>. Checked 2026-11-03. Live primary notice read. Page bears old launch date and current site footer; neither is a verified date of transfer. Linked circular is an image PDF with no extracted text. Current CDC procedures remain pending.

sector_regulator | scope QA | legal: Qatar: NCSA decides NISCF service accreditation. Confirm the relevant service module and required scope.
Applies only: NISCF accreditation only; not a universal provider licence.
Source I:QA-CYBER-ACCREDITATION: NISCF General Policy for National Accreditation V1.0 <https://ncsa.gov.qa/shared/document_library/94787172324409/33000/8826/1.0~c7786091-54da-4189-9dac-2b356f805517?filename=NCSA-NISCF-ACCR-GPNA-V1.0+%284%29.pdf&mimetype=application%2Fpdf>. Checked 2026-11-03. Primary PDF text read. Effective 1 January 2024 with re-accreditation transition. Scheme participation is not evidence of a universal trading licence requirement. Current service module and buyer procurement scope still need checks.

### software | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: United Arab Emirates: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

proof | scope SA | legal: Saudi Arabia: ECC 1-6-3 requires secure development, tested integration and prelaunch hardening.
Applies only: Government, government affiliated or private CNI entity within ECC scope only.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### saas | specific | inherits defaults
Apply only notes for the named jurisdiction and activity. Specific means sourced differences exist; it does not mean every listed country is covered.
Waiting for a source: United Arab Emirates: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Qatar: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Bahrain: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Oman: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.; Kuwait: no direct vertical source in this draft; use applicable country defaults only and state the gap, never another country rule.

sector_regulator | scope SA | legal: Saudi Arabia: CST's Cloud Computing Service Provisioning Regulations replace the older Cloud Computing Regulatory Framework. Check whether the offered service is within that regime.
Applies only: Only if the actual service is covered by the cloud regulations; do not infer registration solely from the SaaS label.
Source I:SA-CLOUD: Cloud Computing Service Provisioning Regulations and guides decision 506/1445 <https://www.cst.gov.sa/en/regulations-and-licenses/decisions/Regulation-1482>. Checked 2026-11-03. Used for current instrument naming only. Cloud service classification and registration require separate review.

### freight-visibility | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | operating: Saudi Arabia: tie customs workflow status to the importer or exporter and its authorised broker, preserving the delegation reference.
Applies only: Suggested visibility evidence derived from the customs delegation workflow.
Source I:SA-CUSTOMS-AUTH: Customs Broker Authorization <https://www.zatca.gov.sa/en/eServices/Pages/eServices-235.aspx>. Checked 2026-11-03. Live primary service page. Published date is service release date. Customs workflow does not mean a freight software supplier itself needs a customs broker licence.

### freight-marketplace | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### seller-shipping | specific | inherits logistics-tech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | operating: Saudi Arabia: preserve the seller shipping handoff to the importer and the broker authorisation scope and duration.
Applies only: Suggested customs evidence; shipping software is not itself a brokerage licence.
Source I:SA-CUSTOMS-AUTH: Customs Broker Authorization <https://www.zatca.gov.sa/en/eServices/Pages/eServices-235.aspx>. Checked 2026-11-03. Live primary service page. Published date is service release date. Customs workflow does not mean a freight software supplier itself needs a customs broker licence.

### last-mile | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### warehousing | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### transport-management | inherited | inherits logistics-tech
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### payments-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope AE | legal: UAE: a retail payment provider's board or designated board committee is responsible for technology risk governance. Confirm the separate contract approval delegation.
Applies only: Retail payment provider within Article 13, not every payment related software vendor.
Source I:AE-PAY-TECH: Retail Payment Services and Card Schemes Regulation Article 13 <https://rulebook.centralbank.ae/en/rulebook/article-13-technology-risk-and-information-security>. Checked 2026-11-03. Primary indexed text read. Scoped retail payment provider obligation. Does not name the buyer's contract signatory.

decision_approvers | scope SA | legal: Saudi Arabia: payment licensees require SAMA non-objection for outsourcing material functions. Senior position holders retain compliance responsibility; identify the internal delegated signatory.
Applies only: A payment licensee and material function under Article 27.
Source I:SA-PAY-IMPLEMENTING: Implementing Regulations of Payments and Payment Services Law Article 27 <https://rulebook.sama.gov.sa/en/implementing-regulations-payments-and-payment-services-law>. Checked 2026-11-03. Live primary rulebook read. Scope and exceptions of law apply. This note does not establish a data storage location.

sector_regulator | scope AE | legal: UAE: the CBUAE law lists payment, stored value and related licensed financial activities. Map the money flow and provider role before selecting the licensing route.
Applies only: For activities within Article 61 and applicable regulations, subject to financial free zone scope.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope SA | legal: Saudi Arabia: Article 7 of the Law of Payments and Payment Services assigns payment oversight and licensing powers to SAMA. Identify the operator or provider role.
Applies only: For payment systems and services in the law's scope.
Source I:SA-PAYMENTS: Law of Payments and Payment Services: Article 7 <https://www.rulebook.sama.gov.sa/en/article-7-24>. Checked 2026-11-03. Use with current implementing regulations; no assertion that every software supplier is a payment provider.

sector_regulator | scope KW | legal: Kuwait electronic payment providers are subject to CBK's Instructions for Regulating the Electronic Payment of Funds under Law No. 20 of 2014. Confirm the licence category and the required governance, security and continuity evidence for the proposed service.
Applies only: Electronic payment activity within CBK's instructions
Source I:KW-PAYMENTS: Instructions for Regulating the Electronic Payment of Funds <https://www.cbk.gov.kw/en/supervision/e-payment-services>. Checked 2026-11-03. Undated current official overview specifies May 2023 issuance. Detailed licence type and subsequent instructions require checking.

data_privacy | scope AE | legal: UAE: Article 14 requires in-scope retail payment personal and payment data to be stored in the UAE; collection must be necessary for the service and supported by explicit user consent.
Applies only: Retail Payment Services and Card Schemes Regulation scope only.
Source I:AE-PAY-DATA: Retail Payment Services and Card Schemes Regulation Article 14 <https://rulebook.centralbank.ae/en/rulebook/article-14-obligations-towards-retail-payment-service-users>. Checked 2026-11-03. Primary indexed text read. Applies to in-scope retail payment services, not a general UAE data localisation rule. No blanket assertion about separate token or stored value regimes.

proof | scope AE | operating: UAE: show the payment data storage map, consent flow, technology risk controls and independent technology audit coverage for the regulated service.
Applies only: Evidence derived from Articles 13 and 14; separate service authorisation remains necessary.
Source I:AE-PAY-DATA: Retail Payment Services and Card Schemes Regulation Article 14 <https://rulebook.centralbank.ae/en/rulebook/article-14-obligations-towards-retail-payment-service-users>. Checked 2026-11-03. Primary indexed text read. Applies to in-scope retail payment services, not a general UAE data localisation rule. No blanket assertion about separate token or stored value regimes.
Source I:AE-PAY-TECH: Retail Payment Services and Card Schemes Regulation Article 13 <https://rulebook.centralbank.ae/en/rulebook/article-13-technology-risk-and-information-security>. Checked 2026-11-03. Primary indexed text read. Scoped retail payment provider obligation. Does not name the buyer's contract signatory.

proof | scope SA | operating: Saudi Arabia: demonstrate the outsourced function's materiality, continued internal control, continuity and SAMA supervisory access without transferring the licensee's responsibilities.
Applies only: Evidence derived from Article 27 for payment licensee outsourcing.
Source I:SA-PAY-IMPLEMENTING: Implementing Regulations of Payments and Payment Services Law Article 27 <https://rulebook.sama.gov.sa/en/implementing-regulations-payments-and-payment-services-law>. Checked 2026-11-03. Live primary rulebook read. Scope and exceptions of law apply. This note does not establish a data storage location.

### core-banking | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope AE | legal: UAE: material bank outsourcing needs CBUAE non-objection supported by board or board committee approval and agreement from internal audit and compliance.
Applies only: A material business activity outsourced by a bank within the CBUAE standards.
Source I:AE-BANK-APPROVAL: Outsourcing Standards for Banks section 8 <https://rulebook.centralbank.ae/en/rulebook/8-non-objection-central-bank>. Checked 2026-11-03. Effective date and in-force status on primary rulebook. Material bank outsourcing only.

decision_approvers | scope SA | legal: Saudi Arabia: bank material outsourcing involves board, delegated authority or board committee approval and SAMA written non-objection.
Applies only: Material outsourcing by a bank within SAMA's rules.
Source I:SA-BANK-OUTSOURCE: Rules on Outsourcing <https://rulebook.sama.gov.sa/en/rules-outsourcing>. Checked 2026-11-03. Live primary rulebook read. Banks only. Foreign branches and overseas service providers have additional conditions. No universal software purchase approval asserted.

sector_regulator | scope AE | legal: UAE: identify the CBUAE licensed banking activity and the bank's permission before reviewing a core banking deployment. DIFC and ADGM need their own regulatory assessment.
Applies only: Bank activity within the relevant jurisdiction; no automatic software vendor licence.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.
Source I:AE-DFSA: About the DFSA <https://www.dfsa.ae/about-dfsa/who-we-are/the-dfsa>. Checked 2026-11-03. No reliable full publication date on the retrieved page. DIFC only. Dubai city does not establish DIFC jurisdiction.
Source I:AE-FSRA: Financial Services Regulatory Authority <https://www.adgm.com/financial-services-regulatory-authority>. Checked 2026-11-03. No reliable full publication date on the retrieved page. ADGM only. Abu Dhabi city does not establish ADGM jurisdiction.

sector_regulator | scope SA | legal: Saudi Arabia: Banking Control Law Article 3 routes a bank licence application through SAMA for its review and recommendation to the statutory licensing authority.
Applies only: Banking business in the law's scope; confirm the current application procedure with SAMA.
Source I:SA-BANK-LICENCE: Banking Control Law Article 3 <https://misa.gov.sa/app/uploads/2025/08/Banking-Control-Law.pdf>. Checked 2026-11-03. Official government hosted English translation. Historical institutional names retained in text; current supervisory authority is Saudi Central Bank. Not a licence application guide.

data_privacy | scope AE | legal: UAE: CBUAE bank outsourcing rules protect data ownership and access. Sharing customer confidential data abroad requires Central Bank approval, prior written customer consent and acknowledgement of possible foreign legal access.
Applies only: A bank outsourcing arrangement within the rule, including its overseas sharing conditions.
Source I:AE-BANK-OUTSOURCE: Outsourcing Regulation for Banks <https://rulebook.centralbank.ae/en/rulebook/outsourcing-regulation-banks>. Checked 2026-11-03. Primary indexed text read; live page returned 403. Bank scope only, not financial free zone rules or every software purchase.

data_privacy | scope SA | legal: Saudi Arabia: bank outsourcing must safeguard customer and financial confidentiality and provide controlled data retrieval or destruction on termination.
Applies only: Bank outsourcing; overseas arrangements have additional SAMA review conditions.
Source I:SA-BANK-OUTSOURCE: Rules on Outsourcing <https://rulebook.sama.gov.sa/en/rules-outsourcing>. Checked 2026-11-03. Live primary rulebook read. Banks only. Foreign branches and overseas service providers have additional conditions. No universal software purchase approval asserted.

proof | scope AE | operating: UAE: prepare the materiality and risk assessments, provider diligence, approval evidence and audit access terms for the bank's non-objection submission.
Applies only: Procurement evidence for CBUAE material bank outsourcing.
Source I:AE-BANK-APPROVAL: Outsourcing Standards for Banks section 8 <https://rulebook.centralbank.ae/en/rulebook/8-non-objection-central-bank>. Checked 2026-11-03. Effective date and in-force status on primary rulebook. Material bank outsourcing only.
Source I:AE-BANK-OUTSOURCE: Outsourcing Regulation for Banks <https://rulebook.centralbank.ae/en/rulebook/outsourcing-regulation-banks>. Checked 2026-11-03. Primary indexed text read; live page returned 403. Bank scope only, not financial free zone rules or every software purchase.

proof | scope SA | operating: Saudi Arabia: give the bank a business case, provider diligence, continuity and exit evidence, and audit access terms for its outsourcing assessment.
Applies only: Evidence derived from SAMA bank outsourcing rules.
Source I:SA-BANK-OUTSOURCE: Rules on Outsourcing <https://rulebook.sama.gov.sa/en/rules-outsourcing>. Checked 2026-11-03. Live primary rulebook read. Banks only. Foreign branches and overseas service providers have additional conditions. No universal software purchase approval asserted.

### lending | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SA | legal: Saudi Arabia: SAMA's finance company compliance and internal audit principles address board and executive responsibilities. Ask the finance company to name its accountable reviewers.
Applies only: For finance and real estate refinance companies within the named principles.
Source I:SA-FINANCE: Compliance and internal audit principles for finance companies <https://sama.gov.sa/en-us/mediacenter/news/pages/news-1044.aspx>. Checked 2026-11-03. Primary indexed official notice read; live open timed out. Only the named finance and refinance company categories.

decision_approvers | scope SA | legal: Saudi Arabia: a finance company needs a board approved outsourcing policy and SAMA non-objection for material outsourcing. Confirm the internal approval delegation in that policy.
Applies only: A licensed finance company under the Finance Companies Control Law.
Source I:SA-FIN-OUTSOURCE: Rules on Outsourcing for Finance Companies <https://rulebook.sama.gov.sa/en/rules-outsourcing-finance-companies>. Checked 2026-11-03. Live primary rulebook read. Finance companies in scope only; no assumption that all lending software or bank lending uses this regime.

sector_regulator | scope AE | legal: UAE: credit and funding facilities are licensed activities under the CBUAE law. Confirm the lender's entity and jurisdiction before choosing the approval path.
Applies only: For activities within the federal law; do not apply this as a licence requirement for all lending software.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

data_privacy | scope SA | legal: Saudi Arabia: finance company outsourcing must safeguard consumer confidentiality and arrange return or destruction at exit, subject to regulatory retention duties.
Applies only: Finance company consumer data handled by an external provider.
Source I:SA-FIN-OUTSOURCE: Rules on Outsourcing for Finance Companies <https://rulebook.sama.gov.sa/en/rules-outsourcing-finance-companies>. Checked 2026-11-03. Live primary rulebook read. Finance companies in scope only; no assumption that all lending software or bank lending uses this regime.

proof | scope SA | operating: Saudi Arabia: prepare provider licence and capability checks, materiality assessment, data safeguards, audit access and continuity terms for the finance company's review.
Applies only: Evidence derived from SAMA's finance company outsourcing rules.
Source I:SA-FIN-OUTSOURCE: Rules on Outsourcing for Finance Companies <https://rulebook.sama.gov.sa/en/rules-outsourcing-finance-companies>. Checked 2026-11-03. Live primary rulebook read. Finance companies in scope only; no assumption that all lending software or bank lending uses this regime.

### wealth-investment | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope AE | legal: UAE: Federal Decree Law 32 of 2025 establishes the Capital Market Authority framework. Confirm whether the activity is under this regime or a financial free zone regulator.
Applies only: For UAE capital market activities in the federal authority's remit; separate DIFC and ADGM scope must be checked.
Source I:AE-CMA: Federal Decree Law 32 of 2025 regarding Capital Market Authority <https://legislation.uaecma.gov.ae/en/capital-market-authority-law>. Checked 2026-11-03. Date is official gazette date. Primary indexed entry read; live open timed out. Do not conflate this authority with the Saudi authority of the same English name.

sector_regulator | scope SA | legal: Saudi Arabia: the Capital Market Authority regulates securities activities under the Capital Market Law. Identify the investment service and entity before selecting obligations.
Applies only: For Saudi capital market activity. This is the Saudi authority.
Source I:SA-CMA: Frequently asked questions for implementing regulations <https://cma.gov.sa/en/RulesRegulations/FAQ/Pages/FAQs.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not confuse with the UAE Capital Market Authority.

sector_regulator | scope OM | legal: In Oman, the Financial Services Authority established under Royal Decree 20/2024 regulates capital markets. Confirm the entity's authorised activity and applicable sector rules.
Applies only: Capital market activity within the Oman FSA remit
Source I:OM-FSA: Establishment of the Financial Services Authority under Royal Decree 20/2024 <https://fsa.gov.om/Home/News/9631>. Checked 2026-11-03. Regulator press release on remit. Detailed licensing rules and subsequent changes must be checked for the activity.

sector_regulator | scope KW | legal: For Kuwait securities activity, check the Capital Markets Authority framework under Law No. 7 of 2010 and its current amendments. Confirm the specific advisory, dealing or management activity before choosing the review requirements.
Applies only: Securities activity within Kuwait CMA's remit
Source I:KW-CMA: Law 7 of 2010 establishing the Capital Markets Authority and regulating securities activities <https://www.cma.gov.kw/en/web/cma/cma-handbook>. Checked 2026-11-03. Current consolidated page includes amendments with future commencement. No future amendment is presented as already effective and no detailed obligation is inferred.

### spend-expense | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope AE | operating: UAE: the FTA electronic invoicing timetable depends on the entity and transaction. Expense software should preserve evidence of the applicable phase.
Applies only: Phased electronic invoicing scope, separate from any payment service authorisation.
Source I:AE-INVOICE: FTA calls on persons subject to electronic invoicing to comply with deadlines <https://tax.gov.ae/en/media.centre/News/federal.tax.authority.calls.on.persons.subject.to.einvoicing.to.comply.wit.the.prescribed.legal.deadlines.and.avoid.administrative.penalties.aspx>. Checked 2026-11-03. Latest accessed notice differs from the older provider designation deadline. No thresholds or universal immediate obligation asserted.

proof | scope SA | operating: Saudi Arabia: preserve the supplier invoice and taxpayer phase evidence in the expense workflow; ZATCA generation and integration requirements are different.
Applies only: Invoices and taxpayers within the electronic invoicing rules; no automatic deduction entitlement.
Source I:SA-INVOICE: Electronic invoice rollout phases <https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. No universal integration deadline, tax rate or revenue threshold asserted.

### insurance | specific | inherits fintech
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope AE | legal: UAE: material insurer outsourcing needs board or board risk/audit committee approval under a board approved policy.
Applies only: Insurance companies within CBUAE risk management and internal control standards.
Source I:AE-INS-OUTSOURCE: Risk Management and Internal Controls Standards for Insurance Companies section 12 <https://rulebook.centralbank.ae/en/rulebook/12-outsourcing>. Checked 2026-11-03. In-force primary indexed text read, live page 403. CBUAE regulated insurance companies, not a rule for every intermediary or financial free zone firm.

decision_approvers | scope SA | operating: Saudi Arabia: the Insurance Authority has a no-objection route for outsourcing licensed companies' key functions. Confirm the insurer's internal signatory separately.
Applies only: Proposed outsourcing of a key function; the service page does not name an internal purchase approver.
Source I:SA-INS-OUTSOURCE: Outsourcing of Critical Functions <https://www.ia.gov.sa/en/eservices-ia/service-details/Assignment-of-essential-tasks>. Checked 2026-11-03. Live primary authority page read. No assertion that a generic vendor contract is a regulated outsourced key function.

sector_regulator | scope AE | legal: UAE: the CBUAE law includes insurance and reinsurance activities. Establish whether the insurer is under the federal regime or a financial free zone regime.
Applies only: For the insurance activity and entity in scope; separate DIFC and ADGM conditions remain conditional.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope SA | legal: Saudi Arabia: the Insurance Authority is the insurance regulator and sets insurance licensing requirements. Use the insurer or intermediary's current regulatory category.
Applies only: For insurance activity in Saudi Arabia within the Authority's remit.
Source I:SA-INSURANCE: About the Insurance Authority <https://www.ia.gov.sa/en/about-ia/about>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not use the older SAMA insurance supervision attribution. Current product regulations still need scope checks.

sector_regulator | scope OM | legal: In Oman, the Financial Services Authority established under Royal Decree 20/2024 regulates the insurance sector. Confirm the entity's authorised activity and applicable sector rules.
Applies only: Insurance activity within the Oman FSA remit
Source I:OM-FSA: Establishment of the Financial Services Authority under Royal Decree 20/2024 <https://fsa.gov.om/Home/News/9631>. Checked 2026-11-03. Regulator press release on remit. Detailed licensing rules and subsequent changes must be checked for the activity.

sector_regulator | scope KW | legal: Kuwait's Insurance Regulatory Unit supervises insurance under Law No. 125 of 2019 and its executive bylaws. Confirm the insurer, intermediary or service role before defining approval evidence.
Applies only: Insurance activity within Kuwait Insurance Regulatory Unit's remit
Source I:KW-INSURANCE: Executive bylaws of Law 125 of 2019 regulating insurance <https://www.iru.gov.kw/ByLaws>. Checked 2026-11-03. Current Arabic regulator text read. No translation treated as authoritative and no specific licence condition asserted.

sector_regulator | scope SA | legal: Saudi Arabia: the Insurance Authority provides distinct licence applications for insurers, foreign branches, intermediaries, aggregators and service providers. Choose the form for the actual activity.
Applies only: Insurance activity within the Insurance Authority regime.
Source I:SA-INS-LICENCE: Apply for a License <https://www.ia.gov.sa/en/apply-for-licenses>. Checked 2026-11-03. Live primary authority page read. No assertion that a generic vendor contract is a regulated outsourced key function.

data_privacy | scope AE | legal: UAE: the insurer's outsourcing contract must preserve data ownership, access and confidentiality, including subcontractors and data return or destruction at exit.
Applies only: An outsourcing arrangement in the CBUAE insurance company standards.
Source I:AE-INS-OUTSOURCE: Risk Management and Internal Controls Standards for Insurance Companies section 12 <https://rulebook.centralbank.ae/en/rulebook/12-outsourcing>. Checked 2026-11-03. In-force primary indexed text read, live page 403. CBUAE regulated insurance companies, not a rule for every intermediary or financial free zone firm.

proof | scope AE | operating: UAE: demonstrate policyholder access controls, subcontractor safeguards and end of contract data handling, and provide the outsourcing register and approval evidence.
Applies only: Evidence derived from CBUAE insurance outsourcing standards; does not demonstrate underwriting performance.
Source I:AE-INS-OUTSOURCE: Risk Management and Internal Controls Standards for Insurance Companies section 12 <https://rulebook.centralbank.ae/en/rulebook/12-outsourcing>. Checked 2026-11-03. In-force primary indexed text read, live page 403. CBUAE regulated insurance companies, not a rule for every intermediary or financial free zone firm.

proof | scope SA | operating: Saudi Arabia: establish the insurer's licence category and whether the proposed function needs the Insurance Authority outsourcing no-objection before finalising the evidence request.
Applies only: Scoping step only; detailed data and outsourcing evidence remains pending.
Source I:SA-INS-LICENCE: Apply for a License <https://www.ia.gov.sa/en/apply-for-licenses>. Checked 2026-11-03. Live primary authority page read. No assertion that a generic vendor contract is a regulated outsourced key function.
Source I:SA-INS-OUTSOURCE: Outsourcing of Critical Functions <https://www.ia.gov.sa/en/eservices-ia/service-details/Assignment-of-essential-tasks>. Checked 2026-11-03. Live primary authority page read. No assertion that a generic vendor contract is a regulated outsourced key function.

### customer-service | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### crm-marketing | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### collaboration | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-growth | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### construction | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### property-management | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### field-services | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### fmcg-retail-execution | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### industry-hr-payroll | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### hotel-lodging | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### retail-restaurant-ops | inherited | inherits vertical-saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### agents-copilots | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### voice-language-models | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### enterprise-search | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### it-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### bpo-cx | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-engineering | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-services | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### operators-connectivity | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope AE | operating: UAE: demonstrate the TDRA licensed entity and public telecom service scope; a supplier contract does not itself grant the right to operate.
Applies only: Public telecom networks and services within the law.
Source I:AE-TELECOM: Issue licences to provide telecommunication services <https://tdra.gov.ae/en/Services/issue-licences-to-provide-telecommunication-services>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not a requirement for every software vendor supplying an operator.

### cpaas-messaging | specific | inherits telecom
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope SA | legal: Saudi Arabia: CST decision 484/1443 establishes a separate SMS service framework covering promotional, informational and response messages. Classify the service before checking its conditions.
Applies only: SMS service scope; detailed current conditions require review.
Source I:SA-SMS-RULES: Regulations of the Provision of the Short Messaging Service SMS <https://www.cst.gov.sa/en/regulations-and-licenses/regulations/Document-504>. Checked 2026-11-03. Current primary regulation page read. Detailed attached conditions not extracted; only activity framework and scope asserted. No inferred sending hours consent exemption or sender identifier format.

### telecom-software | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### business-voice-ucaas | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### developer-platform | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### data-infrastructure | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### observability | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### testing | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### dev-tools | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### cloud-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

sector_regulator | scope OM | legal: Oman: cloud hosting regulation transferred to TRA. Distinguish hosting from supplying a security tool.
Applies only: Cloud hosting service; no blanket licensing claim for security software.
Source I:OM-CYBER-TRANSFER: Accreditation Program and current authority transfer notices <https://www.mtcit.gov.om/media-4/projects-initiatives-12/program-89/accreditation-program-381>. Checked 2026-11-03. Live primary notice read. Page bears old launch date and current site footer; neither is a verified date of transfer. Linked circular is an image PDF with no extracted text. Current CDC procedures remain pending.

proof | scope SA | operating: Saudi Arabia: identify whether the cloud service is within CST provisioning regulations before mapping its security evidence.
Applies only: Cloud provider activity; exact registration and customer scope require review.
Source I:SA-CLOUD: Cloud Computing Service Provisioning Regulations and guides decision 506/1445 <https://www.cst.gov.sa/en/regulations-and-licenses/decisions/Regulation-1482>. Checked 2026-11-03. Used for current instrument naming only. Cloud service classification and registration require separate review.

### identity-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires controlled privileges and periodic access review.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-2.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### email-security | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires phishing protection and email domain validation.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-4.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### awareness-training | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires an approved, periodically reviewed awareness programme.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 1-10.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires external web application security controls.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-15.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### mobile-appsec | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC testing scope includes externally provided smartphone applications.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-11.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### soc-services | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope SA | legal: Saudi Arabia: MSOC subcontracting requires a written NCA request and approval before work starts; the main provider retains its obligations.
Applies only: Subcontracted managed SOC services under section 7; not a blanket rule for all vendor purchases.
Source I:SA-MSOC-FRAMEWORK: Regulatory Framework for Licensing Managed Security Operations Center Services RFMSOC 1 2024 <https://cdn.nca.gov.sa/api/public/cms/files/8417b9fe-8066-47f5-8282-bb1d6ddbfbf5_rfmsoc-EN.pdf>. Checked 2026-11-03. Primary indexed provisions 6.23 and 7 read; alternate official PDF confirms identity but has incomplete text extraction. No unsupported data residency or tier customer scope claim. Arabic is authoritative. Not the March 2026 general services consultation draft.

sector_regulator | scope SA | legal: Saudi Arabia: use NCA RFMSOC 1 2024 to establish the managed SOC service licence. A general provider registration is not evidence of that licence.
Applies only: Managed SOC services within this framework; exact tier and customer category must be checked.
Source I:SA-MSOC-FRAMEWORK: Regulatory Framework for Licensing Managed Security Operations Center Services RFMSOC 1 2024 <https://cdn.nca.gov.sa/api/public/cms/files/8417b9fe-8066-47f5-8282-bb1d6ddbfbf5_rfmsoc-EN.pdf>. Checked 2026-11-03. Primary indexed provisions 6.23 and 7 read; alternate official PDF confirms identity but has incomplete text extraction. No unsupported data residency or tier customer scope claim. Arabic is authoritative. Not the March 2026 general services consultation draft.

sector_regulator | scope OM | legal: Oman: CDC now handles security service accreditation; an old MTCIT listing does not establish the current route.
Applies only: Security assessment or managed security service within the programme; current scope remains pending.
Source I:OM-CYBER-TRANSFER: Accreditation Program and current authority transfer notices <https://www.mtcit.gov.om/media-4/projects-initiatives-12/program-89/accreditation-program-381>. Checked 2026-11-03. Live primary notice read. Page bears old launch date and current site footer; neither is a verified date of transfer. Linked circular is an image PDF with no extracted text. Current CDC procedures remain pending.

data_privacy | scope SA | legal: Saudi Arabia: the MSOC framework requires compliance with applicable NCA controls, including Data Cybersecurity Controls. Establish the applicable data and system scope.
Applies only: Section 6.23; no unverified hosting location requirement asserted.
Source I:SA-MSOC-FRAMEWORK: Regulatory Framework for Licensing Managed Security Operations Center Services RFMSOC 1 2024 <https://cdn.nca.gov.sa/api/public/cms/files/8417b9fe-8066-47f5-8282-bb1d6ddbfbf5_rfmsoc-EN.pdf>. Checked 2026-11-03. Primary indexed provisions 6.23 and 7 read; alternate official PDF confirms identity but has incomplete text extraction. No unsupported data residency or tier customer scope claim. Arabic is authoritative. Not the March 2026 general services consultation draft.

proof | scope SA | operating: Saudi Arabia: present the applicable control compliance evidence and any NCA subcontracting approval with the service licence.
Applies only: Assurance evidence derived from RFMSOC; tier, staffing and customer approval details remain pending.
Source I:SA-MSOC-FRAMEWORK: Regulatory Framework for Licensing Managed Security Operations Center Services RFMSOC 1 2024 <https://cdn.nca.gov.sa/api/public/cms/files/8417b9fe-8066-47f5-8282-bb1d6ddbfbf5_rfmsoc-EN.pdf>. Checked 2026-11-03. Primary indexed provisions 6.23 and 7 read; alternate official PDF confirms identity but has incomplete text extraction. No unsupported data residency or tier customer scope claim. Arabic is authoritative. Not the March 2026 general services consultation draft.

### endpoint-network | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires malware protection and patch management.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-3.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### document-ai | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### ai-video | inherited | inherits ai-native
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### engineering-talent | inherited | inherits ites
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### product-management | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### digital-adoption | inherited | inherits saas
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### pentest | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

decision_approvers | scope QA | operating: Qatar: NCSA makes accreditation decisions; the applicant documents governance and delivery responsibilities. Buyer purchase authority remains separate.
Applies only: NISCF application for the relevant service module.
Source I:QA-CYBER-ACCREDITATION: NISCF General Policy for National Accreditation V1.0 <https://ncsa.gov.qa/shared/document_library/94787172324409/33000/8826/1.0~c7786091-54da-4189-9dac-2b356f805517?filename=NCSA-NISCF-ACCR-GPNA-V1.0+%284%29.pdf&mimetype=application%2Fpdf>. Checked 2026-11-03. Primary PDF text read. Effective 1 January 2024 with re-accreditation transition. Scheme participation is not evidence of a universal trading licence requirement. Current service module and buyer procurement scope still need checks.

sector_regulator | scope OM | legal: Oman: CDC now handles security service accreditation; an old MTCIT listing does not establish the current route.
Applies only: Security assessment or managed security service within the programme; current scope remains pending.
Source I:OM-CYBER-TRANSFER: Accreditation Program and current authority transfer notices <https://www.mtcit.gov.om/media-4/projects-initiatives-12/program-89/accreditation-program-381>. Checked 2026-11-03. Live primary notice read. Page bears old launch date and current site footer; neither is a verified date of transfer. Linked circular is an image PDF with no extracted text. Current CDC procedures remain pending.

proof | scope QA | operating: Qatar: demonstrate legal operating status, staff capability, risk management, subcontractor oversight and delivery methods for the requested accreditation scope.
Applies only: NISCF policy application evidence; penetration testing module details remain pending.
Source I:QA-CYBER-ACCREDITATION: NISCF General Policy for National Accreditation V1.0 <https://ncsa.gov.qa/shared/document_library/94787172324409/33000/8826/1.0~c7786091-54da-4189-9dac-2b356f805517?filename=NCSA-NISCF-ACCR-GPNA-V1.0+%284%29.pdf&mimetype=application%2Fpdf>. Checked 2026-11-03. Primary PDF text read. Effective 1 January 2024 with re-accreditation transition. Scheme participation is not evidence of a universal trading licence requirement. Current service module and buyer procurement scope still need checks.

proof | scope SA | legal: Saudi Arabia: ECC requires periodic testing of externally provided services.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-11.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### attack-surface-dast | specific | inherits cybersecurity
Apply sourced subtype additions only to the named country and activity; retain applicable parent notes. Other countries are not implied covered.
Waiting for a source: Specific means scoped additions exist, not a complete licensing or country review. Check the source limitations and the buyer actual approval delegation.

proof | scope SA | legal: Saudi Arabia: ECC requires vulnerability classification and risk based remediation.
Applies only: Government, government affiliated or private CNI entity within ECC scope; control 2-10.
Source I:SA-ECC-CONTROLS: Essential Cybersecurity Controls ECC 2 2024 full English text <https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf>. Checked 2026-11-03. Final PDF linked by current NCA ECC page, not the consultation copy. Read applicability and relevant controls before use. No full day of issue in document. Government and critical infrastructure scope is not all private business.

### process-orchestration | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### open-source-support | inherited | inherits software
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

### iot-connectivity | inherited | inherits telecom
Use the jurisdiction filtered vertical context. No separate subtype override is established in this bounded draft; remaining subtype depth is outside the final owner scope, not proof that no local difference exists.

## UK

United Kingdom only. Check the relevant UK nation for devolved procurement and transport rules. Country selection does not establish that a buyer or product is regulated. Draft for owner review. Final owner scope permits remaining subtypes to inherit. Specific means a sourced addition for the named country and activity, not complete country coverage. Pending topics retain narrower research gaps.
Countries: GB = United Kingdom
Clues, only in selling context: {"aliases":["UK","United Kingdom"],"countries":[{"code":"GB","name":"United Kingdom","aliases":["UK","United Kingdom","Britain","Great Britain","England","Scotland","Wales","Northern Ireland"],"cities":["London","Manchester","Birmingham","Edinburgh","Cardiff","Belfast"],"currencies":["GBP","pound sterling"],"regulators":["Financial Conduct Authority","Prudential Regulation Authority","Ofcom","Information Commissioner's Office"]}]}

### Defaults

decision_approvers | scope GB | question: Who owns the budget, accepts the operational risk and approves the handling of personal data for this UK purchase?

procurement_payment | scope GB | question: Is this a public tender, a framework purchase or a private contract, and what are the agreed invoice currency, acceptance steps and payment terms?

data_privacy | scope GB | legal: For UK GDPR processing on a controller's behalf, prepare the Article 28 contract, subprocessor approvals and data return or deletion terms before exchanging personal data.
Applies only: Where UK GDPR applies and the supplier is a processor; first establish the parties' actual roles.
Source J:UK-ICO-CONTRACT: Contracts <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/contracts/>. Checked 2026-11-03. Publication date not reliably shown. Primary source text retrieved in search; direct fetch returned 403. Applies only to controller and processor processing within UK GDPR scope.

buyer_language | scope GB | question: Which language and terminology does the buying team require for the proposal, training and support?

proof | scope GB | question: What buyer approved evidence and acceptance test will show that this purchase solves the stated problem?

objections | scope GB | question: Which unresolved issue could stop approval: security, implementation effort, accountability, contract terms or proof of value?

sales_motion | scope GB | question: Who must agree the pilot scope, success criteria and route to a paid contract before work starts?

### logistics-tech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

proof | scope GB | legal: For a covered road transport operation, demonstrate how scheduling and record exports help the operator meet the drivers' hours and tachograph duties described by DVSA.
Applies only: Confirm vehicle, route and exemptions first. The cited guidance must not be assumed to establish Northern Ireland requirements.
Source J:UK-DVSA-HOURS: Drivers' hours and tachographs: responsibilities of vehicle operators <https://www.gov.uk/guidance/drivers-hours-goods-vehicles/5-responsibilities-of-vehicle-operators>. Checked 2026-11-03. Updated 2026-07-01. Confirm vehicle, route, exemptions and Great Britain versus Northern Ireland scope before use.

### fintech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope GB | legal: FCA SYSC outsourcing requirements vary by firm and function. Classify the arrangement with the regulated buyer; a standard software purchase is not automatically outsourcing.
Applies only: For UK firms within the relevant FCA rules; test the service against the applicable outsourcing definition.
Source J:UK-FCA-OUTSOURCE: Outsourcing and operational resilience <https://www.fca.org.uk/firms/outsourcing-and-operational-resilience>. Checked 2026-11-03. Updated 2026-07-14. Future reporting rules from 2027 are not treated as current. Buying standard software is not automatically outsourcing.

proof | scope GB | legal: Where the service is outsourced, show the buyer its dependencies, security controls and exit approach. The regulated firm retains responsibility for managing third party risk.
Applies only: For arrangements within the buyer's applicable FCA outsourcing and risk management obligations.
Source J:UK-FCA-OUTSOURCE: Outsourcing and operational resilience <https://www.fca.org.uk/firms/outsourcing-and-operational-resilience>. Checked 2026-11-03. Updated 2026-07-14. Future reporting rules from 2027 are not treated as current. Buying standard software is not automatically outsourcing.

### vertical-saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

proof | scope GB | legal: Screen the industry workflow for high risk under UK GDPR Article 35. Where required, complete the buyer's DPIA and identify mitigations before processing.
Applies only: For likely high risk processing; a sector software label alone does not trigger a DPIA.
Source J:UK-DPIA: When do we need to do a DPIA <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/>. Checked 2026-11-03. No blanket SaaS DPIA requirement.

### ai-native | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope GB | legal: Use the ICO AI guidance to examine risks to individuals when UK personal data enters an AI workflow. Distinguish legal duties from recommended practice; the guidance is under review and is not a statutory code.
Applies only: For AI processing within UK data protection scope; verify current guidance before relying on a particular automated decision rule.
Source J:UK-ICO-AI: About this guidance: AI and data protection <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/>. Checked 2026-11-03. No reliable publication date shown. Guidance is under review following the Data (Use and Access) Act; it is not a statutory code.

### ites | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope GB | legal: Outsourced processing staff must be subject to confidentiality duties, with equivalent Article 28 obligations for subprocessors. Document service team access to customer records.
Applies only: For a UK GDPR processor; assess international transfers separately.
Source J:UK-PROCESSOR-TERMS: What needs to be included in the contract <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/>. Checked 2026-11-03. Controller processor relationships only.

### telecom | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope GB | legal: Ofcom's General Conditions of Entitlement operate under the Communications Act 2003. Identify the network or service being supplied and the providers covered by each relevant condition.
Applies only: For provision of UK electronic communications networks or services; supplying software to an operator does not by itself establish provider status.
Source J:UK-OFCOM-GC: General Conditions of Entitlement <https://www.ofcom.org.uk/phones-and-broadband/accessibility/general-conditions-of-entitlement>. Checked 2026-11-03. Updated 2026-04-08. Each condition has its own regulated provider definition; not all software sellers are communications providers.

### cybersecurity | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

procurement_payment | scope GB | legal: For a qualifying public contract, map the tender's security evidence to PPN 014. It allows Cyber Essentials, Cyber Essentials Plus or equivalent controls; it does not impose certification on every UK purchase.
Applies only: Only for the bodies and contract risks identified in PPN 014. Confirm the actual tender and procurement commencement date.
Source J:UK-CABINET-CYBER: PPN 014: Cyber essentials scheme <https://www.gov.uk/government/publications/ppn-014-cyber-essentials-scheme/ppn-014-cyber-essentials-scheme-html>. Checked 2026-11-03. Applies to stated central government and NHS bodies and qualifying contracts, not all UK procurement. No blanket certification requirement.

### software | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

proof | scope GB | operating: The voluntary Software Security Code calls for a senior responsible owner and evidence of secure development, build protection, vulnerability handling and customer communication.
Applies only: Recommended software assurance, not universal legal certification.
Source J:UK-SOFTWARE-CODE: Software Security Code of Practice <https://www.gov.uk/government/publications/software-security-code-of-practice/software-security-code-of-practice>. Checked 2026-11-03. Voluntary guidance, updated January 2026.

### saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

proof | scope GB | legal: For hosted SaaS acting as a UK GDPR processor, provide subprocessor authorisation, assistance commitments and an effective end of contract data return or deletion process.
Applies only: For the actual processor service; lawful retention and the controller's choice govern exit.
Source J:UK-PROCESSOR-TERMS: What needs to be included in the contract <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/>. Checked 2026-11-03. Controller processor relationships only.

### freight-visibility | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### freight-marketplace | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### seller-shipping | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### last-mile | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### warehousing | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### transport-management | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### payments-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | legal: For safeguarding, CASS 15.2.4 assigns oversight to a director or sufficiently senior manager reporting to the governing body.
Applies only: Only for a safeguarding institution subject to CASS 15; identify the actual appointed person.
Source J:UK-CASS15: CASS 15 Payment services and electronic money: relevant funds <https://handbook.fca.org.uk/handbook/cass15>. Checked 2026-11-03. Rules effective 2026-05-07. Official search text read; direct HTML requires JavaScript. Check safeguarding institution scope and insolvency exceptions.

sector_regulator | scope GB | legal: Separate payment services from electronic money issuance. The FCA explains authorisation and registration under the Payment Services Regulations 2017 and Electronic Money Regulations 2011, with exclusions and existing provider exceptions.
Applies only: Where the firm's own activities fall within UK payment or electronic money regulation; an API supplier is not automatically a regulated provider.
Source J:UK-FCA-PAYMENTS: Payment Services Regulations 2017 and Electronic Money Regulations 2011 <https://www.fca.org.uk/firms/payment-services-regulations-e-money-regulations>. Checked 2026-11-03. Updated 2025-12-17. Technical suppliers are not automatically payment institutions.

data_privacy | scope GB | legal: The FCA payment institution application requires procedures for sensitive payment data and incident reporting. Demonstrate these controls for the proposed payment workflow.
Applies only: For the relevant payment institution application and service, alongside UK GDPR where personal data is processed.
Source J:UK-PI-APPLY: Payment institution applicants <https://www.fca.org.uk/firms/apply-emoney-payment-institution/pi>. Checked 2026-11-03. Primary text read in current official search result. Application requirements vary by authorised or small institution and services.

proof | scope GB | legal: Demonstrate the safeguarding reconciliation, recorded reconciliation point and exception resolution under CASS 15.8.
Applies only: For covered safeguarding institutions; apply the relevant reconciliation day and insolvency provisions.
Source J:UK-CASS15: CASS 15 Payment services and electronic money: relevant funds <https://handbook.fca.org.uk/handbook/cass15>. Checked 2026-11-03. Rules effective 2026-05-07. Official search text read; direct HTML requires JavaScript. Check safeguarding institution scope and insolvency exceptions.

### core-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | legal: Under PRA SS2/21, identify the senior manager assigned outsourcing responsibility and the owner authorised to sign off continuity and exit plans.
Applies only: For a bank and arrangement within the statement's scope; the vendor does not acquire the bank's accountability.
Source J:UK-PRA-SS221: SS2/21 Outsourcing and third party risk management November 2024 <https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2024/ss221-november-2024-update.pdf>. Checked 2026-11-03. Current version confirmed on PRA landing page; effective 2024-12-31. March 2026 future version takes effect in March 2027 and is not used.

sector_regulator | scope GB | legal: A new UK bank applies to the Prudential Regulation Authority. Establish whether the prospect is the regulated institution or its technology supplier before assigning banking approval work.
Applies only: Where the activity involves establishing a bank; this is not a licence requirement for ordinary core banking software supply.
Source J:UK-PRA-AUTH: New firm authorisation <https://www.bankofengland.co.uk/prudential-regulation/Authorisations/new-firm-authorisation>. Checked 2026-11-03. Publication date not shown. Not a claim that software providers need a banking or insurance authorisation.

data_privacy | scope GB | legal: For material core banking outsourcing, SS2/21 expects data classification and agreed availability, confidentiality and integrity controls.
Applies only: Where the agreement transfers data; assess processing locations and access risks.
Source J:UK-PRA-SS221: SS2/21 Outsourcing and third party risk management November 2024 <https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2024/ss221-november-2024-update.pdf>. Checked 2026-11-03. Current version confirmed on PRA landing page; effective 2024-12-31. March 2026 future version takes effect in March 2027 and is not used.

proof | scope GB | legal: Show a tested core banking continuity plan and a documented stressed exit, including recoverable data and measurable success criteria.
Applies only: For material outsourcing under SS2/21 Chapter 10, with proportionate testing.
Source J:UK-PRA-SS221: SS2/21 Outsourcing and third party risk management November 2024 <https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2024/ss221-november-2024-update.pdf>. Checked 2026-11-03. Current version confirmed on PRA landing page; effective 2024-12-31. March 2026 future version takes effect in March 2027 and is not used.

### lending | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | legal: CONC 5.2A.33 requires written creditworthiness policies to be approved by the governing body or senior personnel, except for a sole trader.
Applies only: For the covered lender's creditworthiness policies, not every individual loan or technology purchase.
Source J:UK-CONC52A: CONC 5 Responsible lending <https://handbook.fca.org.uk/handbook/conc5>. Checked 2026-11-03. Current official text read through search. Direct HTML requires JavaScript. Consumer credit scope and exceptions apply.

sector_regulator | scope GB | legal: Consumer lending permissions and CONC 5.2A govern the covered creditworthiness assessment. Separate credit risk from affordability risk.
Applies only: For regulated consumer credit lending within CONC 5.2A, after checking exclusions.
Source J:UK-FCA-CREDIT: Apply to become a consumer credit lender or hirer <https://www.fca.org.uk/firms/authorisation/consumer-credit-lenders-hirers>. Checked 2026-11-03. Updated 2024-09-17. Consumer activity scope; do not apply automatically to commercial lending.
Source J:UK-CONC52A: CONC 5 Responsible lending <https://handbook.fca.org.uk/handbook/conc5>. Checked 2026-11-03. Current official text read through search. Direct HTML requires JavaScript. Consumer credit scope and exceptions apply.

data_privacy | scope GB | legal: Demonstrate what customer and credit reference information supports the assessment and why it is sufficient and proportionate under CONC 5.2A.
Applies only: For covered lending decisions; lawful processing and processor contracts still require a separate UK GDPR check.
Source J:UK-CONC52A: CONC 5 Responsible lending <https://handbook.fca.org.uk/handbook/conc5>. Checked 2026-11-03. Current official text read through search. Direct HTML requires JavaScript. Consumer credit scope and exceptions apply.

proof | scope GB | legal: For regulated consumer lending, the FCA expects evidence showing how credit risk, affordability and customers in financial difficulty are handled. Demonstrate the relevant decision and escalation workflow.
Applies only: For consumer credit activities within the FCA's authorisation scope; do not extend automatically to all commercial credit or software vendors.
Source J:UK-FCA-CREDIT: Apply to become a consumer credit lender or hirer <https://www.fca.org.uk/firms/authorisation/consumer-credit-lenders-hirers>. Checked 2026-11-03. Updated 2024-09-17. Consumer activity scope; do not apply automatically to commercial lending.

proof | scope GB | legal: Show how the assessment records both repayment risk and customer affordability, and how policy changes reach the approving body.
Applies only: For the applicable CONC assessment; do not infer the same workflow for exempt lending.
Source J:UK-CONC52A: CONC 5 Responsible lending <https://handbook.fca.org.uk/handbook/conc5>. Checked 2026-11-03. Current official text read through search. Direct HTML requires JavaScript. Consumer credit scope and exceptions apply.

### wealth-investment | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | legal: The investment firm remains responsible for suitability when its recommendation or portfolio decision uses an automated system. Identify its accountable service approver.
Applies only: For advice or portfolio management subject to COBS 9A, not every execution only service.
Source J:UK-COBS9A: COBS 9A Suitability <https://handbook.fca.org.uk/handbook/cobs9a>. Checked 2026-11-03. Current official chapter search text read. Do not assume all execution only services require the same suitability assessment.

sector_regulator | scope GB | legal: Use the FCA application category for the actual consumer investment activity, such as financial advice, wealth management, stockbroking or operating an investment platform.
Applies only: Where the firm's own UK investment activity requires authorisation; a software product label does not determine permission.
Source J:UK-FCA-WEALTH: Authorisation <https://www.fca.org.uk/firms/authorisation>. Checked 2026-11-03. Publication date not established. Directory supports regulator routing, not a complete account of permissions or exemptions.

data_privacy | scope GB | legal: COBS 9A requires sufficient, reliable client information about investment objectives, financial circumstances and relevant knowledge and experience.
Applies only: For the service's suitability assessment; retain UK GDPR role and access controls.
Source J:UK-COBS9A: COBS 9A Suitability <https://handbook.fca.org.uk/handbook/cobs9a>. Checked 2026-11-03. Current official chapter search text read. Do not assume all execution only services require the same suitability assessment.

proof | scope GB | legal: Demonstrate a suitability decision with reliable inputs, visible profiling limitations and evidence that ongoing client information stays current.
Applies only: For advice or portfolio management within COBS 9A; match the actual service and client.
Source J:UK-COBS9A: COBS 9A Suitability <https://handbook.fca.org.uk/handbook/cobs9a>. Checked 2026-11-03. Current official chapter search text read. Do not assume all execution only services require the same suitability assessment.

### spend-expense | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | operating: The employer owns the HMRC expense checking system. Identify its delegated payment approver and demonstrate the controls for bespoke subsistence claims.
Applies only: For bespoke or industry wide rates; benchmark scale rates have a different checking rule.
Source J:UK-HMRC-CHECK: EIM30275 Checking systems: models <https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30275>. Checked 2026-11-03. Publication date not reliably shown. Does not impose the same receipt check on benchmark scale rates after 2019.

sector_regulator | scope GB | legal: If an expense product also executes payments or issues electronic money, assess those activities against the Payment Services Regulations 2017 or Electronic Money Regulations 2011 before promising a regulated service.
Applies only: Only where the actual service includes an in scope payment or electronic money activity; expense record keeping alone does not establish that scope.
Source J:UK-FCA-PAYMENTS: Payment Services Regulations 2017 and Electronic Money Regulations 2011 <https://www.fca.org.uk/firms/payment-services-regulations-e-money-regulations>. Checked 2026-11-03. Updated 2025-12-17. Technical suppliers are not automatically payment institutions.

data_privacy | scope GB | legal: Restrict employee expense records to authorised users and preserve accuracy and recoverability under the ICO employment records guidance.
Applies only: For personal employment records in UK GDPR scope, not a mandate that every buyer use an identical approval hierarchy.
Source J:UK-ICO-EMPLOYMENT: Collecting and keeping employment records <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/employment-practices-and-data-protection-keeping-employment-records/collecting-and-keeping-employment-records>. Checked 2026-11-03. Publication date not reliably shown. Applicable to personal employment records; no universal HR role or retention period inferred.

proof | scope GB | legal: Demonstrate an expense trail linking date, purpose, amount and employee contribution to the employer's year end reporting evidence.
Applies only: For employer expenses and benefits reported to HMRC.
Source J:UK-HMRC-EXPENSE: Expenses and benefits for employers: Record keeping <https://www.gov.uk/employer-reporting-expenses-benefits/record-keeping>. Checked 2026-11-03. Publication date not shown. Scope is employer expense and benefit records, not all company accounting retention rules.

### insurance | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

decision_approvers | scope GB | legal: For insurance manufacture, PROD 4.2.9 makes the manufacturer's governing body responsible for endorsing and reviewing the product approval process.
Applies only: Only where the firm has the relevant manufacturing responsibility, including applicable lead firm arrangements.
Source J:UK-PROD42: PROD 4.2 Manufacture of insurance products <https://handbook.fca.org.uk/handbook/prod4/prod4s2>. Checked 2026-11-03. Current official chapter as of 2026-11-02. Scope includes manufacturing and relevant lead firm exceptions; not every insurance distributor.

sector_regulator | scope GB | legal: Distinguish an insurer from an insurance intermediary. New insurers apply to the Prudential Regulation Authority; the FCA lists a separate authorisation route for general insurance intermediaries.
Applies only: For authorisation of the relevant UK insurance business; do not treat an insurer's software supplier as the insurer.
Source J:UK-PRA-AUTH: New firm authorisation <https://www.bankofengland.co.uk/prudential-regulation/Authorisations/new-firm-authorisation>. Checked 2026-11-03. Publication date not shown. Not a claim that software providers need a banking or insurance authorisation.
Source J:UK-FCA-WEALTH: Authorisation <https://www.fca.org.uk/firms/authorisation>. Checked 2026-11-03. Publication date not established. Directory supports regulator routing, not a complete account of permissions or exemptions.

data_privacy | scope GB | legal: When underwriting or claims use health data, establish an Article 6 lawful basis and an Article 9 condition, plus applicable Data Protection Act conditions.
Applies only: Only for special category processing; ordinary financial data is not automatically special category data.
Source J:UK-ICO-SPECIAL: What are the rules on special category data <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/>. Checked 2026-11-03. Publication date not reliably shown. Do not treat all financial data as special category data. Automated decision rules are not asserted here.

proof | scope GB | legal: Show the insurance product approval record, target market review and corrective action history that PROD 4.2 requires to be documented for audit.
Applies only: For insurance manufacturers and products within PROD 4.2.
Source J:UK-PROD42: PROD 4.2 Manufacture of insurance products <https://handbook.fca.org.uk/handbook/prod4/prod4s2>. Checked 2026-11-03. Current official chapter as of 2026-11-02. Scope includes manufacturing and relevant lead firm exceptions; not every insurance distributor.

### customer-service | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### crm-marketing | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### collaboration | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-growth | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### construction | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### property-management | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### field-services | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### fmcg-retail-execution | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### industry-hr-payroll | specific | inherits vertical-saas
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

proof | scope GB | legal: For UK PAYE payroll, demonstrate the Full Payment Submission sent to HM Revenue and Customs on or before payday, with a controlled correction process.
Applies only: For employers reporting PAYE payroll; check permitted reporting exceptions for the actual circumstances.
Source J:UK-HMRC-PAYROLL: Running payroll: Reporting to HMRC: FPS <https://www.gov.uk/running-payroll/reporting-to-hmrc>. Checked 2026-11-03. Publication date not shown. PAYE payroll and reporting exceptions must be checked for the employer.

### hotel-lodging | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### retail-restaurant-ops | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### agents-copilots | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### voice-language-models | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### enterprise-search | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### it-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### bpo-cx | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-engineering | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### operators-connectivity | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### cpaas-messaging | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### telecom-software | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### business-voice-ucaas | specific | inherits telecom
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.

proof | scope GB | legal: For a covered UK voice service, test emergency access and caller location handling against Ofcom General Condition A3 rather than presenting ordinary call availability as sufficient.
Applies only: Only for providers and services within the condition's scope; confirm the service classification.
Source J:UK-OFCOM-GC: General Conditions of Entitlement <https://www.ofcom.org.uk/phones-and-broadband/accessibility/general-conditions-of-entitlement>. Checked 2026-11-03. Updated 2026-04-08. Each condition has its own regulated provider definition; not all software sellers are communications providers.

### developer-platform | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-infrastructure | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### observability | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### testing | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### dev-tools | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### cloud-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: cloud-security: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Show how customer environments are separated, how administration is controlled and which audit records the cloud service exposes. NCSC principles guide assurance; a self declaration is not proof of implementation.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-CLOUD: Cloud security principles <https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### identity-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: identity-security: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Show joiner, mover and leaver controls, privileged access restrictions and proportionate authentication. Include evidence that access is removed when duties or employment change.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-IDENTITY: 10 Steps: Identity and access management <https://www.ncsc.gov.uk/collection/10-steps/identity-and-access-management>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### email-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: email-security: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Demonstrate anti-spoofing, filtering, staff reporting and incident response together. NCSC treats phishing protection as layers; training completion alone does not establish email security.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-EMAIL: Phishing attacks: defending your organisation <https://www.ncsc.gov.uk/guidance/phishing>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### awareness-training | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: awareness-training: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Make training relevant to employees' work and use feedback to improve it. Include a practical route to report suspicious activity without blame.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-TRAINING: 10 Steps: Engagement and training <https://www.ncsc.gov.uk/collection/10-steps/engagement-and-training>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: appsec: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Show secure development rules, code review, protected build credentials and separation of production from development. Match assurance to the data the application handles.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-APPSEC: Cloud principle 7: Secure development <https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-7-secure-development>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### mobile-appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: mobile-appsec: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: For applications handling OFFICIAL data, show secure local storage, protected transmission and server enforced authorisation. Review what exposure to other applications or a compromised device means.
Applies only: NCSC guidance for applications handling OFFICIAL data; not a universal requirement for commercial apps.
Source J:UK-NCSC-MOBILE: Application development guidance introduction <https://www.ncsc.gov.uk/guidance/application-development-guidance-introduction>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### soc-services | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: soc-services: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Define what monitoring should detect, protect the logs and show how alerts reach an exercised response process. Collecting events alone does not demonstrate an effective monitoring service.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-SOC: 10 Steps: Logging and monitoring <https://www.ncsc.gov.uk/collection/10-steps/logging-and-monitoring>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### endpoint-network | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: endpoint-network: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Show hardened device configurations, restricted communication flows and containment between critical network components. Test recovery and the protection of administrative interfaces against the stated threat model.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-ENDPOINT: 10 Steps: Architecture and configuration <https://www.ncsc.gov.uk/collection/10-steps/architecture-and-configuration>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### document-ai | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### ai-video | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### engineering-talent | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-management | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-adoption | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### pentest | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: pentest: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Agree authorised targets, techniques and operational limits before testing. Track findings to remediation; a penetration test is a point in time assessment, not a permanent security guarantee.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-PENTEST: Penetration testing <https://www.ncsc.gov.uk/guidance/penetration-testing>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### attack-surface-dast | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: attack-surface-dast: check FCA Handbook and authorisation guidance; PRA rules; ICO UK GDPR guidance; relevant UK sector authority for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope GB | operating: Map scans to the asset inventory, including exposed application interfaces. Triage findings by exploitability and business impact, record mitigation and use manual testing where automated scans leave gaps.
Applies only: Voluntary UK NCSC guidance; any contractual obligation needs separate confirmation.
Source J:UK-NCSC-VULN: 10 Steps: Vulnerability management <https://www.ncsc.gov.uk/collection/10-steps/vulnerability-management>. Checked 2026-11-03. Voluntary guidance, not a universal procurement mandate. Publication date not reliably established.

### process-orchestration | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### open-source-support | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### iot-connectivity | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

## Western Europe

This draft covers Austria, Belgium, France, Germany, Liechtenstein, Luxembourg, Monaco, the Netherlands and Switzerland. The UK has its own file. This is a declared country scope, not a claim that all European markets are covered. EU provisions are attached only to the listed EU countries when that territorial scope is sourced. Liechtenstein, Monaco and Switzerland receive separately sourced notes. No country is a regional default. Draft for owner review. Final owner scope permits remaining subtypes to inherit. Specific means a sourced addition for the named country and activity, not complete country coverage. Pending topics retain narrower research gaps.
Countries: AT = Austria (EU member); BE = Belgium (EU member); FR = France (EU member); DE = Germany (EU member); LI = Liechtenstein; LU = Luxembourg (EU member); MC = Monaco; NL = Netherlands (EU member); CH = Switzerland
Clues, only in selling context: {"aliases":["Western Europe"],"countries":[{"code":"AT","name":"Austria","aliases":["Austria","Österreich"],"cities":["Vienna"],"currencies":[],"regulators":["Finanzmarktaufsicht"]},{"code":"BE","name":"Belgium","aliases":["Belgium","Belgique","België"],"cities":["Brussels"],"currencies":[],"regulators":["National Bank of Belgium"]},{"code":"FR","name":"France","aliases":["France"],"cities":["Paris","Lyon"],"currencies":[],"regulators":["Autorité de contrôle prudentiel et de résolution","Arcep"]},{"code":"DE","name":"Germany","aliases":["Germany","Deutschland"],"cities":["Berlin","Frankfurt","Munich"],"currencies":[],"regulators":["BaFin","Bundesnetzagentur"]},{"code":"LI","name":"Liechtenstein","aliases":["Liechtenstein"],"cities":["Vaduz"],"currencies":[],"regulators":["Financial Market Authority Liechtenstein"]},{"code":"LU","name":"Luxembourg","aliases":["Luxembourg"],"cities":[],"currencies":[],"regulators":["Commission de Surveillance du Secteur Financier"]},{"code":"MC","name":"Monaco","aliases":["Monaco"],"cities":[],"currencies":[],"regulators":["Commission de Contrôle des Activités Financières"]},{"code":"NL","name":"Netherlands","aliases":["Netherlands","Nederland"],"cities":["Amsterdam","Rotterdam"],"currencies":[],"regulators":["De Nederlandsche Bank"]},{"code":"CH","name":"Switzerland","aliases":["Switzerland","Schweiz","Suisse","Svizzera"],"cities":["Zurich","Geneva","Bern"],"currencies":[],"regulators":["FINMA","Federal Data Protection and Information Commissioner"]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country and legal entity will buy, and who approves the budget, operational risk and data processing?

procurement_payment | scope COMMON | question: What tender or contracting route, invoice currency, acceptance process and payment terms has this buyer specified?

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: For the listed EU countries, establish controller and processor roles under the General Data Protection Regulation. Put the processing contract and written subprocessor authorisation in place before personal data is shared.
Applies only: Only for processing within GDPR territorial and material scope; determine the parties' roles for each processing purpose.
Source J:EU-GDPR: Data controller or data processor <https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en>. Checked 2026-11-03. Publication date not shown. Territorial scope and actual processing role must be established.

data_privacy | scope CH | legal: Switzerland: under Article 9 of the Federal Act on Data Protection, check processor instructions, confidentiality and security, and obtain controller approval before further outsourcing.
Applies only: For processing within Swiss FADP scope. Separately check the countries of processing and any cross border disclosure.
Source J:CH-FADP: Outsourcing of data processing <https://www.edoeb.admin.ch/en/outsourcing-of-data-processing>. Checked 2026-11-03. Publication date not shown. Swiss law; cross border disclosure requires a separate assessment.

data_privacy | scope LI | legal: Liechtenstein: the Datenschutzstelle explains that an Article 28 GDPR contract must define the processing and the controller's and processor's respective duties.
Applies only: For a controller and processor relationship subject to GDPR in Liechtenstein; this does not establish the scope of other EU instruments.
Source J:LI-GDPR: Verantwortlicher <https://www.datenschutzstelle.li/datenschutz/themen-z/verantwortlicher>. Checked 2026-11-03. Publication date not shown. German primary guidance; do not infer applicability of other EU legislation from GDPR.

data_privacy | scope MC | legal: Monaco: Article 26 of Loi n° 1.565 du 3 décembre 2024 requires a written processor contract specifying the processing and the parties' obligations.
Applies only: For personal data processing subject to Monaco's law and a genuine controller and processor relationship.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

buyer_language | scope COMMON | question: Which language does each country's buying team require for the proposal, implementation, evidence and support?

proof | scope COMMON | question: Which buyer approved workflow and acceptance test would demonstrate value in the named country?

objections | scope COMMON | question: Which unresolved requirement could stop approval in this country, and whose evidence will settle it?

sales_motion | scope COMMON | question: Who owns the local pilot and the decision to proceed to a paid contract?

### logistics-tech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope CH | legal: Switzerland: OTR 1 governs covered professional driver records. The competent cantonal authority determines applicability.
Applies only: Check vehicle, route and exemptions rather than importing EU scope.
Source J:CH-ROAD: Ordonnance sur les chauffeurs OTR 1 <https://www.astra.admin.ch/fr/ordonnance-sur-les-chauffeurs-otr-1>. Checked 2026-11-03. Check vehicle route and exemptions.

sector_regulator | scope MC | legal: Monaco: Article 2 of Ordonnance souveraine no 1.302 requires prior Minister of State authorisation for Monaco public transport or vehicle hire enterprises.
Applies only: For activity within the France Monaco transport instrument, not merely a technology supplier.
Source J:MC-ROAD: Ordonnance souveraine no 1.302 <https://legimonaco.mc/tnc/ordonnance/1956/04-11-1.302/>. Checked 2026-11-03. France Monaco transport instrument, not all logistics software.

proof | scope AT,BE,FR,DE,LU,NL | legal: In the listed EU countries, test the road operator's workflow against Regulation (EC) No 561/2006, including the relevant vehicle and route scope and any national derogation.
Applies only: For covered road transport operations, not every logistics software workflow. Confirm the national exception rather than importing another country's.
Source J:EU-ROAD: Driving time and rest periods <https://transport.ec.europa.eu/transport-modes/road/social-provisions/driving-time-and-rest-periods_en>. Checked 2026-11-03. Publication date not shown. Vehicle and route scope plus national derogations matter; no blanket rule for all logistics software.

proof | scope LI | legal: Liechtenstein: covered tachograph operations require driver and vehicle records to be read and archived. Local guidance distinguishes cross border operations and exceptions.
Applies only: For vehicles and journeys within the locally stated scope.
Source J:LI-ROAD: Digitaler Fahrtenschreiber und Tachographenpflicht <https://www.llv.li/de/privatpersonen/mobilitaet-reisen-und-ausland/fuehrerschein/digitaler-fahrtenschreiber-und-tachographenpflicht>. Checked 2026-11-03. Cross border and national operations differ.

### fintech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: DORA requires the financial entity to assess ICT provider risk before contracting. Identify the buyer's accountable risk reviewer and supply evidence for that assessment.
Applies only: For the covered entity's third party ICT risk process; this does not classify every supplier as a designated critical provider.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

sector_regulator | scope CH | legal: Switzerland: FINMA has different authorisation routes for banking, securities, insurance and asset management. Start with the actual financial activity and legal entity.
Applies only: Where Swiss financial market law requires a permit, registration or other authorisation; ordinary technology supply alone does not establish that requirement.
Source J:CH-FINMA: Authorisation to operate in the financial market <https://www.finma.ch/en/authorisation/authorisation-overview/>. Checked 2026-11-03. Publication date not shown. Activity specific permits, registration or self regulatory organisation routes; no blanket fintech licence.

sector_regulator | scope LI | legal: Liechtenstein: the Financial Market Authority lists separate licensing routes for banks, investment firms, payment institutions and electronic money institutions. Confirm the activity before using a route.
Applies only: For an institution undertaking the relevant regulated activity in Liechtenstein, not solely a technology supplier.
Source J:LI-FMA: Financial Institutions Division <https://www.fma-li.li/en/financial-intermediaries/financial-institutions-division>. Checked 2026-11-03. Publication date not shown. Directory establishes routes, not complete substantive permissions.

sector_regulator | scope MC | legal: Monaco: financial activities under Act No. 1.338 require the relevant CCAF authorisation and a separate government business approval. Credit institution status also involves ACPR authorisation.
Applies only: Only for the financial activities and institutions covered by the cited formalities; do not extend this route to every fintech business.
Source J:MC-CCAF: Formalities for carrying out a financial activity <https://ccaf.mc/en/authorised-firms/carrying-out-a-financial-activity/formalities/>. Checked 2026-11-03. Publication date not shown. CCAF financial activity scope, not a general licence for all insurance or payment services.

procurement_payment | scope AT,BE,FR,DE,LU,NL | legal: For an EU financial entity within Regulation (EU) 2022/2554, DORA, prepare the ICT service description, processing locations, subcontracting terms and exit evidence needed for the buyer's contract review.
Applies only: For financial entities and ICT arrangements within DORA scope; identify whether a critical or important function is supported.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

### vertical-saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

proof | scope AT,BE,FR,DE,LU,NL | legal: Check the industry workflow against GDPR Article 35 and the national authority's DPIA list, including sensitive data, monitoring and significant automated decisions.
Applies only: For likely high risk processing; sector label alone is insufficient.
Source J:EU-DPIA: Be compliant: DPIA <https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en>. Checked 2026-11-03. Risk specific; check local list and exceptions.

proof | scope CH | legal: Switzerland: for high risk industry processing, the Article 22 DPIA describes the workflow, risks to individuals and protective measures.
Applies only: Where likely high risk is established, not every software deployment.
Source J:CH-DPIA: Data protection impact assessment <https://www.edoeb.admin.ch/en/data-protection-impact-assessment>. Checked 2026-11-03. Potential high risk threshold, not every software project.

proof | scope LI | legal: Liechtenstein: Article 35 requires prior assessment for likely high risk processing. Check the industry workflow against Datenschutzstelle criteria and the local list.
Applies only: Where the actual processing is likely high risk.
Source J:LI-DPIA: Datenschutz Folgenabschatzung <https://www.datenschutzstelle.li/datenschutz/themen-z/datenschutz-folgenabschaetzung>. Checked 2026-11-03. Local source verifies Liechtenstein applicability.

proof | scope MC | legal: Monaco: assess the industry workflow against Article 35 and Arrete ministeriel 2025-361 criteria, including profiling and significant automated decisions.
Applies only: Where the law's high risk criteria apply; do not import another country's DPIA list.
Source J:MC-DPIA: Arrete ministeriel 2025-361 <https://legimonaco.mc/tnc/arrete-ministeriel/2025/07-14-2025-361>. Checked 2026-11-03. Specific criteria, not blanket software approval.

### ai-native | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope CH | legal: Switzerland: the FADP applies to AI processing. FDPIC highlights transparency about purpose, functioning and data sources and a DPIA for high risk use.
Applies only: For AI using personal data in Swiss law scope, not EU AI Act applicability.
Source J:CH-AI: AI and data protection <https://www.edoeb.admin.ch/en/ai-and-data-protection>. Checked 2026-11-03. Swiss law, not EU AI Act.

data_privacy | scope LI | operating: Liechtenstein: Datenschutzstelle guidance asks AI users to establish supplier roles, training reuse, legal basis, transfers, accuracy, security and individual rights.
Applies only: Guidance for AI personal data use, not blanket product approval.
Source J:LI-AI: Kunstliche Intelligenz <https://www.datenschutzstelle.li/datenschutz/themen-z/kuenstliche-intelligenz>. Checked 2026-11-03. Guidance not product approval.

data_privacy | scope MC | legal: Monaco: Article 19 limits solely automated decisions with legal or similarly significant effects. Check exceptions and required human intervention and contest safeguards.
Applies only: For decisions within Article 19, not every AI output.
Source J:MC-PRIVACY-LAW: Loi no 1.565 du 3 decembre 2024 <https://legimonaco.mc/tnc/loi/2024/12-03-1.565>. Checked 2026-11-03. Current 27 October 2026 version; criminal justice chapter not applied to ordinary businesses.

proof | scope AT,BE,FR,DE,LU,NL | legal: For the listed EU markets, classify the provider or deployer role under the AI Act and demonstrate the Article 50 transparency measures that apply to the actual system.
Applies only: For AI systems within the Act's scope. Check the relevant paragraph, exceptions and transition before stating a duty or date.
Source J:EU-AI: Transparency obligations under Article 50 of the AI Act <https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act>. Checked 2026-11-03. Publication date not shown. Check the exact paragraph and transition; do not treat all AI obligations as applying on one date.

### ites | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: For outsourced IT or business processing, establish whether the service follows customer instructions or decides its own purposes. GDPR roles and subprocessor permissions follow that activity.
Applies only: For GDPR personal data processing; not every contractor is a processor.
Source J:EU-GDPR: Data controller or data processor <https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en>. Checked 2026-11-03. Publication date not shown. Territorial scope and actual processing role must be established.

data_privacy | scope CH | legal: Switzerland: outsourcing customer data retains the controller's Article 9 checks. Define service team access, instructions and onward outsourcing permissions.
Applies only: For outsourced personal data within Swiss FADP.
Source J:CH-FADP: Outsourcing of data processing <https://www.edoeb.admin.ch/en/outsourcing-of-data-processing>. Checked 2026-11-03. Publication date not shown. Swiss law; cross border disclosure requires a separate assessment.

data_privacy | scope LI | legal: Liechtenstein: specify the outsourced processing task and instructions in the Article 28 agreement before service staff handle personal data.
Applies only: For a GDPR controller processor relationship in Liechtenstein.
Source J:LI-GDPR: Verantwortlicher <https://www.datenschutzstelle.li/datenschutz/themen-z/verantwortlicher>. Checked 2026-11-03. Publication date not shown. German primary guidance; do not infer applicability of other EU legislation from GDPR.

data_privacy | scope MC | legal: Monaco: the outsourced provider must offer sufficient organisational and technical guarantees and follow documented processing instructions.
Applies only: For a processor within Loi no 1.565.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

### telecom | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope DE | legal: Germany: section 5 Telekommunikationsgesetz requires notification of covered public networks and publicly available services to Bundesnetzagentur. Number independent interpersonal telecommunications services are excluded from this notification.
Applies only: For the actual provider and service within section 5; other obligations can still apply to excluded services.
Source J:DE-TKG: Meldepflicht <https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Unternehmenspflichten/Meldepflicht/start.html>. Checked 2026-11-03. Publication date not shown. German version supplies the exclusion omitted in the shorter English page.

sector_regulator | scope FR | legal: France: Ordonnance n° 2021-650 removed the prior operator declaration under CPCE Article L.33-1. Arcep says operator status still follows the actual activity.
Applies only: For the prior declaration addressed by Arcep; this does not remove numbering, emergency access or other applicable duties.
Source J:FR-TELECOM: Questions fréquentes for communications operators <https://extranet.arcep.fr/communications-electroniques/questions-frequentes>. Checked 2026-11-03. Publication date not shown. Removal of this declaration does not remove other operator obligations.

sector_regulator | scope AT | legal: Austria: section 6 Telekommunikationsgesetz 2021 requires the intended provision, change or cessation of a covered public network or communications service to be notified to RTR.
Applies only: For networks or services within the notification scope; confirm the provider's actual role.
Source J:AT-TELECOM: General Authorization <https://www.rtr.at/TKP/was_wir_tun/telekommunikation/anbieterservice/allgemeingenehmigung/Allgemeingenehmigung.en.html>. Checked 2026-11-03. Publication date not shown. Establish the actual public network or service before assigning notification.

sector_regulator | scope BE | legal: Belgium: the Electronic Communications Act of 13 June 2005 and Royal Decree of 7 March 2007 govern BIPT notification before operator activity. Number independent interpersonal services are excluded from this notification.
Applies only: For covered Belgian operator activity; the notification exception does not establish exemption from all telecom duties.
Source J:BE-TELECOM: Notifying the BIPT <https://www.bipt.be/sectors/telecommunications/being-an-operator-in-belgium/notifying-the-bipt>. Checked 2026-11-03. Publication date not shown. Number independent interpersonal communications are excluded from this notification; other duties may remain.

sector_regulator | scope LU | legal: Luxembourg: Article 15 of the Loi du 17 décembre 2021 requires an undertaking subject to general authorisation to notify the ILR before providing the covered electronic communications network or service.
Applies only: Confirm the actual network, service and general authorisation scope.
Source J:LU-TELECOM: Notification et autorisation <https://www.ilr.lu/secteurs-activites/communications-electroniques/devenir-operateur/notification-et-autorisation/>. Checked 2026-11-03. Publication date not shown. Applies to undertakings subject to general authorisation; service classification matters.

sector_regulator | scope NL | legal: Netherlands: ACM's Telecommunicatiewet guidance requires notification for covered public electronic communications services, networks and associated facilities. Identify signal transport and the provider responsible to the customer.
Applies only: For activities meeting ACM's stated provider criteria; content creation or ordinary hosting alone does not establish the same role.
Source J:NL-TELECOM: Registratie telecomaanbieders <https://www.acm.nl/nl/telecom/telefonie-internet-tv-aanbieden/registratie-telecomaanbieders>. Checked 2026-11-03. Publication date not shown. Dutch primary guidance distinguishes signal transport from content and ordinary hosting.

sector_regulator | scope CH | legal: Switzerland: under the Telecommunications Act, the Federal Office of Communications registers providers using the specified licensed radio frequencies or nationally managed addressing resources.
Applies only: For the resources and provider relationships identified by Swiss OFCOM. Providers without those resources are not automatically on this register; other duties can still apply.
Source J:CH-TELECOM: Registration and publication as a TSP <https://www.bakom.admin.ch/en/registration-and-publication-as-a-tsp>. Checked 2026-11-03. Do not confuse Swiss OFCOM with UK Ofcom. Registration scope does not exhaust surveillance or other obligations.

sector_regulator | scope LI | legal: Liechtenstein: Article 19 Kommunikationsgesetz requires notification to the Amt für Kommunikation for covered electronic communications networks or services, excluding number independent interpersonal services.
Applies only: For the provider's actual service in Liechtenstein; do not apply the Swiss registration route.
Source J:LI-TELECOM: Melderegister, Meldepflicht und Meldung <https://www.llv.li/de/landesverwaltung/amt-fuer-kommunikation/elektronische-kommunikation/meldepflicht-meldung-und-melderegister>. Checked 2026-11-03. Publication date not shown. Liechtenstein source is llv.li; li.admin.ch is a Swiss surveillance authority and must not be used for Liechtenstein.

sector_regulator | scope MC | legal: Monaco: Ordonnance Souveraine n° 7.997, as amended by n° 12.143 in 2026, assigns telecom resources and operator concession oversight to the Direction des Plateformes et des Ressources Numériques.
Applies only: For Monaco telecom resources and operator activities within the retained remit; establish the required concession or authorisation for the actual activity.
Source J:MC-TELECOM-AUTH: Ordonnance Souveraine n° 7.997 du 12 mars 2020 <https://journaldemonaco.gouv.mc/fr/Journaux/2020/Journal-8488/Ordonnance-Souveraine-n-7.997-du-12-mars-2020-portant-creation-de-la-Direction-des-Plateformes-et-des-Ressources-Numeriques>. Checked 2026-11-03. Read with the 2026 amendment. Do not reuse the obsolete Direction des Communications Électroniques name.
Source J:MC-DIGITAL-2026: Ordonnance Souveraine n° 12.143 du 24 septembre 2026 <https://journaldemonaco.gouv.mc/Journaux/2026/Journal-8819/Ordonnance-Souveraine-n-12.143-du-24-septembre-2026-portant-creation-d-une-Delegation-Interministerielle-au-Numerique-et-des-Directions-la-composant>. Checked 2026-11-03. Only the retained telecommunications remit is used; do not infer broader licence procedures.

data_privacy | scope MC | legal: Monaco: Article 28-7 of Loi n° 1.383 protects private electronic correspondence handled by covered communications operators and online correspondence services. Review access to message content and associated identity data.
Applies only: For the operators and services within that article, subject to its statutory exceptions; not a blanket prohibition on authorised security processing.
Source J:MC-CORRESPONDENCE: Loi n° 1.383 du 2 août 2011 pour une Principauté numérique <https://legimonaco.mc/tnc/loi/2011/08-02-1.383>. Checked 2026-11-03. Publication date not established from current consolidated text. Search retrieved version current 2026-10-01. Direct fetch timed out; read primary indexed Article 28-7. Specific legal exceptions remain.

### cybersecurity | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: For an EU buyer, assess Directive (EU) 2022/2555, NIS2, through the named country's implementation and the buyer's entity category. The Commission's transposition tracker is not a substitute for the applicable national instrument.
Applies only: Where NIS2 may cover the entity; do not assume a uniform national filing route or deadline.
Source J:EU-NIS2: NIS2 Directive transposition in EU countries <https://digital-strategy.ec.europa.eu/en/policies/nis-transposition>. Checked 2026-11-03. Publication date not established. Tracker is a state of play, not a final finding of national legal compliance.

sector_regulator | scope LI | legal: Liechtenstein: covered financial entities follow DORA; FMA ICT Security Directive 2021/3 remains for supervised entities outside DORA. Establish the buyer's category first.
Applies only: For the relevant FMA supervised entity, not every cybersecurity customer.
Source J:LI-DORA: DORA FAQs <https://www.fma-li.li/en/supervision-regulation/dora/faqs>. Checked 2026-11-03. English page machine translated; applicability verified separately from EU membership.

proof | scope CH | legal: Switzerland: the Information Security Act and Cybersecurity Ordinance require reporting of qualifying cyberattacks by covered critical infrastructure operators. Show how detection evidence reaches the buyer's reporting owner.
Applies only: Only for covered entities and incidents after checking ordinance exemptions; a security supplier is not automatically the reporting entity.
Source J:CH-CYBER: Legal basis for the reporting obligation <https://www.bacs.admin.ch/en/legal-basis-for-the-reporting-obligation>. Checked 2026-11-03. Publication date not shown. Entity, incident and ordinance exemptions must be checked; not every Swiss company is covered.

proof | scope MC | legal: Monaco: Article 31 security evidence should address unauthorised access, loss, alteration and recovery and evaluation of the measures.
Applies only: For covered personal data processing, not a universal security certification.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

### software | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: For manufacturers of products with digital elements in CRA scope, Article 14 reporting covers actively exploited vulnerabilities and severe security incidents from September 2026.
Applies only: Check product scope and exclusions; standalone SaaS and open source steward obligations are not automatically identical.
Source J:EU-CRA-REPORT: Cyber Resilience Act reporting obligations <https://digital-strategy.ec.europa.eu/en/policies/cra-reporting>. Checked 2026-11-03. Product scope and exceptions apply; open source stewards have later commencement.

data_privacy | scope CH | legal: Switzerland: Article 7 makes the controller plan data protection and limit data through default settings. Demonstrate the relevant application settings.
Applies only: For FADP personal data processing; do not assign controller duties to a producer without that role.
Source J:CH-PRIVACY-DESIGN: Federal Act on Data Protection <https://www.fedlex.admin.ch/eli/cc/2022/491/en>. Checked 2026-11-03. English informational translation; actual processing scope applies.

data_privacy | scope LI | legal: Liechtenstein: where a software service processes customer personal data, establish its Article 28 role and contractual protections. Software sale alone does not establish processor status.
Applies only: For actual GDPR processing on behalf of a controller.
Source J:LI-GDPR: Verantwortlicher <https://www.datenschutzstelle.li/datenschutz/themen-z/verantwortlicher>. Checked 2026-11-03. Publication date not shown. German primary guidance; do not infer applicability of other EU legislation from GDPR.

data_privacy | scope MC | legal: Monaco: Article 31 requires risk appropriate security and evaluation of controls. Demonstrate the measures relevant to the application's personal data.
Applies only: For covered controller or processor activity under Loi no 1.565.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

### saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope CH | legal: Switzerland: hosted processors need controller approval for further outsourcing and must preserve instructions, confidentiality and security. Show the hosting and support subcontractor chain.
Applies only: FADP Article 9 scope; cross border disclosure needs a separate assessment.
Source J:CH-FADP: Outsourcing of data processing <https://www.edoeb.admin.ch/en/outsourcing-of-data-processing>. Checked 2026-11-03. Publication date not shown. Swiss law; cross border disclosure requires a separate assessment.

data_privacy | scope LI | legal: Liechtenstein: an Article 28 agreement defines the hosted processing, duration and controller and processor duties.
Applies only: For a GDPR controller processor relationship in Liechtenstein.
Source J:LI-GDPR: Verantwortlicher <https://www.datenschutzstelle.li/datenschutz/themen-z/verantwortlicher>. Checked 2026-11-03. Publication date not shown. German primary guidance; do not infer applicability of other EU legislation from GDPR.

data_privacy | scope MC | legal: Monaco: a hosted processor follows documented instructions under an Article 26 written agreement defining the service, data and parties' duties.
Applies only: For personal data processing within Loi no 1.565.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

proof | scope AT,BE,FR,DE,LU,NL | legal: For hosted SaaS in the listed EU countries, show the processor agreement, authorised subprocessor chain and controls enabling the controller's data protection duties.
Applies only: For GDPR processing on a controller's behalf; assess roles per purpose.
Source J:EU-GDPR: Data controller or data processor <https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en>. Checked 2026-11-03. Publication date not shown. Territorial scope and actual processing role must be established.
Source J:EU-PRIVACY-DESIGN: Guidelines 4/2019 Article 25 <https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf>. Checked 2026-11-03. Article 25 does not directly address every producer or processor.

### freight-visibility | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### freight-marketplace | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### seller-shipping | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### last-mile | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### warehousing | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### transport-management | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### payments-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: MC: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.; CH: waiting for decision_approvers, data_privacy, proof. Named source checks: FINMA Banking Act, FinIA and Insurance Supervision Act guidance; FDPIC current FADP guidance. Existing notes retain their stated activity scope.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: DORA Article 5 assigns ICT risk framework approval and oversight to the financial entity's management body.
Applies only: For DORA financial entities within Article 5, after checking exclusions and the simplified framework.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

decision_approvers | scope LI | legal: Liechtenstein applies DORA through its EEA DORA Implementation Act. For covered entities, Article 5 places ICT framework approval with the management body.
Applies only: For covered banks or payment institutions; check DORA exclusions and simplified framework.
Source J:LI-DORA: DORA FAQs <https://www.fma-li.li/en/supervision-regulation/dora/faqs>. Checked 2026-11-03. English page machine translated; applicability verified separately from EU membership.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: Under Directive (EU) 2015/2366, PSD2, national authorities authorise payment institutions. Use the EBA register to locate the entity and then verify the national authorisation and services.
Applies only: For covered payment or electronic money institutions; the EBA register itself confers no legal rights.
Source J:EU-PSD2: Register of payment and electronic money institutions under PSD2 <https://eba.europa.eu/risk-and-data-analysis/data/registers/payment-institutions-register>. Checked 2026-11-03. Publication date not shown. Central register has no legal significance; national register controls.

sector_regulator | scope DE | legal: Germany: the Zahlungsdiensteaufsichtsgesetz provides BaFin authorisation routes for payment institutions and electronic money institutions. Confirm the actual activity and exclusions.
Applies only: For the activities and institutions within ZAG; do not infer payment institution status from supplying an API.
Source J:DE-PAYMENTS: Payment institutions and electronic money institutions <https://www.bundesbank.de/en/tasks/financial-supervision/individual-aspects/payment-institutions-and-e-money-institutions-622962>. Checked 2026-11-03. Publication date not shown. Exclusions and actual service model must be checked.

sector_regulator | scope AT | legal: Austria: FMA licenses payment institutions under ZaDiG 2018 and registers account information service providers.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:AT-PAYMENTS: Licencing and Registration of Payment Services <https://www.fma.gv.at/en/financial-service-providers/payment-institutions/licencing-and-registration-of-payment-services/>. Checked 2026-11-03. No publication date shown. Check actual payment activity and exemptions.

sector_regulator | scope BE | legal: Belgium: The Act of 11 March 2018 governs payment and electronic money institutions; verify the NBB authorisation category.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:BE-PAYMENTS: Act of 11 March 2018 on payment institutions and electronic money institutions <https://www.nbb.be/en/financial-supervision-and-resolution/cross-cutting-and-international-aspects/news-and/act-11-march>. Checked 2026-11-03. Act date is 11 March; publication date is 26 March. Do not conflate them.
Source J:BE-AUTH: Information on authorisations <https://www.nbb.be/en/financial-oversight/general/authorisation-information>. Checked 2026-11-03. No publication date shown. Does not give NBB every FSMA conduct or investment adviser function.

sector_regulator | scope FR | legal: France: Under the Code monetaire et financier, ACPR authorises payment institutions; account information only providers use registration.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:FR-PAYMENTS: Etablissement de paiement et prestataire de service information sur les comptes <https://acpr.banque-france.fr/en/node/26808>. Checked 2026-11-03. No publication date shown. ACPR route and Banque de France security opinion; simplified route limitations retained.

sector_regulator | scope LU | legal: Luxembourg: CSSF authorisation or registration under the Law of 10 November 2009 depends on payment, electronic money or account information activity.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:LU-PAYMENTS: Authorisation procedure of a PI or EMI or registration of an AISP <https://www.cssf.lu/en/authorisation-procedure-payment-institution-or-electronic-money-institution-registration-aisp/>. Checked 2026-11-03. No publication date shown. Use actual activity; limited network exclusions can still require notification.

sector_regulator | scope NL | legal: Netherlands: Payment service market access falls under the Wft; DNB handles authorisation and prudential supervision, with AFM conduct supervision.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:NL-PAYMENTS: Laws and regulations on market access of payment service providers <https://www.dnb.nl/en/sector-information/open-book-supervision/open-book-supervision-sectors/payment-institutions/licensing-requirement-for-payment-service-providers-overview/laws-and-regulations-on-the-market-access-of-payment-service-providers/>. Checked 2026-11-03. DNB current page identifies PSD2 basis. No claim that all payments software is regulated.

sector_regulator | scope CH | legal: Switzerland: Distinguish a banking licence from the Article 1b Banking Act FinTech licence, which restricts investment of accepted deposits and payment of interest.
Applies only: For the entity actually performing the regulated activity, after checking exclusions, existing permissions and cross border routes.
Source J:CH-FINTECH-LICENCE: FinTech licence <https://www.finma.ch/en/authorisation/fintech/fintech-bewilligung/>. Checked 2026-11-03. No publication date shown. Does not establish that every payment software provider needs a licence.

sector_regulator | scope LI | legal: Liechtenstein: FMA authorises payment institutions under ZDG and ZDV. A provider performing only account information services uses registration.
Applies only: For covered payment services after checking the statutory activity and exemptions.
Source J:LI-PAYMENTS: FMA Guidelines 2019/8 Licence as a payment institution <https://www.fma-li.li/fma-li/documents/rechtsgrundlagen/wegleitungen/fma-wl-2019-8-en.pdf>. Checked 2026-11-03. Last amended 12 December 2024. Payment activity and exclusions must be established.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: Payment initiation providers must not store sensitive payment data; account information providers must restrict data use to the requested account information service.
Applies only: For the respective PSD2 services as implemented nationally, not every payment platform.
Source J:EU-PSD2-LAW: Directive 2015/2366 Payment Services Directive <https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32015L2366>. Checked 2026-11-03. Directive applied through national law. Service specific obligations are not rules for every payment software product.

data_privacy | scope LI | legal: Liechtenstein ZDG Article 100 limits service data processing to what is necessary and addresses user consent, alongside applicable data protection legislation.
Applies only: For covered payment service data processing, with the statutory exceptions checked.
Source J:LI-PAYMENT-DATA: Payment Services Act translation <https://www.regierung.li/files/attachments/950-1-zdg-250201-en.pdf>. Checked 2026-11-03. English translation of 1 February 2025 version; authoritative German law prevails. Official indexed text read; subsequent direct PDF fetch returned 404.

proof | scope AT,BE,FR,DE,LU,NL | legal: For payment initiation or account information services, show how credentials are protected and account access stays within the permitted service.
Applies only: For the Article 66 or 67 service performed by the authorised or registered provider.
Source J:EU-PSD2-LAW: Directive 2015/2366 Payment Services Directive <https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32015L2366>. Checked 2026-11-03. Directive applied through national law. Service specific obligations are not rules for every payment software product.

proof | scope LI | legal: Liechtenstein ZDG Article 101 requires operational and security controls and risk assessment reporting. Show incident handling and mitigation evidence for the payment service.
Applies only: For payment service providers within the current Article 101 scope.
Source J:LI-PAYMENT-DATA: Payment Services Act translation <https://www.regierung.li/files/attachments/950-1-zdg-250201-en.pdf>. Checked 2026-11-03. English translation of 1 February 2025 version; authoritative German law prevails. Official indexed text read; subsequent direct PDF fetch returned 404.

### core-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: MC: waiting for decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: DORA Article 5 assigns ICT risk framework approval and oversight to the financial entity's management body.
Applies only: For DORA financial entities within Article 5, after checking exclusions and the simplified framework.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

decision_approvers | scope LI | legal: Liechtenstein applies DORA through its EEA DORA Implementation Act. For covered entities, Article 5 places ICT framework approval with the management body.
Applies only: For covered banks or payment institutions; check DORA exclusions and simplified framework.
Source J:LI-DORA: DORA FAQs <https://www.fma-li.li/en/supervision-regulation/dora/faqs>. Checked 2026-11-03. English page machine translated; applicability verified separately from EU membership.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

decision_approvers | scope CH | legal: Switzerland: the bank specifies internal outsourcing approval and signing responsibilities. FINMA Circular 2018/3 requires a responsible monitoring unit while retaining accountability with the bank.
Applies only: For significant outsourced functions within the circular; check applicable proportionality and exemptions.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

sector_regulator | scope AT | legal: Austria: the ECB lists Finanzmarktaufsicht as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope BE | legal: Belgium: the ECB lists National Bank of Belgium as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope FR | legal: France: the ECB lists Autorité de contrôle prudentiel et de résolution as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope DE | legal: Germany: the ECB lists BaFin as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope LU | legal: Luxembourg: the ECB lists Commission de Surveillance du Secteur Financier as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope NL | legal: Netherlands: the ECB lists De Nederlandsche Bank as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope CH | legal: Switzerland: FINMA's Article 1a Banking Act assessment concerns the bank's deposit or refinancing activity; the core system supplier does not acquire a banking licence by supplying software.
Applies only: For the relevant regulated institution and activity; establish the legal entity and permission before mapping platform controls.
Source J:CH-BANK: Authorisation requirements for banks <https://www.finma.ch/en/authorisation/banks-and-securities-firms/getting-licensed/banks/>. Checked 2026-11-03. No publication date shown. Actual deposit or refinancing activity determines scope; no numerical threshold is reproduced.

sector_regulator | scope LI | legal: Liechtenstein: Use the BankA framework effective from February 2025 for banks; investment firms have separate WPFG and WPDG requirements.
Applies only: For the relevant regulated institution and activity; establish the legal entity and permission before mapping platform controls.
Source J:LI-BANK-FRAMEWORK: New legal framework for the supervision of banks and investment firms <https://www.fma-li.li/en/news/neuer-rechtsrahmen-fuer-die-aufsicht-ueber-banken-und-wertpapierfirmen-1090>. Checked 2026-11-03. Do not substitute the former single Banking Act framework for the new split.

sector_regulator | scope MC | legal: Monaco: Credit institution status involves ACPR authorisation. Keep the banking authorisation distinct from CCAF approval for enumerated investment activities.
Applies only: For the relevant regulated institution and activity; establish the legal entity and permission before mapping platform controls.
Source J:MC-CCAF: Formalities for carrying out a financial activity <https://ccaf.mc/en/authorised-firms/carrying-out-a-financial-activity/formalities/>. Checked 2026-11-03. Publication date not shown. CCAF financial activity scope, not a general licence for all insurance or payment services.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: For credit institutions in the Single Supervisory Mechanism, the ECB grants the banking licence through the relevant national authority entry point. The country supervisor listed here is not a substitute for this authorisation.
Applies only: For banks in the SSM licensing framework; verify legal entity, activity and any exemption.
Source J:EU-BANK-LICENCE: Authorisations <https://www.bankingsupervision.europa.eu/activities/authorisation/html/index.en.html>. Checked 2026-11-03. Banking Union credit institution route; other financial entities and national exemptions need separate treatment.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: DORA Article 30 requires ICT contracts to identify processing and storage countries and address data protection. This is not an EU only hosting mandate.
Applies only: For ICT contracts of covered EU financial entities under DORA Article 30.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

data_privacy | scope LI | legal: DORA Article 30 requires ICT contracts to identify processing and storage countries and address data protection. This is not an EU only hosting mandate.
Applies only: For covered Liechtenstein entities under the EEA DORA Implementation Act and DORA Article 30.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.
Source J:LI-DORA: DORA FAQs <https://www.fma-li.li/en/supervision-regulation/dora/faqs>. Checked 2026-11-03. English page machine translated; applicability verified separately from EU membership.

data_privacy | scope CH | legal: Swiss bank outsourcing contracts must define security controls. Overseas arrangements must preserve enforceable audit access and access in Switzerland to information needed for restructuring or resolution.
Applies only: For outsourcing within Circular 2018/3; this does not impose Swiss only hosting.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

proof | scope AT,BE,FR,DE,LU,NL | legal: DORA Article 24 calls for proportionate resilience testing and documented correction of weaknesses. Show the bank's relevant test and remediation evidence.
Applies only: For covered EU banks, accounting for microenterprise and simplified framework provisions.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

proof | scope LI | legal: DORA Article 24 calls for proportionate resilience testing and documented correction of weaknesses. Show the bank's relevant test and remediation evidence.
Applies only: For covered Liechtenstein banks under the EEA DORA Implementation Act, accounting for relevant exceptions.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.
Source J:LI-DORA: DORA FAQs <https://www.fma-li.li/en/supervision-regulation/dora/faqs>. Checked 2026-11-03. English page machine translated; applicability verified separately from EU membership.

proof | scope CH | legal: Show the outsourced function inventory, risk assessment, monitoring evidence and enforceable bank, auditor and FINMA inspection rights.
Applies only: For the bank's significant outsourced functions and relevant subcontractors.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

### lending | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: LI: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FMA Liechtenstein BankA/WPFG/WPDG framework, ZDG guidelines and DORA FAQs; Datenschutzstelle guidance. Existing notes retain their stated activity scope.; MC: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.; CH: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FINMA Banking Act, FinIA and Insurance Supervision Act guidance; FDPIC current FADP guidance. Existing notes retain their stated activity scope.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: The EBA loan guidelines place the credit decision with the authorised decision maker under the institution's policies and governance. Identify that delegation rather than assume a universal committee.
Applies only: For institutions and credit products within EBA/GL/2020/06; national supervisory applicability must be confirmed.
Source J:EU-LOAN-GL: EBA Guidelines on loan origination and monitoring <https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2020/Guidelines%20on%20loan%20origination%20and%20monitoring/884283/EBA%20GL%202020%2006%20Final%20Report%20on%20GL%20on%20loan%20origination%20and%20monitoring.pdf>. Checked 2026-11-03. Official indexed final text read; direct PDF fetch 403. Not consultation responses. Check institution and credit product scope.

sector_regulator | scope DE | legal: Germany: the Bundesbank explains activity based authorisation under the Kreditwesengesetz. Determine whether the business conducts regulated banking or financial services before assigning a lending permission.
Applies only: For the business's own regulated activity; technology support for a lender does not alone establish authorisation scope.
Source J:DE-FINTECH: FinTech technology enabled financial innovation <https://www.bundesbank.de/en/tasks/financial-supervision/individual-aspects/fintech-622840>. Checked 2026-11-03. Publication date not shown. Fintech is not a separate legal category and not all fintech is regulated.

sector_regulator | scope AT | legal: Austria: banking transactions within BWG require the applicable authorisation. FMA distinguishes CRR banks using the ECB route from institutions authorised nationally.
Applies only: For the stated regulated lender and credit activity, with exemptions and existing permissions checked.
Source J:AT-BANK-LICENCE: Licensing and notification <https://www.fma.gv.at/en/banks/licensing-notification/>. Checked 2026-11-03. Applies to regulated banking transactions, not all lending software.

sector_regulator | scope BE | legal: Belgium: FSMA supervises access for consumer and mortgage credit providers. Determine that credit category before selecting the permission.
Applies only: For the stated regulated lender and credit activity, with exemptions and existing permissions checked.
Source J:BE-CREDIT: Credit provider <https://www.fsma.be/en/credit-provider>. Checked 2026-11-03. Consumer and mortgage credit scope; not a universal corporate lending permission.

sector_regulator | scope FR | legal: France: habitual own account lending can require ACPR authorisation as a societe de financement under the Code monetaire et financier.
Applies only: For the stated regulated lender and credit activity, with exemptions and existing permissions checked.
Source J:FR-CREDIT: Societe de financement <https://acpr.banque-france.fr/fr/professionnels/lacpr-vous-accompagne/banque/creer-ma-societe/mes-procedures/societe-de-financement>. Checked 2026-11-03. Financing company route; separate payment electronic money and investment permissions.

sector_regulator | scope LU | legal: Luxembourg: professionals granting loans to the public on own account can fall under Article 28-4 of the Law of 5 April 1993 and CSSF supervision.
Applies only: For the stated regulated lender and credit activity, with exemptions and existing permissions checked.
Source J:LU-CREDIT: Adaptation of FAQ on PFS granting loans to the public <https://www.cssf.lu/en/2021/06/adaptation-of-the-faq-on-the-statuses-of-pfs-with-respect-to-the-pfs-status-relating-to-the-granting-of-loans-to-the-public-article-28-4-of-the-law-of-5-april-1993-on-the-financial-sector-lfs/>. Checked 2026-11-03. Activity based assessment; not authority to collect deposits.

sector_regulator | scope NL | legal: Netherlands: nonbank credit providers use the applicable AFM route. A bank with the relevant ECB or DNB licence can offer credit under the Wft without a separate AFM licence.
Applies only: For the stated regulated lender and credit activity, with exemptions and existing permissions checked.
Source J:NL-CREDIT: Licence application and bank market entry <https://www.afm.nl/nl-nl/sector/themas/verplichtingen-voor-ondernemingen/melden-en-aanvragen/vergunningaanvraag>. Checked 2026-11-03. Nonbank financial services route. Exemptions and existing bank licence permissions need checking.
Source J:NL-BANK-PERMISSIONS: Toetreding banks <https://www.afm.nl/nl-nl/sector/banken/toetreding>. Checked 2026-11-03. Applies to banks already holding the relevant licence.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: Before the loan agreement, the EBA guidelines call for sufficient, accurate and current borrower data supporting creditworthiness and risk assessment.
Applies only: For credit assessments within the guidelines; collection must also comply with applicable personal data law.
Source J:EU-LOAN-GL: EBA Guidelines on loan origination and monitoring <https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2020/Guidelines%20on%20loan%20origination%20and%20monitoring/884283/EBA%20GL%202020%2006%20Final%20Report%20on%20GL%20on%20loan%20origination%20and%20monitoring.pdf>. Checked 2026-11-03. Official indexed final text read; direct PDF fetch 403. Not consultation responses. Check institution and credit product scope.

proof | scope AT,BE,FR,DE,LU,NL | legal: The documented assessment must justify approval or refusal. Preserve the decision conditions and evidence that prerequisites were met before agreement and disbursement.
Applies only: For the loan origination process within EBA/GL/2020/06 paragraphs 193 to 198.
Source J:EU-LOAN-GL: EBA Guidelines on loan origination and monitoring <https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2020/Guidelines%20on%20loan%20origination%20and%20monitoring/884283/EBA%20GL%202020%2006%20Final%20Report%20on%20GL%20on%20loan%20origination%20and%20monitoring.pdf>. Checked 2026-11-03. Official indexed final text read; direct PDF fetch 403. Not consultation responses. Check institution and credit product scope.

### wealth-investment | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: LI: waiting for decision_approvers, data_privacy, proof. Named source checks: FMA Liechtenstein BankA/WPFG/WPDG framework, ZDG guidelines and DORA FAQs; Datenschutzstelle guidance. Existing notes retain their stated activity scope.; MC: waiting for decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.; CH: waiting for decision_approvers, data_privacy, proof. Named source checks: FINMA Banking Act, FinIA and Insurance Supervision Act guidance; FDPIC current FADP guidance. Existing notes retain their stated activity scope.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: Under Article 22 of Regulation 2017/565, the management body appoints the compliance officer; the compliance function reports on controls and deficiencies.
Applies only: For MiFID investment firms. Confirm the buyer's delegated purchasing authority separately.
Source J:EU-MIFID-ORG: Delegated Regulation 2017/565 consolidated 2 August 2022 <https://eur-lex.europa.eu/eli/reg_del/2017/565/2022-08-02/eng>. Checked 2026-11-03. Current consolidation confirmed by EUR Lex. Consolidation is informational; official legal acts prevail.

sector_regulator | scope AT | legal: Austria: WAG 2018 Article 3 requires the relevant investment service licence from FMA.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:AT-WEALTH: Licences: Investment service providers <https://www.fma.gv.at/en/financial-service-providers/investment-service-providers/licences/>. Checked 2026-11-03. No publication date shown. General application information is under revision; current page still states licence route.

sector_regulator | scope BE | legal: Belgium: Separate FSMA's portfolio management and investment advice category from NBB's stockbroking authorisation category.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:BE-WEALTH: Portfolio management and investment advice company <https://www.fsma.be/en/portfolio-management-and-investment-advice-company>. Checked 2026-11-03. Selected English guidance only; no legal detail borrowed from outdated 2013 consolidated law.
Source J:BE-AUTH: Information on authorisations <https://www.nbb.be/en/financial-oversight/general/authorisation-information>. Checked 2026-11-03. No publication date shown. Does not give NBB every FSMA conduct or investment adviser function.

sector_regulator | scope FR | legal: France: AMF authorises portfolio management companies; other investment services use ACPR authorisation after AMF programme approval.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:FR-WEALTH: Provide investment services in France <https://www.amf-france.org/en/professionals/investment-services-providers/my-relations-amf/provide-investment-services>. Checked 2026-11-03. Separate AMF asset management company route must not be conflated.
Source J:FR-AMF-AUTH: Authorise <https://www.amf-france.org/en/amf/amf-regulation/authorise>. Checked 2026-11-03. No publication date captured. Different professional categories use different routes.

sector_regulator | scope DE | legal: Germany: Separate investment services under WpIG from financial services under KWG before choosing the permission route.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:DE-WEALTH: Investment institutions and financial services institutions <https://www.bundesbank.de/en/tasks/financial-supervision/individual-aspects/investment-institutions-and-financial-services-institutions>. Checked 2026-11-03. No publication date shown. Current article distinguishes regimes unlike older financial services summary.

sector_regulator | scope LU | legal: Luxembourg: CSSF authorises investment firms under Articles 13 to 24-9 of the Law of 5 April 1993.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:LU-WEALTH: Legal requirements and authorisation procedure for investment firms <https://www.cssf.lu/en/legal-requirements-authorisation-procedure-investment-firms/>. Checked 2026-11-03. Updated 2026-03-04. Different requirements apply to particular activities and client asset permissions.

sector_regulator | scope NL | legal: Netherlands: AFM issues investment firm authorisations. Do not use the DNB payments licence as evidence of investment permissions.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:NL-FINANCIAL-AUTH: Authorisation and supervision <https://www.afm.nl/en/sector/themas/over-het-toezicht-en-beleid-van-de-afm/authorisation-and-supervision>. Checked 2026-11-03. No publication date shown. Activity specific route, not universal AFM licensing.

sector_regulator | scope CH | legal: Switzerland: Commercial portfolio managers require FINMA authorisation under FinIA and normally ongoing supervision by a supervisory organisation.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:CH-PORTFOLIO: Portfolio managers and trustees <https://www.finma.ch/en/authorisation/portfolio-managers-and-trustees/>. Checked 2026-11-03. No publication date shown. Group supervision exceptions apply.

sector_regulator | scope LI | legal: Liechtenstein: Investment firms use the WPFG and investment services use the WPDG under the framework effective from February 2025.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:LI-BANK-FRAMEWORK: New legal framework for the supervision of banks and investment firms <https://www.fma-li.li/en/news/neuer-rechtsrahmen-fuer-die-aufsicht-ueber-banken-und-wertpapierfirmen-1090>. Checked 2026-11-03. Do not substitute the former single Banking Act framework for the new split.

sector_regulator | scope MC | legal: Monaco: CCAF authorisation under amended Act No. 1.338 applies to the listed portfolio management and order reception or transmission activities.
Applies only: For the specified investment entity and activity; check exemptions, group supervision and cross border permissions.
Source J:MC-WEALTH: Management advisory services and reception transmission of orders <https://ccaf.mc/en/authorised-firms/financial-activities/management-advisory-services-and-reception-transmission-of-orders/>. Checked 2026-11-03. No publication date shown. Only enumerated regulated activities.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: Article 21 requires systems that protect information security, integrity and confidentiality. Suitability workflows also need reliable client information for the relevant assessment.
Applies only: For the investment firm and covered advisory or portfolio service.
Source J:EU-MIFID-ORG: Delegated Regulation 2017/565 consolidated 2 August 2022 <https://eur-lex.europa.eu/eli/reg_del/2017/565/2022-08-02/eng>. Checked 2026-11-03. Current consolidation confirmed by EUR Lex. Consolidation is informational; official legal acts prevail.

proof | scope AT,BE,FR,DE,LU,NL | legal: For an EU investment firm, check the national register for the legal entity and authorised investment activities. ESMA's consolidated register points back to national authorities.
Applies only: For regulated investment services; the evidence must match the actual entity and service offered.
Source J:EU-INVEST: Is the firm regulated? <https://www.esma.europa.eu/investor-corner/is-the-firm-regulated>. Checked 2026-11-03. Publication date not shown. Check the actual legal entity and service; database inclusion does not replace licence scope review.

proof | scope AT,BE,FR,DE,LU,NL | legal: For retail investment advice, Article 54 requires a suitability report explaining the recommendation against the client's circumstances, objectives and risk capacity. Automation does not transfer the firm's assessment responsibility.
Applies only: For advice requiring suitability assessment; distinguish execution only and other services.
Source J:EU-MIFID-ORG: Delegated Regulation 2017/565 consolidated 2 August 2022 <https://eur-lex.europa.eu/eli/reg_del/2017/565/2022-08-02/eng>. Checked 2026-11-03. Current consolidation confirmed by EUR Lex. Consolidation is informational; official legal acts prevail.

### spend-expense | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: AT: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FMA banking, payments, WAG 2018 and VAG 2016 licensing guidance. Existing notes retain their stated activity scope.; BE: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: NBB authorisation categories and FSMA credit provider and portfolio management guidance. Existing notes retain their stated activity scope.; FR: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: ACPR authorisation procedures and AMF investment service guidance. Existing notes retain their stated activity scope.; DE: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: BaFin ZAG and VAG guidance and Bundesbank KWG/WpIG authorisation guidance. Existing notes retain their stated activity scope.; LI: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FMA Liechtenstein BankA/WPFG/WPDG framework, ZDG guidelines and DORA FAQs; Datenschutzstelle guidance. Existing notes retain their stated activity scope.; LU: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CSSF Law of 5 April 1993 and payments guidance; CAA insurance law consolidated 3 April 2026. Existing notes retain their stated activity scope.; MC: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.; NL: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: DNB Wft authorisation guidance and AFM licence application guidance. Existing notes retain their stated activity scope.; CH: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FINMA Banking Act, FinIA and Insurance Supervision Act guidance; FDPIC current FADP guidance. Existing notes retain their stated activity scope.

procurement_payment | scope FR | legal: France's invoicing rollout requires receipt from September 2026 when the supplier must issue electronically. Large and intermediate enterprises issue from that date; smaller and micro enterprises follow in September 2027.
Applies only: For businesses and transactions within the French electronic invoicing reform; distinguish invoice intake from payment execution.
Source J:FR-EINVOICE-TIMING: Electronic invoicing implementation timetable <https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation>. Checked 2026-11-03. Updated 16 January 2026. Apply only to transactions and businesses within the French reform.

### insurance | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: LI: waiting for decision_approvers, data_privacy, proof. Named source checks: FMA Liechtenstein BankA/WPFG/WPDG framework, ZDG guidelines and DORA FAQs; Datenschutzstelle guidance. Existing notes retain their stated activity scope.; MC: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CCAF Act No. 1.338 and ACPR Monaco banking guidance; Monaco APDP current privacy guidance. Existing notes retain their stated activity scope.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: The manufacturer's responsible body endorses and remains accountable for the written product approval process, including when product design is outsourced.
Applies only: For manufacturers within Regulation 2017/2358; distributor roles are distinct.
Source J:EU-INS-PRODUCT: Delegated Regulation 2017/2358 consolidated 2 August 2022 <https://eur-lex.europa.eu/eli/reg_del/2017/2358/2022-08-02/eng>. Checked 2026-11-03. Applies to insurance product manufacturers and relevant distributors, not every insurance technology supplier.

decision_approvers | scope CH | legal: Swiss insurers define their internal outsourcing signers. Outsourcing significant functions affects the business plan and requires the applicable FINMA authorisation.
Applies only: For insurer outsourcing within Circular 2018/3, with captive exceptions checked.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

sector_regulator | scope DE | legal: Germany: an insurtech carrying on insurance business needs the applicable authorisation under the Versicherungsaufsichtsgesetz. BaFin's guidance ties this to the insurance activity.
Applies only: For conducting insurance business, not merely supplying insurance software.
Source J:DE-INSURANCE: Unterliegen Insurtechs einer Aufsichtspflicht? <https://bafin.de/SharedDocs/FAQs/DE/Fintech/Geschaeftsmodelle/Insurtechs/FAQ_Allgemein/4.html>. Checked 2026-11-03. Publication date not shown. German primary text. Does not make every insurance technology vendor an insurer.

sector_regulator | scope FR | legal: France: ACPR's authorisation routes distinguish insurance undertakings from banking institutions. Confirm the prospect's insurance entity and approved activity.
Applies only: For institutions within ACPR's insurance authorisation remit; do not treat a software supplier as an insurer.
Source J:FR-AUTH: Authorising undertakings <https://acpr.banque-france.fr/en/nos-missions/authorising-undertakings>. Checked 2026-11-03. Publication date not shown. Different routes by regulated activity; not all French finance is supervised solely by ACPR.

sector_regulator | scope AT | legal: Austria: Insurer licensing is governed by Versicherungsaufsichtsgesetz 2016 through FMA, with the appropriate domestic or cross border route.
Applies only: For carrying on insurance business; an intermediary or technology supplier is a different activity.
Source J:AT-INSURANCE: Licence: insurance <https://www.fma.gv.at/en/insurance/licence/>. Checked 2026-11-03. No publication date shown. Check domestic, EEA passport or third country branch route.

sector_regulator | scope BE | legal: Belgium: NBB's insurance and reinsurance authorisation category is separate from payment and stockbroking permissions.
Applies only: For carrying on insurance business; an intermediary or technology supplier is a different activity.
Source J:BE-AUTH: Information on authorisations <https://www.nbb.be/en/financial-oversight/general/authorisation-information>. Checked 2026-11-03. No publication date shown. Does not give NBB every FSMA conduct or investment adviser function.

sector_regulator | scope NL | legal: Netherlands: DNB authorisation or a valid exemption is required for insurer activity under the Wft.
Applies only: For carrying on insurance business; an intermediary or technology supplier is a different activity.
Source J:NL-INSURANCE: Prohibition on operating as an insurer without authorisation <https://www.dnb.nl/en/sector-information/open-book-supervision/open-book-supervision-sectors/insurers/market-access-insurers/prohibition-on-operating-as-an-insurer-without-authorisation/>. Checked 2026-11-03. Not an insurance intermediary licence.

sector_regulator | scope CH | legal: Switzerland: FINMA licenses insurers under the Insurance Supervision Act and approves relevant business plan changes.
Applies only: For carrying on insurance business; an intermediary or technology supplier is a different activity.
Source J:CH-INSURANCE: Licensing in the insurance sector <https://www.finma.ch/en/authorisation/insurers/>. Checked 2026-11-03. No publication date shown. Insurers, not ordinary insurance technology suppliers.

sector_regulator | scope LI | legal: Liechtenstein: Article 11 VersAG requires the FMA licence before a supervised insurer starts business.
Applies only: For carrying on insurance business; an intermediary or technology supplier is a different activity.
Source J:LI-INSURANCE: FMA Instruction 2017/26 Formation of an insurance undertaking <https://www.fma-li.li/files/list/fma-wegleitung-grundung-eines-vu-en-final.pdf>. Checked 2026-11-03. Published 2017-12-29; amended 2024-02-14. Relevant legislation controls individual cases.

sector_regulator | scope LU | legal: Luxembourg: Article 44 of the amended insurance sector law requires prior authorisation through CAA. Article 45 ties the permission to the approved insurance classes.
Applies only: For establishing an insurer or extending its insurance classes, subject to statutory exceptions.
Source J:LU-INS-LAW: Loi du 7 decembre 2015 sur le secteur des assurances consolidated 3 April 2026 <https://www.caa.lu/uploads/documents/files/Loi_SecteurAssurances_2015-12-07_coord_2026-04-03_ESAP_.pdf>. Checked 2026-11-03. CAA informational consolidation; authentic Memorial text prevails. Do not reuse the old Ministerial route from the unamended 2015 text.

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: Insurance processing involving health data needs an applicable GDPR Article 9 condition as well as an Article 6 basis. Check additional national health data conditions.
Applies only: Where underwriting, claims or related processing uses personal health data; ordinary contract necessity alone is insufficient.
Source J:EU-GDPR-LAW: Regulation 2016/679 GDPR <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679>. Checked 2026-11-03. National law can impose additional conditions on health data. A normal contract basis alone does not displace Article 9.

data_privacy | scope CH | legal: Swiss insurer outsourcing must preserve contractual security requirements and supervisory access to information, including when the provider is overseas.
Applies only: For outsourced functions within the circular; separate personal data requirements still apply.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

proof | scope AT,BE,FR,DE,LU,NL | legal: For an EU insurance undertaking, verify authorisation with the relevant national authority. EIOPA states that national registers prevail over conflicting entries in its consolidated register.
Applies only: For insurance undertakings; do not use the same register as proof of an intermediary's permission.
Source J:EU-INSURANCE: Register of Insurance Undertakings <https://register.eiopa.europa.eu/registers/register-of-insurance-undertakings>. Checked 2026-11-03. Publication date not shown. Undertakings and intermediaries differ; national registers prevail.

proof | scope AT,BE,FR,DE,LU,NL | legal: Retain product approval actions for audit, with testing against the target market and corrective action. The target assessment includes relevant sustainability objectives.
Applies only: For product manufacture and significant changes within Articles 4 6 and 9.
Source J:EU-INS-PRODUCT: Delegated Regulation 2017/2358 consolidated 2 August 2022 <https://eur-lex.europa.eu/eli/reg_del/2017/2358/2022-08-02/eng>. Checked 2026-11-03. Applies to insurance product manufacturers and relevant distributors, not every insurance technology supplier.

proof | scope CH | legal: Maintain the insurer outsourcing inventory with business plan form J and the related control and audit evidence.
Applies only: For insurer functions within Circular 2018/3.
Source J:CH-OUTSOURCING: FINMA Circular 2018/3 Outsourcing <https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2018-03-01012021_de.pdf>. Checked 2026-11-03. Current circular index lists November 2020 amendment. The URL suffix is de but the retrieved document is English. Does not cover every portfolio manager or FinTech licence holder.

### customer-service | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### crm-marketing | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### collaboration | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-growth | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### construction | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### property-management | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### field-services | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### fmcg-retail-execution | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### industry-hr-payroll | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### hotel-lodging | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### retail-restaurant-ops | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### agents-copilots | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### voice-language-models | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### enterprise-search | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### it-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### bpo-cx | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-engineering | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### operators-connectivity | specific | inherits telecom
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: operators-connectivity: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

sector_regulator | scope CH | legal: Swiss operator registration depends on using the specified licensed spectrum or nationally managed addressing resources. Establish the operator's actual resource use before treating registration as a prerequisite.
Applies only: For Swiss telecommunications service providers within the Telecommunications Act registration trigger.
Source J:CH-TELECOM: Registration and publication as a TSP <https://www.bakom.admin.ch/en/registration-and-publication-as-a-tsp>. Checked 2026-11-03. Do not confuse Swiss OFCOM with UK Ofcom. Registration scope does not exhaust surveillance or other obligations.

### cpaas-messaging | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### telecom-software | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### business-voice-ucaas | specific | inherits telecom
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: business-voice-ucaas: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope CH | legal: For a Swiss service that supplies public telephony, verify emergency call routing and caller location transfer against the applicable OFCOM technical rules. Establish whether the offering is public telephone service before applying this obligation.
Applies only: Publicly available telephone service; use the edition and routing table valid at implementation.
Source J:CH-EMERGENCY: Emergency call requirement SR 784.101.113/1.3 <https://www.bakom.admin.ch/en/sr-78410111313-emergency-call-requirement>. Checked 2026-11-03. Edition and routing table must be checked for the deployment date. Page publication date not established.

### developer-platform | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-infrastructure | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### observability | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### testing | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### dev-tools | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### cloud-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: cloud-security: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: ENISA suggests demonstrating protected cloud backups and tested recovery across availability zones where the architecture uses them.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### identity-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: identity-security: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Document access policy and risk appropriate authentication for remote, sensitive and privileged access.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first.
Source J:EU-NIS2-IMPLEMENT: Implementing Regulation (EU) 2024/2690 <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690>. Checked 2026-11-03. Relevant essential or important entities only. National scope identification remains necessary. Does not establish Swiss Monaco or Liechtenstein applicability.

### email-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: email-security: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Demonstrate controls against malicious email content and unauthorised software, with user reporting and safe email practices.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first.
Source J:EU-NIS2-IMPLEMENT: Implementing Regulation (EU) 2024/2690 <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690>. Checked 2026-11-03. Relevant essential or important entities only. National scope identification remains necessary. Does not establish Swiss Monaco or Liechtenstein applicability.

### awareness-training | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: awareness-training: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: ENISA evidence examples include role specific training objectives, effectiveness assessments and training after relevant role changes.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: appsec: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Show development security rules covering specification through testing, including outsourced development and protected development environments.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### mobile-appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: mobile-appsec: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: For mobile application deployments, document permitted device use, secure configuration and separation of development from operational systems.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### soc-services | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: soc-services: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Show log review, alarm response, retention decisions and controls against unauthorised log access or alteration.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### endpoint-network | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: endpoint-network: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Limit network connections to operational need; show endpoint execution controls and protection against malicious software.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first.
Source J:EU-NIS2-IMPLEMENT: Implementing Regulation (EU) 2024/2690 <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690>. Checked 2026-11-03. Relevant essential or important entities only. National scope identification remains necessary. Does not establish Swiss Monaco or Liechtenstein applicability.

### document-ai | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### ai-video | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### engineering-talent | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-management | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-adoption | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### pentest | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: pentest: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Record test scope, method, findings and remediation. Choose penetration testing when the risk assessment supports that technique.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first. ENISA examples are guidance.
Source J:EU-ENISA-TECH: NIS2 technical implementation guidance version 1.0 <https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf>. Checked 2026-11-03. Nonbinding examples. Paraphrased from ENISA under CC BY 4.0; examples are not new legal requirements.

### attack-surface-dast | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: attack-surface-dast: check National sector authority and privacy authority for AT BE FR DE LI LU MC NL CH; EU law only where applicability is verified for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for LI, MC, CH. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope AT,BE,FR,DE,LU,NL | operating: Security testing may include vulnerability scanning and dynamic application tests. Select methods by risk and feed findings into control review.
Applies only: For relevant digital entities within Implementing Regulation 2024/2690 in the named EU countries; establish national entity scope first.
Source J:EU-NIS2-IMPLEMENT: Implementing Regulation (EU) 2024/2690 <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690>. Checked 2026-11-03. Relevant essential or important entities only. National scope identification remains necessary. Does not establish Swiss Monaco or Liechtenstein applicability.

### process-orchestration | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### open-source-support | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### iot-connectivity | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

## North America

This draft covers the United States, Canada and Mexico. It is not one legal market. State, province, territory, buyer type and activity must be established where relevant. No US state rule is presented as national, and no US, Canadian or Mexican rule is borrowed by another country. Draft for owner review. Final owner scope permits remaining subtypes to inherit. Specific means a sourced addition for the named country and activity, not complete country coverage. Pending topics retain narrower research gaps.
Countries: US = United States; CA = Canada; MX = Mexico
Clues, only in selling context: {"aliases":["North America"],"countries":[{"code":"US","name":"United States","aliases":["United States","United States of America","USA","U.S."],"cities":["New York","San Francisco","Boston","Chicago","Austin"],"currencies":["USD","US dollar"],"regulators":["Federal Deposit Insurance Corporation","Office of the Comptroller of the Currency","Federal Communications Commission","Securities and Exchange Commission","FinCEN"]},{"code":"CA","name":"Canada","aliases":["Canada"],"cities":["Toronto","Vancouver","Montreal","Ottawa"],"currencies":["CAD","Canadian dollar"],"regulators":["Office of the Superintendent of Financial Institutions","Bank of Canada","Canadian Radio-television and Telecommunications Commission"]},{"code":"MX","name":"Mexico","aliases":["Mexico","México"],"cities":["Mexico City","Ciudad de México","Monterrey","Guadalajara"],"currencies":["MXN","Mexican peso"],"regulators":["Comisión Nacional Bancaria y de Valores","Comisión Nacional de Seguros y Fianzas","Comisión Reguladora de Telecomunicaciones"]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country, state or province and legal entity will buy, and who signs off budget, operational risk and personal data handling?

procurement_payment | scope COMMON | question: What procurement route, invoice currency, tax treatment, acceptance terms and payment schedule has this buyer confirmed?

data_privacy | scope US | operating: United States: the FTC's business guidance recommends documenting the personal data held, restricting access, retaining only what is needed and disposing of it safely. Use that evidence to substantiate security claims.
Applies only: Business security guidance, not a certification or a substitute for state, sector and contractual requirements.
Source J:US-FTC-SECURITY: Start with Security: A Guide for Business <https://www.ftc.gov/business-guidance/resources/start-security-guide-business>. Checked 2026-11-03. Publication date not reliably established. Guidance derived from cases; individual settlement orders do not apply to every business.

data_privacy | scope CA | legal: Canada: under PIPEDA, an organisation remains accountable for personal information sent to a processor and must use contractual or other means to provide comparable protection.
Applies only: For processing within PIPEDA scope. The cited guidance excludes public sector transfers and does not replace provincial rules.
Source J:CA-PIPEDA: Guidelines for processing personal data across borders <https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/>. Checked 2026-11-03. Publication date not reliably established. Does not cover public sector transfers or detailed provincial private sector requirements.

data_privacy | scope CA | legal: Canada: establish the province, sector and data flow before selecting privacy requirements. PIPEDA and provincial laws can govern different parts of the same operation.
Applies only: Private sector commercial processing; do not present one province's law as the rule for all of Canada.
Source J:CA-PROVINCES: Provincial laws that may apply instead of PIPEDA <https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/r_o_p/prov-pipeda>. Checked 2026-11-03. Publication date not reliably established. Sector, province and data flow determine applicable law.

data_privacy | scope MX | legal: Mexico: use the Ley Federal de Protección de Datos Personales en Posesión de los Particulares to establish the responsible party and processor roles. The law designates Secretaría Anticorrupción y Buen Gobierno as the Secretaría.
Applies only: For private sector processing within the law, after checking its exclusions; public sector processing has a different instrument.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

buyer_language | scope COMMON | question: Which language does the buying team require for the contract, implementation, evidence and support?

proof | scope COMMON | question: Which local workflow and buyer approved acceptance test will show that the proposed outcome is achievable?

objections | scope COMMON | question: Which unresolved approval requirement is most likely to block the purchase, and who can validate the evidence?

sales_motion | scope COMMON | question: Who owns the pilot, its success criteria and the decision to fund the next stage in each market?

### logistics-tech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope MX | legal: Mexico: NOM-087-SCT-2-2017 addresses driving and break times for drivers in federal motor transport services. Confirm that the operator's service is within this scope.
Applies only: For covered federal motor transport services; do not import US or Canadian hours rules.
Source J:MX-ROAD: NOM-087-SCT-2-2017 <https://platiica.economia.gob.mx/normalizacion/nom-087-sct-2-2017/>. Checked 2026-11-03. Catalogue supports identity and scope, not detailed timing claims. Verify the operator's covered activity.

proof | scope US | legal: United States: for operations covered by 49 CFR Part 395, demonstrate the driver's duty record and electronic logging workflow, including the applicable exceptions.
Applies only: For covered US motor carrier operations. Software supply alone does not make the supplier a motor carrier.
Source J:US-ELD: General Information about the ELD Rule <https://www.fmcsa.dot.gov/hours-service/elds/general-information-about-eld-rule>. Checked 2026-11-03. Publication date not shown. Applies to covered US operations, including certain foreign domiciled drivers, not all fleet software.

proof | scope CA | legal: Canada: for a covered federal motor carrier operation, verify the electronic logging device against the Commercial Vehicle Drivers Hours of Service Regulations and Transport Canada's certification requirement.
Applies only: For federally regulated operations after checking exemptions; US compliance alone does not establish Canadian compliance.
Source J:CA-ELD: Electronic logging devices for commercial drivers and motor carriers <https://tc.canada.ca/en/road-transportation/electronic-logging-devices/electronic-logging-devices-commercial-drivers-motor-carriers>. Checked 2026-11-03. Publication date not shown. Federal scope and listed exemptions matter; US compliance alone is not sufficient.

### fintech | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

decision_approvers | scope CA | legal: Canada: OSFI Guideline B-10 leaves accountability with the federally regulated financial institution. Identify its third party risk owner and match evidence to the arrangement's risk and criticality.
Applies only: Only for federally regulated financial institutions and covered branches, not every provincial financial business.
Source J:CA-OSFI-B10: Third Party Risk Management Guideline B-10 <https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline>. Checked 2026-11-03. Guidance scope is federally regulated institutions and relevant branches, not every Canadian fintech or provincial insurer.

sector_regulator | scope MX | legal: Mexico: the Ley para Regular las Instituciones de Tecnología Financiera distinguishes collective financing institutions and electronic payment fund institutions. Confirm the actual activity before selecting the CNBV authorisation route.
Applies only: For the designated financial institutions and activities covered by the law; a fintech label does not put every software supplier in scope.
Source J:MX-FINTECH: Instituciones de Tecnología Financiera <https://www.gob.mx/cnbv/acciones-y-programas/instituciones-de-tecnologia-financiera>. Checked 2026-11-03. Publication date not reliably captured. Scope is designated financial institutions, not all businesses described as fintech.

procurement_payment | scope US | legal: United States: align a bank buyer's evidence review with the OCC, Federal Reserve and FDIC Interagency Guidance on Third Party Relationships. Prepare for due diligence, contract review, monitoring and exit planning.
Applies only: For banking organisations supervised by the issuing agencies; expectations depend on the arrangement's risk and complexity.
Source J:US-BANK-THIRDPARTY: Interagency Guidance on Third Party Relationships: Risk Management <https://www.fdic.gov/news/financial-institution-letters/2023/fil23029.html>. Checked 2026-11-03. Supervisory guidance, not a new licence or a universal checklist for every nonbank.

### vertical-saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope CA | legal: Canada: PIPEDA safeguards depend on data sensitivity, amount, use and risk. Health or financial workflows need stronger protection appropriate to that assessment.
Applies only: Where PIPEDA governs; provincial health and private sector laws are not replaced.
Source J:CA-SAFEGUARDS: PIPEDA Principle 7 Safeguards <https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/principles/p_safeguards>. Checked 2026-11-03. PIPEDA scope only; no mandated product.

data_privacy | scope MX | legal: Mexico: Article 18 requires safeguards reflecting risk and data sensitivity. Assess the actual industry records rather than assume one security level for all sectors.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

### ai-native | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope CA | operating: Canada: OPC AI guidance calls for legal authority, transparency, explainability, privacy safeguards and limits on personal information sharing.
Applies only: Guidance for applicable Canadian privacy law, not a separate AI licensing regime.
Source J:CA-AI-PRIVACY: AI privacy and your business <https://www.priv.gc.ca/en/privacy-topics/technology/artificial-intelligence/ai_business/>. Checked 2026-11-03. Guidance, not AI licence; provincial scope requires checking.

data_privacy | scope MX | legal: Mexico: when model inputs or outputs contain personal data, the 2025 law governs roles, security and confidentiality. An AI label does not establish an exemption.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

proof | scope US | operating: United States: if the buyer uses the NIST AI Risk Management Framework, organise evidence around the risks of the actual use case. NIST describes the framework as voluntary.
Applies only: Use only as an agreed assurance framework; do not represent it as a general legal approval or claim it is uniquely applicable to the US.
Source J:US-AI-RMF: AI Risk Management Framework <https://www.nist.gov/itl/ai-risk-management-framework>. Checked 2026-11-03. Webpage publication date not established. Framework release date 2023-01-26. Not a general legal mandate.

### ites | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope MX | legal: Mexico: Article 20 confidentiality controls cover people involved in processing and continue after the relationship ends. Address service staff and support access.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

proof | scope US | operating: United States: FTC guidance recommends capable service providers, written security requirements and verification during outsourced information handling.
Applies only: Business guidance; sector and state obligations need separate scope checks.
Source J:US-FTC-SUPPLIERS: Start with Security <https://www.ftc.gov/business-guidance/resources/start-security-guide-business>. Checked 2026-11-03. Guidance from enforcement cases, not universal certification.

proof | scope CA | legal: Canada: demonstrate how outsourced access and processing maintain comparable protection under the PIPEDA organisation's accountability.
Applies only: For PIPEDA processing; establish province, sector and data flows.
Source J:CA-PIPEDA: Guidelines for processing personal data across borders <https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/>. Checked 2026-11-03. Publication date not reliably established. Does not cover public sector transfers or detailed provincial private sector requirements.

### telecom | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

sector_regulator | scope CA | legal: Canada: CRTC registration and the relevant provider obligations depend on the telecommunications service supplied. The CRTC lists specific reseller exemptions; an exemption from registration does not remove all consumer duties.
Applies only: For Canadian telecommunications provision; establish provider type, services and exemptions before assigning obligations.
Source J:CA-TELECOM: Responsibilities and Regulatory Obligations for Non Facilities Based Providers <https://crtc.gc.ca/eng/comm/telecom/respnon.htm>. Checked 2026-11-03. Publication date not shown. Registration exemptions do not remove all consumer protections.

sector_regulator | scope US | legal: United States: a covered interconnected voice service must be assessed against the FCC E911 requirements in 47 CFR 9.11. Establish the service classification and geographic scope first.
Applies only: Only for interconnected VoIP services and calls within the rule's scope; do not extend this to all communications software.
Source J:US-E911: 47 CFR 9.11 E911 Service <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-9/subpart-D/section-9.11>. Checked 2026-11-03. Publication date omitted for continuously updated code; latest amendment shown 2026-01-14. Geographic service conditions and fixed versus nonfixed service matter.

proof | scope MX | legal: Mexico: verify the operator's service, territory and authorisation validity in the Comisión Reguladora de Telecomunicaciones public concessions register.
Applies only: For a relevant concession, permit or authorisation; registry verification does not establish that every telecom software vendor needs one.
Source J:MX-TELECOM: Registro Público de Concesiones <https://rpc.crt.gob.mx/vrpc>. Checked 2026-11-03. Publication date not shown. Registry supports verification, not a general conclusion that every telecom software supplier needs a concession.

### cybersecurity | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope MX | legal: Mexico: Articles 18 and 19 cover risk based safeguards and notice of breaches significantly affecting individuals. Link response evidence to the controller's duties.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

proof | scope US | operating: United States: ask whether the buyer's contract requires the NIST Cybersecurity Framework. NIST says most organisations use it voluntarily; the framework is not itself a regulatory certification.
Applies only: A government or contractual requirement needs its own scope check; do not infer a universal mandate.
Source J:US-CSF: Frequently Asked Questions about the Cybersecurity Framework <https://www.nist.gov/cyberframework/faqs>. Checked 2026-11-03. Publication date not shown. NIST is not a regulatory agency; individual obligations need separate evidence.

proof | scope CA | operating: Canada: the Canadian Centre for Cyber Security's baseline guidance recommends a written incident plan with named responsibilities. Show the buyer how the proposed service fits its response process.
Applies only: Recommended baseline guidance for small and medium organisations; confirm suitability for the buyer's risk rather than asserting certification.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### software | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope MX | legal: Mexico: Article 18 requires administrative, technical and physical safeguards. Demonstrate application protection against unauthorised use, alteration and loss.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

proof | scope US | operating: United States: NIST SSDF 1.1 supports producer and buyer assurance for secure development, software protection and vulnerability response.
Applies only: Recommended framework unless the applicable contract or rule requires it; draft 1.2 is not final.
Source J:US-SSDF: NIST SP 800-218 SSDF 1.1 <https://csrc.nist.gov/pubs/sp/800/218/final>. Checked 2026-11-03. 1.1 remains final; 1.2 is draft. Contract mandate needs separate evidence.

proof | scope CA | operating: Canada: Cyber Centre joint software guidance recommends evidence of secure design, build protection, maintenance and customer communication.
Applies only: Recommended assurance, not universal statutory certification.
Source J:CA-SOFTWARE-CODE: Joint software security code guidance <https://www.cyber.gc.ca/en/news-events/joint-guidance-software-security-code-practice>. Checked 2026-11-03. Recommended practice, not universal certification.

### saas | specific | inherits defaults
Country scoped vertical context supplements the defaults. Apply only notes for the named country and activity.

data_privacy | scope CA | legal: Canada: hosted personal data within PIPEDA requires comparable protection through contractual or other means while the customer retains accountability.
Applies only: PIPEDA scope only; provincial and public sector requirements can differ.
Source J:CA-PIPEDA: Guidelines for processing personal data across borders <https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/>. Checked 2026-11-03. Publication date not reliably established. Does not cover public sector transfers or detailed provincial private sector requirements.

data_privacy | scope MX | legal: Mexico: establish hosted service controller and processor roles under the 2025 private sector data law; security controls must reflect the data and risk.
Applies only: For private sector personal data within the current LFPDPPP, not public sector processing or an AI specific licence.
Source J:MX-DATA-SECURITY: Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>. Checked 2026-11-03. 2025 replacement private sector law, not repealed article numbering.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

proof | scope US | operating: United States: FTC guidance recommends testing privacy and security features, written provider security expectations and ongoing oversight.
Applies only: Business security guidance for the hosted service, not universal certification.
Source J:US-FTC-SUPPLIERS: Start with Security <https://www.ftc.gov/business-guidance/resources/start-security-guide-business>. Checked 2026-11-03. Guidance from enforcement cases, not universal certification.

### freight-visibility | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### freight-marketplace | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### seller-shipping | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### last-mile | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### warehousing | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### transport-management | inherited | inherits logistics-tech
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### payments-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for decision_approvers, data_privacy, proof. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for sector_regulator, decision_approvers, data_privacy. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for decision_approvers, data_privacy, proof. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

sector_regulator | scope US | legal: United States: determine whether the actual funds activity makes the entity a money services business under 31 CFR Chapter X. FinCEN registration has exceptions, including a person acting solely as another MSB's agent.
Applies only: For federal MSB registration scope; this does not settle state licensing, bank charter or other obligations.
Source J:US-FINCEN: Money Services Business Registration <https://www.fincen.gov/resources/money-services-business-msb-registration>. Checked 2026-11-03. Publication date not shown. Federal registration is not a determination of state licensing or banking authority.

sector_regulator | scope MX | legal: Mexico: an institution issuing, administering, redeeming or transmitting electronic payment funds can fall within the CNBV electronic payment fund institution category under the Ley para Regular las Instituciones de Tecnología Financiera.
Applies only: Only where the actual activity matches the statutory category; an API or accounting feature alone is insufficient.
Source J:MX-FINTECH: Instituciones de Tecnología Financiera <https://www.gob.mx/cnbv/acciones-y-programas/instituciones-de-tecnologia-financiera>. Checked 2026-11-03. Publication date not reliably captured. Scope is designated financial institutions, not all businesses described as fintech.

proof | scope CA | legal: Canada: a payment service provider within the Retail Payment Activities Act needs the applicable operational risk, incident response and end user funds safeguards. Show how the buyer's framework handles the proposed service.
Applies only: For payment activities and providers within RPAA scope; determine whether funds are held and check exclusions.
Source J:CA-RPAA: Retail payments supervisory framework <https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/>. Checked 2026-11-03. Publication date not shown. Apply only to payment service providers and activities in scope; check exclusions and funds handling.

### core-banking | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for sector_regulator, decision_approvers, data_privacy. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for sector_regulator, decision_approvers, data_privacy. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for decision_approvers, data_privacy, proof. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

sector_regulator | scope MX | legal: Mexico: commercial bank authorisation under the Ley de Instituciones de Credito is granted through CNBV after its board agreement and a favourable Banco de Mexico opinion.
Applies only: For organising and operating the bank, not licensing its core platform supplier.
Source J:MX-BANK: Banks <https://www.cnbv.gob.mx/en/Supervised-Entities/Banks/Paginas/Banks.aspx>. Checked 2026-11-03. Official search text read; direct fetch timed out. CNBV authorisation requires board agreement and favourable Banco de Mexico opinion.

proof | scope US | legal: United States: a bank's use of a third party does not remove its responsibility for safe operations and applicable law. Provide control and monitoring evidence for the bank's chosen supervisory review.
Applies only: For a supervised bank relationship; a core banking platform supplier does not inherit the bank's charter.
Source J:US-BANK-THIRDPARTY: Interagency Guidance on Third Party Relationships: Risk Management <https://www.fdic.gov/news/financial-institution-letters/2023/fil23029.html>. Checked 2026-11-03. Supervisory guidance, not a new licence or a universal checklist for every nonbank.

proof | scope CA | legal: Canada: OSFI B-10 applies proportionate oversight to a federally regulated institution's third party arrangement. Agree the criticality and continuity evidence with the institution.
Applies only: For institutions within B-10 scope; do not assume provincial institutions have the same supervisory route.
Source J:CA-OSFI-B10: Third Party Risk Management Guideline B-10 <https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline>. Checked 2026-11-03. Guidance scope is federally regulated institutions and relevant branches, not every Canadian fintech or provincial insurer.

### lending | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for sector_regulator, decision_approvers, data_privacy. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

proof | scope US | legal: United States: under ECOA Regulation B, 12 CFR 1002.9, required adverse action reasons must identify the principal factors actually used. Demonstrate the explanation workflow for the creditor's applicable notice route.
Applies only: For covered credit decisions and notices; check business credit, incomplete application and other exceptions rather than applying one notice process to every loan.
Source J:US-REG-B: 12 CFR 1002.9 Notifications <https://www.consumerfinance.gov/rules-policy/regulations/1002/9/>. Checked 2026-11-03. No standalone publication date shown. Direct rule used instead of relying on an older circular. Business credit and other notification exceptions must be checked.

### wealth-investment | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for decision_approvers, data_privacy, proof. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for decision_approvers, data_privacy, proof. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for decision_approvers, data_privacy. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

sector_regulator | scope US | legal: United States: an investment adviser may be registered with the SEC or one or more state securities authorities. Verify the entity's actual registration and applicable exceptions before assigning an approval route.
Applies only: Investment adviser registration only; not the registration regime for every broker, fund or software supplier.
Source J:US-ADVISERS: Investment Adviser Registration <https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/investment-advisers-0>. Checked 2026-11-03. Publication date not shown. Investment advisers differ from brokers and other financial intermediaries.

sector_regulator | scope CA | legal: Canada: National Instrument 31-103 and related rules govern dealer and adviser registration through provincial and territorial securities authorities. Verify the category, permitted activity and exemptions.
Applies only: For covered securities businesses; the national search does not create a federal securities licence.
Source J:CA-SECURITIES: Registration Information <https://www.securities-administrators.ca/industry-resources/registration-information/>. Checked 2026-11-03. Publication date not shown. Check exemptions, registration category and principal regulator; not a federal securities licence.

sector_regulator | scope MX | legal: Mexico: Article 225 of the Ley del Mercado de Valores requires registration of covered investment advisers with CNBV.
Applies only: For habitual professional portfolio administration or individualised investment advice within the statutory category.
Source J:MX-ADVISER: Preguntas Frecuentes: Asesores en Inversiones <https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/ASESORES_EN_INVERSIONES/Paginas/PreguntasFrecuentes.aspx>. Checked 2026-11-03. Official search text read; direct fetch returned 502. Covers registered investment advisers rather than every wealth platform.

proof | scope MX | legal: Mexico: demonstrate that adviser orders remain documented in the client's name and that the adviser workflow does not take prohibited custody of client money or securities.
Applies only: For registered investment adviser activities; permitted remuneration is distinct from custody.
Source J:MX-ADVISER: Preguntas Frecuentes: Asesores en Inversiones <https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/ASESORES_EN_INVERSIONES/Paginas/PreguntasFrecuentes.aspx>. Checked 2026-11-03. Official search text read; direct fetch returned 502. Covers registered investment advisers rather than every wealth platform.

### spend-expense | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for decision_approvers, data_privacy, proof. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for sector_regulator, decision_approvers, data_privacy, proof. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

sector_regulator | scope CA | legal: Canada: assess any actual retail payment function in an expense product against the Retail Payment Activities Act before promising a payment service.
Applies only: Only if the service performs covered payment functions; expense record keeping alone does not establish RPAA scope.
Source J:CA-RPAA: Retail payments supervisory framework <https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/>. Checked 2026-11-03. Publication date not shown. Apply only to payment service providers and activities in scope; check exclusions and funds handling.

### insurance | specific | inherits fintech
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: US: waiting for decision_approvers, data_privacy, proof. Named source checks: FinCEN MSB rules, OCC bank charter guidance, SEC adviser rules and the named applicable state regulator; FTC Safeguards Rule. Existing notes retain their stated activity scope.; CA: waiting for decision_approvers, data_privacy, proof. Named source checks: Bank of Canada RPAA guidance, OSFI bank and insurer guidance, CSA NI 31-103 as locally adopted and OPC PIPEDA guidance. Existing notes retain their stated activity scope.; MX: waiting for decision_approvers, data_privacy, proof. Named source checks: CNBV ITF and bank authorisation rules, CNBV investment adviser rules, CNSF insurance rules, SAT CFDI guidance and current DOF private sector data law. Existing notes retain their stated activity scope.

sector_regulator | scope US | legal: United States: insurance regulation is primarily state based. NAIC supports state regulators but does not issue licences, and a model law is not automatically law in any state.
Applies only: Identify the relevant state and adopted instrument before attaching a specific insurance or cyber obligation.
Source J:US-INSURANCE: Understanding the NAIC: Governance and Accountability <https://content.naic.org/about/understanding-naic-governance-accountability>. Checked 2026-11-03. Publication date not shown. NAIC is a regulatory support body, not a licensing regulator. Check state enactments separately.

sector_regulator | scope MX | legal: Mexico: establishing an insurance institution requires the corresponding CNSF authorisation. Keep this approval route separate from CNBV fintech authorisation.
Applies only: For establishing an insurance institution; not every insurance intermediary or technology supplier.
Source J:MX-INSURANCE: Autorización para constituir, organizar y funcionar como Institución de Seguros <https://www.gob.mx/cnsf/acciones-y-programas/autorizacion-para-constituir-organizar-y-funcionar-como-institucion-de-seguros>. Checked 2026-11-03. Applies to establishing an insurance institution, not every intermediary or software supplier.

sector_regulator | scope CA | legal: Canada: federally incorporated insurers use the Insurance Companies Act route, with Ministerial incorporation and a separate Superintendent order to commence business.
Applies only: Federal incorporation only. Provincial insurance permissions and foreign branch routes require separate checks.
Source J:CA-INSURANCE-INC: Guide for Incorporating Federally Regulated Insurance Companies <https://www.osfi-bsif.gc.ca/en/data-forms/applications-approvals/transaction-instructions/guide-incorporating-federally-regulated-insurance-companies>. Checked 2026-11-03. Guide revised May 2013 and describes expectations at 2012 year end. Current Act index separately checked through 2026-09-30. No provincial requirements inferred.

buyer_language | scope MX | legal: Mexico: the CNSF insurance institution application requires the specified documents in Spanish. Prepare the approval evidence in the required language.
Applies only: Only for that authorisation application; this does not establish the language preference of every private buyer.
Source J:MX-INSURANCE: Autorización para constituir, organizar y funcionar como Institución de Seguros <https://www.gob.mx/cnsf/acciones-y-programas/autorizacion-para-constituir-organizar-y-funcionar-como-institucion-de-seguros>. Checked 2026-11-03. Applies to establishing an insurance institution, not every intermediary or software supplier.

### customer-service | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### crm-marketing | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### collaboration | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-growth | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### construction | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### property-management | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### field-services | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### fmcg-retail-execution | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### industry-hr-payroll | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### hotel-lodging | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### retail-restaurant-ops | inherited | inherits vertical-saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### agents-copilots | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### voice-language-models | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### enterprise-search | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### it-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### bpo-cx | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-engineering | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-services | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### operators-connectivity | specific | inherits telecom
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: operators-connectivity: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.

proof | scope CA | legal: A Canadian registration application identifies the provider's services, response manager and facilities status. Facilities based applicants include network and interconnection diagrams; verify the applicable category and exemptions first.
Applies only: For providers required to register with the CRTC; not a licence imposed on a software only vendor.
Source J:CA-TELECOM-REGISTER: Register as a telecommunications provider: application <https://crtc.gc.ca/eng/comm/telecom/registr4.htm>. Checked 2026-11-03. Check exemption criteria and registration category first. Publication date not established.

### cpaas-messaging | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### telecom-software | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### business-voice-ucaas | specific | inherits telecom
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: business-voice-ucaas: country specific source check incomplete for CA, MX. Check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation. Existing scoped notes remain valid only for their stated countries.

proof | scope US | legal: United States: for a covered interconnected VoIP service, test emergency routing, location handling and the required subscriber notice of service limitations under 47 CFR 9.11.
Applies only: Match fixed or nonfixed service requirements and the rule's geographic conditions.
Source J:US-E911: 47 CFR 9.11 E911 Service <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-9/subpart-D/section-9.11>. Checked 2026-11-03. Publication date omitted for continuously updated code; latest amendment shown 2026-01-14. Geographic service conditions and fixed versus nonfixed service matter.

### developer-platform | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### data-infrastructure | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### observability | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### testing | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### dev-tools | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### cloud-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: cloud-security: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Assess cloud data location, deletion and administrator access; demonstrate protected connections and separate administrative credentials.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### identity-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: identity-security: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Use least privilege, individual accounts and prompt removal of obsolete access; demonstrate authentication controls for privileged accounts.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### email-security | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: email-security: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Show email filtering and DMARC implementation, including how malicious links and attachments are handled.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### awareness-training | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: awareness-training: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Cover malicious emails, password practice, approved applications and safe online behaviour in employee training.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: appsec: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for CA, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope US | operating: Map secure development evidence to the SSDF lifecycle, including protected development work, security testing and vulnerability response. Confirm which practices the buyer's contract actually requires.
Applies only: NIST SSDF 1.1 guidance; not an automatic obligation for every US software supplier.
Source J:US-SSDF: NIST SP 800-218 SSDF 1.1 <https://csrc.nist.gov/pubs/sp/800/218/final>. Checked 2026-11-03. 1.1 remains final; 1.2 is draft. Contract mandate needs separate evidence.

### mobile-appsec | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: mobile-appsec: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Show separation of work and personal app data, encrypted sensitive storage and trusted application sources.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### soc-services | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: soc-services: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Document who handles incidents and how external responders are engaged; connect detection to the response plan.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### endpoint-network | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: endpoint-network: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for US, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope CA | operating: Show malware protection, firewall controls and separation between guest access and the corporate network.
Applies only: Voluntary Canadian guidance for smaller organisations.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### document-ai | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### ai-video | inherited | inherits ai-native
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### engineering-talent | inherited | inherits ites
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### product-management | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### digital-adoption | inherited | inherits saas
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### pentest | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: pentest: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for CA, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope US | operating: Agree assessment scope and authorised methods, document findings and plan mitigation. NIST SP 800-115 describes the benefits and limitations of testing techniques rather than certifying a product.
Applies only: Technical testing guidance; establish contractual and system owner authorisation separately.
Source J:US-SECURITY-TEST: NIST SP 800-115 Technical Guide to Information Security Testing and Assessment <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf>. Checked 2026-11-03. Final technical guidance, not a universal statutory requirement or product certification.

### attack-surface-dast | specific | inherits cybersecurity
Country and activity scoped additions supplement the vertical. Other countries use applicable vertical notes. Specific status does not assert complete country depth.
Waiting for a source: attack-surface-dast: check US federal and applicable state regulator; Canadian federal and applicable provincial regulator; Mexican sector authority and current legislation for country specific obligations, approval roles and evidence. No sourced finding of equivalence is recorded.; No separately sourced subtype addition in this bounded pass for CA, MX. Applicable vertical notes remain available; do not apply the other country's guidance.

proof | scope US | operating: Use vulnerability scanning within a planned assessment. Review findings and technique limitations before treating a scan as evidence of effective security.
Applies only: NIST testing guidance; scan coverage alone is not a comprehensive assurance programme.
Source J:US-SECURITY-TEST: NIST SP 800-115 Technical Guide to Information Security Testing and Assessment <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf>. Checked 2026-11-03. Final technical guidance, not a universal statutory requirement or product certification.

### process-orchestration | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### open-source-support | inherited | inherits software
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.

### iot-connectivity | inherited | inherits telecom
Uses the applicable vertical notes. No separate subtype research completed in this owner approved bounded pass; no equivalence claim is made.
