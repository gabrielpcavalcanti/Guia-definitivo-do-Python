"""
Faça um programa que receba 6 números inteiros e mostre:
- Os números pares digitados;
- A soma dos números pares digitados;
- Os números ímpares digitados;
- A quantidade de números ímpares digitados;
"""

vector_v: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(6):
    value: int = int(input("Digite um valor inteiro: "))

    vector_v.append(value)

even_numbers: list[int] = list(filter(lambda x: x % 2 == 0, vector_v))
odd_numbers: list[int] = list(filter(lambda x: x % 2 != 0, vector_v))

print(f'Elementos pares do vetor v: {even_numbers} e a soma é {sum(even_numbers)}')
print(f'Elementos impares do vetor v: {odd_numbers} e a soma é {sum(odd_numbers)}')
