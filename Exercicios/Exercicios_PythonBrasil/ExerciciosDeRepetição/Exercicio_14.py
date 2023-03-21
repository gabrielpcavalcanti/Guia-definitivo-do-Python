"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
num_3 = float(input("Digite um número: "))
num_4 = float(input("Digite um número: "))
num_5 = float(input("Digite um número: "))
num_6 = float(input("Digite um número: "))
num_7 = float(input("Digite um número: "))
num_8 = float(input("Digite um número: "))
num_9 = float(input("Digite um número: "))
num_10 = float(input("Digite um número: "))

pares = 0
impares = 0

lista = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]

for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print("A quantidade de numeros pares é: {} \nA quantidade de núemros ímpares é: {}".format(pares,impares))

