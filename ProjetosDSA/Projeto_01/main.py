import random

print("Bem-vindo(a) ao jogo da forca!")
print("Adivinhe a palavra abaixo: \n")

palavras = ["banana", "uva"]
chances = 6
letras_erradas = []

palavra_escolhida = random.choice(palavras)
codigo = "_ " * len(palavra_escolhida)

while True:

    print(codigo)
    print()

    print("Chances restantes: ", chances)
    print("Letras erradas \n", letras_erradas)


    letra = input("Digite uma letra: ")

    if letra in palavra_escolhida:
        



