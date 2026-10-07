import services.produto
from services.produto import vender_produto
import pytest
from unittest.mock import Mock

@pytest.fixture
def mocks_produtos(monkeypatch):
    estoque_mock = Mock(return_value=10)
    preco_mock = Mock(return_value=50)
    mudar_estoque_mock = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_mock)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_mock)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque_mock)

    return {
        'estoque': estoque_mock,
        'preco': preco_mock,
        'diminuir_estoque': mudar_estoque_mock
    }


@pytest.mark.parametrize(
    'quantidade',
    [
        1, 2, 5
    ]
)

def test_venda_sucedida(mocks_produtos, quantidade):
    
    resultado = vender_produto('pera', quantidade)

    assert resultado == 'Venda realizado com sucesso'
    mocks_produtos['diminuir_estoque'].assert_called_once_with('pera', quantidade)


def test_venda_invalida(mocks_produtos):

    resultado = vender_produto('pera', 100)

    assert resultado == 'Não foi possivel finalizar a venda!'
    mocks_produtos['diminuir_estoque'].assert_not_called()



def test_venda_sem_estoque(mocks_produtos, monkeypatch):

    estoque_mock = Mock(return_value=0)

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_mock)

    resultado = vender_produto('pera', 2)

    assert resultado == 'Não temos estoque desse produto'
    mocks_produtos['diminuir_estoque'].assert_not_called()


@pytest.mark.parametrize(
        'quantidades_invalidas',
        [0, -2]
)
def test_quantidades_invalidas(mocks_produtos, quantidades_invalidas):

    resultado = vender_produto('pera', quantidades_invalidas)

    assert resultado == 'Não foi possivel finalizar a venda!'
    mocks_produtos['diminuir_estoque'].assert_not_called()
    