# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 1 - Questão 6

# entrada da distância a percorrer e da velocidade média
distancia = float(input('Distância a percorrer (Km): '))
velocidade = float(input('Velocidade média (Km/h): '))

# cálculo do tempo e exibição do mesmo
tempo = distancia / velocidade
print ('Tempo aproximado da viagem: %.1f hora(s)' % tempo)
