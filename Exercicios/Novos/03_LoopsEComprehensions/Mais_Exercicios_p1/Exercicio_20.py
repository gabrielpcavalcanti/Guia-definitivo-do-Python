"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um 
vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares 
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""

vector: list[int] = []
odd_numbers: list[int] = []

while True:

    value: int = int(input("Digite um valor inteiro: "))

    if value not in range(0,50):
        continue
    else:
        vector.append(value)

    if len(vector) == 10:
        break

odd_numbers = list(filter(lambda x: x % 2 == 1, vector))

for values_01, values_02 in zip(vector, odd_numbers):
    print(f'{values_01} {values_02}')
