altura = float(input("Digite sua altura: "))

peso_ideal_Homens = (72.7*altura) - 58
peso_ideal_Mulheres = (62.1*altura) - 44.7

print()
print("Peso ideal para homens é: {:.2f} Kg".format(peso_ideal_Homens))
print("Peso ideal para Mulheres é: {:.2f} Kg".format(peso_ideal_Mulheres))