"""
Faça um programa que calcule e escreva o valor de S

S = 1/1 + 3/2 + 5/3 + 7/4 ··· 99/50
"""

sum: float = 0
numerator: int = 1
denomenator: int = 1

for i in range(50):
    sum += numerator / denomenator

    numerator += 2
    denomenator += 1

print(f'O valor de S é {sum:.2f}')
