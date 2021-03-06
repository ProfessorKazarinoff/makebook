# coding: utf-8
from __future__ import unicode_literals

import io
import os


config_text = """# coding: utf-8
# makebook-config.py
#
# Configuration for makebook
#
TITLE = ""
AUTHOR = ""
PUBLISH_DATE = ""
PUBLISHER = ""
SOURCE_DIR = ""
SOURCE_FORMAT = ""
FILES_TO_EXCLUDE = ""
OUT_DIR = ""
OUT_FORMAT = ""
TEMPLATES_DIR = ""
TEMPLATE = ""
FILES_TO_COPY = []
PLUGINS = []
CUSTOM_READER = False
CUSTOM_WRITER = False
OUT_IMAGES_DIR = ""
"""


def write_config(base_dir):
    config_path = os.path.join(base_dir, "makebook-config.py")
    io.open(config_path, "w", encoding="utf-8").write(config_text)


def create_book(book_name):
    """function creates the skelton directory structure for make a new book and config file"""
    pass
