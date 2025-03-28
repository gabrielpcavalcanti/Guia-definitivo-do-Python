"""
Leia um ângulo em gruas e apresente-o convertido em radianos.
A fórmula de concersão é R = D * PI / 180, sendo R o ângulo em radianos e D o ângulo em graus e PI = 3.14.
"""

PI = 3.14

D = float(input("Digite o ângulo em graus: "))

R = D * PI / 180

print("O ângulo em radianos: {:.2f}".format(R))
