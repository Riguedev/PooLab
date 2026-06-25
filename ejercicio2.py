class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, dinero):
        self.saldo += dinero
        print("Has depositado: " + str(dinero))

    def retirar(self, dinero):
        if self.saldo < dinero:
            print("Saldo insuficiente")
            return
        self.saldo -= dinero
        print("Has retirado: " + str(dinero))

    def mostrar_saldo(self):
        print("Tu Saldo actual es de: " + str(self.saldo))


cuenta = CuentaBancaria("Ado", 1000)
cuenta.depositar(100)
cuenta.retirar(300)
cuenta.mostrar_saldo()