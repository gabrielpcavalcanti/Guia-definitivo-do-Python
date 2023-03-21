from datetime import datetime

now = datetime.now()
yaer = now.year


def voto():
    print('-' * 30)
    ano = int(input("Em que ano você nasceu? "))
    idade = yaer - ano

    if idade >= 18 and idade < 65:
        return f'Com {idade} VOTO OBRIGATÓRIO'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} VOTO OPICIONAL'
    elif idade >= 65:
        return f'Com {idade} VOTO OPICIONAL'
    else:
        return f'Com {idade} NÃO VOTA'

print(voto())



