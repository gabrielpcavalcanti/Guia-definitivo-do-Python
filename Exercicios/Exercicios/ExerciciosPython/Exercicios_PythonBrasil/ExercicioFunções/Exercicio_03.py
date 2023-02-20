"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""

# primeira maneira 

def soma(num1,num2,num3):
    print(num1 + num2 + num3)


soma(1,2,4)

# segunda maneira

def soma_segunda_maneira(num1,num2,num3):
    return num1 + num2 + num3


print(soma_segunda_maneira(1,2,4))

# terceira maneira

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

def soma_tres():
    soma = num1 + num2 + num3
    return soma


print(soma_tres())

