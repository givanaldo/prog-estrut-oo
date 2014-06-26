# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 2 - Questão 7

# Se 1 litro pinta 3 metros quadrados, então uma lata (18 litros) pinta 54 metros quadrados

# entrada da área a ser pintada
# o comando chr(178) retorna o "elevado a dois (²)" como string
area_pintada = float(input('Área a ser pintada (m' + chr(178) + '): '))

# testa se a divisão é inteira pelo número de latas
if area_pintada % 54 == 0:
  num_latas = area_pintada // 54
else:
  num_latas = (area_pintada // 54) + 1

# calcula o valor da compra
valor_compra = num_latas * 80

# exibe os resultados
print('Quantidade de latas: %d' % num_latas)
print('Preço total: R$ %.2f' % valor_compra)
