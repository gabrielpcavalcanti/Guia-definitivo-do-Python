""" 
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996. 

Aprofundamento: Veja quais desses são bissextos: years = [1996, 2000, 2012, 2024, 1999, 1900, 2019,  2021, 2022, 2100]
"""

def leap_year(number: int) -> str:

    if number % 400 == 0:
        return f'{number} é um ano bissexto.'
    
    elif (number % 4 == 0) and (number % 100 != 0):
        return f'{number} é um ano bissexto.'

    return f'{number} não é um ano bissexto.'

def main() -> None:
    
    # year: int = int(input("Digite um ano: "))
    # print(leap_year(year))

    years = [1996, 2000, 2012, 2024, 1999, 1900, 2019,  2021, 2022, 2100, 2026]

    for year in years:

        print(leap_year(year))


if __name__ == '__main__':
    main()
