from PyQt6.QtGui import QPixmap

class IoTObject:
    """Clase base para todos los objetos IoT."""
    def __init__(self, name, image_path):
        self.name = name
        self.pixmap = QPixmap(image_path).scaled(60, 60)

    def get_name(self):
        return self.name

    def get_pixmap(self):
        return self.pixmap
