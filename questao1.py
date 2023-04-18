#O Enunciado está no README!!!!!

print('Bem vindo a loja Angeles Vinicius RU: 1550002\n')

valorOriginal = float(input('Entre com o valor do produto: R$ '))  # Entrada de valor do produto
quantidade = int(input('Entre com a quantidade do produto? '))  # Entrada de quantidade de produto

# Desconto aplicado
if 0 <= quantidade < 5:
    desconto = 0
elif 5 <= quantidade < 19:
    desconto = 0.03
elif 20 <= quantidade < 99:
    desconto = 0.06
else:
    desconto = 0.10

# Resultados
semDesconto = valorOriginal * quantidade
comDesconto = semDesconto - semDesconto * desconto

print('O valor sem desconto foi R${:.2f}'.format(semDesconto))
print('O valor com desconto foi R${:.2f}'.format(comDesconto, desconto))
print('Tenha um excelente dia...')
