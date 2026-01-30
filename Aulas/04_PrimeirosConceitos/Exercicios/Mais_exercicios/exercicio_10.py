"""
Leia o valor do raio de um circulo e imprima a área do circulo.
A área do circulo é: A = PI * R**2, sendo PI = 3.141592.
"""

PI = 3.141592

radious: float = float(input("Digite o raio do circulo: "))

print(f'A área do circulo é {PI * radious**2}')
