import pytest

class Produto:

    def __init__(self, nome, preco, estoque):
        if preco < 0:
            raise ValueError
        if estoque < 0:
            raise ValueError

        self.nome = nome
        self.preco = preco
        self.estoque = estoque


@pytest.fixture
def produto():
    return Produto('Notebook', 3500, 10)


@pytest.fixture
def produto_sem_estoque():
    return Produto('Mouse', 80, 0)


def test_nome(produto):
    assert produto.nome == 'Notebook'

def test_estoque(produto):
    assert produto.estoque == 10

def test_estoque_zero(produto_sem_estoque):
    assert produto_sem_estoque.estoque == 0
    