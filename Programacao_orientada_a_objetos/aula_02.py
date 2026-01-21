class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    parâmetros:
    nome: str - Nome da pessoa
    idade: int = Idade da pessoa
    """
    def __init__(self, nome: str= "", idade: int = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade
    

    def __str__(self) -> str:  # DUNDER Method
        return "Classe gafanhoto"
    

    def __getstate__(self) -> object:
        return f'Nome: {self.idade} Idade: {self.idade}'
    
    # Métodos de Instância
    def aniversario(self):
        """teste 1,23"""
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'


# Declaração de objetos
g1 = Gafanhoto(nome="Gabriel", idade=27)

g1.aniversario()

print(g1.__str__())

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

print(g1.mensagem())

print(g1.__doc__)  # DUNDER Atribute. Mostra a documentação do objeto, no caso, da classe gafanhoto, jé que o objeto criado vem dessa classe.
