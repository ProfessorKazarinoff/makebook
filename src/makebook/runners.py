# runners.py
"""
functions to run build tasks
"""
import os
from pathlib import Path
from .writers import copy_all_images_to_dir, export_tex
from .readers import iter_notebook_paths, merge_notebooks


def build_tex(input_dir=None, output_dir=None, template_file_path=None):
    """
    a function to build a tex file given a notebook directory path
    """
    if not input_dir:
        input_dibr = Path(Path.cwd(),'notebooks')
    if not output_dir:
        output_dir = Path(Path.cwd(),'out')
    if not template_file_path:
        template_file_path = Path(
        Path.cwd(), "conversion_tools", "templates", "book37.tplx"
    )

    copy_all_images_to_dir(input_dir, output_dir)
    nb_path_lst = iter_notebook_paths(input_dir)
    nbnode = merge_notebooks(nb_path_lst)
    export_tex(nbnode, output_dir, pdf=False, template_file=template_file_path)
