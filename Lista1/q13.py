# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 13

# entrada da largura e do comprimentos da sala
largura = float(input('Largura da sala em metros: '))
comprimento = float(input('Comprimento da sala em metros: '))

# cálculo da área da sala em metros quadrados
area = largura * comprimento

# cálculo da potência necessária, sabendo que 1 metro quadrado necessita de 18 W
potencia = area * 18

# cálculo da quantidade de lâmpadas, sabendo que temos apenas lâmpadas de 100W
# testa se temos a quantidade exata de lâmpadas de acordo com a potência
if potencia % 100 == 0:
    num_lampadas = potencia // 100
else: # precisa de mais uma lâmpada
    num_lampadas = (potencia // 100) + 1

# exibe o resultado
# o comando chr(178) retorna o "elevado a dois (²)" como string
print("Para iluminar uma sala de %.2fm x %.2fm (%.2fm%s) são necessários %.2fW, ou seja, %d lâmpadas de 100W." % (largura, comprimento, area, chr(178), potencia, num_lampadas))