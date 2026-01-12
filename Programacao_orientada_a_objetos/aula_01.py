# Declaração de classes
class Gafanhoto:

    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0
    
    
    # Métodos de Instância
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'


# Declaração de objetos
g1 = Gafanhoto()

g1.nome = "Gabriel"
g1.idade = 27

g1.aniversario()

print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Sofia"
g2.idade = 1

g2.aniversario()

print(g2.mensagem())


# O self é um valor temporario para a instancia de um objeto. self.idade -> g1.idade.
# Duranta a execução, ele substitui o self pela nome do objeto que chamou

# Todos atributos de instancia tem um self.