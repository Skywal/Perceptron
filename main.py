import sys # needed to pass argv into QApplication
import os
from PyQt5 import QtWidgets
import pyqtgraph as pg

from design import perceptron as design # converted design file

import graph
import database as db


""" Main window """
class PerceptronApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self) # this needed for initializing of design
        
        self.setup_vars() # make instance of all global variables for this class

        self.start_conditions() # apply firs start condition 

        self.event_holders() # bind events and event holders

        self.setup_graph() # implementing graph output 
    
    def setup_vars(self):
        """ Initial setup of the global variables """

        self.maxNumEpoch = 1000 # maximum number of epochs that will be perform at training model
        self.maxError = 0 # maximal possible error of data evaluation
        self.passedEpochs = 0 # epoch count that passed before successfull training
        self.error = 0 # actual error of data evaluation

        self.database = db.Database() # create instance of database object to work with .CSV file and data
    
    def setup_graph(self):
        """ Initial setup of the graphical output """

        self.graph_widg = graph.Graph() # create instance of the graph class
        self.graph_layout = QtWidgets.QVBoxLayout(self.graphic) # creating layout inside an empty widget
        
        #self.graphic.setParent(None) # delete widget in case of parent reposition

        self.graph_layout.addWidget(self.graph_widg) # add graph widget insige layout

    def start_conditions(self):
        self.maxNumEpochInput.setText(str(self.maxNumEpoch))
        self.maxErrorInput.setText(str(self.maxError))

    def event_holders(self):
        """ Bind events """

        self.selectButton.clicked.connect(self.browse_folder_action) 
        self.loadButton.clicked.connect(self.load_data_action)
        self.StartButton.clicked.connect(self.start_action)

    def browse_folder_action(self):
        """Select file from local disc by button press"""

        self.filenameInput.clear() # cleat the line before writing
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")[0]

        if file_name:
            self.filenameInput.setText(str(file_name)) # write a string 
    
    def load_data_action(self):
        """Open selected file and read the data by button press"""
        
        self.database.read_csv(self.filenameInput.text())
        
        print("--=== Plotting data! ===--")
        self.plot_data()
        
    def plot_data(self):
        """Plot data on the graph widget"""
        
        # split input data by last row value
        list_zero, list_one = self.database.data_separation(self.database.get_data())

        self.graph_widg.plot_first_from_list(list_zero) # blue dots
        self.graph_widg.plot_second_from_list(list_one) # red dots
        
    def start_action(self):
        pass


def main():

    app = QtWidgets.QApplication(sys.argv) # new instance of QApplication
    window = PerceptronApp() # create object of PerceptronApp
    window.show() # show the window
    app.exec_() # start app

# if we start file directly
if __name__ == "__main__":
    main()