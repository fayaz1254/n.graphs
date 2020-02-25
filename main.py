from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from xml.etree.ElementTree import parse, dump

import networkx as nx
import os


class Graph(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        loadUi("main.ui", self)
        self.GraphFigure.figure.clf()
        self.setWindowTitle("N.Graphs")
        self.addGraph.clicked.connect(self.update_graph)
        self.addToolBar(NavigationToolbar(self.GraphFigure.canvas, self))

    def update_graph(self):
        self.GraphFigure.figure.clf()
        file = ("dolphins.gml")

        a = None
        G = None
        d = None
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".gml":
            G = nx.read_gml(file)
            d = dict(G.degree)
        else:
            a = mmread(file)
            G = nx.from_scipy_sparse_matrix(a, parallel_edges=False, create_using=None, edge_attribute='weight')
            d = dict(G.degree)
        nx.draw(G, node_size=[v*125 for v in d.values()])
        self.GraphFigure.canvas.draw()

app = QApplication([])
window = Graph()
window.show()
app.exec_()
