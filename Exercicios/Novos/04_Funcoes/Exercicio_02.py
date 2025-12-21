""" 
Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""

def is_even(number: int) -> bool:

    return number % 2 == 0


def main() -> None:
    
    number_01: int = int(input("Digite um número: "))

    if is_even(number_01):
        print(f'O número {number_01} é par')

    else:
        print(f'O número {number_01} é impar')
        
 
if __name__ == '__main__':
    main()
    