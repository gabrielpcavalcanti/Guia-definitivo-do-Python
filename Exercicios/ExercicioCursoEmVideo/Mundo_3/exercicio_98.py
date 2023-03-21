import time 

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contador de {inicio} até {fim} de {abs(passo)} a {abs(passo)}')

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            time.sleep(0.5)
            cont += passo
        print()

    elif inicio > fim:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            time.sleep(0.5)
            cont -= passo
        print()


contador(1,10,1)
contador(10,0,2)

print('Agora é a sua vez de personalizar a contagem')
ini = float(input('INICIO: '))
fim = float(input('FIM: '))
pas = float(input('PASSO: '))

contador(ini,fim,pas)
