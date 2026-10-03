import pytest

def calcular_media(a, b):
    if a < 0 or b < 0:
        raise ValueError('Os números não podem ser negativos!')

    return (a + b) / 2

def test_media():
    assert calcular_media(10, 6) == 8

def test_media_zero():
    assert calcular_media(0, 10) == 5

def test_media_erro():
    with pytest.raises(ValueError):
        calcular_media(-5, 10)
