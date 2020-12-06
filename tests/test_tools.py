import json
import os
from unittest import TestCase

import requests_mock
from rawsec_cli.tools import loadInventoryJson, getToolsJson, getResourcesJson, getCTFJson, getOperatingJson, \
    getToolsCategory, getResourcesCategory, getCTFCategory, getOperatingCategory, getToolsByCategory, \
    getResourcesByCategory, getOperatingByCategory, getCTFByCategory, getAllTools, getAllResources, getAllCTF, \
    getAllOperating


class TestTools(TestCase):
    def setUp(self):
        self.json = {
            "tools": {"binary_exploitation": {"tools": [{"name": "test"}]}},
            "resources": {"binary_exploitation": {"resources": [{"name": "test"}]}},
            "operating_systems": {"binary_exploitation": {"operating_systems": [{"name": "test"}]}},
            "ctf_platforms": {"binary_exploitation": {"ctf_platforms": [{"name": "test"}]}}
        }

    @requests_mock.mock()
    def testLoadInventoryJson(self, inventory):
        status_code = 200
        inventory.get("https://inventory.raw.pm/api/api.json", json={"tools": {}}, status_code=status_code)
        self.assertEqual(loadInventoryJson(), {"tools": {}})

    @requests_mock.mock()
    def testLoadInventoryJsonError(self, inventory):
        status_code = 200
        inventory.get("https://inventory.raw.pm/api/api.json", json={"": {}}, status_code=status_code)
        self.assertEqual(loadInventoryJson(), {})

    def testGetToolsJson(self):
        self.assertEqual(getToolsJson({}), {})
        self.assertEqual(getToolsJson({"tools": "test"}), "test")

    def testGetResourcesJson(self):
        self.assertEqual(getResourcesJson({}), {})
        self.assertEqual(getResourcesJson({"resources": "test"}), "test")

    def testGetCTFJson(self):
        self.assertEqual(getCTFJson({}), {})
        self.assertEqual(getCTFJson({"ctf_platforms": "test"}), "test")

    def testGetOperatingJson(self):
        self.assertEqual(getOperatingJson({}), {})
        self.assertEqual(getOperatingJson({"operating_systems": "test"}), "test")

    def testGetToolsCategory(self):
        self.assertEqual(getToolsCategory(self.json), ["binary_exploitation"])

    def testGetResourcesCategory(self):
        self.assertEqual(getResourcesCategory(self.json), ["binary_exploitation"])

    def testGetCTFCategory(self):
        self.assertEqual(getCTFCategory(self.json), ["binary_exploitation"])

    def testGetOperatingCategory(self):
        self.assertEqual(getOperatingCategory(self.json), ["binary_exploitation"])

    def testGetToolsByCategory(self):
        self.assertEqual(getToolsByCategory({}, "test"), [])
        self.assertEqual(getToolsByCategory(self.json, "binary_exploitation"), [{"name": "test"}])

    def testGetResourcesByCategory(self):
        self.assertEqual(getResourcesByCategory({}, "test"), [])
        self.assertEqual(getResourcesByCategory(self.json, "binary_exploitation"), [{"name": "test"}])

    def testGetCTFByCategory(self):
        self.assertEqual(getCTFByCategory({}, "test"), [])
        self.assertEqual(getCTFByCategory(self.json, "binary_exploitation"), [{"name": "test"}])

    def testGetOperatingByCategory(self):
        self.assertEqual(getOperatingByCategory({}, "test"), [])
        self.assertEqual(getOperatingByCategory(self.json, "binary_exploitation"), [{"name": "test"}])

    def testGetAllTools(self):
        self.assertEqual(getAllTools({}), [])
        self.assertEqual(getAllTools(self.json), [{"name": "test"}])

    def testGetAllResources(self):
        self.assertEqual(getAllResources({}), [])
        self.assertEqual(getAllResources(self.json), [{"name": "test"}])

    def testGetAllCTF(self):
        self.assertEqual(getAllCTF({}), [])
        self.assertEqual(getAllCTF(self.json), [{"name": "test"}])

    def testGetAllOperating(self):
        self.assertEqual(getAllOperating({}), [])
        self.assertEqual(getAllOperating(self.json), [{"name": "test"}])
