# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 9

# entrada da quilometragem percorrida e dos dias de aluguel do carro
km = float(input('Quilômetros percorridos: '))
dias = int(input('Dias de aluguel: '))

# cálculo do preço a ser pago e exibição
preco = 60*dias + 0.15*km
print('Valor a ser pago: R$ %.2f' % preco)
