print('Bem-Vindo ao Programa de Feijoada do Angeles Vinicius RU: 150002\n')


# Função 1: volumeFeijoada
def volumeFeijoada():
    # Loop para verificar se o volume atende ao intervalo válido
    while True:
        print('Menu Volume Feijoada')
        # Loop para verificar se a entrada é numérica
        while True:
            try:  # Try para evitar erro quando o usuário digitar um valor não numérico
                volume = float(input('Entre com a quantidade que deseja (ml): '))
            except ValueError:
                print('Foi inserido um valor não numérico')
                print('Por favor, entre com o volume novamente')
                continue
            break
            # Verifica se o volume esta dentro da faixa com a qual o restaurante trabalha
        if 300 <= volume <= 5000:
            valor = volume * 0.08
        else:
            print('Não aceitamos porções menores do que 300ml ou maiores do que 5l. Tente novamente!')
            continue
        break
    return valor


# Função 2: opcaoFeijoada
def opcaoFeijoada():
    # Loop para verificar se a opção informada é válida
    while True:
        print('Menu Opção Feijoada')
        print('Entre com a opção de Feijoada: ')
        print('b- Básica (Feijão + paiol + costelinha)')
        print('p- Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s- Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
        opcao = input('>> ')

        # Estrutura if, elif e else para definir multiplicador
        if (opcao == 'b'):
            multiplicador = 1.00
        elif (opcao == 'p'):
            multiplicador = 1.25
        elif (opcao == 's'):
            multiplicador = 1.50
        else:
            print('Você não digitou uma opção válida.')
            continue
        break

    return multiplicador


# Função 3: acompanhamentoFeijoada
def acompanhamentoFeijoada():  # Armazena o total do valor adicional
    adicional = 0  # Loop para verificar se a opção informada é válida
    while True:
        print('Deseja mais algum acompanhamento?: ')
        print('0- não desejo mais acompanhamentos (encerrar pedido)')
        print('1- 200g de arroz')
        print('2- 150g de farofa especial')
        print('3- 100g de couve cozida')
        print('4- 1 laranja descascada')
        acompanhamento = int(input('>> '))

        # Estrutura if, elif e else aplicadas às condicões fornecidas pela tabela
        if (acompanhamento == 0):
            break
        elif (acompanhamento == 1):
            adicional += 5
            continue
        elif (acompanhamento == 2):
            adicional += 6
            continue
        elif (acompanhamento == 3):
            adicional += 7
            continue
        elif (acompanhamento == 4):
            adicional += 3
            continue
        else:
            print('Você não digitou uma opção válida')
            continue
    return adicional


# Execuções das funções para armazenar saidas
volume = volumeFeijoada()
opcao = opcaoFeijoada()
adicional = acompanhamentoFeijoada()

# Calcula e mostra o valor total
total = (volume * opcao) + adicional
print('O valor a ser pago é (R$): {:.2f} (volume = {:.2f} * opção = {:.2f} + acompanhamento = {:.2f})'.format(total,
                                                                                                              volume,
                                                                                                              opcao,
                                                                                                              adicional))
print('Obrigado pela preferência!')