"""
Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de concersão é D = R * 180 / PI, sendo R o ângulo em radianos e D o ângulo em graus e PI = 3.14.
"""

PI = 3.14

R = float(input("Digite o ângulo em radianos: "))

D = R * 180 / PI

print("O ângulo em graus é: {:.2f}".format(D))
