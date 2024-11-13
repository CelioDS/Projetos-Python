class Conta:
    def __init__(self,agencia=0, saldo=0):
        self.agencia = agencia,
        self._saldo = saldo



    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def msotrar(self):
        return  self._saldo

    @property
    def saldo(self):
        return self._saldo


conta = Conta("0001", 100)

conta.depositar(100)
print(conta.agencia, conta.saldo)
print(conta.msotrar())





