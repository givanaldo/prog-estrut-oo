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

print(fatores)