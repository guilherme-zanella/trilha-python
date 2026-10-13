from services.produto import criar_produto
import services.produto
import pytest
from unittest.mock import Mock

def test_criar_produto(monkeypatch):

    salvar_produto_mock = Mock()

    monkeypatch.setattr(services.produto, 'salvar_produto', salvar_produto_mock)

    criar_produto('Notebook', 3500, 10)

    salvar_produto_mock.assert_called_once()

    produto = salvar_produto_mock.call_args.args[0]

    assert produto.nome == 'notebook'
    assert produto.preco == 3500
    assert produto.estoque == 10
