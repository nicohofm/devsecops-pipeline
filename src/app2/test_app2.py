import pytest
from app2 import calculation


def test_calculate():
    a = 5
    b = 6
    assert calculation(a, b) == 11