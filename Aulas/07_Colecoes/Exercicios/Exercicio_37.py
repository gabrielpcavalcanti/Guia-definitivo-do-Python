"""
Considere um vetor A com 11 elementos onde Al < A2 < --- < A6 > A7 > A8 >
... > A11, ou seja, está ordenado em ordem crescente até o sexto elemento, e a partir
desse elemento está ordenado em ordem decrescente. Dado o vetor da questão anterior,
proponha um algoritmo para ordenar os elementos.
"""

vector_01_06: list[float] = []
vector_07_11: list[float] = []


print("Digite os valores do primeiro vetor: \n")

for _ in range(6):
    value: float = float(input("Digite um valor inteiro: "))

    vector_01_06.append(value)

for _ in range(5):
    value: float = float(input("Digite um valor inteiro: "))

    vector_07_11.append(value)

vector_01_06.sort()
vector_07_11.sort(reverse=True)

print(vector_01_06 + vector_07_11)
