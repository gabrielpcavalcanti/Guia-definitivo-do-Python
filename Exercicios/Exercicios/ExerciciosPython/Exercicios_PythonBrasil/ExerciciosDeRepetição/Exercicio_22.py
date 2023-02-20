"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""

while True:

    num = int(input("Digite um número inteiro: "))
    divisores = []

    if num == 1:
        print("1 não é número primo.")
        continue
    
    for i in range(1,num + 1):
        if num % i == 0:
            divisores.append(i)
    
    if len(divisores) == 2:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo, mas os divisores são:")
        print(divisores)
