# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 4

# entrada dos números a ser calculado o MDC
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    dividendo = num1
    divisor = num2
else:
    dividendo = num2
    divisor = num1

while divisor != 0:
    temp = divisor
    divisor = dividendo % divisor
    dividendo = temp

print("O MDC entre %d e %d é %d" % (num1, num2, dividendo))

# Pseudocódigo do Algoritmo de Euclides
'''
AlgoritmoDeEuclides(a: inteiro; b: inteiro): inteiro

variáveis
   divisor: inteiro
   dividendo: inteiro
   c: inteiro
início

   se b > a então
   início
     dividendo = b
     divisor = a
   senão
     dividendo = a
     divisor = b
   fim-se

   enquanto resto(dividendo/divisor) ≠ 0
   início
      c = resto(dividendo/divisor)
      dividendo = divisor
      divisor = c
   fim-enquanto

   AlgoritmoDeEuclides = divisor
fim-função
'''