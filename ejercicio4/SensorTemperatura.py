class SensorTemperatura:
    def __init__(self, ubicacion, temperatura):
        self.__ubicacion = ubicacion
        self.__temperatura = temperatura

    def mostrar_temperatura(self):
        print("La temperatura es: " + str(self.__temperatura))

    def verificar_estado(self):
        if(self.__temperatura <= 30):
            print("Temperatura normal")
        elif(self.__temperatura > 30):
            print("Alerta: temperatura elevada")
