# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 6

# entrada do número que deseja saber se é triangular
num = int(input('Entre com o número: '))
é_triangular = False

for i in range(3, num+1):
    if (i-2)*(i-1)*i == num:
        print("O número %d é triangular, pois %d x %d x %d = %d" % (num, i-2, i-1, i, num))
        é_triangular = True
        break

if é_triangular == False:
    print('O número %d não é triangular.')
