# -*- coding: cp1252 -*-
# Sequ�ncia de Fibonacci

termo = input("Digite o n-�simo termo de Fibonacci: ")
print("Sequ�ncia de Fibonnaci at� o n-�simo termo: ")
if termo == 1:
    print("1")
elif termo == 2:
    print("1 1")
else:
    i = 2
    x = y = 1
    z = 0
    print("1  1 "),
    while (i < termo):
        i = i + 1
        z = x + y
        x, y = y, z
        print("%d " % z),
