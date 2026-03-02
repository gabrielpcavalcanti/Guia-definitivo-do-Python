"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá
subir para atingir o seu objetivo. 
"""

hight_ladder_step = float(input("Digite a altura do degrau: "))
hight = float(input("Qual altura deseja alcançar: "))

steps = hight / hight_ladder_step

print("A quantidade de degraus para atingir o seu objetivo é: {}".format(steps))
