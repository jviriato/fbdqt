from PyQt5.QtWidgets import *
from view.presenca import Ui_Frequencia

from main import *
db = Database("localhost", "viriato", "dinossauro", "mydb")

class Frequencia(QMainWindow, Ui_Frequencia):
    def __init__(self):
        super(Frequencia, self).__init__()
        self.setupUi(self)
        header = self.tablePresenca.setColumnWidth(1, 80)
        header = self.tablePresenca.setColumnWidth(2, 80)
        header = self.tablePresenca.setColumnWidth(3, 80)
        header = self.tablePresenca.setColumnWidth(4, 200)
        header = self.tablePresenca.setColumnWidth(5, 90)
        header = self.tablePresenca.setColumnWidth(6, 60)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Presenca(db, "Frequencia"));
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Presenca(db, "Frequencia"));
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Presenca(db, "Frequencia"));
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Presenca(db, "Frequencia"))


    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tablePresenca.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name + " ORDER BY Turma_idTurma"
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idFrequencia = row["idFrequencia"]
            idTurma = row["Turma_idTurma"]
            nomeTurma = row["nomeTurma"]
            idAluno = row["Aluno_idAluno"]
            nomeAluno = row["nomeAluno"]
            data = row["Data"]
            presenca = row["Presenca"]
            self.tablePresenca.setItem(i, 0, QTableWidgetItem(str(idFrequencia)))
            self.tablePresenca.setItem(i, 1, QTableWidgetItem(str(idTurma)))
            self.tablePresenca.setItem(i, 2, QTableWidgetItem(str(nomeTurma)))
            self.tablePresenca.setItem(i, 3, QTableWidgetItem(str(idAluno)))
            self.tablePresenca.setItem(i, 4, QTableWidgetItem(str(nomeAluno)))
            self.tablePresenca.setItem(i, 5, QTableWidgetItem(str(data)))
            self.tablePresenca.setItem(i, 6, QTableWidgetItem(str(presenca)))

        return 0

    def adicionar_item_Tabela_Presenca(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeTurma  = self.linenomeTurma.text()
        nomeAluno = self.linenomeAluno.text()
        Data = int(self.lineData.text())
        presenca = self.linePresenca.text()

        if(nomeTurma != '' and nomeAluno != '' and Data != '' and presenca != ''):
            num_rows = db.returnNumRows(table_name)

            query = "SELECT idAluno FROM Aluno WHERE nomeAluno = '{0}'".format(nomeAluno)
            db.cur.execute(query)
            result = db.cur.fetchall()
            for i, data in enumerate(result):
                idAluno = data["idAluno"]

            query = "SELECT idTurma FROM Turma WHERE nomeTurma = '{0}'".format(nomeTurma)
            db.cur.execute(query)
            result = db.cur.fetchall()
            for i, data in enumerate(result):
                idTurma = data["idTurma"]

            query = "INSERT INTO %s VALUES (NULL, '%s', '%s', '%s', '%s')" % ("Frequencia", idTurma, idAluno, Data, presenca)
            print(query)
            db.cur.execute(query)
            db.db.commit()
            self.popularTabela(db, "vw_frequencia")


    def editar_item_Tabela_Presenca(self, db, table_name):
        index = self.tablePresenca.currentIndex()
        row = index.row()
        column = index.column()

        idPresenca = int(self.tablePresenca.item(row,0).text())
        nomePresenca = str(self.tablePresenca.item(row,1).text())
        turno = str(self.tablePresenca.item(row,2).text())
        idProfessor = int(self.tablePresenca.item(row,3).text())
        idDisciplina = int(self.tablePresenca.item(row,4).text())
        Data = str(self.tablePresenca.item(row,5).text())

        query = "UPDATE %s SET nomePresenca = '%s', turno = '%s ' WHERE idPresenca = %d" % (table_name, nomePresenca, turno, idPresenca)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "vw_frequencia")

    def buscar_item_Tabela_Presenca(self, db, table_name):
        text = self.lineBusca.text()

        query = "SELECT * FROM {0} WHERE {1} LIKE '{2}%' OR {3} LIKE '{2}%' OR {4} LIKE '{2}%' OR {5} LIKE '{2}%' OR {6} LIKE '{2}%' OR {7} LIKE '{2}%'".format("vw_frequencia", "idFrequencia", text, "nomeTurma", "Turma_idTurma", "nomeAluno", "Aluno_idAluno", "Presenca")
        num_rows = db.cur.execute(query)
        result = db.cur.fetchall()

        self.tablePresenca.setRowCount(num_rows)
        for i, row in enumerate(result):
            idFrequencia = row["idFrequencia"]
            idTurma = row["Turma_idTurma"]
            nomeTurma = row["nomeTurma"]
            idAluno = row["Aluno_idAluno"]
            nomeAluno = row["nomeAluno"]
            data = row["Data"]
            presenca = row["Presenca"]
            self.tablePresenca.setItem(i, 0, QTableWidgetItem(str(idFrequencia)))
            self.tablePresenca.setItem(i, 1, QTableWidgetItem(str(idTurma)))
            self.tablePresenca.setItem(i, 2, QTableWidgetItem(str(nomeTurma)))
            self.tablePresenca.setItem(i, 3, QTableWidgetItem(str(idAluno)))
            self.tablePresenca.setItem(i, 4, QTableWidgetItem(str(nomeAluno)))
            self.tablePresenca.setItem(i, 5, QTableWidgetItem(str(data)))
            self.tablePresenca.setItem(i, 6, QTableWidgetItem(str(presenca)))

    def remover_item_Tabela_Presenca(self,db, tableName):
        index = self.tablePresenca.currentIndex()
        row = index.row()
        column = index.column()

        item = self.tablePresenca.item(row, 0)
        idFrequencia = int(item.text())
        #       remover aluno do Turma
        query = "DELETE FROM Frequencia WHERE idFrequencia = {0}".format(idFrequencia)
        print(query)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "vw_frequencia")
