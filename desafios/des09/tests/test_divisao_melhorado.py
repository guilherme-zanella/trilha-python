import pytest

def dividir(a, b):
    return a / b

@pytest.mark.parametrize(
    'a, b, resultado',
    [
        (10, 2, 5),
        (20, 4, 5),
        (9, 3, 3)
    ]
)
def test_divisao(a,b,resultado):
    assert dividir(a,b) == resultado
    