"""
Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 
em 1000, imprimindo Seu valor na tela, até que Seu valor seja 100.000 (cem mil).
"""

num: int = 0

while num < 100_000:

    print(num + 1000)
    num += 1000
