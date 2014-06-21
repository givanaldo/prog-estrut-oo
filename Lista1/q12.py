# Disciplina: Programação Estrutura e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 12

# entrada da largura e do comprimentos da sala
largura = float(input('Largura da sala em metros: '))
comprimento = float(input('Comprimento da sala em metros: '))

# cálculo da área da sala em metros quadrados
area = largura * comprimento

# cálculo da potência necessária, sabendo que 1 metro quadrado necessita de 18 W
potencia = area * 18
print("Para iluminar uma sala de %.2fm x %.2fm (%.2fm%s) são necessários %.2fW" % (largura, comprimento, area, chr(178), potencia))