# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 4

# entrada de dados (números do tipo float)
salario = float(input('Informe o salário: '))
porcentagem = float(input('Informe a porcentagem de aumento: '))

# calculando o aumento salarial
aumento = salario * (porcentagem/100)
novo_salario = salario + aumento

# exibindo o valor do aumento e o novo salário
print('Aumento: R$ %.2f' % aumento)
print('Novo salário: R$ %.2f' % novo_salario)
