from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox
from CRUD.crudEstudiantes import *
from CRUD.crudProfesores import *
from CRUD.crudEvaluacion import *
from CRUD.crudTemas import *
from CRUD.crudPublicaciones import *
from CRUD.crudResultadoEvaluaciones import *
from CRUD.crudInvestigacion import *


class Ui_ingresarDatos(object):


    def openMenu(self, main_w, ingresarDatos):
        ingresarDatos.close()
        main_w.show()

    def setupUi(self, ingresarDatos, MainWindow):
        self.opti = 0
        ingresarDatos.setObjectName("ingresarDatos")
        ingresarDatos.resize(439, 466)
        self.centralwidget = QtWidgets.QWidget(ingresarDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.nMatriculaT = QtWidgets.QLineEdit(self.centralwidget)
        self.nMatriculaT.setGeometry(QtCore.QRect(140, 30, 211, 31))
        self.nMatriculaT.setObjectName("nMatriculaT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label.setObjectName("label")
        self.nombreT = QtWidgets.QLineEdit(self.centralwidget)
        self.nombreT.setGeometry(QtCore.QRect(140, 80, 211, 31))
        self.nombreT.setObjectName("nombreT")
        self.apellidoT = QtWidgets.QLineEdit(self.centralwidget)
        self.apellidoT.setGeometry(QtCore.QRect(140, 130, 211, 31))
        self.apellidoT.setObjectName("apellidoT")
        self.idIT = QtWidgets.QLineEdit(self.centralwidget)
        self.idIT.setGeometry(QtCore.QRect(140, 180, 211, 31))
        self.idIT.setObjectName("idIT")
        self.extraText = QtWidgets.QLineEdit(self.centralwidget)
        self.extraText.setGeometry(QtCore.QRect(140, 230, 211, 31))
        self.extraText.setObjectName("extraText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.insertar())
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 141, 31))
        self.pushButton.setObjectName("pushButton")

        self.buttonInicio = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openMenu(MainWindow, ingresarDatos))
        self.buttonInicio.setGeometry(QtCore.QRect(240, 360, 141, 31))
        self.buttonInicio.setObjectName("pushButton_2")

        self.buttonEstudiante = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeEst())
        self.buttonEstudiante.setGeometry(QtCore.QRect(40, 280, 90, 31))
        self.buttonEstudiante.setObjectName("buttonEstudiante")

        self.buttonProfesor = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changePro())
        self.buttonProfesor.setGeometry(QtCore.QRect(130, 280, 90, 31))
        self.buttonProfesor.setObjectName("buttonProfesor")

        self.buttonEvaluacion = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeEva())
        self.buttonEvaluacion .setGeometry(QtCore.QRect(220, 280, 90, 31))
        self.buttonEvaluacion .setObjectName("buttonEvaluacion")

        self.buttonInvestigacion = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeInve())
        self.buttonInvestigacion.setGeometry(QtCore.QRect(310, 280, 90, 31))
        self.buttonInvestigacion.setObjectName("buttonInvestigacion")

        self.buttonPublicacion = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changePubl())
        self.buttonPublicacion.setGeometry(QtCore.QRect(80, 320, 90, 31))
        self.buttonPublicacion.setObjectName("buttonPublicacion")

        self.buttonResultados = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeRe())
        self.buttonResultados.setGeometry(QtCore.QRect(170, 320, 90, 31))
        self.buttonResultados.setObjectName("buttonResultados")

        self.buttonTema = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeTema())
        self.buttonTema.setGeometry(QtCore.QRect(260, 320, 90, 31))
        self.buttonTema.setObjectName("buttonTema")

        self.mensajeNM = QtWidgets.QLabel(self.centralwidget)
        self.mensajeNM.setGeometry(QtCore.QRect(360, 40, 47, 14))
        self.mensajeNM.setText("")
        self.mensajeNM.setObjectName("mensajeNM")
        self.mensajeN = QtWidgets.QLabel(self.centralwidget)
        self.mensajeN.setGeometry(QtCore.QRect(360, 90, 47, 14))
        self.mensajeN.setText("")
        self.mensajeN.setObjectName("mensajeN")
        self.mensajeA = QtWidgets.QLabel(self.centralwidget)
        self.mensajeA.setGeometry(QtCore.QRect(360, 140, 47, 14))
        self.mensajeA.setText("")
        self.mensajeA.setObjectName("mensajeA")
        self.mensajeIDIT = QtWidgets.QLabel(self.centralwidget)
        self.mensajeIDIT.setGeometry(QtCore.QRect(360, 190, 47, 14))
        self.mensajeIDIT.setText("")
        self.mensajeIDIT.setObjectName("mensajeIDIT")
        self.mensajeExtra = QtWidgets.QLabel(self.centralwidget)
        self.mensajeExtra.setGeometry(QtCore.QRect(360, 240, 47, 14))
        self.mensajeExtra.setText("")
        self.mensajeExtra.setObjectName("mensajeExtra")
        self.mensajeGeneral = QtWidgets.QLabel(self.centralwidget)
        self.mensajeGeneral.setGeometry(QtCore.QRect(20, 230, 251, 16))
        self.mensajeGeneral.setText("")
        self.mensajeGeneral.setObjectName("mensajeGeneral")
        ingresarDatos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ingresarDatos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        ingresarDatos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ingresarDatos)
        self.statusbar.setObjectName("statusbar")
        ingresarDatos.setStatusBar(self.statusbar)
        self.actionInicio = QtWidgets.QAction(ingresarDatos)
        self.actionInicio.setObjectName("actionInicio")
        self.actionVer_Datos = QtWidgets.QAction(ingresarDatos)
        self.actionVer_Datos.setObjectName("actionVer_Datos")
        self.menuMenu.addAction(self.actionInicio)
        self.menuMenu.addAction(self.actionVer_Datos)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.nMatriculaT.setValidator(QIntValidator())
        self.idIT.setValidator(QIntValidator())

        self.extraText.hide()

        self.retranslateUi(ingresarDatos)
        QtCore.QMetaObject.connectSlotsByName(ingresarDatos)

    def retranslateUi(self, ingresarDatos):
        _translate = QtCore.QCoreApplication.translate
        ingresarDatos.setWindowTitle(_translate("ingresarDatos", "MainWindow"))
        self.label.setText(_translate("ingresarDatos", "Numero de Matricula"))
        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.label_3.setText(_translate("ingresarDatos", "Apellido"))
        self.label_4.setText(_translate("ingresarDatos", "ID Investigacion"))
        self.label_5.setText(_translate("ingresarDatos", ""))
        self.pushButton.setText(_translate("ingresarDatos", "Registrar"))
        self.buttonInicio.setText(_translate("ingresarDatos", "Inicio"))
        self.menuMenu.setTitle(_translate("ingresarDatos", "Menu"))
        self.actionInicio.setText(_translate("ingresarDatos", "Inicio"))
        self.actionVer_Datos.setText(_translate("ingresarDatos", "Ver Datos"))
        self.buttonEstudiante.setText(_translate("ingresarDatos", "Estudiante"))
        self.buttonProfesor.setText(_translate("ingresarDatos", "Profesor"))
        self.buttonEvaluacion.setText(_translate("ingresarDatos", "Evaluacion"))
        self.buttonInvestigacion.setText(_translate("ingresarDatos", "Investigacion"))
        self.buttonPublicacion.setText(_translate("ingresarDatos", "Publicacion"))
        self.buttonResultados.setText(_translate("ingresarDatos", "Resultado"))
        self.buttonTema.setText(_translate("ingresarDatos", "Tema"))

    def clearT(self):
        self.nMatriculaT.setText("")
        self.nombreT.setText("")
        self.apellidoT.setText("")
        self.idIT.setText("")
        self.extraText.setText("")
        self.mensajeExtra.setText("")
        self.mensajeIDIT.setText("")
        self.mensajeA.setText("")
        self.mensajeN.setText("")
        self.mensajeNM.setText("")

    def insertar(self):
        check = True
        num = True

        if self.nMatriculaT.text() == "" and self.nMatriculaT.isVisible():
            self.mensajeNM.setText("*")
            check = False
        else:
            self.mensajeNM.setText("")


        if self.nombreT.text() == "" and self.nombreT.isVisible():
            self.mensajeN.setText("*")
            check = False
        else:
            self.mensajeN.setText("")

        if self.apellidoT.text() == "" and self.apellidoT.isVisible():
            self.mensajeA.setText("*")
            check = False
        else:
            self.mensajeA.setText("")

        if self.idIT.text() == "" and self.idIT.isVisible():
            self.mensajeIDIT.setText("*")
            check = False
        else:
            self.mensajeIDIT.setText("")

        if self.extraText.text() == "" and self.extraText.isVisible():
            self.mensajeExtra.setText("*")
            check = False
        else:
            self.mensajeExtra.setText("")

        if check == False:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingresa datos en los campos marcados por *")
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
        if num == False:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Los datos marcados por # deben ser numericos")
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()

        response = -1

        if check and num and self.opti==0:
            response = crudEstudiantes("localhost", "root", "Odiolapapa11", "pabd").createEstudiante(self.nMatriculaT.text(),self.nombreT.text(),self.apellidoT.text(),self.idIT.text())

        if check and num and self.opti == 1:
            response = crudProfesores("localhost", "root", "Odiolapapa11", "pabd").createProfesor(self.nMatriculaT.text(), self.nombreT.text(), self.apellidoT.text(), self.idIT.text())

        if check and num and self.opti == 2:
            response = crudEvaluacion("localhost", "root", "Odiolapapa11", "pabd").createEvaluacion(self.nMatriculaT.text(), self.nombreT.text(), self.apellidoT.text(), self.idIT.text(), self.extraText.text())

        if check and num and self.opti == 3:
            response = crudInvestigacion("localhost", "root", "Odiolapapa11", "pabd").createInvestigacion(self.nMatriculaT.text(), self.nombreT.text(), self.apellidoT.text(), self.idIT.text())

        if check and num and self.opti == 4:
            response = crudPublicaciones("localhost", "root", "Odiolapapa11", "pabd").createPublicacion(self.nMatriculaT.text(), self.nombreT.text(), self.apellidoT.text(), self.idIT.text(), self.extraText.text())

        if check and num and self.opti == 5:
            response = crudResultadosEvaluacion("localhost", "root", "Odiolapapa11", "pabd").createResultado(self.nMatriculaT.text(), self.nombreT.text(), self.apellidoT.text())

        if check and num and self.opti == 6:
            response = crudTemas("localhost", "root", "Odiolapapa11", "pabd").createTema(self.nMatriculaT.text(), self.nombreT.text())

        print(response)

        if self.opti == 0:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El numero de matricula del estudiante ya existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La ID de investigacion no existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 1:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El numero de documento del profesor ya existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La extension ya esta en uso")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 2:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La ID ya esta en Uso")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El Profesor con ese Documento no Existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 3:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La ID ya esta en Uso")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El Tema con esa ID no Existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 4:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La ID ya esta en Uso")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La Investigacion con est ID no Existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 5:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El Numero de Matricula no Existe")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()
        elif self.opti == 6:
            if response == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La ID ya esta en Uso")
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            elif response == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Mensaje")
                msg.setText("Creacion correcta")

                x = msg.exec_()

    def changeEst(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.show()
        self.extraText.hide()

        _translate = QtCore.QCoreApplication.translate

        self.label.setText(_translate("ingresarDatos", "Numero de Matricula"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", "Apellido"))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", "ID Investigacion"))
        self.idIT.setValidator(QIntValidator())

        self.label_5.setText(_translate("ingresarDatos", ""))
        self.extraText.setValidator(None)

        self.opti = 0

    def changePro(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.show()
        self.extraText.hide()

        _translate = QtCore.QCoreApplication.translate

        self.label.setText(_translate("ingresarDatos", "Documento"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre Completo"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", "Modalidad"))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", "Extension"))
        self.idIT.setValidator(QIntValidator())

        self.label_5.setText(_translate("ingresarDatos", ""))
        self.extraText.setValidator(None)

        self.opti = 1

    def changeEva(self):
        self.clearT()

        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.show()
        self.extraText.show()

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ingresarDatos", "ID"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", "Fecha"))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", "Cant. Preguntas"))
        self.idIT.setValidator(QIntValidator())

        self.label_5.setText(_translate("ingresarDatos", "Doc. Profesor"))
        self.extraText.setValidator(QIntValidator())

        self.opti = 2

    def changeInve(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.show()
        self.extraText.hide()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ingresarDatos", "ID"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", "Enfoque"))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", "Tema ID"))
        self.idIT.setValidator(QIntValidator())

        self.label_5.setText(_translate("ingresarDatos", ""))
        self.extraText.setValidator(None)

        self.opti = 3

    def changePubl(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.show()
        self.extraText.show()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ingresarDatos", "ID"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", "Fecha"))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", "Cant. Palabras"))
        self.idIT.setValidator(None)

        self.label_5.setText(_translate("ingresarDatos", "ID Investigacion"))
        self.extraText.setValidator(QIntValidator())

        self.opti = 4

    def changeRe(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.show()
        self.idIT.hide()
        self.extraText.hide()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ingresarDatos", "# Matricual Estudiante"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "ID de Evaluacion"))
        self.nombreT.setValidator(QIntValidator())

        self.label_3.setText(_translate("ingresarDatos", "Resultado"))
        self.apellidoT.setValidator(QIntValidator())

        self.label_4.setText(_translate("ingresarDatos", ""))
        self.idIT.setValidator(None)

        self.label_5.setText(_translate("ingresarDatos", ""))
        self.extraText.setValidator(QIntValidator())

        self.opti = 5

    def changeTema(self):
        self.clearT()
        self.nMatriculaT.show()
        self.nombreT.show()
        self.apellidoT.hide()
        self.idIT.hide()
        self.extraText.hide()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ingresarDatos", "ID"))
        self.nMatriculaT.setValidator(QIntValidator())

        self.label_2.setText(_translate("ingresarDatos", "Nombre"))
        self.nombreT.setValidator(None)

        self.label_3.setText(_translate("ingresarDatos", ""))
        self.apellidoT.setValidator(None)

        self.label_4.setText(_translate("ingresarDatos", ""))
        self.idIT.setValidator(None)

        self.label_5.setText(_translate("ingresarDatos", ""))
        self.extraText.setValidator(QIntValidator())

        self.opti = 6


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ingresarDatos = QtWidgets.QMainWindow()
    ui = Ui_ingresarDatos()
    ui.setupUi(ingresarDatos)
    ingresarDatos.show()
    sys.exit(app.exec_())

