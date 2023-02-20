"""
Leia um valor em segundos e imprima em horas, minutos e segundos.
"""
# Aviso: Não consegui resolver esse problema com os conhecimentos já adiquiridos. Esse exercicio devia estar na proxima secção ( estrututas de controle)
# Caso não entenda o código, volte a esse exercício quando souber as estruturas de controle.


value_seconds = int(input("Digite o valor em segundos: "))

if value_seconds >= 60:
    value_minute = int(value_seconds / 60)
    print(f'0:{value_minute}:0')

    if value_minute >= 60:
        value_hora = int(value_minute / 60)
        print(f'{value_hora}:0:0')
    
    #elif value_minute < 60:
        #print(f'0:{value_minute}:{value_seconds}')

elif value_seconds < 60:
    print(f'0:0:{value_seconds}')
    
else:
    print("Error, de run novamente edigite o número positivo.")
