# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curso.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_curso(object):
    def setupUi(self, curso):
        curso.setObjectName("curso")
        curso.resize(690, 491)
        self.tableCurso = QtWidgets.QTableWidget(curso)
        self.tableCurso.setGeometry(QtCore.QRect(40, 40, 601, 331))
        self.tableCurso.setRowCount(3)
        self.tableCurso.setObjectName("tableCurso")
        self.tableCurso.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCurso.setHorizontalHeaderItem(2, item)
        self.tableCurso.horizontalHeader().setStretchLastSection(True)
        self.widget = QtWidgets.QWidget(curso)
        self.widget.setGeometry(QtCore.QRect(390, 380, 151, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnInserir = QtWidgets.QPushButton(self.widget)
        self.btnInserir.setObjectName("btnInserir")
        self.verticalLayout_4.addWidget(self.btnInserir)
        self.btnExcluir = QtWidgets.QPushButton(self.widget)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout_4.addWidget(self.btnExcluir)
        self.widget1 = QtWidgets.QWidget(curso)
        self.widget1.setGeometry(QtCore.QRect(40, 380, 151, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNomeCurso = QtWidgets.QLabel(self.widget1)
        self.labelNomeCurso.setObjectName("labelNomeCurso")
        self.verticalLayout.addWidget(self.labelNomeCurso)
        self.linenomeCurso = QtWidgets.QLineEdit(self.widget1)
        self.linenomeCurso.setObjectName("linenomeCurso")
        self.verticalLayout.addWidget(self.linenomeCurso)
        self.widget2 = QtWidgets.QWidget(curso)
        self.widget2.setGeometry(QtCore.QRect(210, 380, 151, 81))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelsiglaCurso = QtWidgets.QLabel(self.widget2)
        self.labelsiglaCurso.setObjectName("labelsiglaCurso")
        self.verticalLayout_2.addWidget(self.labelsiglaCurso)
        self.lineSiglaCurso = QtWidgets.QLineEdit(self.widget2)
        self.lineSiglaCurso.setObjectName("lineSiglaCurso")
        self.verticalLayout_2.addWidget(self.lineSiglaCurso)
        self.tableCurso.raise_()
        self.lineSiglaCurso.raise_()
        self.labelNomeCurso.raise_()

        self.retranslateUi(curso)
        QtCore.QMetaObject.connectSlotsByName(curso)

    def retranslateUi(self, curso):
        _translate = QtCore.QCoreApplication.translate
        curso.setWindowTitle(_translate("curso", "Form"))
        item = self.tableCurso.horizontalHeaderItem(0)
        item.setText(_translate("curso", "idCurso"))
        item = self.tableCurso.horizontalHeaderItem(1)
        item.setText(_translate("curso", "nomeCurso"))
        item = self.tableCurso.horizontalHeaderItem(2)
        item.setText(_translate("curso", "siglaCurso"))
        self.btnInserir.setText(_translate("curso", "Inserir"))
        self.btnExcluir.setText(_translate("curso", "Excluir"))
        self.labelNomeCurso.setText(_translate("curso", "Nome do Curso"))
        self.labelsiglaCurso.setText(_translate("curso", "Sigla do Curso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    curso = QtWidgets.QWidget()
    ui = Ui_curso()
    ui.setupUi(curso)
    curso.show()
    sys.exit(app.exec_())

