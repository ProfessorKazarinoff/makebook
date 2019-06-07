# setup.py

from setuptools import setup, find_packages
import sys


assert sys.version_info >= (3, 6, 0), "makebook requires Python 3.6+"
from pathlib import Path

CURRENT_DIR = Path(__file__).parent


def get_readme() -> str:
    """
    a function to pull the long description from the README.md file
    """
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


README = get_readme()
CHANGELOG = ""
description = "\n".join([README, CHANGELOG])
VERSION = "2019.06.04"

setup(
    name="makebook",
    version=VERSION,
    url="https://github.com/ProfessorKazarinoff/makebook",
    author="Peter Kazarinoff",
    maintainer="Peter Kazarinoff",
    description="A package that converts directories of notebooks into a book",
    long_description=description,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["Click"],
    entry_points={"console_scripts": ["makebook=makebook.cli:cli"]},
)
