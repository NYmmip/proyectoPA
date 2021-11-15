from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD.crudEstudiantes import *
from CRUD.crudProfesores import *
from CRUD.crudEvaluacion import *
from CRUD.crudInvestigacion import *
from CRUD.crudPublicaciones import *
from CRUD.crudResultadoEvaluaciones import *
from CRUD.crudTemas import *


class Ui_verDatos(object):
    def openMenu(self, main_w, verDatos):
        verDatos.close()
        main_w.show()

    def setupUi(self, verDatos, MainWindow):
        verDatos.setObjectName("verDatos")
        verDatos.resize(608, 399)
        self.centralwidget = QtWidgets.QWidget(verDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 581, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.buttonInicio = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openMenu(MainWindow, verDatos))
        self.buttonInicio.setGeometry(QtCore.QRect(270, 320, 121, 31))
        self.buttonInicio.setObjectName("buttonInicio")
        self.estudianteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda :self.showEstudiantes())
        self.estudianteButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.estudianteButton.setObjectName("estudianteButton")
        self.profesorButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda :self.showProfesores())
        self.profesorButton.setGeometry(QtCore.QRect(85, 10, 75, 23))
        self.profesorButton.setObjectName("profesorButton")
        self.evaluacionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showEvaluaciones())
        self.evaluacionButton.setGeometry(QtCore.QRect(160, 10, 75, 23))
        self.evaluacionButton.setObjectName("evaluacionButton")
        self.investigacionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showInvestigaciones())
        self.investigacionButton.setGeometry(QtCore.QRect(235, 10, 90, 23))
        self.investigacionButton.setObjectName("investigacionButton")
        self.publicacionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showPublicaciones())
        self.publicacionButton.setGeometry(QtCore.QRect(325, 10, 90, 23))
        self.publicacionButton.setObjectName("PublicacionButton")
        self.resultadosButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showResultados())
        self.resultadosButton.setGeometry(QtCore.QRect(415, 10, 75, 23))
        self.resultadosButton.setObjectName("resultadosButton")
        self.temaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showTemas())
        self.temaButton.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.temaButton.setObjectName("temaButton")
        verDatos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(verDatos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        verDatos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(verDatos)
        self.statusbar.setObjectName("statusbar")
        verDatos.setStatusBar(self.statusbar)
        self.actionInicio = QtWidgets.QAction(verDatos)
        self.actionInicio.setObjectName("actionInicio")
        self.actionIngresar_Datos = QtWidgets.QAction(verDatos)
        self.actionIngresar_Datos.setObjectName("actionIngresar_Datos")
        self.menuMenu.addAction(self.actionInicio)
        self.menuMenu.addAction(self.actionIngresar_Datos)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(verDatos)
        QtCore.QMetaObject.connectSlotsByName(verDatos)


    def retranslateUi(self, verDatos):
        _translate = QtCore.QCoreApplication.translate
        verDatos.setWindowTitle(_translate("verDatos", "MainWindow"))
        self.buttonInicio.setText(_translate("verDatos", "Inicio"))
        self.estudianteButton.setText(_translate("verDatos", "Estudiantes"))
        self.profesorButton.setText(_translate("verDatos", "Profesores"))
        self.evaluacionButton.setText(_translate("verDatos", "Evaluaciones"))
        self.investigacionButton.setText(_translate("verDatos", "Investigaciones"))
        self.publicacionButton.setText(_translate("verDatos", "Publicaciones"))
        self.resultadosButton.setText(_translate("verDatos", "Resultados"))
        self.temaButton.setText(_translate("verDatos", "Temas"))
        self.menuMenu.setTitle(_translate("verDatos", "Menu"))
        self.actionInicio.setText(_translate("verDatos", "Inicio"))
        self.actionIngresar_Datos.setText(_translate("verDatos", "Ingresar Datos"))

    def showEstudiantes(self):
        estudiantes = crudEstudiantes("localhost", "root", "Odiolapapa11", "pabd").getEstudiantes()
        attr = list(estudiantes[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(estudiantes))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(estudiantes):
            self.tableWidget.setItem(x,0,QtWidgets.QTableWidgetItem(str(y.numeroMatricula)))
            self.tableWidget.item(x,0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombre)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.apellido)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(y.investigacionId)))
            self.tableWidget.item(x, 3).setFlags(QtCore.Qt.ItemIsEnabled)

    def showProfesores(self):
        profesores = crudProfesores("localhost", "root", "Odiolapapa11", "pabd").getProfesores()
        attr = list(profesores[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(profesores))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(profesores):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.documento)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombreCompleto)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.modalidad)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(y.numeroExtension)))
            self.tableWidget.item(x, 3).setFlags(QtCore.Qt.ItemIsEnabled)

    def showEvaluaciones(self):
        evaluaciones = crudEvaluacion("localhost", "root", "Odiolapapa11", "pabd").getEvaluaciones()
        attr = list(evaluaciones[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(evaluaciones))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))
        for x, y in enumerate(evaluaciones):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.id)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombre)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.fecha)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(y.cantidadPreg)))
            self.tableWidget.item(x, 3).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(str(y.profesorDoc)))
            self.tableWidget.item(x, 4).setFlags(QtCore.Qt.ItemIsEnabled)

    def showInvestigaciones(self):
        evaluaciones = crudInvestigacion("localhost", "root", "Odiolapapa11", "pabd").getInvestigaciones()
        attr = list(evaluaciones[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(evaluaciones))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(evaluaciones):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.id)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombre)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.enfoque)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(y.temaId)))
            self.tableWidget.item(x, 3).setFlags(QtCore.Qt.ItemIsEnabled)

    def showPublicaciones(self):
        evaluaciones = crudPublicaciones("localhost", "root", "Odiolapapa11", "pabd").getPublicaciones()
        attr = list(evaluaciones[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(evaluaciones))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(evaluaciones):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.id)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombre)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.fecha)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(y.cantidadP)))
            self.tableWidget.item(x, 3).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(str(y.investigacionId)))
            self.tableWidget.item(x, 4).setFlags(QtCore.Qt.ItemIsEnabled)

    def showResultados(self):
        evaluaciones = crudResultadosEvaluacion("localhost", "root", "Odiolapapa11", "pabd").getResultados()
        attr = list(evaluaciones[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(evaluaciones))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(evaluaciones):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.nMatricualEstu)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.evaluacionId)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(y.resultado)))
            self.tableWidget.item(x, 2).setFlags(QtCore.Qt.ItemIsEnabled)

    def showTemas(self):
        evaluaciones = crudTemas("localhost", "root", "Odiolapapa11", "pabd").getTemas()
        attr = list(evaluaciones[0].__dict__.keys())
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(attr))
        self.tableWidget.setRowCount(len(evaluaciones))

        for x, y in enumerate(attr):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(x, item)
            item = self.tableWidget.horizontalHeaderItem(x)
            item.setText(_translate("verDatos", y))

        for x, y in enumerate(evaluaciones):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(y.id)))
            self.tableWidget.item(x, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(y.nombre)))
            self.tableWidget.item(x, 1).setFlags(QtCore.Qt.ItemIsEnabled)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verDatos = QtWidgets.QMainWindow()
    ui = Ui_verDatos()
    ui.setupUi(verDatos)
    verDatos.show()
    sys.exit(app.exec_())

