"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros 
cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados 
do vetor C. 
"""

vector_01: list[int] = []
vector_02: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(4):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()
print("Digite os valores do segundo vetor: \n")

for _ in range(4):
    value: int = int(input("Digite um valor inteiro: "))

    vector_02.append(value)

set_01: set[int] = set(vector_01)
set_02: set[int] = set(vector_02)

print()

if set_01.difference(set_02): 
    print(f'O valor do vetor C = A - B é {set_01.difference(set_02)}.')
else:
    print("O vetor é nulo.") 
