"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do segundo.
"""

vector_01: list[int] = []
vector_02: list[int] = []
vector_03: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()
print("Digite os valores do segundo vetor: \n")

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector_02.append(value)

print()

for i in range(10):

    vector_03.append(vector_01[i])
    vector_03.append(vector_02[i])

print(vector_03)
