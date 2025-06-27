"""
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores ímpares de v para v1, e os valores pares de v para v2. Note que cada
um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são
utilizados. No final escreva os elementos UTILIZADOS de v1 e v2.
"""

vector_v: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(10):
    value: int = int(input("Digite um valor inteiro: "))

    vector_v.append(value)

print(f'Elementos pares do vetor v: {list(filter(lambda x: x % 2 == 0, vector_v))}')
print(f'Elementos impares do vetor v: {list(filter(lambda x: x % 2 != 0, vector_v))}')
