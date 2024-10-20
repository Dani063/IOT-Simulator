from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QPainter, QDrag
from PyQt6.QtCore import QMimeData, Qt

class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(DropLabel, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setFixedSize(2020, 1080)  # Tamaño grande para el drop label
        self.setStyleSheet("background-color: lightgray; padding: 10px;")
        self.images = []  # Lista para almacenar imágenes arrastrables
        self.background_pixmap = None  # Imagen de fondo

    def set_background_image(self, image_path):
        """Establece la imagen de fondo del DropLabel."""
        self.background_pixmap = QPixmap(image_path).scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.update()

    def dragEnterEvent(self, event):
        if event.mimeData().hasText() or event.mimeData().hasImage():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            image = event.mimeData().imageData()
            pixmap = QPixmap.fromImage(image)

            # Obtener la posición donde se soltó la imagen
            drop_position = event.pos()

            # Agregar la imagen arrastrable a la lista
            self.images.append((pixmap, drop_position))
            self.update()

        event.acceptProposedAction()

    def paintEvent(self, event):
        """Dibuja el fondo y todas las imágenes en las posiciones almacenadas."""
        painter = QPainter(self)

        if self.background_pixmap:
            painter.drawPixmap(self.rect(), self.background_pixmap)

        for pixmap, position in self.images:
            painter.drawPixmap(position.x(), position.y(),
                               pixmap.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        painter.end()
