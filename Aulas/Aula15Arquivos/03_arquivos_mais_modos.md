# Modos dos arquivos

Existe 4 tipos de modos de abertura de arquivos principais: r -> read; w - > write; a -> append e x - > escrita de arquivos não criados

· Read é o modo padrão de abertura do python, ele está apto a ler e somente ler o arquivo.
· Write é o modo de escrita de arquivos, ele subtitui o conteúdo de um arquivo com coisas novas ou cria um arquivo se ele não existir 
· Append é o modo que adiciona coisas ao arquivo sem que o conteúdo antigo seja apagado, ele sempre insere dados na últma linha do arquivo.
· x é um modo que abre para a escrita de arquivo caso ele não exista, se existir, gera erro.

Há mais um modo que pode ser utlizado em conjunto com qualquer outro modo que é o '+', ele habilita a leitura e escrita de um arquivo.

## Exemplo 'r'

```Python
with open('frutas.txt') as arq:
    ler = arq.read()
    print(ler)
```
## Exemplo 'w'

```Python
with open('carros.txt', 'w') as arq:
    arq.write('BMW' + '\n')
    arq.write('Ford' + '\n')
    arq.write('Mercedes' + '\n')
    arq.write('Lamborghini' + '\n')
```
## Exemplo 'a'

```Python
with open('frutas.txt', 'a') as arq:
    arq.write('uva' + '\n')
    arq.write('pera')
```
## exemplo 'x'

```Python
with open('arquivo x', 'x') as arq:
    for i in range(10):
        arq.write('i')
```
## exemplo '+'

```Python
with open('frutas.txt', 'r+') as arq:
    arq.write('podemos escrever agora.')
    ler = arq.read()
    print(ler)
```
