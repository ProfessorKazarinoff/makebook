# cli.py

import click


@click.command()
def main():
    """
    Example script.
    """
    click.echo(click.style("\nWelcome to makebook!", fg="green"))
    click.echo(
        click.style(
            "\n\nA Python package that makes books from notebooks and markdown files\n",
            fg="blue",
        )
    )


def cli_main():
    main()
