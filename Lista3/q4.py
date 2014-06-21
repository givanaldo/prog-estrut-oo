# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 4

# entrada do número para o qual o número de Fibonacci será exibido
termo = int(input('Digite o n-ésimo termo de Fibonacci: '))

# cálculo do n-ésimo termo informado pelo usuário
if termo == 1 or termo == 2:
    print('F(%d) = 1' % termo)
else:
    i = 2
    x = y = 1
    z = 0
    while i < termo:
        i = i + 1
        z = x + y
        x, y = y, z
    print('F(%d) = %d' % (termo, z))
