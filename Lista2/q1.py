# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 1

# entrada dos lados do triângulo (a, b e c)
a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

# regras para definir o tipo do triângulo
if (a > b + c) or (b > a + c) or (c > a + b):
  print('Não pode ser um triângulo, pois um dos lados é maior que a soma dos outros.')
elif a == b == c:
  print ('O triângulo é Equilátero.')
elif a == b or b == c or a == c:
  print ('O triângulo é Isósceles.')
else:
  print ('O triângulo é Escaleno.')
