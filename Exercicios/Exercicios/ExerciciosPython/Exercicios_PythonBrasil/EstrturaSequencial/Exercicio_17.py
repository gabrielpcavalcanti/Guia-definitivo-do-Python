tamanho = float(input("Qual o tamho da área a ser pintada: "))

lata_tinta_18 = tamanho / 108
preco_18 = lata_tinta_18 * 80

lata_tinta_3p6 = tamanho / 21.6
preco_3p6 = lata_tinta_3p6 * 25

mistura = tamanho % 108
resto3p6 = mistura / 21.6


print()
print("A quantidade de latas de 18 litros: {:.2f}".format(lata_tinta_18))

print()
print("A quantidade de latas de tinta de 3.6 litros: {:.2f}".format(lata_tinta_3p6))

