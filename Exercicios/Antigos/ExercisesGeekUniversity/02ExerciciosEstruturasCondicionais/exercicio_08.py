"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e 
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um 
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser 
informado ao usuário e o programa termina.
"""

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

if 0 <= nota_1 <= 10 and 0 <= nota_2 <=10:
    media = (nota_1 + nota_2) / 2
    print()
    print(f'A média das notas é {media}')

else:
    print()
    print("Valor inválido.")
