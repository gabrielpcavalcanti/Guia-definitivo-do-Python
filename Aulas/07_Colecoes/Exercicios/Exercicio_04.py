"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois va- 
lores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa 
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""

vector: list[int] = []

for value in range(8):
    val: int = int(input("Digite um número inteiro: "))

    vector.append(val)

value_01: int = int(input("Digite um número de 1 a 8: "))
x: int = vector[value_01 - 1]
value_02: int = int(input("Digite um número de 1 a 8: "))
y: int = vector[value_02 - 1]

print(f'A soma de {x} com {y} é {x + y}')
