# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 14

# a soma dos impostos dá 40%. Assim, o valor final do automóvel é o valor sem impostos somado com 40%
# Assim, valor_final = valor_sem_impostos + 0.4 * valor_sem_impostos

# entrada do valor de venda do automóvel
valor_venda = float(input('Valor de venda do automóvel: '))

# cálculo do valor do automóvel sem impostos
valor_sem_impostos = valor_venda / 1.4

# impressão dos resultados
print('ICMS: R$ %.2f' % (valor_sem_impostos * 0.18)) # ICMS é 18%
print('IPI: R$ %.2f' % (valor_sem_impostos * 0.13)) # ICMS é 13%
print('PIS: R$ %.2f' % (valor_sem_impostos * 0.014)) # ICMS é 1,4%
print('Cofins: R$ %.2f' % (valor_sem_impostos * 0.076)) # ICMS é 7,6%
print('Valor sem impostos: R$ %.2f' % valor_sem_impostos) # valor do automóvel sem os 40%