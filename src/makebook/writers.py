# writers.py

import shutil
import os
import re
from pathlib import Path
import sys
from nbconvert import LatexExporter, NotebookExporter, HTMLExporter, PDFExporter
from nbconvert.preprocessors import RegexRemovePreprocessor
from nbconvert.writers import FilesWriter
from nbformat import NotebookNode
from .utils import convert_links


def copy_all_images_to_dir(notebooks_dir_path=None, out_dir_path=None):
    """
    a function to copy the all of the images out of a input_dir/subdir/images into
    one big folder in output_dir/images
    """
    if not notebooks_dir_path:
        notebooks_dir_path = Path(Path.cwd(), "notebooks")
        if not notebooks_dir_path.exists():
            notebooks_dir_path.mkdir()
    if not out_dir_path:
        out_dir_path = Path(Path.cwd(), "out")
    REG_nb_dir = re.compile((r"(\d\d)-*"))
    try:
        os.listdir(notebooks_dir_path)
    except FileNotFoundError as e:
        print(f"input path {notebooks_dir_path} does not exhist \n{e}")
        exit(1)
    # erase the /out_dir/images dir if it exists
    if os.path.exists(os.path.join(out_dir_path, "images")):
        shutil.rmtree(os.path.join(out_dir_path, "images"))
    p = Path(out_dir_path, "images")
    p.mkdir(parents=True)
    out_images_dir_path = Path(out_dir_path, "images")

    for dir in os.listdir(notebooks_dir_path):
        if REG_nb_dir.match(dir):
            if os.path.exists(os.path.join(notebooks_dir_path, dir, "images")):
                scr_dir = os.path.join(notebooks_dir_path, dir, "images")
                for f in os.listdir(scr_dir):
                    try:
                        shutil.copy(os.path.join(scr_dir, f), out_images_dir_path)
                    except IOError as e:
                        print("Unable to copy file. %s" % e)
                        exit(1)
                    except:
                        print("Unexpected error:", sys.exc_info())
                        exit(1)


class MyLatexExporter(LatexExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ("resolve_references", convert_links)


class MyLatexPDFExporter(PDFExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ("resolve_references", convert_links)


def export_tex(
    combined_nb: NotebookNode, output_file: Path, pdf=False, template_file=None
):
    """
    A function that exports a .tex file from a notebook node object
    """
    resources = {}
    resources["unique_key"] = "combined"
    resources["output_files_dir"] = "combined_files"

    # log.info('Converting to %s', 'pdf' if pdf else 'latex')
    exporter = MyLatexPDFExporter() if pdf else MyLatexExporter()
    if template_file is not None:
        exporter.template_file = str(template_file)
    mypreprocessor = (
        RegexRemovePreprocessor()
    )  # Create an instance of the RegexRemovePreprocessor
    mypreprocessor.patterns = ["\s*\Z"]  # supply a re pattern (in a list) to the preprocessor's .patterns attribute
    exporter.register_preprocessor(mypreprocessor, enabled=True)  # apply the preprocessor to the exporter
    writer = FilesWriter(build_directory=str(output_file.parent))
    output, resources = exporter.from_notebook_node(combined_nb, resources)
    writer.write(output, resources, notebook_name=output_file.stem)
