"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima 
o vetor, o maior elemento e a posição que ele se encontra. 
"""

vector: list[int] = []

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

print(f'O maior valor é: {max(vector)} e sua posição é {vector.index(max(vector))}')
