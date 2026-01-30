"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir o seu objetivo. 
"""

hight_ladder_step: float = float(input("Digite a altura do degrau: "))
hight: float = float(input("Qual altura deseja alcançar: "))

steps: float = hight / hight_ladder_step

print(f'A quantidade de degraus para atingir o seu objetivo é: {steps}')
