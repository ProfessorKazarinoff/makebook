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
    click.echo("Creating a file: makebook-config.py ...")
    config_dir = os.getcwd()
    write_config(config_dir)
    click.echo(f"makebook-config.py created in {os.getcwd()}")
    ctx.exit()


config_help = "Creates a makebook config file called makebook-config.py"
version_help = "Prints out the makebook version number."


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--version",
    "-v",
    help=version_help,
    is_flag=True,
    callback=print_version_callback,
    expose_value=False,
    is_eager=True,
)
@click.option(
    "-g",
    "--generate-config",
    help=config_help,
    is_flag=True,
    callback=generate_config_callback,
    expose_value=False,
    is_eager=True,
)
# @click.argument('-s','--source','source',
#     help="source directory",
#     required = False,
#     type=click.Path(exists=True))
# options to include:
# -c --config config file path
# -s --source source dir path
# -o --output output dir path
# -t --template template file path
# -n --name file name of output file
# -i --include list of file paths to include in the output dir
# -e --exclude list of file paths to exclude from the source dir
@click.pass_context
def cli(ctx):#, debug, source):
    """makebook is a Python package that turns notebooks into books"""
    ctx.ensure_object(dict)
    #ctx.obj['SOURCE_DIR'] = source


build_help = "Run the build tool to convert a directory of notebooks to a .tex file"
source_directory_help = "The directory that contains the source notebooks"


@cli.command(help=build_help)
@click.option(
    "-s","--source", "source",
    nargs=1,
    type=click.Path(
        exists=True, file_okay=True, dir_okay=True, readable=True, allow_dash=True
    ),
    help="input directory or file",
    show_default = True,
    required = False,
    default = Path(Path.cwd(),"notebooks")
)
@click.option(
    "-o","--output-directory", "output_dir",
    nargs=1,
    type=click.Path(
        exists=False, file_okay=False, dir_okay=True, readable=False, allow_dash=True
    ),
    help="output directory for generated file",
    show_default = True,
    required = False,
    default = Path(Path.cwd(),"output")
)
@click.option(
    "-f","--file-name", "output_file_name",
    nargs=1,
    type=click.File('wb'),
    help="generated file name",
    show_default = True,
    required = False,
    default = "output.tex"
)
@click.option(
    "-c","--config", "config_file_path",
    nargs=1,
    type=click.Path(
        exists=False, file_okay=True, dir_okay=False, readable=True, allow_dash=True
    ),
    help="config file path",
    show_default = True,
    required = False,
    default = Path(Path.cwd(),'makebook-config.py'),
)
@click.option(
    "-t","--template", "template_file_path",
    nargs=1,
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, readable=True, allow_dash=True
    ),
    help="template file path",
    show_default = True,
    required = False,
    default = Path(Path.cwd(),'templates','book37.tplx'),
)
@click.option(
    "-i","--include", "include_file_paths",
    nargs=1,   #TODO: see if this option can accept more than two files
    type=click.Path(
        exists=True, file_okay=True, dir_okay=True, readable=True, allow_dash=True
    ),
    help="files and directories to copy into output dir",
    required = False)
@click.option(
    "-e","--exclude", "exclude_file_paths",
    nargs=1,   #TODO: see if this option can accept more than one file
    type=click.Path(
        exists=True, file_okay=True, dir_okay=True, readable=True, allow_dash=True
    ),
    help="files and directories in source to ignore when building the book",
    required = False)
@click.pass_context
def build(ctx, source, output_dir, output_file_name, config_file_path, template_file_path, include_file_paths,exclude_file_paths):
    """build book from source directory"""
    # ctx.obj['DEBUG']  # grabe the DEBUG object from the ctx context
    click.echo("building from source...")
    source_dir = Path(Path.cwd(), source)
    out_dir = Path(Path.cwd(), output_dir)
    click.echo(f"source directry: {str(source_dir)}")
    click.echo(f"output directory: {str(out_dir)}")
    click.echo(f"output filename: {str(output_file_name)}")
    #click.echo(f"using config file: {str(config_file_path)}")
    click.echo(f"using template: {str(template_file_path)}")
    #build_tex()  # args(input_dir=None, output_dir=None, output_file_stem=None, template_file_path=)


if __name__ == "__main__":
    cli(obj={})
