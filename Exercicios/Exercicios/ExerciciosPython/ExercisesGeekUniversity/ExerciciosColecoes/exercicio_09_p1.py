"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores 
lidos na ordem inversa. 
 """

lista_num = []
lista_inversa = []

while True:

    num = int(input("Digite um número par: "))

    if num % 2 == 0:
        lista_num.append(num)
    else:
        continue

    if len(lista_num) == 6:
        break

for k in range(1,7):

    lista_inversa.append(lista_num[-k])

print(lista_inversa)
