# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 8 - utilizando funções

def fatorial(n):
    import math
    lista_fatoriais = []
    for i in range(1, n+1):
        lista_fatoriais.append(math.factorial(i))
    return lista_fatoriais

def fibonacci(n):
    seq = [1, 1]
    for i in range(2, n+1):
        seq.append(seq[i-1]+seq[i-2])
    return seq

def distanciaDoisPontos(x1, y1, x2, y2):
    import math
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def diaNascimento(data):
    import datetime
    semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia, mes, ano = data.split("/")
    data = datetime.date(int(ano), int(mes), int(dia))
    return semana[data.weekday()]

def trianguloPascal(n):
    lista = [[1],[1,1]]
    for i in range(1,n):
        linha = [1]
        for j in range(len(lista[i])-1):
            linha.append(lista[i][j] + lista[i][j+1])
        linha.append(1)
        lista.append(linha)
    return lista

if __name__ == "__main__":
    fatoriais = fatorial(5)
    for i in range(len(fatoriais)):
        print("Fatorial(%d) = %d" % (i+1, fatoriais[i]))

    lista_fibonacci = fibonacci(10)
    print("\nSequência de Fibonacci:"),
    for i in lista_fibonacci:
        print(i, end=" ")

    x1 = 0
    x2 = 0
    y1 = 10
    y2 = 10
    print("\n\nDistância de (%d, %d) para (%d, %d) = %.2f" % (x1, x2, y1, y2, distanciaDoisPontos(x1, x2, y1, y2)))

    data = "20/02/1998"
    print("\n%s --> nasceu no(a) %s\n" % (data, diaNascimento(data)))

    linhasPascal = trianguloPascal(5)
    for linha in linhasPascal:
        for n in linha:
            print(n, end=" ")
        print("")
