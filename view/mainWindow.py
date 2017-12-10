# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelDiariodeClasse = QtWidgets.QLabel(self.centralwidget)
        self.labelDiariodeClasse.setObjectName("labelDiariodeClasse")
        self.gridLayout.addWidget(self.labelDiariodeClasse, 0, 0, 1, 1)
        self.tableCurso = QtWidgets.QTableWidget(self.centralwidget)
        self.tableCurso.setRowCount(3)
        self.tableCurso.setObjectName("tableCurso")
        self.tableCurso.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableCurso, 1, 0, 1, 2)
        self.nomeCurso = QtWidgets.QVBoxLayout()
        self.nomeCurso.setObjectName("nomeCurso")
        self.labelNomeCurso = QtWidgets.QLabel(self.centralwidget)
        self.labelNomeCurso.setObjectName("labelNomeCurso")
        self.nomeCurso.addWidget(self.labelNomeCurso)
        self.linenomeCurso = QtWidgets.QLineEdit(self.centralwidget)
        self.linenomeCurso.setObjectName("linenomeCurso")
        self.nomeCurso.addWidget(self.linenomeCurso)
        self.gridLayout.addLayout(self.nomeCurso, 2, 0, 1, 1)
        self.btnInserir = QtWidgets.QPushButton(self.centralwidget)
        self.btnInserir.setObjectName("btnInserir")
        self.gridLayout.addWidget(self.btnInserir, 2, 1, 1, 1)
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setObjectName("btnExcluir")
        self.gridLayout.addWidget(self.btnExcluir, 3, 1, 1, 1)
        self.siglaCurso = QtWidgets.QVBoxLayout()
        self.siglaCurso.setObjectName("siglaCurso")
        self.labelsiglaCurso = QtWidgets.QLabel(self.centralwidget)
        self.labelsiglaCurso.setObjectName("labelsiglaCurso")
        self.siglaCurso.addWidget(self.labelsiglaCurso)
        self.lineSiglaCurso = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSiglaCurso.setObjectName("lineSiglaCurso")
        self.siglaCurso.addWidget(self.lineSiglaCurso)
        self.gridLayout.addLayout(self.siglaCurso, 4, 0, 1, 1)
        self.tableCurso.raise_()
        self.labelDiariodeClasse.raise_()
        self.btnInserir.raise_()
        self.btnExcluir.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelDiariodeClasse.setText(_translate("MainWindow", "Diário de Classe"))
        item = self.tableCurso.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "idCurso"))
        item = self.tableCurso.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nomeCurso"))
        item = self.tableCurso.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "siglaCurso"))
        self.labelNomeCurso.setText(_translate("MainWindow", "Nome do Curso"))
        self.btnInserir.setText(_translate("MainWindow", "Inserir"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))
        self.labelsiglaCurso.setText(_translate("MainWindow", "Sigla do Curso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

