# Herança

A ideia é a mesma que o seu própio significado, ou seja, herdar algo, alguma coisa. No caso da programação é herdar
código (Atributos e métodos de uma classa criada ou já pré-existente). Com a herança é possível reaproveitar código e extender nossas classes.

Para a herança funcionar da melhor forma possível, é precciso pensar em classes genéricas que servem para muitas outras entidades. Por exemplo: 
uma cliente e um funcionário, ambos são pessoas, então a classe generica seria uma pessoa. A classe cliente e funcionário herdariam os atributos e métodos da classe pessoas.

inicialmente vamos contruir as classes funcionário e cliente. Nada de novo aqui.

```Python
class Funcionario:

    def __init__(self, nome, sobrenome, idade, cpf, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario

    def nome_completo(self):
        return f'O seu nome completo é: {self.nome} {self.sobrenome}'
    

class Cliente:

    def __init__(self, nome, sobrenome, idade, cpf, servico = True):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def nome_completo(self):
        return f'O seu nome completo é: {self.nome} {self.sobrenome}'

```

Perceba que tanto funcionário quando cliente são pessoas. Então podemos criar uma classe genérica. Essa classe é chamada de:
classe mãe, classe pai, classe genética ou super classes. Já as classes que vao herdar são chamadas de classes filhas ou classes base.

```Python
class Pessoa:

    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def nome_completo(self):
        return f'O seu nome completo é: {self.nome} {self.sobrenome}'


```

## Super( )

Para conseguir importar todos os atributos e métodos da classe mãe é preciso colocar dentro do costrutor da classe filha
o método super( ).\__init__( ) ou NomeDaClasseMae.\__init__(self). Ele vai "puxar" as informações da classe mãe para as classes filhas.

Vamos ver como fica o código agora.

```Python
class Pessoa:

    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def nome_completo(self):
        return f'O seu nome completo é: {self.nome} {self.sobrenome}'
    

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, idade, cpf, salario):
        super().__init__(nome, sobrenome, idade, cpf)
        self.salario = salario


class Cliente(Pessoa):

     def __init__(self, nome, sobrenome, idade, cpf, servico = True):
        Pessoa.__init__(self, nome, sobrenome, idade, cpf)


cliente_01 = Cliente("Gabriel", "Cavalcanti", "23", "119.056.864-04")

print(cliente_01.nome_completo())

```

```Python
O seu nome completo é: Gabriel Cavalcanti
```

perceba que tem que colocar entre ( ) a classe mãe, para que o Python entenda quem é quem.

Veja também que o método nome_completo da classe mãe pode ser utilizado na classe cliente sem problema algum.
