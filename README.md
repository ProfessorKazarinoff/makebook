# !! Under Construction !! Not Ready for Use !!

# Welcome to the Makebook Documentation 
 
Makebook is a Python project that makes books from Jupyter notebooks and markdown files.

## Installation

```text
git clone https://github.com/ProfessorKazarinoff/makebook.git
cd makebook
python -m venv venv
venv\Scripts\activate.bat   # source venv/bin/activate
(venv) pip install -r requirements.txt
(venv) pip install .        # install a local version of the makebook package
```

## Commands

Makebook offers the following cli commands

| command | output |
| --- | --- |
| ```makebook``` | prints makebook command line options |
| ```makebook --help``` | prints Makebook command line options |
| ```makebook -v or --version``` | prints the date-based version number |
| ```makebook -g or --generate-config``` | create a ```makebook-config.py``` configuration file |
| ```makebook build``` | build a book out of Jupyter notebooks |

## Project layout

    makebook-config.py  # The configuration file.
    notbooks/
        ch1.ipynb       # Jupyter notebook containing text.
        ch2.ipynb
        ...             # Other notebook files.
    out/
        book.tex        # The output LaTeX file
