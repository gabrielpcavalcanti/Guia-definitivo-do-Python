"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e 
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um 
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser 
informado ao usuário e o programa termina.
"""

grade_01: float = float(input("Digite a primeira nota: "))
grade_02: float = float(input("Digite a segunda nota: "))

media: float = (grade_01 + grade_02) / 2
    
print()

if 0 <= grade_01 <= 10 and 0 <= grade_02 <=10:
    print(f'A média das notas é {media}')

else:
    print("Valor inválido.")
