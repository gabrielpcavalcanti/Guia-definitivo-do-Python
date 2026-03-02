"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela 
a seguir, verifique e mostra qual a classificação dessa pessoa. 

    Altura                                  Peso 
                  Até 60           Entre 60 e 90 (Inclusive)       Acima de 90 
Menor que 1,20    A                         D                          G
De 1,20 a 1,70    B                         E                          H
Maior que 1 ,70   C                         F                          I
"""

altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso em Kg: "))

if altura < 1.2 and peso <= 60:
    print("A")

elif altura >= 1.2 and altura < 1.7 and peso <= 60:
    print("B")

elif altura >= 1.7 and peso <= 60:
    print("C")

elif altura < 1.2 and peso >= 60 and peso <= 90:
    print("D")

elif altura >= 1.2 and altura < 1.7 and peso >= 60 and peso <= 90:
    print("E")

elif altura >= 1.7 and peso >= 60 and peso <= 90:
    print("F")

elif altura < 1.2 and peso > 90:
    print("G")

elif altura >= 1.2 and altura < 1.7 and peso > 90:
    print("H")

elif altura >= 1.7 and peso > 90:
    print("I")

else:
    print("Valor inválido")

