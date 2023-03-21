"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, 
assim como a diferença existente entre ambos.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite um número inteiro: "))

if num_1 > num_2:
    print()
    print("{} é maior que {}".format(num_1,num_2))
    print("A difrença entre eles é: {}".format(num_1 - num_2))

else:
    print()
    print("{} é maior que {}".format(num_2,num_1))
    print("A difrença entre eles é: {}".format(num_2 - num_1))

