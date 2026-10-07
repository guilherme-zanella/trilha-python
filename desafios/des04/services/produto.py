from models.produto import Produto
from database.produto import *

def criar_produto(nome, preco, estoque):
    p = Produto(nome, preco, estoque)
    salvar_produto(p)

def vender_produto(produto, quantidade: int):
    estoque = estoque_produto(produto)
    if estoque:
        if estoque >= quantidade and quantidade > 0:
            diminuir_estoque(produto, quantidade)
            print()
            print(f'Venda realizada!')
            print()

            print(f'Produto: {produto}')
            print(f'Quantidade: {quantidade}')

            preco = preco_produto(produto) * quantidade
            print(f'Valor da venda: R${preco:.2f}')

            print(f'Estoque restante: {estoque}')
            return f'Venda realizado com sucesso'
        else:
            print('Não foi possível finalizar a venda!')
            return f'Não foi possivel finalizar a venda!'
    else:
        print(f'Não temos estoque desse produto!')
        return f'Não temos estoque desse produto'
