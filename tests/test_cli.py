# test_cli.py

from makebook import cli_main
from subprocess import check_output
import sys

import click
from click.testing import CliRunner


def test_cli_main():
    runner = CliRunner()
    result = runner.invoke(cli_main)
    assert result.exit_code == 0
    assert "Welcome to makebook!" in result.output


def test_cli_generate_config():
    assert False
