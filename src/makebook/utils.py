# utils.py


def get_version():
    return "2019.06.05"


import re

from pandocfilters import toJSONFilter, applyJSONFilters, RawInline


def convert_link(key, val, fmt, meta):
    if key == "Link":
        target = val[2][0]
        # Links to other notebooks
        m = re.match(r"(\d+\-.+)\.ipynb$", target)
        if m:
            return RawInline("tex", "Chapter \\ref{sec:%s}" % m.group(1))

        # Links to sections of this or other notebooks
        m = re.match(r"(\d+\-.+\.ipynb)?#(.+)$", target)
        if m:
            # pandoc automatically makes labels for headings.
            label = m.group(2).lower()
            label = re.sub(r"[^\w-]+", "", label)  # Strip HTML entities
            return RawInline("tex", "Section \\ref{%s}" % label)

    # Other elements will be returned unchanged.


def convert_links(source):
    return applyJSONFilters([convert_link], source)
