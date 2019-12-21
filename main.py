import sys # needed to pass argv into QApplication
import os
from PyQt5 import QtWidgets
import pyqtgraph as pg

from design import perceptron as design # converted design file

import graph
import database as db
import neural_manager as n_manager


""" Main window """
class PerceptronApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self) # this needed for initializing of design
        
        self.init_vars() # make instance of all global variables for this class
        self.init_extern() # initialise all variables from external modules

        self.set_up_inputs() # set up start value at active text inputs 

        self.event_holders() # bind events and event holders
        
    
    def init_vars(self):
        """ Initial setup of the global variables """

        self.maxNumEpoch = 1000 # maximum number of epochs that will be perform at training model
        self.maxError = 0 # maximal possible error of data evaluation
        self.passedEpochs = 0 # epoch count that passed before successfull training
        self.error = 0 # actual error of data evaluation

        self.optimal_epochs = 0 # epochs passed before optimal weights value was found
        self.optimal_weights = [] # weights with smallest error 

    def init_extern(self):
        """ Initialize all variables from orther modules aka by reference"""

        self.database = db.Database() # create instance of database object to work with .CSV file and data
        
        self.setup_graph() # implementing graph output 

    def set_up_inputs(self):
        """ Set text in input boxes at start"""
        self.maxNumEpochInput.setText(str(self.maxNumEpoch))
        self.maxErrorInput.setText(str(self.maxError))

        self.errorInput.setText("")
        self.passedEpochsInput.setText("")

    def read_inputs(self):
        """ Read data from active text inputs """
        if self.maxNumEpochInput.text():
            self.maxNumEpoch = int(self.maxNumEpochInput.text())
        else:
            self.maxNumEpoch = 0

        if self.maxErrorInput.text():    
            self.maxError = float(self.maxErrorInput.text())
        else:
            self.maxError = 0


    def neuron(self, synapses, max_error, epochs):
        
        self.net_manager = n_manager.NetManager(database=self.database.get_data(), synapses=synapses, max_error=max_error)
        
        self.net_manager.train_network(epochs=epochs)

    def calculate_line(self):
        ## TEST 
        db_data = list(self.database.get_data())
        line_list = [] # x1 raw
        
        for i in range(len(db_data)):
            line_list.append(db_data[i][0:1])
        
        final_line =[] # x1
        
        for i in range(len(line_list)):
            final_line.append(float(line_list[i][0]))
        
        line_x2 = (self.net_manager.predict_2d(final_line))
        
        return final_line, line_x2
    
    def plot_line(self, x1_arr, x2_arr):
        self.graph_widg.plot_line(x1_arr, x2_arr)

    def neural_sequence(self):
        """ Neuron initialuze, train, predict and plot predictions sequence """

        synapses = len(self.database.get_data()[0][:-1]) # how many input data columns are in the list

        self.neuron(epochs=self.maxNumEpoch, max_error=self.maxError, synapses=synapses)
        
        if synapses <= 2:
            x1_arr, x2_arr =self.calculate_line() 
            self.plot_line(x1_arr, x2_arr)
        
        self.passedEpochs = self.net_manager.get_epochs_passed()
        self.error = self.net_manager.get_error()
        self.optimal_epochs = self.net_manager.get_opt_epochs()
        self.optimal_weights = self.net_manager.swap_weights()

        self.text_out([0])
    

    def text_out(self, weights=[0]):
        """ Output text-info into all available information outputs """
        self.errorInput.setText(str(self.error))
        self.passedEpochsInput.setText(str(self.passedEpochs))

        self.listWidget.addItem(f"\nMaximum number of epochs = {self.maxNumEpoch}, Maximum error = {self.maxError}")
        self.listWidget.addItem(f"Passed epochs = {self.passedEpochs}, error = {self.error}")
        self.listWidget.addItem(f"Optimal values ​​of the synaptic weights were found after {self.optimal_epochs} epochs:")
        
        for i in range(len(self.optimal_weights)):
            self.listWidget.addItem(f"w{i}={self.optimal_weights[i]}")


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
        """ Open selected file and read the data on Load button press """
        
        self.restart_all() # before start new session set up all to start state

        self.database.read_csv(self.filenameInput.text())
        
        # ouptut on text widget
        self.listWidget.addItem(f"{self.database.get_items_count()} input vectors in {self.database.get_items_dimensions()}-dimensional space have been loaded")

        print("--=== Plotting data! ===--")
        self.plot_data() # graph plot

    def start_action(self):
        """ Begin action on start button """
        self.read_inputs()

        self.neural_sequence()


    def setup_graph(self):
        """ Initial setup of the graphical output """

        self.graph_widg = graph.Graph() # create instance of the graph class
        self.graph_layout = QtWidgets.QVBoxLayout(self.graphic) # creating layout inside an empty widget
        
        #self.graphic.setParent(None) # delete widget in case of parent reposition

        self.graph_layout.addWidget(self.graph_widg) # add graph widget insige layout
        
    def plot_data(self):
        """Plot data on the graph widget"""
        
        list_zero, list_one = self.database.data_separation(self.database.get_data()) # split input data by last row value

        self.graph_widg.plot_first_from_list(list_zero) # blue dots
        self.graph_widg.plot_second_from_list(list_one) # red dots

        
    def restart_all(self):
        """ Bring all current state to start state """

        self.listWidget.clear() # delete all output
        
        self.plot_line([0], [0]) # erase builded line
        
        self.init_vars() # reset all global variables
        self.set_up_inputs() # reset data in active text inputs
        


def main():

    app = QtWidgets.QApplication(sys.argv) # new instance of QApplication
    window = PerceptronApp() # create object of PerceptronApp
    window.show() # show the window
    app.exec_() # start app

# if we start file directly
if __name__ == "__main__":
    main()