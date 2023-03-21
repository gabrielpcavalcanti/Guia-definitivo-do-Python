tamanho = float(input("Qual o tamho da área a ser pintada: "))

lata_tinta = tamanho / 54

preco = lata_tinta * 80

print()
print("A qunatidade de lata de tintas é: {:.2f}".format(lata_tinta))
print("O preço a ser pago é: {:.2f}".format(preco))

