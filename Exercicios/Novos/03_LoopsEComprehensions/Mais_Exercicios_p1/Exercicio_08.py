"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos 
na ordem inversa. 
"""

vector: list[int] = []

for _ in range(6):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

print(vector[::-1])
