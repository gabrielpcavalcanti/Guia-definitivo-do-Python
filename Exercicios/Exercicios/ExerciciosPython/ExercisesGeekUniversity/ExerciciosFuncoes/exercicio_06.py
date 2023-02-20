""" Essa é o modulo tal """

def segundos(hora, minuto, segundo):
    """
    Teste para Docstrings.

    Parameters:
        hora (int): valor da hora.
        minuto (int): Valor dos minutos.
        segundo (int): Valor dos segundos.

    Returns:
        horas_seg + minuto_seg + segundo(int): retorna o valor em segundos.

    """

    horas_seg = hora * 60 * 60
    minuto_seg = minuto * 60
    return horas_seg + minuto_seg + segundo

print(segundos(5, 30, 54))
