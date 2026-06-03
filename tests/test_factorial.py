import pytest
from factorial import factorial

def test_factorial_pos():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_large():
    assert factorial(10) == 3628800
    assert factorial(15) == 1307675368000
    assert factorial(20) == 2432902008176640000

def test_float():
    with pytest.raises(TypeError):
        factorial(5.5)

def test_string():
    with pytest.raises(TypeError):
        factorial("5")
        
def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)
        