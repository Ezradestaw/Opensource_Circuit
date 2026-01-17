from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.figure = Figure(figsize=(5,4))
        self.canvas = Canvas(self.figure)

        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, x, y):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_title("Simulation Result")
        self.canvas.draw()
