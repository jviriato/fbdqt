# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 160, 156))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCursos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCursos.setObjectName("btnCursos")
        self.verticalLayout.addWidget(self.btnCursos)
        self.btnTurmas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnTurmas.setObjectName("btnTurmas")
        self.verticalLayout.addWidget(self.btnTurmas)
        self.btnAlunos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAlunos.setObjectName("btnAlunos")
        self.verticalLayout.addWidget(self.btnAlunos)
        self.btnProfessores = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnProfessores.setObjectName("btnProfessores")
        self.verticalLayout.addWidget(self.btnProfessores)
        self.btnDisciplinas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDisciplinas.setObjectName("btnDisciplinas")
        self.verticalLayout.addWidget(self.btnDisciplinas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCursos.setText(_translate("MainWindow", "Cursos"))
        self.btnTurmas.setText(_translate("MainWindow", "Turmas"))
        self.btnAlunos.setText(_translate("MainWindow", "Alunos"))
        self.btnProfessores.setText(_translate("MainWindow", "Professores"))
        self.btnDisciplinas.setText(_translate("MainWindow", "Disciplinas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

