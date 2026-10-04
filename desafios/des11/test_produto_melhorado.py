from produto import Produto
import pytest

@pytest.fixture
def produto():
    return Produto('Notebook', 3500, 15)

@pytest.fixture
def produto_sem_estoque():
    return Produto('Mouse', 100, 0)

def test_nome(produto):
    assert produto.nome == 'Notebook'

def test_estoque(produto):
    assert produto.estoque == 15

def test_sem_estoque(produto_sem_estoque):
    assert produto_sem_estoque.estoque == 0

def test_preco_negativo():
    with pytest.raises(ValueError):
        Produto('Fone', -40, 1)

def test_estoque_negativo():
    with pytest.raises(ValueError):
        Produto('Teclado', 100, -10)
