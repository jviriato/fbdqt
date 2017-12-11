from PyQt5.QtWidgets import *
from view.curso import Ui_curso
from main import *
class Curso(QMainWindow, Ui_curso):
    def __init__(self):
        super(Curso, self).__init__()
        self.setupUi(self)
        header = self.tableCurso.setColumnWidth(1, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Cursos(db, "Curso"));
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Cursos(db, "Curso"));
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Cursos(db, "Curso"));

    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableCurso.setRowCount(num_rows)
        query = "SELECT idCurso, nomeCurso, siglaCurso FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idCurso = row["idCurso"]
            nomeCurso = row["nomeCurso"]
            siglaCurso = row["siglaCurso"]
            self.tableCurso.setItem(i, 0, QTableWidgetItem(str(idCurso)))
            self.tableCurso.setItem(i, 1, QTableWidgetItem(str(nomeCurso)))
            self.tableCurso.setItem(i, 2, QTableWidgetItem(str(siglaCurso)))

    def check_if_exists_in_db(self, result, siglaCurso, nomeCurso):
        for i, entry in enumerate(result):
            if siglaCurso == entry['siglaCurso']:
                print("Essa sigla já existe!")
                return 1
            elif nomeCurso == entry['nomeCurso']:
                print("Esse curso já existe!")
                return 1
        return 0

    def adicionar_item_Tabela_Cursos(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeCurso  = self.linenomeCurso.text()
        siglaCurso = self.lineSiglaCurso.text()

        if(nomeCurso != '' and siglaCurso != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, siglaCurso, nomeCurso) == 0:
                query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (
                table_name, nomeCurso, siglaCurso)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                self.popularTabela(db, "Curso")

    def remover_item_Tabela_Cursos(self, db, table_name):
        index = self.tableCurso.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableCurso.item(row,0)

        id = int(item.text())

        query = "DELETE FROM %s WHERE idCurso = %d" % (table_name, id)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Curso")

    def editar_item_Tabela_Cursos(self, db, table_name):
        index = self.tableCurso.currentIndex()
        row = index.row()
        column = index.column()

        idCurso = int(self.tableCurso.item(row,0).text())
        nomeCurso = str(self.tableCurso.item(row,1).text())
        siglaCurso = str(self.tableCurso.item(row,2).text())

        query = "UPDATE %s SET nomeCurso = '%s', siglaCurso = '%s ' WHERE idCurso = %d" % (table_name, nomeCurso, siglaCurso, idCurso)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "Curso")


