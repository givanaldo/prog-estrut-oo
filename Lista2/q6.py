# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 6

# entrada do ganho por hora e do número de horas trabalhadas
valor_hora = float(input('Valor por hora trabalhada: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))

# cálculo do salário e dos valores dos impostos
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

# exibição dos resultados
print('+ Salário Bruto: R$ %.2f' % salario_bruto)
print('- IR: R$ %.2f' % ir)
print('- INSS: R$ %.2f' % inss)
print('- Sindicato: R$ %.2f' % sindicato)
print('= Salário Líquido: R$ %.2f' % salario_liquido)

