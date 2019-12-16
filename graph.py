from PyQt5 import Qt
import pyqtgraph as pg
import numpy as np

class Graph(Qt.QWidget):
"""Widget class that displays graph"""

    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self) # create layout

        self.view = view = pg.PlotWidget() # make a plot area
        view.setBackground('w')
        
        # remove axis from plot
        view.hideAxis('left')
        view.hideAxis('bottom')
        
        layout.addWidget(self.view) # show up plot area

        self.line_pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.trand_line = view.plot(pen=self.line_pen) # create instance of a line

        # create instance of one of dots they will be reusable
        self.first_dot_cloud = view.plot(pen=None, symbol='o', symbolPen=None,
                                            symbolSize=10, symbolBrush='m')

        self.second_dot_cloud = view.plot(pen=None, symbol='t', symbolPen=None,
                                            symbolSize=10, symbolBrush='b')
        

    def plot_first_dots(self,x=[0], y=[0]):
        """Draw dot like graph with dots coord 'x' and 'y'"""
        self.first_dot_cloud.setData(x, y)

    def plot_second_dots(self,x=[0], y=[0]):
        """Draw dot like graph with dots coord 'x' and 'y'"""
        self.second_dot_cloud.setData(x, y)

    def plot_line(self, x=[0], y=[0]):
        """Draw line graph with dots coord 'x' and 'y'"""
        self.trand_line.setData(x, y)

if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Graph()
    w.show()
    app.exec()
