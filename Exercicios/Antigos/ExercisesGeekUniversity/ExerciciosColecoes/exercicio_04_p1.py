"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois va- 
lores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa 
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""

lista_num = []

for i in range(8):

    num = int(input("Digite um número: "))
    lista_num.append(num)

indice_x = int(input("Digite um número de 1 a 8: "))
x = lista_num[indice_x - 1]

indice_y = int(input("Digite um número de 1 a 8: "))
y = lista_num[indice_y - 1]

print(x + y)
