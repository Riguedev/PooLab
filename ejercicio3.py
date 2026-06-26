class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print("Nombre: " + self.nombre)
        print("Precio: " + str(self.precio))
        print("Cantidad: " + str(self.cantidad))

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad += (nueva_cantidad)

    def calcular_valor_total(self):
        print("Valor total: " + str(self.cantidad * self.precio))

producto1 = Producto("Nintendo Switch", 300, 25)
producto2 = Producto("PS4", 400, 50)
producto3 = Producto("Xbox One", 400, 15)

producto1.mostrar_producto()
producto2.mostrar_producto()
producto3.mostrar_producto()

producto2.actualizar_cantidad(-5)

producto1.calcular_valor_total()
producto2.calcular_valor_total()
producto3.calcular_valor_total()