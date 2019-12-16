# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perceptron.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FileLayout = QtWidgets.QHBoxLayout()
        self.FileLayout.setObjectName("FileLayout")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setObjectName("fileLabel")
        self.FileLayout.addWidget(self.fileLabel)
        self.filenameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameInput.setObjectName("filenameInput")
        self.FileLayout.addWidget(self.filenameInput)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.FileLayout.addWidget(self.loadButton)
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setObjectName("selectButton")
        self.FileLayout.addWidget(self.selectButton)
        self.verticalLayout.addLayout(self.FileLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.GraphicLayout = QtWidgets.QHBoxLayout()
        self.GraphicLayout.setObjectName("GraphicLayout")
        self.graphic = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphic.sizePolicy().hasHeightForWidth())
        self.graphic.setSizePolicy(sizePolicy)
        self.graphic.setMinimumSize(QtCore.QSize(500, 500))
        self.graphic.setObjectName("graphic")
        self.GraphicLayout.addWidget(self.graphic)
        self.horizontalLayout_4.addLayout(self.GraphicLayout)
        self.StateLayout = QtWidgets.QVBoxLayout()
        self.StateLayout.setObjectName("StateLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.StateLayout.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_3.addWidget(self.StartButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MaxiTextVertLayout = QtWidgets.QVBoxLayout()
        self.MaxiTextVertLayout.setObjectName("MaxiTextVertLayout")
        self.maxNumOfEpochsLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxNumOfEpochsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxNumOfEpochsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxNumOfEpochsLabel.setObjectName("maxNumOfEpochsLabel")
        self.MaxiTextVertLayout.addWidget(self.maxNumOfEpochsLabel)
        self.maxErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxErrorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxErrorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxErrorLabel.setObjectName("maxErrorLabel")
        self.MaxiTextVertLayout.addWidget(self.maxErrorLabel)
        self.horizontalLayout.addLayout(self.MaxiTextVertLayout)
        self.MaxInputVertLayout = QtWidgets.QVBoxLayout()
        self.MaxInputVertLayout.setObjectName("MaxInputVertLayout")
        self.maxNumEpochInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxNumEpochInput.sizePolicy().hasHeightForWidth())
        self.maxNumEpochInput.setSizePolicy(sizePolicy)
        self.maxNumEpochInput.setMinimumSize(QtCore.QSize(50, 0))
        self.maxNumEpochInput.setObjectName("maxNumEpochInput")
        self.MaxInputVertLayout.addWidget(self.maxNumEpochInput)
        self.maxErrorInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxErrorInput.sizePolicy().hasHeightForWidth())
        self.maxErrorInput.setSizePolicy(sizePolicy)
        self.maxErrorInput.setMinimumSize(QtCore.QSize(50, 0))
        self.maxErrorInput.setObjectName("maxErrorInput")
        self.MaxInputVertLayout.addWidget(self.maxErrorInput)
        self.horizontalLayout.addLayout(self.MaxInputVertLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StateTextVertLayout = QtWidgets.QVBoxLayout()
        self.StateTextVertLayout.setObjectName("StateTextVertLayout")
        self.passedEpochLabel = QtWidgets.QLabel(self.centralwidget)
        self.passedEpochLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passedEpochLabel.setObjectName("passedEpochLabel")
        self.StateTextVertLayout.addWidget(self.passedEpochLabel)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.StateTextVertLayout.addWidget(self.errorLabel)
        self.horizontalLayout_2.addLayout(self.StateTextVertLayout)
        self.StateStateVertLayout = QtWidgets.QVBoxLayout()
        self.StateStateVertLayout.setObjectName("StateStateVertLayout")
        self.passedEpochsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passedEpochsInput.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passedEpochsInput.sizePolicy().hasHeightForWidth())
        self.passedEpochsInput.setSizePolicy(sizePolicy)
        self.passedEpochsInput.setMinimumSize(QtCore.QSize(50, 0))
        self.passedEpochsInput.setObjectName("passedEpochsInput")
        self.StateStateVertLayout.addWidget(self.passedEpochsInput)
        self.errorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.errorInput.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorInput.sizePolicy().hasHeightForWidth())
        self.errorInput.setSizePolicy(sizePolicy)
        self.errorInput.setMinimumSize(QtCore.QSize(50, 0))
        self.errorInput.setObjectName("errorInput")
        self.StateStateVertLayout.addWidget(self.errorInput)
        self.horizontalLayout_2.addLayout(self.StateStateVertLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.StateLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.StateLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Perceptron"))
        self.fileLabel.setText(_translate("MainWindow", "File:"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.selectButton.setText(_translate("MainWindow", "Select"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.maxNumOfEpochsLabel.setText(_translate("MainWindow", "Maximum number of epochs:"))
        self.maxErrorLabel.setText(_translate("MainWindow", "Maximum error:"))
        self.passedEpochLabel.setText(_translate("MainWindow", "Passed epochs:"))
        self.errorLabel.setText(_translate("MainWindow", "Error:"))
