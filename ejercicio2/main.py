#Importamos la clase Cuenta Bancaria 
from CuentaBancaria import CuentaBancaria

#Se crea la instancia de la clase CuetaBancaria
cuenta = CuentaBancaria("Ado", 1000)

#Ejecutamos los metodos de la clase
cuenta.depositar(100)
cuenta.retirar(3000)
cuenta.mostrar_saldo()