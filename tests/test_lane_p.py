import unittest,json,hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'tests/lane-p-inventory.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
header=lambda s:re.match(r'\ufeff?---\r?\n.*?\r?\n---(?:\r?\n|$)',s,re.S)[0]
class PluginRegressions(unittest.TestCase):
 def test_frozen_metadata_and_real_payload_hashes(self):
  for row in DATA['skills']:
   raw=(ROOT/row['path']).read_bytes();s=raw.decode();self.assertEqual(sha(header(s).encode()),row['frontmatter_sha256'],row['path']);self.assertEqual(sha(raw.replace(b'\r\n',b'\n')),row['after_sha256'],row['path'])
 def test_P0_country_product_binding_and_M075_source_scope(self):
  for row in DATA['skills']:
   p=ROOT/row['path'];ref=p.parent/'references/region-context.md';raw=ref.read_bytes();self.assertEqual(sha(raw),row['reference_sha256']);s=raw.decode();self.assertIn('Bind each country to the affirmative seller offering',s);self.assertIn('Transaction denomination',s);self.assertNotIn('where the insurer or takaful operator relies on customer consent',s);self.assertIn('Part B, paragraphs 2.1, 5.2 and 10.6',s)
 def test_M096_explicit_reference_dependencies_exist(self):
  for row in DATA['skills']:
   p=ROOT/row['path'];s=p.read_bytes().decode();self.assertNotIn('scoring methodology.md',s)
   for name in set(re.findall(r'references/[A-Za-z0-9_./-]+\.md',s)):
    self.assertTrue(any((parent/name).exists() for parent in [p.parent,*p.parent.parents] if parent==ROOT or ROOT in parent.parents),str(p)+': '+name)
 def test_M031_country_and_route_are_explicit(self):
  for row in DATA['skills']:
   if 'eu-trust-centre' not in row['path']:continue
   s=(ROOT/row['path']).read_bytes().decode();self.assertNotIn('Health-tech adds BfArM/DiGA as Q8-adjacent',s);self.assertIn('confirmed Germany digital health application',s);self.assertIn('statutory reimbursement route',s)
 def test_M032_no_default_market_or_EU_cluster_superlative(self):
  for row in DATA['skills']:
   if 'prompt-pack-builder' not in row['path']:continue
   s=(ROOT/row['path']).read_bytes().decode();self.assertNotIn('Default markets: DACH + Nordics',s);self.assertNotIn('default to Germany only',s);self.assertNotIn('most rigorous GDPR market',s);self.assertNotIn('highest EU AI adoption',s);self.assertIn('Switzerland is not an EU member',s);self.assertIn('Norway is not an EU member',s)
 def test_M058_no_unsupported_country_bonuses(self):
  for row in DATA['skills']:
   if not any(x in row['path'] for x in ['gtm-motion-picker','epic-motion-diagnostic']):continue
   s=(ROOT/row['path']).read_bytes().decode();self.assertNotRegex(s,r'(?:India B2B|Middle East): E \+[12]')
 def test_M091_no_predictive_output_from_signals(self):
  for row in DATA['skills']:
   if not any(x in row['path'] for x in ['renewal-save-plan','guard-defend-renewal']):continue
   s=(ROOT/row['path']).read_bytes().decode();body=s[len(header(s)):];self.assertIn('No generated renewal probability or GRR forecast',body);self.assertNotIn('Renewal Probability: [X]%',body)
 def test_M094_connector_body_matches_registered_names(self):
  for row in DATA['skills']:
   s=(ROOT/row['path']).read_bytes().decode();body=s[len(header(s)):]
   if row['path'].endswith('helix-mcp-gtm-alpha/SKILL.md'):
    for name in DATA['tools']['alpha']:self.assertIn(name,body)
    self.assertNotIn('epic_quick_score',body);self.assertNotIn('epic_gtm_audit',body);self.assertIn('30, 60 or 90',body)
   if row['path'].endswith('helix-mcp-revenue-enablement/SKILL.md'):
    for name in DATA['tools']['revenue']:self.assertIn(name,body)
 def test_M104_no_prescriptive_software_stack(self):
  for row in DATA['skills']:
   if row['repo'] not in ['content-writing-thought-leadership','newsletter-creation-curation','social-media-management','b2b-sales-enablement']:continue
   if row['repo']=='b2b-sales-enablement' and 'sales-proposal-builder' not in row['path']:continue
   s=(ROOT/row['path']).read_bytes().decode();body=s[len(header(s)):]
   if any(x in row['path'] for x in ['sales-proposal-builder','SKILL.md']):
    self.assertNotRegex(body,r'(?i)(?:Tools:|Use |Option 1:|Best for growth)[^\n]*(?:Canva|Figma|Taplio|Shield|ConvertKit)');self.assertIn('https://calendly.com/shashwat-gtmhelix/45min',body)
if __name__=='__main__':unittest.main()
