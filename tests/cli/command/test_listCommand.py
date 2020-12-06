from unittest import TestCase

from rawsec_cli.cli.cli import cli
from click.testing import CliRunner


class TestListCommand(TestCase):
    def setUp(self):
        self.json = {
            "tools": {
                "binary_exploitation": {
                    "tools": [{"name": "tools", "website": "test"}]
                }
            },
            "resources": {
                "binary_exploitation": {"resources": [{"name": "resources"}]}
            },
            "operating_systems": {
                "binary_exploitation": {
                    "operating_systems": [{"os": "operating_systems"}]
                }
            },
            "ctf_platforms": {
                "binary_exploitation": {
                    "ctf_platforms": [{"name": "ctf_platforms"}]
                }
            },
        }

    def testSearchTools(self):
        result = CliRunner().invoke(
            cli,
            ["list", "tools", "binary_exploitation"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("tools", result.output)

        result = CliRunner().invoke(
            cli, ["list", "tools", "azdazdzd"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 1)

        result = CliRunner().invoke(
            cli, ["list", "tools"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)

    def testSearchResource(self):
        result = CliRunner().invoke(
            cli,
            ["list", "resources", "challenges_platforms"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("name", result.output)

        result = CliRunner().invoke(
            cli, ["list", "resources", "azdazdzd"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 1)

        result = CliRunner().invoke(
            cli, ["list", "resources"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)

    def testSearchCtf(self):
        result = CliRunner().invoke(
            cli, ["list", "ctf", "attack_defense"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("name", result.output)

        result = CliRunner().invoke(
            cli, ["list", "ctf", "azdazdzd"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 1)

        result = CliRunner().invoke(
            cli, ["list", "ctf"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)

    def testSearchOs(self):
        result = CliRunner().invoke(
            cli, ["list", "os", "maintained"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("os", result.output)

        result = CliRunner().invoke(
            cli, ["list", "os", "azdazdzd"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 1)

        result = CliRunner().invoke(
            cli, ["list", "os"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)

        result = CliRunner().invoke(
            cli, ["list", "os", "--base", "Ubuntu"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)
