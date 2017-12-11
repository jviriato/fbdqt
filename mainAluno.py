from PyQt5.QtWidgets import *
from view.Aluno import Ui_Form

from main import *
db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")

class Aluno(QMainWindow, Ui_Form):
    def __init__(self):
        super(Aluno, self).__init__()
        self.setupUi(self)
        header = self.tableAluno.setColumnWidth(1, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Aluno(db, "Aluno"));
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Aluno(db, "Aluno"));
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Aluno(db, "Aluno"));

        # self.tableAluno.cellClicked.connect(self.cell_was_clicked)
    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableAluno.setRowCount(num_rows)
        query = "SELECT idAluno, nomeAluno, matricula FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idAluno = row["idAluno"]
            nomeAluno = row["nomeAluno"]
            matricula = row["matricula"]
            self.tableAluno.setItem(i, 0, QTableWidgetItem(str(idAluno)))
            self.tableAluno.setItem(i, 1, QTableWidgetItem(str(nomeAluno)))
            self.tableAluno.setItem(i, 2, QTableWidgetItem(str(matricula)))

    def check_if_exists_in_db(self, result, matricula, nomeAluno):
        for i, entry in enumerate(result):
            if matricula == entry['matricula']:
                print("Essa matrícula já existe!")
                return 1
            elif nomeAluno == entry['nomeAluno']:
                print("Esse Aluno já existe!")
                return 1
        return 0

    def adicionar_item_Tabela_Aluno(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeAluno  = self.linenomeAluno.text()
        matricula = self.lineMatricula.text()

        if(nomeAluno != '' and matricula != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, matricula, nomeAluno) == 0:
                query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (
                table_name, nomeAluno, matricula)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                self.popularTabela(db, "Aluno")

    def remover_item_Tabela_Aluno(self, db, table_name):
        index = self.tableAluno.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableAluno.item(row,0)

        id = int(item.text())

        query = "DELETE FROM %s WHERE idAluno = %d" % (table_name, id)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Aluno")


    def editar_item_Tabela_Aluno(self, db, table_name):
        index = self.tableAluno.currentIndex()
        row = index.row()
        column = index.column()

        idAluno = int(self.tableAluno.item(row,0).text())
        nomeAluno = str(self.tableAluno.item(row,1).text())
        matricula = str(self.tableAluno.item(row,2).text())

        query = "UPDATE %s SET nomeAluno = '%s', matricula = '%s ' WHERE idAluno = %d" % (table_name, nomeAluno, matricula, idAluno)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Aluno")
