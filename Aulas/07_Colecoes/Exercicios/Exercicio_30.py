"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números que
estão em ambos os vetores. Não deve conter números repetidos
"""

vector_01: list[int] = []
vector_02: list[int] = []
intersection: list[int] = []

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

intersection = list(set(vector_01).intersection(set(vector_02)))

print(f'A intersecção é {intersection}')
