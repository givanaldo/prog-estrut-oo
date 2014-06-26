# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 10

# Fazendo uma regra de três:
# 10 min   -- 1 cigarro
# 1440 min -- x cigarros (1 dia = 24 horas = 1440 minutos)
# ==> 144 cigarros tiram 1 dia de vida de um fumante

# entrada da quantidade de cigarros por dia e o anos fumados
cigarros = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Quantos anos já fumou: '))

# números de cigarros fumados ao longo dos anos de fumante
total_cigarros = (anos * 365) * cigarros

# cálculo dos dias perdidos e exibição
dias_perdidos = total_cigarros / 144
print('Você perdeu aproximadamente %d dias' % dias_perdidos)

# Calcular na forma ano/dias
anos = dias_perdidos // 365
dias = dias_perdidos % 365
print('Você perdeu aproximadamente %d ano(s) e %d dia(s)' % (anos, dias))
