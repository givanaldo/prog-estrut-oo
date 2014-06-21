# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 5

# entrada do preço da mercadoria e do desconto a ser dado
preco_mercadoria = float(input('Preço da mercadoria: '))
porcentagem = float(input('Porcentagem de desconto: '))

# cálculo do desconto e do novo preço da mercadoria
desconto = preco_mercadoria * (porcentagem/100)
novo_preco = preco_mercadoria - desconto

# exibição do valor de desconto e do preço a pagar
print('Desconto: R$ %.2f' % desconto)
print('Preço a pagar: R$ %.2f' % novo_preco)
