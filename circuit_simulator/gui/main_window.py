from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from gui.toolbar import ToolBar
from gui.canvas import CircuitCanvas
from gui.component_palette import ComponentPalette
from gui.plotting import PlotWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Open Circuit Simulator")
        self.setGeometry(100, 100, 1200, 800)

        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

        self.canvas = CircuitCanvas()
        self.palette = ComponentPalette()
        self.plot_window = PlotWindow()

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.palette)
        layout.addWidget(self.canvas)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
