class DispositivoRed:
    def __init__(self, nombre_dispositivo , direccion_ip, estado):
        self.nombre_dispositivo = nombre_dispositivo
        self.direccion_ip = direccion_ip
        self.estado = estado

    def mostrar_dispositivo(self):
        print("Dispositivo: " + self.nombre_dispositivo + "\n")
        print("IP: " + self.direccion_ip + "\n")
        print("Estado: " + self.estado + "\n")

    def activar(self):
        if(self.estado == "Activo"):
            print("El dispositivo: " + self.nombre_dispositivo + "ya esta activo")
            return
        self.estado = "Activo"
        print("Se ha activado el dispositvo: "  + self.nombre_dispositivo)

    def desactivar(self):
        if self.estado == "Inactivo":
            print("El dispositivo: " + self.nombre_dispositivo + " ya está inactivo")
            return
        self.estado = "Inactivo"
        print("Se ha desactivado el dispositivo: " + self.nombre_dispositivo)

    def verificar_conexion(self):
        if(self.estado == "Activo"):
            print("Conexión: El dispositivo está conectado a la red.")
        elif(self.estado == "Inactivo"):
            print("Conexión: El dispositivo no está conectado a la red.")
    