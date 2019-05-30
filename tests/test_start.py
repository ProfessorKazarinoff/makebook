# test_start.py

from makebook import mb


def test_always_pass():
    assert True


def test_always_fail():
    assert False


def test_makebook_mb_function():
    out = mb()
    assert out == "makebook function"
