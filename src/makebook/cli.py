# cli.py

import click

@click.command()
def main():
    """Example script."""
    click.echo('Welcome to makebook \nthe Python package that makes books')

def cli_main():
    main()