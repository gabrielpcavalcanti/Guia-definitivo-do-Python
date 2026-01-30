"""
c) Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.
"""

year: int = int(input("Digite um ano: "))

if year % 400 == 0:
    print()
    print("Ano bissexto")

elif year % 4 == 0 and not (year % 100 == 0):
    print()
    print("Ano bissexto")

else:
    print()
    print("Ano não bissexto")
