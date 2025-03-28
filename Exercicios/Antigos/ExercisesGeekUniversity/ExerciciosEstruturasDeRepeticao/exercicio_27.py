"""
Em Matemática, o número harmonico designado por H(n) define-se como sendo a soma 
da série harmonica: 
H(n) = 1 + 1/2 + 1/3 + ... + 1/n 
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n). 
"""

num = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, num +1):
    termo = 1 / i
    soma += termo

print("O valor de H(n) é {:.2f}".format(soma))
