""" 
Crie uma função que recebe uma lista de números e retorna a soma de todos os elementos.
"""

def sum_list(list: list[int]) -> int:

    return sum(list)


def main() -> None:
    
    print(sum_list([1, 2, 4, 5, 6, 7, 8]))
 

if __name__ == '__main__':
    main()