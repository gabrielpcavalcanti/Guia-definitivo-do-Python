"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: 
• O número digitado ao quadrado 
• A raiz quadrada número digitado
"""

num = int(input("Digite um número: "))

if num >= 0:
    num_quad = num ** 2
    raiz = num ** (1/2)
    print()
    print("O número {} ao quadrado é {}".format(num,num_quad))
    print(f'A raiz do número {num} é: {raiz}')

else:
    print("Digite um número positivo.")

