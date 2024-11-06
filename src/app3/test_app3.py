import pytest
from app3 import check_password


def test_valid_password():
    assert check_password("1234") == True


def test_invalid_password():
    assert check_password("wrongPassword") == False
