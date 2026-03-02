"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos 
juntamente com o maior, o menor e a média dos valores. 
"""

vector: list[float] = []

for _ in range(5):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

print(vector)
print(f'O maior valor é {max(vector)}')
print(f'O menor valor é {min(vector)}')
print(f'A média dos valores é {sum(vector) / len(vector)}')
