ganha_hora = int(input("Digite quanto vc ganha por hora: "))
numero_hora = float(input("Digite quantas horas horas trabalhou o mês: "))

salario_Bruto = ganha_hora * numero_hora
ir = 0.11 * salario_Bruto
inss = 0.08 * salario_Bruto
sindicato = 0.05 * salario_Bruto
salario_liquido = salario_Bruto - ir - inss - sindicato

#Letra A
print()
print("Letra a:")
print("O seu salário bruto é: {:.2f}".format(salario_Bruto))

#Letra B
print()
print("Letra b:")
print("Quanto pagou ao innss: {:.2f}".format(inss))

#Letra C
print()
print("Letra c:")
print("Quanto pagou ao sindicato: {:.2f}".format(sindicato))

#Letra D
print()
print("Letra d:")
print("O seu inposto de renda é: {:.2f}".format(ir))

#Letra E
print()
print("Letra e:")
print("O seu salário líquido: {:.2f}".format(salario_liquido))

