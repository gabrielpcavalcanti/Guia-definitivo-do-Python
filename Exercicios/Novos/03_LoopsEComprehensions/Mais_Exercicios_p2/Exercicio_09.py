""" 
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e 
quantas vezes o maior numero foi lido. A quantidade de números a serem lidos deve ser 
fornecida pelo usuårio.
"""

quantity: int = int(input("Digite a quantidade de números que queira ler: "))
count: int = 0
numbers: list[float] = []

print()

while count < quantity:

    value: float = float(input("Digite a um número: "))

    count += 1
    numbers.append(value)

print(f'\nO maior número digitado foi {max(numbers)} e quantidade de vez digitadas foi {numbers.count(max(numbers))}.')
