def factorial(num: int) -> int:

    list_num: list[int] = [x for x in range(1, num + 1)]
    fact = 1

    for i in list_num:
        
        fact = fact * i
    
    return fact


def main() -> None:
    
    num: int = int(input("Digite um número: "))
    
    print(f'O fatotial de {num} é igual a {factorial(num)}')
    print(f'{num}! = {factorial(num)}')

 
if __name__ == '__main__':
    main()
