"""Test file for search File"""
from rawsec_cli.search import search_project
from rawsec_cli.search import search_project_ctf
from rawsec_cli.search import search_project_operating
from rawsec_cli.search import search_project_resources
from rawsec_cli.search import search_project_tools

rawsec_json = {
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


def test_search_project_tools():
    """test search_project_tools function"""
    assert search_project_tools(rawsec_json, "tools") == [{"name": "tools"}]


def test_search_project_resources():
    """test search_project_resources function"""
    assert search_project_resources(rawsec_json, "resources") == [
        {"name": "resources"},
    ]


def test_search_project_ctf():
    """test search_project_ctf function"""
    assert search_project_ctf(rawsec_json, "ctf_platforms") == [
        {"name": "ctf_platforms"},
    ]


def test_search_project_operating():
    """test search_project_operating function"""
    assert search_project_operating(rawsec_json, "operating_systems") == [
        {"os": "operating_systems"},
    ]


def test_search_project():
    """test search_project function"""
    assert search_project(rawsec_json, "tools") == [{"name": "tools"}]
