"""
b) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):**

• Homens: (72.7 * h) — 58 

• Mulheres: (62.1 * h) — 44.7

Se o valor for inválido, escreva: Sexo inválido.
"""

hight: float = float(input("Digite sua altura: "))
person_sex: str = input("Digite seu sexo (m para homens e f para mulheres): ".lower())

ideal_man_weight: float = (72.7 * hight) - 58 
ideal_woman_weight: float = (62.1 * hight) - 44.7

if person_sex == "m":
    print()
    print(f'Seu peso ideal é: {ideal_man_weight} kg.')

elif person_sex == "f":
    print()
    print(f'Seu peso ideal é: {ideal_woman_weight} kg.')

else:
    print()
    print("Sexo inválido.")
