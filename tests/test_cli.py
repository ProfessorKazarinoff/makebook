# test_start.py

from makebook import cli_main

def func():
    pass

def test_cli_main():
    assert type(cli_main) == type(func)
