from services.produto import criar_produto, vender_produto, mostrar_produtos, definir_estoque

def main():
    while True:
        print()
        print(' Loja '.center(30, '='))
        print()

        print('''Opções:
[ 1 ] Criar produto
[ 2 ] Ver produtos
[ 3 ] Vender produtos
[ 4 ] Mudar estoque
[ 5 ] Sair''')
        try:
            opcao = int(input('Qual sua opção? '))
        except ValueError:
            print('Erro! Digite um número válido')
            continue

        match opcao:
            case 1:
                nome = str(input('Nome: '))
                preco = float(input('Preço: '))
                estoque = int(input('Estoque: '))

                criar_produto(nome, preco, estoque)

            case 2:
                mostrar_produtos()

            case 3:
                produto = str(input('Qual produto será vendido? ')).strip().lower()
                quantidade = int(input('Qual será a quantidade vendida? '))
                vender_produto(produto, quantidade)

            case 4:
                produto = str(input('Nome do produto: ')).strip().lower()
                estoque = int(input('Estoque: '))
                definir_estoque(produto, estoque)

            case 5:
                break


if __name__ == '__main__':
    main()