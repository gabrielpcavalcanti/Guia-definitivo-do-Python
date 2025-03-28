"""
Escreva um programa para calcular o valor da série, para 5 termos. 
s = 0 + 1/2! + 2/4! + 3/6! + ... .
"""

from math import factorial as fac
soma = 0
c = 0

for i in range(5):
    if i % 2 == 0:
        termo = c / (fac(i))
        soma += termo
        c += 1
        continue
    else:
        continue

print("O valore de s é : {:.2f}".format(soma))
