# -*- coding: cp1252 -*-
n1 = input("Digite o primeiro n�mero: ")
n2 = input("Digite o segundo n�mero: ")

if n1 > n2:
    dividendo = n1
    divisor = n2
else:
    dividendo = n2
    divisor = n1

while divisor != 0:
    temp = divisor
    divisor = dividendo % divisor
    dividendo = temp

print("O MDC entre %d e %d � %d" % (n1, n2, dividendo))
