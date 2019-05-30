# setup.py

from setuptools import setup, find_packages

setup(
    name="makebook",
    version="2018.05.29",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
