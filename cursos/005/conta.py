class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0) -> None:
        # print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


if __name__ == '__main__':
    conta = Conta(123, "Nico", 55.5, 1000.0)
    conta1 = Conta(1, "Fulano", 0.0)
    conta2 = Conta(2, "Beltrano", 0.0)
    conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

    conta.extrato()
    conta.deposita(15.0)
    conta.extrato()
    conta.saca(10.0)
    conta.extrato()
