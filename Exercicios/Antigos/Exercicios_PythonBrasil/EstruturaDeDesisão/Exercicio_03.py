"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = str(input("Digite F para feminino e M para masculino: ").upper())

print()

if sexo == 'M':
    print("Sexo Masculino")
elif sexo == 'F':
    print("Sexo Feminino")
else:
    print("Sexo inválido")