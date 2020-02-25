from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class GraphFigure(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
