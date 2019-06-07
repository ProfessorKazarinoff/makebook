# test_utils.py

from makebook import get_version
from datetime import datetime


def test_get_version():
    v = get_version()
    y_str = str(datetime.today().year)
    assert type(v) == type("2019.06.06")
    assert v.startswith(y_str)
    assert v.split(".")[0] == y_str
