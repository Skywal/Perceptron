import sys # needed to pass argv into QApplication
from PyQt5 import QtWidgets

from design import perceptron as design # converted design file

class PerceptronApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        
        # here access to variables, methods etc. in perceptron.py file

        super().__init__()
        self.setupUi(self) # this needed for initializing of design
    

def main():
    app = QtWidgets.QApplication(sys.argv) # new instance of QApplication
    window = PerceptronApp() # create object of PerceptronApp
    window.show() # show the window
    app.exec_() # start app

# if we start file directly
if __name__ == "__main__":
    main()