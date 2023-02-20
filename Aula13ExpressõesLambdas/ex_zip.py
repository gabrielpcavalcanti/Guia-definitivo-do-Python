x = int(input())

lista_0 = [num for num in range(x )]
lista_1 = [num for num in range(1, x )]
lista_final = []

print(lista_0)
print(lista_1)

for i, j in zip(lista_1, lista_0):
    n = 3 * i - j
    lista_final.append(n)

print(lista_final)