from iot_object import IoTObject

class Actuador(IoTObject):
    """Clase base para todos los actuadores."""
    def __init__(self, name, image_path):
        super().__init__(name, image_path)

class ActuadorLuz(Actuador):
    """Actuador de luz específico."""
    def __init__(self):
        super().__init__("Actuador de Luz", "path/to/light_actuator_image.png")

class ActuadorPuerta(Actuador):
    """Actuador para abrir/cerrar puertas."""
    def __init__(self):
        super().__init__("Actuador de Puerta", "path/to/door_actuator_image.png")
