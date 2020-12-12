"""Test file for search File"""
from unittest import TestCase

from rawsec_cli.search import searchProject
from rawsec_cli.search import searchProjectCTF
from rawsec_cli.search import searchProjectOperating
from rawsec_cli.search import searchProjectResources
from rawsec_cli.search import searchProjectTools


class TestSearch(TestCase):
    """Test search class"""
    def setUp(self):
        """setup test"""
        self.json = {
            "tools": {"binary_exploitation": {"tools": [{"name": "tools"}]}},
            "resources": {
                "binary_exploitation": {"resources": [{"name": "resources"}]},
            },
            "operating_systems": {
                "binary_exploitation": {
                    "operating_systems": [{"os": "operating_systems"}],
                },
            },
            "ctf_platforms": {
                "binary_exploitation": {
                    "ctf_platforms": [{"name": "ctf_platforms"}],
                },
            },
        }

    def testSearchProjectTools(self):
        """test searchProjectTools function"""
        self.assertEqual(
            searchProjectTools(self.json, "tools"),
            [{"name": "tools"}],
        )

    def testSearchProjectResources(self):
        """test searchProjectResources function"""
        self.assertEqual(
            searchProjectResources(self.json, "resources"),
            [{"name": "resources"}],
        )

    def testSearchProjectCTF(self):
        """test searchProjectCTF function"""
        self.assertEqual(
            searchProjectCTF(self.json, "ctf_platforms"),
            [{"name": "ctf_platforms"}],
        )

    def testSearchProjectOperating(self):
        """test searchProjectOperating function"""
        self.assertEqual(
            searchProjectOperating(self.json, "operating_systems"),
            [{"os": "operating_systems"}],
        )

    def testSearchProject(self):
        """test searchProject function"""
        self.assertEqual(
            searchProject(self.json, "tools"),
            [{"name": "tools"}],
        )
