# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'turma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Turma(object):
    def setupUi(self, Turma):
        Turma.setObjectName("Turma")
        Turma.resize(679, 585)
        self.tableTurma = QtWidgets.QTableWidget(Turma)
        self.tableTurma.setEnabled(True)
        self.tableTurma.setGeometry(QtCore.QRect(30, 20, 601, 331))
        self.tableTurma.setRowCount(3)
        self.tableTurma.setObjectName("tableTurma")
        self.tableTurma.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTurma.setHorizontalHeaderItem(5, item)
        self.tableTurma.horizontalHeader().setDefaultSectionSize(100)
        self.tableTurma.horizontalHeader().setStretchLastSection(True)
        self.form = QtWidgets.QFrame(Turma)
        self.form.setGeometry(QtCore.QRect(10, 440, 651, 111))
        self.form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form.setObjectName("form")
        self.label = QtWidgets.QLabel(self.form)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 17))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 461, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelnomeTurma = QtWidgets.QLabel(self.layoutWidget)
        self.labelnomeTurma.setObjectName("labelnomeTurma")
        self.verticalLayout.addWidget(self.labelnomeTurma)
        self.linenomeTurma = QtWidgets.QLineEdit(self.layoutWidget)
        self.linenomeTurma.setObjectName("linenomeTurma")
        self.verticalLayout.addWidget(self.linenomeTurma)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTurno = QtWidgets.QLabel(self.layoutWidget)
        self.labelTurno.setObjectName("labelTurno")
        self.verticalLayout_2.addWidget(self.labelTurno)
        self.lineTurno = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineTurno.setDragEnabled(True)
        self.lineTurno.setObjectName("lineTurno")
        self.verticalLayout_2.addWidget(self.lineTurno)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelidProfessor = QtWidgets.QLabel(self.layoutWidget)
        self.labelidProfessor.setObjectName("labelidProfessor")
        self.verticalLayout_3.addWidget(self.labelidProfessor)
        self.lineProfessor = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineProfessor.setObjectName("lineProfessor")
        self.verticalLayout_3.addWidget(self.lineProfessor)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.labelidDisciplina = QtWidgets.QLabel(self.layoutWidget)
        self.labelidDisciplina.setObjectName("labelidDisciplina")
        self.verticalLayout_10.addWidget(self.labelidDisciplina)
        self.lineDisciplina = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineDisciplina.setText("")
        self.lineDisciplina.setObjectName("lineDisciplina")
        self.verticalLayout_10.addWidget(self.lineDisciplina)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelData = QtWidgets.QLabel(self.layoutWidget)
        self.labelData.setObjectName("labelData")
        self.verticalLayout_5.addWidget(self.labelData)
        self.lineData = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineData.setObjectName("lineData")
        self.verticalLayout_5.addWidget(self.lineData)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.layoutWidget_2 = QtWidgets.QWidget(self.form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 10, 151, 92))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnInserir = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnInserir.setObjectName("btnInserir")
        self.verticalLayout_4.addWidget(self.btnInserir)
        self.btnEditar = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnEditar.setObjectName("btnEditar")
        self.verticalLayout_4.addWidget(self.btnEditar)
        self.btnExcluir = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnExcluir.setObjectName("btnExcluir")
        self.verticalLayout_4.addWidget(self.btnExcluir)
        self.layoutWidget_3 = QtWidgets.QWidget(Turma)
        self.layoutWidget_3.setGeometry(QtCore.QRect(80, 370, 481, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBusca = QtWidgets.QLabel(self.layoutWidget_3)
        self.labelBusca.setObjectName("labelBusca")
        self.horizontalLayout_2.addWidget(self.labelBusca)
        self.lineBusca = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineBusca.setObjectName("lineBusca")
        self.horizontalLayout_2.addWidget(self.lineBusca)

        self.retranslateUi(Turma)
        QtCore.QMetaObject.connectSlotsByName(Turma)

    def retranslateUi(self, Turma):
        _translate = QtCore.QCoreApplication.translate
        Turma.setWindowTitle(_translate("Turma", "Form"))
        item = self.tableTurma.horizontalHeaderItem(0)
        item.setText(_translate("Turma", "idTurma"))
        item = self.tableTurma.horizontalHeaderItem(1)
        item.setText(_translate("Turma", "nomeTurma"))
        item = self.tableTurma.horizontalHeaderItem(2)
        item.setText(_translate("Turma", "turno"))
        item = self.tableTurma.horizontalHeaderItem(3)
        item.setText(_translate("Turma", "idProfessor"))
        item = self.tableTurma.horizontalHeaderItem(4)
        item.setText(_translate("Turma", "idDisciplina"))
        item = self.tableTurma.horizontalHeaderItem(5)
        item.setText(_translate("Turma", "Data"))
        self.label.setText(_translate("Turma", "Manipulação"))
        self.labelnomeTurma.setText(_translate("Turma", "Nome da Turma"))
        self.labelTurno.setText(_translate("Turma", "Turno"))
        self.labelidProfessor.setText(_translate("Turma", "Id do Professor"))
        self.labelidDisciplina.setText(_translate("Turma", "Id da Disciplina"))
        self.labelData.setText(_translate("Turma", "Data da Turma"))
        self.btnInserir.setText(_translate("Turma", "Inserir"))
        self.btnEditar.setText(_translate("Turma", "Editar"))
        self.btnExcluir.setText(_translate("Turma", "Excluir"))
        self.labelBusca.setText(_translate("Turma", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Turma = QtWidgets.QWidget()
    ui = Ui_Turma()
    ui.setupUi(Turma)
    Turma.show()
    sys.exit(app.exec_())

