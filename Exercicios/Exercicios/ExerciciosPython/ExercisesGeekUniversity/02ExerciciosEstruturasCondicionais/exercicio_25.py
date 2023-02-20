"""
Calcule as raízes da equação de 2° grau. 
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não 
é equação de segundo grau". 
• Se delta < 0, não existe real. Imprima a mensagem Não existe raiz. 
• Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única. 
• Se delta >= 0, imprima as duas raízes reais. 
"""

print("Calculo das raizes da equação de segundo grau")
print("ax² + bx + c")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if c == 0:
    print()
    print(f"equação escolhida: {a}x² + {b}x")
else:
    print()
    print(f"equação escolhida: {a}x² + {b}x + {c}")

print()

if a == 0:
    print("Não existe raiz")

elif delta == 0:
    x = -b / 2 
    print(f"A raiz é {x}")
    print("Raiz única")

elif delta >= 0:
    x1 = (-b + (delta ** (1/2))) / (2*a)
    x2 = (-b - (delta ** (1/2))) / (2*a)
    print(f"As raizes são {x1} e {x2}")

elif delta < 0:
    print("Não existe raiz")

