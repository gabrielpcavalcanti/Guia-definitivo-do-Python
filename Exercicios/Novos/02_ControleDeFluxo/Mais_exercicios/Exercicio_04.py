"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número 
inválido". Se o número for positivo, calcular o logaritmo deste número. 
"""

import math  # Será tratado em aulas futuras.
import os

num: int = int(input("Digite um número inteiro: "))

if num > 0:
    log = math.log(num,10)
    print(f'O logarítimo do número {num} é {log}')

else:
    print("Número inválido.")
