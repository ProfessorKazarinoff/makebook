# test_start.py

from makebook import mb, copy_all_images_to_dir

def test_always_pass():
    assert True


def test_always_fail():
    assert False


def test_makebook_mb_function():
    out = mb()
    assert out == "makebook function"

def test_copy_all_images_to_dir():
    assert False
