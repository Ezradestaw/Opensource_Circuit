from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class CircuitCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(500)
        self.setStyleSheet("background-color: #1e1e1e;")

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.white, 2)
        painter.setPen(pen)
        painter.drawText(20, 30, "Draw your circuit here...")
