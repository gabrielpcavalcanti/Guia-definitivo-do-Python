"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado 
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 
8%). Faça um programa em que o usuário entre com o valor e o estado destino do 
produto e o programa retorne o preço final do produto acrescido do imposto do estado 
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem 
de erro. 
"""

valor = float(input("Digite o valor: "))
estado = input("Digite o estado (MG, SP, RJ, MS): ")

if estado == "MG":
    valor_final = valor + (valor * 0.07)
    print(valor_final)

elif estado == "SP":
    valor_final = valor + (valor * 0.12)
    print(valor_final)

elif estado == "RJ":
    valor_final = valor + (valor * 0.15)
    print(valor_final)

elif estado == "MS":
    valor_final = valor + (valor * 0.08)
    print(valor_final)

else:
    print("Erro")

