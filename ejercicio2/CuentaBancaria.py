#Clase encargada de manejar cuentas bancarias

class CuentaBancaria:

    #Definicion de las propiedades
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    #Metodo encargado de manejar los depositos de la cuenta.
    def depositar(self, dinero):
        self.saldo += dinero
        print("Has depositado: " + str(dinero))

    #Metodo encargaddo de manejar el retiro de dinero de la cuenta ademas valida que no puedas sacar mas de lo que posee el usuario
    def retirar(self, dinero):
        if self.saldo < dinero:
            print("Saldo insuficiente")
            return
        self.saldo -= dinero
        print("Has retirado: " + str(dinero))

    #Este metodo muestra el saldo actual de la cuenta
    def mostrar_saldo(self):
        print("Tu Saldo actual es de: " + str(self.saldo))