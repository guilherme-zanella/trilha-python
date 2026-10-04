class Produto:

    def __init__(self, nome, preco, estoque):
        if preco < 0:
            raise ValueError
        if estoque < 0:
            raise ValueError

        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        