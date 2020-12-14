"""Test cli file"""
from unittest import TestCase

from click.testing import CliRunner

from rawsec_cli.cli.cli import cli


class TestCli(TestCase):
    """Test Cli class"""

    def testVersion(self):
        """ test searchTools function"""
        result = CliRunner().invoke(
            cli,
            ["-V"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("version", result.output)
        self.assertIn("commit", result.output)
