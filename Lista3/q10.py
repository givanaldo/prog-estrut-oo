# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 10

# entrada do inteiro positivo
num = int(input("Digite o número: "))

# usando fatiamento em strings para inverter o número e convertendo novamente em inteiro
num_str = str(num)
num_contrario = int(num_str[::-1])
print("Exibição invertida: %d" % num_contrario)