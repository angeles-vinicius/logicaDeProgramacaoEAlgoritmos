print('Bem Vindo ao Controle de Estoque da Mercearia do Angeles Vinicius RU: 150002\n')


# Função 1: cadastrarProduto
def cadastrarProduto(codigo):
    nome = input('Por favor, entre com o NOME do Produto: ')
    fabricante = input('Por favor, entre com o FABRICANTE do Produto: ')
    valor = float(input('Por favor, entre com o VALOR (R$) do Produto: '))

    return nome, fabricante, valor


# Função 2: ConsultarProduto
def consultarProduto(codigo, nome, fabricante, valor):
    # Loop para exibir as opções e executar operações até que se escolha a opção Retornar
    while True:
        print('Escolha a opção desejada:')
        print('1-Consultar Todas os Produtos')
        print('2-Consultar Produtos por Código')
        print('3-Consultar Produtos por Fabricante')
        print('4-Retornar')
        opcao = int(input('>> '))
        n = len(codigo)

        if (opcao == 1):
            print('-------------------------')
            for i in range(n):
                print('Codigo: {}'.format(codigo[i]))
                print('Nome: {}'.format(nome[i]))
                print('Fabricante: {}'.format(fabricante[i]))
                print('Valor: R$ {:.2f}'.format(valor[i]))
            print('------------------------')

        elif (opcao == 2):
            produtoProcurado = int(input('Digite o CODIGO do Produto: '))
            # Encontrar posição relacionada ao código de interesse
            contador = 0
            for i in range(n):
                if (produtoProcurado == codigo[i]):
                    contador += 1
                    print('------------------------')
                    print('Codigo: {}'.format(codigo[i]))
                    print('Nome: {}'.format(nome[i]))
                    print('Fabricante: {}'.format(fabricante[i]))
                    print('Valor: R$ {:.2f}'.format(valor[i]))
                    print('------------------------')
                    break
            if (contador == 0):
                print('Codigo não cadastrado.')

        elif (opcao == 3):
            produtoProcurado = input('Digite o FABRICANTE do Produto: ')
            # Encontrar posições relacionadas ao fabricante de interesse
            contador = 0
            print('--------------------')
            for i in range(n):
                if (produtoProcurado == fabricante[i]):
                    contador += 1
                    print('Codigo: {}'.format(codigo[i]))
                    print('Nome: {}'.format(nome[i]))
                    print('Fabricante: {}'.format(fabricante[i]))
                    print('Valor: R$ {:.2f}'.format(valor[i]))
                print('--------------------')
                if (contador == 0):
                    print('Fabricante não cadastrado.')
        elif (opcao == 4):
            break

        else:
            continue

        # Função removerProduto


def removerProduto():
    CodigoRemover = int(input('Digite o codigo do Produto a ser removida: '))
    CodigoRemover -= 1

    # Remover valores relacionados ao código informado em todas as listas
    del (codigo[CodigoRemover])
    del (nome[CodigoRemover])
    del (fabricante[CodigoRemover])
    del (valor[CodigoRemover])


# Inicializando variáveis principais
contador = 0
codigo = []
nome = []
fabricante = []
valor = []

# Loop para exibir as opções e executar operações até que se escolha a opção Sair
while True:
    print('Escolha a opção desejada:')
    print('1-Cadastrar Produto')
    print('2-Consultar Produto(s)')
    print('3-Remover Produto')
    print('4-Sair')
    option = int(input('>> '))

    if (option == 1):
        print('Você selecionou a opção de cadastrar Produto(s)')
        contador += 1
        print('Código do Produto(s): 00{}'.format(contador))
        novoNome, novoFabricante, novoValor = cadastrarProduto(contador)
        # Insere as novas informações à lista já existente
        codigo.append(contador)
        nome.append(novoNome)
        fabricante.append(novoFabricante)
        valor.append(novoValor)

    elif (option == 2):
        print('Você selecionou a opção de consultar Produto(s)')
        consultarProduto(codigo, nome, fabricante, valor)
    elif (option == 3):
        print('Você selecionou a opção de remover Produto(s)')
        removerProduto()
    elif (option == 4):
        print('Obrigado pela preferência!')
        break
    else:
        print('Opção inválida')
        continue