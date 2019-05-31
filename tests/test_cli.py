# test_start.py

from makebook import cli_main, main
from subprocess import check_output
import sys

import click
from click.testing import CliRunner


def test_cli_main():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Welcome to makebook!" in result.output
