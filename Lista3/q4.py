# -*- coding: cp1252 -*-
#n-ésimo termo de Fibonacci

termo = input("Digite o n-ésimo termo de Fibonacci: ")
if (termo == 1 or termo == 2):
    print("F(%d) = 1" % termo)
else:
    i = 2
    x = y = 1
    z = 0
    while (i < termo):
        i = i + 1
        z = x + y
        x, y = y, z
    print("F(%d) = %d\n" % (termo, z))
