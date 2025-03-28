"""
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 
5, mas não simultaneamente pelos dois. 
"""

num= int(input("Digite um número inteiro: "))

div_3 = num % 3

div_5 = num % 5

print()

if (div_3 == 0 or div_5 == 0) and (div_5 == 0 and not div_3 == 0 or not div_5 == 0 and div_3 == 0) :
    print(f"O número {num} é dividivel por 3 ou por 5, mas não pelos dois ao mesmo tempo.")

