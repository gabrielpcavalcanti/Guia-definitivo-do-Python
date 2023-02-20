"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
import math

nums = []
nums_quadrado = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    nums.append(num)
    num_quadrado = math.pow(nums[0],2)
    nums_quadrado.append(num_quadrado)

print(f"A soma dos quadrados é: {sum(nums_quadrado)}")

