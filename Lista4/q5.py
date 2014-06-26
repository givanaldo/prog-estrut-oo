# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 4 - Questão 5

# copiei e colei o texto da lista aqui
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

# exibição do texto original
print("Texto original:")
print("%s\n" % texto)

# conversão do texto para letras minúsculas
texto = texto.lower()

# retirada das pontuações do texto. Troca a pontuação por vazio.
for c in ".,:":
    texto = texto.replace(c, "")

# exibição do texto sem pontuações e em letras minúsculas
print("Texto sem pontuações e em letras minúsculas:")
print("%s\n" % texto)

# separação das palavras dos texto em uma lista. Cada palavra é um elemento da lista
lista = texto.split()

# separação das palavras que possuem umas das letras da palavra 'python' e que tenham mais de 4 caracteres
resposta = []
for palavra in lista:
    if len(palavra) > 4:        
        for letra in palavra:
            if letra in 'python':
                resposta.append(palavra)
                break

# exibição da quantidade de palavras encontradas que seguem a regra
print("Foram encontradas %d palavras:" % len(resposta))

# exibição das palavras
for x in resposta:
    print("- %s" % x),


