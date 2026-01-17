from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ComponentPalette(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        for name in ["Resistor", "Capacitor", "Inductor", "Diode", "Source"]:
            btn = QPushButton(name)
            btn.setStyleSheet("background:#2c3e50;color:white;padding:8px;border-radius:6px;")
            layout.addWidget(btn)

        self.setLayout(layout)
