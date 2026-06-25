class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)
        print("Carrera: " + self.carrera)


estudiante1 = Estudiante("Jesús", "22", "Técnico en Desarollo de Software")
estudiante2 = Estudiante("Reyna", "23", "Técnico en Electronica")

estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()