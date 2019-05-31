# cli.py

import click
from .utils import get_version

config_help = "Creates a makebook config file called makebook-config.py"
version_help = "Prints out the makebook version number"
help_help = "Show makebook cli options"


@click.command()
@click.option(
    "-g", "--generate-config", "generate_config", help=config_help, is_flag=True
)
@click.option("-v", "--version", "version", help=version_help, is_flag=True)
@click.option("-h", "ask_help", help=help_help, is_flag=True)
def cli_main(generate_config, version, ask_help):
    """
    Example script.
    """
    if generate_config:
        click.echo("generating config doc")
        click.echo("creating a file called makebook-config.py")
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


# make a command that generates the config file
# > makebook --generate-config

# make a command option that includes > makebook build--config-file or -c
# make a command > makebook build --source-dir or -s
# make a command > makebook build --out-dir or -o

# def cli_main():
#    main()
