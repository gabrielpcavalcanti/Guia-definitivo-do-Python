peso = float(input("Digite o valor do peso dos peixes: "))

execesso = peso - 50
multa = execesso * 4

print()
print("O valor do execesso é: {:.2f} kg".format(execesso))
print("O valor da multa é: R$ {:.2f} ".format(multa))


