"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando ele- 
mentos repetidos. 
"""

vector: list[float] = []

for _ in range(20):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

print(set(vector))
