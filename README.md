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

## Proposed architecture

<mxfile host="www.draw.io" modified="2020-01-17T23:31:26.762Z" agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0" etag="G2wtNnQAXX-ezs7RZzNh" version="12.5.5" type="device"><diagram id="XuhPmgCMEE0XtlMNZ33W" name="Page-1">5VtRb5swEP41eWwENoT0cUu7desmReqktY80OIEOMDJOQ/brZ4INSa9pqJr2CHuJ8OHD9ufvzncHGdBJUnwVfhb+5AGLB8QKigG9GBDiEE/9loJ1JfBGWrAQUVCJ7EZwE/1lWmhp6TIKWL7TUXIeyyjbFc54mrKZ3JH5QvDVbrc5j3dHzfwFA4KbmR9D6e8okGElHbtWI79i0SI0I9uWvpP4prMW5KEf8NWWiF4O6ERwLqurpJiwuMTO4FLpfdlzt56YYKlsoxByz/kz+baY2tfTjP2aXbnfr8/G1VMe/XipF6wnK9cGARYoQHSTCxnyBU/9+LKRfhZ8mQasHMZSrabPD84zJbSV8IFJuda76y8lV6JQJrG+W41ZDrR3bVqU86WYsRcWZDjiiwWTL/Tz6h1QzGU8YVKslZ5gsS+jx915+JpDi7pfA7O60Ei/AnUboF6tKwfgr8JIspvM36x5pSxsFzg/zyrSz6Oi3ACN5CMTkhUvYwnXbhQ8TVhtsWPdXG3RX4vCLeYb2fHBsvrGUa8lR88xOeoB1DPBzpSbnUeLLtKUONg8dfrG0/OWPLUpJlHPAezdJaljYZN01DeSVuRrw1IX9cin0J/yXFaRa0fZ6o6w2dq/8NRty1bcANV99vQXzA+6SFSPIBOV9C5GtdsGqTZqlGpw/g+B32cjH+QhYH7QVe8wxs5gSe8yg7oUd5CkqKmBeTAMurrKVdvCTmMJNOxTJ2vbDIGMMMlKe3eUtQaeWpjAE5iaJVEQxGyl1txJJ0GwywgEFl1Onaujtk5ijOokepcRtwaeonpnAgtnK6E8geikg6DYlRunf4fZW+1eq055lMpm6+oX3WbrRk/3pDIMrfZkW+p5vIHY0KPoGLnkd1cJ7mJXfChMLU6c4Hbb1z240ZoNQ4+HnKdKch/z+y6QldKO1R+og0FNVkTyVquX13fl9ZC4unlRbN27WJtGqhZ8a55QNrbVynajt2kZxSMagtm+jhc3aO8S9dbAvzkU3Kh+EsJfb3XIyiM2339UUxBl2U++uHqlgrqo5nDUA92geDoOEj+fdSBmp25LrdMq1Pc3FKZVXScrem5FYQTElzJblp5nHsWdKFkB1NADdpiQJgFAqrHgEpgDuB0Bpnq59fdBACSbPIPS6N24BVAaRtk6hZaIjZRNsaGCL/VkITuHE3nG7j4WJ/gpyVDk3QPKxGZ4QNnQRQGUTisIsdu+JkaNQcwswRekw2yNR1NzIqDT0sGtHgxNweBu686B4oFScsfbBYQza2iNvAMlhE1rykSkcGNicPS6Amn97R/qlz0EOmzJkkwNDSPLj7aG93TSqtn8GatKxpt/tNHLfw==</diagram></mxfile>

