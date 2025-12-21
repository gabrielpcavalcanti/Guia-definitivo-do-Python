""" 
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

def whos_bigger(number_01: float, number_02: float) -> str:

    if number_01 > number_02:
        return f'O maior número é: {number_01}'
    
    elif number_02 > number_01:
        return f'O maior número é: {number_02}'
    
    return f'Na verdade os números são iguais'

def main() -> None:
    
    number_01: float = float(input("Digite um número: "))
    number_02: float = float(input("Digite um número: "))

    print()

    print(whos_bigger(number_01, number_02))
 
if __name__ == '__main__':
    main()
