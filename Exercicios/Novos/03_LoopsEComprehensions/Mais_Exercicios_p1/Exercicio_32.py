"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não
informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso
abaixo:

- Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
- Produto entre x e y: multiplicação de cada elemento de x como elemento da mesma posição em y.
- Diferença entre x e y: todos os elementos de x que não existam em y.
- Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.
- União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.

"""

vector_01: list[int] = []
vector_02: list[int] = []
sum_vectors: list[int] = []
dot_product: list[int] = []

print("Digite os valores do primeiro vetor: \n")

while len(vector_01) != 5:

    value: int = int(input("Digite um valor inteiro: "))
    
    if value in vector_01:
        print("Valor repetido. Digite outro valor.")
        continue
    else:
        vector_01.append(value)

print()

print("Digite os valores do segundo vetor: \n")

while len(vector_02) != 5:

    value: int = int(input("Digite um valor inteiro: "))
    
    if value in vector_02:
        print("Valor repetido. Digite outro valor.")
        continue
    else:
        vector_02.append(value)

print()

print("Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y")

for i in range(5):

    sum_vectors.append(vector_01[i] + vector_02[i])

print(f'{sum_vectors}\n')

print("Produto entre x e y: multiplicação de cada elemento de x como elemento da mesma posição em y.")

for i in range(5):

    dot_product.append(vector_01[i] * vector_02[i])

print(f'{dot_product}\n')

print("Diferença entre x e y: todos os elementos de x que não existam em y.")

print(f'{list(set(vector_01).difference(set(vector_02)))}\n')

print("Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.")

print(f'{list(set(vector_01).intersection(set(vector_02)))}\n')

print("União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.")

print(f'{list(set(vector_01).union(set(vector_02)))}\n')
