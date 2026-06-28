#Importamos las clase Estudiante al Script
from Estudiante import Estudiante

#Creamos dos estudiantes (Instancias de la clase Estudiante)
estudiante1 = Estudiante("Jesús", "22", "Técnico en Desarollo de Software")
estudiante2 = Estudiante("Reyna", "23", "Técnico en Electronica")

#Utilizamos el metodo "mostrar_informacion" para mostrar los datos del objeto en pantalla
estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()