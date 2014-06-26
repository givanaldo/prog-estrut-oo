# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 8

# entrada da temperatura em Fahrenheit
fahr = float(input('Temperatura em Fahrenheit: '))

# conversão para Celsius e exibição
celsius = (fahr - 32) * 5 / 9
print('%.2f em Fahrenheit corresponde a %.2f em Celsius' % (fahr, celsius))
