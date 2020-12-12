"""Test file for tools File"""
from unittest import TestCase

import requests_mock

from rawsec_cli.tools import getAllCTF
from rawsec_cli.tools import getAllOperating
from rawsec_cli.tools import getAllResources
from rawsec_cli.tools import getAllTools
from rawsec_cli.tools import getCTFByCategory
from rawsec_cli.tools import getCTFCategory
from rawsec_cli.tools import getCTFJson
from rawsec_cli.tools import getOperatingByCategory
from rawsec_cli.tools import getOperatingCategory
from rawsec_cli.tools import getOperatingJson
from rawsec_cli.tools import getResourcesByCategory
from rawsec_cli.tools import getResourcesCategory
from rawsec_cli.tools import getResourcesJson
from rawsec_cli.tools import getToolsByCategory
from rawsec_cli.tools import getToolsCategory
from rawsec_cli.tools import getToolsJson
from rawsec_cli.tools import loadInventoryJson


class TestTools(TestCase):
    """Test tools class"""

    def setUp(self):
        """setup test"""
        self.json = {
            "tools": {"binary_exploitation": {"tools": [{"name": "test"}]}},
            "resources": {
                "binary_exploitation": {"resources": [{"name": "test"}]},
            },
            "operating_systems": {
                "binary_exploitation": {
                    "operating_systems": [{"name": "test"}],
                },
            },
            "ctf_platforms": {
                "binary_exploitation": {"ctf_platforms": [{"name": "test"}]},
            },
        }

    @requests_mock.mock()
    def testLoadInventoryJson(self, inventory):
        """test loadInventory function"""
        status_code = 200
        inventory.get(
            "https://inventory.raw.pm/api/api.json",
            json={"tools": {}},
            status_code=status_code,
        )
        self.assertEqual(loadInventoryJson(), {"tools": {}})

    @requests_mock.mock()
    def testLoadInventoryJsonError(self, inventory):
        """test loadInventory function when call failed"""
        status_code = 200
        inventory.get(
            "https://inventory.raw.pm/api/api.json",
            json={"": {}},
            status_code=status_code,
        )
        self.assertEqual(loadInventoryJson(), {})

    def testGetToolsJson(self):
        """test getToolsJson function"""
        self.assertEqual(getToolsJson({}), {})
        self.assertEqual(getToolsJson({"tools": "test"}), "test")

    def testGetResourcesJson(self):
        """test getResourcesJson function"""
        self.assertEqual(getResourcesJson({}), {})
        self.assertEqual(getResourcesJson({"resources": "test"}), "test")

    def testGetCTFJson(self):
        """test getCTFJson function"""
        self.assertEqual(getCTFJson({}), {})
        self.assertEqual(getCTFJson({"ctf_platforms": "test"}), "test")

    def testGetOperatingJson(self):
        """test getOperatingJson function"""
        self.assertEqual(getOperatingJson({}), {})
        self.assertEqual(
            getOperatingJson({"operating_systems": "test"}),
            "test",
        )

    def testGetToolsCategory(self):
        """test getToolsCategory function"""
        self.assertEqual(getToolsCategory(self.json), ["binary_exploitation"])

    def testGetResourcesCategory(self):
        """test getResourcesCategory function"""
        self.assertEqual(
            getResourcesCategory(self.json),
            ["binary_exploitation"],
        )

    def testGetCTFCategory(self):
        """test getCTFCategory function"""
        self.assertEqual(getCTFCategory(self.json), ["binary_exploitation"])

    def testGetOperatingCategory(self):
        """test getOperatingCategory function"""
        self.assertEqual(
            getOperatingCategory(self.json),
            ["binary_exploitation"],
        )

    def testGetToolsByCategory(self):
        """test getToolsByCategory function"""
        self.assertEqual(getToolsByCategory({}, "test"), [])
        self.assertEqual(
            getToolsByCategory(self.json, "binary_exploitation"),
            [{"name": "test"}],
        )

    def testGetResourcesByCategory(self):
        """test getResourcesByCategory function"""
        self.assertEqual(getResourcesByCategory({}, "test"), [])
        self.assertEqual(
            getResourcesByCategory(self.json, "binary_exploitation"),
            [{"name": "test"}],
        )

    def testGetCTFByCategory(self):
        """test getCTFByCategory function"""
        self.assertEqual(getCTFByCategory({}, "test"), [])
        self.assertEqual(
            getCTFByCategory(self.json, "binary_exploitation"),
            [{"name": "test"}],
        )

    def testGetOperatingByCategory(self):
        """test getOperatingByCategory function"""
        self.assertEqual(getOperatingByCategory({}, "test"), [])
        self.assertEqual(
            getOperatingByCategory(self.json, "binary_exploitation"),
            [{"name": "test"}],
        )

    def testGetAllTools(self):
        """test getAllTools function"""
        self.assertEqual(getAllTools({}), [])
        self.assertEqual(getAllTools(self.json), [{"name": "test"}])

    def testGetAllResources(self):
        """test getAllResources function"""
        self.assertEqual(getAllResources({}), [])
        self.assertEqual(getAllResources(self.json), [{"name": "test"}])

    def testGetAllCTF(self):
        """test getAllCTF function"""
        self.assertEqual(getAllCTF({}), [])
        self.assertEqual(getAllCTF(self.json), [{"name": "test"}])

    def testGetAllOperating(self):
        """test getAllOperating function"""
        self.assertEqual(getAllOperating({}), [])
        self.assertEqual(getAllOperating(self.json), [{"name": "test"}])
