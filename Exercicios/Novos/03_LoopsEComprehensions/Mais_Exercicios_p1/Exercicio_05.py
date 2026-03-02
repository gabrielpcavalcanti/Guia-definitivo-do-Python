"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. 
"""

vector: list[int] = []

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

even: list[int] = list(filter(lambda x: x % 2 == 0, vector))

print(f'Os valores são: {even}')
print(f'A quantidade de números pares é: {len(even)}')
      