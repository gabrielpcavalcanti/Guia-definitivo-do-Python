"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

num_01: float = float(input("Digite um número: "))
num_02: float = float(input("Digite um número: "))
num_03: float = float(input("Digite um número: "))

if num_01 > num_02 and num_01 > num_03 and num_02 > num_03:
    print(f"{num_03} {num_02} {num_01} ")

elif num_01 > num_02 and num_01 > num_03 and num_03 > num_02:
    print(f"{num_03} {num_01} {num_02} ")

elif num_02 > num_01 and num_02 > num_03 and num_01 > num_03:
    print(f"{num_03} {num_01} {num_02} ")

elif num_02 > num_01 and num_02 > num_03 and num_03 > num_01:
    print(f"{num_01} {num_03} {num_02} ")

elif num_03 > num_01 and num_03 > num_02 and num_02 > num_01:
    print(f"{num_01} {num_02} {num_03} ")

elif num_03 > num_01 and num_03 > num_02 and num_01 > num_02:
    print(f"{num_01} {num_03} {num_02} ")
