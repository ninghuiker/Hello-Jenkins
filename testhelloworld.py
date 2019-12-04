import pytest
from helloworld.py import *

def test_hello():
    result = hello()
    assert result == "Hello!"
