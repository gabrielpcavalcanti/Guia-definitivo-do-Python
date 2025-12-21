""" 
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das 
seguintes médias de acordo com um valor digitado pelo usuário:

(a) Geométrica

(b) Ponderada

(c) Harmônica

(d) Aritmética
"""

def geometric_mean(number_01: float, number_02: float, number_03: float) -> float:
    return ((number_01 * number_02 * number_03) ** (1/3))


def weighted_mean(number_01: float, number_02: float, number_03: float) -> float:
    return (number_01 + 2 * number_02 + 3 * number_03) / 6


def harmonic_mean(number_01: float, number_02: float, number_03: float) -> float:
    return (1 / ( 1/ number_01 + 1 / number_02 + 1 / number_03))


def aritimetic_mean(number_01: float, number_02: float, number_03: float) -> float:
    return ((number_01 + number_02 + number_03) / 3)


def main() -> None:
    
    number_01: int = int(input("Digite o primeiro valor: "))
    number_02: int = int(input("Digite o segundo valor: "))
    number_03: int = int(input("Digite o terceiro valor: "))

    mean_choice: str = input("Digite a média que quer calcular ((a) Geométrica (b) Ponderada (c) Harmônica (d) Aritmética)): ")
    mean_choice = mean_choice.lower()

    match mean_choice:

        case "a":

            print()
            print(f'A média geométrica é: {geometric_mean(number_01, number_02, number_03):.2f}.')
        
        case "b":

            print()
            print(f'A média ponderada é: {weighted_mean(number_01, number_02, number_03):.2f}.')
        
        case "c":

            print()
            print(f'A média harmônica é: {harmonic_mean(number_01, number_02, number_03):.2f}.')
        
        case "d":

            print()
            print(f'A média aritimética é: {aritimetic_mean(number_01, number_02, number_03):.2f}.')

        case _:
            print()
            print("Erro.")
 
 
if __name__ == '__main__':
    main()
