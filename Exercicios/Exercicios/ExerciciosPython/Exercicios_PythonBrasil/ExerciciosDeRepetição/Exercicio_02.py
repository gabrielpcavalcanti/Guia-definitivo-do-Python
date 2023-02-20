"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome_usuário = str(input("Digite o seu usuário: "))
senha = str(input("Digite a sua senha: "))

while nome_usuário == senha:
    print("Erro, usuário igual a senha")
    nome_usuário = str(input("Digite o seu usuário: "))
    senha = str(input("Digite a sua senha: "))

# Outra forma 


while True:

    nome_usuario = input("Usuário: ")
    senha = input("Senha: ")

    if nome_usuario == senha:
        print("Erro. Escolha um nome diferente ou uma senha difetente.")
        continue
    else:
        print("Usuário e senha aceitos.")
        break