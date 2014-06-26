# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 7

# entrada do valor da conta e do valor pago, desprezando os centavos
# Ou seja, as entradas são de números inteiros
conta = int(input('Valor da conta: '))
pagamento = int(input('Valor do pagamento: '))

# Notas disponíveis: 50, 20, 10, 5, 2, 1
troco = pagamento - conta
print("Troco: R$ %d" % troco)
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    quantidade_notas = troco // nota
    if quantidade_notas != 0:
        print("   -- %d nota(s) de %d" % (quantidade_notas, nota))
    troco = troco % nota
