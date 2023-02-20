"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se 
for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 
1988, 1992, 1996 

"""

ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    print("Ano bissexto")

elif ano % 4 == 0 and not (ano % 100 == 0):
    print("Ano bissexto")

else:
    print("Ano não bissexto")

