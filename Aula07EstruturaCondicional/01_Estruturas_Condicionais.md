# Estruturas Condicionais

A partir de agora o universo da programação se abre. As possíbilidades aumentam concideravelmente.

 Até agora somente executamos códigos que leam linha poor linha, com as estruturas condicionais isso muda, já que o código pode pular linhas dependendo se condições são satisfeitas ou não. 

Esse tipo de estrutura possibilita uma maior complexidade e ao mesmo tempo facilidade para escrever um código.

Como o nome diz, é uma condição. Faremos uma "Pergunta" para o programa é caso for satisfeira fará uma coisa, se não, fará outra.

Existem três estruturas condicionais no Python, são elas o if (se), else (se não) e elif( se não se). Esse última é uma junção das outras duas.

## indentação

Antes da falar das estruturas é obrigatório entender que o python funciona utilizando identação. Nada mais é que uma forma de organizar o código e estabelecer hieraquias dentro de blocos de comandos.

Todo bloco de comando no Python se inicia com os : , ele diz ao Python que um novo bloco de comando é criado.

A identação no python são 4 espaços ou um TAB. Então toda vez que colocar uma estrutura é necessário que a linha(s) de baixo estaja(m) quatro espaços à frente.

Se estiver confuso, calma, isso é padrão no Pyhton. É bem rápida a sua adaptação.

## If

É a primeira estrutura condicional. Funciona da seguinte maneira: caso uma condição seja satisfeita, execute o bloco de comando, caso não seja, siga em frente.

utilizamos os operadores e variáveis para fazer uma condição. Cada uma delas tem um valor de verdade: ou é True ou é False. Se for verdadeiro, executa, se não, a instrução do bloco de comando do if é ignorado. 

Esse valor de verdade pode mudar durante a execução do programa, por exemplo: a varivável muda de valor e agora a condição vira verdeira, o código é execultado ou vice-versa.

Como funciona o comando: Coloca a palavra reservada if. Em seguida coloca a condição e os :.

nas linhas de baixo, mostra o que será executado caso seja verdadeiro. Perceba que está identado, ou seja, cria um bloco de comando a partir do quarto espaços.

```python
valor = 19

if valor > 18:
    print(f'sua idade é {idade}.')
```
```Python
Sua idade é 19
```
## Else

Você pode estar se perguntando se caso a condição seja falsa o que acontece. Ai que entra o else. Ela é uma estrutura que somente pode ser usada com o if junto, nunca sozinha. 

```python
nome = 'rafael'

if nome == 'gabriel':
    input("O seu nome é gabriel")

else:
    print("Seu nome deveria ser gabriel")
```

## Elif

A condição elif é uma junção das duas outras. Ela serve para colocar várias condições antes de ter uma final, no caso o else. Podemos colocar vários if`s, mas não fica bem escrito e organizado.

Só utilize o elif se a condição ainda estiver de acordo com o if original, caso contrário, o programa pode interromper a verificação de condições e não funcionar adquadamente.

O comamdo else sempre será o ultimo comando condicional e ele nunca tem um condição assiciada, somente o else: . Além disso, o else não é obrigatótio, ou seja, caso nenhum dos testes passem e não queria qe faça nada com o resultado obtido ou ainda que esses dados sejam inválidos, não coloque o comando else.

```Python
idade = 18

if idade >= 18:
    print("maior de idade")

elif idade > 0 and idade < 18 :
    print("menor de idade")

else:
    print("idade inválida")
```

## Avançando nas estrururas condicionais

Assim que entender como funciona as estruturas condiocionais é possível dar mais complexidade ao código com a mesmas estrutura condicional. 

Além disso é possível misturae estruturas condicionais com as de repetição, listas, truplas, etc. As possibilidades são infinitas. vermos tudo mais para frente.

Podemos colocar estruturas condicionais dentro de estrututuras condicionais, quantas quisermos.

A cada nova estrutura, abre um novo bloco de comando, também identado.

```Python
idade = int(input("Digite a sua idade: "))

if idade > 18:
    if idade =! 0:
        print(mior de idade)
    else:
        print("idade inválida")

elif idade <18:
    if idade =! 0:
        print("Menor de idade")
    else:
        print("Idade inválida")

else:
    print("Deu errro, digite novamente")
```

Perceba a hierarquia dos blocos de comando. Os que estiverem dentro de outra condição será dependente da de fora. As que estiveram na mesmo posiçãom será de mesma hierarquia.

### operadores lógicos

Já vimos os operadores lógicos and, or, not e is. Podemos utilizar eles dentros das nossas condições aumentando o nosso leque de possibilidades.

```Python
ligado = True
Desligado = False
x = 2

if ligado:
    if x ==2:
        print("Está ligado")
        print(f'x é igual a {x}')
    else:
        print("Está desligado")

elif ligado and Desligado:
    print("Erro no sistema, não pode estár ligado e desligado ao mesmo tempo!!!")

else:
    print("Está desligado")
```

```Python
valor = 5

if valor < 5 or valor >= 2:
    print(valor)

else:
    Print(valor - 2)
```

```Python
ligado = True

if not ligado:
    print("Deligado")
```
