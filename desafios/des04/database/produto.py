import json
from pathlib import Path

arquivo = Path(__file__).resolve().parent / 'produtos.json'

def salvar_produto(produto):
    dicionario = {'nome':produto.nome, 'preco': produto.preco, 'estoque': produto.estoque}

    with open(arquivo, 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    for p in dados:
        if dicionario['nome'] == p['nome']:
            print(f'{produto} já adicionado')
            break
    else:
        dados.append(dicionario)

    with open(arquivo, 'w', encoding='utf-8') as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)
        

def estoque_produto(produto):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        dados = json.load(arq)
        for p in dados:
            if p['nome'] == produto:
                return int(p['estoque'])
        else:
            print(f'{produto} não foi encontrado na lista')


def preco_produto(produto):
    with open(arquivo, 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for p in dados:
                if p['nome'] == produto:
                    return p['preco']
            else:
                print(f'{produto} não foi encontrado na lista')

def diminuir_estoque(produto, quantidade):
    if quantidade >= 0:
        with open(arquivo, 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for p in dados:
                if p['nome'] == produto:
                    if quantidade < p['estoque']:
                            p['estoque'] = p['estoque'] - quantidade
                            with open(arquivo, 'w', encoding='utf-8') as arq:
                                json.dump(dados, arq, indent=4, ensure_ascii=False)
                                break
            else:
                print(f'{produto} não foi encontrado na lista')

def definir_estoque(produto, quantidade: int):
    if quantidade >= 0:
        with open(arquivo, 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for p in dados:
                if p['nome'] == produto:
                    if quantidade > p['estoque']:
                        p['estoque'] = quantidade
                    with open(arquivo, 'w', encoding='utf-8') as arq:
                        json.dump(dados, arq, indent=4, ensure_ascii=False)
                        break
            else:
                print(f'{produto} não foi encontrado na lista')


def mostrar_produtos():
    with open(arquivo, 'r', encoding='utf-8') as arq:
        produtos = json.load(arq)

    print('Produtos disponiveis:')
    print()
    for valor in produtos:
        print(f'{valor['nome']} - R${valor['preco']:.2f} - Estoque: {valor['estoque']}')
    print()
   