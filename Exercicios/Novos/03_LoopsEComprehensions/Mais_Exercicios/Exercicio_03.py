"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das 
componentes deste vetor, armazenando o em outro vetor. Os conjuntos têm 
10 elementos cada. Imprimir todos os conjuntos. 
"""

vector: list[int] = []

for value in range(10):
    val: int = int(input("Digite um número inteiro: "))

    vector.append(val)
    
print(vector)

vector_02: list[float] = list(map(lambda x: x**2, vector))

print(vector_02)
