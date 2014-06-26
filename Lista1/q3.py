# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 3

# entrada das informações
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

# convertendo dias, horas, minutos e segundos e exibindo o resultado em segundos.
total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print('Total em segundos: %d' % total_segundos)
