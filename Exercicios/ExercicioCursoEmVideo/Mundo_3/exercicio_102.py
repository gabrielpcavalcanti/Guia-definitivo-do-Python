def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opicinal) Mostra ou não a conta.
    :return: O valor fatorial de um número n.
    """
    print('-' * 30)
    fotorial = 1
    if show == True:
        for i in range(n, 1, -1):
            fotorial *= i
            print(f'{i} x', end=' ')
        print(f'1 = {fotorial}')
    else:
        for i in range(n, 1, -1):
            fotorial *= i
        print(fotorial)


fatorial(5) 
