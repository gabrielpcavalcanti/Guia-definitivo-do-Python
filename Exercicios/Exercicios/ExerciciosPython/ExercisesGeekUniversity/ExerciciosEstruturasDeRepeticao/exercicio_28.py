"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, 
conforme a fórmula a seguir:
E = 1 + 1/1! + 1/2! +1/3! + + I/N!
"""

from math import factorial as fac
soma = 0

num = int(input("Digite um número: "))

for i in range(0, num):
    termo = 1 / (fac(i))
    soma += termo

print("O valore de E é : {:.2f}".format(soma))
