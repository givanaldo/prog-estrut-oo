# Disciplina: Programação Estruturada e Orientada a Objetos
# Professor: Givanaldo Rocha
# Lista 3 - Questão 2

# entrada do usuário
usuario = input('Usuário: ')

# entrada da senha até que a mesma seja diferente do nome do usuário
senha = usuario
while senha == usuario:
    senha = input('Senha: ')
    if senha == usuario:
        print('A senha não pode ser igual ao nome de usuário. Entre com a senha novamente!!!')

print('Usuário e senha registrados com sucesso.')
print('Usuário: %s ### Senha: %s' % (usuario, senha))