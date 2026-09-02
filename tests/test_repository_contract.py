import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_manifest_has_bootstrap_files(self):
        manifest = json.loads((ROOT / "PROCESS_MANIFEST.json").read_text())
        for relative in manifest["bootstrap_order"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_has_required_safety_terms(self):
        skill = (ROOT / "skills/integrations/maton-operations/SKILL.md").read_text()
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("MATON_API_KEY", skill)
        self.assertIn("aprovação explícita", skill)
        self.assertIn("Não mostre", skill)
        self.assertIn("não pedir ID antes", skill)

    def test_inventory_is_read_only(self):
        script = (ROOT / "skills/integrations/maton-operations/scripts/inventory_maton.py").read_text()
        self.assertIn('fetch("/connections")', script)
        self.assertIn('fetch("/triggers")', script)
        self.assertNotIn('Request(BASE_URL + path, data=', script)


if __name__ == "__main__":
    unittest.main()
