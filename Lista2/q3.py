# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 3

# entrada do peso dos peixes
peso = float(input('Peso dos peixes (Kg): '))

# cálculo do excesso e da multa
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

# exibição dos resultados
print ('Multa de R$ %.2f' % multa)
print ('Excesso: %.2f Kg' % excesso)
