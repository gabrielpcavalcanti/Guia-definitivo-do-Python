"""
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor.
"""

vector_01: list[int] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(5):
    value: int = int(input("Digite um valor inteiro: "))

    vector_01.append(value)

print()

primos = []
posicoes = []

for i in range(len(vector_01)):
    n = vector_01[i]
    if n < 2:
        continue
    if n == 2:
        primos.append(n)
        posicoes.append(i)
        continue
    if n % 2 == 0:
        continue
    primo = True
    for j in range(3, int(n**0.5) + 1, 2):
        if n % j == 0:
            primo = False
            break
    if primo:
        primos.append(n)
        posicoes.append(i)

print("Primos:", primos)
print("Posições:", posicoes)
