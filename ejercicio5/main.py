from Libro import Libro

#Creamos los dos libros
libro1 = Libro("Harry Potter: y la piedara filosofal", "JK Rowling")
libro2 = Libro("Habitos Atomicos", "James Clear")

#Prestamos el Libro 2

libro2.prestar()

#Intentamos Prestarlo Nuevamente

libro2.prestar()

#Devolveremos el Libro 2
libro2.devolver()

#Mostramos los estados de los libros

print("Estado del Libro 1 \n")
libro1.mostrar_estado()

print("Estado del Libro 2 \n")
libro2.mostrar_estado()