# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 8

# entrada do número que deseja saber se é primo
num = int(input('Digite um número: '))

# Um número é primo se é divisível apenas por ele mesmo e por 1.
# Só faz sentido testar da metade do número para trás, pois acima já se tem certeza
# que não é divisível, além dele mesmo, é claro.
é_primo = True
for i in range(2, num//2):
    if num%i == 0: # encontrou um divisor diferente de 1 e o próprio número
        é_primo = False
        break  # não faz sentido continuar, já que o número não é primo.
# exibição do resultado
if é_primo == True:
    print("O número %d é primo." % num)
else:
    print("O número %d não é primo." % num)