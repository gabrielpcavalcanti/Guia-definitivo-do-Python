"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon- 
tram o maior e o menor valor. 
"""

vector: list[float] = []

for _ in range(5):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

print(vector)
print(f'A posiçãao do maior valor é {vector.index(max(vector))}')
print(f'A posição do menor valor é {vector.index(min(vector))}')
