"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, 
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 
dias em anos não bissextos. 
"""

date: str = input("Digite uma data no formato DD/MM/AAAA: ")

day: int = int(date[0:2])
month: int = date[3:5]
year: int = int(date[6:])

