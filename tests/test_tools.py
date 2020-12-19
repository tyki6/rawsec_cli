"""Test file for tools File"""
from rawsec_cli.tools import get_all_ctf
from rawsec_cli.tools import get_all_operating
from rawsec_cli.tools import get_all_resources
from rawsec_cli.tools import get_all_tools
from rawsec_cli.tools import get_ctf_by_category
from rawsec_cli.tools import get_ctf_category
from rawsec_cli.tools import get_ctf_json
from rawsec_cli.tools import get_operating_by_category
from rawsec_cli.tools import get_operating_category
from rawsec_cli.tools import get_operating_json
from rawsec_cli.tools import get_resources_by_category
from rawsec_cli.tools import get_resources_category
from rawsec_cli.tools import get_resources_json
from rawsec_cli.tools import get_tools_by_category
from rawsec_cli.tools import get_tools_category
from rawsec_cli.tools import get_tools_json
from rawsec_cli.tools import load_inventory_json

rawsec_json = {
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


def test_load_inventory_json(requests_mock):
    """test load_inventory_json function"""
    status_code = 200
    requests_mock.get(
        "https://inventory.raw.pm/api/api.json",
        json={"tools": {}},
        status_code=status_code,
    )
    assert load_inventory_json() == {"tools": {}}


def test_load_inventory_json_error(requests_mock):
    """test load_inventory_json function when call failed"""
    status_code = 200
    requests_mock.get(
        "https://inventory.raw.pm/api/api.json",
        json={"": {}},
        status_code=status_code,
    )
    assert load_inventory_json() == {}


def test_get_tools_json():
    """test get_tools_json function"""
    assert get_tools_json({}) == {}
    assert get_tools_json({"tools": "test"}) == "test"


def test_get_resources_json():
    """test get_resources_json function"""
    assert get_resources_json({}) == {}
    assert get_resources_json({"resources": "test"}) == "test"


def test_get_ctf_json():
    """test get_ctf_json function"""
    assert get_ctf_json({}) == {}
    assert get_ctf_json({"ctf_platforms": "test"}) == "test"


def test_get_operating_json():
    """test get_operating_json function"""
    assert get_operating_json({}) == {}
    assert get_operating_json({"operating_systems": "test"}) == "test"


def test_get_tools_category():
    """test get_tools_category function"""
    assert get_tools_category(rawsec_json) == ["binary_exploitation"]


def test_get_resources_category():
    """test get_resources_category function"""
    assert get_resources_category(rawsec_json) == ["binary_exploitation"]


def test_get_ctf_category():
    """test get_ctf_category function"""
    assert get_ctf_category(rawsec_json) == ["binary_exploitation"]


def test_get_operating_category():
    """test get_operating_category function"""
    assert get_operating_category(rawsec_json) == ["binary_exploitation"]


def test_get_tools_by_category():
    """test get_tools_by_category function"""
    assert get_tools_by_category({}, "test") == []
    assert get_tools_by_category(rawsec_json, "binary_exploitation") == [
        {"name": "test"},
    ]


def test_get_resources_by_category():
    """test get_resources_by_category function"""
    assert get_resources_by_category({}, "test") == []
    assert get_resources_by_category(rawsec_json, "binary_exploitation") == [
        {"name": "test"},
    ]


def test_get_ctf_by_category():
    """test get_ctf_by_category function"""
    assert get_ctf_by_category({}, "test") == []
    assert get_ctf_by_category(rawsec_json, "binary_exploitation") == [
        {"name": "test"},
    ]


def test_get_operating_by_category():
    """test get_operating_by_category function"""
    assert get_operating_by_category({}, "test") == []
    assert get_operating_by_category(rawsec_json, "binary_exploitation") == [
        {"name": "test"},
    ]


def test_get_all_tools():
    """test get_all_tools function"""
    assert get_all_tools({}) == []
    assert get_all_tools(rawsec_json) == [{"name": "test"}]


def test_get_all_resources():
    """test get_all_resources function"""
    assert get_all_resources({}) == []
    assert get_all_resources(rawsec_json) == [{"name": "test"}]


def test_get_all_ctf():
    """test get_all_ctf function"""
    assert get_all_ctf({}) == []
    assert get_all_ctf(rawsec_json) == [{"name": "test"}]


def test_get_all_operating():
    """test get_all_operating function"""
    assert get_all_operating({}) == []
    assert get_all_operating(rawsec_json) == [{"name": "test"}]
