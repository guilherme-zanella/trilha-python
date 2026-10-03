import pytest

def multiplicar(a, b):
    return a * b

@pytest.mark.parametrize(
    'a, b, resultado',
    [
        (2, 2, 4),
        (-2, 3, -6),
        (-4, -4, 16)
    ]
)
def test_multiplicacao(a,b,resultado):
    assert multiplicar(a,b) == resultado