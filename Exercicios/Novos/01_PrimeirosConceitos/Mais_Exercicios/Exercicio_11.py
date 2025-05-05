"""
Leia um ângulo em gruas e apresente-o convertido em radianos e vice-versa.
A fórmula de concersão é R = D * PI / 180, sendo R o ângulo em radianos e D o ângulo em graus e PI = 3.14.
A fórmula de concersão é D = R * 180 / PI, sendo R o ângulo em radianos e D o ângulo em graus e PI = 3.14.
"""

PI: float = 3.14

angle_degres: float = float(input("Digite o ângulo em graus: "))
angle_rad: float = float(input("Digite o ângulo em radianos: "))

print(f'O ângulo em radianos é: {angle_degres * PI / 180}.')
print(f'O ângulo em graus é: {angle_rad * 180 / PI}.')
