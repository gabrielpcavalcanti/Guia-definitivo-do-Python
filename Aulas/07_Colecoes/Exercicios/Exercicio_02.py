"""
Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela ou valores lidos.
"""

# While
cont: int = 6
values: list[int] = []

while cont > 0:
    value: int = int(input("Digite um valor inteiro: "))

    values.append(value)

    cont -= 1

print(values)

# For
lista_num = []

for i in range(6):

    num = int(input("Digite um número: "))
    lista_num.append(num)

print(lista_num)
