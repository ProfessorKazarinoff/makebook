# test_cli.py
from pathlib import Path
import click
from click.testing import CliRunner
import pytest
from makebook import cli


def test_foo_bar(script_runner):
    ret = script_runner.run("--version")
    assert ret.success
    # just for example, let's assume that foobar --version
    # should output 3.2.1
    assert "2019" in ret.stdout
    assert ret.stderr == ""


@pytest.mark.script_launch_mode("subprocess")
def test_cli_with_pytest_plugin(script_runner):
    ret = script_runner.run("makebook", "--version")
    assert ret.success
    assert "2019" in ret.stout
    assert ret.stderr == ""


def test_cli_main():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Welcome to Makebook!\n\n" in result.output
    assert (
        "Makebook is a Python package that turns notebooks into books" in result.output
    )


def test_cli_version():
    runner = CliRunner()
    command_list = ["--version", "-v"]
    for command in command_list:
        result = runner.invoke(cli, [command])
        assert "2019" in result.output
    assert result.exit_code == 0


def test_cli_help():
    runner = CliRunner()
    command_list = ["--help", "-h"]
    for command in command_list:
        result = runner.invoke(cli, [command])
        assert "Options:" in result.output
        assert "-h, --help" in result.output
    assert result.exit_code == 0


def test_cli_build_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["build", "--help"])
    assert (
        "Run the build tool to convert a directory of notebooks to a .tex file"
        in result.output
    )
    assert "-h, --help" in result.output
    assert result.exit_code == 0


def test_cli_create():
    runner = CliRunner()
    result = runner.invoke(cli, ["create"])
    assert "Creating a new book called" in result.output
    assert result.exit_code == 0


def test_cli_create_name():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "-n", "my_title"])
    assert "Creating a new book called my_title" in result.output
    assert result.exit_code == 0


@pytest.fixture()
def test_cli_generate_config(tempdir):
    runner = CliRunner()
    command_list = ["--generate-config", "-g"]
    for command in command_list:
        result = runner.invoke(cli, [command])
        assert result.exit_code == 0
        assert Path(tempdir.path, "makebook-config.py").exists()
