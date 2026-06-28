class Estudiante:
    def __init__(self, nombre, edad, carrera): #Definicion de las propiedades
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    #Este metodo permite mostrar la informacion que contiene el Objero
    def mostrar_informacion(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)
        print("Carrera: " + self.carrera)
