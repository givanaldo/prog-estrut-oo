# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 8

# entrada do número a ser decomposto em fatores primos
num = int(input('Digite um número: '))

# decomposição em fatores primos
fatores = []
quociente = num
fator = 2
while quociente != 1:
    if quociente % fator == 0:
        quociente /= fator
        fatores.append(fator)
    else:
        fator += 1

print("%d =" % num, end=" ")
for i in range(len(fatores)):
    print("%d" % fatores[i], end=" ")
    if i != len(fatores)-1:
        print("x", end=" ")

multiplicidade = 1
print("\n%d =" % num, end=" ")
for i in range(len(fatores)):
    if i == 0 or multiplicidade == 1:
        print("%d^" % fatores[i], end="")
    if i!= 0 and fatores[i] == fatores[i-1]:
        multiplicidade += 1
    else:
        print("%d" % multiplicidade, end=" ")
        multiplicidade = 1
        if i != len(fatores)-1:
            print("x", end=" ")
