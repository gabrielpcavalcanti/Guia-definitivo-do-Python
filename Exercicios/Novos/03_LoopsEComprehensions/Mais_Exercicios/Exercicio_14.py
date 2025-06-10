"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais 
e os escreva na tela. 
"""

vector: list[float] = []
vector_equal: list[float] = []

for _ in range(10):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

for val in vector:
    if vector.count(val) != 1:
        vector_equal.append(val)
    else:
        continue

print(f'Os elementos repetidos são: {set(vector_equal)}')
