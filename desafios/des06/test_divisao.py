import pytest

def dividir(a, b):
    return a / b

def test_divisao():
    with pytest.raises(ZeroDivisionError):
        dividir(10,0)
