# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 9

# entrada do número a ser decomposto em fatores primos
num = int(input('Digite um número: '))

# decomposição em fatores primos sem as multiplicidades
fatores = []
quociente = num
fator = 2
while quociente != 1:
    if quociente % fator == 0:
        quociente /= fator
        fatores.append(fator)
    else:
        fator += 1

# exibição do resultado
print("%d =" % num, end=" ")
for i in range(len(fatores)):
    print("%d" % fatores[i], end=" ")
    if i != len(fatores)-1:
        print("x", end=" ")

###########################################################
###########################################################
# decomposição em fatores primos com as multiplicidades
fatores = []
multiplicidades = []
quociente = num
indice = 0
multiplicidade = 0
fator = 2
while quociente != 1:
    if quociente % fator == 0:
        quociente /= fator
        if multiplicidade == 0:
            fatores.append(fator)
            multiplicidade += 1
            multiplicidades.append(multiplicidade)
        else:
            multiplicidade += 1
            multiplicidades[indice] = multiplicidade
    else:
        fator += 1
        indice = len(fatores)
        multiplicidade = 0

# exibição do resultado
print("\n%d =" % num, end=" ")
for i in range(len(fatores)):
    print("%d**%d" % (fatores[i], multiplicidades[i]), end=" ")
    if i != len(fatores)-1:
        print("x", end=" ")

