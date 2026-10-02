import pytest

def soma(a, b):
    return a + b

def dividir(a, b):
    return a / b

def test_soma():
    assert soma(1, 1) == 2

def test_divisao():
    assert dividir(10, 2) == 5

def test_divisao_error():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)