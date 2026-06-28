#importamos la clase Producto al archivo
from Producto import Producto

#Creamos 3 instancias de Productol
producto1 = Producto("Nintendo Switch", 300, 25)
producto2 = Producto("PS4", 400, 50)
producto3 = Producto("Xbox One", 400, 15)

#Ejecutamos los metodos para poder mostrar prooductos 
producto1.mostrar_producto()
producto2.mostrar_producto()
producto3.mostrar_producto()

#Actualizar la cantidad del proucto 1
producto2.actualizar_cantidad(-5)

#Realizamos la ejecucion de el metodo 
producto1.calcular_valor_total()
producto2.calcular_valor_total()
producto3.calcular_valor_total()