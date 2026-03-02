"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união
entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não
deve conter números repetidos.
"""

vector_01: list[int] = []
vector_02: list[int] = []
union: list[int] = []

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

union= list(set(vector_01).union(set(vector_02)))

print(f'A intersecção é {union}')
