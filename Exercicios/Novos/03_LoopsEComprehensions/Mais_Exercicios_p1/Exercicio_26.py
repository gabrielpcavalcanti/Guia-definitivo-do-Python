"""
Faça um programa que calcule o desvio padrão de um vetor contendo 10 números.
"""

vector_01: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()

mean: float = sum(vector_01) / len(vector_01)

step_01: list = list(map(lambda x: (x - mean)**2, vector_01))

standard_deviation: float = ((1/9) * sum(step_01))**(1/2)

print(f'O desvio padrão é {standard_deviation:.2f}')
