import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from sensor import SensorTemperatura, SensorHumedad
from actuador import ActuadorLuz, ActuadorPuerta
from drop_label import DropLabel  # Reutiliza el DropLabel del código anterior

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        taskbar_layout = QHBoxLayout()

        # Crear instancias de los sensores y actuadores
        sensor_temp = SensorTemperatura()
        sensor_humedad = SensorHumedad()
        actuador_luz = ActuadorLuz()
        actuador_puerta = ActuadorPuerta()

        # Crear etiquetas para arrastrar los objetos
        taskbar_layout.addWidget(self.create_draggable_label(sensor_temp))
        taskbar_layout.addWidget(self.create_draggable_label(sensor_humedad))
        taskbar_layout.addWidget(self.create_draggable_label(actuador_luz))
        taskbar_layout.addWidget(self.create_draggable_label(actuador_puerta))

        taskbar_widget = QWidget()
        taskbar_widget.setLayout(taskbar_layout)

        # Crear área de mapa (DropLabel)
        self.drop_label = DropLabel("Suelta los objetos aquí")

        layout.addWidget(taskbar_widget)
        layout.addWidget(self.drop_label)
        self.setLayout(layout)

    def create_draggable_label(self, iot_object):
        """Crea un QLabel arrastrable para un objeto IoT."""
        label = QLabel(iot_object.get_name(), self)
        label.setPixmap(iot_object.get_pixmap())
        label.setFixedSize(60, 60)
        return label
