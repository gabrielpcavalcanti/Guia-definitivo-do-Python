class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id: int, nome: str, saldo: float = 0) -> None:
        
        self.id = id
        self.titular = nome
        self.saldo = saldo

        print(f'Conta Bancária criada com sucesso. Saldo atual: {self.saldo}')

    def __str__(self) -> str:
        return f'A conta bancária {self.id} de {self.titular} tem saldo de R$ {self.saldo:,.2f}'
    

    def depositar(self, valor: float) -> None:
        self.saldo += valor

        print(f'Deposito de R$ {valor} na conta {self.id} de titular {self.titular}')
        print(f'Valor final: {self.saldo:,.2f}\n')


    def sacar(self, valor: float) -> None:

        if valor > self.saldo:
            print(f'Saque NEGADO de R$ {valor:,.2f} da conta {self.id}')
        else:
            self.saldo -= valor
            
            print(f'Saque de R$ {valor:,.2f} na conta {self.id} de titular {self.titular}')
            print(f'Valor final: {self.saldo:,.2f}\n')



c1 = ContaBancaria(id=112, nome="Gabriel", saldo=3000)
print(c1)  # __str__()

print(c1.__doc__)

c1.depositar(500)

print(c1)

c1.sacar(500_000)

print(c1)