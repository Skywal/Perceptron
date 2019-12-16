import sys # needed to pass argv into QApplication
import os
from PyQt5 import QtWidgets
import pyqtgraph as pg

from design import perceptron as design # converted design file

import graph

class PerceptronApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self) # this needed for initializing of design
        
        # bind events and event holders
        self.selectButton.clicked.connect(self.browse_folder) 
        self.loadButton.clicked.connect(self.load_data)

        self.graph_widg = graph.Graph() # create instance of the graph class
        self.graph_layout = QtWidgets.QVBoxLayout(self.graphic) # creating layout inside an empty widget
        
        #self.graphic.setParent(None) # delete widget in case of parent reposition

        self.graph_layout.addWidget(self.graph_widg) # add graph widget insige layout
            
    def browse_folder(self):
        """Select file from local disc"""

        self.filenameInput.clear() # cleat the line before writing
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")[0]

        if file_name:
            self.filenameInput.setText(str(file_name)) # write a string 
    
    def load_data(self):
        """Open selected file"""
        pass
        
    def plot_data(self):
        """Plot data on the graph widget"""

        self.graph_widg.plot_line()
        self.graph_widg.plot_first_dots()
        self.graph_widg.plot_second_dots((0,1,2,3,4,5,6),(0,1,2,3,4,5,6))


def main():

    app = QtWidgets.QApplication(sys.argv) # new instance of QApplication
    window = PerceptronApp() # create object of PerceptronApp
    window.show() # show the window
    app.exec_() # start app

# if we start file directly
if __name__ == "__main__":
    main()