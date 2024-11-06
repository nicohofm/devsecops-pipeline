import pytest
from app1 import hello


def test_hello():
    assert hello == "Hello, DevSecOps!"