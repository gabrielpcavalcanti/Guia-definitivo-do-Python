def consumo(distancia, litros):
    cons = distancia / litros
    if cons < 8:
        return 'Venda o carro'
    elif 8 <= cons <= 14:
        return 'Econômico'
    elif cons > 12:
        return 'Super Econômico' 

