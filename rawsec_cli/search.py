import requests

from rawsec_cli.tools import getTools, getToolsCategory


def searchTool(json, name):
    for category in getToolsCategory(json):
        items = getTools(json, category)
        for item in items:
            if item["name"] == name:
                return item
    return {}


# r = requests.get("https://inventory.raw.pm/api/api.json")
#
# print(searchTool(r.json(), "jwt_tool"))
