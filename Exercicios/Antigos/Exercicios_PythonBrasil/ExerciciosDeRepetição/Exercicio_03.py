"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = str(input("Digite seu nome: ").upper())
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = str(input("Digite seu sexo. M para masculuno e F para feminimo: ").upper())
    estado_Civil = str(input("Digite seu estado civil (s para solteiro, c para casado, v para viuvo e d para divoeciado): ").upper())

    if len(nome) <= 3:
        print("O nome está errado")
        continue
    elif idade < 0 or idade > 150:
        print("A idade está errada")
        continue
    elif salario < 0:
        print("O salário está errado")
        continue
    elif sexo != "F" and sexo != "M":
        print("Sexo inválido")
        continue
    elif estado_Civil != "S" and estado_Civil != "C" and estado_Civil != "V" and estado_Civil != "D":
        print("Estado civil inválido")
        continue
    else:
        print("Todos os dados estão corretos")
        break