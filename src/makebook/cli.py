# cli.py

import os
from pathlib import Path
import click

from .utils import get_version
from .commands import write_config
from .runners import build_tex


def print_version_callback(ctx, param, value):
    """
    function to be used as a call back by click to print the version
    ctx is the context that gets passed from the click command to the function
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Makebook Version: {get_version()}")
    ctx.exit()

def generate_config_callback(ctx, param, value):
    """
    function to be used as a call back by click to generate a boilerplate config file
    ctx is the context that gets passed from the click command to the function
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo("Generating config file...")
    click.echo("Creating a file called makebook-config.py")
    config_dir = os.getcwd()
    write_config(config_dir)
    click.echo(f"Makebook Version: {get_version()}")
    ctx.exit()


config_help = "Creates a makebook config file called makebook-config.py"
version_help = "Prints out the makebook version number."


@click.group()
@click.option('--version',"-v", help=version_help, is_flag=True, callback=print_version_callback, expose_value=False, is_eager=True)
@click.option("-g", "--generate-config",
                help=config_help, is_flag=True, callback=generate_config_callback, expose_value=False, is_eager=True)
@click.pass_context
def cli(ctx):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    ctx.ensure_object(dict)

build_help = "Run the build tool to convert a directory of notebooks to a .tex file"

@cli.command(help=build_help)
@click.pass_context
def build(ctx):
    click.echo("building from source...")
    source_dir = Path(Path.cwd(),'notebooks')
    out_dir = Path(Path.cwd(),'out')
    click.echo(f"source directry: {source_dir}")
    click.echo(f"output directory: {out_dir}")
    #build_tex()

if __name__ == '__main__':
    cli(obj={})
