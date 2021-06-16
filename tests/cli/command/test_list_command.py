"""Test file for listCommand File"""
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


def test_list_tools():
    """ test searchTools function"""
    result = CliRunner().invoke(
        cli,
        ["list", "tools", "binary_exploitation"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "tools" in result.output

    result = CliRunner().invoke(
        cli,
        ["list", "tools", "azdazdzd"],
        catch_exceptions=False,
    )
    assert result.exit_code == 1

    result = CliRunner().invoke(
        cli,
        ["list", "tools"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0


def test_list_resource():
    """ test searchResource function"""
    result = CliRunner().invoke(
        cli,
        ["list", "resources", "challenges_platforms"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    result = CliRunner().invoke(
        cli,
        ["list", "resources", "azdazdzd"],
        catch_exceptions=False,
    )
    assert result.exit_code == 1

    result = CliRunner().invoke(
        cli,
        ["list", "resources"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0


def test_list_ctf():
    """ test searchCtf function"""
    result = CliRunner().invoke(
        cli,
        ["list", "ctf", "attack_defense"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    result = CliRunner().invoke(
        cli,
        ["list", "ctf", "azdazdzd"],
        catch_exceptions=False,
    )
    assert result.exit_code == 1

    result = CliRunner().invoke(
        cli,
        ["list", "ctf"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0


def test_list_os():
    """ test searchOs function"""
    result = CliRunner().invoke(
        cli,
        ["list", "os", "maintained"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "os" in result.output

    result = CliRunner().invoke(
        cli,
        ["list", "os", "azdazdzd"],
        catch_exceptions=False,
    )
    assert result.exit_code == 1

    result = CliRunner().invoke(
        cli,
        ["list", "os"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    result = CliRunner().invoke(
        cli,
        ["list", "os", "--base", "Ubuntu"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0


# https://github.com/mBouamama/rawsec_cli/issues/17
def test_list_os_project_transferred():
    """ test searchOs function when category is project_transferred"""
    result = CliRunner().invoke(
        cli,
        ["list", "os", "project_transferred"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "Total" in result.output
