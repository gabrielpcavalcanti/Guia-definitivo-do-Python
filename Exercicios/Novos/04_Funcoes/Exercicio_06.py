""" 
Escreva uma função que recebe um número n e retorna uma lista com todos os números de 1 até n. Teste algumas vezes a função criada.
"""

def creat_list_number(number: int) -> list[int]:

    return [number for number in range(1, number + 1)]


def main() -> None:
    
    print(creat_list_number(5))
    print(creat_list_number(10))
    print(creat_list_number(15))
    print(creat_list_number(20))


if __name__ == '__main__':
    main()
