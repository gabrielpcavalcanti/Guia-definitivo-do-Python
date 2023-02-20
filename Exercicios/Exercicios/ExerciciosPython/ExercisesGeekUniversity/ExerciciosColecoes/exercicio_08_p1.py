"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos 
na ordem inversa. 
"""

lista_num = []
lista_inversa = []

for i in range(6):

    num = int(input("Digite um número: "))
    lista_num.append(num)

for k in range(1,7):

    lista_inversa.append(lista_num[-k])

print(lista_inversa)
