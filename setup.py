# setup.py

from setuptools import setup, find_packages

README = ""
CHANGELOG = ""
description = u'\n'.join([README, CHANGELOG])

setup(
    name="makebook",
    version="2018.05.30",
    url='https://github.com/ProfessorKazarinoff/makebook',
    author = "Peter Kazarinoff",
    maintainer = "Peter Kazarinoff",
    description = 'A package to convert directories of notebooks into a book',
    long_description=description,
    license='GNU General Public License v3.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
