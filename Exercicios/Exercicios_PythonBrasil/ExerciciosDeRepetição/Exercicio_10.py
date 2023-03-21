"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite um número inteiro: "))

lista = []

for i in range(num_1 + 1, num_2, 1):
    if num_1 < num_2:
        lista.append(i)
    else:
        print("intervalo inválido")
        break

print(lista)

# Outra forma

while True:

    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))

    for num in range(num1 + 1, num2):
        print("{}".format(num), end=' ') 
        
    break

