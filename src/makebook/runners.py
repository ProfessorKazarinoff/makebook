# runners.py
"""
functions to run build tasks
"""
import os
from pathlib import Path
from .writers import copy_all_images_to_dir, export_tex
from .readers import iter_notebook_paths, merge_notebooks


def build_tex(input_dir=None, output_dir=None):
    """
    a function to build a tex file given a notebook directory path
    """
    copy_all_images_to_dir(input_dir, output_dir)
    nb_path_lst = iter_notebook_paths(input_dir)
    nbnode = merge_notebooks(nb_path_lst)
    outfile_Path = Path(Path.cwd(), "pdf", "out")
    template_file_Path = Path(
        Path.cwd(), "conversion_tools", "templates", "book37.tplx"
    )
    export_tex(nbnode, outfile_Path, pdf=False, template_file=template_file_Path)
