"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado 
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 
8%). Faça um programa em que o usuário entre com o valor e o estado destino do 
produto e o programa retorne o preço final do produto acrescido do imposto do estado 
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem 
de erro. 
"""

price: float = float(input("Digite o valor do produto: "))
state: str = input("Digite o estado de destino (MG, SP, RJ, MS): ").upper()

match state:

    case "MG":
        tax: float = 0.07

    case "SP":
        tax: float = 0.12

    case "RJ":
        tax: float = 0.15
        
    case "MS":
        tax: float = 0.08

    case _:
        print("Estado inválido!")

final_price: float = price * (1 + tax)

print(f"Preço final com tax para {state}: R$ {final_price:.2f}")
