# test_cli.py
from pathlib import Path
import click
from click.testing import CliRunner
import pytest
from makebook import cli_main


def test_cli_main():
    runner = CliRunner()
    result = runner.invoke(cli_main)
    assert result.exit_code == 0
    assert "Welcome to makebook!" in result.output


def test_cli_version():
    runner = CliRunner()
    command_list = ["--version", "-v"]
    for command in command_list:
        result = runner.invoke(cli_main, [command])
        assert "2019" in result.output


@pytest.fixture()
def test_cli_generate_config(tempdir):
    runner = CliRunner()
    command_list = ["--generate-config", "-g"]
    for command in command_list:
        result = runner.invoke(cli_main, [command])
        assert result.exit_code == 0
        assert Path(tempdir.path, "makebook-config.py").exists()
