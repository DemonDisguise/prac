# test_fibonacci.py

import pytest
from fibonacci import fibonacci


def test_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_small_values():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_large_value():
    assert fibonacci(15) == 610


def test_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_invalid_type():
    with pytest.raises(ValueError):
        fibonacci("5")