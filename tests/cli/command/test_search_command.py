"""Test file for searchCommand File"""
from click.testing import CliRunner

from rawsec_cli.cli.cli import cli

rawsec_json = {
    "tools": {
        "binary_exploitation": {
            "tools": [{"name": "tools", "website": "test"}],
        },
    },
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


def test_search(mocker):
    """ test search function"""
    mocker.patch(
        "rawsec_cli.search.search_project",
        return_value=[{"name": "tools", "website": "test"}],
    )
    result = CliRunner().invoke(
        cli,
        ["search", "tools"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "tools" in result.output


def test_search_only_1_result():
    """ test search only 1 result function"""
    result = CliRunner().invoke(
        cli,
        ["search", "myjwt"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "myjwt" in result.output

    result = CliRunner().invoke(
        cli,
        ["search", "wfuzz"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "wfuzz" in result.output


def test_search_not_found():
    """ test search incorrect project function"""
    result = CliRunner().invoke(
        cli,
        ["search", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "Project not found!" in result.output
