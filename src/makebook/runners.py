# runners.py
"""
functions to run build tasks
"""

from .writers import copy_all_images_to_dir, export_nbnode
from .readers import iter_notebook_paths, merge_notebooks


def build_tex(input_dir=None,output_dir=None):
    """
    a function to build a tex file given a notebook directory path
    """
    copy_all_images_to_dir(input_dir,output_dir)
    #iter_notebook_paths(input_dir)
    merge_notebooks()
    export_nbnode()
