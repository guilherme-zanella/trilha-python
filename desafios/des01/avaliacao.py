class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f'{self.nome} custa {self.preco} e temos {self.estoque} no estoque'


class ListaProdutos:
    def __init__(self, lista: list):
        self.produtos =lista

    def mostar_produtos(self):
        conteudo = '-'*30
        for p in self.produtos:
            conteudo += f'\n{p.nome} (R${p.preco:.2f}): {p.estoque} no estoque'
        conteudo += '\n'
        conteudo += '-'* 30
        print(conteudo)

    def adicionar_produto(self, produto):
        if produto not in self.produtos:
            self.produtos.append(produto)
        else:
            print(f'{produto} já adicionado na lista')

    def procurar_produto(self, produto: str):
        for p in self.produtos:
            if produto == p.nome:
                print(f'{p.nome} (R${p.preco}): {p.estoque} no estoque')
                break
        else:
            print(f'{produto} não foi encontrado na lista')

    def altera_estoque(self, produto, estoque):
        for p in self.produtos:
            if produto == p.nome:
                p.estoque = estoque
                break
        else:
            print(f'{produto} não encontrado na lista')

    def total(self):
        total = 0
        for p in self.produtos:
            total += p.preco * p.estoque

        print(f'O valor total dos produtos é: R${total:.2f}')



produtos = [
    Produto('Notebook', 2500, 8),
    Produto('Mouse', 100, 20),
    Produto('Teclado', 150, 15)
]

l = ListaProdutos(produtos)
l.adicionar_produto(Produto('Fone', 200, 5))
l.mostar_produtos()
l.altera_estoque('Fone', 30)
l.procurar_produto('Fone')
l.total()
