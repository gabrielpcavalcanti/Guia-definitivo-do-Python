"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

vetor = [ 1, 2, 3, 4 ,5]

print(vetor)

# Outro jeito 

lista_num = []

while True:
    num = float(input("Digte um número:"))
    lista_num.append(num)

    if len(lista_num) == 5:
        print(lista_num)
        break
    
