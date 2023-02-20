"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

veri_temperatura = 9999

lista_temperaturas = []

while veri_temperatura != -273:
    
    veri_temperatura = float(input("Digite o valor da temperatura em graus Celcius (Digite -273 para parar): "))
    lista_temperaturas.append(veri_temperatura)

lista_temperaturas.pop()
maximo_temp = max(lista_temperaturas)
minimo_temp = min(lista_temperaturas)
media = sum(lista_temperaturas) / len(lista_temperaturas)

print(f"Temperatura máxima: {maximo_temp} graus Celcius")
print(f"Temperatura mínima: {minimo_temp} graus Celcius")
print(f"Temperatura media: {media} graus Celcius")

