"""
b) Dado cinco frases abaixo, descubra qual não é o palíndromo.

"A torre da derrota"

"Roma me tem amor" 

"A casa sacada"

"Socorram me subi no ônibus em Marrocos" 

"Anotaram a data da maratona" 
"""

phrase_01: str = "A torre da derrota"
phrase_02: str = "Roma me tem amor" 
phrase_03: str = "A casa sacada"
phrase_04: str = "Socorram me subi no onibus em Marrocos"
phrase_05: str = "Anotaram a data da maratona" 

print(f'A frase é um palíndromo: {phrase_01.replace(" ", "").casefold() == phrase_01.replace(" ", "").casefold()[::-1]}.')
print(f'A frase é um palíndromo: {phrase_02.replace(" ", "").casefold() == phrase_02.replace(" ", "").casefold()[::-1]}.')
print(f'A frase é um palíndromo: {phrase_03.replace(" ", "").casefold() == phrase_03.replace(" ", "").casefold()[::-1]}.')
print(f'A frase é um palíndromo: {phrase_04.replace(" ", "").casefold() == phrase_04.replace(" ", "").casefold()[::-1]}.')
print(f'A frase é um palíndromo: {phrase_05.replace(" ", "").casefold() == phrase_05.replace(" ", "").casefold()[::-1]}.')
