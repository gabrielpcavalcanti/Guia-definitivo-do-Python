"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem 
valores negativos.  
"""

vector: list[int] = []

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    if value >= 0:
        vector.append(value)

    elif value < 0:
        value = 0
        vector.append(value)

    else:
        continue

print(vector)
