# test_utils.py

from makebook import get_version
from datetime import datetime


def test_get_version():
    v = get_version()
    y_str = str(datetime.today().year)
    m_str = str(datetime.today().month)
    assert v.startswith(y_str)
    assert m_str in v
    assert v.split(".")[0] == y_str
    assert v.split(".")[1] == m_str
