"""
Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses
valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
final na tela os valores em ordem.
"""

vector_01: list[float] = []

print("Digite os valores do primeiro vetor: \n")

for _ in range(10):
    value: float = float(input("Digite um valor inteiro: "))

    vector_01.append(value)

    vector_01.sort()

    print(vector_01)

print(vector_01)
