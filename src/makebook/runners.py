# runners.py
"""
functions to run build tasks
"""
import os
from pathlib import Path
from .writers import copy_all_images_to_dir, export_tex
from .readers import iter_notebook_paths, merge_notebooks


def build_tex(
    input_dir=None, output_dir=None, output_file_stem=None, template_file_path=None
):
    """
    a function to build a tex file given a notebook directory path. Consists of four parts:
    1. copy all of the images from the source dir to an output/images dir
    2. builds a list of file paths for all the notebooks in the source dir
    3. merges together all the notebooks in the source dir into one big notebook node object
    4. exports the big notebook node object to a .tex file
    """
    if not input_dir:
        input_dibr = Path(Path.cwd(), "notebooks")
    if not output_dir:
        output_dir = Path(Path.cwd(), "out")
    if not template_file_path:
        template_file_path = Path(Path.cwd(), "templates", "book37.tplx")
    if not output_file_stem:
        output_file_stem = "output"

    output_file_path = Path(output_dir, output_file_stem)

    copy_all_images_to_dir(input_dir, output_dir)
    nb_path_lst = iter_notebook_paths(input_dir)
    nbnode = merge_notebooks(nb_path_lst)

    export_tex(nbnode, output_file_path, pdf=False, template_file=template_file_path)
