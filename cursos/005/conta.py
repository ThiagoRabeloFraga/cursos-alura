class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0) -> None:
        # print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


if __name__ == '__main__':
    conta = Conta(123, "Nico", 55.5, 1000.0)
    conta1 = Conta(1, "Fulano", 100.0, 1000.0)
    conta2 = Conta(2, "Beltrano", 0.0)
    conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

    conta.extrato()
    conta.deposita(15.0)
    conta.extrato()
    conta.saca(10.0)
    conta.extrato()

    conta2.transfere(10.0, conta)
    conta2.extrato()
