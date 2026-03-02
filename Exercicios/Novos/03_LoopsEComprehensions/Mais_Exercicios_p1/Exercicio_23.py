"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto
escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar, sendo que o produto escalar é dado por: x1 *y1 + x2 *y2 + ... + xn *yn.
"""

vector_01: list[int] = []
vector_02: list[int] = []
vector_03: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(5):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()
print("Digite os valores do segundo vetor: \n")

for _ in range(5):
    value: int = int(input("Digite um valor inteiro: "))

    vector_02.append(value)

print()

for i in range(5):

    vector_03.append(vector_01[i] * vector_02[i])
    
print(vector_01)
print(vector_02)
print(f'O produto escalar entre o vetor 1 e o vetor 2 é: {sum(vector_03)}.')
