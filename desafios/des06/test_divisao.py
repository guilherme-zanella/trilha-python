def dividir(a, b):
    return a / b

def test_divisao():
    assert dividir(10, 0) == ZeroDivisionError

test_divisao()