"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, 
imprima o numero ao quadrado.
"""

num = float(input("Digite um número real: "))

if num >= 0:
    raiz = num ** (1/2)
    print()
    print(f'A raiz do número {num} é: {raiz}') 

else:
    num_quad = num ** 2
    print()
    print("O número {} ao quadrado é {}".format(num,num_quad))

