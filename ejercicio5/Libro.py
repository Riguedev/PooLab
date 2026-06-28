class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Éxito: El libro " + self.titulo + " ha sido prestado.\n")
        else:
            print("Error: El libro " + self.titulo + " ya está prestado y no se puede prestar. \n")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Éxito: El libro " + self.titulo + " ha sido devuelto y ahora está disponible.\n")
        else:
            print(f"Mensaje: El libro " + self.titulo + " ya estaba en la biblioteca.\n")

    def mostrar_estado(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print("Libro: " + self.titulo + " | Autor: " + self.autor + " | Estado: " + estado + "\n")