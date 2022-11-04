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