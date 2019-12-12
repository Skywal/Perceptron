import sys # needed to pass argv into QApplication
import os
from PyQt5 import QtWidgets

from design import perceptron as design # converted design file

class PerceptronApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self) # this needed for initializing of design

        self.selectButton.clicked.connect(self.browse_folder)
    
    def browse_folder(self):
        self.filenameInput.clear()
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")[0]

        if file_name:
            self.filenameInput.setText(str(file_name))

def main():
    app = QtWidgets.QApplication(sys.argv) # new instance of QApplication
    window = PerceptronApp() # create object of PerceptronApp
    window.show() # show the window
    app.exec_() # start app

# if we start file directly
if __name__ == "__main__":
    main()