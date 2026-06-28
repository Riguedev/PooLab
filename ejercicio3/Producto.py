#Clase Encargada de manejar la inforamacion de los prouductos
class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #Mostrar los Datos de los prouductos
    def mostrar_producto(self):
        print("Nombre: " + self.nombre)
        print("Precio: " + str(self.precio))
        print("Cantidad: " + str(self.cantidad))

    #Permite Añadir o Quitar productos
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad += (nueva_cantidad)

#Este metodo realiza calculo de valor total de los prouducto (Precio de audifonos)
    def calcular_valor_total(self):
        print("Valor total: " + str(self.cantidad * self.precio))

        