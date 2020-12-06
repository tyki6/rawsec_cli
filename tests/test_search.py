from unittest import TestCase

from rawsec_cli.search import searchProjectTools, searchProjectOperating, searchProjectCTF, searchProjectResources, \
    searchProject


class TestSearch(TestCase):
    def setUp(self):
        self.json = {
            "tools": {"binary_exploitation": {"tools": [{"name": "tools"}]}},
            "resources": {"binary_exploitation": {"resources": [{"name": "resources"}]}},
            "operating_systems": {"binary_exploitation": {"operating_systems": [{"os": "operating_systems"}]}},
            "ctf_platforms": {"binary_exploitation": {"ctf_platforms": [{"name": "ctf_platforms"}]}}
        }

    def testSearchProjectTools(self):
        self.assertEqual(searchProjectTools(self.json, "tools"), [{"name": "tools"}])

    def testSearchProjectResources(self):
        self.assertEqual(searchProjectResources(self.json, "resources"), [{"name": "resources"}])

    def testSearchProjectCTF(self):
        self.assertEqual(searchProjectCTF(self.json, "ctf_platforms"), [{"name": "ctf_platforms"}])

    def testSearchProjectOperating(self):
        self.assertEqual(searchProjectOperating(self.json, "operating_systems"), [{"os": "operating_systems"}])

    def testSearchProject(self):
        self.assertEqual(searchProject(self.json, "tools"), [{"name": "tools"}])