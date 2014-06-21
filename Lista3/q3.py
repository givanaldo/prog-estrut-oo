# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 3

# definindo configuração inicial
popA = 80000 # População do país A
taxa_popA = 0.03 # 3% - taxa anual de crescimento do país A
popB = 200000 # População do país B
taxa_popB = 0.015 # 1,5% - taxa anual de crescimento do país B

# simular o crescimento populacional até que a população A seja maior ou igual à população B
anos = 0
while popA < popB:
    popA += popA * taxa_popA
    popB += popB * taxa_popB
    anos += 1

# exibindo o resultado
print('População A: %d' % popA)
print('População B: %d' % popB)
print('Tempo para A superar ou igualar B: %d anos' % anos)