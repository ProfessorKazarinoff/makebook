# readers.py

import os
import re
from pathlib import Path

def mb():
    return "makebook function"


def iter_notebook_paths(notebook_dir_name='notebooks'):
    """
    function outputs a list of paths of the all notebooks inside sub dirs inside the notebook dir
    :param notebook_dir_name: str, the main directory with the notebooks, default 'notebooks'
    :return: lst, example ['../notebooks/00-Prefence/00.01-Introduction.ipynb','../notebooks/01-Introduction/01.01-The-Python-REPL.ipynb']
    """
    NOTEBOOK_DIR = os.path.join(Path.cwd(), notebook_dir_name)
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    nb_path_lst = []
    for sub_dir_path in iter_notebook_sub_dirs_path(notebook_dir_name):
        for file in os.listdir(sub_dir_path):
            if REG_nb.match(file):
                nb_path = os.path.join(sub_dir_path, file)
                nb_path_lst.append(nb_path)

    return sorted(nb_path_lst)

def iter_notebook_sub_dirs_path(notebook_dir_name='notebooks'):
    """
    function outputs a list of paths of the notebooks sub dirs inside the notebook dir
    :param notebook_dir_name: str, the main directory with the notebooks, default 'notebooks'
    :return: lst, example ['../notebooks/00-Prefence','../notebooks/01-Introduction']
    """
    NOTEBOOK_DIR = os.path.join(os.pardir, notebook_dir_name)
    REG_nb_dir = re.compile((r'(\d\d)-*'))
    nb_sub_dir_path_lst = []
    for dir in os.listdir(NOTEBOOK_DIR):
        if REG_nb_dir.match(dir):
            dir_path=os.path.join(os.pardir, notebook_dir_name, dir)
            nb_sub_dir_path_lst.append(dir_path)
    return sorted(nb_sub_dir_path_lst)


def merge_notebooks():
    """
    a function that creates a single notebook node object from a list of notebook file paths
    :param filename_lst: lst, a list of .ipynb file paths
    :return: a single notebookNode object
    """
    pass
