# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 1

nota = -1
while nota < 0.0 or nota > 10.0:
    nota = float(input("Digite uma nota: "))
    if nota < 0.0 or nota > 10.0:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

print("Nota válida: %.1f" % nota)
