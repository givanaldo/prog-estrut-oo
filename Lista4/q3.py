# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 3

# módulo para gerar números aleatórios
import random

# gera números aleatórios entre 1 e 100 e adiciona nas duas listas
lista1 = []
lista2 = []
for i in range(10):
    lista1.append(random.randint(1,100))
    lista2.append(random.randint(1,100))

print(lista1)
print(lista2)

# cria terceira lista com os elementos das outras duas listas alternados
lista3 = []
for x in range(10):
    lista3.append(lista1[x])
    lista3.append(lista2[x])

print(lista3)
