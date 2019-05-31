# Welcome to the Makebook Documentation

Makebook is a Python project that makes books from Jupyter notebooks and markdown files.

## Installation

```
git clone https://github.com/ProfessorKazarinoff/makebook.git
cd makebook.git
python -m venv venv
venv\Scripts\activate.bat   # source venv/bin/activate
(venv) pip install -r requirements.txt
(venv) pip install .        # install local version of makebook package
```

## Commands

Makebook offers the following cli commands

| command | output |
| --- | --- |
| ```makebook``` | prints welcome message |
| ```makebook -h or --help``` | prints makebook command line options |
| ```makebook -v or --version``` | prints the date-based version number |
| ```makebook -g or --generate-config``` | create a ```makebook-config.py``` configuration file |

## Project layout

    makebook-config.py  # The configuration file.
    notbooks/
        ch1.ipynb       # Jupyter notebook containing text.
        ...             # Other notebook files.
    out/
        book.tex        # The output LaTeX file
