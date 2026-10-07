import services.produto
from services.produto import vender_produto
import pytest
from unittest.mock import Mock

@pytest.mark.parametrize(
    'quantidade',
    [
        1, 2, 5
    ]
)

def test_venda_sucedida(monkeypatch, quantidade):

    estoque_mock = Mock(return_value=10)

    preco_mock = Mock(return_value=50)

    mudar_estoque_mock = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_mock)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_mock)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque_mock)
    
    resultado = vender_produto('pera', quantidade)

    assert resultado == 'Venda realizado com sucesso'
    mudar_estoque_mock.assert_called_once_with('pera', quantidade)


def test_venda_invalida(monkeypatch):
    estoque_mock = Mock(return_value=10)
    
    preco_mock = Mock(return_value=50)

    mudar_estoque_mock = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_mock)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_mock)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque_mock)

    assert vender_produto('pera', 100) == 'Não foi possivel finalizar a venda!'
    mudar_estoque_mock.assert_not_called()

