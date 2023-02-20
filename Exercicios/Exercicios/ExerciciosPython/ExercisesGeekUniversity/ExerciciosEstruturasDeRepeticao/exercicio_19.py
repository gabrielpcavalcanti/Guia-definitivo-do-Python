"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saida 
cada um dos algarismos que compõem o número.
"""

while True:
    num = int(input("Digite um número inteiro entre 100 e 999: "))

    num_str = str(num)

    if num >= 100 and num <= 999:
        for i in num_str:
            print(i)
        break
    else:
        print("Número digitado inválido")
        continue
