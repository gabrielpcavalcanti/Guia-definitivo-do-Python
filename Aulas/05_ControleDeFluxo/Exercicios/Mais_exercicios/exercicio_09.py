"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco- 
lhida. Escreva uma mensagem de erro se a opção for inválida. 
Escolha a opção: 
1— Soma de 2 números,
2— Diferença entre 2 números (maior pelo menor), 
3— Produto entre 2 números,
4— Divisão entre 2 números (o denominador não pode ser zero). 
"""

print("""Escolha a opção: 
1— Soma de 2 números,
2— Diferença entre 2 números (maior pelo menor), 
3— Produto entre 2 números,
4— Divisão entre 2 números (o denominador não pode ser zero).  """)

print()

choice: int = int(input("Digite a opção que deseja: "))

print()

match choice:

    case 1:
        num_01:float = float(input("Digite um número: "))
        num_02: float = float(input("Digite um número: "))

        print(f'\nA soma dos número é {num_01 + num_02}')
    
    case 2:
        num_01: float = float(input("Digite um número: "))
        num_02: float = float(input("Digite um número: "))
        
        if num_01 > num_02:
            print(f'\nA diferença é {num_01 - num_02}')

        else:
            print(f'\nA diferença é {num_02 - num_01}')

    case 3:
        num_01: float = float(input("Digite um número: "))
        num_02: float = float(input("Digite um número: "))

        print(f'\nO produto entre os números é: {num_01 * num_02}')

    case 4:
        num_01: float = float(input("Digite um número: "))
        num_02: float = float(input("Digite um número: "))

        if num_02 > 0:
            print(f'\nA divisão entre os números é: {num_01 / num_02}')
    
    case _:
        print("Escolha inválida.")
