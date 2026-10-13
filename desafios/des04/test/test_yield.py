import pytest


class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


@pytest.fixture
def produto():
    produto = Produto('Notebook', 3500, 10)

    yield produto

    produto.estoque = 0


def test_produto(produto):
    assert produto.estoque == 10