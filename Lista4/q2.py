# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 2

# módulo para gerar números aleatórios
import random

# gera 20 números aleatório entre 1 e 100 e adiciona em uma lista
lista = []
for i in range(20):
    lista.append(random.randint(1,100))

print(lista)

# separar os números pares e ímpares em listas distintas
par = []
impar = []
for x in lista:
    if x%2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(par)
print(impar)
