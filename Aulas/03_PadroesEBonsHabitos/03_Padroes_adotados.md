# Padrões adotados no curso

No Python e em qualquer linugagem de programação, existem boas regras de conduta a serem usadas e maneiras mais adequadas de escrever o código, tornado-o mais claro a todos. 

O PEP8 é um guia de estilo, será usado nesse curso. Além do mais, outros padrões serão utilizados e serão mostrados aqui (proprios e do clean code). É o que eu acredito ser a melhor forma de escrever um certo conceito da programação no python. Mas assim como na observação feita no arquivo do PEP8, se não enteder algum conceito, não fique assustado. 

Não utilizarei tudo desde o início, mas com o tempo, mais tópicos serão dados e o padrão de escrita do código mudará um pouco até um ponto que vejo como sendo bem escrito. Não uso tudo desde o início, pq não há necessidade e ficaria muito complexo sem a necessidade.

Esse padrões não precisam ser adotados e você que escolhe eles. Uma vez adotado, siga com eles durante todo o projeto, para manter a consistencia. Escolhi eles porque acredito que seja a melhor forma de escreve e aprender Python.

Alguns dos padrões adotados vão paracer com outras linguagens de programação. Não faria sentiso isso porque o python facilita as coisas e tem sua própria forma de escrever e pode ser pedante de escrever, mas em pontos específicos, isso é bom e mostrarei aqui. 

Em projetos e em exercícios mais simples, a maioria desses padrões são desnecessários, mas com o passar o tempo, eles ficam mais complexos e a necessidade de adota-los fica maior, então usar o PEP8 e esses padrões é bom saber desde o início.

Algumas vezes vai parecer que o código fica mais poluído, mas escrito de uma forma elegante, se torna muito útil, como veremos. Muitos dos padrões afetados aqui são obrigatórios em outros linguas, o pyhton da liberdade de escrever em diversas maneiras. 

