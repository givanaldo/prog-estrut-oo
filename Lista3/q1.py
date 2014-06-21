# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 1

numero = -1
while numero < 0.0 or numero > 10.0:
    numero = float(input("Digite uma nota: "))
    if numero < 0.0 or numero > 10.0:
        print("Número inválido. Digite entre 0 e 10.")
print("OK")
