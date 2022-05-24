# Operadores matemáticos

Após ter o primeiro contato com a programação, estamos preparados para avançar nesse
universo. O Python e imagino que todas as outras linguagens de programação apresentam operadores que aumentam a complexidade e possibilitam realizar tarefas mais interessantes.

O primeiro tipo de operador são os matemáticos, eles nos premitem fazer contas matemática,
não brinca! Com esse nova possibilidade, qualquer operação matemática pode ser resolvida
por meio da programação.

Ps: Não é necessário ser um gênio da matemática para programar, mas saber alguma
coisa ajuda muito.

No Python existem 6 operações matemáticas básicas já implementadas. São elas:

* Soma ( + )
* Subtração ( - )
* Multiplicação ( * )
* Divisão ( / )
* Divisão inteira ( // )
* Módulo ( % )
* Potenciação ( ** )

Possui os mesmos significados da matemática. As duas operações que possa haver alguma dúvida é a % e //. o % da
o resto da divisão de dois números e o // da a a parte inteira da divisão.

### Soma

```python
4 + 10
5.25 + 3.25
```

```python
14
8.50
```

### Subtração

```python
7 - 8
3.6 - 2
```

```python
-1
1.6
```

### Multiplicação

```python
3 * 2
25.2 * 4
```

```python
6
100.8
```

### Divisão

```python
1 / 2
100 / 4
```

```python
0.5
25
```
### Divisão inteira

```python
1 // 2
100 // 4
```

```python
0
25
```

### Módulo

```python
50 % 4
36 % 6
```

```python
2
0
```

### Potenciação

```python
2 ** 5
3 ** 3
```

```python
32
27
```

Não sei se percebeu, mas o Python por padrão não tem a operação de radiciação. Se quiser contornar isso, importe o pacote math (sem a necessidade de instalação) e utilize a função sqrt( ) (apenas raiz quadrada) ou eleve o número a (1/2) ou (1/3), dependendo do qual tipo de raiz que queira.

```python
import math

math.sqrt(16)
math.sqrt(100)
```

```python
4.0
10.0
```

```python
# Caso não queira utilizar o sqrt( )

16 ** (1/2)
27 ** (1/3)
```

```python
4.0
3.0
```

Obs: Podemos colocar qualquer tipo de operação dentro de variáveis. Não fiz isso aqui, pois ainda não vimos esse conteúdo. Veremos ele em outra aula.

### Ordem das operações

O Python segue a mesma convensão da matemática, ou seja, a ordem é primeiro resolver as chaves depois os colchetes e por fim os parênteses. Porem o python nao utiliza as { } ou [ ] para esse fim. Então utiliza somente parênteses. A preferência é resolver primeiro as operações de dentro e depois as de fora. Sempre de dentro para fora.

Em relação aos operadores, A potencia tem preferencia, depois a divisão e multiplicação e por fim a adição e subtração. Sempre resolve da esquerda para a direita.

```python
x = ( 4 + 5 * 2) / 1 - 3
print(x) 
```

```python
11.0
```

obs: x, no exemplo acima é uma variável. Não se preucupe porque veremos com calma em outra aula e você usará isso toda hora na programação.
