"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá 
ser impresso o maior e o menor elemento do vetor. 
"""

lista_num = []

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

maximo = max(lista_num)
minimo = min(lista_num)

print(f"Maior elemento {maximo}")
print((f"Maior elemento {minimo}"))
