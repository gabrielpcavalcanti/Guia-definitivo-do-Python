"""
Leia quatro notas, calcule a média aritimética e imprima o resultado.
"""

test_1 = float(input("Digite a primeira nota: "))
test_2 = float(input("Digite a segunda nota: "))
test_3 = float(input("Digite a terceira nota: "))
test_4 = float(input("Digite a quarta nota: "))

mean = (test_1 + test_2 + test_3 + test_4) / 4

print(f'A média aritimética é: {mean}')
