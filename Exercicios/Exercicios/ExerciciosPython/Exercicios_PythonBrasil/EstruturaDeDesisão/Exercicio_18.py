"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

print()

# Meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 < dia < 31:
        if ano > 0:
            print("{}/{}/{}".format(dia, mes, ano))
        else:
            print("Erro")

# Meses com 30 dias
elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 < dia < 30:
        if ano > 0:
            print("{}/{}/{}".format(dia, mes, ano))
        else:
            print("Erro")
else:
    print("Não é uma data válida.")

