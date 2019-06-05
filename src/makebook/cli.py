# # cli.py

# import click
# from .utils import get_version
# from .commands import write_config
# from .runners import build_tex
# import os

# config_help = "Creates a makebook config file called makebook-config.py"
# version_help = "Prints out the makebook version number."
# help_help = "Show this message and exit."
# build_help = "Run the build tool to convert a directory of notebooks to a .tex file"

# @click.group()
# #@click.command()
# @click.option(
#     "-g", "--generate-config", "generate_config", help=config_help, is_flag=True
# )
# @click.option("-b", "--build", "build", help=build_help, is_flag=True)
# @click.option("-v", "--version", "version", help=version_help, is_flag=True)
# @click.option("-h", "ask_help", help=help_help, is_flag=True)
# @click.pass_context
# def main(ctx,generate_config, build, version, ask_help):
#     """
#     Makebook is a Python package used to create books from Jupyter Notebook files.
#     There is a command-line interface to generate a configuration file.
#     The configuration file can be modified and be used to build the book
#     """
#     if generate_config:
#         click.echo("Generating config file...")
#         click.echo("Creating a file called makebook-config.py")
#         config_dir = os.getcwd()
#         write_config(config_dir)
#     elif build:
#         click.echo("Building a .tex file from a directory of notebooks...")
#         build_tex()
#         click.echo(".tex file available in out directory")
#     elif ask_help:
#         click.echo("Working on calling the help function and show help")
#     elif version:
#         click.echo(f"Makebook Version: {get_version()}")
#     else:
#         click.echo(click.style("\nWelcome to makebook!", fg="green"))
#         click.echo(
#             click.style(
#                 "\n\nA Python package that makes books from notebooks and markdown files\n",
#                 fg="blue",
#             )
#         )

# @main.command()  # @cli, not @click!
# @click.pass_context
# def sync(ctx):
#     click.echo('Syncing')

# @main.command()
# @click.option("--filename", help="full path to the png file")
# @click.pass_context
# def png(ctx, filename):
#     click.echo('Running png command')

# # make a command option that includes > makebook build --config-file or -c
# # make a command > makebook build --source-dir or -s
# # make a command > makebook build --outfile or -o

# if __name__ == "__main__":
#     main(obj={})

# # def cli_main():
# #    main()
import click

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

@click.group()
@click.option('--debug/--no-debug', default=False, is_flag=True)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.pass_context
def cli(ctx, debug):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    ctx.ensure_object(dict)

    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context
def sync(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))

if __name__ == '__main__':
    cli(obj={})