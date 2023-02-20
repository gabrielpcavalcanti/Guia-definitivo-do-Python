"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.reverse()

print(lista)

# Outra forma

lista = []

for i in range(10):
    num = float(input("Digite um número: "))
    lista.append(num)

lista.reverse()

print(lista)



