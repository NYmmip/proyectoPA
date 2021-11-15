from verDatos import *
from ingresarDatos import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def openVD(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_verDatos()
        self.ui.setupUi(self.window, MainWindow)
        MainWindow.hide()
        self.window.show()

    def openIDA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ingresarDatos()
        self.ui.setupUi(self.window, MainWindow)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeL = QtWidgets.QLabel(self.centralwidget)
        self.welcomeL.setGeometry(QtCore.QRect(130, 70, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.welcomeL.setFont(font)
        self.welcomeL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcomeL.setObjectName("welcomeL")

        self.ingrearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openIDA())
        self.ingrearButton.setGeometry(QtCore.QRect(150, 180, 131, 51))
        self.ingrearButton.setObjectName("ingrearButton")

        self.cerrarButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openIDA())
        self.cerrarButton.setGeometry(QtCore.QRect(150, 180, 131, 51))
        self.cerrarButton.setObjectName("ingrearButton")

        self.verDatosButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openVD())
        self.verDatosButton.setGeometry(QtCore.QRect(150, 240, 131, 51))
        self.verDatosButton.setObjectName("verDatosButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIngresar = QtWidgets.QAction(MainWindow)
        self.actionIngresar.setObjectName("actionIngresar")
        self.actionVer_Datos = QtWidgets.QAction(MainWindow)
        self.actionVer_Datos.setObjectName("actionVer_Datos")
        self.menuMenu.addAction(self.actionIngresar)
        self.menuMenu.addAction(self.actionVer_Datos)
        self.menubar.addAction(self.menuMenu.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeL.setText(_translate("MainWindow", "BIENVENIDO"))
        self.ingrearButton.setText(_translate("MainWindow", "INGRESAR DATOS"))
        self.verDatosButton.setText(_translate("MainWindow", "VER DATOS"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.actionVer_Datos.setText(_translate("MainWindow", "Ver Datos"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

