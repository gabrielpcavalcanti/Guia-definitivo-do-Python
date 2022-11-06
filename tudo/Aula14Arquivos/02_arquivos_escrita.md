# Arquivos - escrita

Veremos agora como escrever coisas dentro de arquivos. Saiba que caso queria escrever em um arquivo, não será possível
ler e vice-versa. É preciso fazer uma coisa por vez no arquivo.

Ao abrir um arquivo com o modo de escrita, ele cria o arquivo no sistema operacional e caso ele já exista, todo conteúdo do 
arquivo principal será deletado e colocado no arquivo novo, fique atento em relação a isso.

Após abrir o arquivo com o modo de escrita: 'w', utilizamos o método write( ) para escrever dentro do arquivo.

```Python
with open("arquivo_novo.txt", mode='w') as arquivo_novo:
    arquivo_novo.write("Frase escrita no arquivo novo")
```

```Python
# O que vai aparecer no arquivo arquivo_novo:

Frase escrita no arquivo novo
```

Se quisermos escrever mais linhas, basta adicionar vários comando .write( ).


```Python
with open("arquivo_novo2.txt", mode='w') as 2:
    arquivo_novo2.write("Frase escrita no arquivo novo\n")
    arquivo_novo2.write("Frase escrita no arquivo novo\n")
    arquivo_novo2.write("outro escrita no arquivo novo de novo")

```
```Python
# O que vai aparecer no arquivo arquivo_novo2:

Frase escrita no arquivo novo
Frase escrita no arquivo novo
outro escrita no arquivo novo de novo
```

Realizando agora um programa mais complexo

```Python
with open('frutas.txt', 'w') as arq:
    while True:
        try:
            fruta = input("Digite uma fruta para adicionar a lista, caso queira parar, digite sair: ")
            if fruta != 'sair':
                arq.write(fruta + '\n')
            else:
                break
            except:
                print("É preciso colocar um valor válido")

```     

```Python
# Exemplo
Banana
Maça
Laranja
Goiaba
```
