"""
Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor ordenado.
"""

vector_01: list[float] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(10):
    value: float = float(input("Digite um valor inteiro: "))

    vector_01.append(value)

vector_01.sort()

print(vector_01)
