"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número 
inválido". Se o número for positivo, calcular o logaritmo deste número. 
"""

import math

num = int(input("Digite um número: "))

if num > 0:
    log = math.log(num,10)
    print("O logarítimo do número {} é {}".format(num,log))

else:
    print("Número inválido.")

