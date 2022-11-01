class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0) -> None:
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


if __name__ == '__main__':
    conta1 = Conta(1, "Fulano", 0.0)
    conta2 = Conta(2, "Beltrano", 0.0)
    conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

    print(conta1.saldo)
