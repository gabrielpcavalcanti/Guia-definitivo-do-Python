number_01: int = int(input("Digite o primeiro valor: "))
number_02: int = int(input("Digite o segundo valor: "))
number_03: int = int(input("Digite o terceiro valor: "))

mean_choice: str = input("Digite a média que quer calcular ((a) Geométrica (b) Ponderada (c) Harmônica (d) Aritmética)): ".lower())

match mean_choice:

    case "a":
        geometric_mean: float = ((number_01 * number_02 * number_03) ** (1/3))
        print(f'A média geométrica é: {geometric_mean:.2f}.')
    
    case "b":
        weighted_mean: float = (number_01 + 2 * number_02 + 3 * number_03) / 6
        print(f'A média ponderada é: {weighted_mean:.2f}.')
    
    case "c":
        harmonic_mean: float = (1 / ( 1/ number_01 + 1 / number_02 + 1 / number_03))
        print(f'A média harmônica é: {harmonic_mean:.2f}.')
    
    case "d":
        aritimetic_mean: float = ((number_01 + number_02 + number_03) / 3)
        print(f'A média aritimética é: {aritimetic_mean:.2f}.')

    case _:
        print("Erro.")

