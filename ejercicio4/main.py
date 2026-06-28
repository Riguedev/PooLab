from SensorTemperatura import SensorTemperatura

sala_de_conferencias = SensorTemperatura("Sala de Conferencias", 24)
salones_de_clases = SensorTemperatura("Salones de Clases", 20)
sala_de_servidores = SensorTemperatura("Sala de Servidores", 35)

print("-- Estado del Sensor de la Sala de Conferencias --")
sala_de_conferencias.mostrar_temperatura()
sala_de_conferencias.verificar_estado()

print("-- Estado del Sensor de la Sala de Conferencias --")
salones_de_clases.mostrar_temperatura()
salones_de_clases.verificar_estado()

print("-- Estado del Sensor de la Sala de Servidores --")
sala_de_servidores.mostrar_temperatura()
sala_de_servidores.verificar_estado()