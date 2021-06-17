"""Test cli file"""
from click.testing import CliRunner

from rawsec_cli.cli.cli import cli


def test_version():
    """test version function"""
    result = CliRunner().invoke(
        cli,
        ["-V"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "version" in result.output
    assert "commit" in result.output
