import random 
import time

numeros = []
numpar = []

def sorteia(numeros):
    print("Sortiando 5 valores da lista: ", end='')
    for i in range(0,5):
        numeros.append(random.randint(1,10)) 
        print(numeros[i], end=' ', flush=True)   
        time.sleep(0.5)
    print("PRONTO!")
   

def somapar(numeros):
    for i in numeros:
        if i % 2 == 0:
            numpar.append(i)
    soma = sum(numpar)
    print(f"Somando os valores pares de {numeros}, temos {soma}")


sorteia(numeros)
somapar(numeros)


