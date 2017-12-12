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
        MainWindow.resize(464, 243)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 164, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCursos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCursos.setObjectName("btnCursos")
        self.verticalLayout.addWidget(self.btnCursos)
        self.btnAlunos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAlunos.setObjectName("btnAlunos")
        self.verticalLayout.addWidget(self.btnAlunos)
        self.btnProfessores = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnProfessores.setObjectName("btnProfessores")
        self.verticalLayout.addWidget(self.btnProfessores)
        self.btnTurmas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnTurmas.setObjectName("btnTurmas")
        self.verticalLayout.addWidget(self.btnTurmas)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 49, 164, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnDisciplinas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnDisciplinas.setObjectName("btnDisciplinas")
        self.verticalLayout_2.addWidget(self.btnDisciplinas)
        self.btnCurso_has_Disciplinas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnCurso_has_Disciplinas.setObjectName("btnCurso_has_Disciplinas")
        self.verticalLayout_2.addWidget(self.btnCurso_has_Disciplinas)
        self.btnTurma_has_Aluno = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnTurma_has_Aluno.setObjectName("btnTurma_has_Aluno")
        self.verticalLayout_2.addWidget(self.btnTurma_has_Aluno)
        self.btnFrequencia = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnFrequencia.setObjectName("btnFrequencia")
        self.verticalLayout_2.addWidget(self.btnFrequencia)
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
        self.btnAlunos.setText(_translate("MainWindow", "Alunos"))
        self.btnProfessores.setText(_translate("MainWindow", "Professores"))
        self.btnTurmas.setText(_translate("MainWindow", "Turmas"))
        self.btnDisciplinas.setText(_translate("MainWindow", "Disciplinas"))
        self.btnCurso_has_Disciplinas.setText(_translate("MainWindow", "Disciplinas em Cursos"))
        self.btnTurma_has_Aluno.setText(_translate("MainWindow", "Alunos em Turmas"))
        self.btnFrequencia.setText(_translate("MainWindow", "Frequências"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

