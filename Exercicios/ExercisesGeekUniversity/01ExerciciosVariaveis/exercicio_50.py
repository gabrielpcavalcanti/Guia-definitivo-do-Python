"""
Implemente um programa que calcula o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
"""

age = int(input("Digite sua idade: "))
year = int(input("Digite o ano atual: "))

born = year - age

print("O ano de nascimento é: {}".format(born))
