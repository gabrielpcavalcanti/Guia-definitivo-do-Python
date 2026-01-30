"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das 
seguintes categorias: 

Categoria   Idade 
Infantil A  5 a 7 
Infantil B  8 a 10 
Juvenil A   11 a 13 
Juvenil B   14 a 17 
Sênior     maiores de 18 anos 
 
"""

age: int = int(input("Enter the swimmer's age: "))

print()

match age:
    case age if 5 <= age <= 7:
        category: str = "Infant A"

    case age if 8 <= age <= 10:
        category: str = "Infant B"

    case age if 11 <= age <= 13:
        category: str = "Juvenile A"

    case age if 14 <= age <= 17:
        category: str = "Juvenile B"

    case age if age >= 18:
        category: str = "Senior"

    case _:
        category: str = "Invalid age for classification (under 5 years)"

print(f"Category: {category}")
