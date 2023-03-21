"""
O valor de 7.800.000.000 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
O primeiro ganhador receberá 46%;
O segundo receberá 32%;
O terceiro receberá o restante.
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

value = 7_800_000_000

first_winner = value * 0.46
secund_winner = value * 0.32
third_winner = value - (first_winner + secund_winner)

print(f'O primeiro ganhador vai receber R$ {first_winner}, O segundo vai receber R$ {secund_winner} e o terceiro vai receber R$ {third_winner}')

print(first_winner + secund_winner + third_winner)
