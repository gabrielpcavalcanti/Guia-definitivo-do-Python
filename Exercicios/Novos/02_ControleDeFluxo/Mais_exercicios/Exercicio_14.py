"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela 
a seguir, verifique e mostra qual a classificação dessa pessoa. 

    Altura                                  Peso 
                  Até 60           Entre 60 e 90 (Inclusive)       Acima de 90 
Menor que 1,20    A                         D                          G
De 1,20 a 1,70    B                         E                          H
Maior que 1,70    C                         F                          I
"""

hight: float = float(input("Digite a altura: "))
weight: float = float(input("Digite o peso: "))

if hight < 1.20:

    if weight < 60:
        print("A")

    elif weight >= 60 and weight <= 90:
        print("D")
    
    elif weight > 90:
        print("G")

elif hight >= 1.20 and hight <= 1.70:

    if weight < 60:
        print("B")

    elif weight >= 60 and weight <= 90:
        print("E")
    
    elif weight > 90:
        print("H")    

elif hight > 1.70:
     
     if weight < 60:
        print("C")

     elif weight >= 60 and weight <= 90:
        print("F")
    
     elif weight > 90:
        print("I")
    