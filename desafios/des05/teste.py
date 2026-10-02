def somar(a, b):
    return a + b

def dividir(a, b):
    return a / b

def test_soma():
    assert somar(2, 3) == 5

def test_divisao():
    assert dividir(10, 2) == 5
    

test_divisao()
test_soma()