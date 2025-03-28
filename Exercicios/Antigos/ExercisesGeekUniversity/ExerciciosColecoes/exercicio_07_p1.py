"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima 
o vetor, o maior elemento e a posição que ele se encontra. 
"""

lista_num = []

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

print(lista_num)

maximo = max(lista_num)

print(max(lista_num))

print(lista_num.index(maximo))
