"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 *i)%(i + 1), sendo 
i a posição do elemento no vetor. Em seguida imprima o vetor na tela. 
"""

vector: list[int] = []

for i in range(50):
    vector.append((i + 5*i) % (i + 1))

print(vector)
