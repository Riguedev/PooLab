class Empleado:
    def __init__(self, nombre, cargo, horas_trabajadas, pago_por_hora):
        self.nombre = nombre
        self.cargo = cargo
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora
    
    def mostrar_informacion(self):
        print("Empleado: " + self.nombre + "\n")
        print("Cargo: " + self.cargo + "\n")
        print("Horas trabajadas: " + str( self.horas_trabajadas) + "$" + "\n")
        print("Pago por hora: " + str(self.pago_por_hora) + "$" + "\n")
        print("Pago Mensual: " + str(self.calcular_salario()) + "$" + "\n")