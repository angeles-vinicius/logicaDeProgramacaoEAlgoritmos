print('Bem-Vindo a Pizzaria do Angeles Vinicius RU: 150002\n')
print('-----------------------Cardápio----------------------')
print('| Código |  Descrição  | Pizza Média | Pizza Grande |')
print('|   21   |  Napolitana |    R$ 20,00 |     R$ 26,00 |')
print('|   22   |  Margherita |    R$ 20,00 |     R$ 26,00 |')
print('|   23   |  Calabresa  |    R$ 25,00 |     R$ 32,50 |')
print('|   24   |  Toscana    |    R$ 30,00 |     R$ 39,00 |')
print('|   25   |  Portuguesa |    R$ 30,00 |     R$ 39,00 |')
print('-----------------------------------------------------\n')

# Recebe o valor da conta do cliente
total = 0
# Loop principal (Uso do while e do break)

while True:
    tamanho = input('Qual o tamanho de pizza que deseja (M/G)?: ')
    if (tamanho == 'M'):
        precos = [20, 20, 25, 30, 30]
    elif (tamanho == 'G'):
        precos = [26, 26, 32.50, 39, 39]
    else:
        # Opção inválida caso o usuário digite um numero não relacionado na tabela

        print('Opção Inválida')
        continue
        # volta para o começo do while

    codigo = int(input('Entre com o código do sabor desejado: '))  # Estrutura if, elif e else
    if (codigo == 21):
        print('Você pediu uma Pizza Napolitana')
        total += precos[0]
    elif (codigo == 22):
        print('Você pediu uma Pizza Margherita')
        total += precos[1]
    elif (codigo == 23):
        print('Você pediu uma Pizza Calabresa')
        total += precos[2]
    elif (codigo == 24):
        print('Você pediu uma Pizza Toscana')
        total += precos[3]
    elif (codigo == 25):
        print('Você pediu uma Pizza Portuguesa')
        total += precos[4]
    else:
        # Opção inválida caso o usuário digite um numero não relacionado na tabela
        print('Opção Inválida')
        continue  # volta para o começo do while

    repetir = int(input('Deseja pedir mais alguma coisa? \n1 - Sim\n0 - Não\n>> '))
    if (repetir == 1):
        continue
    else:
        # valor total do pedido
        print('O Total a ser pago é: R$ {:.2f}'.format(total))
        print('Obrigado pela preferência!')
    break 