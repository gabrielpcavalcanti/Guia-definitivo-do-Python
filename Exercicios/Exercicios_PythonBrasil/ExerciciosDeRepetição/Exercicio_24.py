"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

while True:

    quant_notas = int(input("Digite a quantidade de notas: "))

    notas_lista = []

    for i in range(quant_notas):
        notas = float(input("Digite a nota: "))
        notas_lista.append(notas)

    print(f"A média das notas são: {sum(notas_lista) / quant_notas}")


        

