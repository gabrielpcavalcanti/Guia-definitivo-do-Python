"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

lista_nums_1 = []
lista_nums_2 = []
lista_intercalados = []

for i in range(10):
    nums_1 = int(input("Digite um número: "))
    lista_nums_1.append(nums_1)

for j in range(10):
    nums_2 = int(input("Digite um número: "))
    lista_nums_2.append(nums_2)

lista_nums = lista_nums_1 + lista_nums_2

print(lista_nums_1)
print(lista_nums_2)
print(lista_nums)
print(lista_intercalados)

# Não terminei