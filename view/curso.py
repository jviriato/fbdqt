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
        curso.resize(690, 598)
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
        self.frame = QtWidgets.QFrame(curso)
        self.frame.setGeometry(QtCore.QRect(100, 470, 491, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 17))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 304, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNomeCurso = QtWidgets.QLabel(self.layoutWidget)
        self.labelNomeCurso.setObjectName("labelNomeCurso")
        self.verticalLayout.addWidget(self.labelNomeCurso)
        self.linenomeCurso = QtWidgets.QLineEdit(self.layoutWidget)
        self.linenomeCurso.setObjectName("linenomeCurso")
        self.verticalLayout.addWidget(self.linenomeCurso)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelsiglaCurso = QtWidgets.QLabel(self.layoutWidget)
        self.labelsiglaCurso.setObjectName("labelsiglaCurso")
        self.verticalLayout_2.addWidget(self.labelsiglaCurso)
        self.lineSiglaCurso = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineSiglaCurso.setObjectName("lineSiglaCurso")
        self.verticalLayout_2.addWidget(self.lineSiglaCurso)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(330, 10, 151, 92))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnInserir = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnInserir.setObjectName("btnInserir")
        self.verticalLayout_4.addWidget(self.btnInserir)
        self.btnEditar = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnEditar.setObjectName("btnEditar")
        self.verticalLayout_4.addWidget(self.btnEditar)
        self.btnExcluir = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout_4.addWidget(self.btnExcluir)
        self.layoutWidget2 = QtWidgets.QWidget(curso)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 400, 481, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineBusca = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineBusca.setObjectName("lineBusca")
        self.horizontalLayout_2.addWidget(self.lineBusca)

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
        self.label.setText(_translate("curso", "Manipulação"))
        self.labelNomeCurso.setText(_translate("curso", "Nome do Curso"))
        self.labelsiglaCurso.setText(_translate("curso", "Sigla do Curso"))
        self.btnInserir.setText(_translate("curso", "Inserir"))
        self.btnEditar.setText(_translate("curso", "Editar"))
        self.btnExcluir.setText(_translate("curso", "Excluir"))
        self.label_2.setText(_translate("curso", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    curso = QtWidgets.QWidget()
    ui = Ui_curso()
    ui.setupUi(curso)
    curso.show()
    sys.exit(app.exec_())

