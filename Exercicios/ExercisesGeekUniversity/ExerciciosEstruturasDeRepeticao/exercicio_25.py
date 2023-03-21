"""
Faga um programa que some todos os números naturais abaixo de 1000 que säo múltiplos de 3 ou 5.
"""

c = 1
soma = 0

while c < 15:
    if c % 3 == 0 or c % 5 == 0:
        soma += c
        c += 1
        continue
    else:
        c += 1
        continue

print(soma)
