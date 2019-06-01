# cli.py

import click
from .utils import get_version
from .commands import write_config
import os

config_help = "Creates a makebook config file called makebook-config.py"
version_help = "Prints out the makebook version number."
help_help = "Show this message and exit."


@click.command()
@click.option(
    "-g", "--generate-config", "generate_config", help=config_help, is_flag=True
)
@click.option("-v", "--version", "version", help=version_help, is_flag=True)
@click.option("-h", "ask_help", help=help_help, is_flag=True)
def cli_main(generate_config, version, ask_help):
    """
    Makebook is a Python package used to create books from Jupyter Notebook files.
    There is a command-line interface to generate a configuration file.
    The configuration file can be modified and be used to build the book
    """
    if generate_config:
        click.echo("Generating config file...")
        click.echo("Creating a file called makebook-config.py")
        config_dir = os.getcwd()
        write_config(config_dir)
    elif ask_help:
        click.echo("Working on calling the help function and show help")
    elif version:
        click.echo(f"Makebook Version: {get_version()}")
    else:
        click.echo(click.style("\nWelcome to makebook!", fg="green"))
        click.echo(
            click.style(
                "\n\nA Python package that makes books from notebooks and markdown files\n",
                fg="blue",
            )
        )


# make a command option that includes > makebook build --config-file or -c
# make a command > makebook build --source-dir or -s
# make a command > makebook build --outfile or -o

# def cli_main():
#    main()
