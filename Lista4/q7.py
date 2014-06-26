# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 7

# entrada do número de termos
n = int(input("Número de termos para o cálculo de %s: " % chr(960)))

# ordem do termo (1, 2, 3, ..., n)
k = 1
# denominador para a divisão (1, 3, 5, 7, 9, ...)
denominador = 1

# cálculo do valor de PI para n termos
valor_pi = 0
while k <= n:
    # termo ímpar, então SOMA
    if k % 2 == 1:
        valor_pi = valor_pi + 4/denominador
    # termo par, então SUBTRAI
    else:
        valor_pi = valor_pi - 4/denominador
    k = k + 1
    denominador = denominador + 2

# exibição do resultado. Quanto maior o valor de n, mais próximo o valor de PI será de 3,1416.
print("Valor aproximado de %s = %.4f" % (chr(960), valor_pi))