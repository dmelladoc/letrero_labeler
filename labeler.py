# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from glob import glob
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(100, 100, 1000, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(10, 10, 981, 401))
        self.imagen.setText("")
        self.imagen.setObjectName("imagen")
        self.btnOn = QtWidgets.QPushButton(self.centralwidget)
        self.btnOn.setGeometry(QtCore.QRect(20, 430, 411, 41))
        self.btnOn.setObjectName("btnOn")
        self.btnOn.clicked.connect(self.onEncendido)

        self.btnOff = QtWidgets.QPushButton(self.centralwidget)
        self.btnOff.setGeometry(QtCore.QRect(570, 430, 411, 41))
        self.btnOff.setObjectName("btnOff")
        self.btnOff.clicked.connect(self.onApagado)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 480, 821, 21))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 410, 991, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(850, 480, 131, 21))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.onSave)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 22))
        self.menubar.setObjectName("menubar")

        self.menuAbrir = QtWidgets.QMenu(self.menubar)
        self.menuAbrir.setObjectName("menuAbrir")
        self.menuAbrir.triggered.connect(self.openFolder)

        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
    
        self.actionSiguiente = QtWidgets.QAction(MainWindow)
        self.actionSiguiente.setObjectName("actionSiguiente")
        self.actionSiguiente.triggered.connect(self.moveNext)
    
        self.actionAnterior = QtWidgets.QAction(MainWindow)
        self.actionAnterior.setObjectName("actionAnterior")
        self.actionAnterior.triggered.connect(self.movePrev)
    
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuVista.addAction(self.actionSiguiente)
        self.menuVista.addAction(self.actionAnterior)
        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #otros
        self.curIndex = 0
        self.information = pd.DataFrame(columns=["Archivo", "Label"])
        self.curFile = ""


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LetreroLabel"))
        self.btnOn.setText(_translate("MainWindow", "Encendido"))
        self.btnOff.setText(_translate("MainWindow", "Apagado"))
        self.label.setText(_translate("MainWindow", "Archivo:"))
        self.btnSave.setText(_translate("MainWindow", "Guardar"))
        self.menuAbrir.setTitle(_translate("MainWindow", "Archivo"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir Carpeta"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSiguiente.setText(_translate("MainWindow", "Siguiente"))
        self.actionSiguiente.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAnterior.setText(_translate("MainWindow", "Anterior"))
        self.actionAnterior.setShortcut(_translate("MainWindow", "Ctrl+A"))


    def openFolder(self):
        dirpath = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Seleccionar Carpeta", "D:\\otros\\express", QtWidgets.QFileDialog.ShowDirsOnly))
        self.allfiles = glob(os.path.join(dirpath, "*.jpg"))
        self.allfiles.sort()
        self.curIndex = 0
        self.nFiles = len(self.allfiles)
        self.setimage(0)
        
    def setimage(self, index):
        if index >= len(self.allfiles):
            index = -1
        path = self.allfiles[index]
        self.imagen.setPixmap(QtGui.QPixmap(path))
        self.label.setText("[{:5d}/{:5d}] ".format(index+1, self.nFiles) + path)
        self.curFile = path

    def moveNext(self):
        self.curIndex += 1
        self.setimage(self.curIndex)
    
    def movePrev(self):
        self.curIndex -= 1
        self.setimage(self.curIndex)

    def onEncendido(self):
        self.information = self.information.append({"Archivo": os.path.basename(self.curFile),
                                                    "Label": 1}, ignore_index=True)
        self.moveNext()

    def onApagado(self):
        self.information = self.information.append({"Archivo": os.path.basename(self.curFile),
                                                    "Label": 0}, ignore_index=True)
        self.moveNext()
    
    def onSave(self):
        #Eliminamos posibles repetidos
        self.information = self.information.drop_duplicates(subset="Archivo",
                                                            keep='last', 
                                                            ignore_index=True)
        self.information.to_csv("etiquetados.csv", index=False)

                

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

