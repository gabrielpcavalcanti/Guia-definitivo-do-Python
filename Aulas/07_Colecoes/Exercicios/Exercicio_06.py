"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá 
ser impresso o maior e o menor elemento do vetor. 
"""

vector: list[int] = []

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

print(f'O maior valor é: {max(vector)}')
print(f'O menor valor é: {min(vector)}')
