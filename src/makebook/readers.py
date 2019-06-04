# readers.py


def mb():
    return "makebook function"


def iter_notebook_paths(notebook_dir_name="notebooks"):
    """
    function outputs a list of paths of the all notebooks inside sub dirs inside the notebook dir
    :param notebook_dir_name: str, the main directory with the notebooks, default 'notebooks'
    :return: lst, example ['../notebooks/00-Prefence/00.01-Introduction.ipynb','../notebooks/01-Introduction/01.01-The-Python-REPL.ipynb']
    """
    pass


def merge_notebooks():
    """
    a function that creates a single notebook node object from a list of notebook file paths
    :param filename_lst: lst, a list of .ipynb file paths
    :return: a single notebookNode object
    """
    pass
