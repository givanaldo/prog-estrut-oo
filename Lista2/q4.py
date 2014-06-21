# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 4

# entrada dos 3 números
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

# definição do maior número
if num1 >= num2 and num1 >= num3:
    print('Maior: %d' % num1)
elif num2 >= num3:
    print('Maior: %d' % num2)
else:
    print('Maior: %d' % num3)

