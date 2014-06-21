# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 2

# entrada do ano a saber se é bissexto ou não
ano = int(input('Ano: '))

# regra para saber se o ano em questão é bissexto ou não
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print('O ano %d é bissexto.' % ano)
else:
  print('O ano %d não é bissexto.' % ano)
