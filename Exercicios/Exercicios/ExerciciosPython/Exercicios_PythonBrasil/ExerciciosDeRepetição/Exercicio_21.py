"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

while True:

    num = int(input("Digite um número inteiro: "))
    divididos = []

    if num == 1:
        print("1 não é número primo.")
        continue
    
    for i in range(1,num + 1):
        if num % i == 0:
            divididos.append(i)
    
    if len(divididos) == 2:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo")
