# Classes

Já sabendo que as classes representam objetos do mundo real, no python elas podem possuir atributos e métodos.

### Atributos 

São características e estados de um objeto que a classe está representando.

Por exemplo, um cachorro: ele possui nome, cor, tamanho, raça etc. Esses seriam os atributos da classe cachorro.

### Métodos

Representam os comportamentos do objeto representado pela classe. Fazemos esses comportamentos atravéz das funções. Então funções dentro de classes são chamados de métodos.

por exemplo, na classe do cachorro podemos pensar em função de latir, correr, ser fofo, nadar, comer etc.

#### Construtor

O contrutor é um método especial que ficam todos os atributos da classe. É com ele que podemos construir objetos e passar suas características.

## Criação de classes

você agora pode estar se perguntando como fazer para criar classes no Pyhton. Criamos isso utilizando a palavra reservada "class" seguido do nome da classe mais os : . 

O nome da classe segue o padrão PascalCase.

```Python
class Cachorro:
    pass
```

dentro da classe iremos colocar os métodos. 

## Criação de objetos

Definindo uma classe e seus atributos e métodos é possível criar infinitos objetos ou também chamado de instâncias. Os atribitos dos objetos estrão dentro do construtor.

No exemplo do cachorro, podemos criar o objeto doguinho_01, doguinho_02, max, rex, ou qualquer nome que quisermos. Cada um deles terão as características da classe cachorro. 

```Python
class Cachorro:
    pass


doguinho_01 = Cachorro() 
rex = Cachorro()

```

Como a classe não possui nada ainda, não é preciso colocar nenhum parâmetro dentro o objeto, mas será preciso quando a classe tiver o construtor, os atributos e os outros métodos. 
