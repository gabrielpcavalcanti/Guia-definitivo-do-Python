"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule 
e imprima a média geral.
"""

vector: list[int] = []

for _ in range(15):
    value: int = int(input("Digite um valor inteiro: "))

    vector.append(value)

print(sum(vector) / len(vector))
