"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

for i in range(4):
    num = float(input("Digite uma nota: "))
    notas.append(num)

print()
print(f"Nota 1: {notas[0]}")
print(f"Nota 2: {notas[1]}")
print(f"Nota 3: {notas[2]}")
print(f"Nota 4: {notas[3]}")
print(f"média: {sum(notas) / len(notas)}")