## Índice  
1. [if \_\_name__ == '\_\_main__' e def main( )](#1---if-__name__--__main__-e-def-main-)  
2. [Type annotations](#2---type-annotations)  
3. [Padrões para variáveis](#3---padrões-para-variáveis)  
4. [Padrões para strings](#4---padrões-para-string)  
5. [Padrões para arquivos](#5---padrão-para-abertura-e-fechamento-de-arquivos)
6. [Padrões para exceções](#6---padrão-para-exceções)
7. [Padrões para programação orientada a objetos](#7---padrões-para-programação-orientada-a-objetos)

## 1 - if \_\_name__ == '\_\_main__' e def main( )

Esse if statement e a função main( ) será explicado com muito detalhe quando formos falar de funções, modulos e classes. 

O padrão adotado nesse curso é que eles sempre serão utilizados quando tiver esses conceitos explicitamente envolvidos. 

As ideias por trás de usar a segunda forma quando utilizarmos funções, modulos e classes são:

- Para o código ficar mais organizado;
- Distinhir quais arquivos são scripts e quais são modulos.

Eles podem ser utilizados desde o início, mas o código fica maior e sem necessidade, como mostrado em um exemplo bem simples.

```python
# Forma mais simples
print("Hello World!")

```

```python
# Forma mais "complexa"
def main() -> None:
    print("Hello World!")
 
 
if __name__ == '__main__':
    main()

```

Os dois códigos darão o mesmo resultado, mas veja com um é mais simples que o outro. Para o incío, não há a necessidade de utilizar todos esses comando, mas com o passar do tempo e complexidade do código, será extremamente útil e adotado em todos os programas.

A segunda forma lembra outras linguagens de programação, como o Java e pode ser familiar para quem já programa. A sintaxe muda, mas o programa é a forma é a mesma. 

Será explicado com mais detalhes na aula, mas o padrão adotado é nessa ordem, de cim para baixo: classes, funções, função main( ) e if \_\_name__ == '\_\_main__':.

```python
class Class:

    def __init__(self):
        pass

    def func01(self):
        pass

    def func02(self):
        pass


def func03() -> None:
    pass

def func04() -> None:
    pass

def main() -> None:
    pass
 
if __name__ == '__main__':
    main()

```

Dica: Para não ter que escrever sempre a função main( ) e if statement, algumas IDE`s já vem pré-configuradas e/ou você pode escrever um tamplate e configurar na própria IDE. 

## 2 - Type annotations

Essa feature do Python é muito útil e quase ninguém adota ela, principalmente no inicío, mas mesmo depois, poucos códigos eu vejo utilizam os tyoe annotation. Se você viu em algum projeto ou repositório, de parabéns a quem escreveu, ele teve cuidado e carinho pelo programa escrito.

Usar o type annotations em Python facilita a leitura dos programas e te alerta quando alguma variável está sendo declarada ou usada de forma errada. Algumas IDE`s avisam do erro, mas é bom utilizar a biblioteca mypy para um melhor checagem dos type annotations.

Drclaram uma variável de um tipo e colocar outro no lugar, não vai fazer o programa "crachar", mas ele te alerta que algo está errado. 

Vejamos cada um deles agora:

### a) Tipos de variáveis primitivas

```python
idade: int = 10
pi_aproximado float = 3.14
logico: bool = True
nome: str = "Sofia"

```

### b) Listas

```python
numeros: list[int] = [1, 2, 3]
palavras: list[str] = ["a", "b", "c"]

```

### c) Truplas

```python
ponto: tuple[int, int] = (10, 20)
dados: tuple[str, int, float] = ("Alice", 25, 1.75)

```

### d) Dicionários

```python
aluno: dict[str, int] = {"idade": 25, "nota": 90}

```

### e) Conjuntos

```python
numeros_unicos: set[int] = {1, 2, 3}

```

### f) Em parametros e argumentos de funções

```python
def soma(a: int, b: int) -> int:
    return a + b

def filtrar_pares(numeros: List[int]) -> List[int]:
    return [n for n in numeros if n % 2 == 0]

```
### g) Em classes 

```python
class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        return f"Olá, meu nome é {self.nome}!"


p: Pessoa = Pessoa("Alice", 25)

print(p.saudacao())  

```

## 3 - Padrões para variáveis

Toda variável seguirá o padão que estiver descrito no clean code, voce pode ve-lo aqui. link arquivo clean code. Ou talvez evaporar o que tiver no arquivo e colocar o que tiver de informaçao durante os arquivos do curso.

## 4 - Padrões para String

### a) Sempre use f-strings

Mesmo podendo fazer a concatenação tradicional, é preferivel o uso de f-strings em todos os casos e será adotado aqui. Ele facilita a leitura e é mais simples de escrever.

```python
nome: str = "Alice"
idade: int = 25

# Sem f-string 
mensagem_tradicional = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos."
print(mensagem_tradicional)

# Usando f-string
mensagem_fstring = f'Olá, meu nome é {nome} e eu tenho {idade} anos.'
print(mensagem_fstring)

```

### b) Use Raw strings para caminhos e regex

As Raw Strings (r"") são usadas para interpretar strings literalmente, sem processar caracteres de escape (\).

Use elas Strings com caminhos de arquivos no Windows e Expressões regulares (regex), onde \ é comum.

Sempre use r"" quando precisar de textos com \ que não devem ser interpretados!

```python
# Caminho de arquivos 

# Sem raw strings
caminho: str = "C:\\novo\\teste\\arquivo.txt"
print(caminho)

# Com raw strings
caminho: str = r"C:\novo\teste\arquivo.txt"
print(caminho)

```

```python
# Regex

import re

padrao: str = r"\d+"  # Ao invés de "\\d+"
texto: str = "Idade: 25 anos"

resultado = re.findall(padrao, texto)
print(resultado)

```


## 5 - Padrão para arquivos

### a) Sempre use with para abertura e fechamento de arquivos

Podemos abrir e fechar arquivos com os métodos .open( ) e .close( ), mas caso tenha algum problema entre esses dois comandos, o arquivo nunca vai ser fechado. Para evitar problemas sempre utize with.

```python
# Usando open() e close()
arquivo = open("exemplo.txt", "w")  
arquivo.write("Olá, mundo!\n")
arquivo.close()

# Usando with open()
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
```

## 6 - Padrão para exceções

### a) Sempre especifique as exceções 

```python
def dividir(a, b):

    try:
        resultado = a / b
        print(f"Resultado: {resultado}")

    # Forma correta e sempre utilizada.
    except ZeroDivisionError:  
        print("Erro: Tentativa de dividir por zero!")
    # Forma correta e sempre utilizada.
    except TypeError:  
        print("Erro: Tipos inválidos! Certifique-se de fornecer números.")
    
    # Forma errada
    except Exception as erro:  
        print(f"Erro inesperado: {erro}")

    # Forma ainda mais errada.
    except:  
        print(f"Erro inesperado.")

```


### b) - Context maneger

## 7 - Padrões para programação orientada a objetos
