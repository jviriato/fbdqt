# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disciplina.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_disciplina(object):
    def setupUi(self, disciplina):
        disciplina.setObjectName("disciplina")
        disciplina.resize(690, 598)
        self.tableDisciplina = QtWidgets.QTableWidget(disciplina)
        self.tableDisciplina.setGeometry(QtCore.QRect(40, 40, 601, 331))
        self.tableDisciplina.setRowCount(3)
        self.tableDisciplina.setObjectName("tableDisciplina")
        self.tableDisciplina.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisciplina.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDisciplina.setHorizontalHeaderItem(1, item)
        self.tableDisciplina.horizontalHeader().setStretchLastSection(True)
        self.frame = QtWidgets.QFrame(disciplina)
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
        self.labelNomeDisciplina = QtWidgets.QLabel(self.layoutWidget)
        self.labelNomeDisciplina.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelNomeDisciplina.setObjectName("labelNomeDisciplina")
        self.verticalLayout.addWidget(self.labelNomeDisciplina)
        self.linenomeDisciplina = QtWidgets.QLineEdit(self.layoutWidget)
        self.linenomeDisciplina.setObjectName("linenomeDisciplina")
        self.verticalLayout.addWidget(self.linenomeDisciplina)
        self.horizontalLayout.addLayout(self.verticalLayout)
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
        self.layoutWidget2 = QtWidgets.QWidget(disciplina)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 400, 481, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBusca = QtWidgets.QLabel(self.layoutWidget2)
        self.labelBusca.setObjectName("labelBusca")
        self.horizontalLayout_2.addWidget(self.labelBusca)
        self.lineBusca = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineBusca.setObjectName("lineBusca")
        self.horizontalLayout_2.addWidget(self.lineBusca)

        self.retranslateUi(disciplina)
        QtCore.QMetaObject.connectSlotsByName(disciplina)

    def retranslateUi(self, disciplina):
        _translate = QtCore.QCoreApplication.translate
        disciplina.setWindowTitle(_translate("disciplina", "Form"))
        item = self.tableDisciplina.horizontalHeaderItem(0)
        item.setText(_translate("disciplina", "idDisciplina"))
        item = self.tableDisciplina.horizontalHeaderItem(1)
        item.setText(_translate("disciplina", "nomeDisciplina"))
        self.label.setText(_translate("disciplina", "Manipulação"))
        self.labelNomeDisciplina.setText(_translate("disciplina", "                                   Nome da Disciplina"))
        self.btnInserir.setText(_translate("disciplina", "Inserir"))
        self.btnEditar.setText(_translate("disciplina", "Editar"))
        self.btnExcluir.setText(_translate("disciplina", "Excluir"))
        self.labelBusca.setText(_translate("disciplina", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    disciplina = QtWidgets.QWidget()
    ui = Ui_disciplina()
    ui.setupUi(disciplina)
    disciplina.show()
    sys.exit(app.exec_())

