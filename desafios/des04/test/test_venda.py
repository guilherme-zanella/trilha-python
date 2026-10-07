import services.produto
from services.produto import vender_produto
import pytest
from unittest.mock import Mock

def test_vender_produto(monkeypatch):

    estoque_fake = Mock(return_value=10)

    preco_fake = Mock(return_value=50)

    mudar_estoque = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_fake)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_fake)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque)

    vender_produto('pera', 2)

    mudar_estoque.assert_called_once_with('pera', 2)

def test_venda_sucedida(monkeypatch):
    estoque_fake = Mock(return_value=10)
    
    preco_fake = Mock(return_value=50)

    mudar_estoque = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_fake)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_fake)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque)

    assert vender_produto('pera', 2) == 'Venda realizado com sucesso'

def test_venda_invalida(monkeypatch):
    estoque_fake = Mock(return_value=10)
    
    preco_fake = Mock(return_value=50)

    mudar_estoque = Mock()

    monkeypatch.setattr(services.produto, 'estoque_produto', estoque_fake)
    monkeypatch.setattr(services.produto, 'preco_produto', preco_fake)
    monkeypatch.setattr(services.produto, 'diminuir_estoque', mudar_estoque)

    assert vender_produto('pera', 100) == 'Não foi possivel finalizar a venda!'
    mudar_estoque.assert_not_called()

