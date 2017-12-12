from PyQt5.QtWidgets import *
from view.turma import Ui_Turma

from main import *
db = Database("localhost", "root", "30101998", "mydb")

class Turma(QMainWindow, Ui_Turma):
    def __init__(self):
        super(Turma, self).__init__()
        self.setupUi(self)
        header = self.tableTurma.setColumnWidth(1, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Turma(db, "Turma"));
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Turmar(db, "Turma"));
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Turma(db, "Turma"));
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Turma(db, "Turma"))


    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableTurma.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idTurma = row["idTurma"]
            nomeTurma = row["nomeTurma"]
            turno = row["turno"]
            idProfessor = row["Professor_idProfessor"]
            idDisciplina = row["Disciplina_idDisciplina"]
            Data = row["Data"]
            self.tableTurma.setItem(i, 0, QTableWidgetItem(str(idTurma)))
            self.tableTurma.setItem(i, 1, QTableWidgetItem(str(nomeTurma)))
            self.tableTurma.setItem(i, 2, QTableWidgetItem(str(turno)))
            self.tableTurma.setItem(i, 3, QTableWidgetItem(str(idProfessor)))
            self.tableTurma.setItem(i, 4, QTableWidgetItem(str(idDisciplina)))
            self.tableTurma.setItem(i, 5, QTableWidgetItem(str(Data)))


    def check_if_exists_in_db(self, result, nomeTurma, turno):
        for i, entry in enumerate(result):
            if nomeTurma == entry['nomeTurma']:
                if turno == entru['turno']:
                    erro = QMessageBox()
                    erro.setText("Essa Turma já existe!")
                    erro.exec()
                    return 1

        return 0

    def adicionar_item_Tabela_Turma(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeTurma  = self.linenomeTurma.text()
        turno = self.lineTurno.text()
        idProfessor = int(self.lineProfessor.text())
        idDisciplina = int(self.lineDisciplina.text())
        Data = (self.lineData.text())

        if(nomeTurma != '' and turno != '' and idProfessor != '' and idDisciplina != '' and Data != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, nomeTurma, turno) == 0:
                query = "INSERT INTO %s VALUES (NULL, '%s', '%s', '%s', '%s', '%s')" % (
                table_name, nomeTurma, turno, idProfessor, idDisciplina, Data)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                self.popularTabela(db, "Turma")


    def editar_item_Tabela_Turma(self, db, table_name):
        index = self.tableTurma.currentIndex()
        row = index.row()
        column = index.column()

        idTurma = int(self.tableTurma.item(row,0).text())
        nomeTurma = str(self.tableTurma.item(row,1).text())
        turno = str(self.tableTurma.item(row,2).text())
        idProfessor = int(self.tableTurma.item(row,3).text())
        idDisciplina = int(self.tableTurma.item(row,4).text())
        Data = str(self.tableTurma.item(row,5).text())

        query = "UPDATE %s SET nomeTurma = '%s', turno = '%s ' WHERE idTurma = %d" % (table_name, nomeTurma, turno, idTurma)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Turma")
