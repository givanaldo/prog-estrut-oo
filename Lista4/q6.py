# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 6

# entrada do número para converter para romanos (máximo: 2013)
num_decimal = int(input("Número em decimal: "))

# criação de listas de correspondências "decimal --> romano"
decimais = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanos = ['M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']

# conversão de decimal para romano. Faz-se a divisão inteira para definir o número de repetições
# de cada correspondente romano.
num_romano = ""
for i in range(len(decimais)):
    count = int(num_decimal // decimais[i])
    num_romano += romanos[i] * count
    num_decimal = int(num_decimal % decimais[i])

# exibição do resultado
print("Número em romano: %s" % num_romano)
