# Dunde Main e Dunder Name

Dunder é o nome para __. Algumas funções no Python possuem esse fromato. exemplos: ```__init__,  __main__,__name__```.

Quando um arquivo python é criado, ele internamente possui o nome de ```__main__```.

```python
# Salvar o arquivo com nome soma.py
a = 2
b = 3
soma = a + b
print(soma)

print(__name__)

```

```python
5
__main__
```

Mesmo que o nome do arquivo seja soma.py, o python o indentifica como ```__main__```.

É bom entender isso porque, quando se cria módulos e os importa para o seu código principal,
todas as operações que foram feitas nele serão importadas e geralmente isso não é bom. Na verdade, só é recomendável colocar classes e funções no módulo criado para evitar a importação de operações indesejadas.

Para evitar que alguma operação no módulo seja importada, no final dele colocamos ```if __name__ == __main__: ```. 
Essa instrução if vai conter todas as operações, fazendo com que só sejam executadas quando o própio módulo for rodado e não o arquivo principal.

```python
# nome do arquivo: soma.py
from matematica import soma

print(soma(3,2))

```

O módulo criado matemática possui o seguinte código

```python
def soma(a,b):
    return a + b

if __name__ == "__main__":
        print("oi")

```

Nele possui uma função soma e a condição ``` if __name__ == __main__: ```. Se executarmos arquivo matemática.py, o código print("oi"), vai ser executado. Mas quando executamos o código soma.py, só é mostrado a saída de print(soma(3,2)). Isso ocorre porque o nome do arquivo não é mais ``` __main__ ``` e sim soma. Então, a condição ``` if __name__ == __main__: ``` não é satisfeita.

Em resumo: quando for criar módulos, evite colocar operações como print, if, with, for, etc.. fora de classes e funções. Caso tenha de colocar alguma operação, coloque-a dentro de ``` if __name__ == __main__: ```, para que essa operaçào não seja levada ao código principal. Só serão levadas as classes e funções do móudulo.
