from math import sqrt


def quadrado_perfeito(num):
    if num > 0 and sqrt(num) ** 2 == num :
        return 'É quadrado perfeito'
    else:
        return 'Não é quadrado perfeito'


    