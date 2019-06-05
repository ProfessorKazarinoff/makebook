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
SOURCE_FORMAT =""
OUT_FORMAT = ""
TEMPLATES_DIR = ""
PLUGINS = []
CUSTROM_READER = False
CUSTOM_WRITER = False
OUT_IMAGES_DIR = ""
"""


def write_config(base_dir):
    config_path = os.path.join(base_dir, "makebook-config.py")
    io.open(config_path, "w", encoding="utf-8").write(config_text)


def build_tex():
    pass
