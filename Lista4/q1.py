# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 1

# módulo para gerar números aleatórios
import random

# gera 10 números aleatório entre 1 e 100 e adiciona em uma lista
lista = []
for i in range(10):
    lista.append(random.randint(1,100))

print(lista)

# a função sort() ordena os elementos de uma lista
lista.sort()

print(lista)

# exibe o primeiro elemento da lista (menor)
print("Menor: %d" % lista[0])

# exibe o último elemento da lista (maior)
print("Maior: %d" % lista[-1])
