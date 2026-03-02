"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a 
quantidade de números negativos e a soma dos números positivos desse vetor. 
"""

vector: list[float] = []

for _ in range(10):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

print(f'Quantidade números negativos: {len(list(filter(lambda x: x<0, vector)))}')
print(f'Soma dos números positivos: {sum(list(filter(lambda x: x>=0, vector)))}')
