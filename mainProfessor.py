from PyQt5.QtWidgets import *
from view.professor import Ui_Form

from main import *
db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")

class Professor(QMainWindow, Ui_Form):
    def __init__(self):
        super(Professor, self).__init__()
        self.setupUi(self)
        header = self.tableProfessor.setColumnWidth(1, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Professor(db, "Professor"));
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Professor(db, "Professor"));
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Professor(db, "Professor"));
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Professors(db, "Professor"))
    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableProfessor.setRowCount(num_rows)
        query = "SELECT idProfessor, nomeProfessor, matricula FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idProfessor = row["idProfessor"]
            nomeProfessor = row["nomeProfessor"]
            matricula = row["matricula"]
            self.tableProfessor.setItem(i, 0, QTableWidgetItem(str(idProfessor)))
            self.tableProfessor.setItem(i, 1, QTableWidgetItem(str(nomeProfessor)))
            self.tableProfessor.setItem(i, 2, QTableWidgetItem(str(matricula)))

    def check_if_exists_in_another_table(self, idProfessor):
        #tabelas que existe professor: Turma
        print("IdProfessor:",idProfessor)
        query = "SELECT Professor_idProfessor FROM Turma WHERE Professor_idProfessor = %s" % idProfessor
        return db.cur.execute(query)


    def check_if_exists_in_db(self, result, matricula, nomeProfessor):
        for i, entry in enumerate(result):
            if matricula == int(entry['matricula']):
                erro = QMessageBox()
                erro.setText("Essa matrícula já existe!")
                erro.exec()
                return 1
            elif nomeProfessor == entry['nomeProfessor']:
                erro = QMessageBox()
                erro.setText("Esse Professor já existe!")
                erro.exec()
                return 1
        return 0

    def adicionar_item_Tabela_Professor(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeProfessor  = self.linenomeProfessor.text()
        matricula = int(self.lineMatricula.text())

        if(nomeProfessor != '' and matricula != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, matricula, nomeProfessor) == 0:
                query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (
                table_name, nomeProfessor, matricula)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                self.popularTabela(db, "Professor")

    def remover_item_Tabela_Professor(self, db, table_name):
        index = self.tableProfessor.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableProfessor.item(row,0)

        id = int(item.text())

        if self.check_if_exists_in_another_table(id) == 0:
            query = "DELETE FROM %s WHERE idProfessor = %d" % (table_name, id)
            db.cur.execute(query)
            db.db.commit()
            self.popularTabela(db, "Professor")
        else:
            erro = QMessageBox()
            erro.setText("Professor presente na tabela Turma!")
            erro.exec()


    def editar_item_Tabela_Professor(self, db, table_name):
        index = self.tableProfessor.currentIndex()
        row = index.row()
        column = index.column()

        idProfessor = int(self.tableProfessor.item(row,0).text())
        nomeProfessor = str(self.tableProfessor.item(row,1).text())
        matricula = str(self.tableProfessor.item(row,2).text())

        query = "UPDATE %s SET nomeProfessor = '%s', matricula = '%s ' WHERE idProfessor = %d" % (table_name, nomeProfessor, matricula, idProfessor)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Professor")

    def buscar_item_Tabela_Professors(self, db, table_name):
        text = self.lineBusca.text()
        query = "SELECT * FROM {0} WHERE {1} LIKE '{2}%' OR {3} LIKE '{2}%' OR {4} LIKE '{2}%'".format(table_name, "idProfessor", text, "nomeProfessor", "matricula")
        num_rows = db.cur.execute(query)
        result = db.cur.fetchall()

        self.tableProfessor.setRowCount(num_rows)
        for i, row in enumerate(result):
            idProfessor = row["idProfessor"]
            nomeProfessor = row["nomeProfessor"]
            matricula = row["matricula"]
            self.tableProfessor.setItem(i, 0, QTableWidgetItem(str(idProfessor)))
            self.tableProfessor.setItem(i, 1, QTableWidgetItem(str(nomeProfessor)))
            self.tableProfessor.setItem(i, 2, QTableWidgetItem(str(matricula)))

