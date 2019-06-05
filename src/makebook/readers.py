# readers.py

import os
import re
from pathlib import Path
import nbformat


def iter_notebook_paths(notebook_dir_name=None):
    if not notebook_dir_name:
        notebook_dir_name = "notebooks"

    rootdir = Path(Path.cwd(), notebook_dir_name)

    # For absolute paths instead of relative the current dir
    file_list = sorted(
        [
            f
            for f in rootdir.resolve().glob("**/*")
            if f.is_file()
            and f.suffix == ".ipynb"
            and not ".ipynb_checkpoints" in str(f)
        ]
    )
    return file_list


def merge_notebooks(filename_lst):
    """
    a function that creates a single notebook node object from a list of notebook file paths
    :param filename_lst: lst, a list of .ipynb file paths
    :return: a single notebookNode object
    """
    merged = None
    for fname in filename_lst:
        with open(fname, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, "name"):
        merged.metadata.name = ""
    merged.metadata.name += "_merged"
    # print(nbformat.writes(merged))
    return merged
