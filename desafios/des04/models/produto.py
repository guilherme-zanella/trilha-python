class Produto:

    def __init__(self, nome: str, preco: float, estoque:int):
        if nome.strip() == None:
            raise ValueError('O nome não pode ser vazio!')
        if preco < 0:
            raise ValueError('O preço do produto não pode ser negativo!')
        if estoque < 0:
            raise ValueError('O estoque não pode ser negativo!')

        self.nome = nome.strip().lower()
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f} - Estoque: {self.estoque}'