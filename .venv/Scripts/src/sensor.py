from iot_object import IoTObject

class Sensor(IoTObject):
    """Clase base para todos los sensores."""
    def __init__(self, name, image_path):
        super().__init__(name, image_path)

class SensorTemperatura(Sensor):
    """Sensor de temperatura específico."""
    def __init__(self):
        super().__init__("Sensor de Temperatura", "path/to/temperature_sensor_image.png")

class SensorHumedad(Sensor):
    """Sensor de humedad específico."""
    def __init__(self):
        super().__init__("Sensor de Humedad", "path/to/humidity_sensor_image.png")
