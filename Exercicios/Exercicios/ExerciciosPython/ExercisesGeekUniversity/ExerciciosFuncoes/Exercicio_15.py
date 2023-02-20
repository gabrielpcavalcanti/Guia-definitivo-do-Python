def verifica_triangulo(ladoa, ladob,ladoc):
    if ladoa > 0 and ladob > 0 and ladoc > 0:
        if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
            return 'É triangulo'
        else:
            return 'Não é um triângulo'
    else:
        return 'Valores inválidos'

def tipo_triangulo(ladoa, ladob, ladoc):
    if verifica_triangulo(ladoa,ladob,ladoc) is True:
        if ladoa == ladob == ladoc:
            return 'É equilatero'
        elif ladoa != ladob != ladoc:
            return 'É escaleno'
        elif ladoa == ladob and ladoa:
            return 'É isoceles'
    else:
        return "erro"

print(tipo_triangulo(3,4,5))
