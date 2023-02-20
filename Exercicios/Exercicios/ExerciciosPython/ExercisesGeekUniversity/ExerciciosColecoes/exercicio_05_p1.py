"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. 
"""

lista_num = []
pares = 0

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

for k in lista_num:

    if k % 2 == 0:
        pares += 1
    else:
        continue

print(pares)
