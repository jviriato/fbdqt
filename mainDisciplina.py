from PyQt5.QtWidgets import *
from view.disciplina import Ui_disciplina

from main import *
class Disciplina(QMainWindow, Ui_disciplina):
    def __init__(self):
        super(Disciplina, self).__init__()
        self.setupUi(self)
        header = self.tableDisciplina.setColumnWidth(1, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Disciplinas(db, "Disciplina"))
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Disciplinas(db, "Disciplina"))
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Disciplinas(db, "Disciplina"))
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Disciplinas(db, "Disciplina"))
    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableDisciplina.setRowCount(num_rows)
        query = "SELECT idDisciplina, nomeDisciplina FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idDisciplina = row["idDisciplina"]
            nomeDisciplina = row["nomeDisciplina"]
            self.tableDisciplina.setItem(i, 0, QTableWidgetItem(str(idDisciplina)))
            self.tableDisciplina.setItem(i, 1, QTableWidgetItem(str(nomeDisciplina)))

    def check_if_exists_in_db(self, result, siglaDisciplina, nomeDisciplina):
        for i, entry in enumerate(result):
            if nomeDisciplina == entry['nomeDisciplina']:
                erro = QMessageBox()
                erro.setText("Essa Disciplina já existe!")
                erro.exec()
                return 1
        return 0

    def adicionar_item_Tabela_Disciplinas(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeDisciplina  = self.linenomeDisciplina.text()

        if(nomeDisciplina != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, nomeDisciplina) == 0:
                query = "INSERT INTO %s VALUES (NULL, '%s')" % (
                table_name, nomeDisciplina)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                self.popularTabela(db, "Disciplina")

    def remover_item_Tabela_Disciplinas(self, db, table_name):
        index = self.tableDisciplina.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableDisciplina.item(row,0)

        id = int(item.text())

        query = "DELETE FROM %s WHERE idDisciplina = %d" % (table_name, id)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Disciplina")

    def editar_item_Tabela_Disciplinas(self, db, table_name):
        index = self.tableDisciplina.currentIndex()
        row = index.row()
        column = index.column()

        idDisciplina = int(self.tableDisciplina.item(row,0).text())
        nomeDisciplina = str(self.tableDisciplina.item(row,1).text())

        query = "UPDATE %s SET nomeDisciplina = '%s' WHERE idDisciplina = %d" % (table_name, nomeDisciplina, idDisciplina)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Disciplina")

    def buscar_item_Tabela_Disciplinas(self, db, table_name):
        text = self.lineBusca.text()
        query = "SELECT * FROM {0} WHERE {1} LIKE '{2}%' OR {3} LIKE '{2}%' OR {4} LIKE '{2}%'".format(table_name, "idDisciplina", text, "nomeDisciplina")
        num_rows = db.cur.execute(query)
        result = db.cur.fetchall()

        self.tableDisciplina.setRowCount(num_rows)
        for i, row in enumerate(result):
            idDisciplina = row["idDisciplina"]
            nomeDisciplina = row["nomeDisciplina"]
            self.tableDisciplina.setItem(i, 0, QTableWidgetItem(str(idDisciplina)))
            self.tableDisciplina.setItem(i, 1, QTableWidgetItem(str(nomeDisciplina)))
