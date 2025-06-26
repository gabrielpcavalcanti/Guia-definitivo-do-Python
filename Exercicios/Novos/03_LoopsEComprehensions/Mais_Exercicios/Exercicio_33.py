"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as
posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser
movidos uma posição para trás no vetor.
"""

vector_01: list[int] = []
vector_02: list[int] = []
compactado: list[int] = []


print("Digite os valores do primeiro vetor: \n")

for _ in range(15):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()

for i in range(15):
    if vector_01[i] != 0:
        compactado.append(vector_01[i])

print(compactado)
