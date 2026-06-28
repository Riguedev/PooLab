from Empleado import Empleado

# 1. Creamos 3 instancias de la clase Empleado
empleado1 = Empleado("Ana Martínez", "Desarrolladora Frontend", 160, 25)
empleado2 = Empleado("Carlos Ruiz", "Diseñador UX", 140, 20)
empleado3 = Empleado("Sofía Gómez", "Gerente de Proyecto", 180, 35)

# 2. Mostramos la información de cada uno usando el método de tu clase
print("=== INFORMACIÓN DE LOS EMPLEADOS ===\n")

print("--- Primer Empleado --- \n")
empleado1.mostrar_informacion()

print("--- Segundo Empleado --- \n")
empleado2.mostrar_informacion()

print("--- Tercer Empleado --- \n")
empleado3.mostrar_informacion()