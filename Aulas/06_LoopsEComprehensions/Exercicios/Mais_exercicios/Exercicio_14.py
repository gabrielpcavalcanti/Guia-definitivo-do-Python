"""
Em Matemática, o número harmonico designado por H(n) define-se como sendo a soma 
da série harmonica: 
H(n) = 1 + 1/2 + 1/3 + ... + 1/n 
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n). 
"""

num: int = int(input("Digite um número inteiro: "))
sumation: float = 0

for i in range(1, num +1):
    termo: float = 1 / i
    sumation += termo

print("O valor de H(n) é {:.2f}".format(sumation))
