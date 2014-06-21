# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 1


a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if (a > b + c) or (b > a + c) or (c > a + b):
  print ('N�o pode ser um tri�ngulo')
  print ('Um dos lados � maior que a soma dos outros')
elif a == b == c:
  print ('Equil�tero')
elif a == b or b == c or a == c:
  print ('Is�sceles')
else:
  print ('Escaleno')
  
