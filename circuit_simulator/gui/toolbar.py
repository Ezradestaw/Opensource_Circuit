from PyQt5.QtWidgets import QToolBar, QAction

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Tools", parent)

        self.addAction(QAction("Run", self))
        self.addAction(QAction("Clear", self))
        self.addAction(QAction("Zoom +", self))
        self.addAction(QAction("Zoom -", self))
        self.addAction(QAction("Undo", self))
        self.addAction(QAction("Redo", self))
