"""
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 
5, mas não simultaneamente pelos dois. 
"""

num = int(input("Digite um número inteiro: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("O número é divisível por 3 e 5 simultaneamente.")

elif (num % 3 == 0) or (num % 5 == 0):
    print("O número é divisível por 3 ou 5, mas não pelos dois.")

else:
    print("O número não é divisível nem por 3 nem por 5.")
