import addition
import pytest

def test_add():
    assert addition.add(3,6) == 9

def test_sub():
    assert addition.sub(5,2) == 3
