"""
Leia um número fornecido pelo usuário. Se o número for positivo, calcule a raiz quadrada do número. 
Se o número for negativo, mostre uma mensagem que o número é inválido.
"""

num = int(input("Digite um número inteiro: "))

if num >= 0:
    raiz = num ** (1/2)
    print()
    print(f'A raiz do número {num} é: {raiz}') 

else:
    print()
    print("Número inválido")

